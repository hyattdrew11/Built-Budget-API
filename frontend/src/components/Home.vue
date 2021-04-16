<template>
  <div class="home">
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand href="#">Get Built</b-navbar-brand>
    </b-navbar>
    <b-container fluid class="mt-3">
      <b-row>
        <b-col md="12">
          <b-card>
            <b-row>
              <b-col md="4">
                <label>Select Customer</label>
                <b-form-select v-model="customer" size="sm" class="mt-3" @change="getBudgetItems(customer.id)">
                  <option v-for="(option, index) in customers" 
                    :key="index"
                    :value="option"
                    >
                    {{ option.name }}
                  </option>
                </b-form-select>
              </b-col>
            </b-row>
            <hr />
            <div v-if="budgetItems.length > 0">
              <b-table striped bordered small hover :items="budgetItems"></b-table>
            </div>
            <div v-else>No budget items</div>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>

const axios = require('axios');
const apiURL = 'http://localhost:5000'
export default {
  name: 'Home',
  data() {
      return {
        customer: null,
        customers: [],
        budgetItems: []
      }
    },
    mounted() {
      this.getCustomers()
    },
    methods: {
      getCustomers() {
        axios.get( apiURL + '/customers')
           .then(({ data }) => { 
            this.customers = data
            this.customer = data[0]
            this.getBudgetItems(this.customer.id)
          })
          .catch(error => {
            console.log(error)
          })

      },
      getBudgetItems(customerID){
        axios.get(apiURL + '/budget/details/' + customerID)
           .then(({ data }) => { 
            this.budgetItems = data.data

          })
          .catch(error => {
            console.log(error)
          })

      }
    }
}
</script>

<style scoped lang="scss"></style>
