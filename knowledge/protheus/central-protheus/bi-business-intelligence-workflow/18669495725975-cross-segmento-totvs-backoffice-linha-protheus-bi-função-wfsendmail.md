---
article_id: 18669495725975
category: BI - Business- Intelligence - Workflow
content_hash: 15066d4a4f736d3ee302f2e22a18d4ca38e9eef7ddc399dd2aa68a5973755376
fetched_at: '2026-06-28T22:37:03.122048+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Função WFSENDMAIL.
type: support-article
updated_at: '2023-10-30T17:56:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18669495725975-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Fun%C3%A7%C3%A3o-WFSENDMAIL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18669457124759) Tempo aproximado para leitura: **03:00 min** **Dúvida**Como utilizar a Função *WFSENDMAIL*?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *BI* – *Workflow* - Todas as releases.  
  
**Solução**Apesar de ter a opção “Enviar Automaticamente” disponível no cadastro de parâmetros do *Workflow* é importante saber que nem sempre é possível enviar as mensagens em um determinado momento. Poderão ocorrer alguns problemas que podem acarretar fila de espera e, com isso, crescerá o número de processos parados. Entre os problemas mais comuns está a perda da comunicação com o servidor de e-mail.  
Para evitar tais problemas é interessante agendar através do Schedule do Protheus a função *WFSendMail* (“Código\_Empresa”, “Código\_Filial”). Assim, haverá a garantia de que a qualquer momento as mensagens  que eventualmente tenham ficado na fila de espera (pasta "Outbox" do *Workflow*) serão enviadas.  
  
Exemplo:  
**WFSendMail( “99”, “01” )  
  
  
Saiba mais:  
[FAQs Workflow](https://tdn.totvs.com/display/PROT/FAQs+-+Workflow)**
