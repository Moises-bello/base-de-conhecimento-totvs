---
content_hash: e8d5a139754414f9996ce5d660832209634d067f725a45d386ded47eb2d98fed
fetched_at: '2026-06-29T00:09:27.188246+00:00'
page_id: '423938451'
product: rm
source: tdn-rm
title: Importação de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938451
version: 15
---

Atenção!

Esta funcionalidade somente está disponível na versão 11.51.45 ou superior.

Para realizar a importação de dados por arquivo texto no Totvs Gestão Contábil será utilizada a ferramenta "RM Conector", que facilita a execução destas operações de forma dinâmica, utilizando a própria regra dos cadastros da contabilidade.

Esta ferramenta pode ser acessada através do Menu Integração > Aba Integração > Conceito. Para incluir um novo Conceito, vá em Processos > Importar Conceito, buscando os Conceitos já disponíveis.

Para a importação do arquivo txt, você deverá selecionar e/ou editar o Conceito referente ao cadastro que deseja importar no Módulo Contábil, na aba *"Conexões de Origem",* na linha de *"Arquivo"*deve ser informado o caminho onde esta o arquivo *txt* feito conforme o Layout*,* e após salvar o cadastro do Conceito. Para a execução da Importação em processo > Processar Conceito.

**Observação**

* Caso seja a primeira vez a utilizar o processo de importação, é necessário que se inclua um novo conceito e defina para qual cadastro o mesmo será utilizado, através do carregamento do arquivo de configurações do conceito (extensão .ICP).
* Totvs Gestão Contábil possui arquivos padrões do Conceito na pasta C:\Totvs\CorporeRM\ObjetosGerenciais\Conceito (ou conforme seu caminho de instalação da Biblioteca, podendo então variar para ambientes em instalação 3 camadas).
* Após carregar o arquivo que conterá a parametrização da importação desejada, o cadastro do Conceito será preenchido automaticamente, necessitando assim que o usuário apenas altere o caminho de origem do arquivo.
* Caso algum item do arquivo de origem não atenda as validações do conceito criado, não será importado nenhum registro.
* No Layout de importação, existe a coluna *"Obrigatório".* Ela consiste na obrigatoriedade ou não do preenchimento do campo. Quando informado com "X", o mesmo tem preenchimento obrigatório e caso não haja nenhuma informação para o campo, é necessário deixar os espaços em branco referente ao campo. Quando vazio, não é necessário o preenchimento do mesmo.
* Para o processo de importação todos os campos de data devem ser preenchidos com 10 posições, conforme descrito no layout de importação, exemplo 01/01/2012.
* Os campos alfanuméricos devem estar colocados da esquerda para a direita.
* Os campos numéricos devem estar colocados da direita para a esquerda.

O processo de importação por texto contempla a importação dos seguintes cadastros:

* Plano de Conta Contábil
* Plano de Conta Gerencial
* Plano de Conta Paralelo
* Centro de Custo
* Lançamento Contábil
* Lançamento Não Quitado
* Histórico Padrão
* Campo Complementar
* Orçamento
* r
* [Saldo MultiMoeda](https://tdn.totvs.com/pages/viewpage.action?pageId=645662141)

Atualmente temos os seguintes Conceitos Disponíveis:

* CONCTB0001 - Importação Centro de Custo
* CONCTB0002 - Importação Lançamentos Não Quitados
* CONCTB0003 - Importação Campo Complementar Conta Contábil
* CONCTB0004 - Importação Contas Contábeis
* CONCTB0005 - Importação Contas do Plano Paralelo
* CONCTB0006 - Importação Contas Gerenciais
* CONCTB0007 - Importação Histórico padrão
* CONCTB0008 - Importação Lançamentos Contábeis - **Novo Modelo**
* CONCTB0009 - Importação Orçamentos
* CONCTB0010 - Importação Saldo Anterior - **Modelo Antigo**
* CONCTB0011 - Importação Lançamentos Contábeis (Arquivo Delimitado) - **Novo Modelo**
* CONCTB0012 - Importação Saldo Multimoeda - **Novo Modelo**
* CONCTB0013 - Importação Saldo Anterior com Rateio (Arquivo Delimitado) - **Novo Modelo**

Dica!

Existem casos em que o conceito não é executado ou importa os valores incorretamente dependendo do conteúdo (letras com acentuação, Ç ou Ã por exemplo) porque o arquivo txt está com uma codificação diferente do conceito. Os conceitos possuem codificação UTF-8, portanto caso o arquivo não tenha essa configuração será necessário altera-lo. Para isso basta editar o conceito e alterar a seguinte configuração:
