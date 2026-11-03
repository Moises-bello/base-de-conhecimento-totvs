---
content_hash: 151fda54edd1db7e4b2fa529f45c3f9ca66344b06543e4f369eba7c2bb418f04
fetched_at: '2026-06-29T00:08:45.788678+00:00'
page_id: '315891298'
product: rm
source: tdn-rm
title: 1452280 EDUCACIONAL01-2779 DT Censo - Cadastro de cursos do MEC de origem na
  habilitação do aluno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315891298
version: 95
---

# CADASTRO CURSO MEC ORIGEM NA HABILITAÇÃO DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Censo - Cadastro curso MEC origem na habilitação do aluno |
| **Situação/Requisito:** | Ao filtrar os cursos MEC para cadastro na habilitação o curso de origem, o sistema buscava informações da tabela de habilitação e não da Cursos MEC. |
| **Solução/Implementação:** | Foi realizado um ajuste que redireciona a busca para a tabela de cursos do MEC, cadastrada no anexo de Instituição do MEC.  Agora, serão retornados todos os cursos cadastrados, que estejam vinculados a alguma matriz aplicada, e que sejam diferente do curso atual.  Os cursos serão filtrados pela instituição de ensino definida para o contexto, conforme parametrização por filial ou nível de ensino. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
