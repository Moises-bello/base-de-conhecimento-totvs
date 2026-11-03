---
article_id: 360034294253
category: Escrita Fiscal - Impostos - ICMS
content_hash: 66222d1ddd149734317591dd825c67adc0a8c2fc297a85cc98524056025f45e0
fetched_at: '2026-06-28T22:39:24.402803+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o
  sistema para calcular SUFRAMA?
type: support-article
updated_at: '2024-07-25T20:01:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-sistema-para-calcular-SUFRAMA
---

**Dúvida**Como configurar o sistema para calcular SUFRAMA?  
  
**Ambiente**Protheus - SIGAFIS – A partir da versão 11.80  
  
**Solução**

Na documentação do link abaixo há 13 exemplos de configuração para o SUFRAMA.

Este documento é um guia que demonstra parâmetros e exemplos de configuração referentes as diversas formas de cálculo do desconto de ICMS, PIS e COFINS em operações para a Zona Franca/Área de Livre Comércio (SUFRAMA).

Por favor, valide qual dos cenários se enquadra sua operação e configure de acordo.

<https://tdn.totvs.com/pages/releaseview.action?pageId=605019302>

Observações:

* Atenção na configuração dos cadastros de Cliente, TES, Produto e nos Parâmetros (SIGACFG).
* Se sua operação não tem o ICMS desonerado, não preencher o campo Mot. Desone (F4\_MOTICM) no TES (deixar campo em branco).
