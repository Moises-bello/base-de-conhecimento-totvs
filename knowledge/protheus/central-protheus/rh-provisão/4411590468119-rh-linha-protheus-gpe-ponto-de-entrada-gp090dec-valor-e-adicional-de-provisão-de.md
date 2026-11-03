---
article_id: 4411590468119
category: RH - Provisão
content_hash: 617cd64ad71b05061023c016653a8bf7efb858df08a2031069bfcfdfbb22bd7f
fetched_at: '2026-06-28T22:43:56.947452+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP090DEC - Valor e Adicional de
  Provisão de 13º Salário
type: support-article
updated_at: '2025-10-06T17:56:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411590468119-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP090DEC-Valor-e-Adicional-de-Provis%C3%A3o-de-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25803037593111) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Utilização do ponto de entrada GP090DEC.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**

**Ponto de Entrada:** GP090DEC - Valor e Adicional de 13º Salário

**Descrição:** Ponto de Entrada para alterar o Valor e Adicionais das Povisões de 13º Salário.

**Programa Fonte:** GPEM080.PRW

**Sintaxe:**  

GP090DEC ()  
Parâmetros: Nenhum  
Retorno: NIL  
  
**Variáveis Disponíveis:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
| nV\_Valor | Numérico | Privado | Sim | Valor da provisão de 13º |
| nV\_Adic | Numérico | Privado | Sim | Valor dos adicionais de 13º |

**Exemplo:**

#Include 'Protheus.ch'

User Function GP090DEC()

nV\_Valor := u\_ValNew() //Valor da provisão de 13º

nV\_Adic := u\_ValAdic() //Valor dos adicionais de 13º

Return( Nil )

**Saiba Mais**  
[Ponto de Entrada GP090DEC](https://tdn.totvs.com/pages/viewpage.action?pageId=6079115)   
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
