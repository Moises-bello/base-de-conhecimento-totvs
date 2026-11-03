---
content_hash: dde584db89ad6c98dc80189e816b6d19306f92b45ea046b2ff490708d156e05d
fetched_at: '2026-06-29T00:09:36.112105+00:00'
page_id: '425459469'
product: rm
source: tdn-rm
title: TOTVS Processo Seletivo - Especificações Técnicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459469
version: 5
---

**Apresentação**

Este documento tem como objetivo, discriminar as principais características técnicas dos aplicativos RM, permitindo a você obter uma melhor compreensão de seu funcionamento e conseqüentemente, aproveitar seus recursos e benefícios.

Características

A linha RM é a solução corporativa de gestão empresarial da TOTVS. Desenvolvido para tecnologia Windows 32 e 64bits, .Net e arquitetura Cliente/Servidor, possui banco de dados único, padrão SQL Structure Query Language (Linguagem de Consulta Estruturada), atualizações on-line, interface padronizada e diversas ferramentas disponíveis. Flexível, possibilita a integração com sistemas específicos de sua empresa.  
    
 Interface Padrão Windows

Possui atualização on-line dos dados de entrada, permitindo acesso às informações atualizadas imediatamente após o término da transação. Possui padronização do uso de teclas e funções, em todos os módulos, de forma a facilitar o seu aprendizado e operação. Possui opção de "fazer" e "desfazer" as ações executadas pelos aplicativos.

Exemplo: inclusão de requisição de material e estorno de requisição de material; inclusão e exclusão e/ou estorno de lançamento; inclusão e exclusão de conta contábil, etc. Apresenta todas as telas e relatórios no ambiente do usuário em português.

Ajuda On-line Sensível à Opção

Possui documentação técnica do sistema em português, através de dispositivo de Ajuda On-Line com orientação detalhada (passo a passo) de como utilizar o aplicativo, bem como os itens de menu e o preenchimento das telas de Ajuda On-line dos campos, opções e erros no padrão Windows.

**1. Ferramentas de Suporte**

As ferramentas de suporte são funcionalidade que servem de apoio para que uma determinada funcionalidade complete seu processamento. Este comportamento pode ser encontrado em várias situações na linha RM, e são imprescindíveis para determinados processos.

Fórmula

As Fórmulas nos aplicativos RM terão, basicamente, três principais objetivos, dentre eles:

* Seleção (restrição da aplicabilidade de alguma operação).
* Definição da forma de cálculo de eventos específicos, inclusive do tipo "base de cálculo", que servem de referência para outros cálculos.
* Relacionamento de valores entre os eventos.

O editor de fórmulas possui um campo de texto para que você monte as estruturas das fórmulas.   
 Usando o editor de fórmulas, as funções e comandos desejados para a criação da fórmula serão movidos para o campo de texto, bastando clicar duas vezes sobre as opções função, comando ou parâmetro. Principais características:

* Permite através de um editor criar fórmulas no sistema
* Permite a aplicação em campos complementares
* Permite seu uso em consultas SQL
* Possibilita aplicação em relatórios do sistema
* Permite uso em processos do RM
* Possibilita exportação do log de execução

Fórmula Visual

Fórmula visual trata-se de uma funcionalidade que executa um fluxo de operações pré-definidas. O fluxo é definido pelo próprio usuário, que através desta ferramenta é capaz de atender diversas particularidades. Principais características:

* Permite a escolha de atividades pré-definidas no RM ou mesmo acrescentar novas atividades
* Permite através de um editor visual criar com fluxos de ações
* Permite a escolha de atividades pré-definidas no RM ou mesmo acrescentar novas atividades
* Permite a customização das funcionalidades do RM a partir das atividades disponíveis
* Permite definir em qual momento a fórmula visual será executada, a partir da manipulação de gatilhos
* Permite o agendamento de uma fórmula visual a partir do agendamento de Jobs.

Mashups

A idéia do Mashup é utilizar uma pesquisa na Web para atualizar dados cadastrais ou simplesmente fazer uma busca. Principais características:

