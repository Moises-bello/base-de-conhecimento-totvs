---
content_hash: 514b387825a01a7865e1f9a99b9f2556e99c55b7e10680dd2ca6eb1930e1acc3
fetched_at: '2026-06-29T00:09:24.715029+00:00'
page_id: '423938006'
product: rm
source: tdn-rm
title: Importação/Exportação de Lista de Preços de Produtos por Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938006
version: 5
---

Os recursos de Importação/Exportação de Lista de Preços de Cliente/Fornecedor por produtos estão disponíveis através do TOTVS Business Conector. Para a utilização destes processos é necessário importar o layout através do Gerador de Saída | Layout | Importar Layout.

**Exportação**

O processo de Exportação consiste em copiar da tabela de Cliente/Fornecedor por produto os valores referentes ao código do produto, valor do produto, coligada e código do fornecedor, gerando um arquivo texto com layout definido.  
 Para gerar o arquivo.txt basta selecionar o layout e executar o processo Geração de Saídas.

**Importação**

O recurso de Importação insere ou atualiza os dados na tabela de produto por Cliente/Fornecedor a partir do arquivo texto criado na exportação. -Se o Cliente/Fornecedor já estiver sido incluído para o produto os valores serão atualizados. Senão, os valores serão inseridos na tabela Cli/For por produto.

* Para utilizar o processo de Importação é necessário importar o Layout através do TOTVS Business Conector | Conceito | Importar Conceito. Na visão do conceito, editar o conceito e acesse "Conexões de Origem", clique sobre a opção "PrecoCliFor" e sobre o botão Editar. Selecionar o arquivo.txt a ser importado, preencha os demais campos na tela e salve as alterações. Após estas configurações, selecione o conceito e clique em Processos | Processar Novo Conceito.   Observações:
* Os dados serão copiados e inseridos na tabela **TPRDCFO**.

***Atenção!*** No caso da importação, o processo é realizado pelo módulo Integração | Conceito. E para a exportação pelo módulo Integração | Gerador de Saídas para as exportações.
