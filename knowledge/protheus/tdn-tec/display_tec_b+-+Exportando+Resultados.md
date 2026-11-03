---
content_hash: 3bcd36908de5d3d667d26f9363f2b9ef13b552dd46d2ced3bc76cd772ad5cc1f
fetched_at: '2026-07-02T19:24:27.066110+00:00'
page_id: '656073814'
product: protheus
source: tdn-tec
title: b - Exportando Resultados
type: documentation
url: https://tdn.totvs.com/display/tec/b+-+Exportando+Resultados
version: 4
---

Ao final da execução o **PROBAT** pode exportar o resultado dos testes automaticamente, conforme possível configurar através do appserver.ini em sessão específica.

```
[PROBAT]
EXPORT_AFTER_RUN=1
EXPORT_FILE_NAME=results
EXPORT_FORMAT=JUnit
```

## **EXPORT\_AFTER\_RUN**

Indica se ao final da execução gera o resultado automaticamente ou não, sendo:

0 = Não gera arquivo.  
1 = Gera arquivo com resultado, baseado em EXPORT\_FILE\_NAME e EXPORT\_FORMAT.

Caso opte pela geração automática, o arquivo será gerado na pasta ROOT/SYSTEM do appserver com o nome definido em [EXPORT\_FILE\_NAME] e com o formato definido em [EXPORT\_FORMAT].

> Quando exportado logo após a execução dos testes serão exportados apenas os resultados da última execução dos Testes.

Porém, caso a escolha opte por não gerar automaticamente, para gerar a exportação é preciso utilizar a Main Function:

**tlpp.probat.export()**

Veja mais sobre esse recurso em: (  )

## **EXPORT\_FORMAT**

Até o momento temos somente implementado o formato jUnit, portanto a chave precisa ser: [EXPORT\_FORMAT=JUnit]

Portanto ao exportar o arquivo, o arquivo XML gerado será no formato jUnit e seu conteúdo será parecido com:

```
<?xml version="1.0"?>  
  <testsuites  id="20190109203113" name="results" type="all" tests="1" skipped="0" failures="0" time="0.002" >  
    <testsuite  id="000001"  name="all"  tests="1" skipped="0" failures="0" time="0.002" >  
      <testcase id="1" name="Class:MANUALUT.TEST_MANUALUT():New() | Method:EXAMPLEFORUSE()" time="0.002" >  
        Folder: TEST/UNIT/MANUALUT | Call: U_manualUT( cTest ) | Expected: {C}-[test_1] | Result: {C}-[test_1]  
      </testcase>  
    </testsuite>  
  </testsuites>
```

## **EXPORT\_FILE\_NAME**

O nome do arquivo pode ser customizado, basta informar o nome desejado por uma chave do INI de seu appserver.

Exemplo 1:

```
[TLPP_ENGINE_TESTS]
FILE_NAME_EXPORT=
```

Irá manter o nome padrão da engine, ou seja, "results" para resultados e "coverage" para cobertura de código.

Ficando:

results.xml -> Resultados em formato jUnit  
coverage.json -> Json de cobertura de código para uso no VsCode  
coverage.xml -> XML com dados da cobertura de código

Exemplo 2:

```
[TLPP_ENGINE_TESTS]
FILE_NAME_EXPORT=customname
```

Gerará então:

customname.xml -> Resultados em formato jUnit  
customname.json -> Json de cobertura de código para uso no VsCode  
customname (1).xml -> XML com dados da cobertura de código

Note que dessa forma, existirá conflitos com arquivos com a mesma extensão e exigirá uma experiência maior do operador para saber a finalidade de cada arquivo.

Por essa razão, sugerimos utilizar um dos dois modos a seguir.

Exemplo 3:

```
[TLPP_ENGINE_TESTS]
FILE_NAME_EXPORT=*customname
```

Gerará então:

unit-customname.xml  
coverage-customname.json  
coverage-customname.xml

Exemplo 4:

```
[TLPP_ENGINE_TESTS]
FILE_NAME_EXPORT=customname*
```

Gerará então:

customname-unit.xml  
customname-coverage.json  
customname-coverage.xml
