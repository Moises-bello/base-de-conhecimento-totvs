---
article_id: 360024950773
category: NFe - Nota Fiscal Eletrônica
content_hash: 0991f6a84da0087d837f52325a774a418367defddaf9b3cd778370c8017b215a
fetched_at: '2026-06-28T22:40:06.744510+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações
  na TAG infCpl ou infAdFisco no XML e no DANFE
type: support-article
updated_at: '2025-06-30T19:13:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-informa%C3%A7%C3%B5es-na-TAG-infCpl-ou-infAdFisco-no-XML-e-no-DANFE
---

**Dúvida**

Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as verões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

***Informações complementares do Danfe:***

1. Preencher o campo ***Mens. p/ Nota***  ***F1\_MENNOTA*** no complemento do Danfe em  ***Informações complementares*** no documento de entrada na aba Nota Fiscal eletrônica.

![F1_MENNOTA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413408851095)

ou

2. Preencher o campo ***Mens. p/ Nota** **C5\_MENNOTA*** Campo de complemento do Danfe do campo **Informações complementares** é preenchido no Pedido de Venda. Observação : Os campos ***F2\_MENNOTA e C5\_MENNOTA*** devem conter o mesmo tamanho no configurador.

![C5_MENNOTA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413415357463)

ou

3. Preencher o campo ***Mens. Padrão C5\_MENPAD*** no pedido de venda com a fórmula. Colocar neste campo a numeração da fórmula criada. **Observação:** O conteúdo preenchido é levado apenas a mensagem para TAG ***dados adicionais do fisco.***

![C5_MENPAD.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413408894743)

ou

4. Preencher o campo ***Formula F4\_FORMULA*** no TES na aba impostos. Colocar neste campo a numeração da fórmula criada.

![F4_FORMULA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413423260311)

ou

5. Preencher o campo ***Formula NFe F4\_******FORINFC*** no TES na aba impostos. Colocar neste campo a numeração da fórmula criada. Colocar neste campo a numeração da fórmula criada. Observação: O campo foi criado para atender o **EFD ICMS/IPI:** [MP - FIS - SPED FISCAL - Como gerar o registro C110](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019777532)

![F4_FORINFC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413423935895)

6. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar** :

**Nome : MV\_NFEMSF4**   
**Tipo :****Caractere**  
**Descrição:** **Parâmetro que determina o tratamento do campo F4\_FORMULA e F4\_FORINFC  para NF-e.**  
**C =Inf. Adicionais cliente;**  
**F =Inf. Adicionais Fisco;**  
**BRANCO=não considera.**

ou

7. Preencher o campo ***A1\_MENSAGE*** no cadastro de cliente.  Colocar neste campo a numeração da fórmula criada.

![A1_MENSAGEM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/10726921271959)

8. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar** :

**Nome : MV\_NFEMSA1**   
**Tipo : Caractere**  
**Descrição :**  
**Parâmetro que determina o tratamento do campo A1\_MENSAGE para NF-e.**   
**C=Inf. Adicionais Cliente;**   
**F=Inf. Adicionais Fisco; BRANCO=não considera.**

* **Saiba mais:**

Existe um parecer da consultoria da TOTVS referente as informações geradas na***TAG infcpl e infadfisco:***

[Parecer da consultoria](https://tdn.totvs.com/pages/releaseview.action?pageId=361433612)

* Para gerar com mais de ***250 caracteres há documentação do link abaixo:***

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares do Danfe com mais de 250 caracteres ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025310894)

* Para verificar todos os ***artigos de NFe, há o link abaixo:***

[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/sections/207068528-NFe-Nota-Fiscal-Eletr%C3%B4nica)
