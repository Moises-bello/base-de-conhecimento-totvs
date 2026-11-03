---
article_id: 360042726953
category: Financeiro - Contas a Pagar
content_hash: 79cfccc83e65c0e6e3b68e924609c415c9e9def318e970910a534de79917ad91
fetched_at: '2026-06-28T22:38:09.885762+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA240 - Na rotina Fina240, opção Borderô ocorre o alerta "Numero
  de código reservado maior que 20"
type: support-article
updated_at: '2021-04-28T15:18:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042726953-MP-SIGAFIN-FINA240-Na-rotina-Fina240-op%C3%A7%C3%A3o-Border%C3%B4-ocorre-o-alerta-Numero-de-c%C3%B3digo-reservado-maior-que-20
---

**Ocorrência**

Na rotina **FINA240**, opção Borderô ocorre o alerta "Numero de código reservado maior que 20".

**Ambiente**  
Exemplo:  
Microsiga-Protheus – Financeiro – A partir da versão 12.1.17  
   
 **Causa**  
 Esse incidente ocorre na **FINA240,** quando ao clicar no borderô o sistema exibe a mensagem:

**"Numero de código reservado maior que 20"**  
   
 **Solução**  
 Para solucionar essa ocorrência, é necessário realizar alteração no parâmetro **"MV\_NUMBORR",** contas a receber ou **"MV\_NUMBORP"**contas a pagar.

**Exemplo:** último borderô gerado = "002398" o parâmetro grava com o conteúdo do próximo borderô, sendo necessário incluir a sequência desejada.
