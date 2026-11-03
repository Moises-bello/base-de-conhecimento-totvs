---
content_hash: 414d34ba7ca35e19e60eff05c1be950da7e81621da8dcdfd1d63aa2295da2bfb
fetched_at: '2026-06-29T00:08:10.850861+00:00'
page_id: '241697367'
product: rm
source: tdn-rm
title: TVBTAW_DT_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBTAW_DT_Rescisao
version: 110
---

# RESCISÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Rescisão |
| **Situação/Requisito:** | Ao tentar cadastrar uma rescisão para um funcionário, o sistema apresenta mensagem informando que que existe uma coluna definida de maneira ambígua, o que impede o cadastro da rescisão. |
| **Solução/Implementação:** | Alteração na consulta responsável por verificar se o funcionário possui movimento em meses posteriores à competência. |
| **Chamados relacionados:** | TVBTAW |

divs
