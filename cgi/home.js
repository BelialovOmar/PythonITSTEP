﻿﻿document.addEventListener('DOMContentLoaded',() => {
    const authButton = document.getElementById('auth-button');
    // if(authButton) authButton.addEventListener('click', authButtonClick );
    
    const infoButton = document.getElementById('info-button');
    if(infoButton) infoButton.addEventListener('click', infoButtonClick );
    
    const productButton = document.getElementById('product-button');
    if(productButton) productButton.addEventListener('click', productButtonClick );
});

function authButtonClick() {
    const userLogin = document.getElementById('user-login').value;
    const userPassword = document.getElementById('user-password').value;
    const credentials = btoa(`${userLogin}:${userPassword}`);
    
    fetch('/auth', {
        headers: {
            'Authorization': `Basic ${credentials}`,
        }
    })
    .then(response => {
        if (!response.ok) throw new Error('Authentication failed');
        return response.json();
    })
    .then(data => {
        document.getElementById('user-token').value = data.token;
    })
    .catch(error => {
        console.error(error);
        document.getElementById('user-token').value = '';
        alert('Authentication failed');
    });
}

function infoButtonClick() {
    const userToken = document.getElementById('user-token').value;
    if (!userToken) {
        alert('No token provided');
        return;
    }

    fetch(`/auth`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${userToken}`,
            'Content-Type': 'application/json'
        }    })
    .then(response => {
        if (!response.ok) throw new Error('Token validation failed');
        return response.json();
    })
    .then(console.log)
    .catch(error => {
        console.error(error);
        document.getElementById('user-token').value = '';
        alert('Token validation failed');
    });
}

function productButtonClick() {
    fetch("/product", {
        method: "POST",
        body: JSON.stringify( {
            name:  document.getElementById("product-name" ).value,
            price: document.getElementById("product-price").value,
            image: document.getElementById("product-image").value
        } )
    }).then(r => r.json()).then(console.log);
}

angular
.module('app', [])
.directive('products', function() {
    return {
      restrict: 'E',
      transclude: true,
      scope: {},
      controller: function($scope, $http) {
        $scope.authToken = "";
        $scope.userLogin = "user";
        $scope.userPassword = "123";
        $scope.products = [];
        $http.get('/product')
        .then( r => $scope.products = r.data.data );

        $scope.addCartClick = (id) => {
            $http({
                url: '/cart',
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${$scope.authToken}`,
                },
                data:  { 'id_product': id } 
            }).then( r => console.log(r) );
            // console.log('cart ' + id + ' ' + $scope.authToken);
        }
        $scope.authClick = () => {
            // console.log($scope.userLogin + ' ' + $scope.userPassword);
            const credentials = btoa( `${$scope.userLogin}:${$scope.userPassword}` )
            $http.get('/auth',{
                headers: {
                    'Authorization': `Basic ${credentials}`,
                }
            }).then( r => $scope.authToken = r.data.token );
        }
      },
      templateUrl: `/tpl/product.html`,
      replace: true
    };
  })