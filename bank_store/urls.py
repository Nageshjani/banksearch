from django.urls import path

from bank_store.views import ifsc, index,branchesData
urlpatterns = [
	#Leave as empty string for base url
	path('', index, name="home"),
	path('ifsc/',ifsc),
	path('branches_data/',branchesData),
]











