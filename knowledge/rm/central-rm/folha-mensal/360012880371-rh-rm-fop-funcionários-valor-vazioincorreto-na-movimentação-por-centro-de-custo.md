---
article_id: 360012880371
category: Folha Mensal
content_hash: e3bb27ef4d0da437e7a07cd0bb44b01a975443077df3824b17c0f014b0a670f8
fetched_at: '2026-06-28T22:47:00.297743+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Funcionários: Valor vazio/incorreto na movimentação por centro
  de custo'
type: support-article
updated_at: '2024-06-19T16:13:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012880371-RH-RM-FOP-Funcion%C3%A1rios-Valor-vazio-incorreto-na-movimenta%C3%A7%C3%A3o-por-centro-de-custo
---

**Ocorrência**No módulo **Folha de Pagamento**, ao gerar Lançamento Financeiro, é apresentada a seguinte mensagem de aviso:  
  
[Aviso] Funcionário XXXX não possui valor ou está com valor incorreto na movimentação por centro de custo na competência X/XXXX para o cálculo do lançamento [IRRFPagar].  
Lançamento "IRRFPagar" não será efetuado.  
  
**Ambiente**RM - Totvs Folha de Pagamento - Todas versões  
  
**Causa**Esse incidente ocorre por dois motivos:  
**01.** No cadastro do funcionário em **Rateio Fixo** não foi informado um **Centro de Custo**;  
**02.** Existe **Centro de Custo** informado dentro do cadastro do funcionário mas foi inserido após o lançamento de folha, sendo assim o sistema não considera o **Centro de Custo**.   
  
**Solução**Para solucionar essa ocorrência, realize os passos a seguir:  
  
**01.** Acesse **Administração de Pessoal | Funcionários** e edite o funcionário com o aviso. Depois vá em **Anexos | Folha de Pagamento | Rateio Fixo** e verifique se existe **Centro de Custo** informado. Caso negativo, será necessário informar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009105511)  
  
**02.** Após verificar e ajustar a aba **Rateio Fixo** no cadastro do funcionário acesse **Administração de Pessoal | Funcionários** e selecione o funcionário. Clique no **Envelope de Pagamento** e depois em **Recalcular**;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008883351)  
  
**03.** Após recalcular o envelope o sistema irá atualizar os valores do funcionário e o envelope por Centro de Custo.   
**04.** Para validar os valores, acesse **Centro de Custo**, no envelope do funcionário.
