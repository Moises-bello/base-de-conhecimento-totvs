---
article_id: 360036123334
category: RH - Cálculo Adiantamento
content_hash: ca861f36846404d2e2311c6550c5eb21a02129b206ba4d1330b5ef2381530329
fetched_at: '2026-06-28T22:43:14.291298+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração de verbas para Adiantamento (regime
  competência)
type: support-article
updated_at: '2025-08-25T20:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036123334-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-para-Adiantamento-regime-compet%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24428400993431)**Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Como configurar as verbas de Adiantamento para regime competência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Para que o adiantamento seja pago conforme regime Competência, deverá entrar na **rotina Verbas em Atualizações > Definições de Cálculo Verbas (GPEA040)** e alterar as verbas relacionadas aos IDs abaixo. Um exemplo de regime competência seria Folha de Pagamento de Agosto/2025 com data de pagamento até 31/08/2025 (Dentro do mesmo mês de competência.   
Nos campos selecionados da **aba Incidências**, alterar conforme cada ID mencionado a seguir:

**Id\_calculo 0006**

![](https://i.imgur.com/riMVyVw.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436486499223)

**Id\_calculo 0007**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440152855)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440154135)

**Id\_calculo 0008**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436486502935)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436486505111)

**Id\_calculo 0009**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436486506263)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440159255)

**Id\_calculo 0010**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436486510999)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440162711)

**Id\_calculo 0011**

**![](https://i.imgur.com/7N6eQuw.png)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440163735)

**Id\_calculo 0012**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440166551)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440167959)

**Id\_calculo 0106**

**![](https://i.imgur.com/ceIIXah.png)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440170263)

Os**id's cálculo 0007/ 0012** são gravadas no **SRC (Consultas> Cálculo por Funcionário)** pela rotina de cálculo do adiantamento. Porém, somente são listadas em relatório de folha, ao solicitar relatório de adiantamento tais verbas não aparecem. Por esta razão definimos como verbas da folha e não do adiantamento.  
  
**OBS.:** As verbas de identificador **0015 e 0066** **não devem** **ter o campo RV\_CODMSEG - V. Mês Segui**preenchido, pois essa configuração deve ser realizada apenas em **REGIME CAIXA.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440172695)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34436440173975)****Saiba mais**  
[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)

[RH - Linha Protheus - GPE - Configuração de verbas para Adiantamento (regime caixa)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006990952-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-de-verbas-para-Adiantamento-regime-caixa)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
