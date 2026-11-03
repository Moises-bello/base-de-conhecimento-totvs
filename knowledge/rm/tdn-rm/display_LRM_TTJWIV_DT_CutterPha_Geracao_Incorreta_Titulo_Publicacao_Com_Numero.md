---
content_hash: 7aba3144b2aa2867a95c300cb56f347a5eb9c01fefeb0d1851279106166b64f0
fetched_at: '2026-06-29T00:06:12.087412+00:00'
page_id: '204968303'
product: rm
source: tdn-rm
title: TTJWIV_DT_CutterPha_Geracao_Incorreta_Titulo_Publicacao_Com_Numero
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJWIV_DT_CutterPha_Geracao_Incorreta_Titulo_Publicacao_Com_Numero
version: 4
---

# CUTTER / PHA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Cutter / Pha* |
| **Situação/Requisito:** | **Ao gerar o Cutter / Pha de uma publicação cujo título começa com numeral, o sistema estava adicionado o primeiro caractere do título e adicionando ao final do cutter, sendo que quando é número, o sistema deve utilizar a primeira letra do numeral por extenso no idioma da publicação*.* |
| **Solução/Implementação:** | *Foi feito o ajuste na geração do cutter, ao identificar que a primeira palavra do título é um numeral, o sistema converte o numeral por extenso no idioma da publicação e retorna a primeira letra deste numeral em minúsculo.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
