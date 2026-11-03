---
article_id: 360033128473
category: Escrita Fiscal - Error.log
content_hash: a3e84ed4e063fade2eca88026493c07e822ea55f0c3b64b3abb76b2662cc609a
fetched_at: '2026-06-28T22:39:32.829891+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Error Log - variable
  is not array - Type [U] on {|x| aTotal[06] += IiF(AllTrim(x[1])$aTotal[07][1],IIf(SubStr(x[1],1,1)$"123",-1*x[11],x[11]),0)}(MATA953.PRX)
type: support-article
updated_at: '2021-07-08T13:13:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033128473-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Error-Log-variable-is-not-array-Type-U-on-x-aTotal-06-IiF-AllTrim-x-1-aTotal-07-1-IIf-SubStr-x-1-1-1-123-1-x-11-x-11-0-MATA953-PRX
---

**Ocorrência**Ao gerar apuração de ICMS (MATA953) está ocorrendo seguinte error logs.

variable is not array - Type [U] on {|x| aTotal[06] += IiF(AllTrim(x[1])$aTotal[07][1],IIf(SubStr(x[1],1,1)$"123",-1\*x[11],x[11]),0)}(MATA953.PRX)   
  
**Ambiente**  
Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
**Causa**   
Esse incidente ocorre, pois parâmetro está incorreto ( MV\_GIASC01 )

|  |
| --- |
| Este parâmetro identifica os contribuintes que são optantes pelo regime Simples. Deve conter todos os CFOPs, tanto de entrada quanto de saída, que forem utilizados nas movimentações. Informe os CFOPs para as movimentações dos optantes pelo Simples. Deverá ser criado um array (entre chaves “{}”) em que, na primeira posição, deverão ser apresentados os CFOPs, separados por barras (“/”) e a segunda posição deverá ser deixada em branco, no seguinte formato: {“/CFOP/CFOP/”,””}. |

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Entre no Configurador ( SIGACFG );  
2. Entre nos Parâmetros;  
3. Busque o parâmetro MV\_GIASC01;  
4. Informe os CFOPs para as movimentações dos optantes pelo Simples. Deverá ser criado um array (entre chaves “{}”) em que, na primeira posição, deverão ser apresentados os CFOPs, separados por barras (“/”) e a segunda posição deverá ser deixada em branco, no seguinte formato: {“/CFOP/CFOP/”,””}.

Exemplo de conteúdo: {“/5101/1101/”,””}
