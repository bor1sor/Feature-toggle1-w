const request = require('supertest')
const agent = request('https://reqres.in/api')


describe("Тест 2 - ну что-нибудь посложнее", function () {
    it("Тест 2.1", function (done) {
        agent
            .get('/user')
            .expect('Content-Type', /json/)
            .expect(200, done)
    })
})