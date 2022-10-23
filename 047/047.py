def remove_elem(items, elem_to_remove):
    if not items:
        return "Empty List"

    if items.count(elem_to_remove) == 0:
        return "Not Found"

    for i in range(items.count(elem_to_remove)):
        items.remove(elem_to_remove)

    return items


def remove_elem2(items, elem_to_remove):
    if len(items) == 0:
        return "Empty List"

    if not items.count(elem_to_remove):
        return "Not Found"

    items.remove(elem_to_remove)

    if not items.count(elem_to_remove):
        return items

    return remove_elem2(items, elem_to_remove)


if __name__ == "__main__":
    print(remove_elem([1, 2, 3, 4], elem_to_remove=2))
    print(remove_elem2([1, 2, 3, 4], elem_to_remove=2))

    print(remove_elem([3, 3, 2, 1], elem_to_remove=3))
    print(remove_elem2([3, 3, 2, 1], elem_to_remove=3))

    print(remove_elem(["a", "b", "c", "b"], elem_to_remove="b"))
    print(remove_elem2(["a", "b", "c", "b"], elem_to_remove="b"))

    print(remove_elem([3, 4, 5, 6], elem_to_remove=7))
    print(remove_elem2([3, 4, 5, 6], elem_to_remove=7))

    print(remove_elem([], elem_to_remove=0))
    print(remove_elem2([], elem_to_remove=0))
