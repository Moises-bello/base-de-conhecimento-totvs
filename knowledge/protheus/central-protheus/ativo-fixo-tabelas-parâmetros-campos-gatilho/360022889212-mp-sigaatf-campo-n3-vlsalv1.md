---
article_id: 360022889212
category: Ativo Fixo - Tabelas, Parâmetros, Campos .Gatilho
content_hash: 37b97f548b0c9599665c70e9306be488c821aebcd9522e5716c7b386dda27fcf
fetched_at: '2026-06-28T22:41:50.329558+00:00'
product: protheus
section_id: 1500001536201
source: central-protheus
title: MP - SIGAATF - Campo N3_VLSALV1
type: support-article
updated_at: '2021-04-28T21:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022889212-MP-SIGAATF-Campo-N3-VLSALV1
---

**Dúvida**Qual o conceito sobre o campo **N3\_VLSALV1** (Valor Salvo) no Ativo Fixo??

**Ambiente**Protheus – Ativo Fixo - 12.1.17  
  
   
**Solução**O campo **N3\_VLSALV1** é utilizado para os bens cujo o tipo de depreciação é a **02-Redução de Saldos**:  
![](https://totvssuporte.zendesk.com/attachments/token/RNbtvinWwQ2PlXg1y512AL81K/?name=inline1777177774.png)​  
  
Características do cálculo:   
 É obrigatório possuir um valor de salvamento.   
 A alíquota é constante e aplicada ao valor residual ao invés do valor original do bem.    
 Caso o método seja mantido até o final da vida útil, o valor residual será igual ao valor de salvamento.    
  
A fórmula para determinar a alíquota é:    
 Taxa de depreciação = 1- (VS/VO)1/n    
Onde:    
**VS** = valor de salvamento e **VO** = valor original    
**n** = período em meses (se a depreciação é mensal ou em anos se é anual)

Verifique uma documentação técnica sobre os tipos de depreciação em: <http://tdn.totvs.com/pages/releaseview.action?pageId=6067612>
