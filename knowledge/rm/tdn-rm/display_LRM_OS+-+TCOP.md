---
content_hash: 4164cae3e305f3cc0f1af56492231850a3bcb5fc538dd3ffc649888d8e562711
fetched_at: '2026-06-29T00:11:45.055064+00:00'
page_id: '819053156'
product: rm
source: tdn-rm
title: OS - TCOP
type: documentation
url: https://tdn.totvs.com/display/LRM/OS+-+TCOP
version: 8
---

**Ordem de Serviço**

As Ordens de Serviços(OS) devem ser emitidas para a execução de serviços nos Objetos de Manutenção. As OS são compostas por itens de serviços e peças. Acesse o menu  Manutenção / Ordem de Serviço.

A Ordem de Serviço apresenta os seguintes status: “Aguardando Análise”, “Não-Iniciado”, “Em Andamento”, “Terminado”, “A Faturar”, “Faturado”.

A numeração da OS é automática de acordo a parametrização do movimento no Sistema de Gestão de Estoque e Faturamento. Quando a OS é gerada recebe o status “Aguardando Análise”, nesta situação não é possível alocar Mão de Obra. O próximo status é “Não-Iniciado” e posteriormente, “Em Andamento”.

Durante a mudança para este último, o usuário tem a opção de alocar Mão-de-Obra. É possível também iniciar, terminar e interromper os serviços. Após a execução dos serviços é possível alterar a OS para o status “Terminado”. A partir desta etapa, a OS pode ser encaminhada para faturamento, alterando-se o status para “A Faturar”. Após ser faturado pelo Sistema de Gestão de Estoque e Faturamento, o status da OS passará a ser “Faturado”.

* **Aguardando Análise:** quando a OS é gerada, recebe o status “Aguardando Análise”, nesta situação não é possível alocar mão-de-obra.
* **Não Iniciado:** o Próximo status na hierarquia é Não-Iniciado. Indica a finalização da análise e passa para a “fila” de execução.
* **Em Andamento:** durante a mudança para este status o usuário tem a opção de alocar mão-de-obra. È possível também iniciar, terminar e interromper serviços. Assim se a mesma tiver um grande número de serviço, todos executados pelo mesmo técnico este é o melhor momento para alocá-los.
* **Terminado:** indica o término da manutenção. Somente é permitida a mudança para o status terminado quando todos os serviços forem completamente concluídos. Um serviço só está concluído quando forem registradas data e hora de conclusão. A partir desta etapa, a OS pode ser encaminhada para faturamento.
* **A Faturar:** no caso de venda de serviço, ao mudar a OS para este status o movimento estará disponível para faturamento no Sistema de Gestão de Estoque e Faturamento.
* **Faturado:** após o faturamento no Sistema de Gestão de Estoque e Faturamento, o movimento assumirá este status. Não sendo permitido nenhuma alteração em movimentos com status Faturado.
* **Em Faturamento:** quando houver um término inadequado do sistema durante um faturamento/ recebimento de pedidos no Sistema de Gestão de Estoque e Faturamento, estes irão apresentar o status “Em faturamento”. Este status só poderá ser alterado no Sistema de Gestão de Estoque e Faturamento, para posterior andamento no Sistema de Gestão de Manutenção.
* **Cancelado:** este status indica que a OS foi cancelada. Somente as Ordens de Serviço com status cancelado podem ser excluídas. Cada gestão de manutenção deve determinar os seus critérios.
* **Bloqueado:** caso seja cadastrado um item de valor maior que o saldo disponível no orçamento, a OS será bloqueada. Para desbloquear a OS o usuário pode editar o valor, ou reprocessar o movimento no Backoffice.

Para efetuar a mudança de status de Ordens de Serviço, basta clicar com o botão direito do mouse sobre uma OS, e proceder a mudança sugerida no menu suspenso que será apresentado.

A mudança de status não precisa acontecer na ordem mencionada acima, pois é possível voltar a situações anteriores, ou passar de um status para outro que não seja o próximo na hierarquia.

