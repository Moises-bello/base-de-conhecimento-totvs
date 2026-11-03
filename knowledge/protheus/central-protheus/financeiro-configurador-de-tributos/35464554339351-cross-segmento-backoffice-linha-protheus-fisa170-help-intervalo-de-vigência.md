---
article_id: 35464554339351
category: Financeiro - Configurador de Tributos
content_hash: 7efa5fb4873736ac5d8f8137362125c1e04b3076f4cf07d303f0fba0fd5eb932
fetched_at: '2026-06-28T22:37:45.787943+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - FISA170 - Help: Intervalo de
  Vigência'
type: support-article
updated_at: '2026-03-23T12:07:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35464554339351-Cross-Segmento-Backoffice-Linha-Protheus-FISA170-Help-Intervalo-de-Vig%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35464554306071) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Help: Intervalo de Vigência. Problema: valores incorretos para a composição do intervalo. Existe uma versão com vigência conflitante com a informada (vigência inicial e final internas).  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**  
Ao alterar a regra financeira, é exibida a mensagem de **Help: Intervalo de Vigência**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464532181911)

Este erro ocorre porque a vigência da regra está em vigor e não pode ser alterada. Para realizar a alteração, é necessário ajustar o período de vigência.

Para realizar o ajuste, clique em **Outras ações > Ajustar vigência.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464554309271)

Em seguida, será necessário ajustar o período de vigência conforme o exemplo abaixo:

* **Início da vigência:** 01/01/2025
* **Fim da vigência:** 31/12/2025

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464532186391)

Ajustado para:

* **Início da vigência:** 01/01/2025
* **Fim da vigência:** 01/01/2025

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464554312471)

A mensagem abaixo será exibida; confirme para continuar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464554313751)

Em seguida, clique em **Outras Ações > Alterar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464554315159)

Realize os ajustes necessários, incluindo o período de vigência. No exemplo abaixo, o ajuste foi realizado no campo **"Aplica-se à Carteira"**, selecionando a opção **1 – Pagar** e  confirme a alteração.

* **Início da vigência:** 02/01/2025
* **Fim da vigência:** 31/12/2025

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464532192663)

Uma nova regra financeira será gerada, identificada como **versão 0002**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464554318103)

É necessário desabilitar a versão anterior. Clique em **Ativar/Desativar.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464532196759)

No campo **Ativo**, selecione **2 – Não** e confirme a alteração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35464532197655)

Como alternativa, é possível também clicar em **Outras Ações> Copiar**, realizar os ajustes necessários e desativar a regra anterior.

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
