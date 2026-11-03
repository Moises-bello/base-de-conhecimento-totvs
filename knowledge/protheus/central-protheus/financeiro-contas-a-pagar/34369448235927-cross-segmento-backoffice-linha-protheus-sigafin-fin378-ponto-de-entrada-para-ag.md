---
article_id: 34369448235927
category: Financeiro - Contas a Pagar
content_hash: c901b7bf160cdfc201f8719a99547dea98fddf62c7461c0bd874323aa5f32180
fetched_at: '2026-06-28T22:38:06.955404+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FIN378 - Ponto de entrada
  para aglutinar impostos de PIS, COFINS E CSLL
type: support-article
updated_at: '2025-08-22T13:55:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34369448235927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FIN378-Ponto-de-entrada-para-aglutinar-impostos-de-PIS-COFINS-E-CSLL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34369448231063) Tempo aproximado para leitura: **00:05min**  
  
**Dúvida**  
Quais são os pontos de entrada para a rotina de aglutinação de impostos de PIS, COFINS E CSLL?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Abaixo estão os pontos de entrada disponíveis na rotina de aglutinação de impostos (FINA378– PIS COFINS E CSLL):

[**F378GRV**](https://tdn.totvs.com/pages/releaseview.action?pageId=563425531) – Executado após a gravação dos títulos de aglutinação de impostos (SE2), permitindo ações adicionais após esse processo.

[**F378CANBX**](https://tdn.totvs.com/display/public/PROT/F378CanBx+-+Armazena+registros+cancelados) - Ponto de Entrada criado dentro da função fa378Can() para armazenar o Recno dos registros que foram cancelados na tabela SE5 (movimentação bancária).

[**FA378EST**](https://tdn.totvs.com/pages/releaseview.action?pageId=563425555) - O ponto de entrada FA378EST é utilizado para validação do cancelamento da aglutinação de PIS/COFINS/CSLL.
