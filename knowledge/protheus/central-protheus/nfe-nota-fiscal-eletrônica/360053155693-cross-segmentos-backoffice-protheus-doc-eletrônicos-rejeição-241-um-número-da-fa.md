---
article_id: 360053155693
category: NFe - Nota Fiscal Eletrônica
content_hash: 77d1f2cfcf6245fdf458c7f5aaca9e6f609542873104244750f4f3d6cac856a5
fetched_at: '2026-06-28T22:40:01.932940+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 241:
  Um número da faixa já foi utilizado'
type: support-article
updated_at: '2022-06-01T18:43:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053155693--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-241-Um-n%C3%BAmero-da-faixa-j%C3%A1-foi-utilizado
---

**Dúvida**Como resolver a rejeição 241: Um número da faixa já foi utilizado ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**Ao tentar transmitir o cancelamento ou inutilização de uma numeração já utilizada na Sefaz, será retornada a rejeição 241 - Um número da faixa já foi utilizado.

Não se pode cancelar/inutilizar numerações de nfe quando já foram **Autorizadas**, **Canceladas**, **Denegadas** ou quando há um **Evento EPEC** vinculado a numeração (mesmo que o **EPEC** ainda não tenha sido conciliado, ou seja, **nfe autorizada**).

* **Exemplo:**

Foi emitida uma nota, que foi denegada por irregularidade do destinatário. Em seguida, o emissor da nota realizou a inutilização da numeração. Nessa situação, a inutilização será rejeitada pelo motivo 241.

Vide regra de validação da Sefaz:

![](http://www.oobj.com.br/bc/assets/Articles/295/Rej241_NFE.PNG)

Existem casos que, por algum problema de comunicação (seja da Sefaz ou do cliente), o TSS não recebeu da Sefaz o retorno de autorização **do cancelamento**, **da inutilização**, **da denegação** ou do **vínculo do EPEC** em suas tabelas.

Neste caso, tente localizar a chave da nota que está tendo a rejeição 241 em sua base de TSS, para se certificar que houve uma transmissão anterior desta nota.  
  
É possível ainda, consultar a inutilização da nota na Sefaz com os dados de CNPJ do emissor, série e número e ano de emissão da nota. Vide link da Sefaz <http://www.nfe.fazenda.gov.br/portal/consulta.aspx?tipoConsulta=inutilizacao&tipoConteudo=YG1QjUXR4PY=>

Caso não localize a chave da nota em sua base de dados ou na Sefaz, sugerimos contatar a Sefaz Estadual (por email, informando o CNPJ emissor, a série e número da nota), solicitando informações da situação da referida nota em seu ambiente.
