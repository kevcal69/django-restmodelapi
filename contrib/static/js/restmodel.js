var RestModel = new function(app, namespace) {
    this.app = app;
    this.namespace = namespace;
}

var RestModel =  (function () {

    // Constructor
    function RestModel(app, namespace) {
        this.app = app;
        this.namespace = namespace;
    }

    function querysetBuilder(data) {
        var query = [];

        for (var key in p) {
            if (p.hasOwnProperty(key)) {
                query.push(key + '=' + p[key]);
            }
        }

        return query.join('&')
    }

    function requestAjax(data) {
        return new Promise(function(resolve, reject) {
            var query_set = '?' + querysetBuilder(data);
            var request = new XMLHttpRequest();
            request.open('GET', '/resource/get/' + query_set, true);

            request.onload = function() {
                if (request.status >= 200 && request.status < 400) {
                    // Success! return promise
                    var resp = JSON.parse(request.responseText);
                    resolve(resp)
                } else {
                    // Error! return promise
                    reject();
                }
            };

            request.onerror = function() {
                reject();
            };

            request.send();
        });
    }


    RestModel.prototype.objects = {

        filter: function(filter) {
            return requestAjax({
                    app: this.app,
                    namespace: this.namespace,
                    filter JSON.stringify(filter)
                }
            );
        }
    }

    return RestModel;
})();
