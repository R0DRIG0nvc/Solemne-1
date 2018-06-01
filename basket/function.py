from django.db.models import Q


def paginationDataTable(POST, Modelo):
    if POST['search[value]'] == '':
        query = Modelo.objects.all()[int(POST['start']):int(POST['start']) + int(POST['length'])]
        json = {"recordsTotal": Modelo.objects.all().count(),
                "recordsFiltered": Modelo.objects.all().count()}
    else:
        query = Modelo.objects.filter(Q(name__icontains=POST['search[value]']) | Q(age__icontains=POST['search[value]']) | Q(email__icontains=POST['search[value]']) | Q(nickname__icontains=POST['search[value]']) | Q(rut__icontains=POST['search[value]']) | Q(dv__icontains=POST['search[value]']))
        json = {"recordsTotal": query.count(),
                "recordsFiltered": query.count()}
    return query, json
