---
content_hash: 9a03fc243720a511a82712ac347c8a3727b02780d216554678e65029dcb29ad2
fetched_at: '2026-06-29T00:09:17.024850+00:00'
page_id: '421388563'
product: rm
source: tdn-rm
title: FIN - Moedas e Índices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388563
version: 6
---

**Definição de Moeda**

Em um significado básico, "moeda" é o meio através do qual são efetuadas as transações monetárias. É a unidade representativa de valor, controlada pelo governo do país, que é o único que pode fixar e controlar seu valor.

Neste módulo você pode cadastrar a moeda corrente do seu país e as de outros países.

**Definição de Índice**

São valores numéricos utilizados para o cálculo de determinados produtos ou serviços.  
Neste módulo podem ser cadastrados vários tipos de índices.  
Na janela principal é possível visualizar de forma simplificada, informações de um ou de vários registros. Você define quantos e quais registros serão apresentados, criando filtros através do Gerenciados de Filtros (localizado na Barra de Ferramentas).   Ao executar um filtro cada registro será apresentado em uma linha e as informações em colunas.

**Dicas**

A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por Usuário ou por Perfis, no menu Segurança dos Serviços Globais.  
Ao clicar sobre o nome de algumas informações a janela de edição do cadastro da informação é apresentada.  
Você pode definir quais as colunas que serão apresentadas na janela de visão dos registros, utilizando a funcionalidade "Configurar Colunas", ícone localizado na barra de ferramentas.

**Identificação**

Nesta pasta são apresentadas informações que identificam a moeda ou o índice. Informações sobre alguns campos:

Defasagem em Meses

Preencha o campo com o número de meses cuja moeda/índice está defasada. Exemplo

São cadastradas as seguintes Cotações:

* 01/10/2008 Valor = 7,000
* 30/09/2008 Valor = 6,000
* 29/09/2008 Valor = 5,000
* 01/09/2008 Valor = 4,000
* 28/08/2008 Valor = 3,000
* 27/08/2008 Valor = 2,000
* 25/07/2008 Valor = 1,000

*No campo Defasagem é informado 0 (zero):*

Ao baixar um lançamento com a data de 01/10/2008 o sistema busca a cotação do dia 01/10, pois considera que a moeda não está defasada.

*No campo Defasagem é informado 1 (um):*

Ao baixar um lançamento com a data de 01/10/2008 o sistema busca a cotação do dia 01/09. Ou seja, o sistema busca a cotação de 30 dias anteriores a data informada.

*No campo Defasagem é informado 2 (dois):*

Ao baixar um lançamento com a data de 01/10/2008 o sistema busca a cotação do dia 01/07.

* Em todos as situações, caso não exista cotação da data procurada pelo sistema, será verificada a data anterior.

Parte Inteira e Parte Fracionária

Informe os nomes para a parte inteira e para a parte fracionária da moeda ou índice.

Exemplo de um cadastro de moeda

* Símbolo = R$
* Tipo = moeda
* Descrição = Real
* Casas Decimais = 2
* Parte Inteira Singular = real
* Parte Inteira Plural = reais
* Parte Fracionária Singular = centavo
* Parte Fracionária Plural = centavos

No cadastro do lançamento financeiro, deve-se observar o respectivo campo para inserir a moeda e/ou o índice, pois o comportamento do sistema será diferente dependendo desses dados.   
Se o objetivo for cadastrar um lançamento em moeda estrangeira, deve-se inserir um código no campo Moeda que esteja cadastrado com o tipo Moeda. E caso seja incluir um lançamento financeiro em real, mas com algum indexador para ajuste de valor, deve-se cadastrar no campo Moeda a moeda Real e no campo Indexador um código cadastrado como Índice.

**Observação**

Quando for inserido uma moeda diferente do Real no campo Moeda do lançamento, o sistema desabilitará o campo Indexador.    
  
Veja Também
