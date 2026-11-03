---
article_id: 9412078890519
category: SIGAEST - PROCESSAMENTOS
content_hash: 6c0537295134c3ad81eee5021842daed9d9f5905b42d3edc4269ceffef127e58
fetched_at: '2026-06-28T22:39:05.009122+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST- type mismatch on +
  on MA300PROCESS
type: support-article
updated_at: '2023-11-16T19:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9412078890519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-type-mismatch-on-on-MA300PROCESS
---

**Ocorrência**Ao processar a rotina MATA300 ou demais, ocorre erro **type mismatch on + on.**  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - 12.1.27/12.1.33.  
  
**Causa**Esse erro normalmente ocorre por conta de alguma inconsistência nos dados processados, como algum campo em branco, caractere especial ou inválido por exemplo.  
  
**Solução**Efetuar a aplicação do ultimo pacote acumulado do estoque custos, e reinstalar as procedures.

Pacote acumulado Estoque custos: **[CLIQUE AQUI](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/EST_expedicao_continua)**

Importante validar se o parâmetro MV\_A300THR possui um numero de threads que atendam sua necessidade.

Recomendado = 1

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)
