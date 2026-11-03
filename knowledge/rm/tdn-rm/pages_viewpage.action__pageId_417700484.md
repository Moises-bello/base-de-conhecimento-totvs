---
content_hash: 230a206a08ae23b82405d53a735608ad99e3b8cf2abcad37df5115c1edd8cc66
fetched_at: '2026-06-29T00:09:12.763296+00:00'
page_id: '417700484'
product: rm
source: tdn-rm
title: Apresentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700484
version: 1
---

\_Toc102300405\_Toc273955078**Apresentação**  
   
Este documento tem como objetivo, discriminar as principais características técnicas de cada produto, permitindo a você obter uma melhor compreensão de seu funcionamento e conseqüentemente, aproveitar seus recursos e benefícios.  
A nossa solução visa auxiliar na gestão de informação hospitalar, não apenas no que diz respeito às infecções hospitalares, mas, também como gerenciador de outros parâmetros da qualidade da assistência. De forma simples, analisa dados e emite relatórios que podem ser convertidos em gráficos ou tabelas. Os dois grandes objetivos  da solução  são facilitar o dia-a-dia dos profissionais que trabalham no gerenciamento da assistência  permitindo melhor integração destes com as equipes e setores do hospital. Relatórios que são exigidos pelas agências fiscalizadoras da saúde são facilmente emitidos; há ferramentas que permitem incorporar dados de áreas específicas do hospital, como o APACHE para a terapia intensiva.   
Pode interagir com outros  sistemas de gestão hospitalar, por exemplo, importar dados do tipo internação e alta, cultura, Antibiótico e cirurgia de um ou vários pacientes. O sistema está muito bem adaptado as reais necessidades dos profissionais da área da saúde em epidemiologia e controle das infecções hospitalares.  
   
 \_Toc273955079**1. Características do RM**  
apresentacaoEste documento tem como objetivo, discriminar as principais características técnicas dos aplicativos RM, permitindo a você obter uma melhor compreensão de seu funcionamento e conseqüentemente, aproveitar seus recursos e benefícios.  
   
 \_Toc273955080**Arquitetura Cliente/Servidor**  
q  Arquitetura Arquitetura Client-Server que permite distribuição de processamento entre a estação cliente e o servidor de banco de dados SQL.  
q   Possui base de dados centralizada, podendo ser acessada simultaneamente por dois ou mais dos módulos que integram o Sistema Corporativo.  
q   A base de dados padrão SQL permite a utilização de geradores de relatórios de terceiros como um complemento ao gerador do próprio sistema.  
q   Desenvolvido em Borland Delphi â 32 Bits e Visual Studio 2005 C#.Net, para plataformas Microsoft Windows (vide tópico Portabilidade).  
q   Plataforma mínima para estação cliente (estação de trabalho) – (Vide Tópico Arquitetura).  
q   Plataforma mínima para o servidor de dados (vide tópico Arquitetura).  
q   Possui modelo de processamento na arquitetura Cliente/Servidor e WEB.  
   Possui compatibilidade com banco de dados ORACLEâ (vide detalhes no tópico Portabilidade).  
q   Trata-se de uma aplicação com todos os módulos integrados, a base de dados é compartilhada com outros aplicativos.  
   Possibilita a exportação e importação de dados para/de outros sistemas, através da definição de layouts especiais, mantendo a integridade dos mesmos.  
   Baseia-se no conceito de transações, mantendo a integridade do Banco de Dados em quedas de energia e falhas de software/hardware.  
   
\_Toc93396136\_Toc94436648\_Toc102970651\_Toc273955081**Interface Padrão Windows**  
  Interface Possui atualização on-line dos dados de entrada, permitindo acesso às informações atualizadas imediatamente após o término da transação.  
   Possui padronização do uso de teclas e funções, em todos os módulos, de forma a facilitar o seu aprendizado e operação.  
   Possui opção de "fazer" e "desfazer" as ações executadas pelos aplicativos.   
   Exemplo: inclusão de requisição de material e estorno de requisição de material; inclusão e exclusão e/ou estorno de lançamento; inclusão e exclusão de conta contábil, etc.  
   Apresenta todas as telas e relatórios no ambiente do usuário em português.  
   
