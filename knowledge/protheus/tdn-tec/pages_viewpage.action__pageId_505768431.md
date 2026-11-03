---
content_hash: 751dfd81df49287b40bafb533cc04677595e0ce5c58b38d3243e4b24a84d6865
fetched_at: '2026-07-02T19:24:25.744228+00:00'
page_id: '505768431'
product: protheus
source: tdn-tec
title: DBAccess - Como configurar um ambiente com MSSQL Server e Collation cirílico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=505768431
version: 11
---

## Descrição

Atualmente é possível utilizar o true em ambientes que utilizam o Collation cirílico.

Para isto, algumas configurações são necessárias para compatibilizar as operação de escrita e leitura.

---

## Ambientes Windows

Em um ambiente com Sistema Operacional Microsoft Windows, algumas configurações específicas são necessárias para o correto funcionamento da aplicação.

Em configurações de Região e Idioma, altere o idioma para aplicações não-Unicode para Russo (Russia).

---

## Ambientes Linux

Em um ambiente com Sistema Operacional Linux, algumas configurações específicas são necessárias para o correto funcionamento da aplicação.

1. Configurar a variável de ambiente LC\_CTYPE com o valor ru\_RU.CP1251
2. Instalar a unixODBC versão 2.3.7 ou superior

Dica

Caso a sua instalação do Linux não possua o codepage indicado na documentação, você pode instalá-lo utilizando o comando abaixo:

---

## Configurações do banco de dados MSSQL Server

O database que será utilizado para atender à este ambiente, deve ter seu *Collation* configurado como CYRILLIC\_GENERAL\_BIN, para assim suportar os caracteres cirílicos.

## Veja também
