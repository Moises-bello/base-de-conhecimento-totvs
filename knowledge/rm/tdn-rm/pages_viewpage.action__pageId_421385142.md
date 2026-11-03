---
content_hash: 5073103bb6b70c1a6c2d51d9e15c2299545685028501c4b52a904ef2c8993752
fetched_at: '2026-06-29T00:09:14.162404+00:00'
page_id: '421385142'
product: rm
source: tdn-rm
title: Revisão de Reprogramação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385142
version: 13
---

---

Para que o processo de gerar Revisão Horizontal de Reprogramação esteja disponível no momento da Revisão Múltipla é imprescindível que o projeto tenha controle de fases e que em "Projetos | Parâmetros | Construção e Projetos | Projetos (F6) | Projeto | Revisão de Reprogramação" tenha sido marcado o parâmetro "Permitir Revisão de Reprogramação na Revisão Múltipla".   
Com este parâmetro marcado ao ser acessado o Processo "Revisões Múltiplas" o sistema permitirá ao usuário optar pela criação de uma Revisão Vertical ou de uma Revisão Horizontal de Reprogramação.  
Este parâmetro não poderá ser desmarcado após ter sido criada alguma revisão horizontal de Venda, Planejamento ou Execução.   
   
Serão gerenciadas pela ferramenta de Revisão de Reprogramação:

* Tarefas – Serviços e Atividades (com PERT e cronograma);
* Composições (com os seus recursos);
* Insumos (com os seus preços);
* Grupos de Custo;
* Parâmetros do Projeto (normalmente, somente os parâmetros que determinam a data do projeto e consequentemente os períodos do cronograma devem ser alterados, mas esta restrição fica a cargo da configuração de segurança).

**Consistências da Revisão de Reprogramação**  
Em "Projetos | Parâmetros | Construção e Projetos | Projetos (F6) | Projeto | Revisão de Reprogramação" é possível definir se na Aplicação da Revisão de Reprogramação, o TOTVS Obras e Projetos irá ou não consistir quando a quantidade utilizada na atividade do projeto principal for diminuída na Revisão de Reprogramação.

* Parâmetro definido como Avisa: O TOTVS Obras e Projetos irá realizar a aplicação e, se a quantidade da tarefa for inferior à quantidade contratada ou comprada será emitido um alerta com todas as atividades que possuem essa característica e o sistema realizará a aplicação;
* Parâmetro definido como Barra: O TOTVS Obras e Projetos irá interromper a execução da aplicação e irá emitir uma mensagem com todas as atividades da Revisão de Reprogramação cuja aplicação tornaria sua quantidade inferior à já contratada;
* Parâmetro definido como Não Confere: O TOTVS Obras e Projetos, executará a aplicação sem consistir a quantidade da tarefa em relação ao contrato e ao plano de compras.

Em "Parâmetros | Construção e Projetos | Projetos (F6) | Contratos | Associação de itens e Objetos" caso o parâmetro "Não associar itens/objetos em mais de 100% da quantidade orçada (Contratos a Pagar)" esteja marcado, os parâmetros das consistências de Revisão de Reprogramação dos Contratos de Serviço, Material, Insumo e Extra-Histograma serão automaticamente definidos como Barra e não será possível alterar seu conteúdo pois os campos serão desabilitados.  
Na aplicação, serão verificados os seguintes tipos de contrato:

* Contrato de Serviço - A aplicação Revisão de Reprogramação irá analisar se a quantidade da tarefa na revisão está respeitando a quantidade já contratada. Assim, caso o processo de aplicação não atenda a esta regra, será acatado o parâmetro de consistência definido;
* Contrato de Parcela Fixa - O processo de aplicação verificará em seu parâmetro de projeto como o TOTVS Obras e Projetos ira se comportar ao detectar que a quantidade associada ao contrato está maior do que a quantidade na planilha de atividade ou que a quantidade na planilha de serviços está menor do que a já associada nos contratos a receber;
* Contrato de Insumo - O TOTVS Obras e Projetos, no momento da aplicação, irá verificar se a quantidade total associada ao contrato está mantida na planilha de atividades assim caso a quantidade total associada ao contrato seja superior ao total do insumo no projeto o TOTVS Obras e Projetos irá verificar os parâmetros de projeto e assim definirá qual comportamento deverá assumir durante esta consistência;
* Contrato Extra-Histograma (apenas caso exista Contrato de Insumo para pelo menos um dos insumos da tarefa) - A mesma consistência do Contrato de Insumo será efetuada para o contrato Extra Histograma, nos casos em que o mesmo for validado.

Estes parâmetros serão definidos no projeto principal e não poderão ser alterados na Revisão de Reprogramação. A consistência dos tipos de contratos e dos pedidos será feita separadamente, exceto quando nos Parâmetros do Projeto, em "Contratos | Liberação" o campo "Consistência entre Pedidos de Material e Contratos" estiver marcado, pois, dessa forma, a consistência será efetuada pela soma das quantidades dos contratos e pedidos e o sistema automaticamente preencherá todos os parâmetros de consistência da Revisão de Reprogramação com Barra, e não permitirá a alteração dos mesmos que estarão desabilitados.

**Criando uma Revisão de Reprogramação**  
Estando na visão de projetos, ao selecionar determinado projeto e entrar em "Processos | Revisões Múltiplas" o usuário poderá incluir uma Descrição para a Revisão que será criada e optar pelo Recálculo do Projeto.  
Recomendamos que este recálculo seja efetuado, garantindo que a revisão horizontal de Revisão de Reprogramação seja criada com os dados atualizados.   
Ao Avançar, o usuário poderá optar por gerar uma Revisão Vertical transformando a fase do projeto, ou por gerar uma Revisão Horizontal de Reprogramação.   
Após optar pela Revisão Horizontal de Reprogramação, o usuário deverá informar quem será o projeto mandatário, o projeto original ou a Revisão de Reprogramação, para a determinação da codificação das tarefas, insumos e grupos de custo quando houver qualquer conflito entre eles. Essa informação será utilizada pelo sistema nas rotinas "" e "" conforme abaixo:

* **Projeto Pai definido como Mandatário**: Se na Revisão de Reprogramação for criada uma tarefa, composição, insumo ou grupo de custo que possua um código que já exista no projeto pai, quando da aplicação da revisão de Revisão de Reprogramação, a tarefa, composição, insumo ou grupo de custo será transferida com um novo código, ou seja, independente do que foi definido na Revisão de Reprogramação, a ordenação dos códigos do projeto pai prevalecerá;
* **Revisão de Reprogramação definida como Mandatária**: Se for criada uma tarefa, composição, insumo ou grupo de custo cujo código já exista no projeto pai, no momento da Aplicação da Revisão de Reprogramação a tarefa do projeto pai terá seu código alterado para o próximo código disponível, o mesmo ocorrendo se na Revisão de Reprogramação for realizada a renumeração das tarefas, ou seja, independente do que existia no projeto pai, a ordenação dos códigos da Revisão de Reprogramação prevalecerá.

O sistema irá verificar se o parâmetro 'Utiliza Planilha de Serviço' está marcado em "Projetos | Parâmetros | Construção e Projetos | Projetos (F6) | Planilha de Serviços" e caso o projeto utilize Planilha de Serviço, o sistema apresentará em tela as atividades da Planilha de Serviços para que sejam selecionadas aquelas que farão parte da Revisão Horizontal de Reprogramação.  
Ao ser selecionado um serviço, o sistema automaticamente irá selecionar também todas as tarefas a ele vinculadas e estas tarefas farão parte da Planilha de Atividades da Revisão de Reprogramação. Assim, ao selecionar os serviços e Avançar o processo, o sistema apresentará a tela com as tarefas da Planilha de Atividades do projeto pai, sendo que as tarefas vinculadas aos serviços selecionados virão automaticamente marcadas.  
Na tela das tarefas da Planilha de Atividades o usuário poderá selecionar outras atividades além das que já vieram marcadas, sejam elas vinculadas a serviços ou não, sendo que, se for selecionada alguma atividade vinculada a algum serviço que não havia sido marcado, o sistema automaticamente irá gerar para a Revisão de Reprogramação o serviço vinculado à mesma, bem como as demais atividades vinculadas a este serviço.  
Os vínculos entre as Planilhas de Serviços e de Atividades serão sempre mantidos, portanto, caso seja desmarcado um serviço, todas as atividades vinculadas ao mesmo serão desmarcadas, e caso seja desmarcada uma atividade, o sistema irá desmarcar o serviço vinculado a essa atividade, bem como todas as demais atividades vinculadas a este serviço.  
No canto esquerdo do rodapé das telas de seleção das atividades da Planilha de Serviços e da Planilha de Atividades será apresentado um contador que informará ao usuário a quantidade de serviços e a quantidade de atividades selecionadas.  
Caso o projeto não utilize a Planilha de Serviços, será apresentada somente a tela com as atividades da Planilha de Atividades para que sejam selecionadas aquelas que farão parte da Revisão de Reprogramação.  
Antes da execução do processo de criação da Revisão Horizontal de Revisão de Reprogramação o sistema exibirá em tela um resumo contendo todas as tarefas da Planilha de Serviços e da Planilha de Atividades que farão parte da Revisão de Reprogramação a ser criada, solicitando a confirmação ou o cancelamento por parte do usuário.  
Na geração de uma de Revisão de Reprogramação, o sistema seguirá as seguintes regras:

* Quando for selecionada uma tarefa, as etapas e obras superiores a esta tarefa serão automaticamente selecionadas e consequentemente copiadas;
* Quando for selecionada uma etapa ou obra, as tarefas abaixo da mesma serão automaticamente selecionadas e consequentemente copiadas;
* Será mantido o mesmo identificador da tarefa na nova revisão, pois ele será utilizado mais tarde para identificar o vínculo da Revisão de Reprogramação com o projeto pai;
* As composições, insumos, cronogramas e preços associados às tarefas selecionadas também serão copiados;
* Antes de realizar a cópia das tarefas, os parâmetros do projeto serão copiados para a nova revisão automaticamente;
* Não serão levados para a revisão de Revisão de Reprogramação os Contratos e suas Medições, Riscos, Apontamentos, Mobilidade e Planos de Compras realizados no projeto pai;
* Os novos projetos de Revisão de Reprogramação criados a partir da versão 12.1.18 do TOP Obras e Projetos contemplarão os processos de Incluir/Alterar/Excluir Grupos de Custo, portanto, caso existam na base Projetos de Revisão de Reprogramação criados em versões anteriores, será necessário realizar um Sincronismo para que seja automaticamente efetuada a atualização dos Grupos de Custo nesses Projetos.

**Ações da Revisão de Reprogramação**  
Após ter sido gerada a Revisão Horizontal de Reprogramação o usuário poderá alterá-la, efetuando assim o replanejamento do projeto.

**Ações Não Permitidas na Revisão de Reprogramação:**

* Alocação de Recursos (exceto Interprojetos);
* Alteração em períodos do cronograma que já vieram travados do projeto pai;
* Alterações no quadro de permanência;
* Apontamentos de Equipamento;
* Apontamento Manual e por Período (validação ao selecionar o projeto no lookup e ao salvar o apontamento);
* Apropriação de Serviços/Insumos;
* Associar Calendário de Turno;
* Ciclos de Transporte;
* Contratos;
* Custos Diretos;
* Custos Indiretos;
* Diário de Projeto;
* Equipamentos Associados ao Projeto;
* Equipes de Mobilidade;
* Equipes de Timesheet;
* Exclusão de Composições não utilizadas;
* Exclusão de Insumos não utilizados;
* Exclusão de tarefas, composições, insumos e/ou grupos de custo que vieram do projeto pai;
* Execução de Tarefas (Monitor e Tray Icon);
* Folhas Tarefa;
* Gerar Lançamento Financeiro;
* Gerar Projeto de Licitação;
* Importação da ORCECERTO;
* Importação de arquivo TXT;
* Importação via MS Project;
* Importar EMOP;
* Importar FGV;
* Importar Insumo do Suprimento/Faturamento;
* Integração com Orçamento;
* Mapa de Apontamentos de Equipamento;
* Mobilidade;
* Pedido de Material;
* Pedido de Material Extra;
* Quadro de Permanência;
* Redução do número de períodos do cronograma;
* Relatório Ciclo de Transporte;
* Relatório Cronograma Mensal;
* Relatório de Folha Tarefa;
* Relatório de Medição Completa;
* Relatório de Plano de Ação;
* Relatório Feedback;
* Relatório Membros de Equipe;
* Saldo para Fluxo de Desembolso;
* Sincronização com MS Project;
* Sincronizar Folha de Ponto;
* Timesheet;
* Transformar Recursos Globais em Locais.

**Ações Permitidas na Revisão de Reprogramação:**

* Alterações na Tarefa (inclusive código);
* Alterações nas Composições e Recursos da Composição;
* Alterações nos Insumos e Preços dos Insumos;
* Alterações nos Grupos de Custo;
* Inclusão de novas Tarefas;
* Inclusão de novas Composições (somente serão consideradas se tiverem associação com alguma tarefa da Revisão de Revisão de Reprogramação – direta ou indireta);
* Inclusão de novos Insumos: (somente serão consideradas se tiverem associação com alguma tarefa da Revisão de Revisão de Reprogramação – direta ou indireta);
* Renumeração e Alteração do Código das Tarefas (serão aplicadas conforme a revisão definida como mandatária);
* Alterações no Cronograma;
* Alterações nos Parâmetros (somente serão aplicadas as alterações referentes ao cronograma);
* Uso do Comparador de Projetos para comparar as alterações realizadas com a revisão de escopo atual;
* Equalização de Insumos;
* Importação via MS Excel para insumos, composições, tarefas e grupos de custo;
* Cópia de Itens;
* Relatórios Periódicos;
* Backup/Restore de Projeto;
* Disciplina (inclusão, edição e exclusão);
* Alterações na Planilha Executiva.

Veja Também

---

[Revisões Múltiplas](http://tdn.totvs.com/pages/viewpage.action?pageId=421385536)
