---
article_id: 29071451029271
category: NFe - Nota Fiscal Eletrônica
content_hash: 70cccc00a28a210a9a904719ffc00ec9458e024be86be5e96ee10a718929b69a
fetched_at: '2026-06-28T22:40:00.037933+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 795 Rejeição :
  Total do ICMS desonerado difere do somatório dos itens'
type: support-article
updated_at: '2025-01-08T18:09:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29071451029271-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-795-Rejei%C3%A7%C3%A3o-Total-do-ICMS-desonerado-difere-do-somat%C3%B3rio-dos-itens
---

**Dúvida**  
Como solucionar a rejeição Rejeição 795 Rejeição : Total do ICMS desonerado difere do somatório dos itens

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS

**Solução**

A rejeição 795 ocorrerá quando o valor da tag vICMSDeson no totalizador (tag ICMSTot) for diferente da soma dos valores de vICMSDeson por item.

Exemplo da emissão de forma correta:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29071450997143)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29071451002007)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29071451006231)

O descritivo desses valores podem ser verificados na planilha financeira da nota ou na tabela CD2 CD2\_DESCZF na linha do CD2\_IMP = ZFM, que armazena os valores escriturados por item.

Se houver divergências nos valores, é necessário validar a escrituração fiscal dos itens. Caso a escrituração esteja correta, recomendamos atualizar o fonte [NFESEFAZ.prw](https://suporte.totvs.com/portal/p/10098/download?e=1152113) do ambiente.

Se o valor de desoneração do ICMS desonerado for informado na tributação de cada item, o totalizador de desoneração do ICMS na NF-e deverá coincidir exatamente com a soma dos valores desonerados dos itens.

Validação da Sefaz:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29071405598743)
