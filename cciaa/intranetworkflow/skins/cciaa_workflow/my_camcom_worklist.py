## Script (Python) "my_camcom_worklist"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Lista revisione camerale
##

if context.portal_membership.isAnonymousUser():
    return []

wf_results = list(context.portal_workflow.getWorklistsResults())
wf_results.sort(lambda x, y: cmp(x.modified(), y.modified()))
member = context.portal_membership.getAuthenticatedMember()

# Ulteriore filtro, se sono un caposervizio vedo quelli del capoufficio SOLO se ho un parametro particolare
# Altrimenti ricontrollo tutti gli elementi ed elimino quelli non nello stato giusto

if 'CSer' in member.getRolesInContext(context) and (not context.REQUEST.get('showcuff') or context.REQUEST.get('showcuff')!='y'):
    tmpList = []
    portal_workflow = context.portal_workflow
    for j in wf_results:
        if portal_workflow.getInfoFor(j, 'review_state', '???')=='attesa_cser':
            tmpList.append(j)
    wf_results = tmpList
elif 'CSer' in member.getRolesInContext(context):
    # Sono CSer ma voglio solo i documenti del CUff
    tmpList = []
    portal_workflow = context.portal_workflow
    for j in wf_results:
        if portal_workflow.getInfoFor(j, 'review_state', '???')=='attesa':
            tmpList.append(j)
    wf_results = tmpList
return wf_results