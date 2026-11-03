---
article_id: 31438209181719
category: Financeiro - Contas a Pagar
content_hash: 9bfbe635f94967e4b30967dfa6acb34f72cd7c04b867a5bd386d7af12fb9ed40
fetched_at: '2026-06-28T22:38:09.812320+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Utilização de ExecAuto
  para preenchimento de rateio SEV e SEZ em rotinas de baixa
type: support-article
updated_at: '2026-02-13T11:31:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31438209181719-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Utiliza%C3%A7%C3%A3o-de-ExecAuto-para-preenchimento-de-rateio-SEV-e-SEZ-em-rotinas-de-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31438256867991) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Atualmente, no módulo Financeiro, é possível utilizar a **execução automática (ExecAuto)** das rotinas de **Baixas Manuais (FINA080) e Baixas Automáticas (FINA090)** para o preenchimento dos campos de rateio nas tabelas SEV e SEZ?

**Ambiente**  
Cross Segmento – TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as releases

**Solução**  
Não é possível realizar o preenchimento ou a gravação de rateios nas tabelas **SEV** e **SEZ** através das rotinas automáticas de baixa (**FINA080** e **FINA090**).

O rateio via **ExecAuto** está disponível exclusivamente no momento da **inclusão do título** (contas a pagar ou a receber), onde a estrutura do array de dados permite o envio das informações de multi natureza.

Para realizar o processo de baixas, você pode fazer isso diretamente pelo sistema, como mostrado a seguir:

![rateio multi.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/38378158491415)

**Saiba mais**  
[**Baixas Pagar Manual - FINA080 - Financeiro - P12**](https://tdn.totvs.com/display/public/PROT/Baixas+Pagar+Manual+-+FINA080+-+Financeiro+-+P12)