\_Toc93396137\_Toc94436649\_Toc102970652\_Toc273955082**Ajuda On-line Sensível à Opção**  
  ajuda Possui documentação técnica do sistema em português, através de dispositivo de Ajuda On-Line com orientação detalhada (passo a passo) de como utilizar o aplicativo, bem como os itens de menu e o preenchimento das telas de Ajuda On-line dos campos, opções e erros no padrão Windows.  
   
\_Toc273955083**2. Natureza Funcional do TOTVS Controle de Infecção Hospitalar**  
Este produto possui as seguintes características técnicas:  
   Cadastro Unidade Clínica. Permite cadastrar todas as unidades clínicas constantes no hospital.   
   Cadastro de Especialidade. Permite cadastrar todas as especialidades constantes no hospital.   
   Cadastro de Médico. Permite cadastrar os  dados dos médicos e o anexo especialidade referente ao mesmo.  
   Cadastro de Equipes Médicas. Permite cadastrar as equipes atuantes no hospital e o anexo referente aos médicos pertencentes a cada equipe.    
   Cadastro de Procedimento Cirúrgico. Este cadastro refere-se a classificação dos procedimentos cirúrgicos conforme definição da metodologia NHSN (National Healthcare Safety Network).  
   Cadastro de Procedimento Invasivo. Este cadastro refere-se a classificação dos procedimentos cirúrgicos conforme definição da metodologia NHSN. A metodologia NHSN acompanha e faz referência às taxas dos seguintes procedimentos invasivos, SVD (Sonda Vesical de Demora), VAP (Ventilação Artificial Prolongada), CVCD (Cateter Venoso Central Dissecado) e CVCP (Cateter Venoso Central Puncionado). Não impedido de cadastrar novos, contudo não há uma taxa para acompanhá-los. Mas, o sistema permite os descritivos em que se permite acompanhar os números de ocorrência dos mesmos.  
   Cadastro de Sítio primário contem como os sítio secundário e grupo de material, ambos vinculados ao sítio primário que correspondem. Sítio Primário/Sítio Secundário são cadastros bloqueados  para inclusão, edição e exclusão  por serem referência da metodologia NHSN ( National Healthcare Safety Network).   
   Cadastro de Evento Adverso permite o usuário criar novos eventos adversos ocorridos com os possíveis motivos/conseqüência.   
   Cadastro Grupo de Germe. Permite cadastrar os grupos germes definidos conforme literatura.   
   Cadastro germe: Os germes são cadastrados conforme definido pela taxonomia mais recente. Tem como dado obrigatório o grupo de germe ao qual o germe faz parte segundo classificação da literatura. Faz-se necessário então o cadastro de grupo germe antes do cadastro germe.  
   Grupo de Antibiótico: Permite cadastrar os grupos de antibióticos conforme estabelecido pela literatura.  
   Cadastro Antibiótico: Os antibióticos são cadastrados conforme estabelecido pela literatura. É necessário o cadastro de grupo de antibiótico antes do cadastro de antibiótico.  
   Cadastro material de cultura: dispõe o grupo de material conforme definido pela metodologia NHSN ( National Healthcare Safety Network). Permite incluir no anexo material, o material detalhado conforme cadastrado no Sistema do Hospital.  
   Cadastro Convênio: Permite cadastrar todos os convênios atuantes no hospital.   
   Cadastro CID: (Cadastro Internacional de Doenças). Este cadastro é incluído no sistema, por ser um cadastro de órgão oficial da saúde.   
   Cadastros | Paciente, dispõe de filtros com várias opções de seleção, permite gravar filtros mais usados pelo usuário. Consta anexo | internações do paciente(s), no qual visualiza todas as datas de internações do(s) paciente(s).   
   Cadastros | Paciente | Internações dispõem de um histórico cronológico com todas as passagens de internações do paciente. Permite o usuário alimentar os dados de internação do paciente manualmente ou a partir de importação diretamente do sistema do hospital. Constam os cadastros referentes aos dados do paciente (área crítica, cultura parcial, cultura final, antibiótico, eventos adversos, infecção, cirurgia e APACHE II);   
   Cadastros | Paciente | Internações | Área Crítica. Permite incluir, editar e excluir internações e procedimentos invasivos utilizado pelo paciente nas áreas críticas (CTI, UTIP, CTI Neonatal);  
   Cadastros | Paciente | Internações | Cultura Parcial. Permite incluir, editar, excluir e acompanhar diariamente o andamento do exame microbiológico (cultura) do(s) paciente(s). Esse cadastro consta às telas de Identificação e Resultado de cultura parcial. É especificamente de utilização do laboratório de Análise Clínicas, porque são informações que somente o profissional do laboratório poderá informar cabendo aos demais setores a consulta desses resultados pelo descritivo de cultura parcial caso o cadastro seja alimentado pelo laboratório;   
   Cadastros | Paciente | Internações | Cultura Final, permite incluir, editar e excluir os resultados finais do exame microbiológico (cultura) do(s) paciente(s). Esse cadastro consta às telas de Identificação, Sítios do pedido de cultura e Resultado do pedido de cultura.   
   Cadastros | Paciente | Internações | Antibiótico, permite incluir, editar e excluir todos os antibióticos prescritos de um paciente em uma determinada internação.   
   Cadastros | Paciente | Internações | Cirurgia. Permite incluir os dados referentes ao(s) procedimento(s) cirúrgico(s) que o paciente foi submetido.   
   Cadastros | Paciente | Internações | Infecção. Permite incluir, editar e excluir as infecções referentes ao paciente em uma determinada internação.   
   Cadastros | Paciente | Internações | Evento Adverso. Permite incluir, editar e excluir os eventos adversos não infecciosos relacionados à assistência ao paciente;  
   Cadastros | Paciente | Internações | APACHE II (Acute Physiology and Chronic Health disease Classification System II),  é um "Sistema de Pontuação de Mortalidade Estimada" para pacientes internados em unidades críticas de adulto (CTI´s, UTI´s).  Consiste num sistema de avaliação da severidade (quantitativa) e prognóstica (qualitativa) dos pacientes críticos que auxilia e agiliza a decisão da equipe médica quanto aos benefícios e cuidados a estes pacientes. Este método permite complementar a necessidade ou suspensão do suporte avançado de vida, comparar o desempenho entre diversas unidades de terapia intensiva, estratificar grupos de pacientes para avaliação de novas tecnologias e procedimentos terapêuticos. Obtem-se os dados através da coleta de variáveis clínicas e laboratoriais, ponderando valores de acordo com os resultados.   
   O aplicativo integra-se a outros sistemas para importar dados de internação. Essa integração está relacionada à importação de internação e alta dos pacientes, Cirurgia, Cultura e Antibiótico.   
   Opções | Impressos | disponibiliza impressos que auxiliam a coleta de dados na busca ativa;  
   Possui relatórios de estatísticas, indicadores gerenciais que disponibilizam taxas a partir de cubos que permitem realizar diversos agrupamentos obtendo inúmeras taxas e gráficos, estratificando-os por todo o hospital ou por uma determinada unidade clínica;   
   Os relatórios de estatísticas disponíveis são: Taxa Global | Taxa de Componente Cirúrgico | Taxa de Utilização de Antibióticos |Taxa de Consumo de Antibiótico | Percentual de Positividade | Frequencia de Germe | Perfil de Sensibilidade | Taxa de Componente Crítico | Taxa de Eventos Adversos| ApacheII.   
   Relatórios | Estatísticas | Taxa Global: O relatório de taxa global analisa através de duas dimensões Unidade Clinica, que corresponde a unidade que o paciente internou. (Andar, enfermarias e áreas criticas) e Especialidade, que corresponde a especialidade que o paciente internou (Clinica medica, ginecologia, etc.).     
   Relatórios | Estatísticas | Taxa Componente Cirúrgico, dispõe de cubos que permite realizar inúmeros agrupamentos obtendo diversos resultados.  
   Relatórios | Estatísticas | Taxa de Utilização de Antibióticos: analisa a utilização de antibiótico no hospital levando em consideração o uso por profilaxia, terapêutico (utilização hospitalar ou comunitária), o percentual hospitalar e comunitário por sitio primário de infecção;   
   Relatórios | Estatísticas | Taxa de Consumo de Antibiótico: Tendo como objetivo incluir taxa que apresente o calculo DDD (dose diária DEFINIDA) por sítio de infecção, via administração (oral e parenteral).  
   Relatórios | Estatísticas | Taxa de Cultura: Possui dois cubos estatísticos, por freqüência dos isolados e por perfil de sensibilidade. A freqüência de isolados apresenta a freqüência dos germes isolados tanto pela flora hospitalar, comunitária e demais tipo de infecção permitindo agrupar dimensões de cubos conforme necessidade de análise do Serviço. O mesmo é permitido para os cubos do perfil de sensibilidade que disponibiliza o percentual de sensibilidade de todos os antibióticos testados para cada germe isolado a partir de inúmeros agrupamentos com os cubos.   
   Relatórios | Estatísticas | Componente Crítico,  a partir dos cubos disponibiliza taxas referentes aos procedimentos invasivos (CVCP – Cateter Venoso Puncionado CVCD – Cateter Venoso Dissecado, SVD – Sonda Vesical de Demora e VAP – Ventilação Artificial Prolongada), por área critica.  O CTI Neonatal tem como parâmetro a faixa de peso.   
   Relatórios | Estatísticas | Taxa de Eventos Adversos: disponibiliza taxas que se referem aos eventos adversos não infecciosos, podendo ter como denominador a densidade de utilização dos procedimentos invasivos;  
   Relatórios | Estatísticas | ApacheII: disponibiliza taxas que se referem a previsão de mortalidade.  
   Relatórios | Indicadores Gerenciais referem-se a dados da internação do paciente como distribuição de freqüência e média de permanência.  
   Relatórios | Descritivos são relatórios que refletem os cadastros dos dados no sistema. Disponibilizam planilhas com relatórios diversos e também gráficos referentes aos mesmos. Possui descritivos de internação (admissão, alta e internados), área crítica, antibióticos, cultura (parcial e final), eventos adversos, cirurgia, infecção.  
   
