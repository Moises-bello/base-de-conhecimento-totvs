---
content_hash: 04e89997777b52c03ff051d01f92d02e47a0f7186a0857764ccfb9a4d8bc4f13
fetched_at: '2026-07-02T19:24:19.657809+00:00'
page_id: '243646125'
product: protheus
source: tdn-tec
title: GetPort
type: documentation
url: https://tdn.totvs.com/display/tec/GetPort
version: 7
---

GetPort

Retorna o número da porta que o servidor de aplicação, license, http ou https está escutando.

## Sintaxe

false [, ,  ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nType | numérico | Indica o tipo da porta (1 - Application, 2 - License, 3 - HTTP, 4 - HTTPS). | X |  |
| lIsSSL | lógico | Recebe por referência a informação se esta porta está ou não usando conexão segura |  | X |
| lHasMPP | lógico | Recebe por referência a informação se esta porta está com Porta Multi Protocolo habilitada |  | X |

Obs. Para a porta do Application Server o valor de **lIsSSL** segue  e a indicação de porta multi protocolo **lHasMPP** segue .

Ref. 

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nPort | numérico | Retorna o número da porta em formato númerico, caso a porta não esteja habilitada ou o tipo da porta não esteja no intervalo de 1 a 4, retorna -1. |

## Exemplos

cppEclipsetruefalse

## Abrangência

AppServer 17.1.1.7 e 17.2.1.7

**Obs**. Os parâmetros "**lIsSSL**" e "**lHasMPP**" somente podem ser recuperados em versões superiores a **19.3.0.2**
