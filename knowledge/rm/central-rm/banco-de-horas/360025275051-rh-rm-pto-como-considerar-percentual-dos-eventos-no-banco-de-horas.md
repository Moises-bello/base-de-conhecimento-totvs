---
article_id: 360025275051
category: Banco de Horas
content_hash: eb1c8b9c51983a99d48285b7d7b40f6623a5b99a01b6d2893d11257d57a640e8
fetched_at: '2026-06-28T22:46:27.793013+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Como considerar percentual dos eventos no banco de horas
type: support-article
updated_at: '2024-06-12T18:51:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025275051-RH-RM-PTO-Como-considerar-percentual-dos-eventos-no-banco-de-horas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503283944343) Tempo aproximado para leitura: 00:03:30 min**

**Dúvida**  
Com considerar percentual dos eventos, no banco de horas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS -Automação de Ponto – A partir da versão 11.80  
  
**Solução**

Quando você utiliza o banco de horas, o saldo previsto exibido na visão do espelho de ponto pode ser o valor efetivamente realizado ou já acrescido com o percentual do evento aplicado. Além disso, você também pode realizar o processo de compensação e/ou lançamento do banco de horas considerando esse percentual.  A seguir segue as opções de parametrização:  
  
**Parametrizador do sindicato, etapa Cálculo:**

1. Acesse no módulo de **Automação de Ponto** o menu **Configurações | Parametrizador.** Ao abrir o assistente, clique em avançar e selecione o processo **Sindicato**. Em seguida, edite o sindicato desejado e clique em avançar:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383926494871)![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383926509207)  
     
   2.  No parametrizador do sindicato na etapa **Cálculo** há os parâmetros **"Considera percentual para o movimento"** e **"Considera percentual para o banco de horas"** que irá validar o valor do percentual para aplicar as extras no banco de horas:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383951856279)  
     
   No cadastro do evento de banco de horas extras, o percentual está para aplicar 1.5% (50%), hora extra realizada:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21384364132631)  
     
   Assim vamos ter os seguintes comportamentos:   
   Ao **marcar** a flag do parâmetro **"Considera percentual para o movimento",** irá permitir que o direcionamento das horas do banco de horas para o movimento considere o percentual de incidência do evento. Por exemplo ao trocar a atitude da ocorrência de compensar para pagar/descontar, o valor do movimento será enviado com o percentual acrescido.   

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383951863191)

   Ao **marcar** o parâmetro **"Considera percentual para o banco de horas",** as horas extras enviadas para o banco de horas serão acrescidas de acordo com o percentual de incidência do evento. Isso significa que você poderá visualizar o saldo previsto já com o percentual aplicado.  
   -Na visão do espelho, guia **totais do dia**, vemos que as colunas Extra Executado e Extra autoiz., está com 02:00 horas e o a coluna Extra Exec. já aparece com o valor de 03:00 acrescido de percentual:   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383951867927)  
     
   -Visão do espelho guia banco de horas:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383951881623)  
     
   -Visão do espelho guia banco de Saldo de banco de horas analítico:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383926556311)  
     
   -Visão do espelho guia banco de Saldo de banco de horas Sintético:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383926565399)  
     
   - No processo de compensação e/ou lançamento do banco de horas, o valor da extra enviada ao movimento também será acrescido do percentual.  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21383951908631)  
     
   **Informações importantes sobre esta forma de percentual:**  
   -Você pode marcar os dois parâmetros juntos, o que facilita o processo.  
   - No cadastro do evento, **não é necessário ter a flag "considera o percentual deste evento na compensação das horas"** marcada.  
   - Ao aplicar o percentual, apenas o evento informando no campo **"Evento relacionado ao RM labore"** será considerado.  
   - Durante a rotina de compensação e/ou lançamento do banco de horas na etapa de compensação, a flag **"Considera o percentual de incidência para a compensação das horas"** pode ficar desmarcada e, mesmo assim, o percentual será aplicado.

**Parametrizador do sindicato, etapa Banco de Horas:**

