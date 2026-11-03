---
content_hash: cddb13768e2005e5c7f08c07a68386feb4643ca62d0591fcafcba50be69ec46e
fetched_at: '2026-06-29T00:09:20.963045+00:00'
page_id: '422545747'
product: rm
source: tdn-rm
title: Ficha Parametrizável da DIPJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545747
version: 3
---

Este recurso é utilizado quando a informação da ficha pode ser originada de fontes diversas na base de dados.  
 Se precisar gerar esta ficha seu cadastro deverá ser editado e para cada registro seu informada a fonte dos dados. As fontes de dados podem ser:

**Períodos Fiscais**. Neste caso deve-se informa o [Tributo](http://tdn.totvs.com/pages/viewpage.action?pageId=422546150) e o campo do [Período de Apuração](http://tdn.totvs.com/pages/viewpage.action?pageId=431677780) do qual deseja carregar o valor.

**Funções**. Neste caso deve-se informar o Tributo e a função que irá retornar o valor desejado.

**Nenhuma**. Se for escolhida esta opção o campo será gerado sempre em branco.

**Contas Contábeis**. Neste caso deve-se informa qual o valor será carregado da Conta Contábil: Débitos, Créditos, Movimentação, Saldo Atual ou Saldo anterior e se este será somado ou subtraído ao ser carregado para o registro.

Pode-se ainda especificar a Filial, uma faixa de centros de custos, contas gerenciais e Históricos Padrão para desconsiderar o encerramento do exercício.

Este recurso até o momento não foi migrado e pode ser acessado pela versão exe do Totvs Gestão Fiscal no seguinte caminho: Cadastros | Tabelas Auxiliares | Obrigações Federais | DIPJ |   
Atenção: Para as fichas 11 e 16 o campo Forma de Determinação da Base de Cálculo será preenchido com o valor 0 - Com base na Receita Bruta e Acréscimos para Lucro Estimado. Já para o Lucro Real, é preenchido com o valor 1 - Com Base em Balanço ou Balancete de Suspensão ou Redução.  
Portanto, para preencher este campo automaticamente, será verificado mês a mês qual é a forma de tributação válida para o tributo (IRPJ e CSLL) no mês. Para isto o processo de geração da rotina irá consultar o cadastro de [Vigência Tributária](http://tdn.totvs.com/pages/viewpage.action?pageId=422546100). Se a forma de tributação é Lucro Estimado, o campo receberá o valor "0". Se for Lucro Real, o processo irá preencher o campo com o valor "1". "0" será o valor default, caso a parametrização no cadastro de vigências não esteja correta.  
Novas fichas poderão ser incluídas manualmente pelo usuário desde que as mesmas estejam de acordo com o layout vigente da DIPJ e sua fonte de dados seja alguma das citadas neste documento.
