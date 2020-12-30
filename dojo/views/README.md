<h1 align="center"> DJANGO VIEWS  NOTES </h1>

### FUNCTION BASED :
 ```python
def example (request):
    context = {
        "items": db_item.objects.all(),
    }
    return render(request,"example.html",context)
```
###CLASS BASED 

####Generic 
pre written built-in views 
* TemplateView
<br>
  in app/urls.py:
  ```python
    urlpatterns = [ 
        path('ex1', TemplateView.as_view(template_name="ex1.html",
                                     extra_context={'title': 'Custom Title'})),
    ]
  ```
