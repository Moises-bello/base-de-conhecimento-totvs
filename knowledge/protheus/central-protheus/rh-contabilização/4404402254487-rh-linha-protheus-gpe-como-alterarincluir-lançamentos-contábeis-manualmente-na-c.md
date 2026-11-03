---
article_id: 4404402254487
category: RH - Contabilização
content_hash: 4333a3b049f7997def9425471bd450317e56f2300769ad806969efe23f95eedf
fetched_at: '2026-06-28T22:43:46.065301+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como alterar/incluir lançamentos contábeis manualmente
  na contabilização da folha de pagamento
type: support-article
updated_at: '2025-07-30T02:30:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404402254487-RH-Linha-Protheus-GPE-Como-alterar-incluir-lan%C3%A7amentos-cont%C3%A1beis-manualmente-na-contabiliza%C3%A7%C3%A3o-da-folha-de-pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33811068525335) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como alterar/incluir lançamentos contábeis manualmente na contabilização da folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**Após  o processamento da rotina GPEM110, os lançamentos contábeis serão apresentados em tela conforme print abaixo:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404415247383)

Para que seja permitida a alteração/inclusão dos lançamentos manualmente, acesse o Configurador (SIGACFG) / Ambiente/Cadastros/Parâmetros:

1) Configure o parâmetro MV\_ALTLCTO = S

**MV\_ALTLCTO:** Permite alterar os lançamentos contábeis de integração. No caso de não permitir a alteração de lançamentos, e se estes tenham alguma inconsistência de valor ou entidades contábeis não existentes, o lançamento será obrigatoriamente gravado como pré-lançamento.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404402093847)  
  
2) Configure o parâmetro MV\_NUMMAN = 99999  
**MV\_NUMMAN:** Limita o número de linhas do documento no lançamento contábil manual  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404416289687)

**Saiba Mais**Para adquirir mais conhecimento acesse os *links* abaixo:  
[MP - SIGACTB - MV\_NUMLIN MV\_NUMMAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006753632-MP-SIGACTB-MV-NUMLIN-MV-NUMMAN)  
[MP - SIGACTB - Habilita a Alterar lançamento de contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019890351-MP-SIGACTB-Habilita-a-Alterar-lan%C3%A7amento-de-contabiliza%C3%A7%C3%A3o-)
