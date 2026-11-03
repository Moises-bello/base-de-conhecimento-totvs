---
article_id: 360017798231
category: RH - Integração de Titulo
content_hash: e87d8d4ff11773e915692797040190273cea1abd6b4768c7486c23c365bf77c5
fetched_at: '2026-06-28T22:43:36.307627+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na Definição de títulos: A natureza não poderá
  ser usada nesta rotina'
type: support-article
updated_at: '2025-07-24T14:21:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017798231-RH-Linha-Protheus-GPE-Erro-na-Defini%C3%A7%C3%A3o-de-t%C3%ADtulos-A-natureza-n%C3%A3o-poder%C3%A1-ser-usada-nesta-rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33686270299415)Tempo aproximado para leitura:00:01:00 min

**Dúvida**Erro na Definição de Títulos: A natureza não poderá ser usada nesta rotina.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - 12.  
  
**Solução:**O campo Uso Natureza (**ED\_USO) tem validação**, devendo ser determinado o tipo de uso da natureza:  
  
**0=Livre; (todos os módulos)** **1=Contas a receber;   
2=Contas a****pagar;   
3=Mov. Bancario**

1) Acesse o módulo Financeiro:   
**-** Atualizações **->** Cadastros **->** Naturezas (selecionar a natureza e clicar em alterar)![kcs10102018.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360013096072)  
  
O campo Uso Natureza (**ED\_USO)** deverá ser preenchido com **0 - Livre** para ser utilizado na rotina **GPEM640** (módulo GPE) e também na rotina **FINA050** (módulo Financeiro).   
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
