---
content_hash: edd13c84c8391d7b2f82294ca2586359177378f6123f6f8865cda0edc7dea8da
fetched_at: '2026-06-29T00:09:25.279271+00:00'
page_id: '423938099'
product: rm
source: tdn-rm
title: Esquema de Exportação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938099
version: 14
---

Os esquemas de exportação permitem agrupar as informações contidas no layout de relatório do parceiro (Elbrus ou SpressCom), para que posteriormente estes dados sejam exportados. Ele pode ser acessado no TOTVS Gestão de Estoque, Compras e Faturamento, na aba Cadastros | Mais | Tabelas Auxiliares | Esquema de Exportação.

No cadastro Esquemas de Exportação poderão ser informadas as seguintes propriedades:

* Aba **Identificação**
  + Descrição do Lote de Esquema.
  + Nome do Arquivo a ser gerado contendo o diretório completo
* Aba **Esquemas**.
  + Código do Esquema composto apenas de números.
  + Layout do Relatório previamente importado.
  + Nome da Tabela Principal.
  + Filtro para a geração de dados.
  + Nome do Arquivo e diretório completo.
  + Se é permitido sobrescrever o arquivo gerado.

### Processos

* **Testar Esquema -** Permite a geração do arquivo texto de acordo com as propriedades informadas (Parceiro Elbrus ou Spress). O Assistente para associação de layout recupera o Layout de acordo com a propriedade Nome do Arquivo. É necessário executar o 'Testar Esquema' antes de utilizar o processo de [Exportação de dados](https://tdn.totvs.com/pages/releaseview.action?pageId=423938100) para avaliar e validar o layout. O processo Testar Esquema não funciona em ambientes multi-tenant.
* **Wizard Esquema de Exportação -** Permite copiar o cadastro escolhido, a partir da seleção do parceiro, das entidades e de um diretório de Gravação.
* **Conversão de Relatórios -** Permite realizar a atualização dos relatórios Delphi para .Net,  de acordo com a tag do Relatório no cadastro de Esquema. É necessário, para a utilização dessa funcionalidade, que os relatórios .Net  estejam importados.  Somente os relatórios disponíveis na visão serão convertidos.

Obervações

Para cadastrar os Esquemas de Exportação os layouts dos parceiros Elbrus e SpressCom deverão ser previamente importados através do TOTVS Integração | [Gerador de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=237383341).

A partir da release 12.1.2402 será possível utilizar este cadastro em ambientes multi-tenant. Para estes ambientes a informação do diretório deverá ser preenchida manualmente tendo em vista o diretório base do seu ambiente, além disso no cadastro do **Esquema de exportação**, é necessário informar o nome do Arquivo com a sua respectiva extensão. Ex.: "Entrada\LOTE.TXT". Para maiores informações sobre como configurar o ambiente acesse: .

### Documentos relacionados

1. [Ponto de Venda](https://tdn.totvs.com/display/public/LRM/Ponto+de+Venda)
2. [Importação de dados via XML - Ponto de Venda](https://tdn.totvs.com/pages/releaseview.action?pageId=423938012)
3. [Exportação de Dados (Parceiro)](https://tdn.totvs.com/pages/releaseview.action?pageId=423938100)
