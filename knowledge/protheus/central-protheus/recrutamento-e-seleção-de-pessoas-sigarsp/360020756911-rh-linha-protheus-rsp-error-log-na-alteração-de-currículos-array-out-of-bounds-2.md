---
article_id: 360020756911
category: Recrutamento e Seleção de Pessoas (SIGARSP)
content_hash: 574c51be349c08a3fc7022e0697af496f2787c8017d4404183cd642a91df9f83
fetched_at: '2026-06-28T22:43:00.917166+00:00'
product: protheus
section_id: 206960907
source: central-protheus
title: 'RH - Linha Protheus - RSP - Error log na alteração de currículos: array out
  of bounds ( 2 of 1 ) on A010ATUSQR(RSPA010.PRW) 25/05/2018 17:25:22 line : 1675'
type: support-article
updated_at: '2021-09-10T02:43:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020756911-RH-Linha-Protheus-RSP-Error-log-na-altera%C3%A7%C3%A3o-de-curr%C3%ADculos-array-out-of-bounds-2-of-1-on-A010ATUSQR-RSPA010-PRW-25-05-2018-17-25-22-line-1675
---

**Dúvida**O que conferir quando ao acessar o Módulo 20 (SIGARSP) **Recrutamento e Seleção,** e solicitar alteração de um currículos, o sistema gera error log:" ***array out of bounds*** **( 2 of 1 ) *on* A010ATUSQR(RSPA010.PRW) 25/05/2018 17:25:22 line : 1675"?**  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recrutamento e Seleção Pessoal – Todas as versões  
  
**Causa**O problema é decorrente a inconsistência no dicionário de dados. A tabela SQR por padrão existem alguns campos com legenda vermelha para demonstrar que não podem ocorrer alterações de estrutura ou de ordem.   
  
No dicionário padrão Totvs, o campo **QR\_VAGA** precisa obrigatoriamente ter ordem 12.   
Se alterada a ordem dos campos QR\_VAGA e QR\_DATA, ocorre o error log.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ajustar ordem dos campos  **QR\_VAGA** e **QR\_DATA** para **12** e **13** conforme dicionário padrão.  
  
**Importante**  
Não é permitida alteração da ordem de campos com legenda vermelha via Configurador. O sistema irá validar as legendas para permissão da manutenção.  
  
**Saiba Mais**[Artigos Recrutamento e Seleção de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960907-RH-Recrutamento-e-Sele%C3%A7%C3%A3o-de-Pessoal)
