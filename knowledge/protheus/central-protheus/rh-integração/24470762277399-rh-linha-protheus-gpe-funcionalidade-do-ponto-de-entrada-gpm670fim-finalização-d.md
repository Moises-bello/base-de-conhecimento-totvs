---
article_id: 24470762277399
category: RH - Integração
content_hash: a3063ec9337a89adfdadc22ba1dca0a5f1b5393a08033017a419b486b521ae4f
fetched_at: '2026-06-28T22:43:44.927971+00:00'
product: protheus
section_id: 360003115611
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do Ponto de Entrada GPM670FIM -
  Finalização da Integração de Títulos
type: support-article
updated_at: '2025-09-11T11:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24470762277399-RH-Linha-Protheus-GPE-Funcionalidade-do-Ponto-de-Entrada-GPM670FIM-Finaliza%C3%A7%C3%A3o-da-Integra%C3%A7%C3%A3o-de-T%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24470762266135) Tempo aproximado para leitura: **00:01:30** min **Dúvida**Funcionalidade do Ponto de Entrada GPM670FIM - Finalização da Integração de Títulos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

O ponto de entrada é executado na finalização do processamento da integração de títulos com o financeiro, para processos do usuário **após** a conclusão da integração.

**Exemplo de utilização**

`User Function``GPM670FIM``()`

`Local cMsg :=``"Integração de títulos finalizada! Acionado PE GPM670FIM."`

`MsgAlert(  cMsg  )`

`Return`

`Ponto de entrada sendo executado:  
  
![GIFgp670fim_.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24574707465367)`

**Saiba Mais:**<https://tdn.totvs.com/pages/viewpage.action?pageId=6079207>
