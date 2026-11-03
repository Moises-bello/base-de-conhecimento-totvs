---
content_hash: c237ee40faca82e3830ab1da16cdff04f393df5a15723cad188456daac0c5ff4
fetched_at: '2026-06-29T00:10:37.827239+00:00'
page_id: '540899121'
product: rm
source: tdn-rm
title: Configurações Gerais 6/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540899121
version: 26
---

false⚠️ ATENÇÃO: Mudança na Geração do XML

Processo descontinuado será realizado o De/para através da aba eSocial diretamente no cadastro de eventos. a partir das versões

Nesta aba é possível fazer as Configurações Gerais relacionadas ao eSocial:   
   
**De/Para eventos férias eSocial (S-1200) para eventos do envelope de pagamento**

Evento IRRF Férias envelope e Evento Pensão Férias envelope

Quando existe verba de IRRF de Férias (cc30 e/ou cc107) e/ou Pensão Alimentícia de Férias (cc113) no envelope de pagamento, no leiaute 2.5 essas verbas não são levadas no evento S-1200, porém elas também compõem o valor da tag **<vrLiq>** do S-1210 (conforme manual do eSocial)  ou no leiaute S-1.0 recibo de ferias no S-1200.

Com isso houve a necessidade em criar o parâmetro **De/Para** para que as verbas acima sejam levadas como desconto no evento S-1200.

**ATENÇÃO:** Os eventos informados nos campos acima, deverão ser do tipo desconto, sem código de cálculo, sem incidência e com natureza da rubrica 9299 - Outros descontos não previstos nos itens anteriores.

Evento INSS Férias Alíquota Normal envelope E Evento INSS Férias Próximo Mês Alíquota Normal Envelope

As verbas INSS Férias com Alíquota Normal (cc90) e INSS Férias Próximo Mês Alíquota Normal envelope (cc137) são geradas no evento S-1010 com a tag <CodIncIRRF> igual a **"43-Deduções da base de cálculo do IRRF de Férias"**, e estas verbas são lançadas tanto no recibo de férias quanto no envelope de pagamento, gerando duplicidade de informações, com isso houve a necessidade em criar os parâmetros **De/Para** para que as verbas acima sejam levadas para o evento S-1200 corretamente sem nenhuma incidência.   

**ATENÇÃO:**eventos dos campos acima, deverão ser do tipo Base de calculo, sem código de cálculo, sem incidências.

Evento Abono Férias envelope

As verbas relacionadas ao abono pecuniário código de calculo **[39](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719764) e [47](https://tdn.totvs.com/pages/viewpage.action?pageId=452718717)** que não tem incidência em IRRF de Férias são geradas com a tag <CodIncIRRF> igual a **"75-Não tributável ou isento de IRRF de Férias"**, e estas verbas são lançadas tanto no recibo de férias quanto no envelope de pagamento, gerando duplicidade de informações, com isso houve a necessidade em criar os parâmetros **De/Para** para que as verbas acima sejam levadas para o evento S-1200 corretamente sem nenhuma incidência.   

**ATENÇÃO:**evento do campo acima, deverão ser do tipo provento, sem código de cálculo, sem incidências.

Evento INSS Férias envelope:

Essa verba tem o proposito de substituir a verba com código de cálculo "82-INSS Férias" existente no envelope de pagamento para envio no evento S-1200 ao eSocial

Essa implementação foi necessária devido às diretrizes estabelecidas pelo leiaute S-1.0, que indicam que os valores relacionados às incidências de IRRF devem ser reportados no recibo de férias.

Na geração do XML do envelope de pagamento, o produto realizará a substituição desse código de cálculo por meio do evento mencionado neste parâmetro.

O montante gerado nessa verba corresponderá à soma dos eventos com o código de cálculo [82 - INSS Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452718205).

**ATENÇÃO:** A verba informada acima, deverá ser do tipo "Desconto" e sem incidências. 

Importante!

Após a inserção da verba neste parâmetro, torna-se imprescindível gerar e enviar o XML S-1010 correspondente a essa verba. Essa etapa é fundamental para garantir a correta geração das tags **<codIncCP>** e **<codIncIRRF>**.

Evento INSS Férias Próximo Mês envelope:

Essa verba tem o proposito de substituir as verbas com códigos de cálculo "130 - INSS Férias Próximo Mês" e "349 - INSS Férias no Terceiro Mês" existentes no envelope de pagamento para envio no evento S-1200 ao eSocial.

Essa implementação foi necessária devido às diretrizes estabelecidas pelo leiaute S-1.0, que indicam que os valores relacionados às incidências de IRRF devem ser reportados no recibo de férias.

Na geração do XML do envelope de pagamento, o produto realizará a substituição desses códigos de cálculos por meio do evento mencionado neste parâmetro.

O montante gerado nessa verba corresponderá à soma dos eventos com os códigos de cálculos: [130 - INSS Férias Próximo Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718229) e [349 - INSS Férias no Terceiro Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719459).

**ATENÇÃO:** A verba informada acima, deverá ser do tipo "Desconto" e sem incidências. 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
