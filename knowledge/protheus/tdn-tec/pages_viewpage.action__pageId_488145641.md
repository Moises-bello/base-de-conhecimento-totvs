---
content_hash: f1220c0ded09c57961139fb3da318bb9080a7906a69d5b3d7817dfe6fdd162f8
fetched_at: '2026-07-02T19:24:24.317179+00:00'
page_id: '488145641'
product: protheus
source: tdn-tec
title: DBAccess - Seção [General], chave CheckDeadLock
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=488145641
version: 6
---

CheckDeadLock

Habilita o true Master (quando utilizada configuração distribuída ) ou o true Standalone a identificar processos em DEADLOCK por tentativa de bloqueio de registros dos processos em execução no mesmo.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| **0 (default)** | Desabilita o mecanismo de identificação de Deadlock |
| 1 | Habilita o mecanismo de identificação de Deadlock |

---

## Exemplo:

---

## Observações

* Quando utilizado o true em modo distribuído, esta configuração deve ser utilizada no true Master

* A partir do DBAccess Build 20191119, o valor *default* desta configuração passa a ser 1 ( habilitada ).

* A partir do DBaccess Build 20200606, o valor *default* desta configuração voltou a ser 0 ( desabilitada ).
* Essa configuração, quando alterada, exige que o serviço do true seja reiniciado para que a nova configuração seja considerada
* Caso seja identificado um Deadlock no bloqueio de registros entre dois ou mais processos, a informação retornada ao true sobre o processo que está bloqueando o registro irá informar que a situação de Deadlock foi identificada
* Para autorizar o true a finalizar um dos processos envolvidos para dar a chance dos demais serem finalizados com sucesso, sem não manter a aplicação bloqueada em loop, deve ser utilizada a configuração **DeadLockExit** na configuração do Database e/ou Ambiente (Esta configuração, quando utilizada em true distribuído, deve ser colocadas nos serviços do true configurados como slave)

---

## Veja também
