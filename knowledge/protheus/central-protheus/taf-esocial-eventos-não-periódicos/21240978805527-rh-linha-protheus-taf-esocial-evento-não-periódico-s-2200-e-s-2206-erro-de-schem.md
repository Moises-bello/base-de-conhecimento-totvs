---
article_id: 21240978805527
category: TAF - eSocial - Eventos Não Periódicos
content_hash: a8897ab3c95a9c9d72d781a3a5e256888e9d9d07aa9bec72663dde237f337ce1
fetched_at: '2026-06-28T22:45:17.972804+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Evento Não Periódico - S-2200 e S-2206
  - Erro de Schema: indAprend - Menor aprendiz -  {http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_02_00}indAprend
  )'
type: support-article
updated_at: '2026-06-24T21:34:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21240978805527-RH-Linha-Protheus-TAF-eSocial-Evento-N%C3%A3o-Peri%C3%B3dico-S-2200-e-S-2206-Erro-de-Schema-indAprend-Menor-aprendiz-http-www-esocial-gov-br-schema-evt-evtAdmissao-v-S-01-02-00-indAprend
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21241014175895) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao tentar transmitir o evento periódico S-2200 (Cadastro Inicial de Vínculo e Admissão) ou o evento S-2206 (Alteração de Contrato de Trabalho) ocorre os erros de Schemas abaixo listados:

***Erro de schema: Element '{<http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_02_00>}tpInsc': This element is not expected. Expected is ( {<http://www.esocial.gov.br/schema/evt/evtAdmissao/v_S_01_02_00>}indAprend ).***

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal- S-2200 (TAFA278) e S-2206 (TAFA276) - Evento Não Periódico - Todas as Versões  
  
**Causa**O erro ocorre pela falta de campo, referente ao Menos Aprendiz, obrigatório para o leiaute S-1.2.  
  
**Solução**Para corrigir o erro, o ambiente precisa estar atualizado com a última **Expedição Contínua do TAF**,  **obrigatório** rodar a rotina **UPDDISTR**, para que os campos sejam criados corretamente, links para download abaixo:

\*\*\*\*Após atualizar o sistema, será necessário, excluir o evento S-2200 ou S-2206 do TAF e integra-lo novamente.

⚠️ Clientes Segregados, RM, Datasul, Logix, entre outros, apenas aplicar a Expedição Contínua do TAF:

[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

⚠️Clientes Protheus, precisam se manter atualizados conforme página de entregas legais do módulo:

<https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21240978760087)
