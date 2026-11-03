---
article_id: 360057245754
category: NFe - Nota Fiscal Eletrônica
content_hash: 511a3b74c7e96061258b3d1b4487d51aa599aa6dfc6b4c930b93795558ceb17b
fetched_at: '2026-06-28T22:40:03.483025+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como corrigir a
  mensagem  999 - Erro na SEFAZ ou Autorizada a operação em contingência
type: support-article
updated_at: '2025-06-17T12:05:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057245754-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-corrigir-a-mensagem-999-Erro-na-SEFAZ-ou-Autorizada-a-opera%C3%A7%C3%A3o-em-conting%C3%AAncia
---

**Dúvida**Como corrigir a mensagem 999 - Erro na SEFAZ ou Autorizada a operação em contingência ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

***Importante:***

Caso a Sefaz não esteja em contingência, atualizar ***as URLs do TSS.*** O pacote pode ser ***acessado no endereço:***

*****1. Atualização do ambiente TSS (repositório e URls)*****

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

[TSS - Atualização das URLs do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS?source=search)

1- Ao apresentar a mensagem **999-Erro na SEFAZ consulte o link abaixo:**

***<https://www.nfe.fazenda.gov.br/portal/principal.aspx>***

2- Neste link, **Clique em Serviços -> Consultar Disponibilidade:**

![20201117_204927.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099786253)

* **Importante:** É possível verificar as ***modalidades de cada UF no final da página acima.***

3- Verifique a cor da legenda, **para UF (estado)** de emissão da sua nota:

**![disponibilidade_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099402473)**

4- Caso a legenda esteja **amarela ou vermelha,** será necessário verificar com a Sefaz se é uma instabilidade momentânea, ou  se está operando em contingência e qual:

**![disponibilidade_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099402533)**

5- Caso esteja operando em **contingência, ir na rotina NFESEFAZ e configurar conforme abaixo:**

**1-** Normal

A modalidade **Normal** é utilizado quando a Sefaz está operando em seu modalidade **normal** e a empresa está com sua rede funcionando.

![modalida_normal.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450876791063)

**2-** Contingência off-line

A **contingência off-line** poderá utilizar quando a empresa estiver sem internet ou quando a Sefaz estiver em contingência, porém será necessário **imprimir o Danfe em papel moeda**.

![modalida_offline.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450876795927)

**3-** Contingência Scan

Para a **SCAN** a série da nota deverá ser de 900 a 999. A modalidade foi **descontinuada** pela Sefaz.

![modalida_scan.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450876801047)

**4-** Ambiente Nacional

![ambiente_nacional.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450840982423)

**5-** Contingência DPEC/ EPEC

A **DPEC** tem a particularidade é necessário alterar o parâmetro de transmissão além da modalidade para DPEC alterar a versão DPEC para 1.01

**Lembrete a modalidade de contingência** ***5-******Contingência DPEC/ EPEC*,** deve ser utilizada apenas caso seja orientado pela Sefaz, pois ao utilizar está opção indevidamente o **Evento fica registrado, mas não Vinculado, ou seja a nota não é autorizada.**

![epec.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450840995735)

**6-** Sefaz virtual

![6_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450841000087)

**7-** Contingência FS-DA

![7_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450876822807)

**8-** Contingência SVC-AN

![8_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450841012503)

**9-** Contingência SVC-RS

![9_modalidade.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15450876835095)

* ***Importante:***

**Lembrando que a modalidade de contingência** ***5-******Contingência DPEC/ EPEC*,** deve ser utilizada apenas caso seja orientado pela Sefaz, pois ao utilizar está opção indevidamente o **Evento fica registrado, mas não Vinculado, ou seja a nota não é autorizada.**

6- Caso esteja com legenda verde operando normal, **verificar se o TSS está atualizado.**

**![disponibilidade_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097094994)**

* **Importante:**

Caso apresente a mensagem WSCERR048 / SOAP FAULT verificar também se a Sefaz está operando em contingência e realizar o mesmo procedimento acima.
