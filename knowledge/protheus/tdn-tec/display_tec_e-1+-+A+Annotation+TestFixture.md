---
content_hash: 9975a01fb8c62d532ff6d5c0be3ad1f0552b58a4f2ab0ce1aaf73346ffc5a5e9
fetched_at: '2026-07-02T19:24:27.001489+00:00'
page_id: '655225033'
product: protheus
source: tdn-tec
title: e-1 - A Annotation TestFixture
type: documentation
url: https://tdn.totvs.com/display/tec/e-1+-+A+Annotation+TestFixture
version: 10
---

Como vimos anteriormente, a marcação de uma função ou classe como Teste do **PROBAT** é feita pela annotation *[TestFixture]*, porém ela possui muito mais funcionalidades além dessa marcação.

Vejamos:

---

## **SUITE**

A propriedade **"suite"** indica para qual suite o teste pertence, porém caso não seja informado através da annotation, o **PROBAT** adiciona o teste para o SUITE ALL.

Caso queira adicionar a outro suite, é preciso informar explicitamente essa propriedade.

| Tipo | Valor Default |
| --- | --- |
| character | "all" |

Exemplos

#### Executa em Modo All:

```
@TestFixture() // Como "ALL" é o valor default, não há necessidade de informá-lo
```

ou

```
@TestFixture(suite="all")
```

ou

```
@TestFixture("all")
```

#### Criando uma suite:

```
@TestFixture(suite="minha_suite")
```

ou

```
@TestFixture("minha_suite")
```

> NOTA:
>
> A forma não nomeada é possível para a propriedade [suite] pois ela é a primeira propriedade descrita na Annotation.
>
> Essa forma só é possível para [suite], as demais propriedades precisam obrigatoriamente ser nomeadas.

---

## **OWNER**

A propriedade **"owner"** indica quem é o "proprietário" do teste.

Sem informar, ele grava como Owner = "Unknown"

| Tipo | Valor Default |
| --- | --- |
| character | "unknown" |

Exemplo:

```
@TestFixture(owner="tlpp")
```

Com isso indico que o TLPP é "proprietário" desse teste.

> Até o momento dessa versão, esse recurso somente registra o "proprietário" no SQLite, pois necessita a implementação para uso de filtros e agrupamentos de resultados por "proprietário".

---

## **THREAD**

Indica se no momento da execução do teste o **PROBAT** irá abrir uma Thread exclusiva para que o teste seja executado.

| Tipo | Valor Default |
| --- | --- |
| character | "yes" |

Exemplos

#### Abre Thread:

```
@TestFixture() // Como "yes" é o valor default, não há necessidade de informá-lo
```

ou

```
@TestFixture(thread="yes")
```

#### NÃO abre Thread:

```
@TestFixture(thread="no")
```

---

## **PRIORITY**

Modifica a prioridade na execução dos testes, permitindo que o desenvolvedor possa indicar a ordem de execução conforme suas necessidades.

| Tipo | Valor Default |
| --- | --- |
| numeric | 100 |

Exemplos

#### Prioridade ALTA:

```
@TestFixture(priority=0)
```

#### Prioridade BAIXA:

```
@TestFixture(priority=999)
```

> * Os números possíveis para informar é de 0 a 999, somente 3 caracteres.
> * Não são permitidos números negativos.

Saiba mais sobre ordem de execução dos testes em [[Ordem e Prioridade](https://tdn.totvs.com/display/tec/e-3+-+Ordem+e+Prioridade)]

---

## **FOLDER**

A propriedade **"folder"** indica o diretório onde se encontra fisicamente o teste.

| Tipo | Valor Default |
| --- | --- |
| character | "" |

Porém, essa informação é facultativa pois o folder pode ser detectado automaticamente caso esteja utilizando boas práticas de desenvolvimento através de namespaces, como o exemplo abaixo:

| Localização física arquivo | Namespace |
| --- | --- |
| /test/date | test.date |

Caso você não queria utilizar namespaces em seu projeto, você pode contornar essa detecção automática informando explicitamente o diretório de seu teste, conforme abaixo:

```
@TestFixture(folder="/test/date")
```

---

## **TEST**

A propriedade **"test"** se refere ao nome do teste, por boas práticas o relacionamos à funcionalidade a ser testada.

| Tipo | Valor Default |
| --- | --- |
| character | "" |

Porém, essa informação é facultativa pois o nome pode ser extraído automaticamente do nome da classe e/ou função de teste.

Por exemplo, ao criarmos o teste para a classe LOGS, criaríamos então um arquivo fonte de teste com o nome: test\_LOGS.  
Nesse caso, o **PROBAT** irá extrair o nome como: "LOGS"

Porém, caso queria dar um nome diferente do extraído automaticamente, pode-se utilizar a propriedade **"test"**.

Exemplo:

```
@TestFixture(test='logs_customizados')
class test_LOGS
```

---

## **DESCRIPTION**

Informa uma descrição para o Teste caso haja a necessidade.

| Tipo | Valor Default |
| --- | --- |
| character | "" |

Exemplo:

```
@TestFixture(description="coloque aqui seu texto explicando o teste")
```

---

## **TARGET**

Informa qual o "alvo" do teste, na qual foi informado pelo Cross-Validation.

| Tipo | Valor Default |
| --- | --- |
| character | "" |

Exemplo:

```
@TestFixture(target="item.1")
```

Veja mais detalhes desse recurso em: [Cross-Validation](https://tdn.totvs.com/display/tec/e-8+-+Cross+Validation)

---

## - **RUNWITHALL** | **RWA**

Determina se Teste será executado com suite ALL ou se sua execução é obrigatório do modo exclusivo

| Tipo | Valor Default |
| --- | --- |
| logical | .T. |

Exemplos

#### Executa em Modo All:

```
@TestFixture() // Como .T. é o valor default, não há necessidade de informá-lo
```

ou

```
@TestFixture(runWithAll=.T.)
```

ou

```
@TestFixture(rwa=.T.)
```

#### NÃO executa em Modo All:

```
@TestFixture(runWithAll=.F.)
```

ou

```
@TestFixture(rwa=.F.)
```
