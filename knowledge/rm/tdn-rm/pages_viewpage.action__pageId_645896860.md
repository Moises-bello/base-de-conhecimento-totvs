---
content_hash: e9fbfee6865505125cc9e695c6bfca5ae2cd654e8777473fcc247d0ccca4a836
fetched_at: '2026-06-29T00:11:11.124555+00:00'
page_id: '645896860'
product: rm
source: tdn-rm
title: Configurações Gerais 7/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=645896860
version: 21
---

false⚠️ ATENÇÃO: Mudança na Geração do XML

Processo descontinuado será realizado o De/para através da aba eSocial diretamente no cadastro de eventos. a partir das versões

### **De/Para Eventos Antecipação de Férias eSocial (S-1200)**

Devido a instrução liberadas no MOS do leiaute S-1.0 referente ao recibo de férias, foi necessário a criação do "De/Para" para os eventos do recibo de férias.

Veja os detalhes em 

Evento Antecipação de Férias (Vencimento):

Essa verba será utilizada para envio dos valores da antecipação de férias para eSocial (leiaute S-1.0).

O valor gerado nessa verba será:

 evento com código de cálculo 38

 proventos sem código de cálculo e com incidência em INSS

 descontos sem código de cálculo e com incidência em INSS ou o código de cálculo 447 para verde amarelo.

**ATENÇÃO**:

A verba informada no campo acima deverá ser do tipo "Provento" e com incidência somente em IRRF de férias. 

Caso possua verbas de médias no recibo de férias essas também serão somadas as verbas de antecipação de férias.

Evento Antecipação Terço de Férias (Vencimento):

Essa verba será utilizada para envio dos valores da antecipação do terço de férias para eSocial (leiaute S-1.0).

O valor gerado nessa verba será:

 evento com código de cálculo 40

 evento com código de cálculo 310

**ATENÇÃO**: A verba informada no campo acima deverá ser do tipo "Provento" e com incidência somente em IRRF de férias.

Evento INSS Antecipação de Férias(Desconto):

Essa verba será utilizada para envio dos valores da provisão de INSS de férias para eSocial (leiaute S-1.0).

O valor gerado nessa verba será:

evento com código de cálculo 82 e código de cálculo 130

**ATENÇÃO**: A verba informada no campo acima deverá ser do tipo "Desconto" e sem incidências. 

Importante!

Após a inserção da verba neste parâmetro, torna-se imprescindível gerar e enviar o XML S-1010 correspondente a essa verba. Essa etapa é fundamental para garantir a correta geração das tags **<codIncCP>** e **<codIncIRRF>**.

Evento Antecipação Primeira Parcela 13º nas Férias(Provento):

Essa verba será levada no S-1200 substituindo o valor do código de calculo 9 existente no envelope. 

O valor gerado nessa verba será:

 evento com código de cálculo 9

**ATENÇÃO**: A verba informada no campo acima deverá ser do tipo "Provento" e sem incidências em FGTS 13. 

Evento Salário Família Antecipação de Férias (Provento):

Essa verba será utilizada para envio dos valores da antecipação do salário família nas férias para eSocial.

O valor gerado nessa verba será:

 evento com código de cálculo 149

**ATENÇÃO:** A verba informada no campo acima deverá ser do tipo "Provento". 

 

### **IMPORTANTE:**

* Caso utilize tomador de serviço o recibo de antecipação de férias será gerado para o tomador empresa.
