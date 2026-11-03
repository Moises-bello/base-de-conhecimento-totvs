---
content_hash: 1971adca468f6f7e2bfe471f5676bc1526a9c6478624b4705ba6fd57ceb453ae
fetched_at: '2026-06-29T00:08:11.206760+00:00'
page_id: '241701980'
product: rm
source: tdn-rm
title: TVBQCC_DT_Termo_Aceite_Nao_Altera_Apos_Primeira_AreaOfertada
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBQCC_DT_Termo_Aceite_Nao_Altera_Apos_Primeira_AreaOfertada
version: 111
---

# TERMO DE ACEITE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Área de interesse ofertada - termo de aceite* |
| **Situação/Requisito:** | *Ao tentar inscrever um candidato em um PS, onde existe mais de uma área ofertada, onde, uma área possui Termo de Aceite e a outra não(Texto Padrão), ao selecionar a área ofertada que possui termo de aceite, o texto do termo de aceite muda corretamente em seguida ao selecionar alguma outra área ofertada que tenha o texto padrão, o texto de termo de aceite não altera para o padrão.* |
| **Solução/Implementação:** | *Foi identificado que o javascript responsável pela alteração, após a primeira seleção de área, o mesmo não estava tratando a alteração quando o termo de aceite da área está vazio, ou seja, utilizaria o padrão. Foi feito o ajuste para que se a área ofertada não tem termo de aceite, é definido o padrão.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVDHS9* |
| **Requisito (ISSUE):** | *N/A* |

divs
