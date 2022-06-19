def queryset_to_dict(queryset):
    dict_c = []
    for item in queryset:
        dict_c.append({
            "id": item.id,
            'name': item.Name,
            'standard': item.Standard, 
            'grade': item.Grade
        })
    return dict_c
    