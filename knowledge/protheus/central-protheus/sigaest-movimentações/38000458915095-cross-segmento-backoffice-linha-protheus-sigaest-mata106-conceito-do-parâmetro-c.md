---
article_id: 38000458915095
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b1b66f9a45def9a2b43d0461ed0b2a3963b46651415f96e06ed7cb7fe225291d
fetched_at: '2026-06-28T22:38:54.047195+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA106 - Conceito
  do parâmetro: Considera data da? (Necessidade/Emissão)'
type: support-article
updated_at: '2026-01-29T11:06:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38000458915095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA106-Conceito-do-par%C3%A2metro-Considera-data-da-Necessidade-Emiss%C3%A3o
---

O campo "Considera data da?" na rotina MATA106 define a prioridade para gerar Solicitações de Compras, escolhendo entre data de necessidade ou data de emissão das SA na MATA105. Se selecionado data de necessidade, as SC são geradas conforme a menor data de necessidade; se data de emissão, conforme a menor data de emissão. O impacto ocorre apenas quando múltiplas pré-requisições são geradas simultaneamente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38000458903959) Tempo aproximado para leitura: **01:00 min**  
  
**Dúvida**  
Qual a finalidade do pergunte "Considera data da?" na rotina de geração de pré-requisição(MATA106)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Esse campo define a prioridade em que as Solicitações de Compras serão geradas, ou pela data de necessidade ou pela data de emissão que são informadas na inclusão da SA na MATA105.  
 Ex:

* Na inclusão da SA foi incluída uma data de necessidade(CP\_DATPRF) posterior a data de emissão(CP\_EMISSAO/DA105DATA) e no pergunte for selecionado Data de Necessidade, a SC será gerada primeiro para as SA's com a data de necessidade menor.
* Quando selecionado por data de emissão, as SC's serão geradas primeiro para as SA's com data de emissão menor.

  Resumindo, esse pergunte só terá impacto nas ordens em que as Solicitações de Compras serão geradas e caso seja gerado diferentes pré-requisições ao mesmo tempo. Caso seja gerado apenas uma pré-requisição, também não terá impacto.

**Saiba mais:**

# [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA106 - Conceito dos parâmetros: Considera o Armazém da SA?, Saldo do Armazém? e Saldo Até o Armazém?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35428967631511) [*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
