---
content_hash: 0b44f1ac163b06d7bb37bd2286cef43a97f008490f23e6f4a655939892ac1c73
fetched_at: '2026-06-29T00:09:29.057857+00:00'
page_id: '423938791'
product: rm
source: tdn-rm
title: Tradução dos Dados do Arquivo XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938791
version: 2
---

No recebimento automático de NF-e, através do job Serviço de Consulta de Arquivos XML, ao identificar o tipo de movimento a ser utilizado, o sistema efetuará a tradução do XML utilizando:

1. Identificação dos Produtos: É efetuada com base nos registros do cadastro Produtos para Importação de XML. Para cada produto no XML, o sistema verificará qual é o produto correspondente no seu cadastro, utilizando-o na inserção do item de movimento. Caso no XML seja encontrado algum produto sem correspondência o processo de Recebimento Automático será abortado, mas o XML será criado na base de dados com o status 'Inconsistente'. Será mostrado no log o problema. Ao ser corrigido, basta alterar o status do registro para pendente e executar novamente.
2. Identificação das Unidades de Medida: Ao encontrar o código da unidade de medida de cada item no arquivo XML, o sistema verificará no cadastro Unidades para Importação de XML qual é o código da Unidade correspondente e o mesmo será utilizado na inserção do item de movimento. Caso no XML seja encontrado alguma unidade sem correspondência o processo de Recebimento Automático será abortado, mas o XML será criado na base de dados  com o status  'Inconsistente'. Será mostrado no log o problema. Ao ser corrigido, basta alterar o status do registro para pendente e executar novamente.
3. Identificação dos CFOP: Se o sistema não identificar a natureza de operação, o movimento será gerado normalmente, no entanto, será atribuído ao mesmo Natureza Incompleta no Status Inclusão via Totvs Colaboração.  Movimentos com Status Inclusão via Totvs Colaboração "Natureza Incompleta " não serão visualizados na rotina de SPED, mas geram Financeiro, Contabilidade, Estoque e Aprovação de  Workflow.
