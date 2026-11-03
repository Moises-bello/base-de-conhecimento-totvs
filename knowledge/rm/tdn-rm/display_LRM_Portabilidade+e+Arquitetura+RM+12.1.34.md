---
content_hash: 648bce72452c4033186726d3709db034068e4e52dd44a5a6585781c9e8521b0f
fetched_at: '2026-06-29T00:11:10.985615+00:00'
page_id: '644720148'
product: rm
source: tdn-rm
title: Portabilidade e Arquitetura RM 12.1.34
type: documentation
url: https://tdn.totvs.com/display/LRM/Portabilidade+e+Arquitetura+RM+12.1.34
version: 15
---

O documento de Portabilidade e Arquitetura RM serve de orientação para as configurações de ambiente que devem ser utilizadas em sua empresa, buscando o melhor desempenho e usabilidade do RM.  
As informações contidas na Portabilidade e Arquitetura RM têm como objetivo apresentar quais os principais sistemas operacionais e navegadores de internet devem ser utilizados para o correto funcionamento do RM.  
O dimensionamento de hardware deste documento é apenas um informativo para uma empresa de médio porte, do contrário, deve-se verificar os requisitos de software e hardware, que melhor se adequem à sua empresa, junto ao Executivo de Conta.

2

## Portabilidade para Servidor de Banco de Dados

### Versões homologadas

| SGBD | 32Bits | 64Bits | Versão/Patch | Info TOTVS |
| --- | --- | --- | --- | --- |
| SQL Server 2012 | X | X | SP3 |  |
| SQL Server 2014 |  | X | SP2 | Recomendado |
| SQL Server 2016 |  | X | SP1 | Recomendado |
| SQL Server 2017 |  | X | RTM | Recomendado |
| SQL Server 2019 |  | X | RTM | Recomendado |
| Oracle 11g | X | X | 11.2.0.1 |  |
| Oracle 12c |  | X | 12.1.0.1  12.2.0.1 |  |
| Oracle 18c |  | X | 18.5.0.0.0 | Recomendado |
| Oracle 19c\* |  | X | 19.3.0.0.0 | Recomendado |

