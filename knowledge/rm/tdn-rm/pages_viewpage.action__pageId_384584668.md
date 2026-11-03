---
content_hash: 783e348602434e4f3ac9126122cc9254701c909b91b5a436131f62ed8afbf079
fetched_at: '2026-06-29T00:09:07.638772+00:00'
page_id: '384584668'
product: rm
source: tdn-rm
title: 3333987  DSAUGHFATF-1369  Erro no estorno do repasse (Após mudança de categoria
  do paciente)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384584668
version: 1
---

# 3333987  DSAUGHFATF-1369  Erro no estorno do repasse (Após mudança de categoria do paciente)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Totvs Gestão Hospitalar |
| **Função:** | Mudança de categoria do paciente (para um paciente que tenha um item com repasse na conta) |
| **Situação/Requisito:** | Ao mudar a categoria o sistema estorna os itens da conta que não constam na tabela da nova categoria.  Porém estes itens estornados, quando possuem repasse, não são tirados da folha de pagamento dos prestadores. |
| **Solução/Implementação:** | Quando executar o estorno de itens (que possuam repasse) através da mudança de categoria, deve retira-los da folha de pagamento do prestador. |
| **Tickets relacionados:** | 3333987 |
| **Requisito:** | DSAUGHFATF-1369 |
