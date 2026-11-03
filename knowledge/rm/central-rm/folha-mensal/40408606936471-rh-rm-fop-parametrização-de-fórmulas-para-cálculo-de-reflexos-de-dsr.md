---
article_id: 40408606936471
category: Folha Mensal
content_hash: 1df59f8dbe910647645130b0263de8cb1fc9ea4ded083b98656de163068e96f9
fetched_at: '2026-06-28T22:46:57.911696+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Parametrização de Fórmulas para Cálculo de Reflexos de DSR
type: support-article
updated_at: '2026-05-12T13:22:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40408606936471-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-de-F%C3%B3rmulas-para-C%C3%A1lculo-de-Reflexos-de-DSR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40408622048535) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida** 

Como parametrizar o sistema para realizar o cálculo dos reflexos de Descanso Semanal Remunerado (DSR) considerando horas extras, comissões e adicional noturno, utilizando o número de dias úteis e domingos/feriados do mês?

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento -Todas as versões

**Solução** 

Para realizar esse cálculo no módulo da Folha de Pagamento RM, é necessário o desenvolvimento de uma fórmula que utilize funções específicas do sistema para identificar os valores incidentes e os dias do calendário. O suporte padrão fornece as funções base, mas a montagem da estrutura lógica da fórmula deve ser realizada conforme a regra de negócio da empresa.

**Principais funções sugeridas:**

* **DSR (Mês, Ano, Período):** Retorna o valor total dos eventos que possuem a incidência de DSR marcada em seu cadastro.
* **NDIASMES (Mês, Ano):** Retorna o número total de dias do mês e ano informados, observando o calendário.
* **NDDSRPER (Data Início, Data Fim, Sábado):** Retorna a quantidade de domingos e feriados (e sábados, se o parâmetro for '1') dentro do período, verificando o calendário da seção e situações do funcionário (admissão, afastamentos, etc).

**Passos**

1. Acesse o cadastro de **Eventos** e certifique-se de que todos os eventos que compõem a base do reflexo (Horas Extras, Comissões, Adicional Noturno) estejam com o campo **DSR** marcado na aba **Incidências**. 

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40408606912663)
2. Crie uma nova **Fórmula** no sistema para o cálculo do reflexo.
3. Utilize a lógica de divisão do valor total incidente pelo número de dias úteis, multiplicando pelo número de domingos e feriados.
4. Exemplo de fórmula com a lógica utilizada para cálculo do DSR, considerando a base do DSR dividida pelos dias úteis e multiplicada pelos dias não úteis (domingos e feriados):

   (DSR(MES,ANO,PERIODO)) /

   (NDIASMES(MES,ANO)-NDDSRPER(MTDATA(01,MES,ANO),ULTDIAMES(MTDATA(01,MES,ANO)),'S')) \*

   (NDDSRPER(MTDATA(01,MES,ANO),ULTDIAMES(MTDATA(01,MES,ANO)),'S'))

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40408606913175)
5. Explicando a lógica da fórmula:

   Onde:

   `DSR(MES,ANO,PERIODO)`  
   Retorna a base dos eventos que possuem incidência de DSR configurada em seu cadastro.

   `(NDIASMES(MES,ANO) - NDDSRPER(MTDATA(01,MES,ANO),ULTDIAMES(MTDATA(01,MES,ANO)),'S'))`  
   Realiza o cálculo dos dias úteis do período.

   `NDDSRPER(MTDATA(01,MES,ANO),ULTDIAMES(MTDATA(01,MES,ANO)),'S')`  
   Retorna a quantidade de dias não úteis do período, considerando domingos e feriados.

   **Observação**:  
   1 - Essa estrutura representa apenas um exemplo de lógica para cálculo. Caso necessite de apoio para criação ou adequação da fórmula conforme a sua regra de negócio, sugerimos o acionamento da nossa equipe de consultoria para avaliação e suporte especializado. Consulte as condições de atendimento.

   2 - Lembrando que o cálculo do Descanso Semanal Remunerado (DSR) pode ser realizado por meio do módulo RM Automação de Ponto. Dessa forma, o sistema permite configurar e efetuar o cálculo do DSR de maneira nativa, sem a necessidade de customizações por fórmula no módulo RM Folha de Pagamento.
6. Salve a fórmula e associe-a ao evento de provento correspondente ao Reflexo de DSR. Em seguida faça o lançamento no envelope de pagamento de forma manual ou global via grupo de eventos.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40408606914199)![](https://centraldeatendimento.totvs.com/hc/article_attachments/40408606914967)

**Saiba Mais**

Para mais informações sobre formulas e função, acesse:

[RH - RM - FOP - Fórmulas e Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413339939351-RH-RM-FOP-F%C3%B3rmulas-e-Fun%C3%A7%C3%B5es)