\_Toc273955084**3.   Limitações**  
\_Toc81101640\_Toc81102273\_Toc81272176\_Toc94091884\_Toc94341530\_Toc102300408   
\_Toc273955085**Limitações Técnicas**  
    Relatórios descritivos com Excel 2010.  
   
\_Toc102300409\_Toc273955086**Limitações de Performance**  
    A não utilização dos filtros nas visões implica em perda de performance.  
   
\_Toc273955087\_Toc102300411**4.   Estrutura das Tabelas**  
  estruturatabelas As entidades manipuladas no aplicativo estão dispostas em diversas tabelas que classificamos de Tabelas Globais e Tabelas Específicas.   
   As Tabelas Globais são aquelas tabelas comuns a todos os segmentos da Linha RM, sendo, portanto manipuláveis por todos os segmentos;  
   As Tabelas Específicas do segmento são aquelas que se encontram disponíveis no segmento, embora possam ser encontradas também compartilhadas entre outros segmentos da Linha RM, visando garantir a integração entre os segmentos.   
   A criação de novas entidades e/ou atributos deverá ser efetuada exclusivamente pela própria TOTVS. Caso necessário, o cliente deverá encaminhar solicitação de inclusão de entidades/atributos ao Depto. de Suporte da TOTVS Sistemas para que a mesma seja encaminhada ao Departamento de Desenvolvimento para avaliação.  
   
   
\_Toc273955088**5.   Implantação**  
   
implantacaoA Área de Serviços da TOTVS visa implantar os seus produtos de acordo com os processos de cada cliente.   
Finalizada a negociação comercial, é realizado o levantamento de processos para compreender as regras do negócio do cliente e verificar se os aplicativos RM atendem às suas necessidades. Os analistas de processos são responsáveis por documentar todos os detalhes dos processos para garantir que o escopo do projeto considere todos os possíveis pontos críticos do projeto, seguindo o padrão proposto pela metodologia de implantação da TOTVS. O cliente valida os processos levantados e o gerente de projetos TOTVS apresenta o cronograma e o projeto de implantação, que informa a programação de tarefas a ser seguida para o sucesso do projeto.   
Durante a execução do projeto são realizadas reuniões de avaliação para garantir o custo e o prazo estipulados projeto. Todos os processos implementados pelos consultores de implantação TOTVS são simulados e validados pelo cliente. Testes integrados também garantem os resultados da implantação de vários módulos associados. Finalizado o período de parametrização e testes, os sistemas entram em produção e são acompanhados na fase inicial. Encerrado o projeto, o cliente assina um termo que formaliza a conclusão das tarefas e o cliente é encaminhado ao Suporte para futuros atendimentos em caso de dúvidas.  
\_Toc81101642\_Toc94091886\_Toc94341532\_Toc514942216\_Toc514943215\_Toc102465132\_Toc102814569\_Toc102818772\_Toc102965916   
Instalação do gerenciador de banco de dados - SGDB  
Deve ser providenciada, caso ainda não tenha sido realizada, instalação do gerenciador de banco de dados de preferência da empresa, conforme a necessidade, e que já se encontre instalada em outros equipamentos ou servidores: SQL e Oracle (vide versão do gerenciador no tópico Portabilidade)  
Instalação da base de dados dos aplicativos RM.  
   
