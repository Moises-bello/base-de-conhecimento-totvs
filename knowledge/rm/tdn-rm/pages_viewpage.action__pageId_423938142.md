---
content_hash: ab8d16386d6324ed8ee468136110ccd3ef6156a3fddac05245743936141174ce
fetched_at: '2026-06-29T00:09:25.418214+00:00'
page_id: '423938142'
product: rm
source: tdn-rm
title: Importação/Exportação de Número(s) de Séries de Produto(s)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938142
version: 4
---

O processo de Exportação de Número(s) de Séries de Produto(s) consiste em copiar do [cadastro de produtos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938817) os valores referentes aos [números de séries](http://tdn.totvs.com/pages/viewpage.action?pageId=423937943) do produto gerando um arquivo texto com um layout pré-definido. Para executar esta rotina é preciso importar o layout através do TOTVS Integração | [Gerador de Saida](http://tdn.totvs.com/pages/viewpage.action?pageId=237383341)| Layout | Importar Layout.   
 Estão disponíveis 3 tipos de layouts: Número de Série de Produto (Cod. Produto), Número de Serie de Produto (Cód. Reduzido), Número de Serie de Produto (Num. Fabricante);  
 O recurso de Importação atualiza inclui os números de série no cadastro do produto, a partir, do arquivo texto criado na exportação. Para utilizar o processo de importação é necessário incluir um novo conceito através do TOTVS Integração |  Condeito | Importar Conceito.  Após a inclusão, edite o conceito e selecione o arquivo texto a ser importado através da opção "Produto", botão Editar. Após salvar as configurações, selecione o conceito e execute Processar Novo Conceito.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.
