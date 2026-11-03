---
content_hash: d7186abf3ca51539293aa893e2c96af00858a616a1ac26e4a60ceb2ce550d46c
fetched_at: '2026-06-29T00:05:47.746481+00:00'
page_id: '1016677348'
product: rm
source: tdn-rm
title: TAA -  DataServer CRMAtendimentoExtData
type: documentation
url: https://tdn.totvs.com/display/LRM/TAA+-++DataServer+CRMAtendimentoExtData
version: 1
---

---

**1 - Dados Gerais**

---

Produto: Totvs CRM

Linha: Linha RM

Módulo: CRM - Atendimento

Função: Consumo REST DataServer via API

País: Brasil

Requisito: Solicitação de documentaçao - DataServer CRMAtendimentoExtData

---

**2 - Operações Suportadas**

---

* GET : Leitura (lista e registro) via DoReadView / DoReadRecord

Por padrão todos os usuários com acesso ao Totvs Aprovações e Atendimento podem visualizar os dados de qualquer atendimento, independentemente do atendente responsável.

A única exceção ocorre quando o nível do acesso do atendimento estiver preenchido com um valor superior ao do atendente associado ao usuário autenticado.

Nesses casos a visualização será restrita apenas ao atendente responsável pelo atendimento ou ao seu superior imediato (chefe).

---

**3 - Instruções Importantes**

---

* Separador correto da PK composta $\_$
* PK composta (ordem):

CODCOLIGADA $\_$ CODLOCAL $\_$ CODATENDIMENTO

**Padrão de url**

* Get (leitura/alteração)

[http://HOST:PORTA/rmsrestdataserver/rest/CRMAtendimentoExtData/{CODCOLIGADA}$\_${CODLOCAL}$\_${CODATENDIMENTO](http://HOSTPORTA)}

* Get registro:

<http://localhost:8051/rmsrestdataserver/rest/CRMAtendimentoExtData/1$_$1$_$100>
