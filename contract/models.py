from django.db import models
import ujson


class ContractManager(models.Manager):
    def create_contract(self, clause=None, **kwargs):
        contract = self.model(**kwargs)
        if clause:
            contract.clause = clause
        contract.save()
        return contract


class Contract(models.Model):
    objects = ContractManager()

    buyer_agreement = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    seller_agreement = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    _clause = models.TextField(
        blank=False,
        null=False,
        default='{"max_id": 1, "clauses": {}}'
    )

    buyer_signature = models.TextField(
        blank=True,
        null=True
    )

    seller_signature = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def clause(self):
        return ujson.loads(self._clause)

    @clause.setter
    def clause(self, value):
        self._clause = ujson.dumps(value)

    def add_step_clause(self, step, fee):
        step = str(step)
        # json.dumps will convert dictionary key to string, so that we need to save key as string
        clause = self.clause
        if step in clause['clauses']:
            return False
        clause['clauses'][step] = {'fee': fee, 'data': []}
        self.clause = clause
        self.save()
        return True

    def add_clause(self, step, content):
        step = str(step)
        clause = self.clause
        if step not in clause['clauses']:
            return False
        clause['clauses'][step]['data'].append({'id': clause['max_id'], 'content': content})
        clause['max_id'] += 1
        self.clause = clause
        self.save()
        return True

    def del_clause(self, index):
        self.reset_agreement()
        clause = self.clause
        for step in clause['clauses']:
            search = list(filter(lambda item: item['id'] == index, clause['clauses'][step]['data']))
            if len(search) != 1:
                continue
            target = search[0]
            clause['clauses'][step]['data'].pop(clause['clauses'][step]['data'].index(target))
            self.clause = clause
            self.save()
            return True
        return False

    def reset_agreement(self):
        self.buyer_agreement = False
        self.seller_agreement = False
        self.save()
        return True
