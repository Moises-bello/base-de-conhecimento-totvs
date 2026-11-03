---
article_id: 26787717723543
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 634a2a8d836cc4ea806a0f8e6decf9037f222bfd279d3b3e345e081f3213c0f0
fetched_at: '2026-06-28T22:37:49.308583+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Retorno com erro Data
  do pagamento deve ser maior ou igual ao dia atual
type: support-article
updated_at: '2024-10-03T17:59:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26787717723543-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Retorno-com-erro-Data-do-pagamento-deve-ser-maior-ou-igual-ao-dia-atual
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26815420340375) Tempo aproximado para leitura: 00:05:00 min**

**Ocorrência**

O pagamento do boleto foi realizado por meio da API do Banco do Brasil; no entanto, retorna no monitor de pendências a seguinte mensagem: **"Data do pagamento deve ser maior ou igual ao dia atual"**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**  
A data de vencimento do título não pode ser inferior a data do dia, caso contrário, será rejeitada pelo banco.

**Solução**

Ajustar a data de vencimento do título para a data atual ou uma data posterior.

**Saiba mais**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Configuração e Funcionalidade da transmissão de boletos API](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16665077816471-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Configura%C3%A7%C3%A3o-e-Funcionalidade-da-transmiss%C3%A3o-de-boletos-API)
