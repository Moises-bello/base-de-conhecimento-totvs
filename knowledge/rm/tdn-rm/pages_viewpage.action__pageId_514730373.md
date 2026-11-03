---
content_hash: b138d62485334ca470b1ecdc7425ed2745355a9a528673b0d5a61f2e08933008
fetched_at: '2026-06-29T00:10:26.744463+00:00'
page_id: '514730373'
product: rm
source: tdn-rm
title: 6785804 FISCAL01-10662 DT Campo Aliquota ICMS - TIpo Tributação Suspenso ou
  Não Incidência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514730373
version: 2
---

Regra de ICMS

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Regra ICMS |
| Ticket: | 6785804 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Regra ICMS |

## **02. SITUAÇÃO/REQUISITO**

Atualmente, a Alíquota ICMS na Natureza Fiscal fica com percentual zerado quando o Tipo Tributação é Suspenso ou Não Incidência. 

Com o comportamento atual do sistema, o Valor do ICMS Desonerado fica sempre zerado caso o sistema esteja parametrizado para utilizar a Alíquota do ICMS da Natureza Fiscal, pois o Valor do ICMS Desonerado é calculado de acordo com a Base de Cálculo do ICMS x Alíquota do ICMS da Natureza Fiscal (ou Alíquota do ICMS por Estado). Nesse cenário, para que o Valor do ICMS Desonerado seja devidamente calculado, será necessário que o campo Alíquota ICMS (da Natureza Fiscal) fique disponível para que o usuário consiga informar um % diferente de 0 (zero) quando o Tipo Tributação for Suspenso ou Não Incidência.

## **03. SOLUÇÃO**

Funcionalidade: Regra de ICMS - Habilitação do campo Alíquota de ICMS

**Cenário I: Campo Habilitado -  Alteração Realizada**

Dado que o flag de ICMS Desonerado está habilitado

E o tipo de tributação é Isento, Não Incidência ou Suspenso

Ao efetuar o CRUD da regra de ICMS

O campo Alíquota de ICMS deve estar habilitado

**Cenário II: Campo Habilitado - Tipos de Tributação com alíquota**

Dado que o tipo de tributação é Tributado, Outros ou Diferido

Ao efetuar o CRUD da regra de ICMS

O campo Alíquota de ICMS deve estar habilitado

**Cenário III: Campo Habilitado - Diferencial de alíquota**

Dado que o tipo de operação é diferencial de alíquota e o tipo de tributação é não incidência

Ao efetuar o CRUD da regra de ICMS

O campo Alíquota de ICMS deve estar habilitado

**Cenário IV: Campo Habilitado - Sem ICMS Desonerado**

Dado que o flag de ICMS Desonerado está desabilitado

E o tipo de ICMS é isento 

E o tipo de operação tributária é substituição tributária ou diferencial de alíquota

Ao efetuar o CRUD da regra de ICMS

O campo Alíquota de ICMS deve estar habilitado

**Cenário V: Campo Desabilitado**

Dado que não ocorreu nenhum dos casos anteriores

Ao efetuar o CRUD da regra de ICMS

O campo Alíquota de ICMS deve estar desabilitado
