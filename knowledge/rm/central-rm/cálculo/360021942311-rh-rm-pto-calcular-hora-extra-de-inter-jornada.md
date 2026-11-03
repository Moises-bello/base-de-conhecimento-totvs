---
article_id: 360021942311
category: Cálculo
content_hash: 11f57ddcabf269094b1e4bb320ca15c3b58a22fb498b81c9effa54ea9f6a1085
fetched_at: '2026-06-28T22:46:29.233980+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular hora extra de inter-jornada
type: support-article
updated_at: '2026-01-27T20:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021942311-RH-RM-PTO-Calcular-hora-extra-de-inter-jornada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503142320023) **Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Como calcular hora extra de inter-jornada?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**  
Para calcular extras de inter-jornada para os funcionários, siga os passos abaixo:

**Atenção**: As extras de inter-jornada serão calculadas somente se o funcionário realizar jornadas que possuem um tempo menor que o mínimo estabelecido entre uma jornada e outra.

1. Acesse o espelho do funcionário, vá em **Processos** e selecione o menu **Parametrizar Funcionário**. Dentro do parametrizador, selecione a **Etapa 1- Horário** e informe o tempo entre as jornadas no campo **Tempo mínimo entre jornadas**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37974811983511)

   **Importante:** O parâmetro **: Considerar jornadas de descanso para interjornada:** Com este parâmetro desmarcado, é levado em consideração a Interjornada de 35h semanais, sendo 11h de interjornada ou o tempo mínimo informado entre jornadas, e 24h de descanso. Com o parâmetro marcado, o comportamento do sistema continua sendo de levar em consideração apenas as 11h entre jornadas de trabalho.
2. Para verificar as ocorrências geradas dos dias que o funcionário não respeitar o tempo mínimo entre as jornadas, acesse a **Janelas de Informações** e selecione a aba **Ocorrências**. A ocorrência para esta exceção é: **EIJ - Extra de Inter-Jornada**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37974811987607)
3. Caso deseje calcular o número de **EIJ** em um evento do Automação de Ponto, utilize o código de cálculo **0039 - Horas Extras Inter-jornada,.**

**Saiba Mais**  
Para mais informações, acesse o link das documentações a seguir:   
[Horário - Tempo mínimo entre jornadas](https://tdn.totvs.com/pages/releaseview.action?pageId=452719358)  
[RH - RM - PTO - Cadastrar eventos para cálculo do ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025095672-RH-RM-PTO-Cadastrar-eventos-para-c%C3%A1lculo-do-ponto)  
[RH - RM - PTO - Cadastrar eventos no sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043969074-RH-RM-PTO-Cadastrar-eventos-no-sindicato)
