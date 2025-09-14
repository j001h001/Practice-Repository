##Method 1 for creating a target_constructor function
'''
def create_container(container_type):
    elif container_type == 'list':
        return []
    elif container_type == 'dict':
        return {}
    elif container_type == 'set':
        return set()
    elif container_type == 'tuple':
        return tuple()

assert create_container('list') == []
assert create_container('dict') == {}
assert create_container('set') == set()
assert create_container('tuple') == tuple()
'''

##Method 2 for creating a target_constructor function 
##This one is a little nicer looking
"""This is a scratch paper file for testing code snippets and ideas.
def create_container(container_type): 
    constructors = {'list': list, 'dict': dict, 'set': set, 'tuple': tuple}
    
    return constructors[container_type]()

assert create_container('list') == []
assert create_container('dict') == {}
assert create_container('set') == set()
assert create_container('tuple') == tuple()
"""
'''
## This is task 2 for checking the container to determine what type it is
## the second part is to return relevant information about item being called
def access_item(item, container):
    if type(container) == list:
        return container[item]
    elif type(container) == dict:
        return container[item]
    elif type(container) == set:
        if item in container:
            return True
        else:
            return False
    elif type(container) == tuple:
        return container[item]
    else:
        print("sorry the program broke")

assert access_item(2, [1, 2, 3, 4]) == 3 
container = {1: 'a', 3: 'c', 4: 'd'}
assert access_item(3, container) == 'c'
assert access_item(2, {1, 2, 3, 4}) == True
assert access_item(5, {1, 2, 3, 4}) == False
assert access_item(2, (1, 2, 3, 4)) == 3
'''
'''
##Another approach to task 2
def access_item(item, container):
    """
    Retrieves an item from a container (list, tuple, dict) by index/key,
    or checks for its presence in a set.
    """
    # First, we simplify the logic for sets. The expression `item in container`
    # already returns True or False, so we can use it directly.
    if isinstance(container, set):
        return item in container

    # For lists, tuples, and dictionaries, the access syntax is the same:
    # container[item]. So we can just try to do that.
    # This is more flexible than checking for each type individually.
    try:
        return container[item]
    except (KeyError, IndexError):
        # This is good practice for handling cases where the key/index
        # doesn't exist, though not required by the original problem.
        # For this problem, we can assume the inputs are always valid.
        print(f"Error: The item '{item}' was not found in the container.")
        return None
    except TypeError:
        # This will catch other types that don't support indexing,
        # but our `isinstance` check for `set` already handles that.
        print(f"Error: The container of type {type(container).__name__} does not support item access.")
        return None
'''
'''
container = [1, 2, 3, 4, 5]
def add_item(item, container, position=None):
    if type(container) == list:
        if position is None:
            container.append(item)
            return container
        else:
            container.insert(position, item)
            return container
    elif type(container) == dict:
        if type(item) == tuple:
            container[item[0]] = item[1]
            return container
        else:
            container[item] = None
            return container
    elif type(container) == tuple:
        if position is not None:
            tuple1 = container[: position]
            tuple2 = container[position :]
            tuple_container = tuple1 + (item,) + tuple2
            return tuple_container
        else:
            new_container = container + (item,)
            return new_container
    elif type(container) == set:
        container.add(item)
        return container

assert add_item(5, [1, 2, 3, 4]) == [1, 2, 3, 4, 5]
assert add_item('c', ['a', 'b', 'd', 'e'], 2) == ['a', 'b', 'c', 'd', 'e']
'''

