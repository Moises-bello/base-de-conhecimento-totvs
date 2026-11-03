---
content_hash: 805563e4b2241c95c5701fea233c2224d59c746eb28e82cb5132cc5b782de5a3
fetched_at: '2026-06-29T00:08:18.590924+00:00'
page_id: '265782640'
product: rm
source: tdn-rm
title: TVVCEH_DT_2Via_Comprovante_Integrado_Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/TVVCEH_DT_2Via_Comprovante_Integrado_Boleto
version: 115
---

# 2ª VIA DE COMPROVANTE - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *2ª via de comprovante - portal* |
| **Situação/Requisito:** | *Ao utilizar o parâmetro "Relatório de boleto e comprovante integrado", ao acessar a opção de 2ª via de comprovante no portal e gerar o comprovante, o boleto não é gerado.* |
| **Solução/Implementação:** | **Foi identificado que o que define além do parâmetro marcado é necessário que o código do lançamento gerado seja passado também, e a passagem do código do lançamento via parâmetro estava incorreto, foi feito o ajuste e o boleto passou a ser gerado corretamente junto com comprovante de inscrição.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
