---
content_hash: 2994e3d3d73004a8ab3129773e1deda02b371f2a545fc0e768fb7f8ff32697bd
fetched_at: '2026-07-02T19:24:26.828589+00:00'
page_id: '654947825'
product: protheus
source: tdn-tec
title: 8 - Como tudo acontece
type: documentation
url: https://tdn.totvs.com/display/tec/8+-+Como+tudo+acontece
version: 15
---

O **PROBAT** procura no RPO por classes e funções que utilizam determinadas annotations para a execução dos testes.

No exemplo usado com a implementação básica de um teste com classe, tivemos a utilização de duas annotations, são elas:

[TestFixture]  
[Test]  
Abaixo vamos resumir como a mágica acontece!

Portanto, detalharemos através dos passos de **A** a **G**.

## **[A]**

Veja o trecho de nosso exemplo:

c#

```
A annotation [TestFixture] serve para marcar a classe ou função como um dispositivo de teste.
```

Somente através dessa marcação é que o **PROBAT** consegue descobrir quais são as classes ou funções específicas de testes.

Um ponto importante é que para fazer uso da annotation referida é preciso importar a include exclusiva do **PROBAT** fazendo a inserção da instrução logo no começo do fonte: [#include "tlpp-probat.th"]

## **[B]**

Veja esse outro trecho do mesmo exemplo:

c#

```
Nesse trecho do código, marcamos o método sampleTest() como um método a ser executado durante os testes através da annotation [Test].
```

Importante ressaltar que a descrição do teste, feito através do primeiro parâmetro da annotation, é obrigatório pois ele passará por uma função que faz essa validação.

> NOTA: Se você declarar uma classe com [TestFixture] e não tiver nenhum método com annotation [Test], seu teste começará a ser executado, porém gerará um resultado do tipo SKIPPED.

## **[C]**

Outro ponto importante para a correta configuração, é utilizar o recurso de namespace.

Veja o trecho:

```
Em nosso exemplo, utilizamos o nome do diretório onde se localiza a implementação do teste, ou seja, test/unit/sample.
```

Essa informação é importante para fácil localização física dos fontes de testes, afinal ele estará identificado como FOLDER, tando na gravação do SQLite como no XML gerado.

Exemplo:

xml
Folder: TEST/UNIT/SAMPLE/ | Description: U\_SAMPLE( cTest ) | Assert: TLPP.PROBAT.ASSERTEQUALS | Call From: TEST\_SAMPLE.TLPP:57 | Expected: {C}-[test\_1] | Result: {C}-[test\_1]
]]>

Outro modo de informar o FOLDER é através da propriedade da annotation, segue:

c#

```
Nesse caso, o PROBAT irá priorizar o valor informado pela annotation.
```

## **[D]**

Uma obrigatoriedade é o uso de duas includes, são elas:

c#

```

```

* A include [tlpp-core.th] só é obrigada nesse exemplo pois escrevemos o teste com classe, pois caso tivéssemos criado o teste com função não precisaríamos.
* A obrigatoriedade da include [tlpp-probat.th] será para todos os testes, pois é nela que se encontram as definições das annotations, comandos e instruções usadas pelo **PROBAT**.

## **[E]**

Por último e não menos importante, para que o teste seja registrado pela **PROBAT** na execução é preciso fazer uso de alguma função assert() dentro do método ou função de teste, veja o trecho:

c#

Porém, para que o assert funcione corretamente, é preciso realizar o "import" do namespace da **PROBAT** em seu fonte de teste, pois essa função é de uso exclusivo do tlppCore.

c#

Ou simplesmente utilizar o namespace diretamente na chamada da função:

c#

```
Em nosso exemplo, utilizamos a função assertEquals() pois faz a comparação entre dois valores que devem ser iguais.
```

Para saber mais em detalhes sobre as funções de asserts disponíveis, acesse o link abaixo!

* [PROBAT - asserts](https://tdn.totvs.com/display/tec/d+-+Asserts)

Após seguir todos os passos acima, basta compilar seu código-fonte de teste para que seja possível executá-lo.

## **[F]**

Para executar seus testes, basta fazer uso da Main Function disponibilizada pelo **PROBAT**, assim podemos executá-la:

* Através de algum código-fonte;
* Diretamente pela execução do VsCode;
* Linha de comando do Sistema Operacional através do appserver.

Exemplos:

###### **1 - Código fonte**

c#

###### **2 - VsCode**

Ao pressionar Crtl + F5 ou F5 em seu VsCode, informe o seguinte na caixa de diálogo aberta:

c#

###### **3 - Linha de comando**

**Windows**

* abra o prompt de comando DOS.
* acesse o diretório onde se encontra o appserver.
* depois utilize o comando:

c#

**Linux**

* abra o Terminal.
* acesse o diretório onde se encontra o appserver.
* depois utilize o comando:

c#

## **[G]**

Resumidamente o **PROBAT** irá obter as funções ou classes de testes através das annotations:

* TestFixture
* Test

Grava as funções no SQLite para uso posterior ou logo em seguida, dependendo do modo escolhido de "discovery".

Ao executar, lê os nomes de funções e classes já descobertos e executa todos os testes que estejam dentro do escopo pedido pela função RUN.

Através das funções de asserts existentes dentro dos fontes de testes, faz as comparações devidas conforme o valor produzido pelo teste e o valor esperado e após grava no SQLite o resultado dessa operação.

Ao final, faz a exportação dos resultados em um arquivo no formato pedido.
