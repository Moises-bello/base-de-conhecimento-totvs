---
article_id: 360045691434
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b27f265f274f8233cef9d25889e63236911ac49a0f1a1fd90fe1935bfcb1bf83
fetched_at: '2026-06-28T22:38:32.678710+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-type mismatch on +  on CTBSERIALI(CTBXSEM.PRW)
type: support-article
updated_at: '2021-04-28T15:53:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045691434-MP-FAT-type-mismatch-on-on-CTBSERIALI-CTBXSEM-PRW
---

**Ocorrência**Ao efetuar a **contabilização** **off** **line** (**CTBANFS**) da **nota** **de** **saída** (**MATA461**), ocorre o erro:

**type mismatch on +  on CTBSERIALI(CTBXSEM.PRW) 02/01/2020 15:42:12 line : 870**

**Ambiente**

Microsiga Protheus - todas as versões.  
   
 **Causa**

O erro ocorre devido a falta de parâmetros do semáforo de contabilização no ambiente ou não criados com os tipos corretos ou não configurados:

**MV\_CTBSER** - Tipo **Numérico** ---> **correto** Tipo **Carácter** com conteúdo 1, 2 ou 3;  
**MV\_CTBNFSE** - Tipo **Numérico** ---> **correto** Tipo **Carácter** com conteúdo 1(ligado)ou 2(desligado);  
**MV\_CTBSERD** - Tipo  **Carácter** ---> **correto** Tipo **Lógico** com conteúdo .T. ou .F. ;  
**MV\_CONOUTR** -Tipo **Carácter**--->**correto** Tipo **Numérico**  com  conteúdo 0, 1, 2 ou 3.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Certificar que os parâmetros de semáforo contábil estejam criados e devidamente configurados no ambiente, caso não estejam configurar conforme as documentações da área:

**[MP - SIGACTB - CONFIGURAÇÃO DE SEMAFORO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006840232-MP-SIGACTB-CONFIGURA%C3%87%C3%83O-DE-SEMAFORO?)** 

**[MP-SIGACTB-Type-mismatch-on-compare-on-CONOUTR?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015938491-MP-SIGACTB-Type-mismatch-on-compare-on-CONOUTR?)**

2. Reiniciar o Smartclient e efetuar o processo de contabilização novamente.

***Obs: Em caso de dúvidas sobre o funcionamento do semáforo contábil, entre em contato coma equipe de atendimento Ativo e Contábil.***