\_Toc102465134\_Toc102814571\_Toc102818774\_Toc102965917\_Toc514942218\_Toc514943217Instalação dos Aplicativos RM  
Primeiramente devem ser instalados os outros aplicativos RM. Através da execução dos processos internos desses aplicativos, a base de dados será alimentada com as informações com as quais o RM Bis poderá utilizar para a geração dos cubos de decisão.  
   
\_Toc81101644\_Toc94091888\_Toc94341534\_Toc102300415\_Toc273955089**6.   Ferramentas de Saídas**  
\_Toc102473714   
\_Toc273955090**Gerador de Relatórios**  
GeradorRelatoriosOs relatórios são criados e formatados nos aplicativos da Linha RM através do recurso Gerador de Relatórios.  
Principais características:  
   Possibilita a exclusão dos relatórios executados através de agendamento conforme uma periodicidade.  
   Possibilita a exclusão de relatórios em bloco.  
   Admite a inclusão de linhas em branco em um relatório do tipo arquivo bancário  
   Permite a criação de relatórios, podendo definir níveis de acesso a esses relatórios.   
   Os relatórios criados podem ser de saída padrão (formato próprio), Texto, RTF, PDF ou Arquivo Bancário (exportação de dados).  
   Permite a visualização de relatórios em uma ou mais coligadas.  
   Permite que todos os relatórios possam ser gerados em vídeo, impressora ou arquivo, com parametrização de páginas inicial e final, bem como número desejado de cópias, entre outras opções.  
   Permite a importação/exportação de um ou mais relatórios.  
   Permite a cópia da estrutura de um relatório, gerando um novo relatório com essa estrutura.  
   Permite a visualização do relatório antes da impressão.  
   Permite gravar última configuração de impressão utilizada.  
   Permite a criação de grupos de relatórios.  
   Permite a cópia dos relatórios entre coligadas  
   Permite montar e alterar relatórios facilmente através de uma interface amigável. Além disto, será possível:  
   Inserir grupos como Cabeçalho e Rodapé de Página, Linha Detalhe, Cabeçalho e Total de Detalhe, Total de Página, Capa e Total de Relatório;  
   Visualizar os grupos de forma hierárquica facilitando a compreensão do relatório;  
   Inserir campos da base de dados, imagens, textos, fórmulas, expressões, consultas SQLs, Stored Procedure, data, hora e contador de páginas no relatório;  
   Visualizar, através de uma régua, o posicionamento dos campos no papel;  
   Mover e copiar campos do relatório;  
   Copiar a formatação de um campo;  
   Selecionar registros a serem impressos (incluir filtro);  
   Alterar a formatação do campo como fonte, borda, formato de impressão e etc.;  
   Determinar campo de ordenação e quebra do grupo;  
   Marcar grupos que não serão impressos dentre outras funcionalidades  
   
\_Toc102473715\_Toc273955091**Planilhas**  
planilhasAs Planilhas dos aplicativos RM possuem uma estrutura bastante semelhante à estrutura das planilhas do MS Excel. Pode conter várias pastas para que o usuário possa organizar vários tipos de relatórios num único arquivo.  
Principais características:  
   Permite a criação de planilhas eletrônicas.  
   Permite a inclusão de novas pastas.  
   Permite inserir sentenças SQL para obter informações da base de dados, através de uma interface amigável para a construção dessas sentenças, inclusive com passagens de parâmetros que podem referencias células da própria pasta ou de outra.  
   Permite inserir Stored Procedures.  
   Permite a inclusão e formatação de gráficos.  
   Permite a formatação dos dados da planilha, como tamanho, cor, número de casas decimais, borda e etc.  
   Permite a cópia da formatação de uma célula para outra.  
   Permite mover e copiar dados de uma célula para outra, inclusive as sentenças SQL e Stored Procedures.  
   Permite inserir e excluir linhas/colunas da planilha.  
   Permite inserir várias funções, como por exemplo, a função SUM para o somatório de uma faixa de dados.  
   Permite a exportação/importação da planilha, como por exemplo, para o MS-Excel.  
   Permite a impressão de parte da planilha (uma ou várias pastas ou mesmo parte de uma pasta).  
   Permite a impressão de uma ou várias planilhas ao mesmo tempo.  
   
