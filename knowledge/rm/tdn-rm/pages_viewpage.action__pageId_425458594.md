---
content_hash: e6daf0551328b12bb4b620430bddc30db2e9ff3594dbd55786ab191671d6d53f
fetched_at: '2026-06-29T00:09:31.280418+00:00'
page_id: '425458594'
product: rm
source: tdn-rm
title: Folha - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458594
version: 4
---

---

### **Permitir cadastrar professor que não seja funcionário**

Quando este parâmetro está habilitado será permitido cadastro um professor que não seja funcionário do folha de pagamento.

### **Utilizar valor da hora/aula**

Neste parâmetro é definido para o folha de pagamento de onde será buscada a informação do valor da hora/aula do professor, se será do cadastro do professor da turma/disciplina ou se é de acordo com a titulação e a função do professor

### **Origem do centro de custo**

Define de onde o TOTVS Folha de Pagamento irá buscar a informação do centro de custo, se é da turma ou da matriz aplicada da turma. Esta informação é utilizada também pelo TOTVS Automação de Ponto, no momento em que enviado a informação das faltas do professor.

Vale ressaltar que na  o centro de custo por padrão é buscado no  do tipo **plano**ou **serviço**, demais contratos não serão considerados. Caso este centro de custo não esteja preenchido no contrato, o sistema irá buscar na turma ou na matriz aplicada da turma conforme a parametrização escolhida.

### **Origem dados financeiros - integração Protheus (item contábil/classe de valor)**

Quando o TOTVS Educacional está integrado com o BackOffice do Protheus é possível informar ao folha de pagamento de irá buscar: da turma ou da matriz aplicada. Esta informação é utilizada também pelo TOTVS Automação de Ponto, no momento em que enviado a informação das faltas do professor.
