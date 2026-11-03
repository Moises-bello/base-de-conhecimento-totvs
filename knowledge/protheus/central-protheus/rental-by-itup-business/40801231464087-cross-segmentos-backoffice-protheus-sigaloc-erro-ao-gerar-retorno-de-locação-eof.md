---
article_id: 40801231464087
category: Rental by ItUp Business
content_hash: 3eab047dad64754443bf19b91661a7eb91f6a3d063ae6a2c4d24661baddb61d1
fetched_at: '2026-06-28T22:36:20.614164+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Erro ao gerar retorno de
  locação EOF Stack em MSRLOCK
type: support-article
updated_at: '2026-05-28T16:48:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40801231464087-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Erro-ao-gerar-retorno-de-loca%C3%A7%C3%A3o-EOF-Stack-em-MSRLOCK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40801241011991) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Erro ao gerar devolução de locação, apresenta a mensagem EOF  "**EOF Stack em MSRLOCK**" como corrigir?   
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Solução**

A mensagem "EOF Stack em MSRLOCK" indica que a rotina tentou reservar um registro para ser manipulado no processamento; mas o ponteiro da tabela estava em FIM DE ARQUIVO (MODO EOF) pois não localizou o dado procurado na Tabela.

Ou seja, algum dado (relacionado a este registro que está sendo processado) está inválido / não foi localizado, apresentando quebra de integridade.  
  
Desenvolvemos a documentação [EOF Stack de chamadas em MSRLOCK.eof Controle de transaçoes Habilitado](https://tdn.totvs.com/pages/releaseview.action?pageId=235575485) onde no **tópico 3 (PROCEDIMENTOS)**, sugerimos uma série de avaliações a serem feitas, bem como explicamos com mais detalhes este erro. Peço gentilmente que valide.
