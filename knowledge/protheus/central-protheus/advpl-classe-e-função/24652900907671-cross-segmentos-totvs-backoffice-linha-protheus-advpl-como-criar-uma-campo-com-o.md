---
article_id: 24652900907671
category: ADVPL - Classe e Função
content_hash: 1d4f663085d4d3da88bc71e8e18f9c2751a8ae0c78b8f68f11f7dea52dd530e2
fetched_at: '2026-06-28T22:40:21.582757+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Como criar uma
  campo com opções de seleção (X3_CBOX)
type: support-article
updated_at: '2024-10-24T15:03:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24652900907671-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-uma-campo-com-op%C3%A7%C3%B5es-de-sele%C3%A7%C3%A3o-X3-CBOX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652916723863) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como criar um campo de usuário que possua opções de seleção (CheckBox)?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Todas as versões.  
  
**Solução**Os campos que possuem opções de seleção apresentam as opções que estão preenchidas no campo "Lista de Opções" (X3\_CBOX):

![Lista de Opções.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652916725527)

E a validação da opção seleciona, para que o usuário não digite uma opção que não esteja disponível, é realizada pela função "Pertence" ([Função Pertence()](https://tdn.totvs.com/x/kYFzAQ)) preenchida no campo "Val. Sistema" (X3\_VALID) ou "Val. Usuário"(X3\_VLDUSER):

![Validação.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24652916726679)

Neste exemplo, as opções disponíveis no campo são F=Física ou J=Jurídica, e a função "Pertence()" garante que o usuário selecione uma das duas, evitando o preenchimento de outro conteúdo.

**Saiba mais:**  [SX3 - Campos das tabelas](https://tdn.totvs.com/x/zQJXAQ)
