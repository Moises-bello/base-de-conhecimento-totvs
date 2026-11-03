---
article_id: 360020068752
category: PCO - Movimentos
content_hash: 3f8d6b9c67df3bcf37978d6841614d5f866d622cec0b85454c751e34eb1feb1b
fetched_at: '2026-06-28T22:37:09.484256+00:00'
product: protheus
section_id: 1500001550962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Aumentar campos de valores
  no módulo PCO (Orçamento/ Lançamento/ Classes)
type: support-article
updated_at: '2023-11-21T13:17:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020068752-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Aumentar-campos-de-valores-no-m%C3%B3dulo-PCO-Or%C3%A7amento-Lan%C3%A7amento-Classes
---

**Dúvida**Como aumentar campos de valores no Módulo PCO?  
   
 **Ambiente**  
Protheus – Planejamento e controle orçamentário – A partir da versão 12.1.17  
  
   
**Solução**

Deverá aumentar o tamanho do campo valor das tabelas AK2\_VALOR e AKD\_VALOR, para o tamanho desejado sem ultrapassar o tamanho máximo permitido

Também deverá aplicar o aumento no cadastro de classes (PCOA020) no campo picture customizada AK6\_CUSTOM  (Informe uma picture customizada no formato ADVPL a ser considerada na

visualização dos valores desta classe) conforme exemplo segue a picture @E 9,999,999,999,999.99
