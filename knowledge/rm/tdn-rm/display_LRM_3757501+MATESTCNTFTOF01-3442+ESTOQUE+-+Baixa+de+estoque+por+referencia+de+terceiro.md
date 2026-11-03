---
content_hash: 289fe31670b6a3df8782ea70592fa507d44fce5f22cc73721a29c3294a888c78
fetched_at: '2026-06-29T00:09:54.957440+00:00'
page_id: '445668972'
product: rm
source: tdn-rm
title: 3757501 MATESTCNTFTOF01-3442 ESTOQUE - Baixa de estoque por referencia de terceiro
type: documentation
url: https://tdn.totvs.com/display/LRM/3757501+MATESTCNTFTOF01-3442+ESTOQUE+-+Baixa+de+estoque+por+referencia+de+terceiro
version: 3
---

# CÓPIA POR REFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Função:** | Cadastro de Movimento, Cópia por Referência |
| **Situação/Requisito:** | Ao usar o assistente de copia por referencia para o movimento (2.2.99 - Estoque de Terceiros), não é mostrado os lotes do item para efetuar a baixa, mesmo o item tendo estoque e lotes com saldo para isso. |
| **Solução/Implementação:** | Garantir que o lote do item de movimento é mostrado quando o tipo de movimento na qual o movimento está associado está parametrizado com o efeito de diminuir o lote de terceiros; e este lote tem saldo positivo. |
| **Conversores e Parâmetros:** | Parametrização para o tipo de movimento para o cenário :  1. No aplicativo de Gestão de Estoque, Compras e Faturamento, siga para Parâmetros em Ambiente e clique em Gestão de Estoque, Compras e Faturamento    2. Clique em Gestão de Estoque e avance  3. Em Tipo de Movimento selecione o tipo de movimento que quer parametrizar para o cenário conhecido e clique no ícone Parametrizar. Ao abrir a tela de processo para parametrizar avance.  4. Selecione o Estoque - Estoque 2/3 e parametrize o atributo do tipo de movimento Efeito Sobre o Saldo de Terceiros para Diminui  5. Avance e finalize para parametrizar. |
| ***Tickets* relacionados:** | 3757501 |
