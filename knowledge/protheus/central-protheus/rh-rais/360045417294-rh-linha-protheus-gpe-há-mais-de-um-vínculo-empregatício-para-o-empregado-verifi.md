---
article_id: 360045417294
category: RH - RAIS
content_hash: 3a7714ef6e154109e0cf185b65e30605cda08b976f64dc86ef4e4e79e2af8832
fetched_at: '2026-06-28T22:44:05.641598+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE -  Há mais de um vínculo empregatício para o empregado.
  Verifique a data de admissão, data de desligamento e cbo
type: support-article
updated_at: '2025-09-04T20:45:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045417294-RH-Linha-Protheus-GPE-H%C3%A1-mais-de-um-v%C3%ADnculo-empregat%C3%ADcio-para-o-empregado-Verifique-a-data-de-admiss%C3%A3o-data-de-desligamento-e-cbo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34709259858583) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**

Ao importar o arquivo da RAIS no validador, é apresentada a mensagem: 2398 - Há mais de um vínculo empregatício para o empregado. Verifique a data de admissão, data de desligamento e cbo.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  A partir da Versão 12.1.17  
  
**Solução**

Esta mensagem é apresentada, pois a importação anterior não foi excluída.

Para que o arquivo da RAIS seja importado corretamente, realize os passos a seguir:

1. No validador GDRais, acesse Declaração / Excluir;
2. Selecione a empresa em questão e clique no botão Excluir;
3. Confirme a exclusão na opção Sim
4. Importe o novo arquivo.

**Saiba mais:**

[RH - RAIS](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030327-RH-RAIS)
