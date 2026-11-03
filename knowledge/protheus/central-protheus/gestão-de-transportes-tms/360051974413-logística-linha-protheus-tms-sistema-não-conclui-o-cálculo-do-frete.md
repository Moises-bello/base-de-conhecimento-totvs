---
article_id: 360051974413
category: Gestão de Transportes (TMS)
content_hash: 396c4652b2012e7a01da248a66cd14368abc5a87b55d88ed74795453be3785ad
fetched_at: '2026-06-28T22:45:33.375647+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Sistema não conclui o Cálculo do Frete
type: support-article
updated_at: '2025-03-10T20:29:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051974413-Log%C3%ADstica-Linha-Protheus-TMS-Sistema-n%C3%A3o-conclui-o-C%C3%A1lculo-do-Frete
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26573548023575)** Tempo aproximado para leitura: **00:01:25 min**  
**Ocorrência**Ao efetuar o cálculo de frete do documento, Sistema não conclui o cálculo, deixando o Sistema com a mensagem **Cálculo de Frete - Calculando Frete...,** travado neste processo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573548028439)

**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Causa**Quando o Sistema não conclui o cálculo do frete, o problema pode estar relacionado à falha cadastral nas regiões utilizadas no seu cálculo de frete. A falha em questão é alguma região possuir ela mesma como sua região coligada - **Grupo Região - DUY\_GRPVEN = Cod. Reg. Col. - DUY\_CDRCOL** no cadastro de **Grupo de Região - TMSA115**.  
  
Ao cadastrar o **Grupo de Região** pelo Sistema não é possível efetuar o cadastro dessa maneira, mas em algumas implantações isso é alterado pelo **APSDU - Backup, Drop e Append de tabela**, o que não é recomendado.  
  
**Solução**Para solucionar essa ocorrência, acesse a rotina **Atualizações/Logística/Grupo Região - TMSA115**e busque pelos códigos das regiões do documento e todas as regiões superiores destas regiões.  
Nenhuma região pode possuir o campo **Grupo Região - DUY\_GRPVEN** igual ao campo **Cod. Reg. Col. - DUY\_CDRCOL.** Se seu cadastro estiver assim, limpe a região do campo **Cod. Reg. Col. - DUY\_CDRCOL** e refaça o cálculo do documento.
