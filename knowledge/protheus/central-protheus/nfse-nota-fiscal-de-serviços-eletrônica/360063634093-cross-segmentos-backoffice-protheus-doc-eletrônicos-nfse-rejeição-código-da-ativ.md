---
article_id: 360063634093
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: cca28b1a037352c59bff80fc0c6771c8321d4eb78104ceeadccc5f4d8566a2e5
fetched_at: '2026-06-28T22:39:58.441932+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  Código da Atividade Inválido (Patos de Minas)
type: support-article
updated_at: '2025-06-25T21:00:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063634093-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-Atividade-Inv%C3%A1lido-Patos-de-Minas
---

**Ocorrência**Ao realizar a transmissão de um RPS para a prefeitura de Patos de Minas ocorre a rejeição: ***"Código da Atividade Inválido".  
  
![](https://totvssuporte.zendesk.com/attachments/token/NgMY2grbyCFwpXdXUH9kIQOUx/?name=inline-478552958.png)***

**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre exclusivamente por dois motivos: conteúdo da tag <tsCodAtiv> estar com conteúdo em branco ou incorreto:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104442213/mceclip0.png)  
  
**Solução**Para correção, deverá informar o Código da Atividade através do campo **B1\_CNAE** (Cadastro do Produto) ou **BZ\_CNAE** (caso utilize Indicador de Produtos).  
  
Pelo [manual de integração da prefeitura](http://187.72.229.145:8088/esiat/Downloads/40Integra%C3%A7%C3%A3o%20WebService/10Manual%20de%20Integra%C3%A7%C3%A3o%20Web%20Service.pdf), esse código da atividade seria o Item da Lista de Serviço, o que geralmente é informado no B1\_CODISS, porém especificamente para essa prefeitura é considerado através do B1\_CNAE.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003404702/mceclip1.png)
