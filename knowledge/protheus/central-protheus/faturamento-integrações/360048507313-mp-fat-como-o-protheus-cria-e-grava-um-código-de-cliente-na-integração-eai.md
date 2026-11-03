---
article_id: 360048507313
category: Faturamento - Integrações
content_hash: 4eb508c0184eb4c33168aae8b9d6822ce30bbb79bb7fc3ef07230d62692fc7c5
fetched_at: '2026-06-28T22:38:26.568139+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: MP - FAT - Como o Protheus cria e grava um Código de Cliente na Integração
  EAI
type: support-article
updated_at: '2021-04-28T15:15:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048507313-MP-FAT-Como-o-Protheus-cria-e-grava-um-C%C3%B3digo-de-Cliente-na-Integra%C3%A7%C3%A3o-EAI
---

**Dúvida**

Como o Protheus cria e grava um **Código de Cliente na Integração EAI**?  
   
 **Ambiente**

Microsiga Protheus -  todas as versões.  
  
**Solução**  
Segue abaixo, um exemplo da a forma que o Protheus monta o Código do Cliente na Integração de forma prática (padrão da integração EAI):  
  
***- EAI com Integração Logix***

O EAI recebe a informação do código como uma informação alfanumérica:   
  
Valor Externo = Valor do XML enviado pelo Logix (097211676000247)  
Valor Interno - Valor gravado na tabela **XXF** que será utilizado no Protheus de acordo com o tamanho do campo **A1\_COD** (09721167)  
  
No cadastro do Cliente - ***Mata030*** (que no exemplo abaixo o tamanho do código é 6), o sistema traz como código 097211 e os dois últimos dígitos grava a loja 67.  
  
![](https://totvssuporte.zendesk.com/attachments/token/U5gbIDOsOGPGiGhAQWGqbXfku/?name=inline-662826309.png)​
