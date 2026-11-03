---
content_hash: 17549a38fac01ae81f11454eeddf3446c8b050c37ea3e3120a007f6796c9b1fd
fetched_at: '2026-06-29T00:08:23.327935+00:00'
page_id: '270079414'
product: rm
source: tdn-rm
title: MRH-1457_DT_Processos_Juridicos
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-1457_DT_Processos_Juridicos
version: 112
---

# PROCESSOS JURÍDICOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Processos Jurídicos |
| **Situação/Requisito:** | No anexo de Depósitos Recursais, ao editar um registro e pesquisar o Cód Reclamado digitando um nome, nenhum registro estava sendo retornado, somente quando se digitava apenas o caractere "%". |
| **Solução/Implementação:** | Alteração do método SetSchema atribuindo a coluna correta para o atributo "Nome". Havia sido atribuída como VRECLAMADO.NUMPROCESSO, o que fazia a pesquisa buscar um valor de "NOME" na coluna "NUMPROCESSO". Agora está como GCOLIGADA.NOMEFANTASIA. Dessa forma a busca passa a filtrar corretamente pelo atributo "NOME". |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | MRH-1457 |
| **Requisito (ISSUE):** |  |

divs
