---
article_id: 360042820233
category: Espelho
content_hash: 1af7733a9c459e1f6b09821a5376999f9d22ecf452f338d8a14d8db0924fb811
fetched_at: '2026-06-28T22:46:31.301750+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: RH - RM - PTO - Batidas desposicionadas (natureza errada) no processo de  importação
  de batidas
type: support-article
updated_at: '2025-12-11T16:52:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042820233-RH-RM-PTO-Batidas-desposicionadas-natureza-errada-no-processo-de-importa%C3%A7%C3%A3o-de-batidas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16034221383191) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Ao importar as batidas, elas ficam deslocadas (natureza errada), o que fazer para que não ocorra este desajuste?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
 **Solução**

Abaixo segue as recomendações mais usuais de parametrização, para que ao importar as batidas as naturezas fiquem corretas:

1. Acesse no modulo de Automação de Ponto menu**Configurações | Parametrizador**e ao abrir o assistente selecione o processo **08.01- Iniciais** e avance.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19945378187159)  
     
   Avance até de Importação, e marque os parâmetros "**Considera a alteração de natureza da batida no processo de acerto de batidas"** e **"Considera a alteração da data de referência no recálculo".**Após marcar os parâmetros avance as demais etapas até concluir.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19945341303575)
2. Acesse o menu **Configurações | Parametrizador | Funcionário** e selecione o funcionado desejado e edite. Avance até etapa **Importação de batidas,** marque a flag do parâmetro **'Considerar jornadas sem trabalho contínuas como única jornada para cálculo da natureza'** e informe a quantidade de horas desejadas no parâmetro **'Tempo de Acrésc. p/ limite da jornada de trabalho anterior/posterior à jornada sem trabalho, para cálculo da natureza',** recomendamos que o tempo preenchido seja de 06:00**.**  
   ​![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11459620803863)  
     
   **Observação**: O tempo informando irá variar de acordo com cada jornada. O cálculo para chegar ao número de horas, ​que deve ser informando no campo é o seguinte:

   Encontre a diferença da jornada anterior com a jornada posterior e dívida por 2.   
   Pegue resultado subtraia pela quantidade de horas de acréscimo informado campo 'Tempo de Acrésc. p/ limite da jornada de trabalho anterior/posterior à jornada sem trabalho, para cálculo da natureza' da etapa 14- Importação de batidas.  
    O resultado da subtração a jornada de descanso, validando assim qual intervalo de continuidade antes de depois para o descanso. Abaixo segue um exemplo do cálculo:  
     
   A quantidade de horas já definida no campo 'Tempo de Acrésc. p/ limite da jornada de trabalho anterior/posterior à jornada sem trabalho, para cálculo da natureza' e de 06:00.  
   Dia 25/05/2021 é uma jornada de compensado das 00:00 às 23:59   
   Dia 26/05/2021 e uma jornada de trabalho 23:00 as 03:00 e 04:20 as 08:30  
   Foram realizadas as seguintes batidas:  
   dia 25/05-> Ent1: 23:02 | Sai1: 03:11  
   dia 26/05-> Ent1: 04:32 | Ent2: 08:42  
   A batida de 08:42 deveria ser uma saída

   A diferença entre a jornada do dia  25/05/2021 e da posterior 26/05/2021 é de 23:00 (é considerado a tolerância caso exista).

   Como a divisão por 2 resulta em 11:30, e este valor será subtraído as 06:00 (número de horas definido no parametrizador).  Assim o resultado é 5:30, então batidas que forem executadas após as 05:30 não serão consideradas para a jornada de descanso e irá com a natureza de entrada.

   Neste cenário, se for alterado o tempo de acréscimo para 02:30, batidas executadas até as 09:00 serão consideradas para jornada de descanso, ficando com a natureza de saída.  
     
   Caso deseje alterar os parâmetros dos funcionários de forma global acesse o link abaixo:  
   [TOTVS RH - Linha RM - PTO - Como fazer a alteração global de parâmetros dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019945111-TOTVS-RH-Linha-RM-PTO-Como-fazer-a-altera%C3%A7%C3%A3o-global-de-par%C3%A2metros-dos-funcion%C3%A1rios)
3. No processo, ao realizar a importação das batidas, no box "Acerta natureza" recomendamos que se utilize a opção **Considerando o horário planejado** ou **Considerando a jornada,** abaixo segue a diferença entre as duas opções:  
    **Considerando o horário planejado:** A importação levará em consideração o horário planejado no dia, ou seja, o horário cadastrado para o funcionário. O sistema calculará a natureza pela proximidade da natureza do horário planejado. Se no horário estiver cadastrado como saída a primeira batida do dia, esta será importada como saída.  
     
   **Considerando a jornada:** O sistema calculará a natureza das batidas conforme a jornada(s) planejada(s) do funcionário. Ao invés de considerar a proximidade da natureza, é considerada a proximidade da jornada planejada. Tratando situações em que o funcionário tem mais de uma jornada planejada no dia, ou mesmo, funcionários que possuem jornada de um dia para o outro.

   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11440476234903)  
     
   4. Para o ajuste das batidas que estão atualmente com a natureza disposicionada, basta seguir o procedimento do link a seguir, após ter seguido os passos citados acima:  
   [RM - PTO - Realizar o acerto da natureza das batidas de forma global.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014576751-RM-PTO-Realizar-o-acerto-da-natureza-das-batidas-de-forma-global-?source=search)

**Saiba Mais:**

Para maiores informações sobre os parâmetros do funcionário da etapa 14 - importação de batidas, acesse a documentação: [Importar batidas](https://tdn.totvs.com/display/public/LRM/Importar+batidas)  
Para maiores informações sobre os demais parâmetros no processo de importar batidas acesse a opção abaixo: [RH - RM - PTO - Como importar as batidas para o Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000486068)  
[RH - RM - PTO - Alteração manual da natureza da batida não ser desfeito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11484220498455)  
[RH - RM - PTO - Batidas com jornada referência errada após realização de recálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11467075990807)
