---
content_hash: f1b5954a692ea3d94db1507b138ef724f9f41431b975edbb396463d667100e90
fetched_at: '2026-06-29T00:06:21.703841+00:00'
page_id: '223177333'
product: rm
source: tdn-rm
title: TTQRD4_DT_SugestaoCompras_Obrigando_Preenchimento_VolumeQuantidadeAno
type: documentation
url: https://tdn.totvs.com/display/LRM/TTQRD4_DT_SugestaoCompras_Obrigando_Preenchimento_VolumeQuantidadeAno
version: 1
---

# SUGESTÃO DE COMPRAS - WEB

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Sugestão de compras WEB* |
| **Situação/Requisito:** | *Foi identificado que ao tentar salvar uma sugestão compras pelo portal o sistema não permite e retorna erro nos campos ANO, VOLUME e QUANTIDADE como sendo obrigatório o preenchimento destes campos.* |
| **Solução/Implementação:** | *Foi identificado que o erro era causado por uma validação incorreta se estes campos possuem somente números, o sistema considera vazio como sendo caractere e retornava o erro, foi feito o ajuste para não validar se os campos possuem somente números se estivem vazio, assim o erro não ocorreu mais.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