##Step 4: Implementing the remove_item function
'''
Next, you are going to implement the remove_item function that removes an item from any basic Python container (list, set, tuple, dict). The function has the following parameters:
item: The object to be removed from the container.
container: The container from which the item is removed (list, set, tuple, dict).
multi: The bool specifier indicating if only the first occurrence of the item should be removed (False) or all of them (True). This parameter has a default value set to True.
The function returns the updated container (or its copy if necessary).
This is how the remove_item function handles removing an item from the individual container types:

test_list = (7,7,7,7,7,7)
def remove_item(item, container, multi=True):
    if type(container) == list:
        if multi == False:
            container.remove(item)
            return container
        else:
            container = [i for i in container if i != item]
            return container
    elif type(container) == dict:
        del container[item]
        return container
    elif type(container) == set:
        container.remove(item)
        return container
    elif type(container) == tuple:
        container = list(container)
        if multi == False:
            container.remove(item)
            return tuple(container)
        else:
            container = [i for i in container if i != item]
            return tuple(container)
            
print(remove_item(7, test_list, multi=True))
'''
'''
#Step 5: Implementing the update_item function
def update_item(orig_item, new_item, container,multi=True):
    if type(container) == list:
        if orig_item in container:
            if multi == False:
                index = container.index(orig_item)
                container[index] = new_item
                return container
            else:
                container = [new_item if i == orig_item else i for i in container]
                return container
        else:
            print("Item not found in list.")
            return container
    elif type(container) == dict:
        if orig_item in container:
            if type(new_item) == tuple:
                container[new_item[0]] = new_item[1]
                del container[orig_item]
                return container
            else:
                container[orig_item] = new_item
                return container
        else:
            print("Key not found in dictionary.")
            return container
    elif type(container) == set:
        if orig_item in container:
            container.remove(orig_item)
            container.add(new_item)
            return container
        else:
            print("Item not found in set.")
            return container
    elif type(container) == tuple:
        if orig_item in container:
            container = list(container)
            if multi == False:
                index = container.index(orig_item)
                container[index] = new_item
                return tuple(container)
            else:
                container = [new_item if i == orig_item else i for i in container]
                return tuple(container)
        else:
            print("Item not found in tuple.")
            return container
'''        

