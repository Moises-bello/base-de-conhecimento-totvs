---
article_id: 360017559512
category: Banco de Horas
content_hash: d27b48316cffb2d3dabab2a7cb7fd7a4fc37d9c793bbb5362edd0991c8d60240
fetched_at: '2026-06-28T22:46:27.816940+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Como configurar o banco de horas por período
type: support-article
updated_at: '2024-06-12T19:00:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017559512-RH-RM-PTO-Como-configurar-o-banco-de-horas-por-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19408945835031) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como configurar o banco de horas por período?   
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**

Antes de iniciar os passos, vamos compartilhar algumas informações importantes sobre o banco de horas por período. **Para garantir que tudo funcione perfeitamente, é necessário realizar a compensação manual do banco de horas por período após o fechamento do ponto do funcionário e antes da liberação mensal.** Mesmo que alguns funcionários não tenham eventos de extras, atrasos ou faltas lançadas para pagamento (movimento), é importante fazer a compensação para atualizar o saldo do banco de horas por período. Lembramos que em períodos anteriores ao atual, não é possível armazenar no banco de horas eventos de horas extras junto com eventos de faltas ou atrasos. Essa separação é fundamental para manter a integridade dos registros.

Agora, para configurar o uso do banco de horas por período, siga atentamente os passos e parâmetros a seguir:

1. Acesse no módulo de **Automação de Ponto,**o menu **Configurações | Parametrizador**. Ao abrir o assistente, clique em avançar e selecione o processo**08.02 - Sindicato** e edite o sindicato desejado. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/19408929236887)
2. Ao abrir o assistente, avance até a etapa **Banco de Horas** e marque o campo "**Utiliza banco de horas**" e em "Tipo de banco de horas", selecione o tipo **Período**.  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21197398990359)  
     
   Importante**:   
   - A partir desta etapa, faça a parametrização conforme sua regra de negócio.**  
   **- Dos passos 3 a 5 serão validos somente para os funcionários que utilizarem horário do tipo rígido.**
3. Na guia "Parâmetros gerais" na etapa do Banco de Horas, há a seção "**Limite de horas diárias**", que permite limitar as ocorrências entre movimento e banco de horas de forma automática ao marcar o campo "**Utiliza Limite de horas diárias**".  E possível optar por limite por percentual e/ou Número de horas. **-Limite por percentual**: Nessa opção, você pode definir um limite máximo de quantidade a ser paga. Todas as quantidades informadas até esse limite serão pagas e enviadas para o movimento.  
   **-Número de horas**: Nessa opção, consideramos a quantidade de horas trabalhadas dentro da jornada, incluindo as horas extras realizadas no dia. As horas que ficarem dentro do limite serão armazenadas como banco de horas, enquanto as horas que ultrapassarem serão pagas.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21225751812503)

   **Observações:**

   * Para aproveitar ao máximo o limite de horas diário, é necessário **desmarcar** o parâmetro "Utiliza compensação manual de horas" no parametrizador do funcionário.   
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21225771658647)
   * Lembre-se de que, ao utilizar esse parâmetro, é necessário **autorizar todas as horas extras** executadas pelo funcionário. Dessa forma, todas as horas extras serão consideradas para o cálculo do sistema, seja para compensação ou pagamento no movimento do funcionário.
   * Ao utilizar as duas opções, o sistema irá considerar primeiro o limite do percentual e, em seguida, o limite de número de horas, no cálculo.
4. Ao ativar o parâmetro "Utiliza Limite de Horas Diárias", você também ativará os parâmetros **"Utiliza limite máximo de horas semanais"** e **"Utiliza limite mínimo"**:

   Ao selecionar o parâmetro "**Utiliza limite máximo de horas semanais**", o sistema considerará um limite máximo de horas trabalhadas (soma das horas trabalhadas dentro da jornada prevista, e as extras realizada). Todas as horas extras realizadas acima desse limite serão pagas no movimento do funcionário, levando em conta o limite diário. As horas que ultrapassarem o "Limite Diário" não serão contabilizadas no limite de horas semanais, pois já foram pagas no movimento.

   Já ao selecionar o parâmetro **"Utiliza limite mínimo de horas semanais"**, o sistema considerará um limite mínimo de horas trabalhadas. Com base nesse limite, o sistema decidirá se as horas de atrasos e/ou faltas serão lançadas no movimento para serem descontadas.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21225751895575)
5. Para ativar os parâmetros adicionais, **"Compensa extra de descanso "**, **"Compensa extra de feriado"** e **"Compensa extras de dia compensado"**, é necessário **desabilitar** o parâmetro **"Utiliza limite máximo de horas semanais"**.

   Esses parâmetros permitem a compensação das horas extras realizadas em dias de descanso, feriados e dias compensados no banco de horas por período, respeitando o limite diário estabelecido. Caso contrário, as horas extras serão pagas no movimento. Caso opte por trabalhar com um percentual, por favor, informe o percentual dentro do limite de horas que serão pagas.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21225771723671)
6. Ainda na etapa de Banco de Horas, temos a guia **"Percentual de Incidência"**. Nela, é possível definir o percentual de incidência sobre o limite de horas da jornada estipulado na parametrização.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21225771746583)  
     
   **Considera percentual para o limite do banco de horas**: Ao habilitar este parâmetro, o sistema calculará um percentual de incidência sobre o limite de horas da jornada estipulado na parametrização.  
   **Considera percentual do evento do banco de horas ao exibir o saldo do banco de horas**: Este parâmetro leva em consideração o percentual do campo "código do evento lançado no movimento do cadastro de eventos do banco de horas" para exibir nas guias saldo de banco sintético e analítico na visão do espelho de ponto do funcionário.   
   **Considera percentual do evento do banco de horas na compensação do banco de horas**: Este parâmetro leva em consideração o percentual do campo "código do evento lançado no movimento do cadastro de eventos do banco de horas" durante o processo de compensação.  
   **Considera percentual ao exibir o saldo do banco de horas**: Este parâmetro tem como objetivo considerar o percentual de incidência das horas extras, para exibir nas guias saldo de banco sintético e analítico na visão do espelho de ponto do funcionário. Importante: Para que os parâmetros funcionem corretamente, é necessário que os eventos de horas extras tenham o parâmetro "Considera percentual de incidência" marcado.
7. Acesse no módulo de **Automação de Ponto,**o menu **Configurações | Parametrizador** . Ao abrir o assistente, clique em avançar e selecione o processo**08.02 - Funcionário** e edite o funcionário desejado. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13661681999127)
8. Ao abrir o assistente, avance até a etapa **Banco de horas funcionário** e marque o parâmetro **"Usa compensação manual de horas".** Marque as opções de Atrasos, Faltas e Horas Extras, que deseja considerar no banco de horas, caso contrário irão para o movimento.  
   ![2018-10-11_12_25_18-Assistente_de_Implanta__o_de_Processos__Processo__08.03_-_Parametrizando_funcion.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013180812)  
   **Observações**:  
   - Ao marcar a opção de horas extras serão enviadas para o banco as ocorrências de horas as extras de compensado, descanso, feriado e normal.  
   -As Horas só serão lançadas para o banco de horas se as mesmas estiverem autorizadas e os eventos a serem calculados estiverem com a opção Utiliza Compensação Manual de Horas marcada.  
   **- Se desejar alterar o parâmetro de maneira global**, siga os passos do link: [Como fazer a alteração global de parâmetros dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019945111-TOTVS-RH-Linha-RM-PTO-Como-fazer-a-altera%C3%A7%C3%A3o-global-de-par%C3%A2metros-dos-funcion%C3%A1rios)
9. Volte ao **Parametrizador do Sindicato** e avance até a etapa **Eventos**. Edite o evento de hora extra desejado e marque a opção **"Utiliza na compensação manual de horas".** Faça o mesmo com os demais eventos em que as horas serão enviadas para o banco de horas.   
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13661973783703)![2018-10-11_12_26_29-.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013190631)
10. Recalcule o espelho do funcionário com todos os parâmetros marcados e verifique as horas na aba **Banco de horas**, **Saldo de Banco de Horas****Analítico** e **"Saldo de Banco de Horas Sintético**" dentro do espelho do funcionário.   
      
    ![2018-10-11_12_32_12-Espelho_do_Funcion_rio_00003_-_MARIA_CONCEICAO_DE_ASSIS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013190651)

**Observação:**Quando se utiliza banco de horas por períodos as colunas de banco de horas na aba Totais do dia não serão preenchidas

**Importante**O banco de horas **por período** registra as compensações do período agrupadas por evento, na tabela ACOMPFUN.

**Saiba Mais**  
Para maiores informações sobre o banco de horas, acesse:  
[Parametrização Banco de Horas](http://tdn.totvs.com/display/public/LRM/Como+Fazer+-+Parametrizacao+de+Banco+de+Horas)  
[Banco de Horas - Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719093)
