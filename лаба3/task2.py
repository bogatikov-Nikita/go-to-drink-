
def find_common_participants(group1, group2, delimiter=","):
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)
    common = set(list1) & set(list2)
    return sorted(common)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")

# Проверка с другим разделителем
result = find_common_participants("Иванов;Петров;Сидоров", "Петров;Сидоров;Смирнов", ";")
print(result)