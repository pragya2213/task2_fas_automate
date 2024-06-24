import requests

class TestFakeStoreApiCart:
    def test_get_singlecart_by_cartid(self):
        url = "https://fakestoreapi.com/carts/5"  
        
        #send request
        response = requests.get(url)

        # Verify status code
        assert response.status_code == 200 

        # Verify content-type
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

        # Verify response structure (Assuming a cart with 'id', 'userId', 'date' and 'products') and cart id
        data = response.json()  
        assert isinstance(data, dict)
        assert "id" in data
        assert "userId" in data
        assert "date" in data
        assert "products" in data
        assert data["id"] == 5
 


    def test_get_limited_carts(self):
        url = "https://fakestoreapi.com/carts?limit=5"  
        
        #send request
        response = requests.get(url)

        # Verify status code
        assert response.status_code == 200 

        # Verify content-type
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

        # Verify number of carts returned is 5
        data = response.json()  
        assert len(data) == 5


    def test_get_sorted_carts_desc(self):
        url = "https://fakestoreapi.com/carts?sort=desc"  
        
        #send request
        response = requests.get(url)

        # Verify status code
        assert response.status_code == 200 

        # Verify content-type
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

        # Verify cart ids returned are in descending order
        data = response.json() 
        data_ids = [ sub['id'] for sub in data ]
        assert sorted(data_ids,reverse=True) == data_ids



    
    def test_get_carts_by_userid(self):
        url = "https://fakestoreapi.com/carts/user/2"  
        
        #send request
        response = requests.get(url)

        # Verify status code
        assert response.status_code == 200 

        # Verify content-type
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

        # Verify all carts returned have same userId
        data = response.json()  
        data_user_ids = [ sub['userId'] for sub in data ]
        assert all(i == data_user_ids[0] for i in data_user_ids)

    def test_post_new_cart(self):
        url = "https://fakestoreapi.com/carts"
        requests_data = {
            "userId": 5,
            "date": "2020-02-03",
            "products":[{"productId":5,"quantity":1},{"productId":1,"quantity":5}]
        }
        #send request
        response = requests.post(url, requests_data)
        # Verify status code
        assert response.status_code == 200

        # Verify cart updated has same userId
        data = response.json()  
        assert data['userId'] == '5'
