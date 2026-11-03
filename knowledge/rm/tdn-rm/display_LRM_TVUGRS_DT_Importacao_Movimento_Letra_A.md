---
content_hash: 17eff1d102f16730e959b5fef2fb96722f68a78c04980a6c5da84a12e8841b8a
fetched_at: '2026-06-29T00:08:18.878189+00:00'
page_id: '266972697'
product: rm
source: tdn-rm
title: TVUGRS_DT_Importacao_Movimento_Letra_A
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUGRS_DT_Importacao_Movimento_Letra_A
version: 112
---

# Importação de Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Importação de Movimento* |
| **Situação/Requisito:** | Devido a migração do processo de "Importação de Movimento" para .Net, o mesmo passou a ser realizado através de Conceito e foi necessário alterar a Ordem da linha de prefixo "A", a qual é responsável por forçar a validação da coligada. |
| **Solução/Implementação:** | Durante a importação de movimentos através de arquivo texto, caso seja necessária a consistência da coligada dos movimentos importados, acrescente a linha abaixo no layout de Movimentos. Esta linha é opcional , o usuário deverá acrescentá-la manualmente, **abaixo** da linha M.  Linha de Dados da Coligada    ***Importante***: A linha de prefixo "A" passa a ser por Movimento, ou seja, na importação em Delphi a mesma era inserida no cabeçalho do arquivo e todos os movimentos à compartilhavam, a partir de agora, será necessário informá-la para cada movimento contido no arquivo. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
