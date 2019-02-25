const supertestUnbound = require('supertest')
require('should')

const serverUrl = process.env.SERVER_URL || 'http://localhost:8000'
console.log(`Using server url='${serverUrl}'`)
const supertest = supertestUnbound(serverUrl)
const authKey = process.env.AUTH_KEY || (() => {throw new Error('AUTH_KEY env var must be defined!')})()

describe('the_app tests ::', () => {
  describe('', () => {
    it('should simulate a typical use case', async() => {
      // create a location
      const loc1Id = await supertest
        .post(`/locations/`)
        .set('Authorization', `Bearer ${authKey}`)
        .send({
          name: 'Loc 1',
        })
        .then(res => {
          assertStatus(201, res)
          const location = res.body.location
          location.should.have.property('name')
          return location.id
        })
      // create a group
      const group1Id = await supertest
        .post(`/groups/`)
        .set('Authorization', `Bearer ${authKey}`)
        .send({
          name: 'Group 1',
          location: loc1Id
        })
        .then(res => {
          assertStatus(201, res)
          const group = res.body.group
          group.should.have.property('name')
          return group.id
        })
      // create a user
      const user1Id = await supertest
        .post(`/users/`)
        .set('Authorization', `Bearer ${authKey}`)
        .send({
          first_name: 'User',
          surname: 'One',
          location: loc1Id,
          groups: [group1Id]
        })
        .then(res => {
          assertStatus(201, res)
          const user = res.body.user
          user.should.have.property('first_name')
          return user.id
        })
    })
  })
})

function assertStatus (status, res) {
  res.status.should.eql(status, JSON.stringify(res.body))
}
