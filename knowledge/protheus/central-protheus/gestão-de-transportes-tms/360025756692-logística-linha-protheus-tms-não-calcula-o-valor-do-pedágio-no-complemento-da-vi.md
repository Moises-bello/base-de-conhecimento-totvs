---
article_id: 360025756692
category: Gestão de Transportes (TMS)
content_hash: 83194b71d6ae3977fe88d221d2373324200f25ca5c7934b28f4277aa5e7864cd
fetched_at: '2026-06-28T22:45:29.450349+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Não calcula o valor do pedágio no complemento
  da viagem quando integrado a operadora PAMCARD
type: support-article
updated_at: '2025-01-06T20:44:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025756692-Log%C3%ADstica-Linha-Protheus-TMS-N%C3%A3o-calcula-o-valor-do-ped%C3%A1gio-no-complemento-da-viagem-quando-integrado-a-operadora-PAMCARD
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29016352869527)** Tempo aproximado para leitura: **00:01:40 min****Dúvida**Como proceder para calcular o valor do pedágio no complemento da viagem quando integrado a operadora **PAMCARD**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para que o cálculo do valor do pedágio seja calculado na inclusão da viagem, no complemento da viagem, é necessário que o mesmo esteja configurado para ser realizado pela **Pamcard**.  
  
Para isso, acesse o **Configurador** **-** **SIGACFG**, **Ambiente/Cadastros/Parâmetros**. Pesquise e configure o parâmetro **MV\_PAMROTA** com **.T.** .  
  
Após, em **Gestão de Transportes - SIGATMS**, acesse **Atualizações/Operadoras de Frota/Operadoras de Frota - TMSAE60**.  
  
Altere o cadastro da Operadora **Pamcard**, opção **02**, e configure o conteúdo do campo **DEG\_CALPDG - Calc.Pedagio** com a opção **1 - Operadora**.  
  
Inclua uma viagem integrada com a Operadora de Frete: **Pamcard - 02** com uma rota existente na **Pamcard**.  
  
Ao confirmar o complemento da viagem será realizado o cálculo do pedágio e o campo Pedágio será atualizado automaticamente com o valor correto.  
  
A rotina irá realizar integração via *Web Service* com o Sistema **Pamcard®** e retornar o valor do pedágio. É importante observar que no momento de efetuar o cadastro do roteiro no Sistema **Pamcard®** é necessário informar no campo **Nome da Rota** o mesmo nome informado no campo **Rota - DA8\_COD** do **Protheus**. O Sistema **Pamcard®** efetua o cálculo através do roteiro previamente cadastrado e o número de eixos dos veículos informados.
