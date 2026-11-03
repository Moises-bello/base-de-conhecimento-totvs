---
article_id: 21253554958103
category: TAF - eSocial - Eventos Periódicos
content_hash: 1682de39df517a6bacbb14ea6d555864b85bc1adacb73d2da196c5d5680ed6b3
fetched_at: '2026-06-28T22:45:18.906164+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: Automação Fiscal - Evento Periódico - S-1210 - Schema - cpfDep - Element [http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_02_00}cpfDep': [facet
  'pattern'] The value " is not accepted by the pattern 1d{11}'.
type: support-article
updated_at: '2024-02-09T21:00:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21253554958103-Automa%C3%A7%C3%A3o-Fiscal-Evento-Peri%C3%B3dico-S-1210-Schema-cpfDep-Element-http-www-esocial-gov-br-schema-evt-evtPgtos-v-S-01-02-00-cpfDep-facet-pattern-The-value-is-not-accepted-by-the-pattern-1d-11
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21253550437015) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**

Ao tentar transmitir o evento S-1210 (Pagamentos de Rendimento) ao governo, eSocial, ocorre o erro de Schema abaixo:

***Erro de schema: Element [[http://www.esocial.gov.br/schema/evt/evtPgtos/v\_S\_01\_02\_00}cpfDep':](http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_02_00%7DcpfDep':) [facet 'pattern'] The value " is not accepted by the pattern 1d{11}'.***  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal- S-1210 (TAFA407) - Evento Periódico - Todas as versões.  
  
**Causa**O erro ocorre pois existe campo de CPF de dependentes (cpfDep)  sem conteúdo, no XML do TAF.  
  
**Solução**

**1.** Para corrigir o erro, o ambiente precisa estar atualizado com a última Expedição Contínua do TAF, links para download abaixo:

⚠️ Clientes Segregados, RM, Datasul, Logix, entre outros, apenas aplicar a Expedição Contínua do TAF:

12.1.33 - Para segregados e para clientes Protheus que possuem Garantia Estendida.

<https://suporte.totvs.com/portal/p/10098/download?e=1043538>

12.1.2210

<https://suporte.totvs.com/portal/p/10098/download?e=1084563>

12.1.2310

<https://suporte.totvs.com/portal/p/10098/download#detail/1126399>

⚠️Clientes Protheus, precisam se manter atualizados conforme página de entregas legais do módulo:

<https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21253550442519)

Documentação completa, para atualização do TAF:

[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

**2.** Após atualizar o sistema, é necessário realizar a exclusão do evento S-1210 inconsistente e integra-lo novamente ao TAF.

**Dica:** Se possui muitos eventos S-1210 para realizar exclusão, utilize a rotina Exclusão em Lote no TAF, seguindo as orientações da documentação:

[Automação Fiscal - Periódicos - Como excluir eventos de folha em lote S-1200 e S-1210 no TAF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036104773)
