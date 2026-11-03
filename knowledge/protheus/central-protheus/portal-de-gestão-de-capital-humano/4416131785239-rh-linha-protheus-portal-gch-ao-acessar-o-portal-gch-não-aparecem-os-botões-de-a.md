---
article_id: 4416131785239
category: Portal de Gestão de Capital Humano
content_hash: 971a5a7918fee1b9ad1324161e0a3b18df82f18b4b14adb09b2ba47370233273
fetched_at: '2026-06-28T22:42:58.877973+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Ao acessar o Portal GCH, não aparecem os
  botões de aprovar e reprovar para o aprovador de solicitações de Justificativa de
  Pré abono
type: support-article
updated_at: '2023-11-27T21:20:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416131785239-RH-Linha-Protheus-PORTAL-GCH-Ao-acessar-o-Portal-GCH-n%C3%A3o-aparecem-os-bot%C3%B5es-de-aprovar-e-reprovar-para-o-aprovador-de-solicita%C3%A7%C3%B5es-de-Justificativa-de-Pr%C3%A9-abono
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19368577946647)Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Ao acessar o Portal GCH, não aparecem os botões de aprovar e reprovar para o aprovador de solicitações de Justificativa de Pré abono **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão Capital Humano - Todas as versões **Solução**Verificado que nas tabelas **RH3 e RH4**, os campos que recebiam os dados de filial como por exemplo: **RH3\_FILAPRO** estavam com tamanho igual a **8**, sendo o campo filial do SIGAMAT do cliente tamanho igual a **2**.  
  
Desta forma, o sistema gravava **'01'** para a tabela **RD0 e '01'** nas tabelas **RH3 e RH4,** gerando inconsistência para o aprovador nas solicitações.  
  
Para verificar os campos e seus tamanhos, acessar Módulo 99 - **SIGACFG > Base De Dados > Dicionários > Base de dados**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19368577957911)   
  
Clicar na lupa para achar a tabela RH3 por exemplo, depois clicar no botão da folha com lápis para editar.![](https://centraldeatendimento.totvs.com/hc/article_attachments/19368577966231)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19368554602647)  
  
Localizar o campo em questão, e clicar no botão da folha com lápis para editar, fazer o ajuste e Salvar.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19368577976599)  
  
Realizado ajuste do tamanho dos campos na RH3 e RH4, e o problema foi solucionado.  
  
**Saiba Mais**  
**[RH - Linha Protheus - PORTAL GCH - Como efetuar solicitação de abono e justificativa de pré abono](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416027072535)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)**
