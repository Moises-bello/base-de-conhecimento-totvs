---
article_id: 4409278982295
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3cf71f4fc9507d67e2aa7b94c4a286903f2070edded1d1c6b902d58394bfa731
fetched_at: '2026-06-28T22:37:21.533550+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como incluir mais de
  uma medição em Aberto para o Contrato ( Múltiplas Medições ) ?
type: support-article
updated_at: '2025-07-25T12:03:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409278982295-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-incluir-mais-de-uma-medi%C3%A7%C3%A3o-em-Aberto-para-o-Contrato-M%C3%BAltiplas-Medi%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18404676092951) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como incluir mais de uma medição em Aberto para um mesmo Contrato ( Múltiplas Medições ) ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos  - A Partir da versão 12.1.25  
  
**Solução**

Nas configurações padrões do Gestão de Contratos as medições devem ser incluídas e encerradas sempre uma a uma, podendo incluir uma segunda medição para um mesmo contrato somente após a primeira ter sido encerrada.

Mas foi criada a possibilidade para se permitir a inclusão de múltiplas medições simultâneas para um mesmo contrato. Dessa forma os saldos das planilhas passam a ser consumidos na inclusão da medição ao invés do encerramento.

Abaixo imagem do campo ***CN1\_SLDMED*** do Tipo de Contrato que deve estar como "2 - Inclusão" para permitir a inclusão duas ou mais medições em aberto ao mesmo tempo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33694036352023)

Para a implementação, verificar a documentação do link abaixo:

[DMANMAT02-30677 DT Permitir a inclusão de múltiplas medições](https://tdn.totvs.com/x/gvwWIw)

***Obs:***

Para a mudança da configuração no modo de utilização no cadastro do Tipo de Contrato, não pode haver nenhuma medição em aberto de contrato que utilize este Tipo de Contrato que está sendo alterado.

***Saiba Mais:***

[DMANMAT02-30677 DT Permitir a inclusão de múltiplas medições](https://tdn.totvs.com/x/gvwWIw)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
