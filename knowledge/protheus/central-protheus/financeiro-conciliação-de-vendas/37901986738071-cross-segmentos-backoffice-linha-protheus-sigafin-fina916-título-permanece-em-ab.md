---
article_id: 37901986738071
category: Financeiro - Conciliação de Vendas
content_hash: fe31b681a55ecf277ba1db37a1f973da5c96feaaed7520beb54aecafff264ff6
fetched_at: '2026-06-28T22:37:26.268981+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA916 - Título permanece
  em aberto após conciliação de vendas
type: support-article
updated_at: '2026-01-26T18:39:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37901986738071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA916-T%C3%ADtulo-permanece-em-aberto-ap%C3%B3s-concilia%C3%A7%C3%A3o-de-vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37901986732951) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Por que, após realizar a conciliação e efetivação de um título na rotina FINA916, o registro permanece com o status "não baixado" no Contas a Receber?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução:**

Esse comportamento ocorre porque a rotina **FINA916 (Conciliação de Vendas)** tem como objetivo **exclusivo** a conferência e a checagem dos registros de vendas entre o sistema Protheus e o arquivo importado da operadora.

A **FINA916** atua apenas como uma **camada de validação**, verificando se a venda informada pela operadora está de acordo com o registro existente no ERP. Essa rotina **não executa a baixa financeira (liquidação)** do título.

Para que o título seja efetivamente baixado no **Contas a Receber** após o processo de conciliação, é necessário utilizar a rotina **FINA918 (Liquidação de Vendas)**. É nessa etapa que o sistema processa o **recebimento financeiro**, realizando a liquidação e alterando o status do título para **baixado**.
