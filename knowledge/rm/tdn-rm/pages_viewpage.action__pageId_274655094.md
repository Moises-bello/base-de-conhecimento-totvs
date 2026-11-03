---
content_hash: b2a278bcb449780f23caef91208f63cfba90712134e73150785e31fbc7463a8c
fetched_at: '2026-06-29T00:08:34.250231+00:00'
page_id: '274655094'
product: rm
source: tdn-rm
title: 566980 FOPROTINAS01-61 DT Importação de Campos Complementares de Dependente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274655094
version: 94
---

# IMPORTAÇÃO DE DADOS DO RM LABORE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Importação de Dados do RM Labore |
| **Situação/Requisito:** | Ao tentar importar campos complementares de dependente através do processo de importação de dados do RM Labore, o sistema obrigava que o usuário informasse todos os campos complementares, mesmo se quisesse alterar apenas 1. |
| **Solução/Implementação:** | Replicar a alteração de campos complementares de funcionário, permitindo que o usuário informe apenas os campos que deseja alterar.  Para alterar os campos complementares do dependente, basta informar na primeira linha do arquivo:  CHAPA;NRODEPEND;NOME\_DO\_CAMPO\_A\_SER\_ALTERADO  E nas linhas posteriores, as informações desejadas. |
| **Tickets relacionados:** | 566980 |

divs
