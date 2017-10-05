from django.conf.urls import url
from Project import views

urlpatterns = [

		url(r'^$', views.frontpage, name = 'frontpage'),
		url(r'^home/$', views.index, name = 'index'),
		url(r'^login/$', views.login, name = 'login'),
		url(r'^register/$', views.register, name = 'register'),
		url(r'^home/checkout/$', views.checkout, name = 'checkout'),
		url(r'^home/updateReservation/$', views.update, name = 'update'),
		url(r'^home/done/$', views.payment_done, name = 'payment_done'),
		url(r'^home/cancelled/$', views.payment_cancelled, name = 'payment_cancelled'),
		url(r'^home/process/$', views.payment_process, name = 'payment_process'),
		url(r'^home/cancelreservation/$', views.CancelReservation, name = 'CancelReservation'),
		url(r'^home/editprofile/$', views.editprofile, name = 'editprofile'),
		url(r'^termsofservice/$', views.termsofservice, name = 'termsofservice'),
		url(r'^privacy/$', views.privacy, name = 'privacy')
	
		#FOR REST_API
		url(r'^account/$', views.Account_list),
		url(r'^account/(?P<pk>[0-9]/$)',views.Account_detail),
		url(r'^parkinglot/$', views.ParkingLot_list),
		url(r'^parkinglot/(?P<pk>[0-9]/$)',views.ParkingLot_detail),
		url(r'^reserveparking/$', views.ReserveParking_list),
		url(r'^reserveparking/(?P<pk>[0-9]/$)',views.ReserveParking_detail),
		url(r'^checkoutticket/$', views.CheckoutTicket_list),
		url(r'^checkoutticket/(?P<pk>[0-9]/$)',views.CheckoutTicket_detail),
		url(r'^reservationfee/$', views.ReservationFee_list),
		url(r'^reservationfee/(?P<pk>[0-9]/$)',views.ReservationFee_detail),
		url(r'^transactionhistory/$', views.TransactionHistory_list),
		url(r'^transactionhistory/(?P<pk>[0-9]/$)',views.TransactionHistory_detail)
		# url(r'^home/(?P<pk>\d+)$', views.profile(model = Account) )


]
