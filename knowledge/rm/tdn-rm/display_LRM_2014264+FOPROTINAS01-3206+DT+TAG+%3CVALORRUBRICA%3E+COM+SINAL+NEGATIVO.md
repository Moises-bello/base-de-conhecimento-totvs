---
content_hash: 173a98a5ffbbe650ac16d5e19a80b51b6de2183adf668273acde226622db95b5
fetched_at: '2026-06-29T00:08:51.612444+00:00'
page_id: '337351234'
product: rm
source: tdn-rm
title: 2014264 FOPROTINAS01-3206 DT TAG <VALORRUBRICA> COM SINAL NEGATIVO
type: documentation
url: https://tdn.totvs.com/display/LRM/2014264+FOPROTINAS01-3206+DT+TAG+%3CVALORRUBRICA%3E+COM+SINAL+NEGATIVO
version: 1
---

# REMOÇÃO DO SINAL NEGATIVO DA TAG <VALORRUBRICA>

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | PPE |
| **Situação/Requisito:** | O sistema gera o valor da tag <valorrubrica> com sinal negativo quando o valor dos eventos de desconto associados a um determinado dispêndio individual supera o valor dos eventos de provento/base associados a ele. |
| **Solução/Implementação:** | Quando o valor total do dispêndio individual for negativo, o sistema passa a zerar esse valor e insere a seguinte mensagem no log de avisos:  "Chapa X - O dispêndio individual Y estava negativo e foi zerado. Isso ocorre quando o valor dos eventos de desconto associados a ele superam o valor dos eventos de provento e base."  Obs.: O processo será finalizado com ressalvas |
| **Tickets relacionados:** | 2014264 |
