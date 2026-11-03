---
article_id: 34369191921815
category: Financeiro - Contas a Pagar
content_hash: 1d2c23b32b25d9b0313916bfef3e3cb82eae0a38ddb44cc575d0906ed7442934
fetched_at: '2026-06-28T22:38:06.952661+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FIN376 - Ponto de entrada
  para aglutinar impostos de IRRF
type: support-article
updated_at: '2025-08-22T13:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34369191921815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FIN376-Ponto-de-entrada-para-aglutinar-impostos-de-IRRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34369208352023) Tempo aproximado para leitura: **00:05min**  
  
**Dúvida**  
Quais são os pontos de entrada para a rotina de aglutinação de impostos de IRRF?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Abaixo estão os pontos de entrada disponíveis na rotina de aglutinação de impostos (FINA376 – IRRF):

[**F376QRY**](https://tdn.totvs.com/pages/releaseview.action?pageId=549489500&utm_source=chatgpt.com) – Permite adicionar complementos à query principal usada na rotina de aglutinação (ou seja, você pode filtrar ou estender a consulta SQL que a rotina utiliza)

**F376BRW** – Normalmente relacionado a ações na exibição browser da rotina (apesar de não haver detalhes explícitos nos resultados, aparece na lista geral de PEs)

[**F376PROJ, F376PRF, F376GRV**](https://tdn.totvs.com/pages/releaseview.action?pageId=549493283) – São executados após a gravação do título de aglutinação de impostos, permitindo ações personalizadas após essa etapa.

[**F376BXTX**](https://tdn.totvs.com/pages/releaseview.action?pageId=6071416)– Relacionado à rotina de baixa de títulos do tipo “TX”, permite acessar informações referentes a essa baixa quando estão envolvidos impostos (PIS, COFINS, CSLL)

[**FA378POS**](https://tdn.totvs.com/display/public/mp/FA378POS+-+Valida+dados+--+11986) – Usado após a confirmação do cancelamento da aglutinação de impostos, ou seja, validação após o cancelamento.

[**F376CANBX**](https://tdn-homolog.totvs.com/pages/releaseview.action?pageId=696705441) – Invocado após o cancelamento da aglutinação, recebe o identificador (R\_E\_C\_N\_O\_) dos títulos cancelados na tabela SE5

**Saiba mais**

[Aglutinação de impostos - FINA376](https://tdn.totvs.com/pages/releaseview.action?pageId=496808458)
