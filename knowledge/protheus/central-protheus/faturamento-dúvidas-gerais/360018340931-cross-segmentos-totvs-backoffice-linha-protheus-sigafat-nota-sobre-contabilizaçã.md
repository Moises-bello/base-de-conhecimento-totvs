---
article_id: 360018340931
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8d8d021025424d39a72090200c63752b3c89688247b755cb878263b46cc0fcb5
fetched_at: '2026-06-28T22:38:30.114284+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Nota sobre Contabilização
  para Nota Fiscal de Serviço Eletrônica
type: support-article
updated_at: '2023-10-04T11:33:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018340931-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-Contabiliza%C3%A7%C3%A3o-para-Nota-Fiscal-de-Servi%C3%A7o-Eletr%C3%B4nica
---

**Dúvida**

Existe lançamento padrão para contabilização do número da **NF de Serviços Eletrônica** após a transmissão?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - todas as versões.

**Solução**

Não existe LP (**lançamento padrão**) para contabilizar a **NFSe** (**Nota Fiscal de Serviço Eletrônica**) de faturamento após sua transmissão.

Os LPs para contabilizar o  RPS são **610 e 620**, onde é possível contabilizar on line, ou contabilizar depois, através do menu miscelâneas, fechamento, contabilização off line, mas ainda sim, o que vai determinar o número a ser contabilizado é a query do LP no histórico de lançamento. No histórico de lançamento, poderá indicar os campos **F2\_doc** ou **D2\_Doc** na query para demonstrar o número do documento, só que este número é o número interno do Protheus, para controle do sistema.

 O código de **NFse**, somente é fornecido posteriormente pela prefeitura, sendo que há prefeituras que mantém o mesmo número de **RPS** e são poucas as que mandam outra numeração de nota , mas esta numeração é um  processo  efetuado no **TSS** e não na geração da nota via rotina **mata461**.

Este é o conceito de processo dentro Sistema.

Paliativamente, pode-se adequar o processo de contabilização para contabilizar off line após a transmissão e quando a prefeitura retornar com o número da nota de serviço, onde o LP atual de contabilização deverá ser atualizado  o seu histórico para informar o número da nota pelo campo **F2\_NFELETR** ao invés do **F2\_doc**, exemplo de histórico: "**Nota de serviço:  "+F2\_NFELETR +"  ref RPS:  " + SF2->F2\_DOC+" - "+SF2->F2\_SERIE .**

 Mas esse controle deverá ser efetuado internamente, gerando talvez um atraso para contabilizar as notas, mas tratando da forma que atenda a necessidade de cada empresa dentro do padrão do sistema.

Maiores detalhes de como são utilizados os lançamentos de contabilização dentro do faturamento, segue link da faq no tdn: **[Integração Faturamento X SigaCtb (SIGAFAT)](https://tdn.totvs.com/x/W2nXIQ)**
