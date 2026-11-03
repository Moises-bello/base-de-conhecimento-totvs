---
article_id: 1500000190402
category: Financeiro - Contas a Pagar
content_hash: 5a19a3dca4fcfa7cbb17e919bac5a61b4890dddc9874b75a5c8b7aa4a319e75a
fetched_at: '2026-06-28T22:38:09.888902+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA240 - Não grava dados do banco do cadastrado fornecedor
  quando o titulo é gerado pela fatura
type: support-article
updated_at: '2022-03-23T01:53:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000190402-MP-SIGAFIN-FINA240-N%C3%A3o-grava-dados-do-banco-do-cadastrado-fornecedor-quando-o-titulo-%C3%A9-gerado-pela-fatura
---

**Dúvida**Na rotina FINA240 ( Borderô de Pagamento ),ao gerar o Borderô não traz os campos( AGENCIA FOR, BANCO FOR E CONTA FOR, ) gravados com os dados no cadastro do FORNECEDOR quando gerados pela rotina de faturas (FINA290), como proceder neste caso?  
  
**Ambiente**Microsiga Protheus - Financeiro - FINA240 - A partir da versão 12.  
  
**Solução**

Na rotina FINA240 ( Borderô de Pagamento ), ao gerar o Borderô não traz os campos( AGENCIA FOR, BANCO FOR  E CONTA FOR,  ) não se trata de um erro, mas sim de um conceito da rotina, pois uma fatura pode  ter vários títulos de vários Bancos diferentes. sendo os títulos especifico de cada banco desta forma o sistema define o critério de qual banco será gravado, uma vez que os bancos são diferentes.

**Exemplo**:  Uma fatura  de origem de 10 títulos, onde 2 títulos são de banco de, onde o campo (AGENCIA FOR, BANCO FOR e CONTA FOR )

fica em branco pois não há como especificar qual Banco será gravado, uma vez que os bancos são diferentes.

**Saiba Mais**  
Pontos de Entrada disponíveis na Rotina  
[MP - SIGAFIN - FINA240 - Borderô de Pagamentos - Ponto de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000048581-MP-SIGAFIN-FINA240-Border%C3%B4-de-Pagamentos-Ponto-de-Entrada?source=search)
