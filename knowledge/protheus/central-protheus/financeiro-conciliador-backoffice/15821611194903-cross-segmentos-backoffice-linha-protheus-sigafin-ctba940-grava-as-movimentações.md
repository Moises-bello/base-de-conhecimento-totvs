---
article_id: 15821611194903
category: Financeiro - Conciliador Backoffice
content_hash: 5b017c025267f868d929a82b143b12fed5b1a368a2876904d4e0b9ab76ad8529
fetched_at: '2026-06-28T22:37:47.201220+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Grava as
  movimentações bancárias com data de 2020
type: support-article
updated_at: '2026-05-27T19:30:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15821611194903-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Grava-as-movimenta%C3%A7%C3%B5es-banc%C3%A1rias-com-data-de-2020
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15821580165655) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao realizar a Conciliação Automática, grava o campo de data (IG\_DTEXTR) com ano de 2020  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para os parâmetros de bancos (FINA130), para o campo Formato Data estar igual a 1.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15821487592215)  
  
**Solução**  
Ajustar o parâmetro para 4 - DDMMAAAA e excluir o processo de conciliação na CTBA940**,** processar novamente o arquivo de conciliação e será gravado o ano do arquivo.
