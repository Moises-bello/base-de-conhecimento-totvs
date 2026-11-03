---
article_id: 360033606334
category: Gestão de Transportes (TMS)
content_hash: 92da1a207c897791019c3f0f8ce8cbb6ff4abab9617f14439d8e040147fe0678
fetched_at: '2026-06-28T22:45:33.289887+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 686 na transmissão do MDF-e
type: support-article
updated_at: '2022-06-15T11:22:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033606334-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-686-na-transmiss%C3%A3o-do-MDF-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Rejeição **686 -****Existe MDF-e não encerrado há mais de 30 dias para o emitente**, na transmissão do **MDF-e - Manifesto de Documento Fiscal eletrônico**.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**Esta rejeição é apresentada quando o **CNPJ - Cadastro Nacional da Pessoa Jurídica** emissor do **MDF-e** possuir algum **MDF-e** que não foi encerrado a mais de 30 dias.  
  
**Solução**Para corrigir a rejeição em questão, é necessário providenciar o encerramento do **MDF-e** que está pendente em sua base.  
  
Para identificar quais os **MDF-es** não encerrados, é necessário acessar a rotina **TMSA144D - Viagem modelo 2**, clicar em **Outras Ações\Manutenção\Manifesto\MDF-e**e na tela de parâmetros, informar o período desejado e na pergunta **Transmissão?** informar **Cons. Nao Enc.**, conforme demonstra imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044032533/mceclip0.png)

Ao clicar em **OK**, serão apresentadas todas as **viagens/manifestos** que não foram encerrados ainda.  
  
Com esta informação, deverá ser avaliada qual a **viagem** que está acima do período de 30 dias e providenciar o encerramento da mesma.  
  
Para conseguir transmitir o encerramento de um **manifesto**, é necessário que a viagem esteja com o *status* **Encerrada - legenda azul** ou **Chegada a filial - legenda laranja**.  
  
Ao fazer o apontamento de **chegada a filial** ou **encerramento** da **viagem**, é necessário transmitir o encerramento do **MDF-e.** Este processo é efetuado em **Outras Ações\Manutenção\Manifesto\MDF-e**, onde na tela de parâmetros do **MDF-e**, o campo **Transmissão?** deve estar configurado como **Encerramento**, conforme demonstra imagem abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043200314/mceclip2.png)​

Enquanto a **viagem** estiver com um dos *status* abaixo, não será permitido o **encerramento** do **MDF-e**, ou seja, o **manifesto** não será apresentado no monitor para encerramento:

* **Aberto - legenda verde**
* **Em trânsito - legenda amarela**
* **Fechada - legenda vermelha.** Esse *status* significa que o caminhão foi fechado.
