---
content_hash: 5b087ae7e24df0bef9fed5afdc94cb196ca39b00ab96a16766f81a3446ec28b4
fetched_at: '2026-06-29T00:06:26.286510+00:00'
page_id: '224457832'
product: rm
source: tdn-rm
title: TUFJPP_Exclusao_Local_Prova_Candidato_Persiste_Registro_Presenca
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFJPP_Exclusao_Local_Prova_Candidato_Persiste_Registro_Presenca
version: 120
---

# ALTERAÇÃO DE LOCAL DE PROVA DO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Alteração de local de prova do candidato* |
| **Situação/Requisito:** | *Quando um local de prova é alterado ou removido de um candidato que já possui registro de presença neste local, o sistema altera ou apaga corretamente o local de prova, porém mantém o registro de presença do candidato, gerando inconsistências na base de dados no momento de importar o gabarito.* |
| **Solução/Implementação:** | *Foi identificado que o sistema só estava tratando a exclusão do registro de presença quando o candidato tinha seu local de prova alterado e não excluído, foi feito o ajuste para que tanto na alteração ou exclusão do local de prova o sistema exclua também o registro de presença vinculado ao candidato.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUHCB8* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.43*  *12.1.10* |
| **Versão Expedida:** | *11.82.43*  *12.1.10* |

divs
