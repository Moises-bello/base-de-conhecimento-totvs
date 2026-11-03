---
article_id: 360019040172
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 16da5a133f7904c392af7888806226e43dabb41f92b5d46cb585d1bd108d5632
fetched_at: '2026-06-28T22:37:23.919620+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Na Revisão de Aditivo,
  sistema não permite a digitação de mais de um dígito na Quantidade do Item
type: support-article
updated_at: '2025-12-01T21:45:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019040172-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Na-Revis%C3%A3o-de-Aditivo-sistema-n%C3%A3o-permite-a-digita%C3%A7%C3%A3o-de-mais-de-um-d%C3%ADgito-na-Quantidade-do-Item
---

**Ocorrência**  
Na Revisão de Aditivo, sistema não permite a digitação  de mais de um dígito na Quantidade do Item  
  
**Ambiente**  
  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Causa**  
No módulo Gestão de Contratos, ao tentar realizar uma revisão de aditivo de prazo, o campo quantidade (CN9\_QTDPAR) permite somente a digitação de uma posição, números de 1 a 9.

Esse incidente ocorre, pois a Picture do campo quantidade (CN9\_QTDPAR) está incorreta.  
  
**Solução**  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o módulo configurador (SIGACFG);  
2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;  
3. Em dicionário de dados localize a tabela CN9 e o campo CN9\_QTDPAR;  
4. Altere a picture do campo de @ 999 para @E 999 e salve a alteração.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