* Realiza a pesquisa de dados na Web para realizar a atualização de cadastros no RM.
* Verifica a existência e a autenticidade de um dado como CPF, CNPJ, CEP, entre outros dados diretamente na internet a fim de possibilitar o cadastro de um registro.

Metadados

O metadados é um mecanismo que possibilita a geração automática de formulários para cadastramento de informações no banco de dados, a fim de dispor de novos cadastros para o RM. Principais características:

* Permite a criação de formulários customizados que realizam gravação na base de dados, também em tabelas customizadas.
* Possui interface de manipulação que permite criação de ferramentas que serão disponibilizadas no módulo de Globais, garantindo a entrada de dados na estrutura de metadados através de uma interface simples e amigável, exigindo o mínimo de esforço do usuário final.
* Possui mecanismo capaz de exportar e importar informações de uma estrutura de metadados, permitindo compartilhar dados de uma base para outra
* Possui mecanismo que permita uma sincronização entre servidores de aplicação em cluster e os clientes distribuídos da aplicação com a finalidade de manter as versões compatíveis de execução de um projeto de metadados.

**2. Ferramentas de Saídas**

Gerador de Relatórios

Os relatórios são criados e formatados nos aplicativos da Linha RM através do recurso Gerador de Relatórios, que é baseado na arquitetura Win32. Principais características:

* Possibilita a exclusão dos relatórios executados através de agendamento conforme uma periodicidade.
* Possibilita a exclusão de relatórios em bloco.
* Admite a inclusão de linhas em branco em um relatório do tipo arquivo bancário
* Permite a criação de relatórios, podendo definir níveis de acesso a esses relatórios.
* Os relatórios criados podem ser de saída padrão (formato próprio), Texto, RTF, PDF ou Arquivo Bancário (exportação de dados).
* Permite a visualização de relatórios em uma ou mais coligadas.
* Permite que todos os relatórios possam ser gerados em vídeo, impressora ou arquivo, com parametrização de páginas inicial e final, bem como número desejado de cópias, entre outras opções.
* Permite a importação/exportação de um ou mais relatórios.
* Permite a cópia da estrutura de um relatório, gerando um novo relatório com essa estrutura.
* Permite a visualização do relatório antes da impressão.
* Permite gravar última configuração de impressão utilizada.
* Permite a criação de grupos de relatórios.
* Permite a cópia dos relatórios entre coligadas
* Permite montar e alterar relatórios facilmente através de uma interface amigável.

Além disto, será possível:

* Inserir grupos como Cabeçalho e Rodapé de Página, Linha Detalhe, Cabeçalho e Total de Detalhe, Total de Página, Capa e Total de Relatório;
* Visualizar os grupos de forma hierárquica facilitando a compreensão do relatório;
* Inserir campos da base de dados, imagens, textos, fórmulas, expressões, consultas SQL, Stored Procedure, data, hora e contador de páginas no relatório;
* Visualizar, através de uma régua, o posicionamento dos campos no papel;
* Mover e copiar campos do relatório;
* Copiar a formatação de um campo;
* Selecionar registros a serem impressos (incluir filtro);
* Alterar a formatação do campo como fonte, borda, formato de impressão e etc.;
* Determinar campo de ordenação e quebra do grupo;
* Marcar grupos que não serão impressos dentre outras funcionalidades.

Planilha Eletrônica

As Planilhas dos aplicativos RM possuem uma estrutura semelhante à estrutura das planilhas do MS Excel. Podem conter várias pastas para que o usuário possa organizar vários tipos de relatórios num único arquivo. Principais características:

