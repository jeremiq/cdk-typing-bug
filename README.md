# To Reproduce
1. create a clean virtualenv
```shell 
pip install -r requirements.txt
mypy stack_with_type_failures.py
```

Results: 
```shell
stack_with_type_failures.py:11: error: List item 0 has incompatible type "ServicePrincipal"; expected "IPrincipal"
stack_with_type_failures.py:11: note: Following member(s) of "ServicePrincipal" have conflicts:
stack_with_type_failures.py:11: note:     Expected:
stack_with_type_failures.py:11: note:         def __jsii_proxy_class__() -> Type[_IPrincipalProxy]
stack_with_type_failures.py:11: note:     Got:
stack_with_type_failures.py:11: note:         def __jsii_proxy_class__() -> Type[_PrincipalBaseProxy]
stack_with_type_failures.py:18: error: List comprehension has incompatible type List[ArnPrincipal]; expected List[IPrincipal]
stack_with_type_failures.py:18: note: Following member(s) of "ArnPrincipal" have conflicts:
stack_with_type_failures.py:18: note:     Expected:
stack_with_type_failures.py:18: note:         def __jsii_proxy_class__() -> Type[_IPrincipalProxy]
stack_with_type_failures.py:18: note:     Got:
stack_with_type_failures.py:18: note:         def __jsii_proxy_class__() -> Type[_PrincipalBaseProxy]
```

