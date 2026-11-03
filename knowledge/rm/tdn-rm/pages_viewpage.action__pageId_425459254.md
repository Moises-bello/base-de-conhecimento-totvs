---
content_hash: 39d2462a989bd876fefdcdfa5e17f42f97855df5d19c31e30fe84596789b44e7
fetched_at: '2026-06-29T00:09:34.829331+00:00'
page_id: '425459254'
product: rm
source: tdn-rm
title: TOTVS Gestão Bibliotecária - Especificações Técnicas 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459254
version: 4
---

**Apresentação**  
   
Este documento tem como objetivo, discriminar as principais características técnicas do TOTVS Gestão Bibliotecária, permitindo a você obter uma melhor compreensão de seu funcionamento e conseqüentemente, aproveitar seus recursos e benefícios.  
O TOTVS Gestão Bibliotecária visa administrar as diversas funções de bibliotecas, arquivos, acervos, locadoras, entre outros. O sistema permite o cadastramento de publicações (livros, revistas, apostilas, jornais e todos os tipos de impressos), CDs, filmes, fitas K-7 e de vídeo, discos etc. Os materiais são classificados por categorias, grupos e tipos de publicações. O TOTVS Gestão Bibliotecária oferece um cadastro completo dos usuários e controla todo o processo de empréstimo, devolução e reserva das obras que compõem o acervo da biblioteca. O sistema possui ainda um controle de prioridade de leitura sobre os exemplares do tipo de publicação periódicos cadastrados no sistema, onde, a cada exemplar recebido o sistema faz reservas para as pessoas que possuem prioridade de leitura sobre o exemplar.  
   
**1. Características do RM**  
O RM é a solução corporativa de gestão empresarial da TOTVS. Desenvolvido para tecnologia Windows 32 bits e arquitetura Cliente/Servidor, possui banco de dados único, padrão SQL Structure Query Language (Linguagem de Consulta Estruturada), atualizações on-line, interface padronizada e diversas ferramentas disponíveis. Flexível, possibilita a integração com sistemas específicos de sua empresa  
   
**Arquitetura Cliente/Servidor**  
·         Arquitetura Client-Server que permite distribuição de processamento entre a estação cliente e o servidor de banco de dados SQL.  
·         Possui base de dados centralizada, podendo ser acessada simultaneamente por dois ou mais dos módulos que integram o Sistema Corporativo.  
·         A base de dados padrão SQL permite a utilização de geradores de relatórios de terceiros como um complemento ao gerador do próprio sistema.  
·         Desenvolvido em Borland Delphi â 32 Bits e Visual Studio 2008 C#.Net, para plataformas Microsoft Windows (vide tópico Portabilidade).  
·         Plataforma mínima para estação cliente (estação de trabalho) – (Vide Tópico Arquitetura).  
·         Plataforma mínima para o servidor de dados (vide tópico Arquitetura).  
·         Possui modelo de processamento na arquitetura Cliente/Servidor e WEB.  
·         Possui compatibilidade com banco de dados ORACLEâ (vide detalhes no tópico Portabilidade).  
·         Trata-se de uma aplicação com todos os módulos integrados, a base de dados é compartilhada com outros aplicativos.  
·         Possibilita a exportação e importação de dados para/de outros sistemas, através da definição de layouts especiais, mantendo a integridade dos mesmos.  
·         Baseia-se no conceito de transações, mantendo a integridade do Banco de Dados em quedas de energia e falhas de software/hardware.  
   
**Interface Padrão Windows**  
·           Possui atualização on-line dos dados de entrada, permitindo acesso às informações atualizadas imediatamente após o término da transação.  
·           Possui padronização do uso de teclas e funções, em todos os módulos, de forma a facilitar o seu aprendizado e operação.  
·           Possui opção de "fazer" e "desfazer" as ações executadas pelos aplicativos.   
·           Exemplo: inclusão de requisição de material e estorno de requisição de material; inclusão e exclusão e/ou estorno de lançamento; inclusão e exclusão de conta contábil, etc.  
·           Apresenta todas as telas e relatórios no ambiente do usuário em português.  
   
**Ajuda On-line Sensível à Opção**  
·       Possui documentação técnica do sistema em português, através de dispositivo de Ajuda On-Line com orientação detalhada (passo a passo) de como utilizar o aplicativo, bem como os itens de menu e o preenchimento das telas de Ajuda On-line dos campos, opções e erros no padrão Windows.  
   