* Permite a criação de planilhas eletrônicas.
* Permite a inclusão de novas pastas.
* Permite inserir sentenças SQL para obter informações da base de dados, através de uma interface amigável para a construção dessas sentenças, inclusive com passagens de parâmetros que podem referencias células da própria pasta ou de outra.
* Permite inserir Stored Procedures.
* Permite a inclusão e formatação de gráficos.
* Permite a formatação dos dados da planilha, como tamanho, cor, número de casas decimais, borda e etc.
* Permite a cópia da formatação de uma célula para outra.
* Permite mover e copiar dados de uma célula para outra, inclusive as sentenças SQL e Stored Procedures.
* Permite inserir e excluir linhas/colunas da planilha.
* Permite inserir várias funções, como por exemplo, a função SUM para o somatório de uma faixa de dados.
* Permite a exportação/importação da planilha, como por exemplo, para o MS-Excel.
* Permite a impressão de parte da planilha (uma ou várias pastas ou mesmo parte de uma pasta).
* Permite a impressão de uma ou várias planilhas ao mesmo tempo.

Cubos

Através dos Cubos é possível realizar uma consulta em toda a base de dados dos aplicativos RM proporcionando a customização da análise e a criação de planilhas e relatórios gerenciais. Principais características:

* Permite as visualizações de Cubos.
* Permite a impressão de Cubos.
* Permite a exportação do cubo para o MS-Excel.
* Permite a visualização de gráficos.
* Permite a exportação e importação de arquivos de Cubos.
* Permite a edição dos parâmetros dos cubos que os possuem.
* Permite a validação de senhas dos cubos que as possuem.
* Possibilita a conversão de cubos Delphi para o Cubo.Net.

Relatórios Fixos

Os relatórios criados internamente pelo aplicativo são conhecidos como relatórios fixos.  O documento de Especificação Técnica de cada produto relaciona os relatórios fixo disponíveis no sistema.

Relatórios do RM Reports

Os relatórios do RM Reports podem ser criados e formatados nos aplicativos da Linha RM utilizando a tecnologia .NET, o que nos permite a geração de relatórios a partir da arquitetura multicamadas, além de relatórios locais. Principais características:

* Permite a criação de relatórios, podendo definir níveis de acesso aos mesmos.
* Permite a visualização de relatórios em uma ou mais coligadas.
* Permite a importação/exportação de um ou mais relatórios.
* Permite a cópia da estrutura de um relatório, gerando um novo relatório com essa estrutura.
* Permite a visualização do relatório antes da impressão.
* Permite gravar última configuração de impressão utilizada.
* Permite a criação de grupos de relatórios.
* Permite montar e alterar relatórios facilmente através de uma interface amigável.

Além disto, será possível:

* Inserir grupos como Margem Superior e Inferior, Cabeçalho e Rodapé do Relatório, Cabeçalho e Rodapé da Página, Rodapé do Grupo, Detalhes, Sub-detalhes Sub-Relatórios;
* Visualizar os grupos de forma hierárquica facilitando a compreensão do relatório;
* Inserir campos da base de dados, imagens, textos, consultas SQL, data, hora e contador de páginas no relatório;
* Visualizar através de uma régua o posicionamento dos campos no papel;
* Mover e copiar campos do relatório;
* Copiar a formatação de um campo;
* Filtrar registros a serem impressos;
* Alterar a formatação do campo como fonte, borda, formato de impressão e etc.;
* Determinar campo de ordenação e quebra do grupo;
* Marcar grupos que não serão impressos dentre outras funcionalidades.
* Permite a inclusão de gráficos de medidores no relatório.

Planilha .Net

O cadastro de Planilhas .Net é baseado no MS Excel 2007 e possibilita o uso de todas as funcionalidades do produto da Microsoft. Principais características:

* Utiliza os recursos do Microsoft Excel 2007 para gerar planilhas nos produtos da Linha RM.
* Permite a criação de planilhas eletrônicas.
* Permite a inclusão de novas pastas.
* Permite inserir sentenças SQL para obter informações da base de dados, através de uma interface amigável para a construção dessas sentenças, inclusive com passagens de parâmetros que podem referencias células da própria pasta ou de outra.
* Permite mover e copiar dados de uma célula para outra, inclusive as sentenças SQL e Stored Procedures que estejam incluídas na consulta SQL.

Gráficos

Os gráficos são resultado do processamento de uma fonte de dados e sua exposição por meio de diversos tipos de gráficos. Principais características:

