---
content_hash: f7ce9eb9aa9db7809b7c09de40bc6ef4e14d2677a34fd592f4bba5a5243be72d
fetched_at: '2026-06-29T00:10:03.670062+00:00'
page_id: '452719125'
product: rm
source: tdn-rm
title: Evento por Tipo de Ocorrência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719125
version: 4
---

Esse anexo somente ficará disponível quando selecionado o código de cálculo 0043 (Tipo Ocorrência), esse por sua vez serve para calcular um evento que contenha tipos de ocorrências customizada pelo usuário ou ocorrências nativas do produto como atrasos, extras, faltas etc.., uma vez associado os tipos de ocorrência ao evento esse será considerado na movimentação.

**Exemplo:** Código e Descrição do Evento: TO01 - TIPO OCORRÊNCIA ADICIONAL NOTURNO, Código de Cálculo: 0043 - Tipo Ocorrência Eventos por Tipo de Ocorrência associados:

ADN - Adicional Noturno, ADFN - Adicional Noturno Extra Feriado Não Autorizado, ADF - Adicional Noturno Extra Feriado Autorizado, ADEN - Adicional Noturno Extra Normal Não Autorizado, ADE - Adicional Noturno Extra Normal Autorizado, ADDN - Adicional Noturno Extra Descanso Não Autorizado, ADD - Adicional Noturno Extra Descanso Autorizado, ADCN - Adicional Noturno Extra Compensado Não Autorizado, ADC - Adicional Noturno Extra Compensado Autorizado.

No exemplo acima todas as ocorrências de Adicional Noturno foram associadas ao evento TO01 - TIPO OCORRÊNCIA ADICIONAL NOTURNO.

Na movimentação do funcionário, será lançado o evento TO01 - TIPO OCORRÊNCIA - ADICIONAL NOTURNO com o somatório de todas as horas de Adicional Noturno que o funcionário realizou, se este evento estiver associado ao parâmetro do sindicato | etapa Eventos.