\_Toc102473716**Cubos**  
cubosAtravés dos Cubos é possível realizar uma consulta em toda a base de dados dos aplicativos RM proporcionando a customização da análise e a criação de planilhas e relatórios gerenciais.   
Principais características:  
   Permite as visualizações de Cubos.  
   Permite a impressão de Cubos.  
   Permite a exportação do cubo para o MS-Excel.  
   Permite a visualização de gráficos.  
   Permite a exportação e importação de arquivos de Cubos.  
   Permite a edição dos parâmetros dos cubos que os possuem.  
   Permite a validação de senhas dos cubos que as possuem.  
   
\_Toc102473717\_Toc273955093**Relatórios Fixos**  
Os relatórios criados internamente pelo aplicativo são conhecidos como relatórios fixos.   
Os relatórios internos do aplicativo são:  
   Relatórios de Estatísticas - estes relatórios dispõem das taxas: global, componente cirúrgico, utilização de antibióticos, cultura (freqüência de isolados e perfil de sensibilidade) e eventos adversos. Estas estatísticas são disponibilizadas por cubo em que permite você relacionar, agrupar os vários dados e criar seu próprio relatório a partir de uma definição que deseja.    
    Relatórios de Indicadores Gerenciais, têm por finalidade gerenciar os vários indicadores fornecendo relatórios  que permitem o acompanhamento de diversos dados que servirão de recurso de informação não somente para o SCIH(Serviço de Controle de Infecções Hospitalares), mas, inclusive para direção do hospital. Esses indicadores têm como foco a distribuição de freqüência,  média de permanência e  taxa de ocupação.  
   Descritivos são relatórios em Excel que disponibiliza planilha com dados dos vários cadastros do produto, além de vários gráficos dos dados. Permite você monitorar a qualidade dos cadastros de entrada de dados dos pacientes. Dispõe dos relatórios descritivos de internação (por admissão, alta e internados), área crítica, antibiótico, cultura, cirurgia, infecção e eventos adversos.   
\_Toc59511253\_Toc81101647\_Toc94091891\_Toc94341537\_Toc102300418   
\_Toc273955094**GráficGraficosos**  
   
Os gráficos são resultado do processamento de uma fonte de dados e sua exposição por meio de diversos tipos de gráficos.  
Principais características:  
   Permite a criação de Categorias de Gráficos  
   Permite a associação de um Perfil de Usuário a uma categoria  
   Permite a associação de uma Categoria de Gráfico a um Gráfico  
   Permite a criação de gráficos.  
   Permite a impressão e visualização de Gráficos.  
   Permite a exportação do resultado do Gráfico.  
   Permite a visualização do Gráfico no site do RM Portal.  
   Permite a definição de parâmetros para a fonte de dados do Gráfico.  
   Permite o envio do gráfico por e-mail.  
   
\_Toc273955095**CenáriosCenarios\_Toc216601165Cenários**  
Os cenários nos permitem a criação de um espaço onde contenha vários recursos utilizados na linha RM, tais como telas em .NET, consulta SQL, Gráficos, RSS e Atendimentos.  
Principais características:  
   Permite a inclusão de uma tela .Net no Cenário.  
   Possibilita a inclusão de uma consulta SQL no Cenário.  
   Permite a inclusão de um Gráfico no Cenário.  
   Possibilita a inclusão de um RSS no Cenário.  
   Permite a inclusão da tela de Atendimentos no Cenário.  
   Possibilita a inclusão de vários cenários.  
   
