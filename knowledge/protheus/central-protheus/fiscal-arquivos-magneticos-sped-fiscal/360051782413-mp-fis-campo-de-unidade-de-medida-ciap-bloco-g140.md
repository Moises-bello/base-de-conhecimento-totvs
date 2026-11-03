---
article_id: 360051782413
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 4f62b8759b23fb4806fd28060984044421fbdd24a4d9af72d78a1d6a1652df86
fetched_at: '2026-06-28T22:42:03.774445+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Campo de Unidade de Medida - CIAP - Bloco G140
type: support-article
updated_at: '2021-04-28T14:25:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051782413-MP-FIS-Campo-de-Unidade-de-Medida-CIAP-Bloco-G140
---

**Dúvida**Preenchimento do campo Unidade de Medida (05 - UNID) no bloco G, registro G140 do SPED FISCAL.  
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
A rotina de manutenção CIAP não possui campo de unidade de medida.

O preenchimento do campo Unidade de Medida (05 - UNID) no bloco G, registro G140 será através do registros abaixo:  
  
Registro 0190 - Identificação das Unidades de Medida

Registro 0200 - Tabela de Identificação do Item (Produtos e Serviços  
  
Registro 0220 - Fatores de Conversão de Unidades

Conforme descrito abaixo em trecho referente a validação do campo Unidade de Medida (05 - UNID) retirado do guia prático do SPED FISCAL:

Campo 05 (UNID) - Validação: o valor informado neste campo deve existir no registro 0190. Caso a unidade de medida informada seja diferente da unidade de medida de controle de estoque informada no Registro 0200, deverá ser informado no Registro 0220 o fator de conversão entre as unidades de medida.

Abaixo informação relevante referente o registro 0190:   
  
Registro tipo 0190 - Identificação das Unidades de Medida

As informações contidas neste registro são obtidas por meio dos Cadastros de Produtos (SB1) e Cadastro de Unidades de Medida (SAH).

Este registro é gerado para todas as unidades de medida utilizadas no período. Por padrão é considerada a primeira unidade de medida do documento, para utilização da segunda ou outra Unidade de Medida, customize o ponto de entrada SPDFIS02. Para mais detalhes sobre este PE, consulte o portal TDN.

Abaixo link contendo as informações referente as unidade de medida dos registros citados acima e do guia prático do SPED FISCAL:

<https://tdn.totvs.com/display/public/PROT/FIS0005_SPED_FISCAL>

<http://sped.rfb.gov.br/estatico/0D/434EFF065B893AB70D59AD102A946DC9237680/2019.05.21_GUIA%20PR%c3%81TICO%20DA%20EFD%20-%20Vers%c3%a3o%203.0.3%20-%20v3%20para%20publica%c3%a7%c3%a3o.pdf>
