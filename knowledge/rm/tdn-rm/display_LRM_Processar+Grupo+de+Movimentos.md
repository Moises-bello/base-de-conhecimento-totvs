---
content_hash: 0246a8dc6102b7974fac1038fa867e678346a14949a6a8e6d902e985c0372f0a
fetched_at: '2026-06-29T00:09:29.117291+00:00'
page_id: '423938814'
product: rm
source: tdn-rm
title: Processar Grupo de Movimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Processar+Grupo+de+Movimentos
version: 2
---

Este processo é utilizado para que os movimentos possam ser criados sem a geração de suas possíveis integrações: Contabilidade, Financeiro e Estoque.   
Sendo assim, um movimento criado com status 'Não Processado' existirá apenas como documentação, sem qualquer efeito sobre o sistema.   
Esta rotina é muito utilizada quando a Empresa tem um 'espelho' do documento fiscal, porém aguarda a chegada 'física' deste documento, para seu devido efeito.   
Esta rotina somente estará disponível caso o tipo de movimento esteja parametrizado para 'Criar Mov. com status "Não Processado".   
Com este parâmetro habilitado, o movimento já é criado com o status "Não Processado", necessitando da interação do Usuário para que as suas integrações e rotinas sejam executadas: efeito Contábil, Financeiro e no Estoque dos Produtos.  
Selecionando o movimento desejado e executando esta rotina, o sistema fará a baixa no estoque dos itens, desde que esteja parametrizado para que algum dos saldos 'Aumente' ou 'Diminua' estoque e o seu status será alterado para "A Faturar" ou "Pendente".
