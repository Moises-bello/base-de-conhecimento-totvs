---
article_id: 360028641911
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 299500403c4f5786ef663279754c65fe71e2104e711e449bd059b76b2fb95d8a
fetched_at: '2026-06-28T22:42:42.033699+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como o programa trabalha com o percentual
  de perda de material indicado na estrutura do produto
type: support-article
updated_at: '2024-02-29T18:08:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028641911-Manufatura-Linha-Protheus-SIGAPCP-Como-o-programa-trabalha-com-o-percentual-de-perda-de-material-indicado-na-estrutura-do-produto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21305163869847)**Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Caso seja indicado no **PCPA200 - Estrutura** que o material sofre perda, campo **G1\_PERDA - Índice Perda**, como o programa utiliza esta informação para calcular a quantidade a ser empenhada do produto?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O programa faz o cálculo descrito abaixo, caso seja indicado perda na **estrutura** do produto:  
**Quantidade empenhada = ( Quantidade/(100 - perda))\*100  
  
**Exemplo:****Uma **OP - Ordem de Produção** de 10 unidades, com quantidade na estrutura de 1,5 do material **MP01**, com o campo **G1\_PERDA** igual a 5.  
  
Então o cálculo será:  
**Quantidade empenhada = ( Quantidade/(100 - perda))\*100**  
**Quantidade empenhada = ( 15/(100 - 5))\*100**  
**Quantidade empenhada = 15,7895**Nesse exemplo a quantidade empenhada para o **MP01**, será de **15,7895.  
  
Importante**A **quantidade** utilizada no cálculo, é a quantidade necessária para atender a demanda para aquela **OP**.
