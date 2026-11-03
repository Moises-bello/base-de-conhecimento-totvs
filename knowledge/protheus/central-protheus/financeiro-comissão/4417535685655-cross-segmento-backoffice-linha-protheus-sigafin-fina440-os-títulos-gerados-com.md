---
article_id: 4417535685655
category: Financeiro - Comissão
content_hash: 2a88470b378f074581060c054f21d9f703c87782f0d46352bd73e3726b6fa265
fetched_at: '2026-06-28T22:37:50.711528+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA440 - Os títulos
  gerados com Tipo CC não estão deduz o ICMS da base de comissão
type: support-article
updated_at: '2025-07-30T20:19:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417535685655-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA440-Os-t%C3%ADtulos-gerados-com-Tipo-CC-n%C3%A3o-est%C3%A3o-deduz-o-ICMS-da-base-de-comiss%C3%A3o
---

**Dúvida**Os títulos gerados com Tipo CC não estão deduz o ICMS da base de comissão?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA440 - Todas as versões  
  
**Solução**

**Verificação da Origem do Título:**

* Quando o campo **E1\_ORIGEM** for igual a **"MATA460"**, indica que o título a receber possui o tipo **"CC"** (E1\_TIPO), o que demonstra a existência de uma **customização** que altera o padrão de gravação.  
  Nesse caso, **não serão consideradas** as configurações definidas no **cadastro do vendedor**, pois, conforme o padrão do módulo **SIGAFAT**, os títulos dessa origem deveriam ser gravados com o tipo **"NF"**. Somente com o tipo padrão é que o **cálculo da comissão ocorre corretamente**.
* Já quando o campo **E1\_ORIGEM** for igual a **"LOJA701"**, os títulos a receber são originados do módulo **SIGALOJA** e também possuem o tipo **"CC"** (E1\_TIPO). Contudo, para essa origem, a **geração da comissão será realizada conforme as regras previstas no módulo**, ou seja, está de acordo com o comportamento esperado.

**Saiba mais**  
[MP - SIGALOJA - Como realizar Calculo de Comissão](MP%20-%20SIGALOJA%20-%20Como%20realizar%20Calculo%20de%20Comiss%C3%A3o)

[Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)
