---
article_id: 13982837224471
category: RH - Integração de Titulo
content_hash: d072145a1456c59a29440e27a8200b24202bc29e676c12357c1bdd84660a6926
fetched_at: '2026-06-28T22:43:36.347102+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Funcionalidade do ponto de Entrada: GP660ROT (Menu
  Cadastro de Movimentação de Títulos)'
type: support-article
updated_at: '2025-07-15T20:36:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13982837224471-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-Entrada-GP660ROT-Menu-Cadastro-de-Movimenta%C3%A7%C3%A3o-de-T%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22757028497175) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Funcionalidade do ponto de Entrada: GP660ROT (Menu Cadastro de Movimentação de Títulos)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal  - Versão 12.1.17  
  
  
**Solução**

Descrição:  
O ponto de entrada permite manipular o menu da rotina de Cadastro de Movimentação de Títulos.

Programa Fonte:

GPEM660.PRX

Sintaxe:  
GP660ROT - Menu Cadastro de Movimentação de Títulos ( [ Param1 ] ) --> aRotina

Parâmetros:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22757039739543)  

Retorno:  

**aRotina**

(array\_of\_record)* Array contendo as rotinas do Menu

Observações

A ordem dos elementos do array que será adicionado ao menu deverá ser:  
1- Nome do botão;  
2-Rotina/Função a ser chamada;  
3-0 ( Obrigatório ser 0 (zero) );  
4-Ordem da rotina. Poder ser Nil (Nulo).

Exemplos:

```
User Function GP660ROT()Local aArea 	:= GetArea()Local aRotina 	:= ParamixB[1]//Alert("Passou pelo PE GP660ROT)aAdd(aRotina, { "TE&STE","fMostLeg", 0 , 5, ,.F.})RestArea(aArea)Return (aRotina)
```

![GIFGP660rot.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/14046854012567)

Saiba Mais:  
[RH - Linha Protheus - GPE - Quais são os pontos de entrada disponíveis na rotina GPEM660](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036292353-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM660)
