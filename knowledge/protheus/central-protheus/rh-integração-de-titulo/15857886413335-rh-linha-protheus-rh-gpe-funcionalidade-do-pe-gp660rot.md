---
article_id: 15857886413335
category: RH - Integração de Titulo
content_hash: 96013c2c7aaf89606ece99c2e58a6481e2f56975b0818afeb189c33de49e40c4
fetched_at: '2026-06-28T22:43:36.478769+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus RH - GPE - Funcionalidade do PE GP660ROT
type: support-article
updated_at: '2025-07-15T20:35:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15857886413335-RH-Linha-Protheus-RH-GPE-Funcionalidade-do-PE-GP660ROT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15857874730135) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Funcionalidade do PE GP660ROT

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal  - Versão 12.1.17  
  
  
**Solução**

Ponto-de-Entrada: GP660ROT (Menu Cadastro de Movimentação de Títulos)Descrição:  
O ponto de entrada permite manipular o menu da rotina de Cadastro de Movimentação de Títulos.

Sintaxe:  
GP660ROT - Menu Cadastro de Movimentação de Títulos ( [ Param1 ] ) --> aRotina

Parâmetros:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15857877577879)  

Retorno:  

**aRotina**

(array\_of\_record)* Array contendo as rotinas do Menu

Observações:

A ordem dos elementos do array que será adicionado ao menu deverá ser:  
1- Nome do botão;  
2-Rotina/Função a ser chamada;  
3-0 ( Obrigatório ser 0 (zero) );  
4-Ordem da rotina. Poder ser Nil (Nulo).

**Exemplos:**

User Function GP660ROT()  
Local aArea := GetArea()  
Local aRotina := ParamixB[1]//Alert("Passou pelo PE GP660ROT)

aAdd(aRotina, { "TE&STE","fMostLeg", 0 , 5, ,.F.})

RestArea(aArea)

Return (aRotina)

**Variáveis:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15857892710295)

![GIFGP660rot.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15863559532823)

**Saiba Mais:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=6079199>
