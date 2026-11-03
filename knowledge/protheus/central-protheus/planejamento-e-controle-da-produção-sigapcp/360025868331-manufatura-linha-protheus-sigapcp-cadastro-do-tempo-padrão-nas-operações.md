---
article_id: 360025868331
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8b3701bbcf1421e0ae4e60db5551856733fb6ce6353f49792b76f7cad28925a5
fetched_at: '2026-06-28T22:42:40.928440+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cadastro do Tempo Padrão nas operações
type: support-article
updated_at: '2025-07-21T14:40:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025868331-Manufatura-Linha-Protheus-SIGAPCP-Cadastro-do-Tempo-Padr%C3%A3o-nas-opera%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como efetuar o cadastro do **Tempo Padrão** nas operações?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O campo **Tempo Padrão** - **G2\_TEMPAD**da rotina **MATA632 - Roteiro de Operações**, depende do valor do parâmetro **MV\_TPHR - Define a unidade padrão para tempos utilizados pelo Sistema de PCP e Estoque**. Nele definimos qual tipo de unidade de tempo será utilizado: **C - Centesimal** ou **N - Normal**. Este parâmetro não deve ser alterado, pois é definido no momento da implantação do Sistema e a sua alteração pode gerar inconsistências nas rotinas que utilizam tempo.   
  
O tratamento do tempo para o campo em questão está relacionado ao parâmetro **MV\_TPHR**:

* Com o **MV\_TPHR** igual a **C**, que é padrão:  
  **G2\_TEMPAD** = 1,00 -> 1 hora ou 60 minutos  
  **G2\_TEMPAD** = 1,25 -> 1 hora e 15 minutos  
  **G2\_TEMPAD** = 1,50 -> 1 hora e 30 minutos  
  **G2\_TEMPAD** = 1,66 -> 1 hora e 40 minutos
* Com o **MV\_TPHR** igual a **N**:  
  **G2\_TEMPAD** = 1,00 -> 1 hora ou 60 minutos  
  **G2\_TEMPAD** = 1,15 -> 1 hora e 15 minutos  
  **G2\_TEMPAD** = 1,30 -> 1 hora e 30 minutos  
  **G2\_TEMPAD** = 1,40 -> 1 hora e 40 minutos

**Importante**Não é recomendável a alteração do campo **G2\_TEMPAD**, por isso deve-se ajustar o campo**Lote Padrão** **- G2\_LOTPAD** para que ao dividi-lo pelo **G2\_TEMPAD** obtenha-se a quantidade de **peça/hora** desejada.
