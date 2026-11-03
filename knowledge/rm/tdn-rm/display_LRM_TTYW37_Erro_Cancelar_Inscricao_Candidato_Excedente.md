---
content_hash: a367c4111d7798c432fa3eca49fa68c4b44f0b30d1bb17117a3338d0995dd313
fetched_at: '2026-06-29T00:06:22.968521+00:00'
page_id: '223926511'
product: rm
source: tdn-rm
title: TTYW37_Erro_Cancelar_Inscricao_Candidato_Excedente
type: documentation
url: https://tdn.totvs.com/display/LRM/TTYW37_Erro_Cancelar_Inscricao_Candidato_Excedente
version: 122
---

# CANCELAMENTO DE INSCRIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cancelamento de Inscrição* |
| **Situação/Requisito:** | *Quando o processo seletivo utiliza controle de vagas, ao tentar cancelar uma inscrição para que o próximo excedente se torne candidato e gere o lançamento financeiro o sistema retorna um erro e não conclui o processo.* |
| **Solução/Implementação:** | *O erro é causado pois a data de emissão do lançamento consta como a data de inscrição do candidato que já estava fora do período mínimo permito para os lançamentos, sendo assim foi feito o ajuste para que a data de emissão do lançamento seja a data atual no momento da operação que gera o lançamento, sendo que a data atual só é considerada quando o lançamento for gerado para um candidato que é excedente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TU5852 |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.9* |
| **Versão Corrigida:** | *11.82.43*  *12.1.9* |
| **Versão Expedida:** | *11.82.43*  *12.1.9* |

divs
