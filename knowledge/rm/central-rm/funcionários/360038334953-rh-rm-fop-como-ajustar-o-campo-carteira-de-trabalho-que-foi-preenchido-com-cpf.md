---
article_id: 360038334953
category: Funcionários
content_hash: 2d1e25b0b57b26eafa16f41be0288f267bb22e6df915108b3430f1d4dcf8e872
fetched_at: '2026-06-28T22:47:03.429736+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Como ajustar o campo Carteira de Trabalho que foi preenchido
  com CPF '
type: support-article
updated_at: '2025-03-12T11:01:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038334953-RH-RM-FOP-Como-ajustar-o-campo-Carteira-de-Trabalho-que-foi-preenchido-com-CPF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:10 min**

**Dúvida**  
Para atender a CTPS Digital, a SEFIP exige que Carteira de Trabalho seja preenchido com os 7 primeiros dígitos do CPF para o número e 4 últimos dígitos para a série. Diante disso, como proceder quando existe funcionários que possuem o campo **Número da Carteira de Trabalho** preenchido com os 8 primeiros dígitos do CPF?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar a demanda, basta o Cliente limpar o campo do número e a serie da CTPS através do Cadastro do Funcionário, porém caso sejam muitos funcionários e seja inviável efetuar o procedimento manualmente, poderá seguir a outra alternativa conforme passos abaixo:  
  
1**.** Foi disponibilizado o Script para a limpeza dos campos da CTPS, caso tenha sido preenchido com o CPF do funcionário para atender a Carteira de Trabalho Digital.    
Para isso, acesse o Portal de Downloads e baixe o script:

Para SQL: [SCRIPT\_AJUSTA\_CTPSDIGITAL\_FUNC.ZIP](https://suporte.totvs.com/portal/p/10098/download#detail/829615)

Para Oracle: [SCRIPT\_AJUSTA\_CTPSDIGITAL\_FUNC-ORACLE.ZIP](https://suporte.totvs.com/portal/p/10098/download#detail/829616)  
  
2**.** Execute o Script conforme orienta o artigo abaixo:  
[RM - BD - Passos "RM Executor de Scripts"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007059632-RM-BD-Passos-RM-Executor-de-Scripts-)  
  
3**.** Após executar o Script, o campo **Carteira de Trabalho** ficará em branco no cadastro do funcionário e ao gerar a SEFIP ou CAGED automaticamente será considerado o CPF do funcionário.  
  
**Importante:** Para os funcionários que utilizam a Carteira de Trabalho Digital, deverá deixar em **branco**os campos **Número da Carteira de Trabalho** e **Série da Carteira de Trabalho** pois o sistema irá levar automaticamente para a SEFIP e o CAGED.  
  
**Saiba mais**Para mais informações sobre acesse:  
[TDN - Carteira de Trabalho Digital](https://tdn.totvs.com/display/public/LRM/CTPS+DIGITAL)
