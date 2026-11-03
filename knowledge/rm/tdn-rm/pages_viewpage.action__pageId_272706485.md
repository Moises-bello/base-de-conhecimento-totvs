---
content_hash: 85a135afbb36272cea237d1599e6eab8f6e51e7cbbf53efe10cb30ec7506dd5c
fetched_at: '2026-06-29T00:08:30.953764+00:00'
page_id: '272706485'
product: rm
source: tdn-rm
title: 519451 MATFATCMPCRM01-79 DT Atribuir Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272706485
version: 110
---

# ATRIBUIR PREÇO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Atribuir Preço. |
| **Situação/Requisito:** | Ao realizar baixa de matéria prima no processo produtivo simples alterando o local de estoque, o custo copiado para o preço não é atualizado. |
| **Solução/Implementação:** | Ao faturar o movimento o serviço de Buscar Preço Default do Produto preencherá a informação de local de estoque conforme configuração de local de estoque do tipo de movimento. Se a configuração do local de estoque for por item de movimento então será utilizado no serviço o local de estoque do item senão será utilizado o local de estoque do movimento para buscar o preço do produto.  Como em movimentos do processo produtivo simples, ao faturar ele expande as estruturas, foi necessário disponibilizar o botão Atribuir preço aos itens selecionados. |
| **Conversores e Parâmetros:** | O botão **Atribuir preço aos itens selecionados** ficará visível quando o tipo de movimento estiver configurado para Buscar Preço Em diferente de Nenhum Preço e Edição do Preço for igual a Edita ou Mostra. (Etapa Item - Preços 1/2). |
| **Tickets relacionados:** | 519451 |
| **Requisito:** | MATFATCMPCRM01-79. |

divs

## Procedimento para Utilização

1. Na tela de Edição do Movimento acesse a pasta Itens.
2. Selecione os itens cujo o preço serão alterados e clique no botão Atribuir preço aos itens selecionados.
3. Na janela apresentada informe a Seleção de Preço e clique no botão OK
