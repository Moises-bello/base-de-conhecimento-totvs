---
content_hash: 01dd0b7dc2c86c03dc8c32225ef58126ea5b4bf9b667444a3d480f96d874f7ae
fetched_at: '2026-06-29T00:06:30.344488+00:00'
page_id: '235320053'
product: rm
source: tdn-rm
title: TULRRL_DT_BOTAO_MULTIPLOS_TOTVS_COLAB
type: documentation
url: https://tdn.totvs.com/display/LRM/TULRRL_DT_BOTAO_MULTIPLOS_TOTVS_COLAB
version: 118
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Função:** | *Inclusão Manual de Movimentos via XML (Totvs Colaboração)* |
| **Situação/Requisito:** | Na inclusão de movimento via XML manual, o sistema considera o parâmetro de recebimento NF-e automático;  Além disso, Na seguinte situação o botão Múltiplos não funciona;  1) Fornecedor configurado para recebimento de pedido.  2) XML com 2 itens, sendo que o primeiro tem quantidade 100 no XML e dois pedidos na base, cada um com quantidade 50 para o item;  3) Ao incluir o movimento via xml, o sistema traz os dois pedidos e na tradução, vincula o item com 100 ao primeiro pedido, porém esse só tem 50.  4) Ao clicar no botão múltiplo para criar a réplica do produto, o sistema exibe a mensagem Este produto não possui saldo disponível para um novo vínculo, estando esse comportamento incorreto, porque não há 100 no pedido 000006;  5) Se continuo o processo, o movimento é aberto e no item fica com a quantidade 100, porém ao salvar, o sistema exibe o erro |
| **Solução/Implementação:** | Melhoria no processo de Inclusão de movimento via XML, para funcionamento do botão Multiplos. O parâmetro foi desconsiderado nesse processo. |
| **Conversores e Parâmetros:** | *12.1.10 e superiores* |
| **Chamados relacionados:** | TULRRL |
| **Requisito (ISSUE):** | MOV000161 - TOTVS Colaboração |

divs
