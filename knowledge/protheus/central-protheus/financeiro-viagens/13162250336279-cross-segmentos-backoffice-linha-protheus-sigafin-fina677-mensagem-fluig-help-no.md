---
article_id: 13162250336279
category: Financeiro - Viagens
content_hash: 8d3b747dc7a4b8cee6abd986f7f4473d64b8b45546087e9c2fe5df8d336aacc4
fetched_at: '2026-06-28T22:38:21.278345+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - Mensagem
  Fluig HELP NOFLUIG ao realizar procedimento de aprovação na prestação de contas
type: support-article
updated_at: '2025-02-06T20:11:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13162250336279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Mensagem-Fluig-HELP-NOFLUIG-ao-realizar-procedimento-de-aprova%C3%A7%C3%A3o-na-presta%C3%A7%C3%A3o-de-contas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**  
Ao realizar aprovação na FINA677 ocorre a Mensagem Fluig HELP NOFLUIG como desabilitar o HELP?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Existe uma chamada no fonte em relação a ativação do controle de Workflow integrado com o Fluig

No cadastro existe a opção tabela **CPF CPF\_STATUS =2** ajustar para 1
