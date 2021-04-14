from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Income Expenses API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.test.com/policies/terms/",
      contact=openapi.Contact(email="shivamchouhan728@gmail.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
    path('expense/', include("expense_app.urls")), 
    path('income/', include("income_app.urls")), 
    path('userstats/', include("userstats_app.urls")), 
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
