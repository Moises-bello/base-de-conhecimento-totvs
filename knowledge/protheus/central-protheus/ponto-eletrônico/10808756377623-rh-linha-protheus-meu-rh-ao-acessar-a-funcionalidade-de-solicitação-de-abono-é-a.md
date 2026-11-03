---
article_id: 10808756377623
category: PONTO ELETRÔNICO
content_hash: dcb34455815d15f03df46e112b3ac19f61b4bdda456b1d3ce1f3df6417f273bf
fetched_at: '2026-06-28T22:44:36.630456+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Ao acessar a funcionalidade de Solicitação de
  Abono é apresentada mensagem de "object Object"
type: support-article
updated_at: '2026-06-19T15:37:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10808756377623-RH-Linha-Protheus-MEU-RH-Ao-acessar-a-funcionalidade-de-Solicita%C3%A7%C3%A3o-de-Abono-%C3%A9-apresentada-mensagem-de-object-Object
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27605994305175) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Por que ao **acessar** a funcionalidade de **Solicitação de Abono** é apresentada mensagem **"*****object Object"***e **não permite incluir Abonos**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**  
Como o erro é causado devido a divergência de fontes e Arquivos do Portal utilizados, para correção deste cenário é necessário:  
**1. Baixar** e **aplicar** o pacote de **Expedição Contínua do RH** mais recente no Repositório do serviço **REST**:   
[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
  
**2. Baixar**e **atualizar** os **Arquivos do Portal** para a última versão mais recente:  
[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
  
3 - Verificar no módulo **16 - SIGAPON, rotina Atualizações -> Cadastro de Ponto -> Motivo de Abono**, se possuem os motivos corretamente cadastrados, e com os campos abaixo como SIM.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27606014342807)  
  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27605994312983)  
  
**Saiba Mais**  
[**RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
