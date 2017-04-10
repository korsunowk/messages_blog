from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from mptt.templatetags.mptt_tags import cache_tree_children


register = template.Library()


class RecurseTreeNode(template.Node):
    def __init__(self, template_nodes, queryset_var, order_var=None):
        self.template_nodes = template_nodes
        self.queryset_var = queryset_var
        self.order_var = order_var

    def _render_node(self, context, node):
        bits = []
        context.push()

        children = node.get_children()

        if children and self.order_var is not None:
            children = children.order_by(self.order_var)

        for child in children:
            bits.append(self._render_node(context, child))
        context['node'] = node
        context['children'] = mark_safe(''.join(bits))
        rendered = self.template_nodes.render(context)
        context.pop()
        return rendered

    def render(self, context):
        queryset = self.queryset_var.resolve(context)
        roots = cache_tree_children(queryset)
        bits = [self._render_node(context, node) for node in roots]
        return ''.join(bits)


@register.tag
def recursetree_edited(parser, token):
    bits = token.contents.split()
    if len(bits) < 2:
        raise template.TemplateSyntaxError(_('%s tag requires a queryset') % bits[0])

    queryset_var = template.Variable(bits[1])

    if len(bits) == 3:
        order_var = bits[2]
    else:
        order_var = None

    template_nodes = parser.parse(('endrecursetree_edited',))
    parser.delete_first_token()

    return RecurseTreeNode(template_nodes, queryset_var, order_var)
