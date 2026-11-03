---
article_id: 360053259094
category: CRM - Dúvidas Gerais
content_hash: 4cc9734636825c8fdd864fca7e06d892ce7a6e318c0bec7ea3eeec6f886bacce
fetched_at: '2026-06-28T22:40:27.459739+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Help FT300PENDF
type: support-article
updated_at: '2024-04-25T12:17:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053259094-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Help-FT300PENDF
---

**Ocorrência**Ao tentar excluir uma oportunidade de venda, o sistema apresenta a mensagem de Help **FT300PENDF**.  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Causa**A oportunidade gerou revisão.  
  
**Solução**Para solucionar analise se  há revisão na oportunidade. Se a Oportunidade tiver gerado uma revisão, não será possível excluí-la, pois cria um vinculo na tabela **ADC**. O que determina se a oportunidade vai gerar revisão ou não é o parâmetro **MV\_FTREVIS**.

![](https://totvssuporte.zendesk.com/attachments/token/GXH4YJfKSyivls9vpZjeouf9O/?name=inline-2056167658.png)  
  
Veja também o parâmetro **MV\_ORCLIPD** tem que está preenchido com cliente ativo.  
O padrão é “00000101”, padrão considerando o tamanho “6” do código, e "2"  da loja. 

![](https://totvssuporte.zendesk.com/attachments/token/lelUQ7jiIJZJjA5EVjSERr2MS/?name=inline-873170584.png)
