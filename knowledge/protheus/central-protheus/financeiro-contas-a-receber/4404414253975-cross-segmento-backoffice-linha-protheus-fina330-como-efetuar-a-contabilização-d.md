---
article_id: 4404414253975
category: Financeiro - Contas a Receber
content_hash: fc45dc1413a94dcbc8e82727d2e88b14f6fc2d191ae65f05ffabd755399dd54c
fetched_at: '2026-06-28T22:38:12.680261+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento -  Backoffice Linha Protheus -FINA330- Como efetuar a  contabilização
  dos valores acessórios pela baixa por compensação
type: support-article
updated_at: '2021-09-03T18:07:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404414253975-Cross-Segmento-Backoffice-Linha-Protheus-FINA330-Como-efetuar-a-contabiliza%C3%A7%C3%A3o-dos-valores-acess%C3%B3rios-pela-baixa-por-compensa%C3%A7%C3%A3o
---

**Dúvida**Como efetuar a contabilização dos valores acessórios pela baixa por compensação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro- A Partir Versão 12  
  
**Solução**Não temos valores acessório para rotina de compensação FINA330 apenas para baixa FINA070, veja a documentação abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=311631483>  
  
Porém, se for em relação a baixa, a rotina FINA070, para a contabilização de valores acessórios o mesmo deve configurar o Lp 520 com a configuração da contabilização, o campo (“Variável CTB”, ABS(TXDVALOR)), qualquer que seja, utilizado no cadastro de tipos de valores acessórios, deverá ser preenchido com um nome para a variável daquele Valor Acessório em questão. Essa variável deverá ser preenchida nos Lançamentos Padronizados, conforme critério de contabilização utilizado.
