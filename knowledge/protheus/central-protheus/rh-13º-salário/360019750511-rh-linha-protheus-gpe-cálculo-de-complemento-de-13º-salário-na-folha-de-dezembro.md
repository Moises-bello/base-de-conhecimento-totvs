---
article_id: 360019750511
category: RH - 13º salário
content_hash: 553da448c3b606cb9d32a2ffea77202f7c10ab90763f378bf05cb265c557998f
fetched_at: '2026-06-28T22:44:00.352687+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE -  Cálculo de Complemento de 13º salário na Folha
  de Dezembro
type: support-article
updated_at: '2026-06-24T19:31:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019750511-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Complemento-de-13%C2%BA-sal%C3%A1rio-na-Folha-de-Dezembro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18886257456535)**Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**Como funciona o cálculo de diferença do 13º salário na folha de dezembro?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução****Porque existe a diferença do 13º salário?**Pelo fato do 13º salário ser pago antes da folha do mês de dezembro ter sido fechada, pode ocorrer de serem lançados eventos com incidência para média de 13º salário, como uma hora extra, por exemplo. Neste caso, o valor da média de 13º salário pago ao funcionário no 13º, ficou menor que o correto, considerando esses valores lançados para a folha de Dezembro, assim, é necessário efetuar o pagamento de diferença de 13º salário para este funcionário.  
  
**Como habilitar o cálculo do complemento?**

Verifique os mnemônicos acessando Atualizações/ Definições de Cálculo/ Mnemônicos (GPEA300)  
  
**P\_CCOMP13 -** Calcula Compl 13 - "**S**" = Sim / "**N**" = Não  
**P\_INCCOMPL** - Se utiliza verba na folha para cálculo do complemento do 13º (preenchimento **.F. ou .T.**)  
  
Além disso, deve existir verba com **Id 0028** - Diferença 13º Salário para pagamento.  
  
**Como estes valores são calculados?**Na folha é realizado exatamente o mesmo cálculo que foi realizado na segunda parcela. É calculado o provento de Segunda Parcela e Média Segunda Parcela, com os novos valores de salário (caso tenha mudado) e o demonstrativo de médias com os valores do mês 12, depois de calculados esses valores, deduzimos os valores já pagos na folha de segunda parcela, referente ao mesmo item.  
  
Exemplo:

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015344811)

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015294972)

**Estes valores podem ficar negativos?**Não, pois no envio do S-1200, o RET não aceita valores negativos.   
[RH - Linha Protheus - GPE - Complemento 13º negativo impede a transmissão do S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062332213-RH-Linha-Protheus-GPE-Complemento-13%C2%BA-negativo-impede-a-transmiss%C3%A3o-do-S-1200?source=search)  
  
Caso não queira considerar o pagamento da diferença quando ocorrer, desative o parâmetro **MV\_DF13NEG / MV\_PROVNEG** – assim, quando for negativo, não será gerada a verba de diferença.  
Esses dois **parâmetros** devem ter preenchimento, **não podendo ficar em branco**. Caso fique em branco, o sistema não realiza o calculo do complemento.

**E os encargos, como são calculados?**Tanto o INSS quanto o IR devem ser calculados levando em consideração o valor total e abatendo o valor já descontado. Em resumo, é calculado novamente o valor de INSS com base nos novos valores, em seguida abatemos o que já foi descontado.

Exemplo:

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015345051)

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015345091)

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015345151)

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015295192)  
  
Essas configurações servem para todos os funcionários, não há como considerar o pagamento da diferença para um Funcionário e para outro não de forma padrão, apenas customizando o sistema, para isso, orientamos o agendamento de um analista Totvs in loco.

**Saber Mais:**

Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>  
[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Como cadastrar o ID 0028 Diferença 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11222463484439-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-0028-Diferen%C3%A7a-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar o ID 0348 Diferença Negativa 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11222354283927-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-0348-Diferen%C3%A7a-Negativa-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410720423959-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionados-ao-c%C3%A1lculo-do-complemento-de-13%C2%BA)  
[RH - Linha Protheus - GPE - Pensão de 13 salário negativa no complemento do 13º Salário, criação id 1679](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414523041943-RH-Linha-Protheus-GPE-Pens%C3%A3o-de-13-sal%C3%A1rio-negativa-no-complemento-do-13%C2%BA-Sal%C3%A1rio-cria%C3%A7%C3%A3o-id-1679?source=search)  
[RH - Linha Protheus - GPE - Como considerar verbas de valor que incorporam ao salário no roteiro FOL para o cálculo do complemento da 2ª parcela do 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018926292-RH-Linha-Protheus-GPE-Como-considerar-verbas-de-valor-que-incorporam-ao-sal%C3%A1rio-no-roteiro-FOL-para-o-c%C3%A1lculo-do-complemento-da-2%C2%AA-parcela-do-13%C2%BA?source=search)
