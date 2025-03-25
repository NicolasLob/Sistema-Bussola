<template>
    <div class="container">
      <h1>Listagem de Aprendizagem</h1>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>CD_DOCUMENTO</th>
              <th>CD_AVALIACAO</th> 
              <th>DC_TECNOLOGIA_PUBLICACAO</th>
              <th>FL_EXTRA</th>
              <th>CD_PAIS</th>
              <th>NM_PAIS</th>
              <th>CD_ESTADO</th>
              <th>NM_ESTADO</th>
              <th>CD_REGIONAL</th>
              <th>NM_REGIONAL</th>
              <th>CD_MUNICIPIO</th>
              <th>NM_MUNICIPIO</th>
              <th>CD_ESCOLA</th>
              <th>NM_ESCOLA</th>
              <th>CD_LOCALIZACAO</th>
              <th>DC_LOCALIZACAO</th>
              <th>CD_TURMA</th>
              <th>CD_TURMA_INSTITUCIONAL</th>
              <th>NM_TURMA</th>
              <th>CD_TURNO</th>
              <th>DC_TURNO</th>
              <th>CD_REDE</th>
              <th>DC_REDE</th>
              <th>CD_ALUNO</th>
              <th>CD_ALUNO_INSTITUCIONAL</th>
              <th>CD_ALUNO_INEP</th>
              <th>NM_ALUNO</th>
              <th>CD_ALUNO_NEC_ESPECIAL</th>
              <th>DC_ALUNO_NEC_ESPECIAL</th>
              <th>DC_CADERNO</th>
              <th>CD_INSTRUMENTO_CAED</th>
              <th>CD_DISCIPLINA</th>
              <th>NM_DISCIPLINA</th>
              <th>CD_ETAPA_APLICACAO</th>
              <th>DC_ETAPA_APLICACAO</th>
              <th>CD_ETAPA_AVALIADA</th>
              <th>DC_ETAPA_AVALIADA</th>
              <th>CD_ENSINO</th>
              <th>DC_ENSINO</th>
              <th>FL_PREVISTO</th>
              <th>FL_AVALIADO</th>
              <th>DC_RESPOSTA</th>
              <th>NU_RESPOSTA</th>
              <th>NU_ACERTO</th>
              <th>NU_TOTAL</th>
              <th>TX_ACERTO</th>
              <th>VL_PROFICIENCIA</th>
              <th>VL_PROFICIENCIA_ERRO</th>
              <th>DC_PADRAO_DESEMPENHO</th>
              <th>CD_HABILIDADE</th>
              <th>NM_HABILIDADE</th>
              <th>DC_HABILIDADE_ACERTO</th>
              <th>DC_HABILIDADE_TOTAL</th>
              <th>RP_COMPONENTE_CURRICULAR</th>
              <th>RP_GABARITO</th>
              <th>DC_ITENS</th>
              <th>NM_HABILIDADE_POR_ITEM</th>
              <th>DC_ITENS_ACERTO</th>
              <th>CD_GRUPO</th>
              <th>NM_GRUPO</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in dados" :key="item.CD_ALUNO">
              <td v-for="(value, key) in item" :key="key">{{ value }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      dados: [],
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:8001/api/aprendizagem/');
        this.dados = response.data;
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  padding: 20px;
  background-color: #1b1f3b;
  color: white;
  text-align: center;
  border-radius: 10px;
}

h1 {
  color: #dbeafe;
  margin-bottom: 20px;
}

.table-container {
  overflow-x: auto;
  border-radius: 8px;
  box-shadow: 0px 4px 6px rgba(15, 15, 15, 0.1);
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: #243c5a;
  color: white;
}

th, td {
  border: 1px solid #4a6fa5;
  padding: 12px;
  text-align: left;
  white-space: nowrap;
}

th {
  background-color: #162447;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #30475e; 
}

tr:hover {
  background-color: #526d82;
}
</style>