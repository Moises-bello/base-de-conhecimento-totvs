---
content_hash: 95e525134a6a42567811e41274a6e44a4885b10514dc406377e25e5baa33edda
fetched_at: '2026-06-29T00:10:37.811252+00:00'
page_id: '540895122'
product: rm
source: tdn-rm
title: Testes comparativos do TDE no SQL Server
type: documentation
url: https://tdn.totvs.com/display/LRM/Testes+comparativos+do+TDE+no+SQL+Server
version: 5
---

No cenário utilizado para os testes comparativos, utilizamos as 4 versões do SQL Server atualmente homologadas para o RM (2012, 2014, 2016 e 2017) e todas estas na release DEVELOPER.

Para maior fidelidade ao teste, utilizamos o mesmo modo de compatibilidade em todas as versões: SQL 2012 (110)

## Resultados

##### Conversão da base de dados EXEMPLO da versão 12.1.22 para a versão 12.1.28:

##### Geração de Espelho de Ponto (PtoProcRelatEspelhoCartao)

##### Solicitação de recálculo da folha de ponto (PtoProcCalculo)

Utilizamos, também, uma base de cliente com aproximadamente 378 funcionários para as mesmas medições:

##### Conversão da base de dados de cliente da versão 12.1.22 para a versão 12.1.28:

##### Geração de Espelho de Ponto (PtoProcRelatEspelhoCartao):

##### Solicitação de recálculo da folha de ponto (PtoProcCalculo):

Não percebemos qualquer incompatibilidade na utilização do TDE com as bases de dados RM.
