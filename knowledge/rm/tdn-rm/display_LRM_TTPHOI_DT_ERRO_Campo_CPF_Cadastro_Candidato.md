---
content_hash: 9bffcf6aac166ba342c27cea3a612f7af50c88d0af0f100cbbb588dca7a2eb34
fetched_at: '2026-06-29T00:06:16.445418+00:00'
page_id: '212898412'
product: rm
source: tdn-rm
title: TTPHOI_DT_ERRO_Campo_CPF_Cadastro_Candidato
type: documentation
url: https://tdn.totvs.com/display/LRM/TTPHOI_DT_ERRO_Campo_CPF_Cadastro_Candidato
version: 1
---

# CADASTRO DE CANDIDATOS (PORTAL)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Cadastro de Candidato (Portal)* |
| **Situação/Requisito:** | *Ao tentar realizar a inscrição de um candidato no processo seletivo, utilizando a opção responsável pelo candidato, o campo CPF desaparece após selecionar o estado natal com isso o usuário fica impossibilitado prosseguir com a inscrição.* |
| **Solução/Implementação:** | *O método responsável por validar a visibilidade do CPF no cadastro de candidato, estava com uma incoerência que o fazia validar apenas para cadastro de candidato. Quando o cadastrado estivesse sendo realizado através de um responsável, o campo ficava com um comportamento inesperado.*  *Foi ajustado a validação realizada neste método, permitindo validar corretamente os valores informados nos parâmetros do sistema.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *Versão na qual está sendo feita a manutenção deste programa.* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs
