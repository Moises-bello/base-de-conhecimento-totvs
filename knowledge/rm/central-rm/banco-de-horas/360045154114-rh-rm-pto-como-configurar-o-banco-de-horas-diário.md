---
article_id: 360045154114
category: Banco de Horas
content_hash: 84282e4f992ed53e4687486c2ba401eee3f3f587b4d87d3d9dda303ebcdebbab
fetched_at: '2026-06-28T22:46:27.778457+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: 'RH - RM - PTO - Como configurar o banco de Horas diário '
type: support-article
updated_at: '2025-04-09T18:52:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045154114-RH-RM-PTO-Como-configurar-o-banco-de-Horas-di%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16530032562839) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como configurar o banco de horas diário, e o banco de horas diário por ocorrência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – 12.1.5 e superiores  
  
**Solução**

Para configurar o uso do banco de horas diário, vou te mostrar os passos e os parâmetros a seguir:

1. Acesse no módulo de **Automação de Ponto** o menu **Configurações | Parametrizador**. Ao abrir o assistente, clique em avançar e selecione o processo **Sindicato**. Em seguida, edite o sindicato desejado:   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21137772393879)![](https://centraldeatendimento.totvs.com/hc/article_attachments/21137804235543)
2. No parametrizar sindicato, avance até a etapa de **Banco de Horas**. Lá, selecione a opção "**Utiliza banco de horas**" e em "Tipo de banco de horas", escolha a opção "**Diário**":   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21137772449431)
3. Na guia **Parâmetros Gerais,** na seção **"Banco de Horas"**, oferecemos a opção de utilizar o tipo de **Banco Diário por Ocorrência**. Essa funcionalidade permite que você modifique a atitude das ocorrências, como atrasos, faltas ou horas extras, para pagamento ou desconto, sem a necessidade de passar pelo processo de compensação do banco de horas. Para configurar o uso do banco por ocorrência, marque o parâmetro **"utiliza banco de horas por ocorrência"**. **Recomendamos a utilização do Banco Diário por Ocorrência pelas possibilidades que proporciona ao tratar as ocorrências e o banco de horas.**  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21168519231255)  
     
   **Importante**: **A partir dos passos abaixo, realize a parametrização conforme sua regra de negócio.**
4. Ainda na seção de banco de horas diário, o campo **Início Compensação** possui a finalidade de determinar se o processo de compensação terá início a partir da primeira faixa de extras ou da última faixa de extras, caso utilize a faixa de extras. É importante ressaltar que essas faixas são cadastradas na etapa **"Faixa de extras"** no parametrizado do sindicato.  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21185615866519)
5. Na seção **"Limite de Extras"**, você tem a opção de definir um **valor limite** para o envio das atitudes de ocorrência (compensar ou pagar) ou alterar entre as faixas existentes. Dessa forma, você pode escolher a quantidade das horas extras realizadas que será acumulada como banco de horas e o que ultrapassar o limite será enviada para o movimento. Além disso, você pode configurar esse limite para ser aplicado diariamente, semanalmente ou no período. Informações sobre os campos da seção **"Limite de extras"**:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21137772488983)  
    **Limite exec. por dia**: Permite estabelecer um limite diário para a jornada de trabalho.  
   **Limite exec. por semana**: Permite estabelecer um limite semanal para a jornada de trabalho.  
   **Limite exec. por período:** Permite estabelecer um limite por período para a jornada de trabalho.  
   **Limite de extra dia**: Considera o valor da hora extra realizada como limite.  
   **Limite de extra executado dia**: Considera o valor das horas trabalhadas dentro da jornada esperada somadas à quantidade de horas extras realizadas no dia, como limite.  
   **Limite de extra semana:** Considera o valor total das horas extras realizadas durante a semana como limite.  
   **Limite de extra executado semana:** Considera o valor das horas trabalhadas dentro da jornada esperada, somadas à quantidade de horas extras realizadas durante a semana, como limite.  
   **Limite de extra período:** Considera o valor total das horas extras realizadas durante o período como limite.  
   **Limite de extra executado período:** Considera o valor das horas trabalhadas dentro da jornada esperada, somadas à quantidade de horas extras realizadas durante o período, como limite.  
   **Início def. limite:** Opção de escolha se o limite será aplicado às horas extras realizadas no início ou no final do dia, no final da semana ou no final do período.  
   **Altera atitude do evento:** Após o valor das extras ultrapassar o limite informado, irá acontecer a troca da atitude da ocorrência para pagar o valor para o funcionário.   
   **Altera faixa**: Caso trabalhe com faixas de pagamento, poderá ser indicada a faixa para a qual a hora extra será alterada após ultrapassar o limite.
6. Na etapa de banco de horas, ao rolar a barra lateral, você encontrará a seção chamada **Atitudes**. Nessa seção, você terá a opção de definir quais ocorrências serão enviadas para compensar ou pagar/descontar. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21168533219991)
7. Nesta seção, há também o parâmetro **"Considera Atitude do Evento"** que tem como objetivo levar em consideração a atitude que está registrada no evento. Você pode encontrar essa informação na Etapa de Eventos parametrizado do sindicato, na aba Informações Adicionais, na seção "Atitude a ser Considerada no Dia/Evento", conforme o passo 9, deste documento.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21187865651351)
8. Ainda na etapa de Banco de Horas, iremos ter a guia **Percentual de Incidência**. Segue abaixo a finalidade de cada campo:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21168533250071)  
     
   **Considera percentual para o limite do banco de horas**: Ao habilitar este parâmetro, o sistema calculará um percentual de incidência sobre o limite de horas da jornada estipulado na parametrização.  
   **Considera percentual do evento do banco de horas ao exibir o saldo do banco de horas**: Este parâmetro leva em consideração o percentual do campo "código do evento lançado no movimento do cadastro de eventos do banco de horas" para exibir nas guias saldo de banco sintético e analítico na visão do espelho de ponto do funcionário.   
   **Considera percentual do evento do banco de horas na compensação do banco de horas**: Este parâmetro leva em consideração o percentual do campo "código do evento lançado no movimento do cadastro de eventos do banco de horas" durante o processo de compensação.  
   **Considera percentual ao exibir o saldo do banco de horas**: Este parâmetro tem como objetivo considerar o percentual de incidência das horas extras, para exibir nas guias saldo de banco sintético e analítico na visão do espelho de ponto do funcionário. Importante: Para que os parâmetros funcionem corretamente, é necessário que os eventos de horas extras tenham o parâmetro "Considera percentual de incidência" marcado.
9. Ainda no parametrizador do sindicato, acesse a etapa **Eventos** e configure os eventos do Automação de Ponto e os relacione ao da Folha Pagamento que irá armazenar as ocorrências e definir os percentuais das horas armazenadas em banco. Abaixo seguem as informações dos campos sobre a guia Identificação:     
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21170291813399)  
    **Código do evento calculado no Totvs Automação de Ponto:** Informe o evento utilizado para o cálculo do movimento no Totvs Automação de Ponto.  
   **Código do evento relacionado RM Labore:** Este evento será associado ao evento no Totvs automação de ponto e utilizado para lançamentos na folha de pagamento.  
   **Código do evento do banco de horas lançado no****movimento:** Informe o evento para cálculo de horas no banco de horas e que posteriormente, poderá ser lançado no movimento (utilizado quando deseja diferenciar o evento do banco de horas do evento a pago/descontando diretamente no movimento do funcionário).  
   **Cadastrar este evento nos eventos a serem lançados o Labore:** Durante a inclusão de um evento, o sistema habilita a opção de incluí-lo também na pasta de "Eventos a serem lançados no Labore".  
   **Considera percentual na compensação de horas:** Ao habilitar este parâmetro, o sistema passará a considerar o percentual cadastrado para o evento e irá multiplicar as horas extras por seus respectivos percentuais para realizar a compensação. Caso contrário, as horas extras serão compensadas com atrasos na proporção 1/1.  
   **Utiliza na compensação manual de horas:** Essa opção será utilizada apenas para os funcionários que possuem banco de horas por período. Ao selecioná-la, o sistema irá lançar as horas extras dos funcionários para o banco de horas. Caso não selecione essa opção, o sistema irá lançar as horas extras para o movimento do funcionário.  
   **Fórmula para lançamentos para o banco de horas:** Informe uma fórmula de cálculo neste campo para que o sistema possa lançar as horas calculadas pela fórmula para o banco de horas. Se houver uma fórmula neste campo, o sistema irá desconsiderar o código de cálculo interno e utilizará o resultado da fórmula.
10. Sobre a guia **Informações adicionais**: Informe neste campo qual atitude é desejada para o evento cadastrado. A informação deste campo está relacionada com o parâmetro 'Considera Atitude do Evento' localizado na parte de Banco de Horas.      
      
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21170280226583)
11. Após efetuar as modificações, avance até a última etapa e salve as alterações no sindicato. Ao acessar o funcionário e executar o **recalculo com todos os parâmetros marcados,** as ocorrências serão gravadas em banco de horas. Para conferir clique nas guias banco de horas, saldo de horas analítico e saldo de banco de horas sintético.  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21187865674263)  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21187897308183)  
    ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21188211258391)

**Saiba mais**[Parametrização de Banco de Horas](https://tdn.totvs.com/display/LRM/Como+Fazer+-+Parametrizacao+de+Banco+de+Horas)  
[Percentuais do banco de horas](https://tdn.totvs.com/display/LRM/DT_Calculo_Hora_Extra_Noturna_Parte1)  
[Limite de Banco de Horas](https://tdn.totvs.com/display/LRM/Banco+de+Horas+-+Parametrizador)  
[Distribuição de Faixa de Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021835171-RH-RM-PTO-Distribui%C3%A7%C3%A3o-de-Faixa-de-Extras)
