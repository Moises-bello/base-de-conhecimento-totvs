---
article_id: 4420154816663
category: Lançamentos Globais
content_hash: 089aff8cccd8150d6894f1293bf6ee81351cd3b45d807a75ced7442e9b700a6e
fetched_at: '2026-06-28T22:46:35.218208+00:00'
product: rm
section_id: 6045394476951
source: central-rm
title: RH - RM - PTO - Agendar o processo de lançamento das batidas de refeição pelo
  horário planejado
type: support-article
updated_at: '2025-01-16T15:25:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420154816663-RH-RM-PTO-Agendar-o-processo-de-lan%C3%A7amento-das-batidas-de-refei%C3%A7%C3%A3o-pelo-hor%C3%A1rio-planejado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503361532567) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como agendar o processo de lançamento das batidas de refeição pelo horário planejado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**

Para agendar o processo de lançamento das batidas de refeição pelo horário planejado, siga os passos abaixo:   
1. Antes de realizar o agendamento, acesse o cadastro do horário do funcionário que será realizado o agendamento e verifique qual ocorrência está cadastrada no intervalo de refeição (Ausência planejada ou Intervalo de ausência do limite de refeição).

No exemplo abaixo, o horário possui Ausência Planejada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277450590487)

No exemplo abaixo, o horário possui intervalo de ausência do limite de refeição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277450593303)  
  
2. Acesse **Processos | Lançamento de Horários** e, ao abrir o assistente, clique em avançar. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277450594583)  
  
3.Faça a parametrização conforme o horário do funcionário:

Abaixo, selecionamos os campos Entrada e Saída referentes à Ausência Planejada e avançamos.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277424932887)  
  
No caso de intervalo de ausência do limite de refeição, iremos marcar as opções de entrada e saída na seção de ausência do limite de refeição:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277424937751)

Se houver o cadastro dos dois tipos de horário, pode ser agendado um único processo; basta marcar as opções de Entrada e Saída da Ausência Planejada e Intervalo de ausência do limite de refeição ao mesmo tempo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277450599703)

3.Após avançar será apresentada a tela de opções de lançamento. Faça a parametrização conforme a sua regra de negócio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277424955671)

4. Após definir a parametrização, clique no botão avançar e será apresentada a tela que trará as opções referentes ao agendamento e você poderá parametrizar com a recorrência desejada. No exemplo abaixo, o processo deverá ser executado pela primeira vez dia 16/01/2025 às 18:00 e após diariamente a cada intervalo de 12:00 hr:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29277450607127)

4. Após definir a parametrização de agendamento, clique em avançar e execute o processo.

5. Para conferir os processos agendados e suas recorrências, acesse o menu **Ambiente | Gerenciamento de Jobs.** Pela coluna **status** é possível conferir se houve erros na execução ou se foi realizado com sucesso.  
  
Observação: Para facilitar a visualização, faça o filtro pela classe do processo PtoProcLancamentoBatidaPeloPlanejado e será apresentado os processos para lançamento de batidas:

**![jobs.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29277450610711)  
  
Importante**Para que o lançamento das batidas pelo horário planejado possa ser executado, é necessário que o ambiente esteja instalado em N camadas. Caso o seu não seja e deseje configurá-lo, verifique os passos da documentação abaixo.  
[Framework - Linha RM - Frame - Configuração para simular 3 camadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006679772-RM-Frame-Configura%C3%A7%C3%A3o-para-simular-3-camadas)  
  
**Saiba Mais**  
Para maiores informações sobre o lançamento de batidas pelo horário planejado, verifique as informações na documentação abaixo.  
[Lançamento de horários](https://tdn.totvs.com/pages/viewpage.action?pageId=452719844)
