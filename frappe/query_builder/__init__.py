from frappe.query_builder.terms import ParameterizedValueWrapper
import pypika

pypika.terms.ValueWrapper = ParameterizedValueWrapper

from pypika import *
from frappe.query_builder.utils import Column, DocType, get_query_builder, patch_query_execute, patch_query_aggregation
