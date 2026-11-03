---
article_id: 23400899238295
category: Escrita Fiscal - Configurador de Tributos
content_hash: f1d7391e444ee2172c51a1d23211d527c79decf6aa1df7c3f268784f777f1a01
fetched_at: '2026-06-28T22:39:17.431733+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como contabilizar
  os tributos genéricos?
type: support-article
updated_at: '2025-03-18T11:35:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23400899238295-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-contabilizar-os-tributos-gen%C3%A9ricos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23400912097175) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como contabilizar os tributos genéricos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Os valores dos tributos poderão ser contabilizados de duas formas, no processamento da apuração e no contabilização do documento fiscal.

Para contabilizar o tributo na apuração, foram criados dois novos códigos de lançamento padrão, **767**para inclusão e **768** para exclusão/estorno, quando estes lançamentos padrão são executados, o título gerado do tributo com valor a pagar estará devidamente posicionado.

Já para contabilizar o tributo no documento fiscal, não foi necessário criado nenhum código de lançamento padrão, serão utilizados os mesmo códigos já existentes para contabilização da nota fiscal, e neste caso os valores dos tributos estarão disponíveis na tabela **F2D(Tributos Genéricos Calculados)**, que são vinculados com o documento fiscal por meio dos campos **D1\_IDTRIB** e **D2\_IDTRIB**. Neste caso é importante ressaltar que pode haver mais de um tributo calculado por item de documento fiscal, então poderá haver mais de uma movimentação na tabela F2D para o item de documento fiscal (SD1, SD2).
