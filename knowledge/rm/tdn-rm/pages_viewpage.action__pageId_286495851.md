---
content_hash: 6051efaad6f684f183605b0783950b6ee36bb2a60e75196ee028486be8297323
fetched_at: '2026-06-29T00:08:40.706427+00:00'
page_id: '286495851'
product: rm
source: tdn-rm
title: 1000735 MSAU-13332 DT Parâmetro Restringe Unidade de Atendimento para Demais
  Rotinas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286495851
version: 104
---

# Parâmetro de restringe unidade de atendimento para demais rotinas

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Leitos |
| **Situação:** | Ao restringir unidades de atendimento para o perfil do usuário, no cadastro do leito quando o usuário pesquisava por leitos, em algumas unidades não eram exibidos os leitos, mesmo o usuário tendo acesso a determinadas unidades de atendimento. |
| **Solução:** | Alterado a busca que era feita na tela de leitos e controle de ocupação, que buscava pela unidade vinculada ao mesmo centro de custo do leito e restringia os leitos que eram exibidos, foi removido esse vínculo e feito a ligação do leito diretamente com a unidade de atendimento, exibindo assim todos os leitos corretamente. |

divs
