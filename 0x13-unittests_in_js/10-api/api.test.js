const { expect } = require('chai');
const request = require('request');
const { spy, stub } = require('sinon');


describe('index page', () => {
  beforeEach(() => {
    this.get = stub(request, 'get');
    this.post = stub(request, 'post');
  });

  afterEach(() => {
    request.get.restore();
    request.post.restore();
  });
  it('error code 404', () => {
    request('http://localhost:7865/cart/hello', function(err, res, body) {
      expect(res.statusCode).to.equal(404);
    });
  });
  it('welcome message', () => {
    request('http://localhost:7865/', function(err, res, body) {
      expect(body).to.equal('Welcome to the payment system');
    });
  });
  it('payment message', () => {
    request('http://localhost:7865/cart/12', function(err, res, body) {
      expect(body).to.equal('Payment methods for cart 12');
    });
  });
  it('api connected', () => {
    request('http://localhost:7865/', function(err, res, body) {
      expect(res.request.method).to.equal('GET');
    });
  });
});
