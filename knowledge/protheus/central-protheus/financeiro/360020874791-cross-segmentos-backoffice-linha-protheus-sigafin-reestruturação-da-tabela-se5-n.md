---
article_id: 360020874791
category: Financeiro
content_hash: 124d116a5ccf140ec20c9e5f86df853624ccf4dcae26f6e36bd40f7432f9ea11
fetched_at: '2026-06-28T22:38:01.003913+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Reestruturação da tabela
  SE5 na família de tabelas FKx
type: support-article
updated_at: '2026-02-04T11:56:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020874791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Reestrutura%C3%A7%C3%A3o-da-tabela-SE5-na-fam%C3%ADlia-de-tabelas-FKx
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38156608875543)** Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
Como será a reestruturação da tabela SE5 na família de tabelas FKx

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

A tabela **SE5**- Movimentações bancárias cresceu ao longo do ciclo de vida das versões do Microsiga Protheus, impactando no processo de evolução do produto.

Para ser possível manter um processo contínuo de evolução do produto, foi elaborado um projeto para reestruturação da tabela de movimentações bancárias, criando uma nova família de tabelas para normalização da tabela **SE5**. Essa nova família de tabelas, com o prefixo **FK**, possui 11 tabelas, sendo:

**FK1** Baixas a receber. Registrar as baixas de títulos a receber.  
**FK2** Baixas a pagar. Registrar as baixas de títulos a pagar.  
**FK3** Impostos calculados. Armazenar os valores de impostos calculados para títulos a receber ou pagar.  
**FK4** Impostos retidos Armazenar os valores de impostos retidos para títulos a receber ou pagar.  
**FK5** Movimentos bancários registra as movimentações bancárias de títulos a receber, a pagar e individuais.  
**FK6** Valores acessórios Registra os valores de juros, multas, descontos, acréscimos, etc. de títulos a receber e pagar.  
**FK7** Tabela auxiliar. Nessa tabela são armazenadas as chaves de amarração entre as tabelas SE1 e SE2 com as tabelas FK1 e FK2  
**FK8** Dados contábeis Gravação de dados complementares da tabela FK5, exclusivamente com dados contábeis.  
**FK9** Complemento de movimento Gravação de dados complementares da tabela FK5, com dados de origem de módulos que integram ao Financeiro.  
**FKA** Rastreio de movimento reúne em um único processo as informações referentes às baixas (FK1/FK2), movimento bancário (FK5) e cheques (SEF) e suas operações de estorno.  
**FKB** Tipos de movimentos de usos internos.  
  
**Importante:**   
Para o correto funcionamento do produto, o compartilhamento das tabelas acima deve ser igual ao da tabela **SE5**.

**Saiba Mais**  
[Reestruturação da tabela SE5 na família de tabelas FKx](http://tdn.totvs.com/pages/viewpage.action?pageId=183730415)
