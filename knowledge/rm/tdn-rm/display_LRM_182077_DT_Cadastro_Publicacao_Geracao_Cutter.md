---
content_hash: b7253c1a30fa80b1008973ac79bfaed524f3559d1be55423a00954c6962617b0
fetched_at: '2026-06-29T00:08:23.749374+00:00'
page_id: '270090442'
product: rm
source: tdn-rm
title: 182077_DT_Cadastro_Publicacao_Geracao_Cutter
type: documentation
url: https://tdn.totvs.com/display/LRM/182077_DT_Cadastro_Publicacao_Geracao_Cutter
version: 112
---

# CADASTRO DE PUBLICAÇÕES - CUTTER

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Cadastro de publicações - CUTTER* |
| **Situação/Requisito:** | *Foi identificado que ao gerar o CUTTER de uma publicação no cadastro/edição de uma publicação, alguns tipos de autores não carregam os códigos corretamente, o sistema sempre considera somente o sobrenome, não considera após a vírgula e em alguns casos, exite por exemplo código para "FRANKLIN, M.", o sistema considera só o "FRANKLIN".* |
| **Solução/Implementação:** | *Foi feito um ajuste na função responsável por carregar o código do CUTTER para que caso o nome do autor esteja formato no padrão "SOBRENOME, NOME", o sistema considere o valor inicial para a busca do código como 'SOBRENOME, N.', assim, garantindo o código correto do autor para geração do CUTTER.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
