---
content_hash: 6a0f1f0122ef19d1b305d25228e88c3df7c58895824042d77820c7f8c6b9c71e
fetched_at: '2026-06-29T00:06:06.891734+00:00'
page_id: '201733101'
product: rm
source: tdn-rm
title: TTDAK2_DT_Exclusao_Matricula_Periodo_Letivo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDAK2_DT_Exclusao_Matricula_Periodo_Letivo
version: 1
---

# EXCLUSÃO DE MATRÍCULA DO PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Exclusão de matrícula do período letivo* |
| **Situação/Requisito:** | *Após executar o processo: Mudar turma/Turno, o sistema não permite excluir a matrícula do aluno no Período Letivo. Conforme a rejeição do chamado: TTBBFR , foi identificado que o erro ocorre porque o sistema tenta excluir SHABILITACAOALUNO sem excluir SHABILITACAOALUNOCOMPL, e isto somente para o ensino básico, que, a priori, não utiliza campo complementar para habilitação do aluno. Observação: O erro também ocorre para o nível de Ensino Superior, porém ocorre ao clicar no botão excluir da tela de cadastro da matrícula do período letivo do aluno.* |
| **Solução/Implementação:** | *Ajuste no data server da habilitação do aluno para que seja inserido os dados dos campos complementares da habilitação do aluno apenas para o nível superior. Além disso, ao se excluir uma matrícula de um aluno, seja excluído também os campos complementares da habilitação do aluno em questão. Já no nível superior ao excluir uma matrícula pela tela de cadastro da matrícula, ajuste feito na validação de datas, que não deverá ser realizada ao excluir a matrícula.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7 e 12.1.8* |
