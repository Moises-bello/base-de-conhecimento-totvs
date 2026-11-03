---
article_id: 360027869112
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 25e2753ea11d238d09fcd3c3e556243720339eb48ae0bad3722147c89ca29dcc
fetched_at: '2026-06-28T22:38:32.683084+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-type mismatch on +  on FT300CARGO(FATN300A.PRX)
type: support-article
updated_at: '2021-04-28T15:54:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027869112-MP-FAT-type-mismatch-on-on-FT300CARGO-FATN300A-PRX
---

**Ocorrência**

Erro na alteração da oportunidade : **type mismatch on + on FT300CARGO(FATN300A.PRX) 11/06/2018 15:50:13 line : 2043**  
   
 **Ambiente**

Microsiga Protheus - versão 12.  
   
 **Causa**

O erro ocorre por que o  x3\_relação (inicializador padrão) do campo **AD2\_CARGO**, está incorreto.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Acesse o configurador, Dicionário, Base de dados, e selecione a tabela **AD2**;  
 2. Ajuste o inicializador padrão do campo **AD2\_CARGO****para IIF(!INCLUI,Ft300NCargo(AD2->AD2\_CODCAR),"")**  ;  
 3. Salve o campo, salve a tabela e atualize o dicionário de dados.

![Altera__o_da_AD2_Cargo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360028015551/Altera__o_da_AD2_Cargo.gif)