#Step 6: Implementing the convert_container function
'''Finally, you are going to implement the convert_container function that transforms any basic Python container (list, set, tuple, dict) to any of the basic container types. The function has the following parameters:
container: The original container (list, set, tuple, dict) that is to be transformed to a new type.
container_type: The str indicator of the type to which the container should be transformed ('list', 'set', 'tuple', 'dict').
The function returns the new container transformed to a new type (container_type).
Alternatively, if container's type matches that described by container_type, it returns the original, unmodified container.
This is how the convert_container function handles transforming container to a new container_type for the individual container types:'''
'''
def convert_container(container, container_type):
    container_type = str(container_type)
    if type(container).__name__ == container_type:
        return container    
    
## Constructing the check for list container and converting it to the relevant container type
    if isinstance(container, list):
        if container_type == 'dict':
            new_container = {}
            for i in container:
                if type(i) == tuple and len(i) == 2:
                    new_container[i[0]] = i[1]
                else:
                    new_container[i] = None
            return new_container
        elif container_type == 'tuple':
            return tuple(container)   
        elif container_type == 'set':
            new_container = set()
            for i in container:
                new_container.add(i)
        return new_container
    else:
        ("There has been an error in the program, please try again. \n This is the error msg from the if container == list argument")

## Constructing the check for dict container and converting it to the relevant container type            
    if isinstance(container, dict):
        if container_type == 'list':
            return list(container.items())
        elif container_type == 'set':
            return set(container.items())
        elif container_type == 'tuple':
            return tuple(container.items())
        else:
            ("There has been an error in the program, please try again. \n This is the error msg from the if container == dict argument")

## Constructing the check for set container and converting it to the relevant container type 
    if isinstance(container, set):
        if container_type == 'list':
            return list(container)
        elif container_type == 'dict':
            new_container = {}
            for i in container:
                if type(i) == tuple and len(i) == 2:
                    new_container[i[0]] = i[1]
                else:
                    new_container[i] = None
            return new_container                    
        elif container_type == 'tuple':
            return tuple(container)
        else:
            ("There has been an error in the program, please try again. \n This is the error msg from the if container == set argument")

## Constructing the check for tuple container and converting it to the relevant container type 
    if isinstance(container, tuple):
        if container_type == 'list':
            return list(container)
        elif container_type == 'dict':
            new_container = {}
            for i in container:
                if type(i) == tuple and len(i) == 2:
                    new_container[i[0]] = i[1]
                else:
                    new_container[i] = None
            return new_container 
        elif container_type == 'set':
            return set(container)
        else:
            ("There has been an error in the program, please try again. \n This is the error msg from the if container == tuple argument")
'''
'''
def convert_container(container, container_type):
    """
    Transforms a Python container to a specified new type.
    """
    # Step 1: Handle the "do nothing" case.
    # This check is clean and efficient at the top.
    if type(container).__name__ == container_type:
        return container

    # Step 2: Handle the complex "to dictionary" conversions.
    # This logic is the most complex, so we can handle it in its own section.
    if container_type == 'dict':
        new_dict = {}
        for item in container:
            # Check if the item is a 2-element tuple for key-value pairing
            if isinstance(item, tuple) and len(item) == 2:
                new_dict[item[0]] = item[1]
            # Otherwise, use the item as a key with a value of None
            else:
                new_dict[item] = None
        return new_dict

    # Step 3: Handle conversions FROM a dictionary.
    # These all use the .items() method to get (key, value) pairs.
    if isinstance(container, dict):
        if container_type == 'list':
            return list(container.items())
        if container_type == 'set':
            return set(container.items())
        if container_type == 'tuple':
            return tuple(container.items())

    # Step 4: Handle all other standard conversions.
    # These are simple cases where the built-in constructors work directly.
    # This block handles list->set, list->tuple, set->list, set->tuple,
    # tuple->list, and tuple->set.
    if container_type == 'list':
        return list(container)
    if container_type == 'set':
        return set(container)
    if container_type == 'tuple':
        return tuple(container)

# You can add all the original assert statements here to test it.
# For example:
assert convert_container([1, (2, 'a')], 'dict') == {1: None, 2: 'a'}
assert sorted(convert_container({1: 'a'}, 'list')) == [(1, 'a')]
assert convert_container((1, 2, 3), 'set') == {1, 2, 3}

print("All sample assertions passed successfully!")
'''

##This is the cleaner version from Gemini
def convert_container(container, container_type):
    """
    Transforms a Python container to a specified new type.
    """
    # Step 1: Handle the "do nothing" case.
    # This check is clean and efficient at the top.
    if type(container).__name__ == container_type:
        return container

    # Step 2: Handle the complex "to dictionary" conversions.
    # This logic is the most complex, so we can handle it in its own section.
    if container_type == 'dict':
        new_dict = {}
        for item in container:
            # Check if the item is a 2-element tuple for key-value pairing
            if isinstance(item, tuple) and len(item) == 2:
                new_dict[item[0]] = item[1]
            # Otherwise, use the item as a key with a value of None
            else:
                new_dict[item] = None
        return new_dict

    # Step 3: Handle conversions FROM a dictionary.
    # These all use the .items() method to get (key, value) pairs.
    if isinstance(container, dict):
        if container_type == 'list':
            return list(container.items())
        if container_type == 'set':
            return set(container.items())
        if container_type == 'tuple':
            return tuple(container.items())

    # Step 4: Handle all other standard conversions.
    # These are simple cases where the built-in constructors work directly.
    # This block handles list->set, list->tuple, set->list, set->tuple,
    # tuple->list, and tuple->set.
    if container_type == 'list':
        return list(container)
    if container_type == 'set':
        return set(container)
    if container_type == 'tuple':
        return tuple(container)

# You can add all the original assert statements here to test it.
# For example:
assert convert_container([1, (2, 'a')], 'dict') == {1: None, 2: 'a'}
assert sorted(convert_container({1: 'a'}, 'list')) == [(1, 'a')]
assert convert_container((1, 2, 3), 'set') == {1, 2, 3}

print("All sample assertions passed successfully!")