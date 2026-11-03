---
content_hash: 6a945b4d4cd57421a6f97f9c306d732f5556ff8ea8bde9b493e188263056b239
fetched_at: '2026-06-29T00:09:15.269653+00:00'
page_id: '421385329'
product: rm
source: tdn-rm
title: Cópia de Itens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385329
version: 6
---

---

Esta opção possibilita a cópia de obras, serviços, composições, insumos, grupos de custo, parâmetros e curvas de distribuição do projeto. Se o projeto corrente for um projeto global, só será possível copiar grupos de custo, insumos ou composições.

**ATENÇÃO:** Porém, em se tratando do processo de Cópia de Itens nem todas devem ser copiadas, considerando que tal processo tem como finalidade o apoio à criação de um novo projeto que normalmente se inicia através de uma Orçamentação e depois o Planejamento.

Nas fases citadas, ainda não existe a necessidade, de folhas tarefas e suas respectivas dependências como apontamentos de coletores e alocações de mão de obra, pois tais funcionalidades são necessárias, considerando o módulo de mobilidade, já na Execução do projeto.

Logo, as informações relacionadas com funcionalidades de mobilidade que estarão presentes no processo de cópia de itens, serão apenas as equipes de projetos, considerando os dois tipos, sendo:

Mobilidade - Gestão de Riscos

Por se tratar de um cadastro que possui integração com o cadastro de pessoas, e insumos, através das funções, sua estrutura poderia ser reaproveitada em outros projetos da mesma base de dados.

Na aba de equipes de projeto serão exibidas todas as equipes existentes no projeto nas quais o usuário poderá selecionar as que deseja copiar para o projeto destino. No momento da cópia de membros de equipes, os insumos relacionados aos mesmos serão copiados automaticamente para que a integridade das informações possa ser preservada.

**Atenção:**  
Somente é possível realizar a cópia de "Equipes de Projeto", desde que o projeto que terá a equipe copiada, não esteja com o status em "Andamento". Pois, um membro de equipe (pessoa) não pode estar alocado em dois projetos em andamento ao mesmo tempo.

Serão exibidas as seguintes colunas na aba de equipes: "Tipo da Equipe", "Descrição", "Responsável", "Tipo do Responsável pela Equipe", "Ativa?".

Dados do Projeto de Origem: Coligada: Coligada do projeto de origem da cópia. Essa cópia leva em consideração que o projeto Global existente na coligada origem não existe na coligada destino, por essa razão, os recursos (insumos e composições) globais, utilizados no projeto origem, e os grupos de custos globais, são copiados como locais. Como os insumos globais são copiados como locais, os seus preços (locais e globais) também são; sendo que os preços locais dos insumos globais são copiados do projeto origem.

Projeto: Projeto de origem da cópia.

Parâmetros: Copia os parâmetros do projeto selecionado para o projeto corrente, ou seja, o conteúdo das pastas Cálculo, Exibição, Cronograma, Campos Livres, Log, Pert / Alocação de Recursos, Insumos, Contratos, Apropriação e Integração.

**Atenção:**  
Caso a filial do projeto de origem da cópia seja diferente da filial do projeto de destino da cópia (projeto aberto), os parâmetros de "Movimentação de Estoque" e "Tipo do Movimento de Transferência" serão alterados para falso e nulo respectivamente e os locais de estoque disponíveis e selecionados serão excluídos.

Grupo de Custo:  
Esta opção possibilita a cópia de grupos de custo do projeto escolhido para o projeto aberto, podendo copiar do próprio projeto aberto. Se o projeto corrente for um projeto global, só será possível copiar grupos de custo, insumos ou composições.

**Observação:**   
Na pasta Defaults, a faixa de códigos de insumos obedecerá a máscara de insumos definida no Menu Opções | Parâmetros | TOTVS Construção Obras e Projetos | Projetos | Pasta Exibição do Projeto Destino. Quando um caractere do código a ser importado não estiver de acordo com a máscara será solicitado um código correspondente para a posição em que ele se encontra. Caso a máscara seja definida com caracteres numéricos e o código a ser importado seja um caractere alfa será solicitado o código correspondente, ou seja, se a máscara é numérica e o código a ser importado é A00001, ao informar como código correspondente ao A o número 9, todos os insumos que possuam esse caractere nessa posição, terão o A substituído por 9. O contrário também pode ocorrer. A máscara pode ser definida com caracteres alfa e o código a ser importado ser um caractere numérico.

