---
article_id: 17696157592343
category: SIGAACD - Automação e Coleta de Dados
content_hash: fa6fd43bf8e2c5246a9555af0a599d768ea04c26a30d93d32fd998d4749b7c84
fetched_at: '2026-06-28T22:39:11.347297+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV166 HELP LOTE
  INVALIDO mesmo informando um Lote que tem saldo
type: support-article
updated_at: '2024-12-16T11:43:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17696157592343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV166-HELP-LOTE-INVALIDO-mesmo-informando-um-Lote-que-tem-saldo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17696137069207) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**

Apresenta o ***HELP LOTE INVALIDO*** ao tentar separar um Lote que temos saldo para movimentação. Não permite continuar a Separação. Como devemos proceder?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17696761512343)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Para a rotina "Ordem de Separação" por "Ordem de Produção", é necessário que no momento de inclusão da Ordem de Produção o **parâmetro F12** da rotina **"SUGERE LOTE/ENDEREÇO A EMPENHAR"** esteja igual a **"Sim"**, para que gere os empenhos dos Lotes a serem separados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17696530403735)

Caso, o **parâmetro F12** da rotina Ordem de Produção (MATA650) **esteja igual a "Não",** é necessário ***estornar a Ordem de Separação***, em seguida,  deverá ser feita manualmente no empenho da OP diretamente na rotina Ajuste de Empenhos (MATA381) definindo os Lotes e Sub-lotes , em seguida refaça o processo.

Veja um exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697215840791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697241554071)

Após o estorno da Ordem de Separação acessar a rotina AJUSTES DE EMEPNHOS (MATA381) e ajustar o empenho informando o Lote.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697284899735)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697356020631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697375631895)

Após efetuado o processo acima, é **necessário estornar a Ordem de Separação e incluir novamente**.

Em seguida refaça todos os passos da rotina sem que apresente o HELP LOTE INVALIDO.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697428324631)

Nesse cenário é egrado uma nova Ordem de Separação, que permite efetuar o processo sem impedimento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697505785751)

**Observe abaixo que agora é apresentado o Lote corrretamente para ser separado.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17697543708823)

***Dica:*** É recomendável quando trabalhar com Lote, ***antes de incluir*** a Ordem de Separação (ACDA100) por Ordem de produção, avaliar se os empenhos foram gerados corretamente.

[**Clique aqui**](https://tdn.totvs.com/pages/releaseview.action?pageId=347470277) **e veja o boletim com mais detalhes sobre esse comportamento.**

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*

*[Ordens de Separação (ACDA100 - SIGAACD)](https://tdn.totvs.com/pages/releaseview.action?pageId=347470277)*
