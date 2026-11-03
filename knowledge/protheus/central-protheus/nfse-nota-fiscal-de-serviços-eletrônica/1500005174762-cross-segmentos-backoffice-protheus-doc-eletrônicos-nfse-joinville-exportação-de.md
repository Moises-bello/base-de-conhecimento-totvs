---
article_id: 1500005174762
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f9902828435f1f93ab732c82a24d8ea2060a215d97fede69e5f707d2c03dedcb
fetched_at: '2026-06-28T22:39:57.527948+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Joinville
  Exportação de Serviço: Rejeição E11 - O valor do ISS não confere'
type: support-article
updated_at: '2025-07-02T14:13:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005174762-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Joinville-Exporta%C3%A7%C3%A3o-de-Servi%C3%A7o-Rejei%C3%A7%C3%A3o-E11-O-valor-do-ISS-n%C3%A3o-confere
---

**Dúvida**

Ao transmitir uma nota de exportação para Joinville, **com o serviço prestado dentro de Joinville**, ocorre a rejeição abaixo E11 - O valor do ISS não confere.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007083541/mceclip1.png)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**

Essa rejeição ocorre quando a tag <CodigoPais> dentro do grupo <Servico> possui um pais diferente de Brasil.

Veja que no exemplo abaixo o município de prestação, a exigibilidade e o município de incidência apontam para Joinville,  somente o país de prestação apontando para Coréia, República da.

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007084041/mceclip2.png)**

Nesse caso para não carregar automaticamente o país do tomador no país da prestação, é importante criar o campo de país na tabela SC5 e informar o nome desse campo dentro do parâmetro: **MV\_ENDPRES.**Para esse procedimento da criação do campo x MV\_ENDPRES, verifique a instrução passada no artigo:  
 [MP - NFSE - Dados da Prestacao](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026101732--MP-NFSE-Dados-da-Prestacao-Endere%C3%A7o-N%C3%BAmero-Complemento-Bairro-e-CEP)

Após criação do campo na SC5, o preenchimento desse campo com o pais da prestação deve ser de acordo com a tabela SYA onde por exemplo o código do **Brasil é 01058.**O TSS será responsável por converter esse código de acordo com o esperado pela prefeitura.Para funcionar corretamente esse procedimento **é importante ter o fonte ABRASF do TSS superior a 12/09/2019**, pois tratamos essa tag na issue DSERTSS2-4698.
