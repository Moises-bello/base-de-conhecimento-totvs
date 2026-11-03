---
article_id: 360019473792
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 65652db3831060d8535e385d876fa9b988976ad024b3e4a12757967b5291ca83
fetched_at: '2026-06-28T22:39:30.662392+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Campo F4_DESCOND
  - Desc Condici '
type: support-article
updated_at: '2021-07-29T14:37:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019473792-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Campo-F4-DESCOND-Desc-Condici
---

**Dúvida**  
Como configurar o Protheus para que a operação seja calculada com

desconto condicional?  
  
**Ambiente**  
Protheus – Financeiro – A partir da versão 11.80  
  
   
**Solução**Caso a operação tenha desconto condicional informar, será necessário configurar o campo F4\_DESCOND.

Se o conteúdo estiver = **Sim**, o desconto não vai ser deduzido da base do ICMS:

Exemplo:

R$ 1.000,00 mercadoria

R$ 10,00 desconto

F4\_DESCOND = **SIM**  
base do ICMS R$ 1.000,00

F4\_DESCOND = **NÃO**  
base do ICMS R$  990,00

 Maiores informações, consulte o link abaixo:

http://tdn.totvs.com/display/public/PROT/Campo+F4\_DESCOND+--+112252
