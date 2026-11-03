---
article_id: 35001849049751
category: Financeiro - Configurador de Tributos
content_hash: 2177e2ab830a3c221531d740c5caf9fdf78597c03e407ba2a07a2982f6edcd1d
fetched_at: '2026-06-28T22:37:46.071394+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Como determinar
  a data da geração do imposto quando gerado na emissão
type: support-article
updated_at: '2025-09-18T16:43:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35001849049751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-determinar-a-data-da-gera%C3%A7%C3%A3o-do-imposto-quando-gerado-na-emiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35001849021591) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como determinar a data da geração do imposto quando gerado na emissão?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210  
  
**Solução**  
A geração do imposto na emissão dependerá da configuração da regra financeira, na qual o fato gerador deve ser definido como **'Competência**'.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35001853863959)

Em seguida, no cadastro da regra de vencimento, deve-se definir a data-base a ser considerada para a geração do imposto, conforme o regime de competência (fato gerador na emissão). Nesse caso, o campo **“Data base p/ vencimento do imposto (Emissão)”** define o critério para a geração do **IRRF**, permitindo a seleção entre as seguintes opções:

* Data de emissão do título principal;
* Data de vencimento real do título principal;
* Data de emissão contábil do título principal (data de entrada do documento no sistema).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35001849027351)

Saiba mais

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
