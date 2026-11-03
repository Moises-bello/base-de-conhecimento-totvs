---
article_id: 7450504719383
category: Materiais - Compras (SIGACOM)
content_hash: 173897498d11880176503f7a2d3eaee4e10e103a06941a3d7a220e8e1c0d5e5f
fetched_at: '2026-06-28T22:41:15.799766+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é gravado o campo
  E1_EMISSAO da  NCC gerado pelo documento de entrada?
type: support-article
updated_at: '2022-07-14T11:04:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7450504719383-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-gravado-o-campo-E1-EMISSAO-da-NCC-gerado-pelo-documento-de-entrada
---

**Dúvida**Qual a data o sistema considera para gravar o campo E1\_EMISSAO no título NCC gerado pela nota de entrada de devolução ?

**Ambiente**Protheus – Compras – Todas as versões

**Solução**Por padrão o sistema considera a **data de emissão da nota de entrada de devolução** para gravar o campo **E1\_EMISSAO no título tipo NCC**. Porém foi liberada uma implementação através da ISSUE :  DMANMAT02-38736 com a criação do parâmetro **MV\_DTEMIBS** para tratar este cenário, onde será possível a escolha entre a *data de emissão da nota* e a *data de digitação da nota*.

O parâmetro só será incorporado no dicionário padrão a partir do release **12.2210.** *Para releases anteriores será necessário criá-lo manualmente conforme documento abaixo :*

[**Data de emissão da NCC quando gerada pelo documento de entrada**](https://tdn.totvs.com/pages/releaseview.action?pageId=698303156)

E efetuar a atualização do sistema mediante a aplicação do pacote :

**12.1.2210: <https://suporte.totvs.com/portal/p/10098/download?e=1073842>**

**12.1.33: <https://suporte.totvs.com/portal/p/10098/download?e=1073841>**

***Para clientes que possuem garantia estendida para o release 27, temos o pacote abaixo também :***

***12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1073840>***

***Saiba Mais :***

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747-MP-SIGACOM-Pontos-de-Entrada-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
