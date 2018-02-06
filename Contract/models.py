from django.db import models
from Order.models import Order
import json


class Contract(models.Model):
    def __init__(self, clause, *args, **kwargs):
        super(Contract, self).__init__(*args, **kwargs)
        self.clause = clause
        self.save()

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='order'
    )

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
        return json.loads(self._clause)

    @clause.setter
    def clause(self, value):
        self._clause = json.dumps(value)

    def add_step_clause(self, step, fee):
        clause = self.clause
        clause['clauses'][step] = {'fee': fee, 'data': []}
        self.clause = clause
        pass

    def add_clause(self, step, content):
        self.reset_agreement()
        clause = self.clause
        if step not in clause['clauses']:
            return False
        clause['clauses'][step]['data'].add({'id': clause['max_id'], 'content': content})
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
            clause['clauses'][step]['data'].pop(clause['clauses'][step]['data'].find(target))
        self.clause = clause
        self.save()
        return True

    def reset_agreement(self):
        self.buyer_agreement = False
        self.seller_agreement = False
        self.save()