È possível cancelar uma OS. O status passará para “Cancelado”. No entanto, OS nesta situação não pode ter seu status alterado. Os motivos são cadastrados no menu Tabelas / Ordem de Serviço /Motivo do Cancelamento da OS.

Apenas OS com status Cancelado, poderão ser excluídas, e a exclusão deverá ser feita pela visão de OS do módulo de Manutenção de Equipamentos:

No vencimento de um plano de manutenção também deve ser emitida uma Ordem de Serviço para a execução do mesmo. Atendimentos e Agendamentos podem ser convertidos em Ordens de Serviço no momento da execução da demanda de manutenção registrada nos mesmos. As OS são geradas a partir de movimentos parametrizados no Sistema de Gestão de Estoque e Faturamento. O Sistema de Gestão de Manutenção lê somente movimentos da série OS para a geração de ordens de serviços. Porém, todos os movimentos do tipo 1 e tipo 2 podem ser utilizados para gerar movimentação dos itens das ordens.

**Parâmetros da Ordem de Serviço**  
Manutenção / Ordem de Serviço.

**Verifica Estoque dos Produtos**  
Marque esta opção para que o sistema verifique se existe a peça que consta na OS no estoque. Caso não exista, o sistema informará que a peça está em falta e oferecerá a possibilidade de substituição por um produto similar - de acordo com o cadastro de produtos do RM Nucleus.

**Permite Alterar Histórico de Problemas**  
Marque esta opção para que o histórico de problemas possa ser alterado livremente. Quando esta opção estiver desmarcada, somente o histórico de problemas do módulo de Ordens de Serviço não poderá ser alterado. No módulo de atendimentos a alteração pode ser efetuada.

**Permite Alterar Funcionário Responsável**  
Marque esta opção para que o funcionário responsável possa ser alterado após a abertura da OS. Caso contrário, o responsável definido na inclusão antes de “Salvar”não poderá ser alterado. Se o funcionário “logado” é um supervisor, este poderá mudar o responsável mesmo com esta opção desmarcada.

Se o usuário que efetuou o login estiver relacionado a um funcionário, o funcionário responsável será preenchido automaticamente, mas ele pode ser modificado na inclusão. Esta opção permite também controle sobre alteração de funcionário responsável pelos atendimentos.

**Permite Alterar OS Cancelada**  
Normalmente não se deve permitir alterar uma OS cancelada. Marcando o parâmetro o sistema permite a alteração.

**Campo indicador de uso na OS é obrigatório**  
Este parâmetro é muito útil para a gestão de manutenção. Obriga que na abertura de uma OS a mesma seja vinculada a um valor de indicador de uso. Assim é possível saber quando, em termos de quilômetros e/horas, por exemplo, foi efetuada a intervenção.

**Permite aumentar ou diminuir preço**  
Permite aumentar e diminuir o preço definido pelo movimento para os itens da OS. No caso de OS de venda de serviços este recurso pode ser necessário.

**Verifica se o funcionário está ativo na data ao fazer apontamento**  
Ao alocar uma mão de obra o sistema irá verificar se a mão-de-obra está ativa na data atual. Se não estiver, o sistema irá apresentar a mensagem: “Mão de obra “XX” encontra-se inativa na data atual! Deseja assim mesmo incluir mão de obra?”

Essa mensagem é necessária apenas para advertir, pois o usuário pode precisar fazer alocação de mão-de-obra retroativa. Porém NÃO será possível apontar horas, caso esteja inativo.

**Utiliza motivo de cancelamento na ordem de serviço**  
Marque esta opção para que seja obrigatório informar o motivo ao cancelar uma OS. Acesse o menu Cadastros / Tabelas Auxiliares / Manutenção / Motivo do Cancelamento da OS.

**Gera Ordem(ns) de Serviço Automática(s)**  
Marque esta opção quando for necessária a geração automática de Ordens de Serviço. Neste caso, será disponibilizada a Pasta “Parâmetros”, no Cadastros de Planos de Manutenção e Agendamento de Serviços onde poderá ser informado o tipo de movimento para o qual será gerada automaticamente a Ordem de Serviço.

**Tipo de Recorrência**  
Permite informar o tipo de recorrência e o horário de execução da geração automática de ordem de serviço. Recorrência significa de quanto em quanto tempo o serviço será executado. O agendamento da próxima execução poderá ser visualizado no menu Sistema / Server / Processos Agendados. Será enviado um e-mail do log de geração automática de ordem de serviço para o e-mail do usuário que iniciou o processo. O processo deverá ser iniciado em Sistema / Server / Executar Processo. O parâmetro “Gera Ordem(s) de Serviço Automática(s)” deverá estar marcado, se o mesmo estiver desmarcado não será possível alterar os campos tipo e hora de recorrência.

**Agrupar planos com mesmo vencimento na mesma OS**  
Ao gerar uma OS para um Objeto de Manutenção, se o mesmo possuir mais de um Plano de Manutenção vencendo juntos, os planos serão agrupados na mesma OS.

**Permite cadastrar OS para objetos que possuam OS aberta**  
Marque esta opção para que seja possível emitir várias ordens de serviço para um mesmo objeto. Caso queira que o sistema lhe informe que já existe outra OS aberta para o mesmo objeto marque o parâmetro “Solicita confirmação ao incluir OS para objetos que possuam” OS aberta.

**Permite transferência de Bem Vinculado a objeto com OS Normal**  
Se marcado, permite fazer a transferência de um Bem no RM que tenha ordem de serviço normal em aberto.

**Permite transferência de Bem Vinculado a objeto com OS em Terceiros**  
Se marcado, permite fazer a transferência de um Bem no RM que tenha ordem de serviço em terceiro em aberto.

**Disponibilizar todas as Mãos de Obras quando não segmentado**  
Se marcado, permite que todo o cadastro de mão de obra fique disponível para serem alocadas em serviços, caso não tenha feito a segmentação de mão de obra por tipo de objeto de manutenção, modelo ou submodelo.

A Parametrização dos movimentos no Sistema de Gestão de Estoque e Faturamento Para o Sistema de Gestão de Manutenção pode ser acessada no menu Cadastros / Tipos de Movimento.

**Pasta Identificação**  
Os campos “Código”, “Séries” e “Nome” são informativos de acordo com os parâmetros determinados no sistema de Gestão de Estoque e Faturamento e não podem ser alterados no Sistema de Gestão de Manutenção.

**Filial:** é possível selecionar a filial “default” que será utilizada ao abrir uma OS utilizando o movimento selecionado.  
**Local de Estoque:** é possível selecionar o Local de Estoque “default” que será utilizada ao abrir uma OS utilizando o movimento selecionado. Os locais de estoque são cadastrados no aplicativo RM Nucleus.

Os dados parametrizados para os campos Filial e Local de Estoque são apenas o “default” e podem ser alterados. Tal parametrização é utilizada no caso da empresa emitir, na maioria das vezes ou sempre, ordens de serviços para a mesma filial e/ou local de estoque.

**Parâmetros Manutenção**  
Os parâmetros de Peças e Serviços são normalmente utilizados pelas assistências técnicas para venda de serviços. Porém, o ideal é utilizar a parametrização de preços para os itens dos movimentos no  
Sistema Gestão de Estoque e Faturamento. O Percentual que incidirá sobre o preço de tabela dos serviços e produtos. O preço original é determinado de acordo com a parametrização do movimento no Sistema de Gestão de Estoque e Faturamento.

Exemplo:  
“% do preço-padrão”  
Suponha que, para o tipo de movimento “Garantia da Fábrica”, utilizado para manutenção de objetos cobertos pela garantia do fabricante, a oficina não cobrará o preço de serviços ou peças. Para este tipo de movimento, deverá ser cadastrado, no campo % do preço-padrão, o valor 0 (zero), ou seja, o cliente não pagará nada pela manutenção (0% do preço-padrão) ou troca de peças. Supondo que seja cadastrado um tipo de movimento “Cliente Preferencial”, que dê um desconto de 40% em produtos ou serviços. Cadastre, então, o valor 60 para o campo % do Preço Padrão, indicando a porcentagem do preço-padrão que o cliente pagará.

Serviços:

* Moeda Hr Padrão: moeda utilizada para a cobrança dos valores.
* Valor Hr Padrão: valor padrão para cobrança de uma hora de serviço. Ao determinar um valor padrão, todos os serviços da OS serão cobrados de acordo com este preço vezes o “Tempo do Serviço”. O “Tempo do Serviço é informado no cadastro de produtos e serviços do Sistema de Gestão de Estoque e Faturamento na Pasta Integração.

Cobrança por Tempo Efetivo: determina a forma de cobrança para os itens serviços da OS aberta com o tipo de movimento selecionado na Pasta Identificação. Ao determinar que a cobrança é por tempo efetivo o sistema calculará o tempo gasto para realizar o serviço com base no apontamento do início e término no mesmo e multiplicará pelo valor da hora padrão.

Caso as Gerais “Valor Hr Padrão” e “Cobrança por Tempo Efetivo” não estejam sendo utilizados os serviços das OS, serão utilizados os valores parametrizado do movimento no Sistema de Gestão de Estoque e Faturamento.

Formato de relatório p/ Impressão na Visão: selecione o formato de relatório do tipo ordem de serviço “default” que será utilizado para imprimir as ordens de serviços abertas com o movimento que esta sendo parametrizado. A OS é impressa no botão Imprimir OS na tela de visão da Ordem de Serviço.

Func. Responsável: determina o funcionário responsável “default” pela abertura das Ordens de Serviço aberta com o movimento que esta sendo parametrizado.

Ordem de Serviço para Terceiros: marcar esta opção para determina que o movimento seja de Ordem de Serviço para Terceiros. Somente os movimentos com este parâmetro podem ser utilizados para a abertura de ordens de serviços para Terceiros.

Não gera OS com Status Aguardando Análise: marcar esta opção determinar que as ordens de serviços aberta com o movimento que esta sendo parametrizado não passará pelo status “Aguardando Análise”. Ou seja, terão como primeiro status “Não Iniciado”.

**Pasta Identificação**  
A OS exigirá Cliente / Fornecedor se o movimento estiver parametrizado para requerê-lo. Se esta tiver um Cliente / Fornecedor e ele tiver um contrato de manutenção para o objeto da OS será possível utilizá-lo. Isto significa abrir a OS com o movimento parametrizado no contrato. Não é permitido alterar o Cliente / Fornecedor de uma Ordem de Serviço em andamento.

A parametrização do número do movimento se será automático ou não. È definido nos parâmetros do Sistema de Gestão de Estoque e Faturamento. Se a numeração esteja selecionada como “MOSTRA”, estará parametrizada para ser automática, fazendo com que o número identificador da Ordem de Serviço seja atribuído automaticamente pelo sistema. Caso a numeração esteja selecionada como “EDITA”, o número da Ordem de Serviço deverá ser informado no momento de sua criação.

Caso a numeração esteja parametrizada para ser informada pelo usuário no momento da criação da OS, poderão existir Ordens de Serviço com o mesmo número. Desta forma, podem ser geradas Ordens de Serviço com o mesmo número desde que não haja coincidência de Coligada e Filial, ou seja, para mesma Coligada só podem existir OS com mesmo número se estes não pertencerem à mesma Filial.

Centro de Custo: permite selecionar um centro de custo para a Ordem de Serviço. No cadastro do Cliente / Fornecedor é possível definir um centro custo default para cada cliente.

Ao cadastrar uma Ordem de Serviço o centro de custo será preenchido com o centro de custo do Objeto de Manutenção, desde que não haja default para o centro de custo do Tipo de Movimento e centro de custo default para o cliente/Fornecedor, ou seja, a busca do centro de custo para a Ordem de Serviço terá a seguinte ordem:

1. Centro de Custo do Cliente/Fornecedor;
2. Centro de Custo do Tipo de Movimento;
3. Centro de Custo do Objeto de Manutenção.

Verificar Local de Instalação: permite a verificar o local onde está instalado o objeto. A instalação de Objetos de Manutenção é efetuada no menu Operações / Instalação de Objeto de Manutenção.

* **Data de Emissão:** esta data já vem preenchida automaticamente pelo sistema com a data e hora atual do servidor, mas pode também ser alterada.
* **Data de Autorização:** data e hora em que foi autorizada a execução dos serviços na OS. O sistema assume que esta é a mudança do status “Não-Iniciado” para “Em Andamento”.
* **Data de Término:** data e hora do término de todos os serviços constantes na OS. O sistema assume que esta é a mudança do status “Em Andamento” para Terminado.
* **Data de Saída:** data e hora em que o que o objeto de manutenção foi liberado da oficina. O sistema assume que esta é a mudança do status “Terminado” para “A Faturar”.
* **Data de Programação:** data e hora para a qual a Ordem de Serviço foi programada. Uso opcional.

**Processos e Informações acessados por meio dos botões da tela de edição da Ordem de Serviço:**

**Indicador de Uso:** acesso ao histórico e apontamento da medição de indicador de uso do objeto de manutenção da OS selecionada.

**Dados de Cliente:** permite visualizar dados do cliente ou fornecedor da OS selecionada. Os campos mostrados não estão disponíveis para edição. A edição deles está disponível no cadastro de Cliente/Fornecedor no aplicativo RM Fluxus.

**Acessório:** permite visualizar os acessórios do Objeto de Manutenção. Os acessórios do Objeto são cadastrados no “Anexo – Acessório” do cadastro do Objeto de Manutenção.

**Problemas:** permite inserir os problemas padronizados diagnosticados nesta intervenção e/ou visualizar os problemas inseridos no atendimento que gerou a OS selecionada. Os Problemas são cadastrados no menu Tabelas / Ordem de Serviço / Problemas.

Para aquelas Ordens de Serviço que foram geradas a partir do módulo de Atendimentos podemos observar que se o atendimento possuir observações cadastradas no campo “Relato Adicional de Problemas”, estes dados também serão visualizados aqui. A alteração de um histórico já gravado depende da sua parametrização em  Parâmetros / Manutenção / Ordem de Serviço “Permite Alterar Histórico de Problemas”. Caso o parâmetro esteja desmarcado, não será permitido alterar o histórico e tornará visível o botão para adicionar um novo texto do problema.

Histórico de Ordem de Serviços: permite pesquisar o histórico de ordens de serviço e atendimentos do objeto de manutenção da OS selecionada.

Alocação de Mãos de obra: permite alocar mão-de-obra para os serviços da OS selecionada. Através deste recurso é possível alocar, para um mesmo serviço, vários técnicos de maneira ágil. Este recurso é muito útil, já que muitas vezes um mesmo técnico realiza todos os serviços da OS.

Resumo Técnico: acesso ao relatório informativo sobre as horas técnicas da OS. As informações contidas no mesmo são:

* Total de Técnicos Alocados: número de técnicos que estão alocados para os serviços constantes na OS (um técnico para cada serviço). Este número só será exibido após a alocação da mão-de-obra na Pasta Itens ou quando o status da OS for alterado de Não-Iniciado para Em Andamento.
* Total de Horas Previstas: tempo previsto para execução de todos os serviços constantes na OS. Este valor é o somatório da multiplicação da quantidade de cada serviço vezes o seu Tempo  
  Padrão. O tempo padrão do serviço é informado no cadastro de produtos e serviços no Sistema de Gestão e Faturamento e pode ser alterado ao incluir o serviço na OS.
