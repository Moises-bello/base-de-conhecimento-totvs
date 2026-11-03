---
article_id: 29652162229143
category: NFe - Nota Fiscal Eletrônica
content_hash: 424f5b252094c7e5abdb89fff8d0df882dde083dc08924486608b5a081718e10
fetched_at: '2026-06-28T22:40:00.095819+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como realizar implementação
  do registro de saída Siare (MG) no ERP
type: support-article
updated_at: '2025-01-31T14:43:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29652162229143-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-realizar-implementa%C3%A7%C3%A3o-do-registro-de-sa%C3%ADda-Siare-MG-no-ERP
---

**Dúvida**  
Como realizar implementação do registro de saída Siare (MG) no ERP ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para realizar a transmissão de uma ou mais nota sem o preenchimento da data de saída devem alterar o parâmetro **MV\_DSAIENT= .T.**

Após realizar a transmissão da nota, com o documento autorizado deve acessar a rotina SPEDNFE e selecionar a opção **4 - Reg. Saída**, conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652158573591)

Em seguida indique o tipo da nota e série:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652162195991)

No primeiro aceso deve configurar os parâmetros em **Outras ações > Parâmetros:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652158577303)

Devem ajustar os parâmetros como exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652162202007)

Após ajuste salve como grupo de administrador "+" e confirme.

Para transmitir o evento deve selecionar a nota, ir em **Outras ações > Transmissão:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652158583959)

A rotina vai abrir um assistente de transmissão com a confirmação do ambiente que está sendo transmitido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652162205079)

Ao avançar devem indicar as informações da data de saída e horário e pode ser indicado o veículo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652158587031)

Ao preencher e avançar o evento será transmitido.

Após a transmissão deve acessar Outras ações > Monitor:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29652158589719)

Indicar a faixa a ser monitorada e verificar o retorno da transmissão.
