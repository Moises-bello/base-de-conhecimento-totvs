---
article_id: 4405110549399
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 9d102be41a70d4dd3e213b9d351c2793fba6ecd664cff1d6f81ec6526864c38d
fetched_at: '2026-06-28T22:42:07.938614+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Porque o Extrator
  Considera a Data de Digitação/Entrada e Não a Data de Emissão do Documento Fiscal?
type: support-article
updated_at: '2022-08-18T17:45:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405110549399-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Porque-o-Extrator-Considera-a-Data-de-Digita%C3%A7%C3%A3o-Entrada-e-N%C3%A3o-a-Data-de-Emiss%C3%A3o-do-Documento-Fiscal
---

**Dúvida**Porque o Extrator Considera a Data de Digitação/Entrada e Não a Data de Emissão do Documento Fiscal?  
  
**Ambiente**  
Protheus - TAF - Todas as versões  
  
**Solução**

O Extrator Fiscal considera a data de digitação/entrada, por motivo de não extrair informações apenas para a obrigação fiscal da EFD REINF.

Hoje o Extrator Fiscal é responsável pela extração das informações para atendimento, como por exemplo, a GIA SP.

Por esse motivo hoje é utilizado a data de digitação/entrada.

O Extrator Fiscal é apenas a rotina que irá extrair as informações referente os documentos fiscais para o TAF.

O módulo que irá gerar a obrigação EFD REINF, será o TAF após efetuar a apuração dos eventos na rotina TAFXREINF.
