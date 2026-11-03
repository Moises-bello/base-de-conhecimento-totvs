---
article_id: 360045353873
category: FATURAMENTO - RELATÓRIOS
content_hash: 7be0367f69831617ac2757ca4efe68a913d2320fe2d94be93ba46e1a4efb0b04
fetched_at: '2026-06-28T22:38:22.982663+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - Relatório
  MATR780 opção Inclui devolução igual sim
type: support-article
updated_at: '2021-06-25T15:48:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045353873-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Relat%C3%B3rio-MATR780-op%C3%A7%C3%A3o-Inclui-devolu%C3%A7%C3%A3o-igual-sim
---

**Duvida**

Relatório MATR780 opção Inclui devolução igual sim.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - A partir da versão 11.80.  
  
**Solução**

Para trazer a informação da nota fiscal de devolução é necessário colocar a data da nota fiscal de origem e configurar os pergunte conforme demonstrado abaixo:

**Exemplo**: fiz uma nota de venda no dia 01/01/2017 e fiz devolução no dia 07/03/2018 tenho que colocar esse período para buscar as duas notas tanto a nota fiscal faturada como a nota fiscal devolvida:

![image2018-3-7_14-10-48.png](https://tdn.totvs.com/download/attachments/342313935/image2018-3-7_14-10-48.png?version=1&modificationDate=1520442649000&api=v2)

**Importante**: Para trazer a nota fiscal de Devolução é obrigatório colocar a data de emissão da nota fiscal de origem. No exemplo acima, seria 01/01/2017, pois a nota fiscal de devolução é vinculada a essa data:

![image2018-3-7_14-11-17.png](https://tdn.totvs.com/download/attachments/342313935/image2018-3-7_14-11-17.png?version=1&modificationDate=1520442678000&api=v2)

**Observação:** Se verificar a nota fiscal de devolução está amarrada a nota fiscal de origem.
