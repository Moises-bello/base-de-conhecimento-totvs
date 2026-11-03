---
content_hash: 9c34b8d6137dfa63eca074f05ad1e8fc81ad3088e08ea748e21fca40d7e4c3bc
fetched_at: '2026-06-29T00:08:12.010203+00:00'
page_id: '243633630'
product: rm
source: tdn-rm
title: TVDBHY_DT_Matricula_Sem_Período_Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243633630
version: 112
---

# MATRÍCULA NO PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Matrícula no período letivo* |
| **Situação/Requisito:** | *-    Durante a matrícula do aluno, quando o sistema está parametrizado para utilizar data contábil por contrato e não se escolhe um plano de pagamento, o sistema obriga que o período, a ser utilizado para o contrato, seja informado para que a matrícula possa prosseguir.*  *-    Durante a matrícula do aluno, quando o sistema está parametrizado para utilizar data contábil por contrato e se escolhe um plano de pagamento, o sistema utiliza o período contábil do plano de pagamento para o contrato do aluno. Por essa razão, uma mensagem apenas informativa é exibida ao usuário, informando-o que o plano não possui data contábil definida e orientando-o a preencher a data contábil ser utilizada para o contrato gerado, conforme acima.*  *-   Se um novo contrato é inserido, quando o sistema está parametrizado para utilizar data contábil por contrato, o sistema obriga que o período contábil seja informado e marca o controle de período contábil como manual. Sempre que o controle de período letivo é manual, o sistema insere informações log no contrato do aluno.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de matrícula, de forma a possibilitar a inclusão de contrato e a finalização do processo de matrícula, mesmo que o período de competência não tenha sido  definido e o sistema esteja parametrizado para utilizar a data de competência do contrato ou do plano de pagamento e a situação de matrícula exija contrato financeiro.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.12* |
| **Versão Corrigida:** | *12.1.12* |
| **Versão Expedida:** | *12.1.12* |

divs
