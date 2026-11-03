---
content_hash: b0c6fdd434c4fa0cedb2fa50302fbae23f614002e6eb79ec51bf36de3251b5e8
fetched_at: '2026-06-29T00:08:10.857480+00:00'
page_id: '241697797'
product: rm
source: tdn-rm
title: TUZOUW_DT_Sefip_Mudanca_Mascara_Cei
type: documentation
url: https://tdn.totvs.com/display/LRM/TUZOUW_DT_Sefip_Mudanca_Mascara_Cei
version: 109
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Criação de rotina que faça atualização do CEI cadastrado no funcionário (PFRATEIOTOMADORES.CEI) conforme CEI cadastrado nos anexos do Cliente e Fornecedor -> CEI do Cliente / Fornecedor (FCFOCEI.CEI).  Após alteração na máscara do CEI, é necessário alterar a mesma no cadastro de Cliente / Fornecedor, porém a mesma não é alterada no cadastro do funcionário, fazendo com que o mesmo não seja levado na SEFIP. |
| **Solução/Implementação:** | *Alterado a Distribuição do Sefip para considerar o CEI da FCFOCEI quando tiver informado o ID do CEI.* |
| **Chamados relacionados:** | *TUZOUW* |

divs
