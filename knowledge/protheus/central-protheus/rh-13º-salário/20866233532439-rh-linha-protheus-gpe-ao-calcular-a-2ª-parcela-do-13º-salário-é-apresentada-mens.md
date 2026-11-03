---
article_id: 20866233532439
category: RH - 13º salário
content_hash: 6a21498e93c38067ee14ecf1e7a89bfaa00fc50c9961a821a6f6f82ad632457a
fetched_at: '2026-06-28T22:44:00.406754+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Ao Calcular a 2ª Parcela do 13º Salário é apresentada
  mensagem Cálculo Finalizado pela FinalCalc() ou Pela EndCalc() - S_VLDFUNC
type: support-article
updated_at: '2026-06-25T10:43:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20866233532439-RH-Linha-Protheus-GPE-Ao-Calcular-a-2%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-%C3%A9-apresentada-mensagem-C%C3%A1lculo-Finalizado-pela-FinalCalc-ou-Pela-EndCalc-S-VLDFUNC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20866233524119) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O que analisar quando ao Processar o Cálculo do Roteiro 132, é apresentada a mensagem "Cálculo Finalizado pela FinalCalc() ou Pela EndCalc() - S\_VLDFUNC" ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.33.  
  
**Solução**  
A Fórmula **S\_VLDFUNC** indica que o funcionário **já teve o cálculo do roteiro 132 processado no ano.**  
  
Consulte nos **acumulados do funcionário** (Tabela SRD), se há cálculos processados no ano em que está sendo processado o cálculo do 13º salário para o roteiro 132.  
Se de fato houver cálculo da 2ª parcela do 13º salário no ano para o funcionário em questão, **o cálculo do 13º será abortado.**  
  
Caso haja diferenças salariais, diferenças de adicionais e/ou médias de 13º salário, esta diferença **será calculada na Folha, como Complemento do 13º Salário.** Para isso, o Roteiro 132 deve estar cadastrado no período e **fechado** e o mnemônico P\_CCOMP13 deve estar habilitado.   
  
Consulte o material abaixo sobre como calcular o complemento de 13º Salário:  
[Cálculo de Complemento de 13º salário na Folha de Dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019750511-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Complemento-de-13%C2%BA-sal%C3%A1rio-na-Folha-de-Dezembro) 

**Saiba Mais**  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409828940055-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionados-ao-c%C3%A1lculo-da-2%C2%AA-parcela-do-13%C2%BA-Sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410720423959-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-do-complemento-de-13%C2%BA)