* Total de Horas Efetivas: total de horas dependidas para a realização dos serviços. Diferença entre hora final e hora inicial do apontamento de cada serviço. Para tal é necessário realizar o apontamento de início e termino de cada serviço.
* Total de horas de Mão de obra: somatório do total de horas despendida por cada técnico alocado na OS. Se em um mesmo serviço tiver mais de um técnico alocado também será incluído no  
  somatório as horas de cada um.

Os dados do Resumo Técnico não estarão disponíveis para Ordem de Serviços para Terceiros, tornando desabilitado o botão.

Contrato deste Cliente: permite visualizar o Contrato de Manutenção para o Objeto de Manutenção da Ordem de Serviço.

Reforma de Pneu: na abertura de Ordem de Serviço para Objeto de Manutenção do tipo Pneu, ao marcar o checkbox “Reforma” o botão “Reforma de Pneu” será habilitado. Clicando no botão será aberta a tela de Reforma de Pneu para informar o processo de reforma, o modelo de desenho e o tipo de borracha. Quando a Ordem de Serviço for concluída no Cadastros de Objeto de Manutenção na Pasta Identificação o campo “Reforma” será incrementado para registrar quantas vezes o objeto passou por reforma.

Desconto: desconto padrão definido para todos os itens da OS. A utilização de desconto é considerada somente quando parametrizado no aplicativo RM Nucleus. Após definido os valores do desconto padrão nos parâmetros do movimento da Ordem de Serviço é possível determinar os valores pré-estabelecidos ou digitar o valor desejado no campo “Desconto”, confirmando o valor para todos os itens, através do botão “Desconto nas Ordens de Serviço”. Caso o valor digitado no campo “Desconto”, seja diferente do estabelecido no parâmetro do movimento da OS, ao clicar no botão “Confirmar Desconto” será exibido uma mensagem de confirmação, informando que o valor do desconto está diferente do valor do desconto padrão.

Despesa: o valor da Despesa pode ser considerado para toda a ordem de serviço, digitando o valor desejado e em seguida clicando no botão “Despesa na Ordem de Serviço”.

É importante a verificação dos seguintes parâmetros no RM Nucleus:

* Afetar desconto do Movimento: se desmarcado, ao efetuar um desconto no item da OS os descontos NÃO modificarão o valor liquido da OS.
* Afetar despesas do Movimento: caso desmarcado, ao efetuar uma despesa no item da OS as despesas NÃO irão modificar o valor liquido da OS.

Atualiza Valores: após inserir os produtos e serviços clique no botão “Atualiza Valores” para efetuar o cálculo do total de serviços e produtos da Ordem de Serviço.

Não é permitido emitir Ordem de Serviço para Objetos Sucateados ou Transferidos. Ao tentar salvar a OS o sistema irá emitir uma mensagem de restrição.

**Itens**  
Permite adicionar os produtos e serviços que compõem a Ordem de Serviço. A partir da inclusão dos produtos é possível requisitá-los, ordenar a compra ou executar qualquer movimento do Sistema Gestão de Estoque e Faturamento necessário para o desenvolvimento da OS. Ao adicionar um produto caso não possua estoque do mesmo no Sistema de Gestão de Estoque e Faturamento o sistema irá emitir a seguinte uma mensagem: "Não existe no local de estoque "X" a quantidade "X" do produto "Determinado pelo usuário", Deseja selecionar um produto similar ou substituir?

O produto similar ou substituto é cadastrado no sistema de Gestão de Estoque e Faturamento. Ao clicar em “SIM” o sistema irá abrir uma tela para com relação de produto similar. Clicando em “NÃO” o produto será inserido na Ordem de Serviço e será necessário providenciar a compra do mesmo. Para os serviços é possível alocar mão-de-obra e gerenciar a execução. Serviços também podem ser requisitados, como por exemplo a Ordem de Serviços de Terceiros.

Os itens do tipo produto ficam com status “Peça destinada à Officina”, o status “Peça Utilizada em Reparos” indica que já foi impresso um pedido de peça pelo técnico da oficina e os itens do tipo serviço ficam com status “Não Inciado”.

