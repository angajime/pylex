# pylex

Fast and simple regex matcher.

# use
```
> python pylex.py input.in
```

### input.in

This must be a file containing a list of regexs and a list of test, formatted like this:
```
^0[0-9]*
[0-9]*0$
%%
0
00
001
1
2
012
210
```

### output

Output is standard console output:

```
^0[0-9]*             0           [PASS] 
^0[0-9]*             00          [PASS] 
^0[0-9]*             001         [PASS] 
^0[0-9]*             1           [FAIL] 
^0[0-9]*             2           [FAIL] 
^0[0-9]*             012         [PASS] 
^0[0-9]*             210         [FAIL] 
[0-9]*0$             0           [PASS] 
[0-9]*0$             00          [PASS] 
[0-9]*0$             001         [FAIL] 
[0-9]*0$             1           [FAIL] 
[0-9]*0$             2           [FAIL] 
[0-9]*0$             012         [FAIL] 
[0-9]*0$             210         [PASS] 
```