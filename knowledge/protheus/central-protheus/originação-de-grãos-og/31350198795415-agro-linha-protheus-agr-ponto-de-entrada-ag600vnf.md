---
article_id: 31350198795415
category: Originação de Grãos (OG)
content_hash: 12a3629d5c8868548184f80d3c7ea05ea88f77597beb947833150ae6818ee975
fetched_at: '2026-06-28T22:45:42.660539+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada AG600VNF
type: support-article
updated_at: '2025-06-25T19:05:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31350198795415-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-AG600VNF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31350241500567) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Para que serve o **Ponto de Entrada** **AG600VNF**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O Ponto de entrada **AG600VNF**  foi criado para Informar série e número da nota fiscal de complemento dos romaneios de algoritmo. Ele utilizado com retorno esperado de array de 3 posições ( **Número da Nota** , **Série, oDlgVincNF** ).

**Ex:**

***Função de usuário AG600VNF()***  
***Local aRet := { "","" }***

**aRet[1] := "Número da nota"**

**aRet[2] := "Série da nota"**

**aRet[3] := "valor da variável oDlgVincNF"**

***Retorno (aRet)***
