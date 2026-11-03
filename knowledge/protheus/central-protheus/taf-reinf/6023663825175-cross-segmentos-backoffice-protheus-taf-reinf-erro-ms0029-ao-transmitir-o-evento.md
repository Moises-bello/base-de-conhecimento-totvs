---
article_id: 6023663825175
category: TAF - REINF
content_hash: 092a6db449c9331001ff2ee773fd1500f3dc43cc01fadd051df48059fca69dc7
fetched_at: '2026-06-28T22:41:34.660340+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF - Erro MS0029 ao transmitir
  o evento R-2099 '
type: support-article
updated_at: '2023-03-31T17:05:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6023663825175-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-MS0029-ao-transmitir-o-evento-R-2099
---

**Dúvida** Erro ao realizar a transmissão do evento R-2099.

![MS0029.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13453156757655)  
  
**Ambiente**A partir do ambiente 12.1.33  
  
**Solução** Para correção do erro MS0029 exclua a apuração INCONSISTENTE do evento R-2099, apure e transmita o evento novamente.

   Como excluir apuração

    No módulo do TAF siga o passo a passo abaixo.

   -> Atualizações.

     -> Eventos REINF.

        -> Periódicos.

           -> R-2099 - Fechamento dos eventos periódicos.

 Ao acessa a rotina localize o período com a inconsistência e exclua a apuração.

![KCS_2099.png2.png.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6023548928791/KCS_2099.png2.png.png)

 Apure e transmita novamente o evento!
