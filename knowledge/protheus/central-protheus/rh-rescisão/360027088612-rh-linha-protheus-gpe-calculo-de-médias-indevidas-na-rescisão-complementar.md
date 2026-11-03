---
article_id: 360027088612
category: RH - Rescisão
content_hash: ee5f4ef45170aee16721f7c97d7d94b0490c81aabd36fb5a5d937ee7dc2f66e8
fetched_at: '2026-06-28T22:43:48.511929+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Calculo de médias indevidas na rescisão complementar
type: support-article
updated_at: '2026-06-25T13:45:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027088612-RH-Linha-Protheus-GPE-Calculo-de-m%C3%A9dias-indevidas-na-rescis%C3%A3o-complementar
---

**Dúvida**  
Calculo de médias indevidas na rescisão complementar  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Cenário

Data de admissão: 15/09/2008

Data de demissão: 28/08/2017

Rescisão complementar: 23/04/2019

Ao calcular a rescisão complementar sistema calcula as verbas de médias indevidamente, estas verbas de médias não fazem parte do calculo da rescisão original.

Ao realizar a impressão do demonstrativo de médias o sistema demonstra períodos desde outubro de 2008, por este motivo o sistema está calculando as médias indevidamente.

Para este cenário deverá entrar no cadastro controle de dias de direito, tabela SRF, localizar a matricula, entrar na opção manutenção e verificar se nesta tabela existe todos os períodos aquisitivos (desda da data da admissão até o desligamento) para o empregado, caso não tenha, deverá informar período a período.

Campos importantes no preenchimento:

Cod. Verba "RF\_PD"

Dt. Ini. Per "RF\_DATABAS"

Dt. Fim. Per "RF\_DATAFIM"

Qd. Ref. Per. "RF\_DIASDIR"

Situação "RF\_STATUS", para este campo deverá informar **pago** para os períodos efetivamente pago, se deixar ativo o sistema irá pagar as férias que não foram quitadas na época na rescisão.

após realizar este ajuste, calcular a rescisão complementar e emitir o demonstrativo de médias observando se o sistema montou corretamente o demonstrativo de médias com os períodos corretos.

**Saber Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
