---
content_hash: 50aafb0b9aed15720daa9e0e690b6a9d80492a9cbce35982f0d68ac4d9adefa4
fetched_at: '2026-06-29T00:08:03.896554+00:00'
page_id: '235328781'
product: rm
source: tdn-rm
title: TUOYCP_DT_CPF_Obrigatorio_Candidato_Estrangeiro_Pametro_Obrigatorio
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOYCP_DT_CPF_Obrigatorio_Candidato_Estrangeiro_Pametro_Obrigatorio
version: 114
---

# CADASTRO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cadastro de candidato* |
| **Situação/Requisito:** | *Foi identificado que na primeira tela de cadastro de candidatos pelo portal, ao informar um candidato estrangeiro a obrigatoriedade do CPF é removida corretamente, porém ao prosseguir para a tela do cadastro completo o sistema volta a tornar o CPF como obrigatório.* |
| **Solução/Implementação:** | *Foi identificado que este ocorre somente quando o parâmetro "Utilizar parametrização do campos da guia 'Documentos' sem exigir obrigatoriedade" está marcado, foi feito o ajuste no javascript que define a obrigatoriedade de documentos quando este parâmetro está marcado e assim a obrigatoriedade de CPF passou a funcionar como o esperado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