Os status dos Serviços são:

* Não Iniciado

Quando inserido na OS e com mão-de-obra alocada ou não.

* Em andamento

Após iniciar o serviço, independente de estar ou não interrompido.

* Terminado

Quando o serviço for completamente executado.

**Apontamento de Mão de Obra**  
Na tela de visão dos itens há três botões “Iniciar Apontamento para Serviço”, “Interrompe Apontamento para Serviço” e “Termina Apontamento para Serviço”. Os mesmo botões são visíveis na edição do item do tipo serviço. Ao editar um serviço a Pasta Mão de Obra será habilitada. A diferença é que na tela de visão da Pasta Itens o apontamento é feito para todos os itens ao mesmo tempo. Na Pasta Mão de Obra o apontamento é feito para cada serviço e mão de obra isoladamente. É possível alocar mais de uma mão-de-obra em um mesmo serviço. Na Pasta Mão de Obra existe também um botão chamado “Inserir Apontamento”, para fazer apontamento múltiplo, ou seja, é possível iniciar, interromper e terminar um serviço em única tela.

* O apontamento é feito apenas para itens do tipo serviços e mão de obra ativa.
* A data e hora de início do apontamento não poderão ser maiores que a data atual.
* A data e hora de início não poderão ser menores que a data e hora de emissão da ordem de serviço.
* A data e hora de término não podem ser maiores do que a atual.
* A data e hora de término não podem ser menores ou iguais à data e hora de inicio.
* Ao incluir vários apontamentos para uma mão-de-obra em um mesmo serviço, a data e hora de início do novo apontamento não poderão ser menores que data e hora do término do último apontamento.

No cadastro de Produtos/Serviços, Anexos Produto – Informações de manutenção, ao marcar o parâmetro “Permite abertura simultânea para mesma mão-de-obra”, o sistema permite fazer apontamentos simultâneos para uma mesma mão de obra. Através do menu Cadastros / Segurança / Perfis , Pasta Acesso à Menus. É possível remover as permissões de acesso aos botões “Iniciar”, “Interromper” e “Terminar” apontamento de mão-de-obra, para determinado perfil de usuários. Faça o logout/login no sistema para que as alterações sejam validadas. É possível criar campos complementares para Ordem de Serviço e para o Item da Ordem de Serviço. Para cadastrar os campos complementares acesse o menu “Cadastros / Campos Complementares / Movimento e Item do Movimento”. Os campos complementares permitem a criação de campos do tipo inteiro, alfanumérico, data, real e texto.

**Backlog Peças e Serviços**  
Ao finalizar os apontamentos nos itens da Ordem de Serviço o campo status ficará como “Terminado” e o campo Processamento ficará como pendente. Ao mudar o status da Ordem de Serviço para “Terminado” sem ter feito o processamento dos itens o sistema o emitirá a seguinte mensagem:

Caso clique em “SIM” o sistema colocará os serviços e/ou peças como pendente para a próxima ordem de serviço. O status da Ordem de Serviço passará para “Terminado” e o campo processamento continuará como Pendente. Ao abrir uma nova Ordem de Serviço para o Objeto de Manutenção na Pasta Itens da Ordem de Serviço clicando no botão “Lista de Peças/Serviços Pendentes” a tela apresenta todos os serviços e peças pendentes para o Objeto Manutenção que podem ser inseridos na Ordem de Serviço atual.

Selecione os itens e clique no botão “OK” e os mesmo serão inseridos na Ordem de Serviço com o status “Não-Iniciado”. Após finalizar o apontamento dos itens para colocar a Ordem de Serviço no status “Terminado” é preciso efetuar o processamento dos itens. Na tela de visão do cadastro de Ordem de Serviço clique no menu Movimentação / Executar Processamento. Ao abrir a tela na Pasta Itens selecionem os itens desejados e clique em “OK” para efetuar o processamento. O campo “Processamento” da Ordem de Serviço e do Item ficará com “Executado”. É possível “Cancelar” e “Dispensar” o processamento dos itens. Ao solicitar a dispensa do processamento o campo “Processamento” ficará como “Dispensado” permitindo  
assim a mudança de status da Ordem de serviço para “Terminado”.

