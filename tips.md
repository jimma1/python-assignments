# Code structure

## Order
* Start with a function named "run" which is called in "main"
* Think of the code as a book where stuff happens in a chronological order
* Make sure a function does one thing, and one thing only.

```python
def run():
    date = _get_date()
    date = do_stuff_with_date(date=date)
    date = do_other_stuff_with_date(date=date)
    show_user_output(date)
```