Modelos de Taxas: Copia taxas a partir do modelo de taxa selecionado de um projeto global para o projeto corrente. Para esse tipo de cópia o projeto origem deve ser sempre um projeto global. Caso não seja, essa pasta fica desabilitada.

Modelo de Taxas copiados para o Projeto destino irão para os Parâmetros do Projeto na Pasta Cálculo / Taxas.

Obs.: Somente serão copiadas as taxas que não tem sua descrição e tipo no projeto destino.

Segurança:  
O usuário só poderá realizar as Cópias de Itens de Coligadas que ele tenha permissão de acesso, e Projetos que sejam do tipo Modelo ou que também tenha permissão de acesso, definidos cadastro de usuários.

[Unidade de Serviço](https://tdn.totvs.com/pages/viewpage.action?pageId=679169991)

**Design Thinking Cópia de Itens.**  
Aplicação da metodologia de Desing Thinking da TOTVS no processo de Cópia de Itens, de forma que o mesmo se torne mais ágil em relação à definição dos itens que deverão ser copiados e todas as suas respectivas configurações.

**Três novas abas na tela do processo:** **Cópia Simplificada:**

Permite a cópia de todo o projeto desejado de forma simplificada, sem distinção de itens por entidade. Estarão disponíveis apenas as entidades que deverão ser copiadas e não os itens de cada uma; A possibilidade de cópia da Planilha de Serviços somente estará disponível se o parâmetro de projeto "Utiliza Planilha de Serviço" do projeto origem estiver marcado;

**Cópia Detalhada:**

Possui todas as funcionalidades de cópia detalhada: Na aba de cada entidade (Sub-Projetos, Tarefa, Composições, etc.) é exibido quais entidades estarão relacionadas com a cópia; Na barra de cada visão das respectivas entidades existe uma nova opção de filtro que permite com que os itens a serem copiados, possam ser filtrados por código utilizando a vírgula ou a quebra de linha como separadores.

**Cópia por Planilha:**

Possibilita uma cópia (importação) a partir de uma planilha em Excel para as planilhas de atividade e(ou) serviço: A coligada e projeto são necessários para a realização da importação e cópia; É possível selecionar o cenário no qual receberá a importação, este somente estará habilitado se o parâmetro de projeto "Utiliza Cenários" estiver marcado; É possível selecionar duas planilhas Excel, uma para cada tipo de planilha do projeto, porém para a Planilha de Serviços somente será possível definir o arquivo se o projeto fizer utilização da mesma (parâmetro de projeto "Utiliza Planilha de Serviço"); A importação em Excel depende de um layout pré-definido e para isso será disponibilizado o layout semelhante ao processo de importação de tarefas considerando, também, as preferências de usuário salvas anteriormente no processo; Ao solicitar a cópia a partir das planilhas, primeiramente será verificado a existência dos recursos (composições e insumos) do arquivo em relação ao projeto origem pré-definido, então, a cópia será realizada e em seguida, a importação das tarefas existentes nas respectivas planilhas; Nessa opção de cópia o usuário terá a possibilidade de também copiar os parâmetros do projeto origem, selecionando a opção "Copiar parâmetros do projeto origem".

**Processo de Importação de Tarefas em Excel**

Permite a importação da Planilha de Serviços e uma nova opção que permite o vínculo do serviço a atividade, sendo que o mesmo somente será considerado ao importar a planilha de atividades. A possibilidade de cópia da Planilha de Serviços somente estará disponível se o parâmetro de projeto "Utiliza Planilha de Serviço" do projeto estiver marcado.

**Melhorias para Mercado Internacional Calculo por Rendimento Diário.**  
Disponível somente para o mercado internacional, para licitações públicas que exigem o detalhamento dos serviços (composições) por rendimento.  
Ao realizar a cópia de composições do tipo "por Rendimento" o sistema realiza a cópia das informações de jornada, rendimento de mão de obra e equipamento.

Ao copiar **Grupos de Custo, Insumos e Tarefas** de uma coligada pra outra, se a Coligada da Natureza Orçamentária informada no cadastro for global, isto é, código da Coligada igual a zero, mantém no registro se não for Global, será verificado se o código existe na Coligada destino, se sim, será alterada a Coligada da Natureza do registro, se não uma mensagem de erro será emitida, abortando o processo.