* Permite programar alertas via e-mail, RSS e processos para atualização de gráficos de Medidor.
* Possibilita a criação de gráficos a partir de registros da visão das actions.
* Possibilita a criação de Gráficos em Anexo
* Permite a criação de Categorias de Gráficos
* Permite a associação de um Perfil de Usuário a uma categoria
* Permite a associação de uma Categoria de Gráfico a um Gráfico
* Permite a criação de gráficos.
* Permite a impressão e visualização de Gráficos.
* Permite a exportação do resultado do Gráfico.
* Permite a visualização do Gráfico no site do RM Portal.
* Permite a definição de parâmetros para a fonte de dados do Gráfico.
* Permite o envio do gráfico por e-mail.
* Possibilita ser aplicado nos Painéis de Metas.
* Permite a seleção de gráfico do tipo Drill Down.

Cenários

Os cenários nos permitem a criação de um espaço onde contenha vários recursos utilizados na linha RM, tais como telas em .NET, consulta SQL, Gráficos, RSS e Atendimentos. Principais características:

* Permite a inclusão de uma tela .Net no Cenário.
* Possibilita a inclusão de uma consulta SQL no Cenário.
* Permite a inclusão de um Gráfico no Cenário.
* Possibilita a inclusão de um RSS no Cenário.
* Permite a inclusão da tela de Atendimentos no Cenário.
* Possibilita a inclusão de vários cenários.

Reader RSS

Permite a leitura dos RSS TOTVS e de terceiros. Principais características:

* Possibilita a inclusão de Canais RSS
* Permite a configuração da cadência de atualização e exibição das RSS.
* Possibilita a inclusão de canais TOTVS S.A.
* Permite a inclusão de canais de terceiros.
* Permite a disponibilização dos canais cadastrados no site do RM Portal.

**3. Segurança dos produtos corporativos**

* Disponibiliza controle de login efetuado pelo sistema, possibilitando definição das transações de inclusão, alteração e exclusão da base. Neste caso, cada usuário deverá fazer login no aplicativo com senha própria e exclusiva, cujo acesso será controlado por Perfil de acessos a Menus, Campos ou Relatórios, previamente definidos, podendo ou não realizar determinada operação, conforme lhe foi permitido no perfil atribuído por um usuário superior hierarquicamente na administração do banco de dados.
* Permite definir diferentes níveis de acesso em cada perfil, de acordo com o grau de necessidade de acessos de cada usuário ou grupo de usuários nos aplicativos.
* Permite a inclusão e manutenção de códigos especiais de acesso ao banco de dados. Os códigos criados referem-se ao acesso e administração do banco de dados e não usuário do aplicativo, que possui outro cadastro próprio. Desta forma, poderão ser criados no aplicativo diferentes códigos de acesso para diferentes usuários do aplicativo, podendo alguns deles ter maiores liberdades como administradores do banco de dados.

**4. Estrutura das Tabelas**

As entidades manipuladas no aplicativo estão dispostas em diversas tabelas que classificamos de Tabelas Globais e Tabelas Específicas. As Tabelas Globais são aquelas tabelas comuns a todos os segmentos da Linha RM, sendo, portanto manipuláveis por todos os segmentos; As Tabelas Específicas do segmento são aquelas que se encontram disponíveis no segmento, embora possam ser encontradas também compartilhadas entre outros segmentos da Linha RM, visando garantir a integração entre os segmentos. A criação de novas entidades e/ou atributos deverá ser efetuada exclusivamente pela própria TOTVS. Caso necessário, o cliente deverá encaminhar solicitação de inclusão de entidades/atributos ao Depto. de Suporte da TOTVS Sistemas para que a mesma seja encaminhada ao Departamento de Desenvolvimento para avaliação.

**5. Implantação**

A Área de Serviços da TOTVS visa implantar os seus produtos de acordo com os processos de cada cliente. Finalizada a negociação comercial, é realizado o levantamento de processos para compreender as regras do negócio do cliente e verificar se os aplicativos RM atendem às suas necessidades.

Os analistas de processos são responsáveis por documentar todos os detalhes dos processos para garantir que o escopo do projeto considere todos os possíveis pontos críticos do projeto, seguindo o padrão proposto pela metodologia de implantação da TOTVS.

