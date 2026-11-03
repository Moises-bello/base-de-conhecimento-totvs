---
content_hash: a850223574dc726eb4e68229d198f8efb88823ce1490d50a491354a890be20f9
fetched_at: '2026-07-02T19:24:28.521241+00:00'
page_id: '793811801'
product: protheus
source: tdn-tec
title: a - Configurando Banco de Dados
type: documentation
url: https://tdn.totvs.com/display/tec/a+-+Configurando+Banco+de+Dados
version: 2
---

Disponibilidade

Recurso disponível a partir do AppServer 20.3.1.14 e tlppCore 01.04.05. Versões anteriores somente gravarão os dados no SQLite.

O PROBAT sempre gravará as execuções em algum Banco de Dados e você poderá indicar em qual Banco gravar.

Sendo assim, podemos configurar de 3 modos distintos, sendo:

* SQLite local;
* DBAccess configurado no Environment;
* DBAccess configurado diretamente no PROBAT.

## **SQLite local**

Esse modo é o nativo do PROBAT, sem a necessidade de configuração manual pois o PROBAT já se auto configura para utilizar o SQLite inserindo a seguinte instrução em seu INI.

Dessa maneira, um arquivo [*SYSTEM.db*] de SQLite será gerado dentro da pasta [*db\_sys*], conforme configuração de seu ambiente.

## **DBAccess configurado no Environment**

Podemos informar ao PROBAT que ele acesse as mesmas configurações de DBAccess feitas diretamente no Environment em uso, nesse caso configure seu ini conforme abaixo:

## **DBAccess configurado diretamente no PROBAT**

É possível também, configurar um DBAccess exclusivo para uso no PROBAT, portanto, em seu ini insira as seguintes chaves:

DBSERVER=
DBALIAS=
DBPORT=]]>

```

```

> Para saber mais sobre as chaves de configuração do DBAccess, acesse: [Seção DBAccess](https://tdn.totvs.com/pages/viewpage.action?pageId=6064885)

Nesse caso, independentemente do DBAccess configurado em seu environment, o PROBAT utilizará as chaves informadas na seção [PROBAT] para realizar a conexão com seu Banco de Dados.
