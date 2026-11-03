---
article_id: 1500003585481
category: Financeiro - Contas a Pagar
content_hash: 29c42afcb356247830ecb5bd98cbb8714966275c8624169c8f35defaaa391e91
fetched_at: '2026-06-28T22:38:09.910414+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA401 - Gerar dados para DIRF utilizando o parâmetro Verifica
  Data ? = Título de imposto
type: support-article
updated_at: '2021-04-28T15:17:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003585481-MP-SIGAFIN-FINA401-Gerar-dados-para-DIRF-utilizando-o-par%C3%A2metro-Verifica-Data-T%C3%ADtulo-de-imposto
---

**Dúvida**Qual parâmetro utilizar para reprocessar os dados para DIRF na rotina FINA401 ?  
  
**Ambiente**Microsiga Protheus - Financeiro - A partir da versão 11.80  
  
**Solução**Para reprocessar os dados para a DIRF na rotina FINA401 utilizar o parâmetro Verifica Data ? = **TÍTULO PRINCIPAL**Embora exista o parâmetro Verifica Data ? **= Titulo de imposto** disponível na rotina, não consta como mecanismo válido na geração da DIRF em nenhuma documentação oficial (Receita Federal)  
  
**Observação:** Não será retirada esta opção pois ela esta vigente desde a criação da rotina e não é prudente retirar funcionalidades que hoje o cliente tem.  
  
**Saiba mais:**  
FIN0041\_CPAG\_Geração\_de\_Dados\_para\_DIRF\_(FINA401)  
<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=224126168>
