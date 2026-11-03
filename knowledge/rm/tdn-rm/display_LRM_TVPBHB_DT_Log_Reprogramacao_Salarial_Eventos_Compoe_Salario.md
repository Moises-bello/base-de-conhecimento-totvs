---
content_hash: 9dc025813e5317f7fbbdcee01efeebb0d966c0d7be80b8fa9d346674cd8dfaee
fetched_at: '2026-06-29T00:08:16.405779+00:00'
page_id: '245171728'
product: rm
source: tdn-rm
title: TVPBHB_DT_Log_Reprogramacao_Salarial_Eventos_Compoe_Salario
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPBHB_DT_Log_Reprogramacao_Salarial_Eventos_Compoe_Salario
version: 112
---

# REPROGRAMAÇÃO SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Reprogramação Salarial* |
| **Situação/Requisito:** | Ao gerar Reprogramação salarial é emitido erro:     Não é permitido associar o mesmo evento em atividades que compõe e outra que não compõe salário.     Atividades Encontradas:        - Atividade Extra associada ao evento [0002]        - Atividade Aula associada ao evento [0002]        Essa validação passou a ser executada a partir da 12.1.12 mas não discrimina claramente qual atividade na mensagem de erro e nem funcionário.     Verificado que o evento 0002 está associado a dois grupos de atividade 20 e 26, mas ambos não compõem salário. |
| **Solução/Implementação:** | *Alterado o log para informar qual o funcionário e quais atividades que compõe ou não compõe salário.*  *Exemplo:*  Professor: XXXXX - NOME PROFESSOR     Não é permitido associar o mesmo evento em atividades que compõe e outra que não compõe salário. Atividades Encontradas: Atividades que compõe salário:  - Atividade Extra associada ao evento [0002] - Data Início da Atividade 01/01/2015  - Atividade Aula - Turma CODIGO TURMA 1 associada ao evento [0002]- Data Início da Atividade 01/01/2015 Atividades que não compõe salário:  - Atividade Aula - Turma CODIGO TURMA 2 associada ao evento [0002]- Data Início da Atividade 01/01/2015 |
| **Chamados relacionados:** | *TVPBHB* |

divs
