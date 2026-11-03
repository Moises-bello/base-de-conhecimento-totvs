---
article_id: 21153713387287
category: RH – DIRF
content_hash: 5f57de54fe726d0f1ef754f170d4951091300fae17ff3e690246d24fdff84c8c
fetched_at: '2026-06-28T22:44:06.794516+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como alterar o código de retenção dos beneficiários
  para a DIRF
type: support-article
updated_at: '2025-08-05T17:00:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21153713387287-RH-Linha-Protheus-GPE-Como-alterar-o-c%C3%B3digo-de-reten%C3%A7%C3%A3o-dos-benefici%C3%A1rios-para-a-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21153653098903) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como alterar o código de retenção dos beneficiários para a DIRF?  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12**.****Solução**Para os funcionários e autônomos que receberam os pagamentos pelo GPE, ao gerar a DIRF o código de retenção é carregado conforme cadastro na rotina Funcionários/Contribuinte individual, conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21153653100183)  
  
Se o campo **Cod. Retenção** estiver preenchido, será carregada a mesma informação para a rotina Manutenção Arquivo, mas se tiver em branco, sempre será carregado o código de retenção 0561.  
  
Então, caso precise alterar, entre na rotina de **Funcionários** ou **Contribuinte Individual** pelo caminho **>Atualizações >Funcionários**, selecione o cadastro e altere o campo **Cod. Retenção** para o código correto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21153653101079)  
  
Na rotina Contribuinte Individual, caso o campo não esteja habilitado, clique [AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009855832) para saber como habilitar.

**Saiba Mais:**[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
