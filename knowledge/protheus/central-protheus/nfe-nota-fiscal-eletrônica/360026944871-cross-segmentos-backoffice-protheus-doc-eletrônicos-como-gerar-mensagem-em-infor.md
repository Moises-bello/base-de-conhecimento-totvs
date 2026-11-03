---
article_id: 360026944871
category: NFe - Nota Fiscal Eletrônica
content_hash: 2c648448693c653eae7914ba9e92779f5f29d56d3435ec1e2ffa596cd61847c6
fetched_at: '2026-06-28T22:40:00.322568+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar mensagem
  em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula '
type: support-article
updated_at: '2024-04-30T03:00:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-mensagem-em-informa%C3%A7%C3%B5es-complementares-TAG-infcpl-e-infadfisco-do-Danfe-utilizando-f%C3%B3rmula
---

**Dúvida**Como gerar mensagem em informações complementares (TAG infcpl e infadfisco)  do Danfe utilizando fórmula ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos  a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para **determina o tratamento do campo F4\_FORMULA e A1\_MENSAGE para NF-e.**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar:**

**Nome : MV\_NFEMSF4**  
**Tipo :****Caractere**  
**Descrição:****Parâmetro que determina o tratamento do campo F4\_FORMULA e F4\_FORINFC  para NF-e.**  
**C =Inf. Adicionais cliente;**  
**F =Inf. Adicionais Fisco;**  
**BRANCO=não considera.**

**Nome : MV\_NFEMSA1  
Tipo : Caractere  
Descrição :  
Parâmetro que determina o tratamento do campo A1\_MENSAGE para NF-e.  
C=Inf. Adicionais Cliente;  
F=Inf. Adicionais Fisco; BRANCO=não considera.**

* Cadastre uma Fórmula:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026275971)

* No Pedido de Venda a fórmula 001 está vinculada no campo C5\_MENPAD.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026275931)

* A fórmula 002 está vinculada na TES utilizada no pedido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026276011)

* DANFE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026275811)

* **Saiba mais:**

Existe um parecer da consultoria da TOTVS referente as informações geradas na **TAG infcpl e infadfisco:**

[Parecer da consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=361433612)

* Para gerar com mais de **250 caracteres há documentação do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares do Danfe com mais de 250 caracteres ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025310894)

* Para verificar todos os **artigos de NFe, há o link abaixo:**

**[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/sections/207068528-NFe-Nota-Fiscal-Eletr%C3%B4nica)**
