---
content_hash: 9e3a547f885203802bf604ecf3ea33be7eb027e8d9c64b16933a0f8feb6e2efc
fetched_at: '2026-06-29T00:10:02.509435+00:00'
page_id: '452718934'
product: rm
source: tdn-rm
title: Processo de configuração da Avaliação de desempenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718934
version: 15
---

**Processo de configuração da Avaliação de desempenho**

---

Este processo irá configurar toda a Avaliação de Desempenho.  
A execução do processo será dividida por etapas, são elas:

* **Criar uma avaliação de desempenho e salvar.**

Após salvar a avaliação, o menu **PROCESSOS** será liberado e a avaliação poderá ser configurada.

* **Assistente de configuração da Avaliação de Desempenho**: Acesse Processos | Processo de configuração da avaliação de desempenho.

Dar um nome ao processo (opcional) e clicar em avançar na primeira tela.   
 

* **Modalidade da Avaliação de Desempenho**: Nesta etapa o usuário definirá qual a modalidade da Avaliação:

   
          90º graus: Avaliadores avaliam seus Avaliados.  
          180º graus: Avaliadores avaliam seus Avaliados, e os Avaliados realizam a Auto avaliação. É possível gerar uma Avaliação Consensual automática ou manualmente;  
          360º graus: Avaliação é feita de modo circular por todos os elementos que mantêm algum tipo de interação com o Avaliado.

* **Pesos para os itens a avaliar**: Nesta etapa o usuário poderá alterar os pesos dos itens avaliados.

* **Itens a avaliar**: Nesta etapa o usuário definirá os itens a serem avaliados na Avaliação de Desempenho.

* **Escala da Avaliação de Desempenho**: Nesta etapa o usuário definirá se irá utilizar a escala padrão do sistema ou não, podendo além de alterar a escala incluir intervalos para a mesma.

   
Exemplo de uma alteração de escala utilizando intervalo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Escala de avaliação** | **Valor da Escala** | **Início do Intervalo** | **Término do Intervalo** |
| Não Atende | 1 | 1 | 1.9 |
| Atende Parcialmente | 2 | 1.91 | 2 |
| Atende | 3 | 2.01 | 3 |
| Supera | 4 | 3.01 | 4 |
| Supera com excelência | 5 | 4.01 | 5 |

O intervalo na escala é um range que estabelece de quanto até quanto será considerada aquela nota. De acordo com os intervalos definidos acima, se a nota obtida for 1.85, será considerada a nota 1.

* **Relatório**: Nesta etapa o usuário definirá o relatório que ficará disponível para os Avaliadores no Portal. No book de relatório da TOTVS o relatório '02.010.01 - Avaliação de Desempenho [Portal]' encontra-se disponível para a geração. Em caso de customização do relatório, é necessário possuir os parâmetros: COLIGADA, CODIGOAD, CODPARTICIPANTE. Para o correto funcionamento, a ordem da inclusão dos parâmetros deve seguir a ordem descrita anteriormente.

* **E-mails Customizados**: Nesta etapa o usuário definirá qual e-mail será enviado para os participantes sobre a execução da avaliação, pendência da avaliação e sobre a avaliação consensual. -E-mail sobre a execução da avaliação: Marcando o parâmetro "Enviar email somente para as avaliações pendentes" o sistema altera o comportamento do processo disponível no menu: Avaliação de desempenho - Processo: Enviar e-mail para os avaliadores A.D. Parâmetro desmarcado: Envia um email listando todas as avaliações independente do seu status. Parâmetro marcado: Envia um email listando somente as avaliações pendentes.  Obs.: Ao clicar para selecionar os e-mails serão exibidos as mensagens customizadas de todas as coligadas. Pode  ser  criado um filtro para facilitar a visualização.

* **Opções de Exibição no Portal**: Nesta etapa o usuário informa se no Portal será exibida a nota da competência e os pesos dos itens avaliados para o Avaliador e se o mesmo irá ou não avaliar diretamente a competência. Informa também qual a ordem que serão respondidos os itens a avaliar (metas e fatores organizacionais).

* **Avaliadores/Avaliados da Avaliação de Desempenho**:   Nesta etapa o usuário definirá quem são os "Avaliadores" e os "Avaliados". Serão exibidos somente avaliados da coligada contexto da Avaliação de Desempenho.
* **Reconfigurar apenas participantes inseridos**: ao marcar este flag quando se realizar alguma alteração na avaliação de desempenho já iniciada, apenas as informações dos funcionários inseridos serão atualizadas.

**Atenção:** - Se o parâmetro "Tipo de Gestão Hierárquica" (Configurações|Parametrizador|Preferências) estiver definido "Por Posição" ao configurar uma avaliação de desempenho será considerado a Gestão de Hierarquia ativa no sistema e as opções acima de elegibilidade serão desconsideradas. Apenas estará disponível o filtro de seleção de funcionário dentre as opções de elegibilidade. - O filtro "Avaliadores" deverá retornar líderes conforme Gestão de Hierarquia ativa.  
**Observação:** - No Processo de Configuração da Avaliação de Desempenho, se o parâmetro "Ocultar notas para o Avaliador/Avaliado" for marcado, o Avaliador/Avaliado não visualizam as notas da Avaliação de Desempenho no Portal.  
Maiores informações sobre a Gestão de Hierarquia consulte o Help.

* **Resumo geral das configurações da montagem da Avaliação de Desempenho**: Nesta etapa o usuário visualizará antes de executar o processo de configuração como ficou a montagem da sua Avaliação.

* **Finalizar o processo**: Nesta etapa o usuário finaliza o processo de configuração.

   
Voltar
