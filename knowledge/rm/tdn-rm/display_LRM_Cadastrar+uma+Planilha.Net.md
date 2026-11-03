---
content_hash: 041c7492fc84c284016a1856e9885a7015d86ce242183cb8ee6ca187816146d7
fetched_at: '2026-06-29T00:10:58.311121+00:00'
page_id: '60523214'
product: rm
source: tdn-rm
title: Cadastrar uma Planilha.Net
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastrar+uma+Planilha.Net
version: 90
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Planilhas .NET                        **Versão:**11.80 |
| **Processo** | **:** | Manipulação de Planilhas .NET |
| **Subprocesso** | **:** |  |
| **Data da publicação** | **:** | 02/07/2014 |

## **PLANILHAS .NET**

### **O que é planilha .NET ?**

Planilha.Net é um recurso disponível no ERP da Linha RM que possibilita a criação de planilhas. Este recurso consegue ler as informações da base de dados e trazê-las para a planilha alinhando com os recursos do Pacote Office, disponíveis pela Microsoft.

false

*A partir da versão **12.1.23 não será mais possível o uso da Planilha.Net como RMPart nos Cenários**. Permanecendo a inclusão de [Planilhas RM](http://tdn.totvs.com/x/MceFDg) somente.*

---

### **Como cadastrar uma planilha .NET ?**

Para cadastrar uma Planilha, acesse o módulo Planilhas.Net no menu **Gestão,** acessando o ERP pela MDI.NET.

Com a visão Planilha.Net carregado, clique no ícone**NOVO**para inserção de uma nova planilha.Net. O sistema apresentará os campos disponíveis para o Cadastro de Planilhas.

### **Funcionalidades de cada campo**

**Nome da Planilha .Net**

Neste campo deve ser informado um nome para a Planilha. Ex.: Listagem dos Funcionários, Listagem das Funções, etc.

**Tipo da Planilha Net**

**Excel:**O sistema irá criar uma planilha a partir do Microsoft Office. Nesta opção é possível utilizar todas as funcionalidades do Microsoft Excel.

**Planilha RM:**Evolução da antiga planilha RM(Delphi). Com opções limitadas de funções se comparada com a versão original do Microsoft Office, porém sem necessidade de licença da Microsoft para uso.

Para habilitar Tipo da Planilha Net **Excel,** Acesse: Parâmetros Globais > Planilha Net e marque a flag "**Utilizar Planilhas Excel**":

**Observação**

Neste campo deve ser informado alguma observação sobre a Planilha. Ex.: Para que a planilha seja executada com sucesso é necessário ter todos os funcionários devidamente cadastrados.

**Grupo de Planilhas**

Neste campo deve ser informado a qual grupo a planilha cadastrada pertencerá. É necessário criar o grupo de planilha, logo após definir o nível de acesso para o grupo criado.

**Observação :**É importante ressaltar que uma vez definido o grupo corretamente, podemos criar regras para este grupo. Ex.: Restringir o acesso de alguns usuários a determinados grupos de planilhas, desta forma, podemos controlar quem poderá visualizar/editar os dados da planilha.

**Nível de Acesso**

Neste campo devemos definir o Nível de Acesso da Planilha. Quando cadastramos um perfil no menu **Segurança**, opção **Perfis**, em **Serviços Globais,**acessando pela nova .MDI, temos a possibilidade de permitir a edição ou a visualização de planilhas através dos campos **Nível de Alteração** e **Nível de Emissão**.

Se no Perfil for cadastrado, Nível de Alteração = 5, Nível de Emissão = 10 e na Planilha o Nível de Acesso = 10. Significa que, o usuário poderá visualizar a planilha, mas não poderá alterar sua estrutura, visto que o nível de alteração é menor que o nível de acesso.

**Planilha Mestre:** Neste campo devemos definir se existe uma Planilha Mestre para a Planilha que está sendo cadastrada. Funciona como uma árvore de planilhas. Ex.: Podemos ter a seguinte estrutura:

**Carregar Planilha Existente:** Neste campo devemos definir se a Planilha que está sendo cadastrada vai ser carregada através de uma outra planilha já existente no computador.

Com o Cadastro devidamente preenchido, podemos clicar em **Salvar** e posteriormente em **OK**. A planilha será salva no Banco de Dados.

Após salvar, podemos iniciar a inserção dos dados. Para isto clique duas vezes sobre a planilha cadastrada para que seja carregado a mesma para o Excel.

Atenção

Caso a planilha não abra é necessário executar o RM.exe como administrador pois ele irá fazer o registros no windows das dll's dsofile.dll e dsofile64.dll que são necessárias para rodar a planilha.net Excel.

---

Ao carregar a planilha temos o ambiente do Excel juntamente com as opções do ERP, que são os itens **Configurações,** **Consulta SQL** e **Gráficos**.

### **Funcionamento de cada item**

|  |  |
| --- | --- |
|  | * **CONFIGURAÇÕES**   **Informe um número ou texto:** Neste campo deverá ser informado um valor default para quando a sentença SQL retornar um dado vazio, ou seja se por ventura ocorrer a pesquisa por um registro e o mesmo não for encontrado, o que for preenchido neste campo “**Informe um número ou texto**”, substituirá o resultado em “branco”. Por padrão, quando a sentença SQL retorna algum dado vazio é exibido o seguinte texto na célula “Nenhum Registro Encontrado”.    **Cor da Célula Chave:** Quando selecionado esta opção será possível definir cores para as células chaves **Primary Key** . Exemplo: Célula Chave é a célula aonde foi inserida uma sentença SQL.  **Cor da Célula de Parâmetro:** Quando selecionado esta opção será possível definir cores para as células de parâmetros. Ex.: Célula de Parâmetro é a célula aonde a sentença SQL lê um parâmetro.    **Todas as Planilhas:** Quando selecionado esta opção, todas as planilhas serão recalculadas automaticamente na inicialização, caso a opção **Recalcular automaticamente na inicialização** estiver selecionada ou através do clique no botão Recalcular.  **Planilha Ativa:** Quando selecionado esta opção a planilha ativa será recalculada automaticamente na inicialização, caso a opção **Recalcular automaticamente na inicialização** estiver selecionada ou através do clique no botão Recalcular.    **Redimensionar células importadas automaticamente:** Quando selecionado esta opção, a célula será redimensionada para o tamanho do campo retornado pela sentença SQL automaticamente.  **Exportar dados a partir da célula selecionada:**Quando selecionado esta opção, o sistema entenderá que a inserção de consultas SQL deverá ocorrer na célula que estiver selecionada. Caso esta opção estiver desmarcada, o sistema carregará os dados da sentença SQL na Célula A1.  **Exibir títulos de colunas:** Quando selecionado esta opção, será exibido na planilha o título das colunas que estão contidos na tabela que foi executado a sentença SQL.  **Usar formatação padrão para o título das colunas:** Quando selecionado, formatará o título das colunas retornado pela sentença SQL, com Bordas e Sombreamento. |

|  |  |
| --- | --- |
|  | * **CONSULTAS SQL**   Através deste item que vamos carregar as informações na Planilha. Deverão ser inseridas as sentenças SQL desejadas para visualização dos dados.  **Consultas SQL selecionadas:** Neste campo deverão ser inseridas as sentenças SQL que vão compor a planilha.    **Detalhes da Consulta Selecionada:** Neste campo deverão ser selecionados os campos da sentença SQL a serem adicionados na Planilha. Clicando-se em **[\*]** todos campos, registros contidos serão adicionados à planilha.    **Parâmetros:** Neste campo deverá ser inserido qual é a célula que sentença SQL deverá ler um determinado valor (parâmetro).  Ex: Foi cadastrado a seguinte sentença SQL:  **SELECT CHAPA, NOME, SALÁRIO FROM PFUNC WHERE CHAPA = :PLN\_$D$5**  Note que a sentença SQL está aguardando um valor para retornar os dados. O parâmetro PLN\_$D$5 será substituído pelo valor da Célula D5. Célula está definida no campo Valor.      **Dados Importados:** Esta opção nos ajuda a localizar os dados retornados por uma sentença SQL. Clicando no campo **Chave** o sistema exibira em qual célula foi inserida a sentença SQL. Clicando em **Planilha**, o sistema exibirá em qual planilha a sentença SQL foi inserida. Clicando em **Intervalo**, o sistema exibirá o espaço ocupado pela sentença SQL na planilha. |

|  |  |
| --- | --- |
|  | * **GRÁFICOS**   Através deste item podemos inserir gráficos nas planilhas. Os gráficos são carregados através da leitura das sentenças SQL.  **Gráficos Inseridos:** Através desta opção vamos inserir as sentenças SQL e configurar a exibição do Gráfico.    **Tipo do Gráfico Selecionado:** Através desta opção vamos mudar o tipo do gráfico selecionado. Ex.: Se for criado um gráfico de Barras e deseja-se mudar para coluna, não é necessário excluir o Gráfico e fazer novamente. Basta clicar no tipo desejado que o gráfico será alterado na Planilha. |

---

### Inserindo uma planilha que lê dados de uma sentença SQL

|  |  |
| --- | --- |
|  | Para inserir uma sentença SQL na planilha, clique na Seção **Consulta SQL**.    Com as opções desta seção carregadas, clique para inserir uma consulta SQL.     Selecione a SQL pelo botão **exibir árvore** ou pelo campo **código da sentença SQL**.    Após seleção da sentença SQL, clique em **OK** para associar a sentença SQL a planilha. |

|  |  |
| --- | --- |
|  | Com a sentença SQL associada a Planilha, necessitamos escolher quais os campos da SQL serão inseridos na Planilha. Para isso, selecione os campos desejados, ou clique em [\*] para inserir todos.     Posteriormente, clique para que os dados retornados pela SQL sejam adicionados na Planilha.    Note que a planilha foi carregada com os dados da sentença SQL. A planilha já está formatada, visto que foram utilizados os recursos do Office. Este é um exemplo do uso das funcionalidades do ERP da TOTVS e do Office em uma mesma interface. |

---

### **Inserindo um Gráfico na Planilha**

|  |  |
| --- | --- |
|  | Para inserir um Gráfico na planilha, clique na Seção **Gráficos**.    Com as opções desta seção carregadas, clique no ícone **Inserir.**    Selecione a SQL pelo botão **exibir árvore** ou pelo campo **código da sentença SQL**.    Clique no botão **Próximo**.    Selecione o **Tipo de Gráfico.**    Clique no botão **Próximo**.    Selecione os campos da Entrada de Legenda (**Eixo X**) e Entrada de Valor **(Eixo Y) .**    Clique no botão **Próximo**.    Configure as opções do Gráfico e clique em **OK.**    Após cadastrar as opções do Gráfico, o mesmo é carregado dentro planilha |

**Informações Adicionais**

A Planilha.Net traz uma série de recursos que aumentam produtividade e diminuem o tempo para realização das tarefas, além de integrar em uma mesma interface recursos do ERP e do Microsoft Excel.

---

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
