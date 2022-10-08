from django.urls import path

from bank_store.views import deleteBranches,insert, getBanks, getBranches, ifsc, index,branchesData,deleteBanks, insertBanks, insertBranches, insertBranches10, insertBranches11, insertBranches12, insertBranches13, insertBranches14, insertBranches15, insertBranches2, insertBranches5, insertBranches6, insertBranches7, insertBranches8, insertBranches9
from bank_store.views import insertBranches2,insertBranches3,insertBranches4
urlpatterns = [
	#Leave as empty string for base url
	path('', index, name="home"),

	
	path('ifsc/',ifsc),
	path('branches_data/',branchesData),



	path('insert_data/',insert),
	path('insert_banks',insertBanks),
	path('insert_branches/',insertBranches),
	path('insert_branches2/',insertBranches2),
	path('insert_branches3/',insertBranches3),
	path('insert_branches4/',insertBranches4),
	path('insert_branches5/',insertBranches5),
	path('insert_branches6/',insertBranches6),
	path('insert_branches7/',insertBranches7),

	path('insert_branches8/',insertBranches8),
	path('insert_branches9/',insertBranches9),
	path('insert_branches10/',insertBranches10),
	path('insert_branches11/',insertBranches11),
	path('insert_branches12/',insertBranches12),
	path('insert_branches13/',insertBranches13),
	path('insert_branches14/',insertBranches14),
	path('insert_branches15/',insertBranches15),


	path('delete_banks/',deleteBanks),
	path('delete_branches/',deleteBranches),

	path('get_banks',getBanks),
	path('get_branches',getBranches),



]

"""
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

"""