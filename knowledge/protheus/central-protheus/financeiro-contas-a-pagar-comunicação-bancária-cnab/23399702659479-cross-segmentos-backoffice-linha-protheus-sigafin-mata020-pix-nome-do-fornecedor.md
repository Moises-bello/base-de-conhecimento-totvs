---
article_id: 23399702659479
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: c6dc3af5b144779cf9100e354e42c3d1515ab7e6a12108cd637b75e7ba375eb9
fetched_at: '2026-06-28T22:37:56.405024+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA020 -  PIX - Nome
  do Fornecedor com asterisco após salvar chave PIX
type: support-article
updated_at: '2024-05-10T19:30:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23399702659479-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA020-PIX-Nome-do-Fornecedor-com-asterisco-ap%C3%B3s-salvar-chave-PIX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23399739327383) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar o cadastro da chave PIX do Fornecedor, a razão social do fornecedor está sendo gravado com um asterisco  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23399739331863)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o tamanho dos campos A2\_NOME e F72\_NOME estão diferentes

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

Acesse o **Modulo Configurador > Bases de dados** e altere o tamanho do campo **F72\_NOME** para ficar igual ao **A2\_NOME**, posteriormente realizar um novo **cadastro de chave PIX.**

**Saiba mais**  
[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