**Requisição de Material**  
Permite a geração de um movimento do tipo Requisição de Material para o Sistema de Gestão de Estoque e Faturamento. A requisição define os produtos necessários à execução da Ordem de Serviço. Caso não tenha os produtos em estoque através desse movimento será possível gerar uma solicitação de compra ou uma ordem de compra.

Importante:

Requisições de material parametrizadas para serem enviadas com o status Não Processado, quando são processadas no Gestão de Estoque e Faturamento recebem o status Pendente para que possam seguir o fluxo normalmente. Não é permitido enviar requisições utilizando o tipo de movimento "OS", somente deverão ser utilizados os tipos solicitação de compra ou ordem de compra.

**Geração de Movimento de Entrada**  
Permite dar entrada de produtos no estoque do Sistema de Gestão de Estoque e Faturamento. Quando um produto não for utilizado em uma Ordem de Serviço é preciso devolvê-lo ao estoque. Assim será gerado um movimento de devolução no Sistema de Gestão de Estoque e Faturamento e o estoque será incrementado de acordo com as quantidades devolvidas.

**Geração de Movimento de Saída**  
Permite dar baixa em estoque dos produtos necessários para execução dos serviços. Será gerado no Sistema de Gestão de Estoque e Faturamento um movimento de baixa de estoque que irá decrementar o saldo físico.

**Movimentos Relacionados**  
Permite visualizar todos os movimentos que foram gerados para a Ordem de Serviço, como: Requisição de Material, Movimento de Saída, Movimento de Entrada, Solicitação de Compra e Ordem de Compra.

**Pasta Indicadores de Uso**  
Os campos “Medidor” e “Acumulado” mostram os valores de indicadores de uso lançados para objeto de manutenção da ordem de serviço selecionada.

Se uma ordem de serviço possuir lançamentos de indicadores de uso com data e hora igual à data e hora de “Emissão”, “Autorização”, “Término” e “Saída” da Ordem de Serviço. Na Pasta de indicadores de uso da tela de Ordem de Serviço, é possível visualizar os valores de indicadores de uso das respectivas datas alternando de acordo com os campos data e hora de “Emissão”, “Autorização”, “Término” e “Saída”. Clique com o botão direito do mouse sobre a Pasta e selecione a opção de data e valor de indicador de uso lançado na respectiva data e será exibido nos campos “Medidor” e “Acumulado”.

**Pasta Planos Realizados**  
Permite visualizar os Planos de Manutenção executados na Ordem de Serviço. As Ordens de Serviço geradas a partir dos módulos Objetos de Manutenção, Contratos de Manutenção e Cronograma de Manutenções, já trazem o Plano de Manutenção executado. Na Pasta Identificação serão mostrados apenas os Planos de Manutenção cadastrados para o Objeto de Manutenção em questão, de acordo com o cadastro de Planos de Manutenção (Modelos e/ou Submodelos).

No momento de se incluir o Plano Realizado, o aplicativo emitirá uma mensagem perguntado se é desejado incluir na Ordem de Serviço o(s) Item(ns) correspondente(s) do Plano de Manutenção selecionado.

No momento de se excluir algum Plano Realizado, o aplicativo emitirá uma mensagem perguntando se é desejado excluir o(s) item(ns) correspondente(s) ao plano, que já estão presentes na Ordem de Serviço.

Seleção de Preço Permite selecionar o preço dos produtos/serviços presentes no Plano de Manutenção, de acordo com a parametrização no Sistema de Gestão de Estoque e Faturamento.

**Anexo - Item da OS**

Esse anexo irá exibir diretamente na tela da visão, os itens de cada OS de forma simples e rápida, sem que seja necessário editar o movimento para consultá-los:
