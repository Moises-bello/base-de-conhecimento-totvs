---
article_id: 360041123514
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4e359766e040d72f841a4abf4b5f7fced9fb4db5b2e2925aa08b91e3f4e95334
fetched_at: '2026-06-28T22:42:41.004642+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campo G2_SETUP
type: support-article
updated_at: '2021-05-27T11:13:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041123514-Manufatura-Linha-Protheus-SIGAPCP-Campo-G2-SETUP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min**  
**Dúvida**Para que serve o campo **G2\_SETUP** do **MATA632 - Roteiro de Operações**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O campo **G2\_SETUP** - **Setup (Hs)** refere-se ao tempo utilizado no processo de produção para preparar o recurso para produção e é utilizado no **MATA690** - **Carga Máquina**.  
Como exemplo de **Setup (Hs)**, podemos considerar a instalação de um molde em uma prensa.  
O tempo de **Setup (Hs)** é considerado como tempo de alocação, sendo utilizado para diferenciar o tempo decorrente da preparação do recurso do tempo, da execução efetiva da operação.  
  
**Exemplo:**  
Supondo que temos duas operações no mesmo recurso para o mesmo produto sendo:  
• 01 - **Setup (Hs)**: 0,25 / **Tempo Padrão**: 1,0 / **Lote padrão**: 10  
• 02 - **Setup (Hs)** 0,25 / **Tempo Padrão**: 0,5 / **Lote padrão**: 10  
  
Ao alocar as operações, o **Carga Máquina** apresentará no gráfico as informações:  
• **Operação** 01: **Preparação**: 15 minutos / **Execução**: 1 hora  
• **Operação** 02: **Preparação**: 15 minutos / **Execução**: 30 minutos  
  
O exemplo passado aqui utiliza o **MV\_PRECISA - Fator de divisão referente ao período mínimo dos Calendários do PCP.**  igual a **4**, ou seja, uma precisão de 15 minutos e **MV\_TPHR - Define a unidade padrão para tempos utilizados pelo Sistema de PCP e ESTOQUE.** igual a **C**.
