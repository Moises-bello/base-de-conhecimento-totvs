---
article_id: 4405003124375
category: SIGAACD - Automação e Coleta de Dados
content_hash: c16eae1ecdeb2edc1074b9de36af26bf73b90e40862c83dcac3037a884dab355
fetched_at: '2026-06-28T22:39:12.504723+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Cenários de Coletor
  Padrão não reproduzidos em Emuladores
type: support-article
updated_at: '2021-07-27T19:52:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405003124375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Cen%C3%A1rios-de-Coletor-Padr%C3%A3o-n%C3%A3o-reproduzidos-em-Emuladores
---

**Dúvida**O que fazer em cenários onde um processo tem determinado comportamento no Coletor Padrão e o mesmo não é reproduzido em Emuladores (VTDEBUG, TeraTerm, etc)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Tempo aproximado para leitura: 00:01:36 min

Todo e qualquer cenário ocorrido no Coletor Padrão que **não é reproduzido** em emuladores **inviabilizam** a atuação do Suporte Técnico padrão, pois o escopo do mesmo consiste em validações de comportamento de fontes do SIGAACD, onde, havendo uma não conformidade nas rotinas, o mesmo deve ser reproduzido em um emulador. Quando isso não acontece, inviabiliza o diagnóstico de não conformidade no produto e fontes envolvidos

Sendo assim, o suporte atua com análise, validação, debug e testes **única e exclusivamente do fonte envolvido no problema**. Caso exista um problema ocorrido apenas no Coletor, recomendamos fortemente que acione ao Suporte da fabricante do mesmo, onde os mesmos poderão indicar situações como por exemplo: atualização geral do Coletor, atualização de firmware, etc.

**VTDEBUG - Limitações**

A Rotina VTDEBUG é de responsabilidade da equipe de Framework e a mesma tem o objetivo de simular um coletor de dados criada para que os desenvolvedores possam debugar uma rotina para investigação de erros, e **seus recursos de tela são limitados**, **não sendo exatamente o que mostraria num coletor de dados real** **e não indicada para uso em substituição ao coletor de dados**. Sempre que tiver situações onde o emulador tem um comportamento visual diferente do Coletor Padrão, estas questões não são validadas pelo Suporte Técnico e o Produto entende que o emulador terá limitações, pois o objetivo não é visual, mas sim de testes.

Para mais informações, clique no link abaixo:

[Limitações - VTDEBUG](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=561064716)

**Layout de tela - Coletores Padrões**

Em cenários em que um coletor padrão, seja de qualquer marca, apresentar problemas de layout, o mesmo deve acionar a fabricante do próprio Coletor, para que sejam efetuados processos de configuração de tela do equipamento.

**Saiba mais:**

*[Clique aqui e veja mais informações sobre Automação e Coleta de Dados (ACD)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
