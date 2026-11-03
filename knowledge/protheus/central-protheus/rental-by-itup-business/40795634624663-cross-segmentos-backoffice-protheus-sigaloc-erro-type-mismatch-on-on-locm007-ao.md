---
article_id: 40795634624663
category: Rental by ItUp Business
content_hash: a855f0c3e6cf90792ec15ba17e27fbaafb620d7a643d9dd21dc5fa1b2e21f70e
fetched_at: '2026-06-28T22:36:20.629641+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Erro type mismatch on + on
  LOCM007 ao efetuar retorno de locação
type: support-article
updated_at: '2026-05-28T14:04:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40795634624663-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Erro-type-mismatch-on-on-LOCM007-ao-efetuar-retorno-de-loca%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40795665447703) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao efetuar o retorno da locação por meio do módulo SIGALOC na rotina LOCA001 (Orçamento), o sistema apresenta o seguinte erro: type mismatch on + on LOCM007(LOCM007.PRW)  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
O problema está relacionado à falta de validação no parâmetro MV\_LOCBAC quando este encontra-se ativo. Por este motivo, as filiais que não possuem a integração com o módulo de Rental apresentam a ocorrência.

Passos

1. Acesse o módulo Configurador (SIGACFG).
2. Vá em Ambiente, clique em Cadastros e selecione Parâmetros.
3. Localize o parâmetro MV\_LOCBAC.
4. Desative o parâmetro para todas as filiais.
5. Crie um parâmetro exclusivo para a filial específica que possui a integração com o módulo de Locação de Equipamentos.
