---
article_id: 360019533092
category: NFe - Nota Fiscal Eletrônica
content_hash: e1d4db4f92b0ef8b353961073223a80c476cf6f9adffb302a48c419a7251ccf3
fetched_at: '2026-06-28T22:40:03.110974+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos  - 109 Rejeição Serviço
  paralisado sem previsão
type: support-article
updated_at: '2025-06-26T14:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019533092-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-109-Rejei%C3%A7%C3%A3o-Servi%C3%A7o-paralisado-sem-previs%C3%A3o
---

**Dúvida**Como corrigir a 109 Rejeição Serviço paralisado sem previsão ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Esta rejeição ocorre porque **a SEFAZ está instável ou indisponível** e **não** consegue processar a solicitação.  
  
É necessário **entrar em contato com a SEFAZ** para verificar o **motivo da instabilidade** e se será **necessário entrar em contingência.**

1- Ao apresentar a mensagem **consulte o link abaixo:**

***<https://www.nfe.fazenda.gov.br/portal/principal.aspx>***

2- Neste link, **Clique em Serviços -> Consultar Disponibilidade:**

![20201117_204927.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408199703)

* **Importante:** É possível verificar as ***modalidades de cada UF no final da página acima.***

3- Verifique a cor da legenda, **para UF (estado)** de emissão da sua nota:

**![disponibilidade_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408202391)**

4- Caso a legenda esteja **amarela ou vermelha,** será necessário verificar com a Sefaz se é uma instabilidade momentânea, ou  se está operando em contingência e qual:

**![disponibilidade_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408204183)**

5- Caso esteja operando em **contingência, ir na rotina NFESEFAZ e configurar conforme abaixo:**

**1-** Normal

A modalidade **Normal** é utilizado quando a Sefaz está operando em seu modalidade **normal** e a empresa está com sua rede funcionando.

![modalida_normal.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071393955351)

**2-** Contingência off-line

A **contingência off-line** poderá utilizar quando a empresa estiver sem internet ou quando a Sefaz estiver em contingência, porém será necessário **imprimir o Danfe em papel moeda**.

![modalida_offline.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071393958423)

**3-** Contingência Scan

Para a **SCAN** a série da nota deverá ser de 900 a 999. A modalidade foi **descontinuada** pela Sefaz.

![modalida_scan.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408211479)

**4-** Ambiente Nacional

![ambiente_nacional.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408213015)

**5-** Contingência DPEC/ EPEC

A **DPEC** tem a particularidade é necessário alterar o parâmetro de transmissão além da modalidade para DPEC alterar a versão DPEC para 1.01

**Lembrete a modalidade de contingência** ***5-******Contingência DPEC/ EPEC*,** deve ser utilizada apenas caso seja orientado pela Sefaz, pois ao utilizar está opção indevidamente o **Evento fica registrado, mas não Vinculado, ou seja a nota não é autorizada.**

![epec.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408214295)

**6-** Sefaz virtual

![6_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408218647)

**7-** Contingência FS-DA

![7_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408223511)

**8-** Contingência SVC-AN

![8_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071393970711)

**9-** Contingência SVC-RS

![9_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071408228759)

* ***Importante:***

**Lembrando que a modalidade de contingência** ***5-******Contingência DPEC/ EPEC*,** deve ser utilizada apenas caso seja orientado pela Sefaz, pois ao utilizar está opção indevidamente o **Evento fica registrado, mas não Vinculado, ou seja a nota não é autorizada.**

6- Caso esteja com legenda verde operando normal, **verificar se o TSS está atualizado e configurado conforme o link abaixo:**

**![disponibilidade_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33071393975319)**

[Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

* **Importante:**

Caso apresente a mensagem WSCERR048 / SOAP FAULT verificar também se a Sefaz está operando em contingência e realizar o mesmo procedimento acima.
