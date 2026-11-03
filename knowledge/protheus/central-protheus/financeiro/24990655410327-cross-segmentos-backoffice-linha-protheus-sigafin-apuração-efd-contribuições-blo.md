---
article_id: 24990655410327
category: Financeiro
content_hash: 350e6f41ca1e98d51155467efc107ffaf4a4242b31e025860b1b3ab223a04f4b
fetched_at: '2026-06-28T22:38:01.215419+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Apuração EFD contribuições
  - Bloco F100, filtrar data de pagamento e não data de emissão
type: support-article
updated_at: '2024-07-18T20:06:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24990655410327-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Apura%C3%A7%C3%A3o-EFD-contribui%C3%A7%C3%B5es-Bloco-F100-filtrar-data-de-pagamento-e-n%C3%A3o-data-de-emiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24990655387415) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Bloco F100, como filtrar data de pagamento e não data de emissão?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Registro F100, sobre Arrendamento Mercantil para considerar a **data de pagamento** de títulos a natureza financeira precisa estar com o campo (**ED\_CLASFIS = 08**), com isso será filtrado o registro pela data de pagamento, desde que estes estejam totalmente baixados.

Para os outros títulos que não utilizam esta classificação na natureza, continua considerando o campo **E2\_EMIS1** para o filtro.  
  
**Saiba mais:**  
[8896683 DSERFINP-31637 DT F100 Créditos de PIS e COFINS sobre Arrendamento Mercantil considerando data de emissão como filtro](https://tdn.totvs.com/pages/releaseview.action?pageId=560651125)  
[Cross Segmentos - TOTVS Backoffice Linha Protheus - SIGAFIN - FINA050 - Gerar registro F100 pelo Contas a Pagar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020780132-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Gerar-registro-F100-pelo-Contas-a-Pagar)  
[SPDF1001 - Alteração do campo de data para o bloco F100 do SPED PISCOFINS](https://tdn.totvs.com/pages/releaseview.action?pageId=6071641)