\***Obs.**: O uso de aplicativos Delphi com o Oracle 19c demandam configurações específicas do SGDB ([Uso de Aplicativos Delphi com o oracle 19C](https://tdn.totvs.com.br/display/LRM/Uso+de+Aplicativos+Delphi+com+o+oracle+19C)), que podem gerar variações em sua performance.

### Codificação de Caracteres (“Collation” do SQL Server e “Character Set” do Oracle)

| SGBD | Collation/Character Set |
| --- | --- |
| SQL Server | SQL\_Latin1\_General\_CP1\_CI\_AI |
| Oracle 11G  Oracle 12C + | WE8ISO8859P1  WE8ISO8859P1\*, WE8ISO8859P15 |

\*Obs: A partir do Oracle 12c  o Character Set "WE8ISO8859P15" é a opção recomendada pela Oracle. Alterações realizadas no Character Set devem ser analisados pelo DBA responsável.

Devido a restrições na Edição Oracle XE 11G de criação do banco de dados com "CharacterSet" diferente de Unicode(AL32UTF8), não é recomendado o uso do mesmo, tendo em vista que o mesmo não atende aos requisitos de Codificação de Caracteres.

### Requisitos de Hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado |
| Intel® Xeon® 3060 (4M  Cache, 2.40 GHz, 1066 MHz  FSB) ou SIMILAR | 8GB | 16GB | Disco SAS 15k, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® W3540 (8M  Cache, 2.93 GHz, 4.80 GT/s  Intel® QPI) ou SIMILAR | 16GB | 32GB | Disco SAS 15k, Placa  Controladora com 256 MB | A cada 100 usuários |

### Restrições e avisos importantes

* As bases de dados RM são compatíveis com TDE (Transparent Data Encryption) para os SGBD’s SQL (2012, 2014, 2016, 2017 e 2019) e Oracle (11g, 12c e 18c). Para mais informações com relação ao TDE, favor verificar em:
  + [TDE SQL Server](https://docs.microsoft.com/pt-br/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver15)
  + [TDE Oracle 11g](https://oracle-base.com/articles/11g/tablespace-encryption-11gr1#tablespace_creation)
  + [TDE Oracle 12c e 18c](https://docs.oracle.com/database/121/ASOAG/configuring-transparent-data-encryption.htm#ASOAG10285)
* A Collation (SQL Server) e o Character Set (Oracle) são codificações de caracteres existentes nos Banco de Dados. Para o correto funcionamento do RM em seu ambiente, certifique-se que as configurações de Collation eCharacter Set estão de acordo com a tabela de codificação de caracteres.
* O banco de dados da RM não suporta replicação total (de todas as tabelas) da base de dados.
* Em ambientes integrados, certifique-se que a base de dados estejaem uma instância diferente de uma base do TOTVS Protheus, devido à distinção de Collations ou Character Sets utilizados nestas soluções. Essa configuração garante bom funcionamento da base de dados.
* Informamos que uma vez ativo o Log de Auditoria, informações em campos do tipo IMAGE, TEXT, MEMO, DIMAGEM e VARCHAR(MAX) para SQL e LONG, LONG RAW, BLOB e CLOB para Oracle, não serão armazenadas. Esta condição tem por finalidade evitar o crescimento excessivo da base de dados e manter sua performance.
* A TOTVS homologou o Oracle nas versões 12c, 18c e 19c utilizando PDB's.

## Níveis de Compatibilidade entre Bancos de Dados

Os SGBD’s são responsáveis por definir níveis de compatibilidade para os Bancos de Dados, a fim de permitir trabalhar em diferentes versões do SQL Server. Abaixo a tabela que representa o nível de compatibilidade suportado nos ambientes da RM e quais níveis de compatibilidade os SGBD’s suportam:

| Versão SQL Server | Níveis de Compatibilidade Suportados no ambiente RM | |
| --- | --- | --- |
| SQL Server 2012 | SQL Server 2012(110) | SQL Server 2014(120) |
| SQL Server 2014 | SQL Server 2012(110) | SQL Server 2014(120) |
| SQL Server 2016 | SQL Server 2012(110) | SQL Server 2014(120) |
| SQL Server 2019 | SQL Server 2012(110) | SQL Server 2014(120) |

A partir da release12.1.17, devido a mudança de comportamento na quebra para conversão de formatos de data realizada pela Microsoft, o produto RM não permitirá uso do nível de compatibilidade (130) disponível no SQL Server 2016 e Azure SQL Database. Neste caso o nível de compatibilidade do banco deve ser alterado para os valores antecedentes ao SQL Server 2016 (100 | 110 | 120) até que as adequações necessárias sejam realizadas nas releases futuras. Abaixo link com a especificação da alteração realizada pela Microsoft: .

Devido ao final do suporte estendido pela Microsoft em relação às plataformas de banco de dados MS SQL Server 2008 e MS SQL Server 2008R2, previsto para 09/07/2019, comunicamos que estas também deixarão de fazer parte da portabilidade de toda linha de produtos RM a partir do Release 12.1.25. [Veja o link](https://support.microsoft.com/pt-br/lifecycle/search?alpha=sql%20server%202008) da documentação oficial da Microsoft sobre o fim do suporte estendido as versões afetadas.

### Restrições e avisos importantes

* O nível de compatibilidade do SQL Server 2000 com outros SGBD’s NÃO confirma que a TOTVS, Linha RM, dará suporte ao banco de dados SQL Server 2000.
* A partir da versão SQL Server 2012 o nível de compatibilidade SQL 2000(80) não será mais suportado. Isso porque a Microsoft dará suporte apenas as duas últimas versões disponíveis no mercado. Mais detalhes sobre níveis de compatibilidade no site da Microsoft: [Clicando aqui](https://docs.microsoft.com/pt-br/sql/database-engine/deprecated-database-engine-features-in-sql-server-2016?redirectedfrom=MSDN&view=sql-server-ver15).
* Para uso de aplicativos Win32 (Delphi) com SGBD igual ou superior ao SQL Server 2012, torna-se necessário criação de uma conexão ODBC. Para maiores informações acesse:

## Portabilidade Para Servidor de Aplicação

### Requisitos de software

| Sistema Operacional | 32bits | 64bits |
| --- | --- | --- |
| Windows Server 2012 |  | X |
| Windows Server 2012  R2 |  | X |
| Windows Server 2016 |  | X |
| Windows Server 2016 Core |  | X |
| Windows Server 2019 |  | X |

| Softwares | 32bits | 64bits |
| --- | --- | --- |
| Microsoft  ou superior | X | X |
| Visual C++ Redistributable for Visual Studio 2015 | X | X |

### Requisitos de hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado\* |
| Intel® Xeon® 3060 (4M Cache, 2.40 GHz, 1066 MHz FSB) ou SIMILAR | 2GB | 4GB | Disco SAS 15k 72GB, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® 3060 (4M Cache, 2.40 GHz, 1066 MHz FSB) ou SIMILAR. | 8GB | 12GB | Disco SAS 15k 75GB, Placa  Controladora com 256 MB | A cada 100 usuários |

### Restrições e avisos importantes

* Utilizar um servidor de aplicação diferente do servidor de JobServer, responsável pela execução dos processos dentro do RM.
* É recomendado que seja utilizada a versão do  igual ou superior a versão 4.8, de acordo com o sistema operacional.

## Portabilidade Para Servidor de Job

### Requisitos de software

| Sistema Operacional | 32bits | 64bits |
| --- | --- | --- |
| Windows Server 2012 |  | X |
| Windows Server 2012  R2 |  | X |
| Windows Server 2016 |  | X |
| Windows Server 2016 Core |  | X |
| Windows Server 2019 |  | X |

| Softwares | 32bits | 64bits |
| --- | --- | --- |
| Microsoft  ou superior | X | X |

### Requisitos de hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado\* |
| Intel® Xeon® 3060 (4M Cache, 2.40 GHz, 1066 MHz FSB) ou SIMILAR | 2GB | 4GB | Disco SAS 15k 72GB, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® 3060 (4M Cache, 2.40 GHz, 1066 MHz FSB) ou SIMILAR. | 8GB | 12GB | Disco SAS 15k 75GB, Placa  Controladora com 256 MB | A cada 100 usuários |

### Restrições e avisos importantes

Os requisitos de hardware podem alterar de acordo com a demanda do servidor. É importante o acompanhamento da carga, pois existem variáveis que influenciam diretamente na performance, como: quantidade de usuários que executam processos, quantidade de processos, volume de dados que o processo está executando e recorrência dos mesmos.

## Portabilidade para Servidor de Terminal Service

O Terminal Services é um serviço que nos permite acessar computadores remotamente e usar aplicativos, através de qualquer computador cliente. Ideal quando os computadores clientes não possuírem hardware suficiente para processar determinadas tarefas. Com a utilização do Terminal Services, o processamento é executado no servidor onde é hospedada a aplicação da Linha RM.

### Requisitos de software

| Sistema Operacional | 32bits | 64bits |
| --- | --- | --- |
| Windows Server 2012 (Terminal Service) |  | X |
| Windows Server 2016 |  | X |
| Windows Server 2016 Core |  | X |
| Windows Server 2019 |  | X |

### Requisitos de hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado\* |
| Intel® Xeon® E3-1220 v6 (vCPU 4, Threads 4, 3.00 GHz,  8 MB Cache) ou SIMILAR | 12GB | 16GB | Disco SAS 15k 72GB, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® E3-1230 v6  (vCPU 4, Threads 8, 3.50 GHz,  8 MB Cache) ou SIMILAR | 24GB | 32GB | Disco SAS 15k 75GB, Placa  Controladora com 256 MB | A cada 100 usuários |

Obs.: Estas configurações foram dimensionadas para camada Client, considerando a utilização do Produto através da MDI.

### Restrições e avisos importantes

* Informamos que o RM não suporta a execução em computadores Thin-Client (Diskless), entretanto este tipo de Hardware pode ser usado em conjunto com Servidores de Terminal Services, desde que os requisitos mínimos de memória e hardware para o software TOTVS da linha RM, neste ambiente, sejam respeitados.

## Portabilidade para Estações de Trabalho

### Requisitos de software

| Sistema Operacional | 32bits | 64bits |
| --- | --- | --- |
| Windows 8.1 Pro | X | X |
| Windows 10 Pro | X | X |

| Softwares | 32bits | 64bits |
| --- | --- | --- |
| Microsoft  ou superior | X | X |
| Visual C++ Redistributable for Visual Studio 2015 | X | X |
| BDE | X | X |

### Versões de navegadores Web homologadas

| Sistema Operacional | Internet Explorer | Mozilla Firefox | Safari | Google Chrome | Microsoft Edge |
| --- | --- | --- | --- | --- | --- |
| Windows 8.1 Pro | Versão 11.0.XX | Versão 45.0.XX | Versão 5.1.7 | Versão 55.0.2883.87 | Versão 85.0.XX |
| Windows 10 Pro | Versão 11.0.XX | Versão 45.0.XX | Versão 5.1.7 | Versão 55.0.2883.87 | Versão 85.0.XX |
| Mac OS X |  |  | Versão 4.0 |  |  |
| iOS (iPad) |  |  | Versão 5.0.2 |  |  |

### Requisitos de hardware

| Processador | Memória RAM | HD/Outros |
| --- | --- | --- |
| Intel® Core™ 2 Duo® de 1.6  GHz ou SIMILAR | 2GB | Espaço disponível em disco de 1  Gbyte para instalação dos produtos. |

### Suporte a ambientes especiais

* Ambiente três camadas com as estações “Cliente” dentro da mesma rede do Servidor de Aplicação está homologado para os produtos RM.
* Ambiente três camadas com as estações de trabalho conectando-se a Servidores de Aplicação via internet através de IP Fixo são suportados, mas possuem restrições de desempenho.
* Ambiente três camadas com as estações clientes conectando-se ao Servidor de Aplicação pela internet através de IP Dinâmico. Este ambiente deve passar por consultoria do Datacenter TOTVS e possui restrições de desempenho.
* É recomendado que seja utilizada a versão do  igual ou superior a versão 4.8, de acordo com o sistema operacional.

### Suporte a versões do Microsoft Office

A partir da versão 12.1.5 os produtos da linha não precisam do Pacote Microsoft Office instalado em suas estações para uso, porém algumas funcionalidades, como Planilhas.Net, são incompatíveis com alguns pacotes. Para uso destas funcionalidades a versão do Microsoft Office de sua estação de trabalho deverá ser uma das listadas abaixo:

| Versão do Office | Pacote | 32bits | 64bits |
| --- | --- | --- | --- |
| Microsoft Office 2019 | Professional Plus | X | X |
| Microsoft Office 2016 | Professional Plus | X | X |
| Microsoft Office 2013 | Standard | X | X |
| Professional Plus | X | X |

Versões da suíte Office

Não são homologadas versões limitadas e tipicamente classificadas como "básicas" por se tratarem de distribuições compactas e que apresentam a falta ou incompatibilidade de componentes.

### Restrições e avisos importantes

* A resolução de vídeo mínima para a execução dos produtos da linha RM é de 1280 x 1024 pixels.
* A TOTVS alerta que não existe versão do BDE para estações 64bit’s.
* O componente Planilha .Net funciona somente nas versões acima mencionadas. Esta mudança está aplicada tanto para as aplicações RM como para nosso novo Front-End, o RM.exe.

## Portabilidade Para Servidor WEB

### Requisitos de software

| Sistema Operacional | 32bits | 64bits |
| --- | --- | --- |
| Windows Server 2012 |  | X |
| Windows Server 2012  R2 |  | X |
| Windows Server 2016 |  | X |
| Windows Server 2016 Core |  | X |
| Windows Server 2019 |  | X |

| Softwares | 32bits | 64bits |
| --- | --- | --- |
| Microsoft  ou superior | X | X |

### Requisitos de hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado\* |
| Intel® Xeon® 3060 (4M Cache, 2.40 GHz, 1066 MHz FSB) ou SIMILAR. | 8GB | 16GB | Disco SAS 15k, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® W3540 (8M Cache, 2.93 GHz, 4.80 GT/s Intel® QPI) ou SIMILAR. | 16GB | 32GB | Disco SAS 15k 75 Placa  Controladora com 256 MB | A cada 100 usuários |

### Restrições e avisos importantes

* Para maiores informações consulte seu Administrador de Rede.
* Para garantir ainda mais a segurança na utilização dos nossos portais WEB, recomendamos uso de protocolo HTTPS.
* Para versão do IIS 6 ou inferior, deve-se instalar o RM Portal como um “Diretório Virtual” e não como Web Site. Em versões superiores, a instalação deve ser como “Aplicativo”.
* É recomendado que seja utilizada a versão do  igual ou superior à versão 4.8, de acordo com o sistema operacional.

## Portabilidade para Estações Disk-Less (Thin-Client)

Informamos que o RM não suporta a execução em computadores Thin-Client (Diskless), entretanto este tipo de Hardware pode ser usado em conjunto com Servidores de Terminal Services, desde que os requisitos mínimos de memória e hardware para o software TOTVS RM neste ambiente sejam respeitados.

## Portabilidade específica por Segmentos

Para especificidades de cada segmento, conferir o documento a seguir: 

## Arquitetura suportada

### Cliente/Servidor

A arquitetura Cliente/Servidor é estruturada em duas camadas. A primeira camada é onde se localiza o aplicativo. Essa camada é responsável pela regra de negócio, comandos de manipulação de dados e interface com o usuário. A troca de dados é realizada pelo framework de comunicação WCF (protocolo TCP e/ou HTTP), onde são enviados dados como mensagens assíncronas de um ponto de extremidade de serviço para outro. Veja sobre [WCF](https://docs.microsoft.com/pt-br/dotnet/framework/wcf/whats-wcf). A segunda camada é onde se encontra a base de dados, responsável pelo armazenamento de informações e execução dos comandos oriundos da camada cliente.

### Multicamadas

A arquitetura Multicamadas é estruturada para poder dar uma maior mobilidade, desempenho e facilidade de manutenções na aplicação. Em seu conceito geral, essa arquitetura, possui no mínimo 3 camadas. A primeira camada contempla a interface com o usuário. A segunda camada é responsável pelo tratamento da regra de negócio do aplicativo. Já a terceira camada é responsável pelas transações do banco de dados.

### Web

A arquitetura Web, o cliente acessa o Servidor Web, onde está instalado o TOTVS Portal, via intranet ou internet. O Servidor Web possui uma camada de Biblioteca cliente, onde se localiza a camada de interface com o usuário, que acessa via WCF o Servidor de Aplicações. Este por sua vez acessa ao Servidor de Banco de Dados via ADO.Net.

### Terminal Service

A arquitetura RM via Terminal Service permite o cliente acessar o Servidor de Terminal Service na rede da empresa ou via internet e utilizar os produtos da Linha RM seguindo a mesma arquitetura de Winform e Webform.

### Restrições e avisos importantes

Durante a instalação, por padrão, são configuradas as seguintes portas de conexão.

* RM.exe, portais e TBC (IIS) comunicam com o servidor de aplicação (HOST) através das portas 8050 e 8051.
* Servidor de aplicação e o servidor de Job’s comunicam com o banco de dados através da porta 8050.
* Servidor de aplicação comunica com o servidor de Job's pela porta 8050.
* Recomendamos que os Servidores de Job’s se comuniquem através da porta 8050.
* Se o cliente expõe seus WebServices externamente, deve-se liberar no Firewall a porta utilizada.

## License Server

O TOTVS License Server é parte do modelo de Licenciamento TOTVS FULL, que controla as licenças de uso de seu software. Uma maneira segura e eficiente de gerenciamento de licenças para os módulos e funcionalidades da TOTVS.

Para maiores informações consulte: .

## Recomendações

* A partir da 12.1.17 é necessário a instalação do  para integração das informações do E-Social.
* Para ambiente com grande volume de processamento, a TOTVS recomenda o uso de um servidor de aplicação.
* Processos para Geração de Cubos e Relatórios, Cálculo de Folha, devem ser agendados para períodos de menor carga de processamento dos servidores.
* Utilize filtros que retornem no máximo 200 registros na visão.
* No cadastro de Servidores de Aplicação, utilize o campo “Número máximo de Registros” para limitar os registros retornados do banco de dados. Para mais informações, acesse o [link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016013767-RM-Frame-Aumentar-quantidade-de-registros-na-vis%C3%A3o-Servidores-de-Aplica%C3%A7%C3%A3o-).
* Não utilize a base de produção para Armazenamento dos Cubos.
* ATENÇÃO: Visando a consistência e melhoria nos processos de banco de dados, a TOTVS orienta aos clientes para que evitem a criação de tabelas, índices ou outros objetos de banco de dados que não sejam do padrão da base original. Caso seja necessário criar algum objeto na base original que não seja referente a alguma customização, pedimos que abram um chamado na TOTVS para que seja feita uma análise da viabilidade de incluirmos esse objeto na base padrão (sendo aprovada a inclusão isso será feito no próximo conversor a ser disponibilizado). Esta medida se faz necessária, para assegurar uma maior consistência da estrutura da base de dados, pois quando a migração de versão ocorre, alguns dos objetos criados pelos clientes podem ser excluídos ou sofrer alterações, o que pode acarretar interferência em processos de integração de terceiros ou alguma outra rotina atrelada ao produto. Reforçamos que a responsabilidade pela manutenção de objetos específicos é toda do cliente. Para maiores informações entre em contato nosso suporte de banco de dados.
* É altamente recomendado que a rede de comunicação do servidor de Banco de Dados, servidor Web, servidor de Aplicação e servidor de Terminal Service seja Gigabit. Para maiores informações consulte seu Administrador de Rede.
* O RM não prestará suporte em sistemas operacionais, produtos ou serviços, incluindo o Office, fora do ciclo de vida estabelecido pela Microsoft.
* A partir da versão 12.1.27 será pré-requisito o sistema a instalação do "Visual C++ Redistributable for Visual Studio 2015", lembrando que até a versão 12.1.26 já era necessário a instalação do "Visual C++ Redistributable for Visual Studio 2012" para funcionamento do Totvs Mashup
* Framework 4.8A partir da versão 12.1.34 a atualização do .NET Framework 4.8 passa a ser obrigatória e deve estar atualizada com a última Release que pode ser realizada através do Windows Update, pacote cumulativo KB a depender da versão do Windows.

**Para mais informações entre em contato com o Help Desk TOTVS 4003-0015**
