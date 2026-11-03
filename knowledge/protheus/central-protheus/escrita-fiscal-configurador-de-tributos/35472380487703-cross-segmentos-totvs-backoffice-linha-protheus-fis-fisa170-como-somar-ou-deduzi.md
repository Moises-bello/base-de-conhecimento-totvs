---
article_id: 35472380487703
category: Escrita Fiscal - Configurador de Tributos
content_hash: 53a6b57c450dfebf364dbb8bbb20f5709f182eb20568faaeb17c65b09d141583
fetched_at: '2026-06-28T22:39:18.381320+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como somar
  ou deduzir impostos no total da nota pelo Configurador de Tributos?
type: support-article
updated_at: '2025-10-07T19:04:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35472380487703-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-somar-ou-deduzir-impostos-no-total-da-nota-pelo-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35472349306135) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como somar impostos no total da nota pelo Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2210  
  
**Solução**

Para somar ou deduzir impostos no total da nota, deve ser configurado o campo Total da nota (CJ2\_STOTNF) na Regra de Escrituração da pasta Regra de Cálculo Documento Fiscal.

No campo em questão há 8 possibilidades de configuração, como poderá validar a seguir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35472380474903)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35472349306903)

Após criar a Regra de Escrituração, vincule no campo Escrituração (F2B\_CODESC) na Regra de Cálculo - Documentos Fiscais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35472349307543)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35472349308311)

Lembrando que cada tributo deve ter sua Regra de Escrituração, pois na dentro do cadastro tem informações de situação tributária.

Todos os tributos podem possuir essa validação, pois o cadastro é livre conforme critério definido pelo cliente.

Com isso, podem ser somados ou subtraídos os seguintes tributos:

ICMS, IPI, PIS, COFINS, CBS, IBS, ISS, IRRF, INSS, etc.

<https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos>
