---
article_id: 360033644253
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 48ad8e6627e67de87c620ea69ccb1d47d3b3583d03d9d51201b3660a5fa1c3df
fetched_at: '2026-06-28T22:42:47.189790+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Corrigir casas decimais na tela Classificação da quantidade
  produzida acima do previsto
type: support-article
updated_at: '2021-09-21T15:53:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033644253-MP-SIGAPCP-Corrigir-casas-decimais-na-tela-Classifica%C3%A7%C3%A3o-da-quantidade-produzida-acima-do-previsto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:55 min**  
 **Dúvida**Como corrigir o número de casas decimais na tela para classificação da quantidade excedente?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Para correção das casas decimais execute os passos abaixo:  
1. Acesse o **SIGACFG - Configuração**  
 2. Selecione a tabela **SD3 - Movimentos internos**  
 3. Ajuste o tamanho dos campos **D3\_QTGANHO - Qtde ganho de produção** e **D3\_QTMAIOR - Qtde produzida a maior**  
4. Se a empresa realiza apontamentos de produção pelo **MATA680 - Produção Pcp Mod1** ou **MATA681 - Produção Pcp Mod2** ajuste também na tabela **SH6 - Movimentação da produção** os campos **H6\_QTGANHO - Qtde. ganho de produção** e **H6\_QTMAIOR - Qtde produzida a maior**
