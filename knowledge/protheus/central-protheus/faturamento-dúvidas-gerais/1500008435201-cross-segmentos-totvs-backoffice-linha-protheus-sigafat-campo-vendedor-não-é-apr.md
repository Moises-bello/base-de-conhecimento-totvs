---
article_id: 1500008435201
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4397f6a5a1fb9de00afb229aa4db13e5bf4ec1cd06a0bffaf46a94b7c63277da
fetched_at: '2026-06-28T22:38:29.945921+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Campo Vendedor
  não é apresentado na posição do cliente
type: support-article
updated_at: '2021-09-09T16:40:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008435201-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Campo-Vendedor-n%C3%A3o-%C3%A9-apresentado-na-posi%C3%A7%C3%A3o-do-cliente
---

**Ocorrência**

O campo vendedor não é apresentado na posição do cliente após a atualização.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012331702/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012683201/mceclip3.png)  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da release 12.1.17.

**Causa**

O campo vendedor deixou de ser exibido na alteração do **finc010** de **22.12.2020**, a equipe de desenvolvimento de produto do Financeiro, efetuou uma limpeza no fonte com retirada de funções não compiladas, onde estavam relacionadas a função **ACAR590**, módulo do **Protheus Educacional** , que não esta compilado no RPO, devido a descontinuidade de uso do módulo em questão, retirando todos os trechos que faziam menção a ele através do parâmetro **MV\_ACATIVO**.  
  
 If ! lSigaGE  
  @ 023,206 SAY STR0057 SIZE 035,07 OF oDlg PIXEL //"**Vendedor**"  
  @ 030,206 MSGET SA1->A1\_VEND    SIZE 053,09 WHEN .F. OF oDlg PIXEL  
 EndIf

Todavia, o campo **Vendedor** é de uso comum em outros módulos que se integram com a rotina de **Posição de Clientes** (**Finc010**), desta forma, a informação passou a reintegrar a rotina a partir de **09.03.2021**, sendo necessária a aplicação do **expedição contínua do módulo Financeiro** no  ambiente para reaver a chamada deste campo na consulta posição de clientes.

**Solução**

Para que o campo Vendedor apareça normalmente na Consulta Posição de Clientes, siga os seguintes passos:  
**1-**Baixe o pacote de **Expedição contínua do Financeiro**, conforme a sua release:

* **<https://suporte.totvs.com/portal/p/10098/download#detail/954746> 12.1.27**
* **<https://suporte.totvs.com/portal/p/10098/download#detail/817562> 12.1.25**

**2-**Via VS-Code, aplique a atualização em seu ambiente de homologação para validar e posteriormente no ambiente de produção.

**3-** Reinicie o Smartclient e abra a consulta Posição de Clientes, para validar a inclusão do campo Vendedor na consulta.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408156668055/mceclip0.png)

***Importante**: A atualização de ambiente deve ser efetuada por um analista que detém plenos conhecimento de estrutura Protheus e ferramenta Vs-CODE, em caso de dúvida na aplicação de pacote na ferramenta, contate nossa equipe de ADVPL.*

*Cliente com ambiente Cloud Protheus, deve solicitar a aplicação junto ao Cloud.*

*Sempre efetuar um backup do RPO antes de qualquer atualização.*
