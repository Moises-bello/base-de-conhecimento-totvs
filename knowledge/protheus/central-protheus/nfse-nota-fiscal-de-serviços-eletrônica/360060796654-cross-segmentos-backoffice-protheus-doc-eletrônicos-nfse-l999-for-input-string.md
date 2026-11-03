---
article_id: 360060796654
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: fe6f0ec54e4c68942ddaf7fa32f89bc37c4be449c1dacb843ca2b9109bf6255e
fetched_at: '2026-06-28T22:39:57.532955+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - L999 - FOR
  INPUT STRING: ""'
type: support-article
updated_at: '2025-07-02T14:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060796654-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-L999-FOR-INPUT-STRING
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre a rejeição: ***L999 - For input string: ""***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103139893/mceclip0.png)

Caso seja verificado a rejeição no XML\_RET (SPED053) ou XML\_ERRO (SPED055) a mensagem completa indica uma orientação para contatar a prefeitura para verificar o real motivo do erro:  
  
![](https://totvssuporte.zendesk.com/attachments/token/YuP0V7bBjWjgUvfUbrwxKHSXA/?name=inline781575149.png)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Normalmente essa rejeição ocorre quando alguma informação obrigatória está ausente no cabeçalho do lote (conteúdo XML\_LOTE da SPED053). Exemplo mais comum: **Inscrição Municipal do Prestador.**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002076042/mceclip1.png)  
  
**Solução**O primeiro passo é verificar essa questão citada acima através da documentação a seguir: [MP - NFSE - IM do Tomador e IM do Prestador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027856371-MP-NFSE-IM-do-Tomador-e-IM-do-Prestador)  
  
*Caso mesmo após preenchimento e o conteúdo gerado no XML\_LOTE, deverá contatar a prefeitura para verificar o real motivo do erro, caso nenhum outro ponto esteja evidente (tag vazia).*
