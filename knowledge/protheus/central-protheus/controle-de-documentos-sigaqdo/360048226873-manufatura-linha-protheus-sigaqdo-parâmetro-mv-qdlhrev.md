---
article_id: 360048226873
category: Controle de Documentos (SIGAQDO)
content_hash: 1114e1a1eb20d4d71fc986d0199076e754dfbbe3919de6149a8befa401318c87
fetched_at: '2026-06-28T22:42:29.233391+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Parâmetro MV_QDLHREV
type: support-article
updated_at: '2021-05-26T12:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048226873-Manufatura-Linha-Protheus-SIGAQDO-Par%C3%A2metro-MV-QDLHREV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Qual o conceito do parâmetro **MV\_QDLHREV**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**O parâmetro **MV\_QDLHREV - Define se o Motivo da Revisão devera ser apagado acada geração de revisão** quando parametrizado como **N** **- Não** mantém um histórico do motivo da revisão informado pelo usuário quando gerado uma nova do documento por meio da opção **Outras Ações/Gera Revisão** da rotina **QDOA050 - Cadastro de Documentos**.  
O texto informado no motivo da revisão é registrado na tabela **QA2 - Textos Gerais do Módulo Qualidade** no campo **QA2\_TEXTO - Linha**, e é visualizado na rotina **QDOA050** na aba **Opções** em **Motivo da Revisão**.
