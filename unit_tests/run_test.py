#! TEST REST ENDPOINTS
import pytest
import requests

api_base_url = 'http://localhost:5000'

def create_delete_customer(customer):
	post 			= requests.post(api_base_url + '/customer/details', json=customer)
	res_json 		= post.json()
	new_customer_id = str(res_json['data']['id'])
	delete  		= requests.delete(api_base_url + '/customer/details/' + new_customer_id) 
	if post.status_code == 202 and delete.status_code == 202:
		return post.status_code
	else:
		return 500

def test_create_delete_customer():
	customer = {"name": "Unit Test","email" : "unit@test.com"}
	assert create_delete_customer(customer) == 202


def create_update_delete_budget_item(customer):
	res_codes = []
	post_customer 			= requests.post(api_base_url + '/customer/details', json=customer)
	res_codes.append(post_customer.status_code)

	res_json 				= post_customer.json()
	new_customer_id 		= res_json['data']['id']
	budget_item 			= [{ "name":"TEST ITEM", "amount": 22356.57, "customer_id" : new_customer_id }]
	post_budget_item 		= requests.post(api_base_url + '/budget/details', json=budget_item)
	res_codes.append(post_budget_item.status_code)

	res_json 				= post_budget_item.json()
	new_budget_item_id 		= res_json['data'][0]['id']
	update_item 			= res_json['data'][0]['name'] = 'TEST ITEM UPDATED'
	update_budget_item  	= requests.put(api_base_url + '/budget/details', json=res_json['data']) 
	res_codes.append(update_budget_item.status_code)

	delete_budget_item  	= requests.delete(api_base_url + '/budget/details/' + str(new_budget_item_id)) 
	res_codes.append(delete_budget_item.status_code)

	delete_customer  		= requests.delete(api_base_url + '/customer/details/' + str(new_customer_id))
	res_codes.append(delete_customer.status_code)
	for x in res_codes:
		if x != 202:
			return False

	return 202

def test_create_update_delete_budget_item():
	customer = {"name": "Unit Test","email" : "unit@test.com"}
	assert create_update_delete_budget_item(customer) == 202