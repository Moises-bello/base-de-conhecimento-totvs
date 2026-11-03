---
article_id: 37641367532567
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a626f7f60a064ac836d56101c353349731a9759186477f9d2b3227292b901c04
fetched_at: '2026-06-28T22:37:22.936176+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNTA300TFS ao
  tentar incluir Cronograma Financeiro/Físico no Cadastro do Contrato
type: support-article
updated_at: '2026-01-13T16:01:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37641367532567-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNTA300TFS-ao-tentar-incluir-Cronograma-Financeiro-F%C3%ADsico-no-Cadastro-do-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37641367499159) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao realizar a inclusão do Cronograma Financeiro no cadastro de um contrato no Gestão de Contrato, ao informar o parâmetro de Periodicidade como "Cond Pagto" ocorre o Help CNTA300TFS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37641683175447)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

No cadasto do contrato, por onceito do sistema quando se utiliza um Tipo de Contrato ou Tipo de Planilha que possui a configuração de "Cron. Fisico = Sim" o sistema não permite a utilização da Periodicidade "Cond Pagto" nos parâmetros para geração de Cronograma Financeiro/Fisico do Contrato.

Assim, nessa situação, para que não ocorra a mensagem de Help CNTA300TFS, deve-se utilizar o parâmetro de Periodicidade diferente de "Cond Pagto":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37641992695959)

Ou caso se deseje utilizar o parâmetro "Periodicidade = Cond Pagto" deve-se utilizar um Tipo de PLanilha / Tipo de Contrato sem Cronograma Fisico, ou seja, com o campo "Cron Fisico = Não":

Exemplo Tipo de Contrato:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37641984078871)

Exemplo Tipo de Planilha:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37641992698391)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
