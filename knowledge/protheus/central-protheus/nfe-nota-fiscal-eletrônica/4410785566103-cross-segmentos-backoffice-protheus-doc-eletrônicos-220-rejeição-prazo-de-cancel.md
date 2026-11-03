---
article_id: 4410785566103
category: NFe - Nota Fiscal Eletrônica
content_hash: aecdabdb42290f837c4f37a2133dbc45bf73c7bfb12b00e4eb64cf5475de5ff4
fetched_at: '2026-06-28T22:40:00.200235+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  220 - Rejeição:
  Prazo de Cancelamento superior ao previsto na Legislação'
type: support-article
updated_at: '2022-05-17T13:07:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410785566103--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-220-Rejei%C3%A7%C3%A3o-Prazo-de-Cancelamento-superior-ao-previsto-na-Legisla%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a 220 - Rejeição: Prazo de Cancelamento superior ao previsto na Legislação  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Depois de passar o prazo de autorização determinado para o cancelamento, **é necessário entrar em contato com a SEFAZ** e verificar qual será o procedimento.

**Se a SEFAZ autorizar o cancelamento fora do prazo:**

1. Preencha o parâmetro **MV\_CANCEXT** com a quantidade de dias para o cancelamento da nota. É necessário verificar quantos dias de sua autorização até a data atual para configurar o parâmetro.

**Exemplo**: MV\_CANCEXT = Ex: 30 (Deixe esse parâmetro como 30, não pode ser colocado 999)

2. Excluir a numeração e **transmitir para realizar o cancelamento.**
