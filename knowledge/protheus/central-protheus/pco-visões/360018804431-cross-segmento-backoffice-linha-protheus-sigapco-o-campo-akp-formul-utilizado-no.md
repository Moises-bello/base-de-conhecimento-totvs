---
article_id: 360018804431
category: PCO - Visões
content_hash: 4fc5d56bc0c7611e74a442b60a1be681ef70ccf053c411338183c76b62ba21cd
fetched_at: '2026-06-28T22:37:08.778704+00:00'
product: protheus
section_id: 1500001550982
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - O campo AKP_FORMUL utilizado
  no cadastro de visões gerenciais orçamentárias pode ser usado com RDMAKES ou com
  fórmulas simples?
type: support-article
updated_at: '2023-11-21T14:15:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018804431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-O-campo-AKP-FORMUL-utilizado-no-cadastro-de-vis%C3%B5es-gerenciais-or%C3%A7ament%C3%A1rias-pode-ser-usado-com-RDMAKES-ou-com-f%C3%B3rmulas-simples
---

**Dúvida**O campo AKP\_FORMUL utilizado no cadastro de visões gerenciais orçamentárias pode ser usado com RDMAKES ou com fórmulas simples?  
   
 **Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

O campo pode ser utilizado das duas formas. Veja os exemplos:

* RDMAKE: preencher com :

U\_RDKMAKE()

* Formula Simples

Iif(dbSelectArea('AKD'),AKD->AKD\_VALOR1, 0)