\_Toc273955096**ReaderRss**  
ReaderRss\_Toc216601166Reader RSS  
Permite a leitura dos RSS TOTVS e de terceiros.  
Principais características:  
   Possibilita a inclusão de Canais RSS  
   Permite a configuração da cadência de atualização e exibição das RSS.  
   Possibilita a inclusão de canais TOTVS S.A.  
   Permite a inclusão de canais de terceiros.  
   Permite a disponibilização dos canais cadastrados no site do RM Portal.  
   
\_Toc273955097 **7.   Segurança dos produtos corporativos**  
  seguranca Disponibiliza controle de login efetuado pelo sistema, possibilitando definição das transações de inclusão, alteração e exclusão da base. Neste caso, cada usuário deverá fazer login no aplicativo com senha própria e exclusiva, cujo acesso será controlado por Perfil de acessos a Menus, Campos ou Relatórios, previamente definidos, podendo ou não realizar determinada operação, conforme lhe foi permitido no perfil atribuído por um usuário superior hierarquicamente na administração do banco de dados.   
   Permite definir diferentes níveis de acesso em cada perfil, de acordo com o grau de necessidade de acessos de cada usuário ou grupo de usuários nos aplicativos.  
   Permite a inclusão e manutenção de códigos especiais de acesso ao banco de dados. Os códigos criados referem-se ao acesso e administração do banco de dados e não usuário do aplicativo, que possui outro cadastro próprio. Desta forma, poderão ser criados no aplicativo diferentes códigos de acesso para diferentes usuários do aplicativo, podendo alguns deles ter maiores liberdades como administradores do banco de dados.  
   
\_Toc273955098**Segurança específica do TOTVS Controle de Infecção Hospitalar**  
   Funcionalidade não disponível.  
   
**8.   Integração**  
\_Toc81101649\_Toc81102276\_Toc81272179\_Toc94091893\_Toc94341539\_Toc102300420\_Toc273955100**Aplicativos do RM**   
   Funcionalidade não disponível.  
   
\_Toc273955101**Terceiros**  
   O aplicativo integra-se a outros sistemas para importar dados necessários à análise individuais dos pacientes;  
   Essa integração está relacionada à importação de internação e alta, cirurgia, cultura e Antibiótico de Paciente.  
   A partir do Importador de Dados o sistema importa os dados necessários do sistema hospitalar que o cliente utiliza sendo permitido essa integração entre os dois sistemas.  
   Acesso direto – São criados arquivos de mapeamento, com os relacionamentos das tabelas do seu sistema de gestão de saúde com as tabelas do sistema permitindo importar os dados de banco para banco.  
   
\_Toc273955102**9. Customização**  
customizacaoA TOTVS possui um departamento responsável por analisar solicitações específicas de clientes ou viabilizar prazos menores para o desenvolvimento de novos recursos. Para solicitar customizações, o cliente deve entrar em contato com o Depto. de Suporte que encaminhará a solicitação para a equipe de customizações.  
   
\_Toc273955103**10. Portabilidade**  
portabilidade\_Toc93396143\_Toc94436655\_Toc216601171Portabilidade  
Os aplicativos da linha RM são homologados para trabalhar nos servidores de banco de dados:

|  |  |  |
| --- | --- | --- |
| **SGDB** | **32 bit** | **64 bit** |
|  |  |  |
| SQL Server 2000 (SP4) | X |  |
| SQL Server 2005\* | X | X |
| SQL Server 2008\* | X |  |
| Oracle 9i (9.2.0.7) | X |  |
| 10g (10.2.0.2) | X |  |
| **11g (11.1.0.6)** | **X** |  |

* + - Os bancos de dados do SQL 2005 e SQL 2008 devem ter o Nível de Compatibilidade "SQL Server 2000 (8)" ou inferior.

      |  |
      | --- |
      | **Importante**: Antes de adquirir qualquer Sistema de Gerenciamento de Banco de Dados citado acima, consulte o site do fabricante para verificar os Requisitos de Sistema e Hardware. |

        
         
         
         
       \* O RM Portal é executado sobre a Microsoft Framework 2.0.
* Apesar de não homologadas para sistema Linux, as páginas são suportadas, não sendo de responsabilidade da TOTVS a configuração do ambiente.
* Os produtos da linha RM são homologados nesses Sistemas Operacionais utilizando o Terminal Service.  
  Não há previsão para migração dos aplicativos RM para execução em ambiente Linux ou Unix.

  | **Atenção**: A Portabilidade dos aplicativos da linha RM sofre alterações periódicas e são divulgadas na área de Cliente on-line. |
  | --- |

   |