O cliente valida os processos levantados e o gerente de projetos TOTVS apresenta o cronograma e o projeto de implantação, que informa a programação de tarefas a ser seguida para o sucesso do projeto. Durante a execução do projeto são realizadas reuniões de avaliação para garantir o custo e o prazo estipulados projeto.

Todos os processos implementados pelos consultores de implantação TOTVS são simulados e validados pelo cliente. Testes integrados também garantem os resultados da implantação de vários módulos associados. Finalizado o período de parametrização e testes, os sistemas entram em produção e são acompanhados na fase inicial.

Encerrado o projeto, o cliente assina um termo que formaliza a conclusão das tarefas e o cliente é encaminhado ao Suporte para futuros atendimentos em caso de dúvidas. Instalação do gerenciador de banco de dados - SGDB

Deve ser providenciada, caso ainda não tenha sido realizada, instalação do gerenciador de banco de dados de preferência da empresa, conforme a necessidade, e que já se encontre instalada em outros equipamentos ou servidores: SQL e Oracle (vide versão do gerenciador no tópico Portabilidade) Instalação da base de dados dos aplicativos RM.

Instalação dos Aplicativos RM Primeiramente devem ser instalados os outros aplicativos RM. Através da execução dos processos internos desses aplicativos, a base de dados será alimentada com as informações com as quais o RM Bis poderá utilizar para a geração dos cubos de decisão.

**6. Customização**

A TOTVS possui um departamento responsável por analisar solicitações específicas de clientes ou viabilizar prazos menores para o desenvolvimento de novos recursos. Para solicitar customizações, o cliente deve entrar em contato com o Depto. de Suporte que encaminhará a solicitação para a equipe de customizações.

**7. Natureza Funcional do Processo Seletivo**

Processos seletivos Permite a criação e gestão de processos seletivos próprios da Instituição de Ensino (ensino básico, graduação, especialização, mestrado, doutorado e pós-doutorado) além da terceirização deste tipo de serviço (prestação de serviço para gestão de processos seletivos de terceiros). Para cada processo seletivo criado é possível:

* Criar outros processos seletivos através de um processo seletivo base.
* Definir um valor padrão para inscrição no processo seletivo, caso este valor atenda a todas as áreas ofertadas.
* Definir fórmula de Classificação Geral utilizando fórmula ou regra interna do sistema, entre todos os candidatos do Processo Seletivo, independente da classificação individual em cada área ofertada.
* Controlar processos seletivos por filial
* Definir calendário de realização das etapas do processo seletivo (inscrição, seleção e divulgação de resultados) paralelamente ou individualmente.
* Criar e Controlar múltiplas áreas de interesse ofertadas.
* Utilizar controle de vagas no processo seletivo.
* Criar e Controlar múltiplas formas de inscrição (inscrição presencial, web, por convênios, etc) com datas de inscrição diferenciadas para cada forma de inscrição.
* Disponibilizar e Controlar locais de realização do processo seletivo, especificando "Campus" no prédio, número de vagas e capacidade de acomodação para candidatos portadores de necessidades especiais.
* Permitir ou não a participação de candidatos treineiros.
* Controlar o número mínimo e máximo de inscrições permitidas por candidato.
* Controlar o número máximo de áreas opcionais permitidas por inscrição de candidato.
* Controle de inscrições canceladas ou excluídas do processo seletivo.
* Utiliza agendamentos de atividades para selecionar candidatos.
* Gera Inscrições anônimas para o processo seletivo.
* Exporta dados de candidatos já inscritos no processo seletivo para confecção de cadernos de provas e arquivo para importação de gabaritos.

Áreas de interesse

Áreas de interesse são os objetos de seleção ofertados em um processo seletivo. Um curso de graduação é uma área de interesse, bem como um cargo ofertado em um concurso público. Para cada área de interesse disponibilizada em um processo seletivo, é possível:

* Controlar número de vagas ofertadas.
* Alterar dados das etapas pelo processo "Alteração de parâmetros de etapa da área ofertada".
* Controlar permissão de descontos sobre inscrições de candidatos.
* Controlar a exigência de línguas estrangeiras para processos de seleção de forma diferenciada (pode ser definido o número de línguas estrangeiras exigidas).
* Utilização de notas do ENEM no processo de apuração (processos seletivos para graduação)
* Definir valor de inscrição e conta caixa diferenciada.
* Definir termo de aceite para inscrição.
* Definir número e tipos de etapas da seleção (etapa de seleção ou divulgação parcial de resultado).
* Definir provas para avaliação de língua estrangeira na seleção.
* Definir agendamentos de recursos para realização do processo seletivo (eletrônico).
* Definir documentação exigida para cada inscrição de candidato.
* Definir faixa etária mínima e máxima para inscrição nesta área.
* Definir fórmula de classificação para esta área.

Gestão de prova

Permite a criação e gestão de provas elaboradas para processos seletivos, através da integração com o módulo de Avaliações (TOTVS Avaliação e Pesquisa). Através deste recurso é possível:

* Manter um banco de questões de prova
* Confeccionar provas utilizando o banco de questões.
* Distribui e cancela cadernos de provas para os candidatos utilizando as provas do TOTVS Avaliação e Pesquisa.
* Utiliza a importação de gabaritos para correção de cada prova via TOTVS Avaliação e Pesquisa.

Inscrição

* Controlar inscrições de candidatos por responsável (Portal).
* Controlar inscrições pelo Portal ou Secretaria.
* Controlar inscrições de candidatos por formas de inscrição diferenciadas.
* Cancela ou Exclui inscrições de candidatos.
* Altera status da opção do candidato. (Desclassifica este candidato a qualquer tempo se for necessário, antes mesmo de participar da seleção).
* Altera forma de inscrição se necessário.

No ato da inscrição é possível:

* Permitir ao responsável do candidato se inscrever e inscrever o candidato sob sua responsabilidade.
* Permitir ao candidato definir a cidade de realização da prova e agendamentos, se tiver.
* Permitir ao candidato informar áreas de interesse opcionais e línguas estrangeiras da opção.
* Permitir ao candidato informar se há necessidade especial (necessidade visual, auditiva, motora, múltipal ou outra).
* Permitir ao candidato preencher um questionário sócio-econômico no ato da inscrição.
* Emitir boleto de pagamento.
* Emitir comprovante de inscrição.

Realização do processo seletivo

* Controlar a entrega de documentos exigidos para inscrição do candidato.
* Controla e aloca candidatos em sala de prova somente após Confirmar as inscrições, que estarão quitadas.
* Alocar automaticamente ou manualmente os candidatos nos locais de realização das etapas de seleção (este processo já aloca de acordo com a (s) necessidade (s) especial (is) do candidato).
* Alocar automaticamente ou manualmente os profissionais nos locais, considerando a função de cada profissional e o local.
* Cancelar áreas ofertadas realocando candidatos ou cancelando inscrições automaticamente.
* Realizar seleção de candidatos através de atividades agendadas. (processo seletivo agendado).

Apuração de resultados

* Registrar presença de candidatos que compareceram ao processo seletivo.
* Importar Notas do ENEM através de arquivos fornecidos pelo INEP.
* Importar gabaritos para correção automática de provas.
* Apurar e classificar automaticamente ou manualmente os candidatos para a área de interesse escolhida (primeira e demais opções), permitindo várias chamadas sucessivas.
* Classificação Geral entre os candidatos de todas as áreas do Processo Seletivo.

Divulgar resultados de processos seletivos pela internet.

* Se parametrizado, divulgar a lista de chamada e o link de classificação geral em "Resultados gerais" do Processo Seletivo.

Fechamento do processo seletivo

* Registrar presença de profissionais alocados no processo seletivo.
* Efetuar pagamento de profissionais presentes no processo seletivo (em folha de pagamento ou através de lançamento financeiro a pagar).
* Exclui lançamentos financeiros não utilizados pelas inscrições anônimas geradas para o processo seletivo.
