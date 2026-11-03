---
article_id: 360034127833
category: RH - Contabilização
content_hash: 726d228feef06537d9fba4c9db0dde75828966bdd75ebadfb780aa3677059476
fetched_at: '2026-06-28T22:43:45.952521+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização não gera as verbas de baixa por
  transferência/Não gera lançamentos na tabela SRZ.
type: support-article
updated_at: '2025-07-29T13:55:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034127833-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-n%C3%A3o-gera-as-verbas-de-baixa-por-transfer%C3%AAncia-N%C3%A3o-gera-lan%C3%A7amentos-na-tabela-SRZ
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33791306532375)**Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**

Não contabiliza as baixas de provisão por transferência/ Não gera SRZ.

**Ambiente:**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa:**Parâmetro **MV\_TRFAMES** preenchido.  
  
**Solução:**

Para que seja contabilizada, o parâmetro **MV\_TRFAMES** deve estar vazio.

Verificar o parâmetro através do configurador, SIGACFG > Ambiente > Cadastro > Parâmetros

**Conceito do parâmetro:**

**Situação 1 = Parâmetro vazio, disponibiliza os valores para a contabilização.**  
**Situação 2 = Parâmetro preenchido, não será contabilizado. Serve apenas pra demonstrar as linhas de baixa de transferência no relatório.** **![](http://tdn.totvs.com/download/attachments/364914692/image2018-5-25_16-19-28.png?version=1&modificationDate=1527276934000&api=v2)**

Para mais detalhes, acesse os links abaixo:

Não gera SRZ - Como conferir? <http://tdn.totvs.com/pages/releaseview.action?pageId=364914692>

Como é utilizado o parâmetro **MV\_TRFAMES?****[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025027553-MP-GPE-Transferência-na-Provisão-Parâmetro-MV-TRFAMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025027553-MP-GPE-Transfer%C3%AAncia-na-Provis%C3%A3o-Par%C3%A2metro-MV-TRFAMES)**

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
