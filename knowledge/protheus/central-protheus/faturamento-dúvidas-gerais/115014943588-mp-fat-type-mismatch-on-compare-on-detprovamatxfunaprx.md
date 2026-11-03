---
article_id: 115014943588
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3789dee97713516980443087f461cec126737dcd60b3d39a72b89a07dee80b4a
fetched_at: '2026-06-28T22:38:31.148544+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT- type mismatch on compare  on DETPROVA(MATXFUNA.PRX)
type: support-article
updated_at: '2021-04-28T15:56:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115014943588-MP-FAT-type-mismatch-on-compare-on-DETPROVA-MATXFUNA-PRX
---

**Ocorrência**   
   
Error log ao gerar a contabilização de NF de SAIDA:  
type mismatch on compare  on DETPROVA(MATXFUNA.PRX) 25/05/2017 18:46:54 line : 6727  
  
**Causa**  
  
O erro ocorre por que o campo CT5\_VALOR precisa receber a query onde ele buscará o valor a ser contabilizado, e no entanto, está informado apenas a conta que ele deverá utilizar para contabilizar, conforme o trecho do erro:  
  
  Local 29: CVALOR(C) :IF(SD2->D2\_FILIAL == '0101','2101050101',IF(SD2->D2\_FILIAL == '0102','2101050102',IF(SD2->D2\_FILIAL == '0103','2101050103',IF(SD2->D2\_FILIAL == '0105','2101050105',SB1->B1\_CONTA))))  
  
Este campo deveria receber algo como SD2->D2\_VALOR, para contabilizar valores,  e não a conta contábil, para informar a conta esta query precisa estar no campo CT5\_DEBIT ou CT5\_CREDIT.  
**Ambiente**  
  
Microsiga Protheus - versão 11 e versão 12  
  
**Solução**  
  
Para solucionar, ajuste a  query de conta contábil no campo correto do lançamento padronizado, no caso CT5\_DEBIT ou CT5\_CREDIT, e nocampo CT5\_VALOR atribua a query para tratamento de valor, segue exemplo para tornar mais fácil o entendimento:  
  
CT5\_DEBIT = SB1->B1\_CONTA --->atribuição da query  para buscar a conta contábil  
CT5\_CREDIT=2101050101 ---->atribuição direta da conta contábil  
CT5\_VALOR = SD2->D2\_VALOR ---> atribuição da query para buscar o valor a ser contabilizado  
  
Veja que desta forma,não gerará o erro de tipo de comparação inválida.  
  
Obs..é necessário conhecimento técnico do processo e um pouco de programação advpl, caso seja necessário, solicite ao ESN um analista desenvolvedor in loco para auxiliar no processo.
