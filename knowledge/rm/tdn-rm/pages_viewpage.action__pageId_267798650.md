---
content_hash: 98b7d16c83b1bef698edf3bb8a4c05428bd8ca6dfe9e37947ae4cb3d37af0f5e
fetched_at: '2026-06-29T00:08:19.929234+00:00'
page_id: '267798650'
product: rm
source: tdn-rm
title: TVV627_DT_Transferência_Retroativa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267798650
version: 112
---

# RESCISÃO - TRANSFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão - Transferência* |
| **Situação/Requisito:** | *Ao realizar uma Transferência com data do mês anterior e tendo o funcionário movimento no mês atual, ao avançar o sistema emite a mensagem abaixo impedindo prosseguir:*  *"Funcionário 124889 possui movimentação lançada em meses posteriores à data de demissão, a rescisão não poderá ser processada."*  *Estão marcados os parâmetros de:*  *"Permite realizar rescisão por transferência com data retroativa à competência atual"*  *"Considera data de transferência igual a data de demissão na transferência sem ônus"* |
| **Solução/Implementação:** | *Realizado o ajuste para validar a transferência baseada nos parâmetros de  *transferência com data retroativa.** |
| **Chamados relacionados:** | *TVV627* |

divs
