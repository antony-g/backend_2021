# Домашнее задание к лекции №2 (объектная модель, метапрограммирование, память)

## 1. Реализовать класс, отнаследованный от списка
При этом один список:
- Можно вычитать из другого [5, 1, 3, 7] - [1, 2, 7] = [4, -1, -4, 7];
- Можно складывать с другим [5, 1, 3, 7] + [1, 2, 7] = [6, 3, 10, 7];
- Результатом сложения/вычитания должен быть новый кастомный список;
- Сложение/вычитание также должно работать с обычными списками:
    [1, 2] +- CustomList([3, 4]) -> CustomList(...)
    CustomList([3, 4]) +- [1, 2] -> CustomList(...)
- При неравной длине, дополнять меньший список нулями только на время выполнения операции. Исходные списки не должны изменяться;
- При сравнении списков должна сравниваться сумма элементов списков;
- Списки можно считать всегда числовыми;
- На все должны быть тесты в отдельном модуле.

## 2. Написать метакласс, который в начале названий всех атрибутов и методов (кроме магических) добавляет префикс "custom_" (+тесты).
    class CustomMeta():
        pass

    class CustomClass(metaclass=CustomMeta):
        x = 50
    
        def line(self):
            return 100

    inst = CustomClass()
    inst.custom_x
    inst.custom_line()

    inst.x  # ошибка
    inst.line() # ошибка
