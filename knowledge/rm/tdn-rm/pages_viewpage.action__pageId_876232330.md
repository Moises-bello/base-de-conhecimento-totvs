---
content_hash: 0663f38b725073b0d45090b3e28c702003d1048895a8990170fc546a2a5d68b0
fetched_at: '2026-06-29T00:11:59.895265+00:00'
page_id: '876232330'
product: rm
source: tdn-rm
title: Importação de Dados via Conceito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=876232330
version: 11
---

Para realizar a importação de dados por arquivo texto no Totvs Gestão de Estoque Compras e Faturamento será utilizada a ferramenta Conceito(ETL), que facilita a execução destas operações de forma dinâmica, utilizando a própria regra dos cadastros de inclusão de registros do módulo .

Esta ferramenta pode ser acessada através do Módulo Integração > Aba Integração > Conceito(ETL). Para incluir um novo Conceito, vá em Processos > Importar Conceito, buscando os Conceitos já disponíveis.

Para a importação do arquivo txt, você deverá selecionar e/ou editar o Conceito referente ao cadastro que deseja importar no Módulo Gestão de Estoque Compras e Faturamento, na aba *"Conexões de Origem",* na linha de *"Arquivo"*deve ser informado o caminho onde esta o arquivo *txt* feito conforme o Layout*,* e após salvar o cadastro do Conceito. Para a execução da Importação em processo > Processar novo Conceito.

**Observação**

* Caso seja a primeira vez a utilizar o processo de importação, é necessário que se inclua um novo conceito e defina para qual cadastro o mesmo será utilizado, através do carregamento do arquivo de configurações do conceito (extensão .ICP).
* Totvs Gestão de Estoque Compras e Faturamento possui arquivos padrões do Conceito que podem ser encontrados utilizando a ferramenta Totvs Compartilhamento Encontrado no **menu Gestão** dentro do módulo.
* Após carregar o arquivo que conterá a parametrização da importação desejada, o cadastro do Conceito será preenchido automaticamente, necessitando assim que o usuário apenas altere o caminho de origem do arquivo.
* Caso algum item do arquivo de origem não atenda as validações do conceito criado, não será importado nenhum registro.
* Os campos alfanuméricos devem estar colocados da esquerda para a direita.
* Os campos numéricos devem estar colocados da direita para a esquerda.

O processo de importação por texto contempla a importação dos seguintes cadastros:

* [Movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=876226391) (CONMOV0013 - Movimento - V4).
* Produto.

Dica!

Existem casos em que o conceito não é executado ou importa os valores incorretamente dependendo do conteúdo (letras com acentuação, Ç ou Ã por exemplo) porque o arquivo txt está com uma codificação diferente do conceito. Os conceitos possuem codificação UTF-8, portanto caso o arquivo não tenha essa configuração será necessário altera-lo. Para isso basta editar o conceito e alterar a seguinte configuração:
