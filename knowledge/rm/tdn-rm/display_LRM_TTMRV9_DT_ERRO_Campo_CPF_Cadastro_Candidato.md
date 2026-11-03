---
content_hash: 0547fb992b5baebe7cbcf79152c71fb5638b8a3a69c751db0f14efd2b07d3242
fetched_at: '2026-06-29T00:06:16.399820+00:00'
page_id: '212897370'
product: rm
source: tdn-rm
title: TTMRV9_DT_ERRO_Campo_CPF_Cadastro_Candidato
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMRV9_DT_ERRO_Campo_CPF_Cadastro_Candidato
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
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *Versão na qual está sendo feita a manutenção deste programa.* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs
