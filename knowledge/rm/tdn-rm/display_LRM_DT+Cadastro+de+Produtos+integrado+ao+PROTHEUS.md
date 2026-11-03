---
content_hash: dfb558956c4e4276aafa091ddc7c39b6d32f1b002433e5c55344de14b0529c82
fetched_at: '2026-06-29T00:08:41.258756+00:00'
page_id: '286521606'
product: rm
source: tdn-rm
title: DT Cadastro de Produtos integrado ao PROTHEUS
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Cadastro+de+Produtos+integrado+ao+PROTHEUS
version: 106
---

# CADASTRO DE PRODUTO - MENSAGEM ÚNICA ITEM

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Integração de Produto. |
| **Situação/Requisito:** | Ao realizar inclusão/alteração no cadastro de Produtos no RM, o RM replica os produtos globais para cada filial no PROTHEUS. |
| **Solução/Implementação:** | Na **inclusão** de um novo produto global, o RM irá replicar os produtos para cada filial no PROTHEUS que está integrada ao RM.  Na **alteração** o RM irá replicar os produtos globais para cada filial no PROTHEUS, somente quando for alterado os campos da tabela Produtos Globais (TPRODUTO) que são sincronizados na mensagem única. São eles: Código do Produto; Descrição do Produto; Nome Fantasia; Inativo; Tipo; Peso Bruto; Peso Líquido; Usa Número de Série; Controlado por Lote; Referência; Número da Nomenclatura Comum do Mercosul (NCM).  **Observação:** este comportamento será aplicado somente quando o RM utilizar Produto Global. Quando não utilizar Produto Global e quando forem alterados os dados de produto específicos por coligadas a sincronização dos dados será realizada normalmente conforme definido no adapter de integração |
| **Conversores e Parâmetros:** | Não se aplica. |
| **Tickets relacionados:** | 966881. |
| **Requisito:** | Integração Manutenção de Ativos x BackOffice RM - cadastro de Produto.  Documento de integração: |

divs
