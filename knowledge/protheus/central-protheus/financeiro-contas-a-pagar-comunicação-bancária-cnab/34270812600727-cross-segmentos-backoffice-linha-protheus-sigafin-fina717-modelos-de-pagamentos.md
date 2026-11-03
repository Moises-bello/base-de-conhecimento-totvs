---
article_id: 34270812600727
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 27ae4971fab65e190a698ce0afa631f4b414c906a837e4b6646d27913f361ae9
fetched_at: '2026-06-28T22:37:56.366529+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA717 - Modelos de
  pagamentos homologados para o banco do Brasil
type: support-article
updated_at: '2025-08-18T18:59:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34270812600727-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA717-Modelos-de-pagamentos-homologados-para-o-banco-do-Brasil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34270777095703) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais os modelos de pagamentos homologados para o banco do Brasil?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**  
É possível gerar um borderô de pagamentos com registro online, para isso bastar acessar as rotina Borderô de pagamentos (**FINA240**) ou Borderô de pagamento com impostos (**FINA241**), ao preencher as informação do banco e subconta previamente cadastrados, será habilitado a opção **Registro Online**, ao marcar essa opção o borderô será marcado para registro online (**EA\_BORAPI**= S).

Modelos de pagamentos (**Tabela genérica 58 do SX5**) homologados para transmissão:

Modelos de pagamentos (Tabela genérica 58 do SX5) homologados para transmissão:  
➔ 30 - Transmissão de liquidação de títulos em cobrança no Itaú  
➔ 31 - Transmissão de pagamento de títulos em outro banco  
➔ 01 - Transmissão de transferência entre contas - Crédito em conta corrente  
➔ 03 - Transmissão de transferência entre contas - DOC  
➔ 41 - Transmissão de transferência entre contas - TED - Outro titular  
➔ 43 - Transmissão de transferência entre contas - TED - Mesmo titular  
➔ 13 - Transmissão de pagamentos de GUIA com código de barras  
➔ 16 - Transmissão de pagamentos da DARF NORMAL  
➔ 18 - Transmissão de pagamentos da DARF SIMPLES  
➔ 17 - Transmissão de pagamentos da GPS  
➔ 45 - Transmissão de transferência PIX
