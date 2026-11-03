---
article_id: 4405264551319
category: SIGAACD - Automação e Coleta de Dados
content_hash: eaa7872ce4c8a8468669baf8ef5e99d5a7a01bbf4a73593348f7cb8b903d68ce
fetched_at: '2026-06-28T22:39:11.216574+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV020 - Não está
  gerando registro de produto MOD via ACD
type: support-article
updated_at: '2022-07-14T12:36:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405264551319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV020-N%C3%A3o-est%C3%A1-gerando-registro-de-produto-MOD-via-ACD
---

**Dúvida**Ao efetuar a produção simples (ACDV020) no ACD, quando se trata de produto MOD não está gerando registros na SD3. Como corrigir este problema?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:26 min**

Neste cenário, devemos verificar o conteúdo do parâmetro MV\_CBCALPR, que determina o Calculo do total de horas na Prod.Mod2 via RF/ ACD. Onde:

.T. = Usar calendário (Padrão) ou

.F. = usar calculo padrão da rotina da Produção Mod.2 (MATA681)

Quando se trata de MOD, é recomendável deixar o parâmetro = .F. para que os registros sejam feitos na SD3 corretamente.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados (ACD)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*

*[Parâmetros SIGAACD (Automação e Coleta de Dados)](https://tdn.totvs.com/pages/releaseview.action?pageId=235596091)*
