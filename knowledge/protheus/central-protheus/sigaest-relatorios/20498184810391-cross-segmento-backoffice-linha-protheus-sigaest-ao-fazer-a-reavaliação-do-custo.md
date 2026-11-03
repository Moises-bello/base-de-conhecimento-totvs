---
article_id: 20498184810391
category: SIGAEST - RELATORIOS
content_hash: 8319ed6eddc7b1c595768e1042397e21bce201b294692764f8797c0c57d109b7
fetched_at: '2026-06-28T22:39:06.007139+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao fazer a Reavaliação
  do Custo Médio gera várias linhas no Kardex, por que isso ocorre?
type: support-article
updated_at: '2025-03-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20498184810391-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-fazer-a-Reavalia%C3%A7%C3%A3o-do-Custo-M%C3%A9dio-gera-v%C3%A1rias-linhas-no-Kardex-por-que-isso-ocorre
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20498184793879) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao fazer a Reavaliação de Custo Médio para um determinado produto aparece várias linhas no relatório MATR900 e na Consulta Diária, o que seriam essas linhas e como remove-las?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Ao fazer a Reavaliação de Custo Médio de um determinado produto e verificar na consulta do relatório MATR900 ou Consulta diária aparece várias linhas com valor zero além do movimento custeado conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20498184795927)

Esse cenário de várias linhas escritas com o tipo "DEA" ou "REA", com custo zero, significa que seu parametro ***MV\_MOEDACM*** deve está com ***conteúdo: "2,3,4,5"*** e com isso gera essas ***linhas para cada moeda***.

Caso desejar que não apresente essas linhas no Kardex e não utilizar essas moedas para custeio, é necessário retirar o conteúdo do parâmetro, estornar e refazer uma nova Reavaliação de Custo Médio e executar novamente a rotina de Custo Médio e verá que não irá mais apresentar.

Segue um exemplo do mesmo produto abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20502711661463)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
