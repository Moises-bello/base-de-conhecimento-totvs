---
content_hash: 148fc7ce168ee47a48d59c711a370e822b16c030d81550a0aadbae2958b19fc9
fetched_at: '2026-06-29T00:08:11.388764+00:00'
page_id: '242391105'
product: rm
source: tdn-rm
title: TUZJ92_DT_Cancelamento_De_Ferias_Ao_Retirar_Permissao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUZJ92_DT_Cancelamento_De_Ferias_Ao_Retirar_Permissao
version: 112
---

# Cancelamento de Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cancelamento de férias* |
| **Situação/Requisito:** | *Ao retirar a permissão do processo de cancelamento de férias de um perfil de usuário, fazer log-off no sistema e em seguida logar com o usuário que possui o perfil que não tem mais permissão para acesso ao processo de cancelamento de férias, o usuário continua tendo acesso ao processo através do menu "Processos" dentro da visão de Período de Gozo. O botão de cancelamento de férias na MDI fica desativado normalmente.* |
| **Solução/Implementação:** | *Verificar a segurança do formulário ao abrir a tela, para evitar buscar o valor que está em cache na segurança da Lib.* |
| **Chamados relacionados:** | *TUZJ92, TVDPTL* |

divs
