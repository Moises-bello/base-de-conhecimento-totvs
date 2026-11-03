---
article_id: 360016455212
category: ADVPL - Classe e Função
content_hash: e6022b632f2f9c3b3b79112a4e2d4a97d14a4a34ab56283eb1d38bedc31382b8
fetched_at: '2026-06-28T22:40:17.067718+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Padrão de projeto
  singleton
type: support-article
updated_at: '2022-06-13T17:19:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016455212-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Padr%C3%A3o-de-projeto-singleton
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**É possível implementar o padrão de projeto ([*design pattern*](https://pt.wikipedia.org/wiki/Padr%C3%A3o_de_projeto_de_software)) [Singleton](https://pt.wikipedia.org/wiki/Singleton)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Atualmente na linguagem ADVPL não é possível implementar o padrão de projeto [Singleton](https://pt.wikipedia.org/wiki/Singleton), dado ao fato que é necessário que a propriedade que armazenará a instância da classe tenha escopo privado (assim como o construtor), contudo o ADVPL não possui identificadores de escopo de privem o usuário do acesso direto.
