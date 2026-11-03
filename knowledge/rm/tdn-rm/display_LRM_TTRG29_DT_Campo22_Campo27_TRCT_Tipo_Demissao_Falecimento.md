---
content_hash: d41d6bf31839026ec546bd5fd0ae701228d6ea4d01c6ae47bc81e9d55e1cb65f
fetched_at: '2026-06-29T00:06:20.446374+00:00'
page_id: '223151929'
product: rm
source: tdn-rm
title: TTRG29_DT_Campo22_Campo27_TRCT_Tipo_Demissao_Falecimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTRG29_DT_Campo22_Campo27_TRCT_Tipo_Demissao_Falecimento
version: 1
---

# TRCT - CAMPOS 22 E 27 IGUAL A FT1 QUANDO TIPO DEMISSÃO FOR IGUAL A 8 OU F

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gerar TRCT de acordo com a Portaria 1.057* |
| **Situação/Requisito:** | Ao gerar o relatório TRCT para um funcionário que esta sendo demitido devido ao falecimento do mesmo, verificamos que o campo 22 e 27 somente é preenchido corretamente quando a rescisão é do tipo 8 - Falecimento. Mas conforme uma consulta na tabela PTPDEMISSAO, existem mais 2 tipos de rescisões por falecimento (F e P). Quando realizada a rescisão para estes tipos, o campo 22 é gerado sem a informação e o campo 27 incorretamente conforma dados da portaria 1057. |
| **Solução/Implementação:** | Realizado ajuste para que seja apresentado no campo 22 – Causa do afastamento (FT1) e campo 27 – Cód. Afastamento (Rescisão do contrato de trabalho por falecimento do empregado) quando o tipo de rescisão for igual a "F - Falecimento p/ acidente de trabalho" Ou "8 - Falecimento" Ou "P - Falecimento p/ doenca profissional". |
| **Chamados relacionados:** | TTRG29 |
| **Versões/Release:** | *11.82.43* |

divs
