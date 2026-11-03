---
content_hash: f3a51509d5fd5d8539a5aee9c01ae75e05ac92e3b6cb236babc11e5f63f2fb11
fetched_at: '2026-06-29T00:06:28.845394+00:00'
page_id: '233762643'
product: rm
source: tdn-rm
title: TTCOY1_DT_SEFIP_TOMADOR_COLIGADA_GLOBAL
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCOY1_DT_SEFIP_TOMADOR_COLIGADA_GLOBAL
version: 118
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Totvs Folha de Pagamento* |
| **Função:** | *Emissão registro 20 e ou 30 do SEFIP* |
| **Situação/Requisito:** | Ao gerar o SEFIP para autônomo do RM Fluxus Pessoa Física que prestem serviço em outro autônomo Pessoa Jurídica, o SEFIP não mais irá agrupá-lo no Tomador Empresa – registro 30 – mais sim irá considerar o Cliente/Fornecedor onde o serviço foi prestado – registro 20 – buscando esta informação no campo Cliente Origem existente no Lançamento do RM Fluxus em Valores | Tributos.  Com este campo em branco agrupamento será mantido no Tomador Empresa.  Porém o sistema não está realizando este processo e quando o autônomo possui um cliente fornecedor no campo Cliente Origem o autônomo não está sendo levado para o SEFIP. |
| **Solução/Implementação:** | O Sistema para a executar o tratamento abaixo para autônomo do RM Fluxus.  Ao gerar o SEFIP para autônomo do RM Fluxus Pessoa Física que prestem serviço em outro autônomo Pessoa Jurídica, o SEFIP não mais irá agrupá-lo no Tomador Empresa – registro 30 – mais sim irá considerar o Cliente/Fornecedor onde o serviço foi prestado – registro 20 – buscando esta informação no campo Cliente Origem existente no Lançamento do RM Fluxus em Valores | Tributos.  Com este campo em branco agrupamento será mantido no Tomador Empresa. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTCOY1 |
| **Requisito (ISSUE):** |  |

divs
