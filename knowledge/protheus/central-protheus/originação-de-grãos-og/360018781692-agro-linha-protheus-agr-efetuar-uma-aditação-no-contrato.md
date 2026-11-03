---
article_id: 360018781692
category: Originação de Grãos (OG)
content_hash: 7138da47c83b7ba8b264b209255a99eb43fbdce93904618f51f196749c7804c8
fetched_at: '2026-06-28T22:45:39.362355+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Efetuar uma aditação no contrato
type: support-article
updated_at: '2025-04-07T20:33:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018781692-Agro-Linha-Protheus-AGR-Efetuar-uma-adita%C3%A7%C3%A3o-no-contrato
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20351456438295)*** Tempo aproximado para leitura: **00:00:40 min  
  
Ocorrência**Nas rotinas **OGA280** - **Contrato de Compra** e **OGA290** - **Contrato de Venda**ao efetuar uma **Aditação** para o contrato, assim que é informado o código do **Motivo de Alteração** é exibida a mensagem: **O Motivo só pode ser utilizado para alteração por Excedente de Carga**.   
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Essa mensagem é exibida quando na rotina **OGA140 -****Motivo de Alteração**, no cadastro utilizado como motivo para a **aditação**, foi informado **1 - Sim** no campo **Excedente**. Quando esse campo está assinalado como **Sim** significa que serão efetuadas **aditações** apenas quando houver **Excedente de Carga**.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acesse o registro do **Motivo de Alteração**;

**2.** No campo **Excedente** informe **2 - Não**;

**3.** Ou cadastre outro **Motivo de Alteração** para ser utilizado, deixando o campo **Excedente** como **2 - Não**.
