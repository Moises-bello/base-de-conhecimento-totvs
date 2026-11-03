---
content_hash: d1ca46a38065b9cacd4a56d003ef39a2289bbb7cbe418716c64211b96ecda06f
fetched_at: '2026-06-29T00:08:17.531142+00:00'
page_id: '255755926'
product: rm
source: tdn-rm
title: TVNURA_DT_Cadastro_Area_Codigo_Manual_CDU
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNURA_DT_Cadastro_Area_Codigo_Manual_CDU
version: 114
---

# CADASTRO DE ÁREA DO CONHECIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Áreas do conhecimento* |
| **Situação/Requisito:** | **O cadastro de 'Áreas do conhecimento' não está permitindo a inclusão de uma área com código '0 - zero', o cadastro de áreas baseadas no CDU possui uma área com código 0 - Generalidades - porém o sistema não permite a inclusão desta área.** |
| **Solução/Implementação:** | **Foi feito um ajuste no cadastro de áreas, assim, quando o parâmetro "Utiliza área conhecimento integrada com CDU / CDD" (Parâmetros -> Controle do acervo -> Publicação) estiver marcado, o sistema irá permitir que seja inserido manualmente o valor do código da área (numérico), que não esteja em uso por outra área, ou seja, a geração do código da área não será sequencial, permitindo assim a inclusão do valor 0 - zero, porém este será validado para garantir que não esteja em uso, se o parâmetro não estiver marcado, continuará a geração automática sequencial do código da área.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVTSE3* |
| **Requisito (ISSUE):** | *N/A* |

divs
