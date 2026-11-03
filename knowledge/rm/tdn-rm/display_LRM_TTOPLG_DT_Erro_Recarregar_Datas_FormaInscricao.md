---
content_hash: 3beabbbbbf998816c156992dee44415917353b8f844f111a15e799c9e9fd0f9a
fetched_at: '2026-06-29T00:06:22.443872+00:00'
page_id: '223918605'
product: rm
source: tdn-rm
title: TTOPLG_DT_Erro_Recarregar_Datas_FormaInscricao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOPLG_DT_Erro_Recarregar_Datas_FormaInscricao
version: 125
---

# FORMA DE INSCRIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Forma de Inscrição* |
| **Situação/Requisito:** | *Ao editar alguma forma de inscrição em um processo seletivo e ao pedir uma nova forma de inscrição dentro desse cadastro, o sistema não carrega as datas do processo seletivo.* |
| **Solução/Implementação:** | *Foi adicionado um evento para que ao clicar no botão para adicionar uma nova forma de inscrição o sistema recarregue as datas, pois o sistema só carregada no evento load da tela, que é executado somente na primeira vez que a tela é aberta. Assim ao criar uma nova forma de inscrição quando a tela já está aberta o sistema passou a carregar as datas do processo seletivo corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
