---
article_id: 360000984707
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4c5a028cc9e3f0d4184240919aa4e0891314758dde52ebc949850cf077193155
fetched_at: '2026-06-28T22:38:28.492367+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Alias does
  not exist SIX (PREVIOUS ERROR : Alias does not exist AOR)'
type: support-article
updated_at: '2023-05-02T17:51:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000984707-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Alias-does-not-exist-SIX-PREVIOUS-ERROR-Alias-does-not-exist-AOR
---

**Dúvida**

Ao abrir o módulo faturamento em modo SIGAMDI ou mudar de módulo ou acessar favoritos, ocorre o erro:

**Alias does not exist SIX ( PREVIOUS ERROR : Alias does not exist AOR )**

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Solução:**

Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Baixe o pacote mais atual da rotina **crma710.prw:  
CRM - <https://tdn.totvs.com/pages/releaseview.action?pageId=521997496#issues-17>  
TMK - <https://tdn.totvs.com/pages/releaseview.action?pageId=521997552#issues-17>**

**2.** Aplique o pacote, via TDS, em seu ambiente de teste (Homologação) para validação e posteriormente, no ambiente de produção.

**Obs: O erro somente deixará de ocorrer, se a rotina CRMA710 estiver igual ou superior a 20.09.17.**

 A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.

Caso não possua a estrutura da tabela AOR e seja necessária para complementar a estrutura, acesse a faq **FAT0233**, onde contém a estrutura para download:  **[Alias does not exist AOR on CRM710P360](http://tdn.totvs.com/pages/viewpage.action?pageId=286500930)**
