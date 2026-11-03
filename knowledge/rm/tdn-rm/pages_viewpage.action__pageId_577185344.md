---
content_hash: de85d67dc9b39e6c582b83435a057ef13bb69ee2eed6c5d0c4737b86e2c4912e
fetched_at: '2026-06-29T00:10:53.120571+00:00'
page_id: '577185344'
product: rm
source: tdn-rm
title: Atualização de hora final  para Honorário e SADT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577185344
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Regras**
   1. **Honorário**
   2. **SADT**
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Ao executar a rotina de encerramento da parcial, caso o atendimento de **Honorário** ou **SADT**esteja com a **hora final** do procedimento vazio, será atualizado o valor regras abaixo.

Regras

## **02.****REGRAS**

Todos os parâmetros citados a seguir estão localizados nas **"Condições Contratuais com Convênios".**

filhosHonorário

## **A. Honorário**

**Quando**

* **Estiver** marcado o parâmetro “**Usa data e hora do honorário como período de início e fim**” ou ”**Usa TISS pacote como procedimento**”, deverá ser atualizado utilizando a data de realização do honorário.
* Houver uma **data final para a parcial** e **não estiver** marcado o parâmetro “**Horário final da cirurgia igual ao horário inicial**”, deverá ser atualizado utilizando a hora da data final da parcial.
* Houver uma **data final para a parcia**l e **estiver** marcado o parâmetro “**Horário final da cirurgia igual ao horário inicial**”, deverá ser atualizado utilizando a hora da data inicial da parcial.
* Houver algum **procedimento****cirúrgico** e **estiver** marcado o parâmetro “**Usa data e hora do registro de informações****cirúrgicas**”, deverá ser atualizado utilizando a hora final do procedimento cirúrgico. **Esta sobrepõem as anteriores.**
SADT

## **B. SADT**

**Quando**

* **Consulta externa** e **estiver** marcado o parâmetro “**Hora Final de Exames igual a hora de saída do paciente”**, deverá ser atualizado utilizando a hora final da realização do procedimento.
* **Consulta interna**, deverá ser atualizado utilizando a hora inicial da realização do procedimento.

## **03. TABELAS UTILIZADAS**

* **SZATENDHONORARIO**
* **SZATENDSADT**
]]>