\_Toc80503400\_Toc80503542\_Toc80520251\_Toc81101650\_Toc94091896\_Toc94341542\_Toc273955104**11.       Arquitetura**  
   
   
\_Toc102300423imagensarquiteturaREQUISITOS **MÍNIMO DE HARDWARE:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Máquinas** | **Processador** | **Memória RAM** | **HD** |
| Estação de Trabalho (cliente) | Processador Intel® Celeron® 430 (1.80 GHz, 512 KB L2 cache, 800 MHz FSB)   ou   Processador AMD Athlon™ 4050e (2.10 GHz, 512 KBx2 L2 cache) | 1GB de memória DDR2, 667MHz | Disco rígido de 160GB SATA, 3.0Gb/s |
| Servidor de Banco de Dados | Processador Intel® Xeon® Quad-Core E5345 (2.33 GHz, 2x4 MB L2 cache, 1333 MHz FSB)   Ou   Processador AMD Opteron™ Quad-Core 2356 (2.30 GHz, 75W, 1Ghz HyperTransport) | Memória de 4GB 667MHz | Disco rígido de 250GB RAID SATA, 3.0Gb/s (2 HDs de 250GB) |
| Servidor WEB | Processador Intel® Xeon® Quad-Core E5310 (1.60 GHz, 2x4 MB L2 cache, 1066 MHz FSB)   Ou   Processador AMD Opteron™ Quad-Core 2350 (2 GHz, 75W, 1Ghz HyperTransport) | Memória de 2GB 667MHz | Disco rígido de 160GB SATA, 3.0Gb/s |
| Servidor de Aplicação\* | Processador Intel® Xeon® Quad-Core E5310 (1.60 GHz, 2x4 MB L2 cache, 1066 MHz FSB)   Ou   Processador AMD Opteron™ Quad-Core 2350 (2 GHz, 75W, 1Ghz HyperTransport) | Memória de 2GB 667MHz | Disco rígido de 160GB SATA, 3.0Gb/s |
| Servidor de Terminal | Processador Intel® Xeon® Quad-Core E5345 (2.33 GHz, 2x4 MB L2 cache, 1333 MHz FSB)   Ou   Processador AMD Opteron™ Quad-Core 2356 (2.30 GHz, 75W, 1Ghz HyperTransport) | Memória de 4GB 667MHz | Disco rígido de 250GB RAID SATA, 3.0Gb/s (2 HDs de 250GB) |

\*Servidor de Aplicação: Este servidor hospeda os arquivos e serviços da aplicação da linha RM.  
   
ATENÇÃO! As configurações acima suportam no máximo 50 acessos por servidor. Para mais informações, entre em contato com a TOTVS BH.  
   
ARQUITETURA **CLIENTE-SERVIDOR (DELPHI).**  
   
   
**Na arquitetura** Cliente Servidor, o cliente acessa o Servidor de Banco de Dados através da camada BDE.  
   
ARQUITETURA RM WINFORM  
   
Na arquitetura RM Winform, o cliente através de uma biblioteca cliente acessa ao Servidor de Aplicação via Remoting que por sua vez acessa ao Servidor de Banco de Dados via ADO.Net.  
   
ACESSO AO RM PORTAL VIA INTRANET E EXTRANET.  
   
Para a arquitetura Web, o cliente acessa o Servidor Web, onde está instalado o RM Portal, via intranet ou extranet (acessando a intranet atrvés da internet). O Servidor de Banco de Dados possui uma camada de Biblioteca cliente que acessa via Remoting o Servidor de Aplicações que por sua vez acessa ao Servidor de Banco de Dados via ADO.Net.  
   
 ARQUITETURA RM VIA TERMINAL SERVICE  
   
   
   
A arquitetura RM via Terminal Service permite o cliente acessar o Servidor de Terminal Service na rede da empresa ou via internet e utilizar os produtos da Linha RM seguindo a mesma arquitetura de Winform e Webform.  
   
\_Toc273955105**12. Módulos do RM Portal**  
   Funcionalidade não disponível.
