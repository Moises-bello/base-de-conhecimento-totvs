---
article_id: 360020579772
category: NFe - Nota Fiscal Eletrônica
content_hash: f3e81cf4a35885f57e19eac1ed28e993f6d4b3c74f915bcaae96929814ea7389
fetched_at: '2026-06-28T22:40:00.254766+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  770 Rejeição
  : CFOP inexistente'
type: support-article
updated_at: '2021-08-23T20:13:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020579772--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-770-Rejei%C3%A7%C3%A3o-CFOP-inexistente
---

**Dúvida**Como Corrigir rejeição 770 : CFOP inexistente

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Neste caso a Sefaz está rejeitando porque o CFOP é inexistente. Verificar junto com o seu fiscal qual CFOP utilizar nesta operação.

**Importante:**

 No site da Sefaz foi disponibilizada a lista abaixo**com os novos CFOPS e com os CFOPS alterados:**

15/01/2020 - Publicada versão atualizada da Nota Técnica **2017.002 v.1.40**

Publicada versão atualizada da [Tabela de CFOP - Vigência 01-02-2020 (Publicada em 15/01/2020)](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=C0HaR0Mo8Lw=)

**(Ao clicar nesse link será baixado um arquivo excel)**

1 - Inclua esses CFOPS novos devem ser incluídos manualmente no Protheus:

* **Para incluir manualmente os novos CFOPS realizar o procedimento do link abaixo:**

[MP - FIS - Como criar novos CFOP´s?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026739072)

2 - Após incluir ou se apenas irá alterar para um que já exista no Protheuspreenchao campo no TES F4\_CF  **Cod. Fiscal**com um dos CFOP

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052264173/mceclip1.png)

 3- Após isso, **exclua a nota e gere novamente**

**Saiba Mais:**

*Caso seja um **CFOP válido**, será necessário **entrar em contato com a SEFAZ** para saber o motivo da rejeição.*

***Fiscalmente qual CFOP**utilizar a TOTVS**não orienta.** Caso haja dúvidas fiscais, **será necessário a empresa**como contribuinte**consultar a Sefaz.** Lembrando que essas consultas **só são feitas pelo contribuinte ou seja pela empresa.***

*Se em alguma **operação interna o CFOP é aceito iniciado por 5** e ao **fazer operação interestadual **iniciado por**  6 ou vice-versa não exista o CFOP** devem ser criados TES diferentes com CFOPs válidos para cada operação.*
