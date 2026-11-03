---
article_id: 360028598192
category: Rescisão
content_hash: fabee2c42eb19537ad552aaacaac5a561e4f49d72ec81ac1579d94f24c998eb1
fetched_at: '2026-06-28T22:46:55.322305+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Como diferenciar o saldo de salário?'
type: support-article
updated_at: '2024-10-23T22:23:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028598192-RH-RM-FOP-Rescis%C3%A3o-Como-diferenciar-o-saldo-de-sal%C3%A1rio
---

**Dúvida**Como realizar diferentes lançamentos de eventos de saldo de salário, para diferentes tipos de funcionários na rescisão?  
**Ambiente**RM - Folha de Pagamento - Todas as versões  
  
**Solução**Ao cadastrar uma rescisão para os funcionários pode acontecer de o evento de pagamento de saldo de salário ser diferente para tipos distintos de funcionários (salário mensal, horas normais, bolsa estágio, etc). Nestes casos, ao realizar uma rescisão e lançar o evento de saldo de salário o sistema lança por padrão o evento de código de cálculo 2, dias trabalhados,que é informado em **Configurações** | **Parametrizador** | **Rescisão** | **Cálculo** | **Evento de Saldo de Salário.**Para ajustar a parametrização para que o sistema diferencie tipos diferentes de funcionários e seu evento de saldo de salário, realize os passos abaixo:  
  
**01.** Crie uma fórmula para realizar a separação dos funcionários e tipos de recebimento. Veja abaixo exemplo de fórmula que poderá ser cadastrada:

```
Se TFUNC = 'T' /*Tipo de funcionário Estagiário*/  
Entao   
'9002' /*Evento para pagamento de estagiário*/  
senao  
'0002'/*Evento para pagamento funcionário mensalista */  
Senao  
Se CREC = 'H' /*Tipo de funcionário Horista*/  
Entao  
'0001'/* Evento para pagamento de funcionário Horista */  
Senao  
'0002'  
FimSe
```

**02.** Acesse **Configurações** | **Parametrizador** |**Rescisão** | **Cálculo** e desmarque o parâmetro **Evento de Saldo de Salário**e marque a opção **Fórmula p/ o evento de saldo de salário**.Agora informe a fórmula criada no passo anterior e salve o cadastro. Com isto o sistema passará a discriminar os tipos de eventos de saldo de salário para os demais tipos de funcionários e tipos de recebimento.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27287528196119)  
  
  
**Observação**  
Poderá adicionar os tipos de recebimentos ou funcionários que desejar no contexto da fórmula. A fórmula informada é apenas um **exemplo**, o suporte padrão não presta auxílio na criação ou manutenção de fórmulas. Para estes casos, verifique a possibilidade de contratar nossa equipe de consultoria tarifada.