**2. Natureza Funcional do TOTVS Gestão Bibliotecária**

**Este produto possui as seguintes características técnicas:**  
·           Permite controlar acessos ao sistema através do login em uma Filial e Unidade de trabalho, que o usuário do sistema terá que fazer para ter acesso aos menus do sistema.  
·           Permite controlar o acesso também para os usuários da biblioteca, cada usuário deverá ter acesso a uma Filial e Unidade.  
·           Controla os acervos compostos por qualquer tipo de publicação (livros, periódicos, vídeos, documentos, cd's, etc), seja particular ou público.  
·           Permite efetuar pesquisas rápidas das publicações do acervo, inclusive via Internet.  
·           Na tela de visão do Usuário (Cliente) pode-se visualizar o responsável financeiro.  
·           Permite cadastrar autores, assuntos e editoras.  
·           Possibilita que o usuário defina a quantidade de exemplares a serem emprestados simultaneamente.  
·           Permite informar se o usuário de um determinado tipo possui ou não data de validade.  
·           Permite a criação de regras de empréstimo, combinando os vários grupos de publicação com cada tipo de usuário da biblioteca, permitindo estabelecer a duração do empréstimo, as multas por atraso, validade de reservas, permissão para renovação e bloqueio de empréstimo para usuários em atraso.  
·           Permite a inclusão e manutenção nas tabelas auxiliares que são utilizadas nos cadastros de Publicações, Exemplares e afins.  
·           Possibilita o cálculo automático da localização do exemplar (Número Cutter) que é formado pela primeira letra em maiúsculo do sobre nome do autor, número de referência (número com maior aproximação do sobre nome do autor) e por último a primeira letra em minúsculo do título da publicação.  
·           Permite definir qual o tipo de referência ao autor deve ser utilizada, Cutter, PHA ou Livre.  
·           Permite que o usuário defina o número máximo de exemplares por tipo de publicação.  
·           Possibilita que o usuário não cobre multa de atraso sobre dias não úteis.  
·           Possibilita na regra de empréstimo a opção de empréstimo por hora.  
·           Permite pesquisar os dados das reservas feitas pelos usuários.  
·           Permite fazer uma reserva utilizando filtros, seja por Volume, Edição e Ano.  
·           Possibilita o acompanhamento das reservas pela fila de reserva.  
·           Possibilita o acompanhamento e cancelamento de uma reserva via Internet.  
·           Permite bloquear reservas para usuários em atraso.  
·           Possibilita cancelar um empréstimo através da janela de devolução.  
·           Permite bloquear empréstimos para usuários inadimplentes.  
·           Permite a renovação de um exemplar.   
·           Permite bloquear a renovação para usuários em atraso.  
·           Possibilita gerar relatórios de acordo com as necessidades dos clientes.  
·           Permite atualizar a situação de empréstimo e devolução dos usuários do TOTVS Gestão Bibliotecária.  
·           Permite verificar a situação atual de empréstimos, devoluções e reservas dos usuários.  
·           Possibilita controlar a situação atual de um determinado exemplar através do seu código ou número do tombo.  
·           Permite consultar a situação financeira dos usuários.  
·           Permite o controle de datas previstas para recebimento dos exemplares de periódicos.  
·           Possibilita a consulta das assinaturas prestes a vencer.  
·           Prioridade de leitura dos exemplares de periódicos recebidos pelo sistema.  
·           Permite a pesquisa do acervo bibliotecário através de dados como título, assunto, autor, editora, ano, entre outros.   
·           Permite pesquisar o acervo bibliotecário através de pesquisa exata, pesquisa por palavra e contendo.  
·           Permite exibir o resultado da pesquisa em forma de árvore, ficha ou no padrão ABNT.  
·           Possibilita personalizar os e-mails enviados pelo sistema.  
·           Permite o envio de e-mail informando sobre a liberação de uma reserva.  
·           Permite a visualização dos autores e dos assuntos relacionados ao artigo.  
·           Permite a normalização automática ao incluir um novo autor.  
·           Permitir abonar multa para devoluções em atraso.  
·           Permite editar os perfis disponíveis através do assistente e alterando os acessos desejados para o RM Portal.  
·           Possibilita o envio de e-mail lembrando os usuários sobre as devoluções pendentes e/ou a fazer.  
·           Permite o envio de e-mail com texto livre para os usuários da biblioteca, o envio poderá ser feito para um determinado tipo de usuários.  
·           Permite a transferência de exemplares entre as filiais e unidades cadastrados no sistema.  
·           Permite à importação das tabelas de assunto, autor, publicação, exemplar, usuários entre outros.  
·           Permite verificar através do sumário, os conteúdos da publicação.  
·           Permite importar as imagens das publicações.  
·           Possibilita exportar dados através do gerador de relatórios.  
·           Permite utilizar o leitor óptico para fazer empréstimo e devolução de exemplares.  
·           Permite consultar no momento do empréstimo através de um link, a quantidade de exemplares que o usuário tem em seu poder. Tal link presta acesso a uma tela de visão onde possui informações sobre dados dos exemplares que estão em poder do usuário.  
·           Permite a utilização de senha para liberação do empréstimo.  
·           Permite alterar o prazo de devolução de um exemplar no momento do empréstimo ou da renovação deste.  
·           Permite que sejam cadastrados vários exemplares de uma única vez, basta informar os dados iniciais (número de exemplares a serem cadastrados, número do tombo inicial, número do exemplar).  
·           Possibilita o cadastro da área e subárea do conhecimento conforme tabela do CNPq.  
·           Possibilidade do controle de duplicação de registros. Impede que Autores, Coleção/série, Editora, Idioma e Local de Publicação sejam cadastrados em duplicidade.  
·           Possibilidade dos principais cadastros do sistema serem feitos sempre em maiúsculo. Através de parâmetros.  
·           Sugestão de compra de novos títulos para compor o acervo.  
·           Inclusão de campos complementares para os cadastros de Publicação, Exemplar e Usuário.  
·         Permite o cadastro de remissivas para autor, editora e assunto.  
·         Permite a visualização de alguns campos no padrão MARC21. Tags 008, 035, 040, 041, 090, 245, 250, 260, 300 e 650.   
·         Permite importar registros bibliográficos e catalográficos através do Assistente de importação padrão MARC21. Tags 020, 041, 080, 082, 090, 100, 110, 111, 130, 240, 245, 250, 260 e 300.  
·         Permite por meio da instalação do scanner de biometria digital Sensor U.are.U Fingerprint Reader da DigitalPersona, o registro e identificação da impressão digital de cada usuário.   
·         Permite considerar apenas dias úteis nos empréstimos.  
·         Permite escolha o tratamento que o sistema dará no caso de lançamentos que vencem em dias não úteis.  
·         Permite configurar as opções de saída de impressão de recibos.   
·         Permite configurar a utilização da impressora não fiscal bematech para emitir recibos de empréstimos, devoluções, renovações e multas.  
·         Permite a impressão de recibos de Empréstimo e Devolução via Gerador de relatórios.   
·         Permita cadastrar o título da publicação, nome do autor, descrição do assunto, descrição da categoria e descrição do grupo de publicação com letra maiúscula.  
·         Presta a opção de adiar o cancelamento de usuários expirados.  
·         Permite utilizar senha para empréstimo.  
·         Permite liberar circulação de exemplares bloqueados.  
·         Permite alterar data de devolução maior do que o definido na regra.  
·         Permite escolher um tipo de código de usuário como padrão no empréstimo.  
·         Permite liberar reservas para usuários com devolução em atraso.  
·         Permite inventariar acervo.  
   
**Integração com TOTVS Gestão Financeira**  
·         Permite gerar os lançamentos para empréstimos e multas.  
·         Permite inserir o percentual de juros que será cobrado por dia de atraso.  
·         Permite inserir o número de dias para o vencimento das cobranças, a partir da data da cobrança.  
·         Permite selecionar o evento contábil default para inclusão de lançamentos.  
·         Permite selecionar o evento contábil default para baixa de lançamentos.  
·          Permite selecionar a conta caixa, o tipo de documento, o tipo contábil e o histórico que serão utilizados no lançamento.  
·         Permite bloquear empréstimo e reservas para inadimplentes do TOTVS Gestão Bibliotecária.   
·         Permite bloquear empréstimo e reservas para inadimplentes do TOTVS Educacional.  
   
**Integração com TOTVS Educacional**  
·           Permite bloquear empréstimos e reservas para alunos que não estão matriculados em nenhuma disciplina.   
·           Permite verificar documentos pendentes ao realizar o empréstimo para aluno.  
·           Permite importa os alunos e professores como usuários do TOTVS Gestão Bibliotecária.  
   
**Integração com TOTVS Folha de Pagamento**  
·         Permite bloquear alteração de dados cadastrais de usuários provenientes do TOTVS Folha de Pagamento.  
·         Permite importar os funcionários do TOTVS Folha de Pagamento como usuários do TOTVS Gestão Bibliotecária.  
·         Permite liberar empréstimos e reservas para funcionários demitidos nos parâmetros de integração com o Labore.  
   
   
 **Integração com TOTVS Gestão de Estoque, Compras e Faturamento**  
   
        ·      Permite solicitar compras de exemplares.  
   
        ·      Permite controlar as políticas de aquisições da biblioteca.   
   
        ·      Permite maior controle dos exemplares solicitados e exemplares pendentes.  
   
   
   
**3. Limitações**  
   
**Limitações Técnicas**  
·         A importação de dados deve seguir um padrão descrito na ajuda do sistema, para que o processo seja feito de forma correta. Se este padrão não for seguido, a importação de dados não será efetuada.  
   
**Limitações de Performance**  
·         A performance do aplicativo depende do banco de dados utilizado e da quantidade de registros cadastrados. Até agora, não houve nenhuma limitação detectada.  
   
   
**4. Estrutura das Tabelas**  
·         As entidades manipuladas no aplicativo estão dispostas em diversas tabelas que classificamos de Tabelas Globais e Tabelas Específicas.   
·          As Tabelas Globais são aquelas tabelas comuns a todos os segmentos da Linha RM, sendo, portanto manipuláveis por todos os segmentos;  
·         As Tabelas Específicas do segmento são aquelas que se encontram disponíveis no segmento, embora possam ser encontradas também compartilhadas entre outros segmentos da Linha RM, visando garantir a integração entre os segmentos.   
A criação de novas entidades e/ou atributos deverá ser efetuada exclusivamente pela própria TOTVS. Caso necessário, o cliente deverá encaminhar solicitação de inclusão de entidades/atributos ao Depto. de Suporte da TOTVS Sistemas para que a mesma seja encaminhada ao Departamento de Desenvolvimento para avaliação.  
   
  
**5. Implantação**  
A Área de Serviços da TOTVS visa implantar os seus produtos de acordo com os processos de cada cliente.   
Finalizada a negociação comercial, é realizado o levantamento de processos para compreender as regras do negócio do cliente e verificar se os aplicativos RM atendem às suas necessidades. Os analistas de processos são responsáveis por documentar todos os detalhes dos processos para garantir que o escopo do projeto considere todos os possíveis pontos críticos do projeto, seguindo o padrão proposto pela metodologia de implantação da TOTVS. O cliente valida os processos levantados e o gerente de projetos TOTVS apresenta o cronograma e o projeto de implantação, que informa a programação de tarefas a ser seguida para o sucesso do projeto.   
Durante a execução do projeto são realizadas reuniões de avaliação para garantir o custo e o prazo estipulados projeto. Todos os processos implementados pelos consultores de implantação TOTVS são simulados e validados pelo cliente. Testes integrados também garantem os resultados da implantação de vários módulos associados. Finalizado o período de parametrização e testes, os sistemas entram em produção e são acompanhados na fase inicial. Encerrado o projeto, o cliente assina um termo que formaliza a conclusão das tarefas e o cliente é encaminhado ao Suporte para futuros atendimentos em caso de dúvidas.  
   
   
**Instalação do gerenciador de banco de dados – SGDB**  
Deve ser providenciada, caso ainda não tenha sido realizada, instalação do gerenciador de banco de dados de preferência da empresa, conforme a necessidade, e que já se encontre instalada em outros equipamentos ou servidores: SQL e Oracle (vide versão do gerenciador no tópico Portabilidade)  
Instalação da base de dados dos aplicativos RM.

**Instalação dos Aplicativos RM**  
Primeiramente devem ser instalados os outros aplicativos RM. Através da execução dos processos internos desses aplicativos, a base de dados será alimentada com as informações com as quais o RM Bis poderá utilizar para a geração dos cubos de decisão.  
   
   
**6. Ferramentas de Suporte**  
   
As ferramentas de suporte são funcionalidade que servem de apoio para que uma determinada funcionalidade complete seu processamento. Este comportamento pode ser encontrado em várias situações na linha RM, e são imprescindíveis para determinados processos.  
   
**Fórmula**  
   
As Fórmulas nos aplicativos RM terão, basicamente, três principais objetivos, dentre eles:  
-Seleção (restrição da aplicabilidade de alguma operação).

* Definição da forma de cálculo de eventos específicos, inclusive do tipo "base de cálculo", que servem de referência para outros cálculos.
* Relacionamento de valores entre os eventos.  
  O editor de fórmulas possui um campo de texto para que você monte as estruturas das fórmulas. Usando o editor de fórmulas, as funções e comandos desejados para a criação da fórmula serão movidos para o campo de texto, bastando clicar duas vezes sobre as opções função, comando ou parâmetro.   
  Principais características:  
         ·          Permite através de um editor criar fórmulas no sistema  
         ·          Permite a aplicação em campos complementares  
         ·          Permite seu uso em consultas SQL  
         ·          Possibilita aplicação em relatórios do sistema  
         ·         Permite uso em processos do RM  
         ·        Possibilita exportação do log de execução  
     
     
  **Fórmula Visual**  
     
     
  Fórmula visual trata-se de uma funcionalidade que executa um fluxo de operações pré-definidas. O fluxo é definido pelo próprio usuário, que através desta ferramenta é capaz de atender diversas particularidades.   
  Principais características:  
        ·        Permite a escolha de atividades pré-definidas no RM ou mesmo acrescentar novas atividades  
        ·        Permite através de um editor visual criar com fluxos de ações  
        ·        Permite a escolha de atividades pré-definidas no RM ou mesmo acrescentar novas atividades  
        ·        Permite a customização das funcionalidades do RM a partir das atividades disponíveis  
        ·        Permite definir em qual momento a fórmula visual será executada, a partir da manipulação de gatilhos  
        ·        Permite o agendamento de uma fórmula visual a partir do agendamento de Jobs.  
     
  **Mashups**  
     
     
  A idéia do Mashup é utilizar uma pesquisa na Web para atualizar dados cadastrais ou simplesmente fazer uma busca.  
  Principais características:
* Realiza a pesquisa de dados na Web para realizar a atualização de cadastros no RM
* Verifica a existência e a autenticidade de um dado como CPF, CNPJ, CEP, entre outros dados diretamente na internet a fim de possibilitar o cadastro de um registro.  
     
  **Metadados**  
     
  O metadados é um mecanismo que possibilita a geração automática de formulários para cadastramento de informações no banco de dados, a fim de dispor de novos cadastros para o RM.  
  Principais características:  
  Permite a criação de formulários customizados que realizam gravação na base de dados, também em tabelas customizadas.  
  Possui interface de manipulação que permite criação de ferramentas que serão disponibilizadas no módulo de Globais, garantindo a entrada de dados na estrutura de metadados através de uma interface simples e amigável, exigindo o mínimo de esforço do usuário final.  
  Possui mecanismo capaz de exportar e importar informações de uma estrutura de metadados, permitindo compartilhar dados de uma base para outra  
  Possui mecanismo que permita uma sincronização entre servidores de aplicação em cluster e os clientes distribuídos da aplicação com a finalidade de manter as versões compatíveis de execução de um projeto de metadados.  
  **7. Ferramentas de Saídas**  
     
  **Gerador de Relatórios**  
  ·           Os relatórios são criados e formatados nos aplicativos da Linha RM através do recurso Gerador de Relatórios, que é baseado na arquitetura Win32.  
  ·           Principais características:  
  ·           Possibilita a exclusão dos relatórios executados através de agendamento conforme uma periodicidade.  
  ·           Possibilita a exclusão de relatórios em bloco.  
  ·           Admite a inclusão de linhas em branco em um relatório do tipo arquivo bancário  
  ·           Permite a criação de relatórios, podendo definir níveis de acesso a esses relatórios.   
  ·           Os relatórios criados podem ser de saída padrão (formato próprio), Texto, RTF, PDF ou Arquivo Bancário (exportação de dados).  
  ·           Permite a visualização de relatórios em uma ou mais coligadas.  
  ·           Permite que todos os relatórios possam ser gerados em vídeo, impressora ou arquivo, com parametrização de páginas inicial e final, bem como número desejado de cópias, entre outras opções.  
  ·           Permite a importação/exportação de um ou mais relatórios.  
  ·           Permite a cópia da estrutura de um relatório, gerando um novo relatório com essa estrutura.  
  ·           Permite a visualização do relatório antes da impressão.  
  ·           Permite gravar última configuração de impressão utilizada.  
  ·           Permite a criação de grupos de relatórios.  
  ·           Permite a cópia dos relatórios entre coligadas  
  ·           Permite montar e alterar relatórios facilmente através de uma interface amigável. Além disto, será possível:  
  ·           Inserir grupos como Cabeçalho e Rodapé de Página, Linha Detalhe, Cabeçalho e Total de Detalhe, Total de Página, Capa e Total de Relatório;  
  ·           Visualizar os grupos de forma hierárquica facilitando a compreensão do relatório;  
  ·           Inserir campos da base de dados, imagens, textos, fórmulas, expressões, consultas SQL, Stored Procedure, data, hora e contador de páginas no relatório;  
  ·           Visualizar, através de uma régua, o posicionamento dos campos no papel;  
  ·           Mover e copiar campos do relatório;  
  ·           Copiar a formatação de um campo;  
  ·           Selecionar registros a serem impressos (incluir filtro);  
  ·           Alterar a formatação do campo como fonte, borda, formato de impressão e etc.;  
  ·           Determinar campo de ordenação e quebra do grupo;  
  ·           Marcar grupos que não serão impressos dentre outras funcionalidades  
     
  **Planilhas**  
  ·         As Planilhas dos aplicativos RM possuem uma estrutura semelhante à estrutura das planilhas do MS Excel. Pode conter várias pastas para que o usuário possa organizar vários tipos de relatórios num único arquivo.  
  **Principais características:**  
  ·         Permite a criação de planilhas eletrônicas.  
  ·         Permite a inclusão de novas pastas.  
  ·         Permite inserir sentenças SQL para obter informações da base de dados, através de uma interface amigável para a construção dessas sentenças, inclusive com passagens de parâmetros que podem referencias células da própria pasta ou de outra.  
  ·         Permite inserir Stored Procedures.  
  ·         Permite a inclusão e formatação de gráficos.  
  ·         Permite a formatação dos dados da planilha, como tamanho, cor, número de casas decimais, borda e etc.  
  ·         Permite a cópia da formatação de uma célula para outra.  
  ·         Permite mover e copiar dados de uma célula para outra, inclusive as sentenças SQL e Stored Procedures.  
  ·         Permite inserir e excluir linhas/colunas da planilha.  
  ·         Permite inserir várias funções, como por exemplo, a função SUM para o somatório de uma faixa de dados.  
  ·           Permite a exportação/importação da planilha, como por exemplo, para o MS-Excel.  
  ·           Permite a impressão de parte da planilha (uma ou várias pastas ou mesmo parte de uma pasta).  
  ·           Permite a impressão de uma ou várias planilhas ao mesmo tempo.  
     
  **Cubos**  
  Através dos Cubos é possível realizar uma consulta em toda a base de dados dos aplicativos RM proporcionando a customização da análise e a criação de planilhas e relatórios gerenciais.   
  Principais características:  
  ·           Permite as visualizações de Cubos.  
  ·           Permite a impressão de Cubos.  
  ·           Permite a exportação do cubo para o MS-Excel.  
  ·           Permite a visualização de gráficos.  
  ·           Permite a exportação e importação de arquivos de Cubos.  
  ·           Permite a edição dos parâmetros dos cubos que os possuem.  
  ·           Permite a validação de senhas dos cubos que as possuem.  
     
  **Gráficos**  
  Os gráficos são resultado do processamento de uma fonte de dados e sua exposição por meio de diversos tipos de gráficos.  
  Principais características:  
  ·         Permite programar alertas via e-mail, RSS e processos para atualização de gráficos de Medidor.  
  ·         Possibilita a criação de gráficos a partir de registros da visão das actions.  
  ·         Possibilita a criação de Gráficos em Anexo  
  ·         Permite a criação de Categorias de Gráficos  
  ·         Permite a associação de um Perfil de Usuário a uma categoria  
  ·         Permite a associação de uma Categoria de Gráfico a um Gráfico  
  ·         Permite a criação de gráficos.  
  ·         Permite a impressão e visualização de Gráficos.  
  ·         Permite a exportação do resultado do Gráfico.  
  ·         Permite a visualização do Gráfico no site do RM Portal.  
  ·         Permite a definição de parâmetros para a fonte de dados do Gráfico.  
  ·         Permite o envio do gráfico por e-mail.  
     
  **Cenários**  
  Os cenários nos permitem a criação de um espaço onde contenha vários recursos utilizados na linha RM, tais como telas em .NET, consulta SQL, Gráficos, RSS e Atendimentos.  
  ·           Principais características:  
  ·           Permite a inclusão de uma tela .Net no Cenário.  
  ·           Possibilita a inclusão de uma consulta SQL no Cenário.  
  ·           Permite a inclusão de um Gráfico no Cenário.  
  ·           Possibilita a inclusão de um RSS no Cenário.  
  ·           Permite a inclusão da tela de Atendimentos no Cenário.  
  ·           Possibilita a inclusão de vários cenários.  
     
  **Reader RSS**  
  Permite a leitura dos RSS TOTVS e de terceiros.  
  Principais características:  
  ·           Possibilita a inclusão de Canais RSS  
  ·           Permite a configuração da cadência de atualização e exibição das RSS.  
  ·           Possibilita a inclusão de canais TOTVS S.A.  
  ·           Permite a inclusão de canais de terceiros.  
  ·           Permite a disponibilização dos canais cadastrados no site do RM Portal.  
    
  **Relatórios Fixos**  
  Os relatórios criados internamente pelo aplicativo são conhecidos como relatórios fixos.   
  O relatório interno do aplicativo TOTVS Gestão Bibliotecária é:  
  ·           Bematech  
  ·           Relatório de recibo de empréstimo e devolução.  
     
  **Relatórios do RM Reports**  
  Os relatórios do RM Reports podem ser criados e formatados nos aplicativos da Linha RM utilizando a tecnologia .NET, o que nos permite a geração de relatórios a partir da arquitetura multicamadas, além de relatórios locais.  
  Principais características:  
  ·         Permite a criação de relatórios, podendo definir níveis de acesso aos mesmos.   
  ·         Permite a visualização de relatórios em uma ou mais coligadas.  
  ·         Permite a importação/exportação de um ou mais relatórios.  
  ·         Permite a cópia da estrutura de um relatório, gerando um novo relatório com essa estrutura.  
  ·         Permite a visualização do relatório antes da impressão.  
  ·         Permite gravar última configuração de impressão utilizada.  
  ·         Permite a criação de grupos de relatórios.  
  ·         Permite montar e alterar relatórios facilmente através de uma interface amigável. Além disto, será possível:  
  ·         Inserir grupos como Margem Superior e Inferior, Cabeçalho e Rodapé do Relatório, Cabeçalho e Rodapé da Página, Rodapé do Grupo, Detalhes, Sub-detalhes Sub-Relatórios;  
  ·         Visualizar os grupos de forma hierárquica facilitando a compreensão do relatório;  
  ·         Inserir campos da base de dados, imagens, textos, consultas SQL, data, hora e contador de páginas no relatório;  
  ·         Visualizar através de uma régua o posicionamento dos campos no papel;  
  ·         Mover e copiar campos do relatório;  
  ·         Copiar a formatação de um campo;  
  ·         Filtrar registros a serem impressos;  
  ·         Alterar a formatação do campo como fonte, borda, formato de impressão e etc.;  
  ·         Determinar campo de ordenação e quebra do grupo;  
  ·         Marcar grupos que não serão impressos dentre outras funcionalidades.  
    
  **Planilha .NET**  
  O cadastro de Planilhas .Net é baseado no MS Excel 2007 e possibilita o uso de todas as funcionalidades do produto da Microsoft.  
  Principais características:  
  ·         Utiliza os recursos do Microsoft Excel 2007 para gerar planilhas nos produtos da Linha RM.  
  ·         Permite a criação de planilhas eletrônicas.  
  ·         Permite a inclusão de novas pastas.  
  ·         Permite inserir sentenças SQL para obter informações da base de dados, através de uma interface amigável para a construção dessas sentenças, inclusive com passagens de parâmetros que podem referencias células da própria pasta ou de outra.  
  ·         Permite mover e copiar dados de uma célula para outra, inclusive as sentenças SQL e Stored Procedures que estejam incluídas na consulta SQL.  
     
  **8. Segurança dos produtos corporativos**  
  ·         Disponibiliza controle de login efetuado pelo sistema, possibilitando definição das transações de inclusão, alteração e exclusão da base. Neste caso, cada usuário deverá fazer login no aplicativo com senha própria e exclusiva, cujo acesso será controlado por Perfil de acessos a Menus, Campos ou Relatórios, previamente definidos, podendo ou não realizar determinada operação, conforme lhe foi permitido no perfil atribuído por um usuário superior hierarquicamente na administração do banco de dados.   
  ·         Permite definir diferentes níveis de acesso em cada perfil, de acordo com o grau de necessidade de acessos de cada usuário ou grupo de usuários nos aplicativos.  
  ·         Permite a inclusão e manutenção de códigos especiais de acesso ao banco de dados. Os códigos criados referem-se ao acesso e administração do banco de dados e não usuário do aplicativo, que possui outro cadastro próprio. Desta forma, poderão ser criados no aplicativo diferentes códigos de acesso para diferentes usuários do aplicativo, podendo alguns deles ter maiores liberdades como administradores do banco de dados.  
     
  **Segurança específica do TOTVS Gestão Bibliotecária**  
  ·         Permite definir as permissões de acesso por Filial/Unidade para cada usuário.  
  ·         Após as definições, os usuários terão acesso somente a Filial/Unidade permitidos.  
     
     
  **9. Integração**  
     
  ***Aplicativos* RM**   
  No funcionamento da integração, os dados são enviados de forma integrada, evitando re-trabalho e inconsistências, para todos os módulos abaixo descritos.

  |  |  |
  | --- | --- |
  | APLICATIVO | RECURSOS DISPONÍVEIS |
  | TOTVS Gestão Financeira | üControle Financeiro |
  | RM Classis Básico/Superior e TOTVS Educacional | üImportação de Alunos e Professores além da atualização de seus dados. |
  | TOTVS Folha de Pagamento | ü Importação de Funcionários como alunos do TOTVS Gestão Bibliotecária. |
  | TOTVS Gestão de Estoque, Compras e Faturamento | ü Controle de aquisição de exemplares |

  **Terceiros**  
  ·           Bematech  
  ·           Impressão de recibo de empréstimo e devolução.  
  ·           Scanner de Biometria Digital  
  Identificação de usuários através da impressão digital. O scanner de Biometria Digital homologado pela TOTVS é o Sensor U.are.U Fingerprint Reader da DigitalPersona.  
     
     
  **10. Customização**  
  A TOTVS possui um departamento responsável por analisar solicitações específicas de clientes ou viabilizar prazos menores para o desenvolvimento de novos recursos. Para solicitar customizações, o cliente deve entrar em contato com o Depto. de Suporte que encaminhará a solicitação para a equipe de customizações.  
     
     
  **11. Módulos do RM Portal**  
     
  **Controle de Biblioteca**  
  ·         Pesquisa do acervo bibliotecário: permite que o usuário faça uma consulta das publicações e exemplares que constituem o acervo bibliotecário.  
  ·         Reserva de exemplares disponíveis: permite a reserva dos exemplares que constitui o acervo.  
  ·         Renovação de empréstimo: para renovar um empréstimo o sistema faz três consistências. A primeira é verificar se a regra de empréstimo permite renovação automática. A segunda é verificar se o usuário não está em atraso (caso a regra de empréstimo esteja definida para barrar empréstimos de usuários em atraso, o sistema não irá fazer a renovação). E a terceira é o acesso do usuário na Unidade (caso nos parâmetro esteja marcado para visualizar exemplares de todas as unidades, pode ocorrer do usuário não ter acesso a alguma Unidade).  
  ·         Acompanhamento da situação atual do usuário: o usuário poderá acompanhar datas de devolução de exemplares, reservas efetuadas e data de validade da reserva.  
  ·         Cancelamento de reserva: o usuário tem a opção de cancelar reservas.  
  ·         Sugestão de compras: o usuário tem a opção de registrar sugestões de compra de publicações a serem acrescidas ao acervo bibliotecário.  
  ·         Acompanhamento de novas aquisições na biblioteca: o usuário poderá verificar quais exemplares foram acrescentados ao acervo em um período informado.  
  ·         Emissão de boletos: o usuário poderá visualizar boletos de lançamentos financeiros gerados na biblioteca.
