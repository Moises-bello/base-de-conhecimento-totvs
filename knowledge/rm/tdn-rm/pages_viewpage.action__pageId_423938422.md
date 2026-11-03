---
content_hash: a84f0934dbd8ad15f7def78800fde50c0e597d7e51566897f0b4cb595c54f63d
fetched_at: '2026-06-29T00:09:26.779023+00:00'
page_id: '423938422'
product: rm
source: tdn-rm
title: Eventos Contábeis de Reavaliação/Avaliação Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938422
version: 3
---

Validação dos eventos contábeis de avaliação/reavaliação patrimonial:

**Evento contábil de Ajustes da Avaliação Patrimonial**

Este evento será utilizado somente quando for implementado o processo de Avaliação no Bonum.NET. Contabiliza a aquisição da Avaliação. No caso de bases convertidas estas aquisições já foram feitas em versões anteriores a 11.50, portanto este evento não será utilizado. Este por sua vez, possui a seguinte configuração:

* Débito – busca o default contábil do grupo de patrimônio da conta que está classificada como PATRIMONIO
* Crédito – busca o default contábil do grupo de patrimônio da conta que está classificada como PATRIMAVAL.

**Evento Contábil de Realização de Ajustes da Avaliação Patrimonial**

Deve-se conferir o evento Realização de Ajustes de Avaliação. Este evento irá contabilizar o valor de realização da avaliação. A realização é somente com base no valor dos patrimônios avaliados. Este evento possui a seguinte configuração:

* Débito – busca o default contábil do grupo de patrimônio da conta que está classificada como PATREAAVAL.
* Crédito – busca o deafult contábil do grupo de patrimônio da conta que está classificada como PATRECAVAL.

**Evento Contábil de Baixa de Ajustes da Avaliação Patrimonial**

Este evento será utilizado quando ocorrer, por exemplo, a baixa dos patrimônios avaliados. Se o patrimônio avaliado for baixado por algum motivo, ocorrerão a baixa do valor do patrimônio com sua depreciação acumulada e também a baixa da avaliação com sua realização acumulada. Este evento possui a seguinte configuração:

* Débito – busca a conta que será informada no processo e aplica na "Baixa – Valor Patrimonial".
* Crédito – busca conta do grupo de patrimônio classificada como PATRIMONIO e aplica "Baixa – Valor Patrimonial".

Esta contabilização vai baixar o valor do patrimônio.

* Débito – busca a conta do grupo de patrimônio classificada como DEPACUM e aplica "Baixa (Depreciação Acumulada)".
* Crédito – busca a conta que será informada no processo e aplica na "Baixa (Depreciação Acumulada".

Esta contabilização vai baixar o valor de depreciação acumulada do patrimônio.

* Débito – busca a conta que está informada no grupo de patrimônio como PATRIMAVAL e aplica "Avaliação – Baixa Avaliação"
* Crédito – busca a conta que será informada no processo e aplica "Avaliação – Baixa Avaliação"

Esta contabilização vai baixar o valor de Avaliação do patrimônio.

* Débito – busca a conta que será informada no processo e aplica "Avaliação – Realização Acumulada"
* Crédito – busca a conta que está informada no grupo de patrimônio como PATREAAVAL e aplica "Avaliação – Realização Acumulada".

Esta contabilização vai baixar o valor da Realização Acumulada do patrimônio.

OBS: No evento de baixa de avaliação foram disponibilizados também os itens para contabilização de ganho ou perda, caso na baixa seja marcada a opção para geração de Ganho/Perda a contabilização deste valor poderá ser feita no patrimônio avaliado.

O que vale ressaltar é que existem dois patrimônios, mas o valor do patrimônio é um só, portanto se o usuário baixar o patrimônio avaliado gerando ganho ou perda, o mesmo deve ficar atento ao cálculo do valor de venda que será informado para cada patrimônio.

**Evento Contábil de Correção Monetária da Avaliação Patrimonial (Positiva)**  
Este evento será utilizado para corrigir o patrimônio avaliado. O que ocorre é que o valor do patrimônio avaliado faz parte do valor total do patrimônio. Então neste caso o valor do Patrimônio avaliado sofre as seguintes correções:

* Correção do valor do Patrimônio
* Correção do valor da depreciação acumulada
* Correção do valor da avaliação
* Correção do valor da Realização Acumulada da Avaliação

Sendo assim, o evento deve estar configurado da seguinte maneira:

* Débito – busca o default contábil do grupo de patrimônio classificado como PATRIMÔNIO e aplica "Correção Monetária (Conta Patrimônio)".
* Crédito – busca o default contábil do grupo de patrimônio classificado como PATCORRECA e aplica "Correção Monetária".

Esta contabilização vai corrigir o valor do Patrimônio.

* Débito – busca o default contábil do grupo de patrimônio classificado como PATCORRECA e aplica "Depreciação Acumulada"
* Crédito – busca o default contábil do grupo de patrimônio classificado como PATDEPACUM e aplica em "Depreciação Acumulada"

Esta contabilização vai corrigir o valor da depreciação acumulada.

* Débito – busca o default contábil do grupo de patrimônio classificado como PATCORAVAL e aplica em "Correção Monetária da Avaliação"
* Crédito – busca o default contábil do grupo de patrimônio classificado como PATRIMAVAL e aplica em "Conta de Avaliação"

Esta contabilização vai corrigir o valor da avaliação.

* Débito – busca o default contábil do grupo de patrimônio classificado como PATREAAVAL e aplica em "Correção monetária da Avaliação Acumulada"
* Crédito – busca o default contábil do grupo de patrimônio classificado como PATCORAVAL  e aplica em "Correção monetária da Avaliação Acumulada".

Esta contabilização vai corrigir o valor da realização da avaliação acumulada.

**Evento Contábil de Correção Monetária da Avaliação Patrimonial (Negativa)**

Este evento possui a mesma lógica do evento acima, porém os itens de eventos serão invertidos, pois neste caso a correção monetária será negativa.
