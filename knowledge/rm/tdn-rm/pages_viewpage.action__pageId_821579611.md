---
content_hash: 077fc1ef078e8dac37af20310f3d974e50245df69fd25f84368f361645785168
fetched_at: '2026-06-29T00:11:45.801932+00:00'
page_id: '821579611'
product: rm
source: tdn-rm
title: Templates da Demonstração Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821579611
version: 2
---

## **Templates DLPA e DMPL**

Os arquivos modelos de DMPL/DLPA para importação estarão disponíveis no diretório de instalação ObjetosGerenciais\Layout

O modelo de DMPL - Demonstração das Mutações do Patrimônio Líquido foi criado de acordo com o padrão existente no [site da BM&FBOVESPA](http://www.bmfbovespa.com.br/Cias-Listadas/Empresas-Listadas/ResumoDemonstrativosFinanceiros.html?codigoCvm=23264&idioma=pt-br).

O objetivo deste modelo é ajudar o usuário a criar a DMPL de acordo com a sua necessidade. Cada empresa possui seus fatos contábeis e poderá alterar/excluir os fatos contábeis e colunas de acordo com a sua necessidade.

Para exclusão dos fatos contábeis na pasta Identificação, subpasta "Fatos Contábeis", o usuário poderá selecionar o fato contábil desejado e clicar no ícone de exclusão. Se desejar excluir alguma coluna deve-se acessar a subpasta "Colunas da Demonstração" e clicar no ícone de exclusão.

Na pasta "Configuração do Layout" é onde será feita a configuração do fato contábil com a sua respectiva coluna.

**Exemplo:**

No Modelo que estamos disponibilizando fizemos a configuração dos fatos contábeis da DMPL do período de 01/01/2013 a 30/09/2013 da TOTVS S/A.

A TOTVS não possui em sua DMPL todos os fatos contábeis apresentados em nosso Modelo, por este motivo configuramos apenas os fatos existentes na demonstração.

O primeiro fato contábil da DMPL - Modelo corresponde aos Saldos Iniciais, então ao acessar a aba "Configuração do Layout" e clicar na coluna "Capita Social Integralizado" o ícone com "(inserir o ícone de exclamação)" significa que será necessário completar a configuração.

Para esta configuração foi utilizada a opção de Origem do Valor = Saldo Inicial e o Sinal = Original. Neste exemplo o cliente pode informar a sua respectiva conta contábil que irá compor a coluna de Capital Social Integralizado. Pode ser utilizado uma ou mais contas contábeis.

Se o usuário não desejar utilizar a opção de Saldo inicial poderá alterar a opção de acordo com o desejado, este é apenas um modelo que pode ser alterado a qualquer momento de acordo com a necessidade do cliente.

Em outro fato contábil como por exemplo o fato contábil "5.04.03" - Opções Outorgadas Reconhecidas foi configurado na coluna "Capital Social Integralizado" a opção de filtro genérico.

Esta opção pode ser utilizada quando por exemplo deseja-se buscar um determinado lançamento/partida contábil dentro de uma movimentação de uma conta contábil. Vamos supor que na movimentação da conta de "capital integralizado" houveram 2 lançamentos/partidas à crédito e para determinado fato contábil deseja-se buscar somente 1 destes lançamentos/partidas.

Neste caso pode ser utilizado a opção de filtro genérico, se o usuário optar por manter esta opção deverá realizar a criação do filtro de acordo com sua necessidade.

O filtro genérico passa a ser processado conforme a Filial (Matriz ou SCP).

**Observação:**

Com relação à geração da DMPL para o SPED CONTÁBIL, o processo foi otimizado, possibilitando a utilização de Filtro Genérico para períodos trimestrais, desde que não seja filtro específicos, por exemplo, IDPARTIDA = 3.

O usuário deverá adaptar/criar a DMPL de acordo com sua necessidade, nos fatos contábeis que foram configurados o cliente deverá analisar se irá mantê-los e caso positivo deverá clicar no ícone "inserir o ícone de exclamação " e alterar as opções conforme desejado. Para os fatos contábeis que não foram configurados, o usuário pode clicar no ícone "inserir o ícone que representado sem configuração" e também realizar sua configuração conforme desejado.

## **Template DRE:**

Também está disponível no By You, central de Download e no diretório de instalação Objetos Gerenciais\Layout o template da DRE para auxiliar os clientes tributados pelo Lucro Real que desejam separar o Resultado Operacional do Não Operacional**.**
