---
content_hash: f50a9855a2df5a8b663a8be1be7e2a68f3f7aa7634a0ce02a6fe6116c7059503
fetched_at: '2026-06-29T00:05:53.265377+00:00'
page_id: '1068938066'
product: rm
source: tdn-rm
title: Portabilidade e Arquitetura RM 12.1.2606
type: documentation
url: https://tdn.totvs.com/display/LRM/Portabilidade+e+Arquitetura+RM+12.1.2606
version: 3
---

O documento de Portabilidade e Arquitetura RM serve de orientação para as configurações de ambiente que devem ser utilizadas em sua empresa, buscando o melhor desempenho e usabilidade do RM.  
As informações contidas na Portabilidade e Arquitetura RM têm como objetivo apresentar quais os principais sistemas operacionais e navegadores de internet devem ser utilizados para o correto funcionamento do RM.  
O dimensionamento de hardware deste documento é apenas um informativo para uma empresa de médio porte, do contrário, deve-se verificar os requisitos de software e hardware, que melhor se adequem à sua empresa, junto ao Executivo de Conta.

2

## Portabilidade para Servidor de Banco de Dados

### Versões homologadas

| SGBD | 32Bits | 64Bits | Nível de Compatibilidade Padrão | Versão/Patch | Info TOTVS | Observações | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SQL Server 2012 | X | X | 110 | SP3 | **Não suportado** | Término do suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/microsoft-sql-server-2012). | RedNot Supported |
| SQL Server 2014 |  | X | 120 | SP2 |  | Término do suporte estendido, mais informações [acesse aqui](https://learn.microsoft.com/pt-br/lifecycle/products/sql-server-2014). | YellowEOL |
| SQL Server 2016 |  | X | 130 | SP1 |  | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/sql-server-2016). | YellowEOL |
| SQL Server 2017 |  | X | 140 | RTM |  | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/sql-server-2017). | YellowEOL |
| SQL Server 2019 |  | X | 150 | RTM | Recomendado |  | GreenSupported |
| SQL Server 2022 |  | X | 160 | [CU5](https://www.microsoft.com/download/details.aspx?id=105013) | Recomendado | **Importante:** Aplicar [atualização cumulativa 5](https://learn.microsoft.com/pt-br/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate5) ou superior. | GreenSupported |
| SQL Server 2025 |  | X | 170 | RTM | Recomendado |  | GreenSupported |
| Oracle 12c |  | X | **Não se aplica** | 12.2 | **Não suportado** |  | RedNot Supported |
| Oracle 18c |  | X | **Não se aplica** | 18.5.0.0.0 |  | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html#:~:text=Premier%20Support%20(PS)%20ended%20Jul,effect%20until%20July%2031%2C%202019.). | YellowEOL |
| Oracle 19c\* |  | X | **Não se aplica** | 19.3.0.0.0 | Recomendado |  | GreenSupported |

\***Obs.**: O uso de aplicativos Delphi com o Oracle 19c demandam configurações específicas do SGDB ([Uso de Aplicativos Delphi com o oracle 19C](https://tdn.totvs.com/x/i1GcJQ)), que podem gerar variações em sua performance.

IMPORTANTE

A partir da release 12.1.2510 todas as versões não suportadas passam a ter seu uso impedido na atualização da base de dados Linha RM.

A partir da release 12.1.2702 o nível 120 passa a ter o seu uso impedido na atualização da base de dados Linha RM.

Oracle 12c, 11g e anteriores.SQL Server 2012 e anteriores.

### Codificação de Caracteres (“Collation” do SQL Server e “Character Set” do Oracle)

| SGBD | Collation/Character Set |
| --- | --- |
| SQL Server | SQL\_Latin1\_General\_CP1\_CI\_AI |
| Oracle 18C + | WE8ISO8859P15  WE8MSWIN1252 |

Devido a restrições na Edição Oracle XE de criação do banco de dados com "CharacterSet" diferente de Unicode(AL32UTF8), não é recomendado o uso do mesmo, tendo em vista que o mesmo não atende aos requisitos de Codificação de Caracteres.

### Requisitos de Hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado |
| Intel® Xeon® 3060 (4M  Cache, 2.40 GHz, 1066 MHz  FSB) ou SIMILAR | 8GB | 16GB | Disco SAS 15k, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® W3540 (8M  Cache, 2.93 GHz, 4.80 GT/s  Intel® QPI) ou SIMILAR | 16GB | 32GB | Disco SAS 15k, Placa  Controladora com 256 MB | A cada 100 usuários |

### Restrições e avisos importantes

* As bases de dados RM são compatíveis com TDE (Transparent Data Encryption) para os SGBD’s SQL ( 2016, 2017,  2019 e 2022) e Oracle (18c). Para mais informações com relação ao TDE, favor verificar em:
  + [TDE SQL Server](https://docs.microsoft.com/pt-br/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver15)
  + [TDE Oracle 18c](https://docs.oracle.com/database/121/ASOAG/configuring-transparent-data-encryption.htm#ASOAG10285)
* A Collation (SQL Server) e o Character Set (Oracle) são codificações de caracteres existentes nos Banco de Dados. Para o correto funcionamento do RM em seu ambiente, certifique-se que as configurações de Collation eCharacter Set estão de acordo com a tabela de codificação de caracteres.
* O banco de dados da RM não suporta replicação total (de todas as tabelas) da base de dados.
* Em ambientes integrados, certifique-se que a base de dados estejaem uma instância diferente de uma base do TOTVS Protheus, devido à distinção de Collations ou Character Sets utilizados nestas soluções. Essa configuração garante bom funcionamento da base de dados.
* Informamos que uma vez ativo o Log de Auditoria, informações em campos do tipo IMAGE, TEXT, MEMO, DIMAGEM e VARCHAR(MAX) para SQL e LONG, LONG RAW, BLOB e CLOB para Oracle, não serão armazenadas. Esta condição tem por finalidade evitar o crescimento excessivo da base de dados e manter sua performance.
* A TOTVS homologou o Oracle nas versões 18c e 19c utilizando PDB's.

---

## Níveis de Compatibilidade entre Bancos de Dados Sql Server

* Quanto à compatibilidade do SGBD SQL Server, considere a tabela na seção "**Portabilidade para Servidor de Banco de Dados**", estando dentro da portabilidade somente as versões com status "**EOL**" e "**SUPPORTED**", conjuntamente com seus níveis de compatibilidade padrão.

  O nível de compatibilidade mínimo aceito na Linha RM será determinado pelo padrão da menor versão com status "**EOL**" mencionada na lista "Portabilidade para Servidor de Banco de Dados", sendo sugerido a utilização do nível de compatibilidade padrão da versão do SQL Server em uso.

  **Exemplo:** O nível de compatibilidade 120 não é mais homologado, visto que o SQL Server 2014, que possui este como padrão, não é suportado na portabilidade.
* Cada versão do SQL Server possui um nível de compatibilidade padrão, podemos ver detalhes nesta página da Microsoft: [Níveis de compatibilidade do SQL Server](https://learn.microsoft.com/pt-br/sql/t-sql/statements/alter-database-transact-sql-compatibility-level?view=sql-server-ver16)

Para uso de aplicativos Win32 (Delphi) com SGBD igual ou superior ao SQL Server 2014, torna-se necessário criação de uma conexão ODBC. Para maiores informações acesse:

---

## Portabilidade para Servidor de Aplicação e Servidor de Job

### Requisitos de software

| Sistema Operacional | 32bits | 64bits | Observações | Status |
| --- | --- | --- | --- | --- |
| Windows Server 2016 |  |  |  | RedNOT Supported |
| Windows Server 2019 |  | X | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/windows-server-2019). Apenas a partir do build 17763.3165. | YellowEOL |
| Windows Server 2022 |  | X | Em suporte padrão, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/windows-server-2022). | GreenSupported |
| Windows Server 2025 |  | X | Em suporte padrão, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/windows-server-2025). | GreenSupported |

| Softwares | 32bits | 64bits | Status |
| --- | --- | --- | --- |
| Microsoft .NET Framework 4.8 |  | X | GreenSupported |
| Visual C++ Redistributable for Visual Studio 2015 |  | X | GreenSUPPORTED |

### Requisitos de hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado\* |
| Intel® Xeon® 3060 (4M Cache, 2.40 GHz, 1066 MHz FSB) ou SIMILAR | 2GB | 4GB | Disco SAS 15k 72GB, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® 3060 (4M Cache, 2.40 GHz, 1066 MHz FSB) ou SIMILAR. | 8GB | 12GB | Disco SAS 15k 75GB, Placa  Controladora com 256 MB | A cada 100 usuários |

### Restrições e avisos importantes

* Utilizar um Servidor de Aplicação diferente do Servidor de JobServer, responsável pela execução dos processos dentro do RM.
* Os requisitos de hardware podem alterar de acordo com a demanda do servidor. É importante o acompanhamento da carga, pois existem variáveis que influenciam diretamente na performance, como: quantidade de usuários que executam processos, quantidade de processos, volume de dados que o processo está executando e recorrência dos mesmos.

---

## Portabilidade para Servidor Web

### Requisitos de software

| Sistema Operacional | 32bits | 64bits | Observações | Status |
| --- | --- | --- | --- | --- |
| Windows Server 2016 |  |  |  | RedNOT Supported |
| Windows Server 2019 |  | X | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/windows-server-2019). Apenas a partir do build 17763.3165. | YellowEOL |
| Windows Server 2022 |  | X |  | GreenSupported |
| Windows Server 2025 |  | X |  | GreenSupported |

| Softwares | 32bits | 64bits | Status |
| --- | --- | --- | --- |
| Microsoft .NET Framework 4.8 |  | X | GreenSupported |

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

---

## Portabilidade para Servidor de Terminal Service

O Terminal Services é um serviço que nos permite acessar computadores remotamente e usar aplicativos, através de qualquer computador cliente. Ideal quando os computadores clientes não possuírem hardware suficiente para processar determinadas tarefas. Com a utilização do Terminal Services, o processamento é executado no servidor onde é hospedada a aplicação da Linha RM.

### Requisitos de software

| Sistema Operacional | 32bits | 64bits | Observações | Status |
| --- | --- | --- | --- | --- |
| Windows Server 2016 |  |  |  | RedNOT Supported |
| Windows Server 2019 |  | X | Término do suporte padrão, em suporte estendido, mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/windows-server-2019). Apenas a partir do build 17763.3165. | YellowEOL |
| Windows Server 2022 |  | X |  | GreenSupported |
| Windows Server 2025 |  | X |  | GreenSupported |

### Requisitos de hardware

| Processador | Memória RAM | | HD/Outros | Núm. de Usuários |
| --- | --- | --- | --- | --- |
| Mínimo | Recomendado\* |
| Intel® Xeon® E3-1220 v6 (vCPU 4, Threads 4, 3.00 GHz,  8 MB Cache) ou SIMILAR | 12GB | 16GB | Disco SAS 15k 72GB, Placa  Controladora com 256 MB | 20 |
| Intel® Xeon® E3-1230 v6  (vCPU 4, Threads 8, 3.50 GHz,  8 MB Cache) ou SIMILAR | 24GB | 32GB | Disco SAS 15k 75GB, Placa  Controladora com 256 MB | A cada 100 usuários |

Obs.: Estas configurações foram dimensionadas para camada Client, considerando a utilização do Produto através da MDI.

### Uso de espaço em disco do WebView2

O WebView 2 é um runtime para plataforma Web, contém binários modificados do Microsoft Edge, ele funciona como um aplicativo de navegador mas é visível apenas dentro do RM. Portanto ele armazena todos os recursos de um navegador, como Cookies, Cache de paginas e demais dados necessários para navegação, assim como o Microsoft Edge.

Estes dados são armazenados na pasta do usuário Windows, é a pasta padrão onde os navegadores salvam seus dados:

"***C:\Users\%USERNAME%\AppData\Local\RM.exe.WebView2***"  
ou  
"**%LOCALAPPDATA%\RM.exe.WebView2**"

Pode inicialmente consumir a partir de 15Mb de espaço em disco, de cada usuário do Windows que acessa o RM, o consumo poderá subir de acordo com a utilização de cada página Web aberta dentro do RM.

### Restrições e avisos importantes

* Informamos que o RM não suporta a execução em computadores Thin-Client (Diskless), entretanto este tipo de Hardware pode ser usado em conjunto com Servidores de Terminal Services, desde que os requisitos mínimos de memória e hardware para o software TOTVS da linha RM, neste ambiente, sejam respeitados.

---

## Portabilidade para Estações de Trabalho

### Requisitos de software

| Sistema Operacional | 32bits | 64bits | Observações | Status |
| --- | --- | --- | --- | --- |
| Windows 10 Pro |  |  | Término do suporte estendido (mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/windows-10-home-and-pro)) | RedNot Supported |
| Windows 11 Pro |  | X | Versões 24H2 e 25H2  (mais informações [acesse aqui](https://docs.microsoft.com/pt-br/lifecycle/products/windows-11-home-and-pro-version-21h2)) | GreenSupported |

| Softwares | 32bits | 64bits | Status |
| --- | --- | --- | --- |
| Microsoft .NET Framework 4.8 |  | X | GreenSupported |
| BDE |  | X | GreenSupported |
| WebView2 Runtime |  | X | GreenSupported |
| Visual C++ Redistributable for Visual Studio 2015 |  | X | GreenSUPPORTED |

### Versões de navegadores Web homologadas

| Sistema Operacional | Mozilla Firefox | Safari | Google Chrome | Microsoft Edge |
| --- | --- | --- | --- | --- |
| Windows 11 Pro | X | X | X | X |
| Mac OS X |  | X |  |  |
| iOS (iPad) |  | X |  |  |

\*Homologado para versão mais atual de cada navegador

### Requisitos de hardware

| Processador | Memória RAM | HD/Outros |
| --- | --- | --- |
| Intel® Core™ 2 Duo® de 1.6  GHz ou SIMILAR | 2GB | Espaço disponível em disco de 1  Gbyte para instalação dos produtos. |

### Uso de espaço em disco do WebView2

O WebView 2 é um runtime para plataforma Web, que contém binários modificados do Microsoft Edge. Ele funciona como um aplicativo de navegador, mas é visível apenas dentro do RM. Portanto ele armazena todos os recursos de um navegador, como Cookies, Cache de paginas e demais dados necessários para navegação.

Estes dados são armazenados na pasta do usuário Windows. O caminho padrão onde os navegadores salvam seus dados é:

"***C:\Users\%USERNAME%\AppData\Local\RM.exe.WebView2***"  
ou  
"**%LOCALAPPDATA%\RM.exe.WebView2**"

Pode inicialmente consumir a partir de 15Mb de espaço em disco, de cada usuário do Windows que acessa o RM. O consumo poderá subir de acordo com a utilização de cada página Web aberta dentro do RM.

### Suporte a ambientes especiais

* Ambiente três camadas com as estações “Cliente” dentro da mesma rede do Servidor de Aplicação está homologado para os produtos RM.
* Ambiente três camadas com as estações de trabalho conectando-se a Servidores de Aplicação via internet através de IP Fixo são suportados, mas possuem restrições de desempenho.
* Ambiente três camadas com as estações clientes conectando-se ao Servidor de Aplicação pela internet através de IP Dinâmico: este ambiente deve passar por consultoria do Datacenter TOTVS e possui restrições de desempenho.

### Suporte a versões do Microsoft Office

Os produtos da linha não precisam do Pacote Microsoft Office instalado em suas estações para uso, porém algumas funcionalidades, como Planilhas.Net, são incompatíveis com alguns pacotes. Para uso destas funcionalidades, a versão do Microsoft Office de sua estação de trabalho deverá ser uma das listadas abaixo:

| Versão do Office | 32bits | 64bits | Observações | Status |
| --- | --- | --- | --- | --- |
| Microsoft Office 2016 |  |  | Término do suporte estendido, mais informações [acesse aqui.](https://docs.microsoft.com/pt-br/lifecycle/products/microsoft-office-2016) | RedNot Supported |
| Microsoft Office 2019 |  |  | Término do suporte estendido, mais informações [acesse aqui.](https://docs.microsoft.com/pt-br/lifecycle/products/microsoft-office-2019) | RedNot Supported |
| Microsoft Office 2021 |  | X |  | GreenSupported |
| Microsoft Office 2024 |  | X |  | GreenSupported |

Versões da suíte Office

Não são homologadas versões limitadas e tipicamente classificadas como "básicas" por se tratarem de distribuições compactas e que apresentam a falta ou incompatibilidade de componentes.  
Apenas o pacote **Professional Plus\*** é homologado.

### Restrições e avisos importantes

* A resolução de vídeo mínima para a execução dos produtos da linha RM é de 1024 x 768 pixels, com escala de 100%.
* A TOTVS alerta que não existe versão do BDE para estações 64bit’s.
* O componente Planilha.Net funciona somente nas versões acima mencionadas.

---

## Portabilidade para Estações Disk-Less (Thin-Client)

Informamos que o RM não suporta a execução em computadores Thin-Client (Diskless), entretanto este tipo de Hardware pode ser usado em conjunto com Servidores de Terminal Services, desde que os requisitos mínimos de memória e hardware para o software TOTVS RM neste ambiente sejam respeitados.

---

## Portabilidade específica por Segmentos

Para especificidades de cada segmento, conferir o documento a seguir: *[Portabilidade específicas de Segmentos - 12.1.2606](https://tdn.totvs.com/x/WbW2Pw)*

---

## Arquitetura suportada

A arquitetura Multicamadas é estruturada para poder dar uma maior mobilidade, desempenho e facilidade de manutenções na aplicação. Em seu conceito geral, essa arquitetura, possui no mínimo 3 camadas. A primeira camada contempla a interface com o usuário. A segunda camada é responsável pelo tratamento da regra de negócio do aplicativo, que é o Servidor de Aplicação. Nesta camada, existe também o Servidor de Jobs, que é responsável pela execução dos processos. Já a terceira camada é responsável pelas transações do banco de dados.

A arquitetura Web, o cliente acessa o Servidor Web, onde está instalado o TOTVS Portal, via intranet ou internet. O Servidor Web possui uma camada de Biblioteca cliente, onde se localiza a camada de interface com o usuário, que acessa o Servidor de Aplicações. Este por sua vez acessa ao Servidor de Banco de Dados.

A arquitetura RM via Terminal Service permite o cliente acessar o Servidor de Terminal Service na rede da empresa ou via internet e utilizar os produtos da Linha RM seguindo a mesma arquitetura de Winform e Webform.

A arquitetura Cliente/Servidor é estruturada em duas camadas. A primeira camada é onde se localiza o aplicativo. Essa camada é responsável pela regra de negócio, comandos de manipulação de dados e interface com o usuário. A segunda camada é onde se encontra a base de dados, responsável pelo armazenamento de informações e execução dos comandos oriundos da camada cliente.  
Este tipo de arquitetura é utilizado em aplicativos Delphi do RM.

### Restrições e avisos importantes

Durante a instalação, por padrão, são configuradas as seguintes portas de conexão.

* RM.exe, portais e TBC (IIS) comunicam com o servidor de aplicação (HOST) através das portas 8050 e 8051.
* Servidor de aplicação e o servidor de Jobs comunicam com o banco de dados através da porta 8050.
* Servidor de aplicação comunica com o servidor de Jobs pela porta 8050.
* Recomendamos que os servidores de Jobs se comuniquem através da porta 8050.
* Se o cliente expõe seus WebServices externamente, deve-se liberar no Firewall a porta utilizada.

---

## License Server

O TOTVS License Server é parte do modelo de Licenciamento TOTVS FULL, que controla as licenças de uso de seu software. Uma maneira segura e eficiente de gerenciamento de licenças para os módulos e funcionalidades da TOTVS.

Versão mínima do License Server

A versão mínima exigida do License Server é a 3.7.0.

### Restrições e avisos importantes

Para maiores informações consulte: .

---

## Recomendações

1. É necessário a instalação do  para integração das informações do E-Social.
2. Para ambiente com grande volume de processamento, a TOTVS recomenda o uso de um servidor de aplicação.
3. Processos para Geração de Cubos e Relatórios, Cálculo de Folha, devem ser agendados para períodos de menor carga de processamento dos servidores.
4. Utilize filtros que retornem no máximo 200 registros na visão.
5. No cadastro de Servidores de Aplicação, utilize o campo “Número máximo de Registros” para limitar os registros retornados do banco de dados. Para mais informações, acesse o [link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016013767-RM-Frame-Aumentar-quantidade-de-registros-na-vis%C3%A3o-Servidores-de-Aplica%C3%A7%C3%A3o-).
6. Não utilize a base de produção para Armazenamento dos Cubos.
7. ATENÇÃO: Visando a consistência e melhoria nos processos de banco de dados, a TOTVS orienta aos clientes para que evitem a criação de tabelas, índices ou outros objetos de banco de dados que não sejam do padrão da base original. Caso seja necessário criar algum objeto na base original que não seja referente a alguma customização, pedimos que abram um chamado na TOTVS para que seja feita uma análise da viabilidade de incluirmos esse objeto na base padrão (sendo aprovada a inclusão isso será feito no próximo conversor a ser disponibilizado). Esta medida se faz necessária, para assegurar uma maior consistência da estrutura da base de dados, pois quando a migração de versão ocorre, alguns dos objetos criados pelos clientes podem ser excluídos ou sofrer alterações, o que pode acarretar interferência em processos de integração de terceiros ou alguma outra rotina atrelada ao produto. Reforçamos que a responsabilidade pela manutenção de objetos específicos é toda do cliente. Para maiores informações entre em contato nosso suporte de banco de dados.
8. É altamente recomendado que a rede de comunicação do servidor de Banco de Dados, servidor Web, servidor de Aplicação e servidor de Terminal Service seja Gigabit. Para maiores informações consulte seu Administrador de Rede.
9. O RM não prestará suporte em sistemas operacionais, produtos ou serviços, incluindo o Office, fora do ciclo de vida estabelecido pela Microsoft.
10. Framework 4.8A atualização do .NET Framework 4.8 é obrigatória e deve estar atualizada com a última Release que pode ser realizada através do Windows Update, pacote cumulativo KB a depender da versão do Windows.
11. Coluna StatusO Status *EOL* reflete o estado do suporte ao respectivo produto no lançamento da release. Independentemente desta coluna, o RM prestará suporte em sistemas operacionais, produtos ou serviços, **apenas** dentro do ciclo de vida estabelecido pela Microsoft.
12. WebView2O WebView2 é necessário para abrir o RM. Nas máquina conectadas na internet, ele é baixado automaticamente. Caso não haja conexão, o instalador pode ser obtido a partir do site da Microsoft: acesse o [link](https://developer.microsoft.com/pt-br/microsoft-edge/webview2/#download-section) (utilizar o *Instalador Autônomo Perene*).
13. O uso do Smart View integrado ao RM pode exigir um custo adicional de infraestrutura. Para mais informações dos requisitos de hardware do Smart View, acesse o .

**Para mais informações entre em contato com o Help Desk TOTVS 4003-0015**
