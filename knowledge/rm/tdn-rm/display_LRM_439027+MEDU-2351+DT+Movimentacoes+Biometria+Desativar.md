---
content_hash: 43472bbd6a609fff0d2a089f82c1f8fa60b4bf2a12635d92fee57f13b0f31915
fetched_at: '2026-06-29T00:08:27.266823+00:00'
page_id: '271404370'
product: rm
source: tdn-rm
title: 439027 MEDU-2351 DT Movimentacoes Biometria Desativar
type: documentation
url: https://tdn.totvs.com/display/LRM/439027+MEDU-2351+DT+Movimentacoes+Biometria+Desativar
version: 109
---

# MOVIMENTAÇÕES - BIOMETRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentações - biometria* |
| **Situação/Requisito:** | *Ao selecionar na tela de movimentações a aba de leitura biométrica o sistema sempre retorna um erro informando falha no dispositivo ou no driver, porém nesta situação o leitor biométrico não é utilizado pela instituição, o que em uma operação diária de movimentações gera grandes transtornos pois se clicar indevidamente na aba o erro é exibido todas as vezes que a aba for selecionada.* |
| **Solução/Implementação:** | *Foi criado um parâmetro para as definições de usuário para que seja ativada ou não a função biométrica, por padrão a biometria sempre ficará ativada, porém se for desativado nos parâmetros, a aba de movimentações não será exibida mais na tela de movimentações, evitando assim que ao clicar indevidamente o erro fique aparecendo na tela e incluindo mais um clique nas operações de movimentações. Foi incluído também para os itens de usuários e reservas uma mensagem de alerta informando que a biometria está desativada ao selecionar a biometria.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
