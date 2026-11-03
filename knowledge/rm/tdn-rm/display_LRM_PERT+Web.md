---
content_hash: b79be0c5697a316701aaa765902a804b0c24e458f18b08fb6a5d513103631f1c
fetched_at: '2026-06-29T00:11:11.032284+00:00'
page_id: '644958302'
product: rm
source: tdn-rm
title: PERT Web
type: documentation
url: https://tdn.totvs.com/display/LRM/PERT+Web
version: 132
---

O **PERT** **Web** representa uma nova maneira de monitorar o planejamento e o progresso da obra, com uma interface extremamente intuitiva e acessível tanto no sistema quanto na web. Ele proporciona aos usuários acesso rápido e eficiente ao status das atividades, além de destacar os caminhos críticos do projeto. Isso permite ajustes no planejamento e garante o foco necessário para evitar atrasos na obra.

**Parâmetros**

**Habilitando o PERT**

* **Projetos:** Menu Projeto > TOTVS Construção Obras e Projetos > Projetos (F6) > PERT / Alocação de Recursos.

**Mais informações:**

Acesse a documentação do Novo PERT Web para detalhes sobre os parâmetros que impactam a ferramenta:  [PERT/Alocação de Recursos (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385179)

Após a Parametrização, é possível acessar o PERT no **Menu Planejamento | PERT** e escolher a Planilha que deseja visualizar - As Planilhas disponíveis são de Atividades, Serviço, Planilha Executiva  e seus respectivos cenários.

**Campos do PERT Web**

## Visão Geral do PERT:

**Topo da Tela:**

* **Data de Início:** Início do projeto (definida em Parâmetros do Projeto > Cronograma > Períodos).
* **Data de Término:** Término do último período do projeto (calculada pelo número de períodos em Parâmetros do Projeto > Cronograma > Períodos).
* **Dias Trabalhados:** Total de dias trabalhados no projeto, do início ao fim.
* **Localizar Tarefa(s):** Encontre tarefas pelo código: digite o código e pressione ENTER para selecionar. A linha azul se moverá para o código pesquisado.

**Benefícios:**

* **Visão rápida:** Veja as datas de início e término do projeto, dias trabalhados e acesse tarefas por código.
* **Navegação facilitada:** Localize tarefas rapidamente com a pesquisa por código.

**Observações:**

* As datas de início e término são configuráveis nos parâmetros do projeto.
* O número de dias trabalhados é atualizado automaticamente.
* A pesquisa por código é útil para encontrar tarefas específicas rapidamente.

**Dicas:**

* Utilize a pesquisa por código para navegar rapidamente pelas tarefas do projeto.
* Monitore os dias trabalhados para acompanhar o andamento do projeto.
* As datas de início e término podem ser ajustadas conforme necessário somente nas tarefas, em obras e etapas as datas não podem ser alteradas.

**Resumo:**

O topo da tela do PERT oferece uma visão geral rápida do projeto, incluindo datas de início e término, dias trabalhados e uma ferramenta de pesquisa para localizar tarefas por código. Essa funcionalidade facilita a navegação e o acompanhamento do andamento do projeto.

## Encontre Tarefas Rapidamente com Pesquisa por Descrição

**Busque com Facilidade:**

* Digite apenas uma parte da palavra-chave da descrição da tarefa.
* O sistema destacará em azul todas as tarefas que contêm a palavra pesquisada.

**Exemplo:**

* Deseja encontrar a tarefa "Preparo formas blocos"?
* Digite apenas "prepa".
* O sistema destacará todas as tarefas que contêm "prepa" na descrição, como "Preparo armação de tubulões", "Preparo armação de blocos", etc.

**Salvar:**

Por default o botão fica desabilitado, habilitando somente quando ocorre alguma alteração dos campos editáveis no PERT.

A partir da primeira alteração, o botão fica disponível para clicar como informado anteriormente:

**Cancelar:**

Cancela as alterações realizadas no PERT e que até o momento não foram salvas.

**Atualizar:**

Atualiza os dados do PERT

O PERT leva em consideração os parâmetros informados para o projeto (trabalho aos sábados, domingos, feriados, jornada, calendário e datas programadas). [PERT/Alocação de Recursos (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385179)

**Calcular PERT**

Calcula os planos cedo e tarde, a folga, e o caminho crítico tendo como referência a obra, ou seja; com base nas informações inicialmente cadastradas para cada tarefa, tais como datas início e fim, duração da tarefa e vínculos existentes entre as tarefas:

**Exportar:**

Nesse botão existem dois processos de exportação que serão descritos logo adiante. Para ambos é necessário selecionar as tarefas que serão exportadas. 

**Exportar PERT para o Cronograma:**

Não disponível no PERT da planilha executiva

Possibilita exportar o que foi planejado, ou realizado, do PERT para o cronograma.  

Para selecionar mais de uma tarefa, utilize o comando Ctrl + clique nas tarefas, ou etapas, para selecionar um intervalo maior. 

Antes de realizar a exportação do PERT para o cronograma, veja mais detalhes em: [Exportar PERT para Cronograma](https://tdn.totvs.com/display/LRM/Exportar+Pert+para+Cronograma) 

**Exportar PERT para PDF:**

Essa funcionalidade permite  exportar PERT para PDF, podendo escolher importar nas opções: Completo (planilha e gráfico) ou apenas a planilha ou apenas o gráfico.

Para exportar para o PDF o sistema considerará apenas 1000 tarefas selecionadas como limite para exportar.

Na tela onde se informa os dados de exportação só permitirá o plano planejado.

**Funções de Planejamento**

**Atualizar Linha Base:**

Não disponível no PERT da planilha executiva

Ao executar esse processo, o PERT atualiza a coluna linha base com a data que será considerada como base do planejamento.

**Linha Base como Planejamento:**

Não disponível no PERT da planilha executiva

Essa funcionalidade atualiza a Data Início e Data Fim respectivamente de todas as tarefas com o valor da coluna Data inicio Base e Data Fim Base.

**Plano Real como Planejamento:**

Essa funcionalidade atualiza a Data Início e Data Fim respectivamente de todas as tarefas com o valor das colunas Data Inicio Real e Data Fim Real.

**Plano Tarde como Planejamento:**

Essa funcionalidade atualiza a Data Início e Data Fim respectivamente de todas as tarefas com o valor das colunas Data Inicio Tarde e Data Fim Tarde.

**Plano Cedo como Planejamento:**

Essa funcionalidade atualiza a Data Início e Data Fim respectivamente de todas as tarefas com o valor das colunas Data Inicio Cedo e Data Fim Cedo.

**Análise de Ordem de Produção:**

Não disponível no PERT da planilha executiva

O processo de análise de ordem de produção será exibido apenas em ambientes integrados com Protheus e com o pacote PCP.

Este processo é responsável por buscar as datas de entrega das ordens de produção no PCP Protheus e atualizar o planejamento das respectivas tarefas no PERT.

Após o processo de envio da requisição de ordem de produção para o PCP, é necessário verificar se a data de fabricação do produto impacta o planejamento da tarefa no PERT. 

No momento em que o processo de “Análise de Ordem de Produção” no PERT, for executado, o TCOP irá consultar se existe alguma ordem de produção para as tarefas que possuem recurso associado e esse recurso tenha produtos manufaturados.

A atualização de datas do PERT, apenas poderá ocorrer se o produto manufaturado associado ao insumo receber uma data de fabricação posterior à data de conclusão (data fim programado) da tarefa; se o cenário ocorrer, será disparado uma mensagem de alerta ao usuário solicitando que o mesmo defina se as datas das tarefas deverão ser atualizadas ou não, como demonstrado na imagem abaixo:

Caso o usuário confirme a atualização da data fim programada no PERT, o TCOP irá atualizar a data fim programada, consequentemente alterando a duração da tarefa. Como a duração da tarefa também pode ser afetada pelo processo de “cálculo de duração por fórmula”, na execução do processo de análise de ordem de produção não será considerado a formula caso a tarefa esteja marcada para utilizar o cálculo de duração por formula. Após as datas das tarefas serem alteradas pelo processo “Analise de ordem de produção”, o TCOP irá disparar automaticamente a funcionalidade de programar do PERT, para manter o planejamento das datas e sucessões de todas as tarefas.

Se o parâmetro do projeto “Atualiza automaticamente pela ordem de produção” estiver selecionado, as datas das tarefas ser]ao atualizadas de acordo com a data programada da ordem de produção, sem a necessidade do alerta, tornando este processo automático. A atualização automática do PERT, fará com que todas as datas planejadas em tarefas e predecessores sejam atualizadas de acordo com a data prevista de fabricação. Mas caso o parâmetro “Atualiza automaticamente pela ordem de produção” não esteja selecionado será disparado o alerta solicitando a atualização, conforme detalhado anteriormente.

Para mais detalhes do parâmetro: [PERT/Alocação de Recursos (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385179)

**Demais recursos e funcionalidades**

**Dividir:**

Não disponível no PERT da planilha executiva 

Cria um(ou mais) intervalo(s), ou pausa(s) em uma tarefa no gráfico de Gantt. Para saber mais .

**Vincular:**

Selecione as tarefas (Ctrl+clique nas tarefas desejadas) e clique no botão Vincular, para que o vínculo entre as tarefas seja criado.

**Desvincular:**

Selecione uma das tarefas vinculadas ou (Ctrl+clique nas tarefas desejadas) e clique no botão Desvincular para que o vínculo seja desfeito.

**Caminho Crítico:** 

Exibe as tarefas criticas. O caminho crítico é a sequência de tarefas que leva mais tempo para ser terminada. Essa sequência determinará o tempo total do projeto de construção e não haverá folgas nas atividades. É a informação mais importante porque, a partir dela, é possível identificar quais serviços devem ser priorizados e finalizados no prazo para que a obra não sofra atrasos.

O caminho crítico será exibido em vermelho quando selecionado o botão de visualização, conforme destaque na imagem abaixo:

**Escala de tempo**

Permite alternar entre diferentes escalas de tempo de acordo com a necessidade ou preferência do usuário, podendo visualizar o gráfico em dias, semanas, meses, trimestre ou ano, conforme demonstrado abaixo:

**Aumentar escala**

Permite ajustar a visualização do Gantt, aumentando a escala de acordo com a preferência do usuário:

**Diminuir escala**

Permite ajustar a visualização do Gantt, diminuindo a escala de acordo com a preferência do usuário:

**Expandir:** 

Expande todos os níveis de tarefas existentes, exibindo obras, etapas e tarefas.

**Resumir:** 

Recolhe as tarefas e etapas, exibindo somente as obras do projeto.

**Configurador de Layout**

**Planejado:**

Exibe o Gantt na sua configuração padrão com base nas datas planejadas início e fim.

**Planejado x Real**, **Planejado x Base**, **Planejado x Cedo**, **Planejado x Tarde:**

Planejado x Base não disponível no PERT da planilha executiva

São os comparativos de visão dentro do Gantt, comparando as datas planejadas com as demais datas do PERT, nesse comparativo a linha da tarefa é dividida em duas, onde as linhas verdes( Obras/Etapas ) e azuis ( Tarefas ) são ainda as datas planejadas que continuam editáveis e as linhas amarelas ( não editáveis ) são as datas Real, Base, Cedo ou Tarde, serão exibidas com base no tipo de layout escolhido, dentro do período em que se encontram nas colunas de data. Abaixo uma imagem de exemplo:

**Desfazer:**

Desfaz a última ação/alteração executada. O botão habilita a partir da primeira alteração feita:

- Quando o usuário realiza várias alterações e ainda não salvou, ele tem a opção de desfazer uma a uma. Limitado às 10 últimas alterações feitas.

**Filtro de Pesquisa**

Disponibilizamos um filtro de pesquisa para facilitar a localização de informações no PERT. Com este recurso, você pode realizar buscas de forma mais precisa, utilizando os seguintes critérios:

* **Cod. Trf.**: Pesquise pelo Código da Tarefa.
* **Nome**: Pesquise pelo nome associado à tarefa.
* **Data de Início**: Defina um intervalo (de - até) para a data inicial da tarefa.
* **Data de Fim**: Defina um intervalo (de - até) para a data de conclusão da tarefa.

Além disso, o filtro inclui as opções **Limpar** (para resetar os critérios de busca) e **Aplicar** (para executar a pesquisa).

### **Informações da planilha PERT:**

**Cód.Trf:**

Código da tarefa na planilha de atividades.

**Nome:**

Descrição da tarefa na planilha de atividades.

**Data Início:**

Data programada para inicar a Etapa.

* Ao adiantar ou atrasar a Data Início Programada de uma Etapa, a Data Fim Programada  será automaticamente ajustada para manter a mesma duração original da tarefa.

**Exemplo:** Se uma tarefa tem início em 01/01/2024 e fim em 15/01/2024 (duração de 14 dias), ao adiar o início para 05/01/2024, o fim será ajustado para 19/01/2024, mantendo os 14 dias de duração.

**Data Fim:**

Data fim planejada para conclusão da etapa de acordo com a duração desta.

* Ao modificar a Data Fim Programada de uma Etapa, a duração será recalculada para refletir a nova data.

**Exemplo:** Se uma tarefa tem início em 01/01/2024 e fim em 15/01/2024 (duração de 14 dias), ao adiantar o fim para 08/01/2024, a duração será automaticamente ajustada para 7 dias.

**Importante:** A duração nunca será negativa. Se a nova Data Fim Programada for muito próxima da Data Início Programada, a duração será ajustada ao mínimo possível (1 dia, por exemplo).

O sistema impedirá que a Data Fim Programada seja definida antes da Data Início Programada. Ao tentar fazer essa alteração, o sistema exibirá uma mensagem de erro.

**Duração****:**

Número de dias programados para a duração da tarefa contando a partir da sua data início até a sua data fim.

**Predecessoras:**

Lista as atividades vinculadas e anteriores à tarefa. A identificação da(s) predecessora(s) é feita através do número da sua linha. Permite os vínculos: II (Início-Início), IF (Início-Fim), FI (Fim-Início) e FF (Fim-Fim). Assim, o formato para predecessora é formado pela linha da tarefa, o tipo de vínculo e defasagem, quando houver. é permitido informar várias predecessoras, bastando apenas separá-las por ";" (ponto e vírgula) conforme demonstrado na célula selecionada na imagem acima.

**% Concluído:**

Percentual concluído para a tarefa no projeto. O PERT Web permite informar percentual com mais de 100% desde que esteja parametrizado para isso veja mais detalhes na documentação dos parâmetros do **[PERT/Alocação de Recursos (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385179)**

**Data Início Real:**

Data em que a tarefa iniciou realmente.

**Data Fim Real:**

Data fim real da tarefa, ou seja, quando ela é 100% concluída.

**Duração Real:**

Quantidade de dias entre a data início e data fim real.

**Folga:**

Dias de folga definidos nos **parâmetros do projeto (Não trabalha sábado/domingo etc)[PERT/Alocação de Recursos (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385179)**

**Data Início Cedo:** 

Data mais cedo possível para se inicar a tarefa.

**Data Fim Cedo:**

Data mais cedo possível calculada para concluir a tarefa.

**Data Início Tarde:**

Data mais tarde possível para se iniciar a tarefa.

**Data Fim Tarde:**

Data mais  tarde para finalizar a tarefa que não afete o cronograma do projeto ou alguma sucessora.

**Data Início Base:**

Não disponível no PERT da planilha executiva 

É preenchida através da função do planejamento "Atualizar Linhas de Base". Pega a data início informada para a tarefa no momento e copia para a linha de base.

**Data Fim Base:**

Não disponível no PERT da planilha executiva

Também é preenchida através da função do planejamento, copiando a data fim da tarefa como base.

**Legenda de cores**

Passando o mouse pela linha, tanto do lado da planilha quanto do gráfico, é possível visualizar a legenda detalhada das cores destacadas no PERT:

**Informações da Tarefa**

Ao dar um duplo clique sobre a tarefa é possível ver os detalhes da tarefa. É exibido uma tela com as seguintes informações : Código da tarefa, nome, percentual concluído, unidade, tarefa crítica , valor unitário, quantidade, valor parcial e duração calculada.

Além disso, são exibidas suas predecessoras e sucessoras, com as informaçoes da tarefa vinculada e o tipo do vinculo:

Se houver um projeto sem períodos definidos nos parâmetros de projeto, mas com o Pert Web habilitado, ao tentar acessar o PERT, será exibida a tela abaixo com uma mensagem mostrando o que deve ser feito para utilizar o PERT Web normalmente. Caso informe os períodos, não é necessário fechar o PERT, clicando no botão Atualizar ele vai recarregar a tela com os períodos criados.

Após definido o cronograma do projeto, ao abrirmos o PERT de um projeto pela primeira vez, a data início default das tarefas será a data início do projeto (definida nos parâmetros) e a duração default será de 1 dia:

**Data fora do cronograma do projeto**

Nos casos em que a parametrização permite que o usuário altere as datas, podem ser escolhidas datas iniciais ou finais que estejam fora do intervalo do projeto, nesse caso é exibida rapidamente uma mensagem informativa no canto superior direto da tela, e também a célula das datas que estiverem fora desse intervalo, são exibidas com uma cor de fundo diferencial, conforme pode ser observado na imagem abaixo:

É importante observar que, mesmo permitindo datas fora do período do projeto, os feriados definidos no calendário dos parâmetros do projeto para o PERT, nunca serão considerados como dias trabalhados para as datas fora do período do projeto.

**Tarefas inativas:**

As tarefas inativas na planilha de atividades serão exibidas com destaque no PERT:

**Ordenação das colunas**

É possível definir a ordem das colunas de acordo com a preferência do usuário, bastando clicar e arrastar para a posição desejada:

**Tarefa Marco**

Marco é uma técnica de Gestão de Projetos que representa o fim de um estágio, de uma entrega de um pacote de trabalho ou fase. Tipicamente composto por um evento de alta importância tal como completude de um pacote, formalização ou sinalização de um entregável, documento ou uma reunião importante de revisão.

Não é uma atividade e não possui duração e corresponde a um ponto de controle em um cronograma, através da definição de pontos de checagem ou marcos de desenvolvimento. Representa a conclusão de um conjunto de tarefas ou fase, passiva de aprovação e formalização por parte do cliente.

Marco

**Usando Marco no Planejamento**

Um marco pode adicionar um significante valor para o planejamento de um projeto. Quando combinado com uma  sofisticada metodologia  tal como o PERT, os  "marcos" permitem uma gestão de projetos mais eficiente para determinar se a execução está em dia ou não. Através da restrição das datas associadas ao marco, o caminho crítico pode determinar os principais intervalos de planejamento do projeto. Defasagens (Latências) podem também ser calculadas para cada intervalo.

Esta segmentação do planejamento do projeto em intervalos permite uma identificação mais precoce dos problemas de planejamento e uma visão melhor das atividades cuja realização é crítica.

Marcos são frequentemente usados para monitorar progresso, principalmente quando eles fazem parte do caminho crítico.

**Características esperadas:**

* A atividade marco não ocupa espaço no cronograma e deve ter data inicio e fim igual a data fim da atividade predecessora. Caso não tenha predecessora terá a data que o usuário atribuir. Ela participa do Calculo do PERT (plano cedo, tarde, folgas, tarefa crítica) da mesma forma que as demais.
* Também não devem aparecer em curvas ABC ou Relatórios relacionados a execução como Relatórios Periódicos, no entanto podem aparecer em relatórios que relacionam tarefas e devem ser copiados pela cópia de itens.
* A tarefa Marco no gráfico Gantt será exibida com o desenho do losango roxo como na imagem acima.

**Como criar um Marco**

Para criar uma nova tarefa já configurada como um marco:

* Pode ser importada um Marco do MS Project.
* Possuir Atividade na Planilha de Atividades e Períodos no Cronograma, assim será gerado as mesmas tarefas no PERT .

Para transformar uma tarefa em marco:

* Na visão do PERT Web altere a Duração da tarefa para  o valor 0, assim automaticamente a tarefa será alterada para 'Marco'.
* Você pode visualizar se a tarefa é 'Marco' ao editar a tarefa na Planilha de Atividades na aba PERT, terá uma flag indicando
