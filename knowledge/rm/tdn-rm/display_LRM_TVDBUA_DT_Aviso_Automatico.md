---
content_hash: b6ab373bf71a8fd04682bf1ec8e7daceeda30eba7bd9eb4ecd7485cf3aa15a46
fetched_at: '2026-06-29T00:08:13.257502+00:00'
page_id: '243658833'
product: rm
source: tdn-rm
title: TVDBUA_DT_Aviso_Automatico
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDBUA_DT_Aviso_Automatico
version: 115
---

# AVISO AUTOMÁTICO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Aviso Automático* |
| **Situação/Requisito:** | O sistema não dispara e-mail referente ao processo de avisos automáticos, do tipo 7 Solicitação alteração dados bancários. Porém gera, indevidamente, aviso para o tipo 8 -Confirmação alteração dados bancários, mesmo que os dados não tenham sido aprovados. |
| **Solução/Implementação:** | Ajuste na rotina de Aviso Automático para gerar registro corretamente de Solicitação de aprovação de dados bancários (7) e Confirmação de alteração de dados bancários para envio de aviso automático. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVDBUA TVGHDD |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.45 12.1.13* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
