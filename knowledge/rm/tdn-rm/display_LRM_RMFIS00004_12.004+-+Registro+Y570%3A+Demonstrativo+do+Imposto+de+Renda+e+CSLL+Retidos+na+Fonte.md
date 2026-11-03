---
content_hash: a13deee15b7a82f37c202efbf164fabdf80f5b721e970a290165ccb4634352bf
fetched_at: '2026-06-29T00:06:02.084734+00:00'
page_id: '198943378'
product: rm
source: tdn-rm
title: 'RMFIS00004_12.004 - Registro Y570: Demonstrativo do Imposto de Renda e CSLL
  Retidos na Fonte'
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00004_12.004+-+Registro+Y570%3A+Demonstrativo+do+Imposto+de+Renda+e+CSLL+Retidos+na+Fonte
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão: 11.82.39 e superiores** |
| **Processo** | **:** | ECF - Escrituração Contábil Fiscal |
| **Subprocesso** | **:** | ECF - Escrituração Contábil Fiscal |
| **Data da publicação** | **:** | 13/08/2015 |

**Regras para geração do registro Y570 - Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte:**

A) Para seleção dos Lançamentos fiscais de retenção do **Liber**

* Lançamento de Saída
* DataLF do Lançamento no período da Rotina
* A Coligada e filial dos lançamentos serão selecionados conforme parametrização da rotina ECF
* Lançamento que não esteja com status Estonado ou Cancelado
* Que tenha cadastrado na pasta Outros Tributos do lançamento os tributos IRRF, IRRF-PJ ou CSLL-RF
* Para Montagem dos Valores dos Tributos serão considerados os valores da Tabela DTRBLAF (Tributos do lançamento)

B) Para seleção dos Lançamentos fiscais de retenção do **Liber** x **Fluxus** x **Nucleus**

Para utilizar a regra "B" é necessário o parâmetro da Tela Filial - Anexo - Parâmetros - Escrituração Contábil - Pasta  Tributação - "Carregar Retenções do Fluxus - Registro Y570" marcado.

* Lançamento de Saída
* A Coligada e filial dos lançamento serão selecionados conforme parametrização da rotina ECF
* Lançamento Fiscal que não seja Estonado ou Cancelado

Serão Selecionados os Lançamentos Observando também as regras abaixo:

1º) Serão selecionados os lançamentos fiscais aplicando a regra geral para o tributos IRRF-PJ. Para Montagem dos valores dos tributos serão considerados os valores da Tabela DTRBLAF (Tributos do lançamento)

2º) Serão selecionados lançamentos fiscais aplicando a regra geral. Os lançamentos fiscais selecionados devem ser vinculados a lançamento financeiro  com a data da baixa dentro do período de geração da rotina ECF.

3º) Serão selecionados lançamentos fiscais aplicando a regra geral.  Os lançamentos fiscais devem ser provenientes do (RMNucleus) Movimento que seja vinculado a lançamento financeiro com com a data da baixa dentro do período da geração da rotina.

Nas regras 2º e 3º, para Montagem dos valores dos tributos serão considerados os valores da Tabela FTRBLAN  (Tributos do lançamento Financeiro) considerando os tributos IRRF ou CSLL-RF.

**IMPORTANTE!** Para geração do Y570 utilizando informações do RM Fluxus será necessário entrar em contato com o Suporte e solicitar o Script ExecSql.RMLIBER.TSGAP6. Ao executar o script será criado o parâmetro “Carregar Retenções do Fluxus” nos parâmetros da ECF no cadastro da Filial. Marcando esse parâmetro o sistema irá verificar os lançamentos financeiros com os tributos CSLL-RF, IRRF. Caso o parâmetro esteja desmarcado o sistema irá verificar as informações somente no RM Liber.
