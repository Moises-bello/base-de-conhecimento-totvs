---
content_hash: e04754f61a0dceb3a690fdd98dd26da96d80c211be31440f72a2700dd83579be
fetched_at: '2026-06-29T00:09:25.422622+00:00'
page_id: '423938144'
product: rm
source: tdn-rm
title: Importação/Exportação de Lista de Preços de Produtos 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938144
version: 3
---

O processo de Exportação de Lista de Preços de Produtos consiste em copiar do [cadastro de produtos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938817) os valores referentes aos preços do produto gerando um arquivo texto com um layout pré-definido. Para executar esta rotina é preciso importar o layout através do TOTVS Integração |  [Gerador de Saídas](http://tdn.totvs.com/pages/viewpage.action?pageId=425459363) | Layout | Importar Layout.

**Identificadores do Produto:** Código do Produto, Código Reduzido, Número do Produto no Fabricante. Para cada um destes identificadores existem dois tipos de layouts:  Layout 1 e Layout 2.  
 O recurso de Importação atualiza os valores para os preços do Produto a partir do arquivo texto criado na exportação. Para utilizar o processo de importação de Lista de Preços de Produtos é necessário incluir um novo conceito através do TOTVS Integração |  Conceito | Importar Conceito.  Após a inclusão, edite o conceito e selecione o arquivo texto a ser importado através da opção "PrecoProduto", botão Editar. Após salvar as configurações, selecione o conceito e execute Processar Novo Conceito.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.
