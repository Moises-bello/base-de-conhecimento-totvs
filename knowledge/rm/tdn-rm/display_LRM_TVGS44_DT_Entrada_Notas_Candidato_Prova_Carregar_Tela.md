---
content_hash: 2fc9cf121eeb4384835ff047fcfea9eccd16d85bc31e94cb8103c586e17726d8
fetched_at: '2026-06-29T00:08:13.385747+00:00'
page_id: '244418117'
product: rm
source: tdn-rm
title: TVGS44_DT_Entrada_Notas_Candidato_Prova_Carregar_Tela
type: documentation
url: https://tdn.totvs.com/display/LRM/TVGS44_DT_Entrada_Notas_Candidato_Prova_Carregar_Tela
version: 116
---

# ENTRADA DE NOTAS DE CANDIDATOS POR PROVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Avaliação e Pesquisa* |
| **Função:** | *Entrada de notas de candidatos por prova* |
| **Situação/Requisito:** | *Ao utilizar a opção de entrada de notas de candidatos por prova, o sistema retorna um erro de chave de registro duplicada e não carrega corretamente a tela.* |
| **Solução/Implementação:** | *Foi identificado que o erro era causado por uma diferença no tamanho dos campos da base de dados com a tela, na base de dados o campo "nome" (PPESSOA.NOME) aceita ate 120 caracteres, porém a tela aceita somente 65, quando o nome que está na base tem mais de 65 caracteres ocorre o erro. Foi feito o ajuste no campo da tela para que fique igual ao da base de dados e solucione o erro.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVGZPH* |
| **Requisito (ISSUE):** | *N/A* |

divs
