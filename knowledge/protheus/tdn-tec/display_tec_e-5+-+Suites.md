---
content_hash: 89ad70dd17fc6b3fc2fcf3793680ec36ccd5ba40406bb002c03e2d761d55f912
fetched_at: '2026-07-02T19:24:27.019158+00:00'
page_id: '655623216'
product: protheus
source: tdn-tec
title: e-5 - Suites
type: documentation
url: https://tdn.totvs.com/display/tec/e-5+-+Suites
version: 6
---

Uma Suíte de Testes é uma coleção de casos de testes que são agrupados para propósitos de execução de testes.

Todos os testes escritos para o **PROBAT** devem pertencer a uma suíte de testes, sendo assim, o desenvolvedor pode informar explicitamente qual suíte ele pertence ou, não informar nada e manter o valor default, ou seja, a suíte "ALL" (todos).

Exemplo:

```
O exemplo acima automaticamente será adicionado na suíte "ALL"
```

## Suítes customizadas

O desenvolvedor pode criar suítes customizadas conforme necessidade.

Por exemplo, pode-se agrupar testes que sejam da suíte "financeiro", outros da suíte "compras" e assim por adiante.  
Ou então, podemos agrupar por "manipulação de arquivo", "apis de integração", "sys\_log", etc...

Veja que ele é flexível para atender as mais diversas necessidades, portanto, quais suítes deverão ser criadas será definido por cada equipe de desenvolvimento.

Para criar, é muito simples:

```
Basta utilizar a propriedade SUITE e informar o nome que desejar.
```

Nesse caso, criamos uma suíte chamada de "sistemico", e nela podemos agrupar todos os testes que precisam ser executados para os testes sistêmicos de um produto.

Uma das vantagens de se organizar os testes por suítes, é que torna possível a execução dos testes somente de uma suíte em específico, informando então na função de RUN que deseja somente executar a suíte "sistemico".

> Veja em mais detalhes os modos de execução em (Executando Testes).

Um ponto importante também a se saber é que, por default, mesmo sendo uma suíte customizada ela será executada no modo ALL a função RUN, ou seja, ao solicitar que todos os testes sejam executados o **PROBAT** irá executar todas as suítes customizadas também.

Exceto se o desenvolvedor indicar explicitamente de que uma determinada suíte é exclusiva.  
Veja mais abaixo:

## Suítes Exclusivas

Utilizando o exemplo de cima, podemos informar ao **PROBAT** que a suíte "sistemico" não pode ser executada no modo ALL, portanto, somente será executada quando for explicitamente informada na função RUN.

Esse recurso é interessante para dar mais flexibilidade ao projeto, e usando mais uma vez o exemplo, a suíte "sistemico" não pode ser executada a cada validação de commits feitos ao projeto. São testes que somente devem ser executados no período de testes Sistêmicos e portanto devem ser exclusivos.

Para indicar que uma suíte é exclusiva, é muito simples.

Sugerimos criar um código fonte somente para essas configurações que o **PROBAT** permite, portanto, sugerimos:

**test\_config.tlpp**

E agora, dentro dele coloque a seguinte instrução:

```
Agora é só compilar o test_config.tlpp e pronto, ele não será mais executado em modo ALL.
```
