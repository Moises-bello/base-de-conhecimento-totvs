---
article_id: 20507404920727
category: Materiais - Compras (SIGACOM)
content_hash: cb154a7a48ddc9b63afc4d5664df64dee7c58d35e1fa6bfd3ac2bf40598133ab
fetched_at: '2026-06-28T22:41:19.928550+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Geração
  do CIAP
type: support-article
updated_at: '2024-06-11T17:41:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20507404920727-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Gera%C3%A7%C3%A3o-do-CIAP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20507404898711) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como é realizado o cálculo do imposto de CIAP, o processo de importação ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

Ao importar um XML de conhecimento de frete que possua o cálculo do imposto de CIAP, o processo de importação ocorrerá através das rotinas de Pré-nota (Mata140) ou Documento de Entrada (Mata103). Dessa forma o valor do CIAP do XML de conhecimento de frete será gerado de forma segregada, ou seja, não será agregado ao CIAP da Nota de Origem como ocorre através do processo de inclusão manual através da rotina de Conhecimento de Frete (Mata116). Atualmente a importação direta do XML pelo Mata116 ainda não é possível, somente através de modificação do processo atual que nesse caso precisa ser solicitado através de Sugestão de Melhoria no Sistema.

Saiba mais em :

[Importador XML - Geração do CIAP](https://tdn.totvs.com/pages/releaseview.action?pageId=818453078)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada Importador XML](Cross%20Segmentos%20-%20Totvs%20Backoffice%20Protheus%20-%20SIGACOM%20-%20Pontos%20de%20Entrada%20Importador%20XML)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
