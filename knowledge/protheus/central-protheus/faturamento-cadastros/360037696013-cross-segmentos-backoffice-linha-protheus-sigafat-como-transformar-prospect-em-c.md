---
article_id: 360037696013
category: Faturamento - Cadastros
content_hash: 230812b6b7aa1b6365dc9ee636fd60b72a3db7b1aefd5d51e6dbf7162cf72504
fetched_at: '2026-06-28T22:38:35.393451+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT -Como transformar prospect
  em cliente sem fechar a oportunidade de venda
type: support-article
updated_at: '2023-07-12T21:14:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037696013-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Como-transformar-prospect-em-cliente-sem-fechar-a-oportunidade-de-venda
---

**Dúvida**

É possível gerar um pedido de venda (**MATA410**) de orçamento (**MATA415**) integrado com uma oportunidade de vendas (**FATA300**) para um prospect (**TMKA260**) e transformá-lo em cliente (**MATA030**),  sem que seja necessário encerrar a oportunidade?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Via oportunidade não é possível, como regra do processo de faturamento é preciso encerrar a oportunidade para  gerar o pedido, e somente com a formalização da venda que o prospect é transformado em cliente.

Para transformar o prospect em cliente via faturamento, basta seguir as configurações do artigo: **[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Transformar Prospect em Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013174528-MP-FAT-Transformar-Prospect-em-Cliente)**

Uma segunda opção de transformar o prospect em cliente é a utilização do módulo Call Center, onde não há o uso da oportunidade dentro do processo de venda, basta incluir um orçamento televendas(**TMKA273**) do tipo faturamento para o prospect e será gerado um pedido para o mesmo já o convertendo para o cliente, conforme artigo: **[Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Transformar Prospect em cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016637631-MP-TMK-Transformar-Prospect-em-cliente)**

E uma última opção é a geração do cliente direto do cadastro de prospect, sem uso de oportunidade de vendas, porém, é necessário a integração de módulos de gestão de concessionária e licença de uso desses módulos(Sigavei, AutoPeças ou Sigaofi), as demais configurações necessárias estão documentadas no artigo:**[MP-FAT-Conversão do prospect em cliente direto do cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036760514-MP-FAT-Convers%C3%A3o-do-prospect-em-cliente-direto-do-cadastro-?source=search)**
