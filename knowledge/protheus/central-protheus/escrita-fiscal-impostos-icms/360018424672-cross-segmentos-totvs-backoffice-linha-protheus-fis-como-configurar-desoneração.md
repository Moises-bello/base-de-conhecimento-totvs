---
article_id: 360018424672
category: Escrita Fiscal - Impostos - ICMS
content_hash: f376d868a3bd33ac0ef3462a9af54fe7490cf25510e96480895357b8f737f4f3
fetched_at: '2026-06-28T22:39:24.391034+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar desoneração
  nas vendas para órgão público '
type: support-article
updated_at: '2024-05-21T16:47:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018424672-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-desonera%C3%A7%C3%A3o-nas-vendas-para-%C3%B3rg%C3%A3o-p%C3%BAblico
---

**Dúvida**Como configurar a desoneração nas vendas para órgão público?   
   
 **Ambiente**Protheus - Livro Fiscais - A partir da versão 11.80  
  
   
**Solução** A configuração correta para desoneração é:

Cliente:   
 Tipo Pessoa (A1\_TPESSOA) = EP -Indica que é empresa pública.

TES:

Agrega Valor (F4\_AGREG) = D – Indica que deve descontar o valor do imposto do valor contábil.  
Cálculo ICMS (F4\_ICM) = Sim – Indica que haverá o cálculo do ICMS.  
Livro Fiscal ICMS (F4\_LFICM) = Isento – Indica que será escriturado como Isento.  
 Sit.Trib.ICMS (F4\_SITTRIB) = 40 – Indica que Isento.  
 Mot.Desone. (F4\_MOTICMS)= 8 - Venda órgão público