1. Na etapa de **Banco de Horas**, iremos ter a guia **Percentual de Incidência**. Segue abaixo a finalidade de cada campo:   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21384752281623)  
     
   As opções de parâmetros disponíveis nesta etapa, oferecem uma variedade de opções para você considerar o percentual. Abaixo, você encontrará detalhes sobre cada parâmetro e exemplo do comportamento.  
   Vamos nos basear com os seguintes horários:  
   Horário planejado  
   08:00 12:00 14:00 18:00 Jornada esperada 08:00  
   Horário executado  
   08:00 12:00 14:00 20:00 Jornada trabalhada 10:00, 08 horas trabalhadas e 02 horas de extra  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403563152279)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403573625623)  
     
   **-Considera percentual para o limite do banco de horas**: Ao habilitar este parâmetro, o sistema calculará um percentual de incidência sobre o limite de horas da jornada estipulado na parametrização.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403563200663)  
     
   Exemplo:   
   No cadastro do evento de horas extras está para aplicar 1.5% (50%), hora extra realizada:   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403573649687)  
     
    Limite definido:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403563223959)  
     
   Na extra realizada no intervalo das 18:00 às 20:00 será aplicada ao limite:  
   O percentual será aplicado a ocorrência para definição do limite: 02:00:00 \* 1,5 = 03:00:00  
   Desse total 01:20 terá sua faixa alterada para 2a Faixa de Extra  
   E o saldo restante de 00:40 irá permanecer na 1a Faixa de extra  
     
   Guia Ocorrências  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403563234199)  
     
   Guia Banco de horas:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403573702935)  
     
   **-Considera percentual do evento do banco de horas ao exibir o saldo do banco de horas:** Este parâmetro leva em consideração o percentual do evento do campo **"código do evento lançado no movimento do cadastro de eventos do banco de horas"** para exibir o saldo nas guias **saldo de banco sintético** e **analítico** na visão do espelho de ponto do funcionário.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403573717527)  
     
   Exemplo:   
   No cadastro do evento de horas, no campo **"código do evento lançado no movimento do cadastro de eventos do banco de horas"** está associado **o evento 0500 - BANCO DE HORAS DOBRADO** dessa forma vai para aplicar o percentual de 2.0% (100%), nas horas extras realizadas:   
     
   Guia Ocorrências  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403573734679)  
   E nas guias saldo de banco de horas sintético e analítico e possível consulta o valor aplicado do percentual.  
   Guia saldo de banco de horas analítico: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403563315479)**Guia saldo de banco de horas sintético: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/21403573751703)  
     
   -Considera percentual do evento do banco de horas na compensação do banco de horas:** Este parâmetro leva em consideração o percentual do campo **"código do evento lançado no movimento do cadastro de eventos do banco de horas"** durante o processo de compensação. Caso ele esteja desmarcado, na rotina de compensação e/ou lançamento do banco de horas será considerado o evento do campo **"código do evento relacionado ao RM Labore".**Além de atualizar o saldo das guias banco de horas sintético e analítico na visão do espelho de ponto, ao realizar o processo de compensação e/ou lançamento do banco de horas será considerado o evento do campo deste campo "**código do evento lançado no movimento do cadastro de eventos do banco de horas"**, ao lançar as horas para movimento:   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21406618856599)  
     
   **-Considera percentual ao exibir o saldo do banco de horas:** Este parâmetro tem como objetivo considerar o percentual de incidência das horas extras, para exibir nas guias saldo de banco sintético e analítico na visão do espelho de ponto do funcionário.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21406618890263)  
     
   Ele considera o campo **"código do evento relacionado ao RM Labore",** no cadastro do evento para aplicar o percentual.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21407003876119)  
     
   Guia saldo de banco de horas analítico:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21406654779415)  
     
   Guia de saldo de banco de horas sintético:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21406618915607)  
   Observações:  
   Para que o campo fique habilitado o campo **"Considera percentual para o banco de horas"** da etapa cálculo deve estar **des****marcado**.  
     
   **Informações importantes sobre esta forma de percentual:**  
   - Você pode marcar os um ou mais parâmetros juntos, o que facilita o processo.  
   - No cadastro do evento, é **necessário** ter a f**lag "considera o percentual deste evento na compensação das horas" marcada**.  
   - Durante a **rotina de compensação e/ou lançamento do banco de horas** na etapa de compensação, a flag **"Considera o percentual de incidência para a compensação das horas" deve estar marcada.**  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21409554324375)

Abaixo segue um exemplo de uma parametrização bastante utilizada, que se propõe a compensar as horas com percentual e lançar para o movimento sem o percentual da compensação. Primeiro valide se de fato o evento cadastrado no Automação de Ponto referente ao banco de horas, ira considera o percentual, para validar siga os passos abaixo:

1. Desmarque a opção "**Considera percentual para o banco de horas"** na etapa cálculo de forma que o mesmo não seja aplicado antes da compensação.  
   ![2019-03-13_12_14_49-Assistente_de_Implanta__o_de_Processos__Processo__08.02_-_Parametrizando_Sindica.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023743531)
2. Marque a opção "**Considera percentual na compensação de horas** " nos eventos de hora extra, para que o sistema aplique o percentual somente no momento da compensação de banco de horas.​  
   ![2019-03-13_12_14_36-.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023705752)
3. Realize o processo de Compensação e/ou Lançamento com a opção "**Considera percentual de incidência para a compensação das horas"** marcada, de forma que o sistema compense as horas com o percentual de incidência dos eventos e remova o percentual após a compensação.  
   ![2019-03-13_12_15_05-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023743551)
4. Caso deseje visualizar o percentual na aba **Saldo de banco de horas sintético**, deverá marcar a opção considera **percentual ao exibir o saldo do banco de horas** na aba **Percentual de Incidência**, no **Parametrizador do Sindicato | Banco de horas**.   
   ![2019-03-13_12_14_17-Assistente_de_Implanta__o_de_Processos__Processo__08.02_-_Parametrizando_Sindica.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360023743511)  
     
   Com as parametrizações citadas acima, o sistema aplicará o percentual na compensação e irá removê-lo ao final. Um exemplo de compensação e lançamento:  
   Extras 100%: 3:00  
   Atrasos: 4:00  
     
   Compensação:  
   Aplicando percentual: 3:00 x 2,00 (percentual de incidência) = 6:00  
   Realizando a compensação: 6:00 - 4:00 = 2:00  
   Removendo percentual: 1 hora extra de saldo  
   Enviar ao movimento: 1 hora extra

**Saiba Mais**  
Para maiores informações acesse:  
[Limite de extras - etapa cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719323)  
[Limite de extras - etapa banco de horas](https://tdn.totvs.com/display/LRM/DT_Calculo_Hora_Extra_Noturna_Parte1)  
[RH - RM - PTO - Cadastrar eventos no Sindicato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043969074)  
[RH - RM - PTO - Como configurar o banco de Horas diário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045154114)   
[RH - RM - PTO - Como configurar o banco de horas por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017559512)
