---
article_id: 360016125731
category: MDFe - Manifesto de Carga
content_hash: cd450aa8ce0f37a6dd5d4a55c9c4cb8c8e9d294acb523283838d3f7fd5b605cf
fetched_at: '2026-06-28T22:40:08.291300+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Falha de
  Schema tpRod
type: support-article
updated_at: '2025-06-10T19:37:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016125731-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Falha-de-Schema-tpRod
---

**Dúvida**Falha de Schema tpRod

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**Ao transmitir MDFe ocorre a seguinte falha de Schema:

O erro ocorre na ***tag <tpRod>*** que está preenchida como 00.

* Conforme Manual de Orientação do Contribuinte do MDFE da SEFAZ, seguem as opções de Tipo de Rodado:

Preencher com:

* 01 - Truck;
* 02 - Toco;
* 03 - Cavalo Mecânico;
* 04 - VAN;
* 05 - Utilitário;
* 06 - Outros.

Com isso o conteúdo 00 não pode ser utilizado para a transmissão do MDFE, porém o campo é utilizado para outras rotinas.

Para a correção preencha os campos abaixo:

1. Preencher no **cadastro de veículos** o campo **DA3\_TIPVEI  "Tipo Veiculo"**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048838533)

2. Em **"Tipo Veiculo"**, clicar na lupa,  assim que apresentar  uma nova tela, preencher os dois campos **DUT\_TIPROD "Tp. Rodado"**e **DUT\_TIPCAR "Tp. Carroce."**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047965234)**

**Obs:** Importante que os campos **DA3\_ CAPACN e DA3\_CAPACM** estejam preenchido nos cadastro do veiculo e do reboque  para gerar a tag **capKG.** O tamanho desses campos devem ser preenchidos com o tamanho máximo de 6 dígitos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23022310987287)
