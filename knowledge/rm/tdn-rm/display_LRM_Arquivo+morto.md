---
content_hash: c925c5508dcd1fa6dc2d7cd0aa6f83be52ea884062b07c0036bb53ac5a3eac3a
fetched_at: '2026-06-29T00:12:06.923660+00:00'
page_id: '918394168'
product: rm
source: tdn-rm
title: Arquivo morto
type: documentation
url: https://tdn.totvs.com/display/LRM/Arquivo+morto
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Arquivar Movimentações de Estoque**
4. **Restaurar Movimentações de Estoque**

sumarioVisão Geral

## **01. VISÃO GERAL**

Os registros de movimentação de estoque são consideravelmente volumosos, pois cada item requisitado gera um novo registro. Neste cenário é possível que a tabela de registros fique muito povoada e gere uma certa degradação na performance do módulo de movimentação de estoque.

Para minimizar esta situação foi desenvolvido o processo de arquivamento de registros. Nele o Administrador define um intervalo de data e todos os registros contidos neste serão removidos da tabela ativa e armazenados uma tabela de backup, gerando um "arquivo-morto" dos registros para poderem ser consultados e até mesmo restaurados para as tabela ativa em casos de auditoria, por exemplo.

Desta forma, podemos reduzir o tamanho da tabela e assim melhorar o desempenho das buscas, deixando de fora registros muito antigos que não são necessários nas atividades diárias.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

1. No menu, acesse **Farmácia > Arquivo Morto**.
2. Na tela do **Arquivo Morto**, você poderá visualizar todas as movimentações de estoque que foram arquivadas.
3. Para arquivar ou restaurar os dados, acesse o menu **Processos (1)** e selecione a ação desejada.

Arquivar Movimentações de Estoque

1. Ao acessar **Processos > Arquivar Movimentações de Estoque**, selecione o período desejado. Todos os registros referentes ao período selecionado serão movidos automaticamente para as tabelas de arquivamento.  
    Clique em **Executar** para confirmar a ação.
2. Ao executar, os arquivos serão movidos das tabelas de uso para suas respectivas tabelas de arquivamento.
Restaurar Movimentações de Estoque

# Restaurar Movimentações de Estoque

1. Ao acessar **Processos > Restaurar Movimentações de Estoque,** selecione o período desejado. Todos os registros referentes ao período selecionado serão movidos automaticamente para as tabelas de arquivamento.  

   Clique em Executar para confirmar a ação.
2. Ao executar, os arquivos serão restaurados para o seu local de origem.
