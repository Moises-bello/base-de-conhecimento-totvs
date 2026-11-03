---
article_id: 23340069641623
category: NFe - Nota Fiscal Eletrônica
content_hash: d7debc255782d90405daa65781c0ef104ded9a0045070eb389cb0970d7827bed
fetched_at: '2026-06-28T22:40:03.707358+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Rejeição 713 -
  Tipo de Emissão diferente de 6 ou 7 para contingência da SVC acessada
type: support-article
updated_at: '2025-06-11T11:52:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23340069641623-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-713-Tipo-de-Emiss%C3%A3o-diferente-de-6-ou-7-para-conting%C3%AAncia-da-SVC-acessada
---

**Dúvida**  
Rejeição 713 - Tipo de Emissão diferente de 6 ou 7 para contingência da SVC acessada?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Causa**

Quando uma NF-e for encaminhada para os Servidores Virtuais de Contingência, disponibilizados pela Sefaz AN e Sefaz RS, com Tipo de Emissão diferente de **"6 - Contingência SVC-AN" ou "7 - Contingência SVC-RS"**, respectivamente, será retornada a **rejeição "713 - Tipo de Emissão diferente de 6 ou 7 para contingência da SVC acessada".**

Exemplo hipotético:

Foi emitida uma NF-e com Tipo de Emissão "1 - Normal" e a mensagem do lote da NF-e, foi encaminhado para o Servidor Virtual de Contingência da Sefaz RS. Como o SVC-RS apenas aceita o Tipo de emissão como 7, a NF-e será rejeitada pelo motivo 713.

Veja regra de validação da Sefaz:

![](http://www.oobj.com.br/bc/assets/Articles/133/Rej713.PNG)

**Solução**

Deve-se verificar duas coisas, o Tipo de Emissão (**tpEmis**) informado na NF-e e para qual Ambiente da Sefaz está sendo encaminhado o Documento Fiscal. Se realmente está emitindo em uma das contingências SVC e está sendo retornado rejeição, o Tipo de Emissão informado está errado, mas se o Tipo de Emissão está correto, então sua NF-e está sendo enviada para o Ambiente errado.

Caso a Sefaz tenha habilitado o ambiente de contingencia **SVC AN** ou **SVC RS**, devera excluir a nota que esta com a rejeição 713 e após isso preparar o documento novamente e antes de transmitir a nota devera alterar a modalidade de de acordo com que a Sefaz da sua UF determinou, para trocar a modalidade de transmissão basta entrar na rotina **Nfe Sefaz - Outras Ações - Parâmetros - NFe** e alterar a modalidade para opção **8-Contingencia SVC-AN ou opção 9-Contingencia SVC-RS**, salvar com grupo administrador Salvar e depois OK. Após isso transmita a nota e monitore.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23340069637399)
