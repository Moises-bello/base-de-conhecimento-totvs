---
article_id: 360026676153
category: Gestão de Armazenagem (WMS)
content_hash: 6cb6fc9d93f872cec291d65bd03a5b37ac25ed9376d33aa1c242cb623178ae50
fetched_at: '2026-06-28T22:45:47.903783+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Cálculo de apanhe mínimo quando não informado
  o DC3_QTDUNI
type: support-article
updated_at: '2025-10-31T22:25:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026676153-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-C%C3%A1lculo-de-apanhe-m%C3%ADnimo-quando-n%C3%A3o-informado-o-DC3-QTDUNI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21717726392599) Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Como funciona o **cálculo de apanhe mínimo** quando não informado o **DC3\_QTDUNI**?  
  
**Ambiente****TOTVS Distribuição** - **TOTVS WMS** (Linha Protheus) - Gestão de Armazenagem (**WMS**) - Todas as versões  
  
**Solução**A **separação mínima** ou **apanhe mínimo** pode ser configurado no cadastro **Sequência Abastecimento - WMSA030**, a partir do campo **DC3\_QTDUNI - Sep Minima**.  
  
No entanto, quando não é informada esta quantidade, o Sistema realiza o cálculo considerando o número de casas decimais do campo. Será aplicada a seguinte fórmula, onde **n** é o número de casas decimais do campo:  
  
**Apanhe Mínimo Unitário = 1/10n****Saiba mais**Informações adicionais podem ser obtidas no documento: [Cálculo de apanhe unitário mínimo para produtos WMS em relação a casas decimais.](https://tdn.totvs.com/pages/viewpage.action?pageId=654947244)  
Também assista ao *Webinar* sobre o cadastro **Sequência de Abastecimento**: [Webinar TOTVS | Desvendando a Sequência de Abastecimento](https://www.youtube.com/watch?v=LggYlJy-GEc)
