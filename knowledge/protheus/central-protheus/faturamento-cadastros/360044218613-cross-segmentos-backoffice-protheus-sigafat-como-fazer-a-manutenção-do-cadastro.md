---
article_id: 360044218613
category: Faturamento - Cadastros
content_hash: c31c8be4d8aefd8c4799c8dc0acb91d60808d55b451461e9086d80c8c15a148f
fetched_at: '2026-06-28T22:38:35.427980+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como fazer a manutenção do
  cadastro de região A1_REGIAO do cadastro de clientes (CRMA980)?
type: support-article
updated_at: '2025-07-25T12:47:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044218613-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-a-manuten%C3%A7%C3%A3o-do-cadastro-de-regi%C3%A3o-A1-REGIAO-do-cadastro-de-clientes-CRMA980
---

**Dúvida**

Como ajustar **tabela A2** do cadastro de região chamado no campo **A1\_REGIAO** no cadastro de clientes **(CRMA980)**?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - todas as versões.  
  
**Solução**

O cadastro da região está dentro da **tabela genérica SX5**, **tabela A2**, o conteúdo padrão recebido é:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408847738007)

E estas informações são passadas para a consulta padrão no campo **A1\_REGIÃO** para serem consultados via F3 no cadastro do cliente:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408847878551)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408860626071)

Para realizar a manutenção acesse:  Configurador -> Base de Dados -> Dicionário -> Base de Dados -> Tabela Genéricas, pesquise por tabela **A2**.

***Importante: Qualquer alteração no conteúdo da tabela que não seja efetuado via Configurador, pode resultar no Help Regnois e não encontraras informações ao efetuar a consulta F3 no campo A1\_REGIÂO. Para adição de novos conteúdos é importante efetuar a manutenção via módulo de Configurador,***

**Obs**: O campo é utilizado no filtro no relatório do Curva ABC por região **MATR755,** para mais informações sobre o relatório, acesse: **[Relatório Curva ABC (MATR765 Por Cliente / MATR755 - Por Região)](https://tdn.totvs.com/x/d7p3DQ)**
