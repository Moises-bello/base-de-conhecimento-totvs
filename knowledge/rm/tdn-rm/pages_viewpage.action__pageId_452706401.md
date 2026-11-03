---
content_hash: 64505844e1334e9bd4c99dea564c5de556f0d25f109a5335c007194406fa0715
fetched_at: '2026-06-29T00:09:58.786862+00:00'
page_id: '452706401'
product: rm
source: tdn-rm
title: 12.1.8 (Estoque, Compras e Faturamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452706401
version: 6
---

Disponibilizado o processo de [Geração de Contrato a partir de Pedido de Compras](http://tdn.totvs.com/pages/viewpage.action?pageId=423938166);

Melhoria CT-e - [Adequação do CT-e às Notas Técnicas 2015/003 e 2015/004](http://tdn.totvs.com/pages/viewpage.action?pageId=423938368).

Realizada melhoria no processo de [Qualificação de Fornecedores](http://tdn.totvs.com/pages/viewpage.action?pageId=423938862):

1. A qualificação do fornecedor será tratada por coligada. Este comportamento será alterado para tratar por coligada como é feito na qualificação de produtos/fornecedor. O campo CODCOLCFO será incluído na tabela TQUALIFICACAOCFO e os tratamentos necessários serão realizados no serviço de qualificação de fornecedores.
2. Na conversão de base de dados o campo CODCOLIGADA da tabela TQUALIFICACAOCFO será alterado para CODCOLCFO e o campo CODCOLIGADA será criado e preenchido da seguinte forma: Caso a coligada do fornecedor (CODCOLCFO) for global, os dados da qualificação serão replicados para todas as coligadas que estiverem parametrizadas para qualificação de fornecedores. Caso contrário (fornecedor não global) o campo CODCOLIGADA será preenchido com a mesma informação do campo CODCOLCFO.

Realizadas melhorias no processo de [Importação de Movimentos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938143) e [Importação de Produtos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938138):

1. Disponibilizada exportação/importação da contabilidade do movimento.
2. O campo DTCADASTRO, da tabela TPRDCODIGO nos layouts de exportação de produtos não será mais importado, sendo este desconsiderado na importação mesmo que estiver informado no arquivo. O mesmo será setado automaticamente com a data do sistema na inclusão. Na exportação não haverá alterações e o campo ainda será exportado mantendo assim o legado no layout.

Disponibilizado o processo de [Aprovação de Movimentos via workflow no Fluig](http://tdn.totvs.com/pages/viewpage.action?pageId=423938696).
