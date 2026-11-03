---
article_id: 360024687994
category: Gestão de Transportes (TMS)
content_hash: 83437846f98fdfbd6d921cd721f0a1cbd97366e7e04d40844d0b869d455688d0
fetched_at: '2026-06-28T22:45:29.518141+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada - TMSTAB
type: support-article
updated_at: '2022-06-20T14:44:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024687994-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TMSTAB
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura:**00:00:50 min **Dúvida**Para que serve e como implementar o Ponto de entrada **TMSTAB**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Ponto de Entrada disponibilizado para a pesquisa de tabela de frete, troca da região de origem e destino da tabela, e troca do código, tipo e sequencia da tabela de ajustes. Está localizado no fonte de funções genéricas **TMSXFUNA**.  
  
No Cálculo do frete, o Ponto de Entrada é chamado no momento da seleção da tabela de frete e retorna um *Array*com a região de inicio e fim, da tabela de frete, código da tabela, tipo da tabela e sequencia do ajuste.

**Variáveis**

**cTabFre** = Tabela de Frete  
**cTipTab** = Tipo de Tabela  
**cSeqTab** = Sequencia   
**cCdrOri** = Código de Região de Origem   
**cCdrDes** = Código de Região de Destino  
**cCodCli** = Código de Cliente  
**cLojCli** = Loja do Cliente  
**cCodNeg** = Código de Negociação do Cliente  
**cServic** = Serviço de Negociação do Cliente

**Exemplo**

*#Include 'Protheus.ch'*

*User Function TMSTAB()*

*Local aRetPE := {}*  
*Local \_cTabFre := PARAMIXB[1]*  
*Local \_cTipTab := PARAMIXB[2]*  
*Local \_cSeqTab := PARAMIXB[3]*  
*Local \_cCdrOri := PARAMIXB[4]*  
*Local \_cCdrDes := PARAMIXB[5]*  
*Local \_cCodCli := PARAMIXB[6]*  
*Local \_cLojCli := PARAMIXB[7]*  
*Local \_cCodNeg := PARAMIXB[8]*  
*Local \_cServic := PARAMIXB[9]*

*//Retorna a tabela de frete inicio e fim de trajeto (região de origem e destino da tabela)*  
*aAdd(aRetPE,'INICIO')*  
*aAdd(aRetPE,'FIM')*

*//Retorna o novo código da tabela, tipo e sequencia do ajuste.*  
*aAdd(aRetPE,"NTAB")*  
*aAdd(aRetPE,"NTIP")*  
*aAdd(aRetPE,"SQ")*

*Return aRetPE*
