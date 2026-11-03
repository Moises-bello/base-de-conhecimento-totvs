---
content_hash: f28aace6f1a9034809fea55e00bf7b360931140b52ddc975097304c9fcadcc9e
fetched_at: '2026-07-02T19:24:27.597180+00:00'
page_id: '658427891'
product: protheus
source: tdn-tec
title: e-8 - Cross Validation
type: documentation
url: https://tdn.totvs.com/display/tec/e-8+-+Cross+Validation
version: 4
---

O "Cross Validation" tem a finalidade de dar ao projeto flexibilidade para validar se existem testes escritos para certos "alvos" conforme necessidade.

O primeiro passo a se fazer é informar ao **PROBAT** qual a função será responsável pela criação da lista, sendo assim, faremos da seguinte forma:

Arquivo appserver.ini

text

```
A seguir, devemos criar a função informada no INI seguindo alguns critérios:
```

* Deve retornar um array simples (vetor);
* Elementos do array devem ser strings;
* Array deve pelo menos ter 1 elemento;
* Função deve estar compilada no mesmo ambiente onde for executar o **PROBAT**.

Exemplo:

c#
> Nesse exemplo utilizamos nomes genéricos para deixar claro de que essa lista pode ser referente a qualquer controle que a equipe de desenvolvimento desejar.

Exemplos de listas:

* Fontes;
* Funções;
* Classes;
* Módulos;
* Recursos;
* Libs;
* etc ...

Ao determinar essa lista, agora seu projeto terá a obrigação de possuir pelo menos 1 teste para cada item.

Caso não exista um teste específico para cada "alvo" da lista, o **PROBAT** irá gerar erro no processo de apuração de resultados.

Portanto, agora temos que escrever o teste, porém devemos marcar o teste com seu respectivo "alvo", caso contrário não haverá como fazer o link entre o "alvo" e o teste.

Para marcar o teste, use a propriedade [target] da annotation [TestFixture], veja:

O exemplo acima está "linkando" o teste com o "item.1" da lista. Porém, ainda não temos teste "linkando" com o "item.2", portanto, caso executarmos o \*\*PROBAT\*\* com esse cenário, teremos um erro registrado.

Logo, após a execução, no processo de apuração do resultado e geração do arquivo de exportação, teremos então algo como:

xml
developed test: test dev OK

[ER0003] item.2: there is no test developed for this element in cross-validation
]]>

Para eliminar esse problema nesse exemplo, teremos então que escrever um teste com o [target] para o "item.2".
