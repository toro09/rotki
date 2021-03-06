<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-row>
          <v-col cols="12">
            <h1 class="page-header">Import Data</h1>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            You can manually import data from the services below by clicking on
            the respective logo
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <h3>Cointracking.info</h3>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            Important notes for importing data from cointracking's CSV exports.
            <ul>
              <li>
                They change their format in a backwards incompatible way quite
                often. As such this import may stop working. If that happens
                open an issue with rotki and we will see what we can do.
              </li>
              <li>
                Trades/deposits/withdrawals from Cointracking do not include
                fees.
              </li>
              <li>
                All trades imported from Cointracking will always be considered
                as buys due to the way the data are represented.
              </li>
              <li>
                ETH/BTC Transactions are treated as deposits/withdrawals so they
                are not imported in Rotkehlchen. To import ETH transactions
                simply input your accounts in
                <router-link to="/accounts-balance">
                  Blockchain Accounts/Balances
                </router-link>
                and they will be imported automatically for you.
              </li>
            </ul>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            For the above reasons it's preferred to directly connect your
            exchanges in order to import data from there. If you do not do that
            a lot of accuracy is lost.
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-img
              max-width="200"
              class="import-data__cointracking-info elevation-1"
              :src="require('../assets/images/cointracking_info.png')"
              @click="coinTrackingInfoImport()"
            ></v-img>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Message } from '@/store/store';

@Component({})
export default class ImportData extends Vue {
  async coinTrackingInfoImport() {
    try {
      const file = await this.$interop.openFile('Select a file');
      if (!file) {
        return;
      }
      await this.$api.importDataFrom('cointracking.info', file);
      this.$store.commit('setMessage', {
        success: true,
        title: 'Import successful',
        description:
          'Data imported from cointracking.info export file successfully'
      } as Message);
    } catch (e) {
      this.$store.commit('setMessage', {
        title: 'Import failed',
        description: e.message
      } as Message);
    }
  }
}
</script>

<style scoped></style>
