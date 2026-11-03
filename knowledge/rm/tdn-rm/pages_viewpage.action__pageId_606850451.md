---
content_hash: bfda1ba7d8417156afc8c9c44b5f59a7035274214334d14b9f3e7f725de7d29b
fetched_at: '2026-06-29T00:10:58.790936+00:00'
page_id: '606850451'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Agendamento > Registro de Atendimento
  Externo com Lançamento de procedimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=606850451
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. **Parametrizações**
   2. **Agendamento**
   3. **Registro de Atendimento**
   4. **Lançamento na Conta**

## **01. VISÃO GERAL**

O objetivo desta funcionalidade é informar no agendamento, qual procedimento deverá ser lançada na conta do paciente **particular**. Para que isso ocorra, deve-se parametrizar o sistema conforme será descrito neste documento.

A funcionalidade é semelhante ao que ocorre com os convênios que utilizam o padrão TISS.

## **02. EXEMPLO DE UTILIZAÇÃO**

falseProcessoParametrizações

Marque a opção abaixo para o procedimento informado no agendamento, seja lançado na conta do paciente.

**Menu Ambiente> Gestão hospitalar > TISS - parâmetros para faturamento> Lança procedimentos de agendamento na conta do paciente em WS TISS**

Como o procedimento informado no agendamento é registrado na aba Guia/Autorização do Registro de Atendimento, deve-se configurar quais faixas de código serão considerados para inclusão na conta do paciente.

Somente as seguintes faixas são consideradas: consulta, clínica médica, exames e pacotes.

**Menu Ambiente> Gestão hospitalar > Faturamento > Autorizações**

Configurados os parâmetros gerais, pode-se definir para cada convênio/contrato se é para lançar na conta do paciente ou não, ao incluir algum item na aba de Guias/Autorizações

Agendamento

Ao realizar um agendamento, utilizando o convênio Particular, deve-se informar o campo Procedimento, para que o mesmo seja lançado na conta do paciente

Registro de Atendimento

Quando o paciente chegar para a consulta, clique no botão Atend. Externo, para registrar o atendimento e neste momento, o lançamento em conta já ocorrerá.

Lançamento na Conta

Após registrar o atendimento, o procedimento informado no agendamento será lançado na conta do paciente, conforme parametrizações acima
