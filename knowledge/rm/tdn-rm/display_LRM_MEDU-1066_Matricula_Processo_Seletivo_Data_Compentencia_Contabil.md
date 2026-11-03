---
content_hash: bb01e54c56148bd42c6c75959fe596d0803ff356eeeea9fabed1be4f14b0e809
fetched_at: '2026-06-29T00:08:22.198677+00:00'
page_id: '269083036'
product: rm
source: tdn-rm
title: MEDU-1066_Matricula_Processo_Seletivo_Data_Compentencia_Contabil
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1066_Matricula_Processo_Seletivo_Data_Compentencia_Contabil
version: 109
---

# Matricula Processo Seletivo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Matricula Processo Seletivo |
| **Situação/Requisito:** | Quando o sistema está parametrizado para utilizar data contábil por Contrato/Pl, ao matricular o aluno pelo 'Processo seletivo' e a situação de matrícula exige contrato, o sistema está exigindo que se informe a data contábil.  Foi feito um ajuste no processo de Matrícula do sistema, através do chamado TVDBHY, para que seja possível prosseguir com a matrícula sem a definição do período contábil e também ajuste na validação ao inserir um contrato sem a indicação da data contábil. Neste momento o sistema apenas apresentará uma mensagem de alerta sobre a ausência da data contábil, mas não impede que o processo seja concluído. A falta da data em questão somente será impeditiva para a realização da contabilização propriamente dita. |
| **Solução/Implementação:** | Baseado no cenário acima ajustamos a validação que impedia o prosseguimento do processo se a data de competência não fosse preenchida, pois agora será apresentada uma mensagem alertando o usuário. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | MEDU-1066 |
| **Requisito (ISSUE):** | *N/A* |

divs
