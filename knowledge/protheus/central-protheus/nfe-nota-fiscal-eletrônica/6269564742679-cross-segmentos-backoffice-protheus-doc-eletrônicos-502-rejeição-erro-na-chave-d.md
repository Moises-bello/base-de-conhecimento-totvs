---
article_id: 6269564742679
category: NFe - Nota Fiscal Eletrônica
content_hash: 1c513ea4f146d1daeb3a63af6ac5cc241d3e1349cbe837cb51c519a8c64e9b76
fetched_at: '2026-06-28T22:40:05.064278+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 502 Rejeição: Erro
  na Chave de Acesso - Campo Id não corresponde à concatenação dos campos correspondentes'
type: support-article
updated_at: '2025-06-18T14:36:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6269564742679-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-502-Rejei%C3%A7%C3%A3o-Erro-na-Chave-de-Acesso-Campo-Id-n%C3%A3o-corresponde-%C3%A0-concatena%C3%A7%C3%A3o-dos-campos-correspondentes
---

**Dúvida**Como solucionar a 502 Rejeição: Erro na Chave de Acesso - Campo Id não corresponde à concatenação dos campos correspondentes

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Acesse na rotina de transmissão ***monitor -> faixa -> schema*** copie o conteúdo completo e verifique  a chave gerada na TAG do XML  ***infNFe versao="4.00" Id***a chave gerada.

![4.0.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10949648869143)

2. O número da Chave da NF-e é composta pelos dados abaixo, conforme ***Manual de Integração do Contribuinte:***

***![dados_da_chave_da_nota.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6269422818455)***

3. Verifique se ***os dados na chave estão corretos***.

![chave.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10949727438615)

* **Saiba mais:**

Se a nota estiver sendo transmitida em modalidade Normal, verifique se a serie da nota está 0-889, para alterar caso não esteja, neste intervalo:

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em editar  **MV\_ESPECIE Ex: 889=SPED**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13101751102103)

2. Após isso, exclua a nota e gere novamente.

 

* ***Validação da Sefaz:***

***![502_rejei__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/6269294184727)***
