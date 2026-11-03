---
content_hash: 983c52828e6e2b25569d5f549360b198b5a5cc6d9bf870616ad5766b14cf5e19
fetched_at: '2026-06-29T00:06:24.246792+00:00'
page_id: '224114888'
product: rm
source: tdn-rm
title: RM Atualizador
type: documentation
url: https://tdn.totvs.com/display/LRM/RM+Atualizador
version: 56
---

**Documentações relacionadas:**

### Atualizador RM

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Banco de Dados |
| **Versão RM** | : | A partir da Versão 12.1.5 |
| **Banco de Dados** | : | SQL Server e Oracle |
| **Processo** | : | Atualizador de base de dados do RM |
| **Sub Processo** | : | Auxílio no processo de conversão da base de dados |

**INTRODUÇÃO**

Este documento objetiva orientar os procedimentos de Atualização da base de dados dos produtos RM.

**DESENVOLVIMENTO/PROCEDIMENTO**

**Portabilidade:**

* É importante a leitura da [Portabilidade](http://tdn.totvs.com/pages/releaseview.action?pageId=165282824) antes da Atualização da base de dados.

**Atualização da base de dados:**

**Requisitos:**

1. A base de dados precisa estar alguma versão anterior a mais atual ou algum patch anterior o mais atual. Para saber a versão da sua base de dados, execute o comando "**SELECT VERSAOBASE FROM GPARAMS**" no seu Gerenciador de Banco de Dados.
2. Instalação da BibliotecaRM [Clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=172297669) para acessar o documento de instalação.

**Atualizando a Base de Dados:**

1. Execute o arquivo "**RM.Atualizador.exe**" no diretório "**...\CorporeRM\RM.Net\**"

2. Na tela “**Bem-Vindo ao Atualizador de Base de Dados TOTVS RM**”, insira o usuário e senha de acesso ao Banco de Banco, escolha o alias de acesso ao banco e clique no botão "**OK**":

       

* Caso não tenha um Alias criado, clique no ícone, apontado pela seta, do contrário, vá para o **passo 3**.

**Obs:**Para os clientes que estão hospedados em Cloud, o acesso pode ser realizado pelo usuário e senha de banco, bem como, o usuário e senha de acesso ao sistema. 

A opção de criar um novo "Alias" não existi nesse contexto, tendo em vista que, o "Alias" referente ao cliente será carregado automaticamente, conforme imagem abaixo:

* Na tela "**Gerenciador de Alias**", clique no ícone com o sinal de mais (+), no canto superior esquerdo da tela, e preencha as informações de acesso ao Banco de Dados. Após o preenchimento, clique no botão "**Testar**" para validar as informações. Clique no botão "**OK**" para fechar a tela.

    3. Na tela "**Atualizações Disponíveis**", clique no botão "**Avançar**". **Observação:** Todas atualizações são obrigatórias e não podem ser desmarcadas.

    4. **Relatório Delphi (A partir da release 12.1.2310)**:

 4.1 Caso **existam** relatórios Delphi executados nos últimos 12 messes:

* + É apresentado um alerta mencionando a descontinuidade dos relatórios Delphi para versões posteriores a 12.1.2310. O cliente deve aceitar o termo para prosseguir.

***OBS:**Após aprovação do termo de aceite, não será apresentado mais esse alerta nas próximas atualizações.*

* + É apresentado na tela de requisitos um alerta referente a descontinuação dos relatórios Delphi.

4.2 Caso **não existam** relatórios executados nos últimos 12 meses, nenhum alerta é apresentado e o aceite é dado automaticamente.

    5. Ao clicar no botão "Avançar" da tela anterior, o processo de Análise de Requisitos será exibido. Aguarde até o término do processo.

* Na tela "**Análise de Requisitos a Atualização**", verifique se todos os requisitos estão atendidos.

         Todos os requisitos advertidos nesta tela possuem sua página com mais detalhes a respeito, segue abaixo uma lista sintética para breve entendimento:

| Requisito | Finalidade |
| --- | --- |
| Versão mínima do RM | Seu objetivo é garantir que a base de dados esteja com versão maior que 11.82.30, sendo assim irá converter a base para respectiva versão do ambiente utilizado. |
| Versão do SGBD | Seu objetivo é garantir a versão do sistema de gerenciamento do banco de dados afim de atender ao documento de portabilidade da versão. |
| Validação de Collation\Caractere Set | Seu objetivo é garantir o grupo de caracteres correto para o sistema afim de atender ao documento de portabilidade da versão. |
| Validação Recovery Model / Tablespaces Autoextend | Apresenta configurações de segurança para seu banco de dados que podem estar desativadas com isso gerando riscos para seu ambiente. |
| Nível de Compatibilidade | Seu objetivo é garantir o Sql Server estar trabalhando com o nível de compatibilidade afim de atender ao documento de portabilidade da versão. |
| Owner do login padrão | Adverte ao usuário que o nome do login dono do banco de dados não é o padrão sugerido, sendo assim o administrador precisa avaliar seus scripts de grants. |
| Transação aberta | Tem objetivo apresentar para o usuário tabelas envolvidas em transações que têm potencial em gerar 'lock' no banco de dados durante a conversão. |
| Servidores Job em execução | Apresenta servidores jobs sendo executados no momento da validação dos requisitos, tais jobs podem abrir transações e que por sua vez gerar locks no banco de dados. |
| Jobs Em Execução | Apresenta jobs sendo executados no momento da validação dos requisitos, tais jobs podem abrir transações e que por sua vez gerar locks no banco de dados. |
| Versão mínima do License Server | A partir da versão 12.1.2205 será obrigatório o uso da versão  3.2 ou posteriores e para a 12.1.2302, será obrigatório o uso da 3.4.3 ou superior. |
| Validação de SMS Válido | A partir da versão 12.1.2302, o atualizador passa a validar se o SMS do License server está válido. |
| Validação da versão utilizada | Alertar o usuário, caso esteja atualizando para versão expirada, próxima de expirar ou que existam patches mais recentes. Em alguns casos, será exibida a validação em uma mensagem após o login no RMAtualizador. (apenas a partir da 12.1.2310) |
| Validação da existência dos arquivos de scripts | Caso o atualizador não encontre o arquivo de script, deverá refazer a instalação da biblioteca (de preferencia para a release mais atual e o ultimo patch disponível). |

    6. Na tela "**Análise de Impactos da Atualização de Versão**", verifique todos os impactos, clicando no link "**Analisar Impactos**".

* Aguarde até que todos os impactos sejam validados pelo Atualizador. Caso não haja impactos, vá para o **passo 6**.

* Para prosseguir marque a opção "**Não desejo analisar os possíveis impactos ou já realizei este procedimento anteriormente**" e clique no botão "**Avançar**".

    7. Na tela "**Backup e Customização**" certifique que você possui uma cópia de segurança (backup) antes do processo de Atualização e que as Customizações, caso possua, já foram analisadas. Em seguida,     clique em "**Avançar**".

    8. Na tela "**Opções**" marque as opções, conforme desejado. Recomendamos aos clientes TOTVS marcarem as duas opções.O envio do **Log de Atualização** para a TOTVS serve de base de conhecimento         para aprimoramento da ferramenta. sem eliminar a abertura de chamados em caso de erros.

* + **Observação:**

Detalhes do compartilhamento da estrutura dos objetos <https://tdn.totvs.com/x/GQyhMQ>

9. Na tela "**Execução**", clique no botão "**Iniciar Atualização**" para iniciar a Atualização da Base de Dados.

9.1 - Seleção da classificação de ambiente

Nesta etapa o usuário irá selecionar qual seria a finalidade da base de dados atual para que o Atualizador faça o ajuste necessário em seu banco de dados. Para mais detalhes acesse a documentação abaixo:

<https://tdn.totvs.com/x/ysAmO>

**Observação**: A partir da versão 12.1.2302, será possível executar o atualizador, mesmo que não existam atualizações pendentes, para que a versão do patch seja registrada no banco de dados. Neste caso, será apresentada a seguinte mensagem:

A partir da versão 12.1.2302, será possível executar o atualizador, mesmo que não existam atualizações pendentes, para que a versão do patch seja registrada no banco de dados. Com isso....

                               

                               

**Atenção!**

**Ao confirmar e seguir o processo, o atualizador irá salvar no banco de dados a versão deste path que está sendo executado, levando em consideração este ser maior em relação ao que estava salvo no banco anteriormente. A coluna que armazena esta informação é a GUPGATUALIZACAO.VERSAOPATCH.**

* Certifique-se de que realmente deseja iniciar o processo clicando no botão "**Sim**".

* Durante a conversão, é possível visualizar o comando que está sendo executado no momento, clicando no link "**Comando em execução...**"..

* Ao finalizar a conversão, a mensagem abaixo será exibida, caso não ocorra erros. Do contrário uma mensagem informando de erros será exibida com as devidas orientações.

* Após clicar no botão "**OK**" da tela anterior, clique no botão "**Avançar"** para ver o resumo da Atualização.

    10. Na tela "**Grandes Tabelas**", é possível visualizar as tabelas de maior volume do seu banco de dados, ordenadas pelo consumo de espaço em disco.

          Cada item exibido conta com uma documentação que orienta o usuário sobre como realizar a redução de dados,

          proporcionando benefícios como economia de armazenamento, melhoria de desempenho e outros ganhos operacionais.

\*A tela só aparece quando existirem tabelas com mais de 100 GBs de espaço utilizado.

Consulte também a documentação centralizada que reúne todos os roteiros disponíveis para essa finalidade: <https://tdn.totvs.com/x/KmTeO>

11. Na tela "**Resumo**" é possível verificar as informações consolidadas das Atualização em "**Visualizar Log**". Em seguida clique em "**Avançar**" para concluir a Atualização. Somente em casos de erros, acione     o Suporte da TOTVS.

      12. Clique em "**Concluir**"para fechar o Atualizador.

Item importante

Executar o configurador do TOTVS Audit imediatamente após a atualização da base de dados garante a atualização dos objetos utilizados nas coletas de auditoria, evitando possíveis perdas de acesso às telas do produto.

**API's do Atualizador:**

Abaixo as orientações para o us

Fluxo das APIs do RM ATUALIZADOR

1. Executar a Atualização:

   * Resultado esperado: Se houver atualizações a serem executadas, a API retorna um JSON com informações sobre o que será atualizado. Se não houver atualizações, a API informa que não há atualizações disponíveis.
2. Executar a Atualização (*noJSON*):

   * Resultado esperado: A API retorna a quantidade de erros que ocorreram durante a execução da atualização. Se não houver atualizações disponíveis, ela retorna "0".
3. Obter o Progresso da Atualização:

   * Resultado esperado: Se houver uma atualização em execução, a API retorna um JSON com informações sobre as etapas da atualização, incluindo progresso, tempo de execução e nome da etapa. Se não houver atualizações em andamento, a API informa que não foram encontradas atualizações.
4. Obter se a base possui scripts pendentes:

   * Resultado esperado: Se houver scripts pendentes, a API retorna *true*, caso não haja scripts pendentes, *false*.
5. Verificar os Pré-Requisitos:

   * Resultado esperado: A API retorna um JSON com as validações dos pré-requisitos do RM Atualizador.
6. Obter os Impactos em Objetos Gerenciais (relatórios, cubos, planilhas) relacionados à Atualização de Versão:

   * Resultado esperado: A API executa a análise de impacto da versão na base de dados e retorna os resultados em um JSON. Se não houver impactos, o JSON será vazio.

| Finalidade | Caminho |
| --- | --- |
| Busca requisitos para conversão | UpgUpgradeWebServer/atualizador/CheckRequirements/{aliasDB} |
| Verifica se existem scripts pendentes após atualizar ambiente | UpgUpgradeWebServer/atualizador/HasPendingScript/{aliasDB} |
| Busca requisitos para conversão ( login com usuário aplicação ) | UpgUpgradeWebServer/atualizador/CheckRequirementsUseRMUser/{aliasDB} |
| Retorna possíveis impactos em Objetos Gerenciais | UpgUpgradeWebServer/atualizador/GetUpgradeImpacts/{aliasDB} |
| Retorna possíveis impactos em Objetos Gerenciais  ( login com usuário aplicação ) | UpgUpgradeWebServer/atualizador/GetUpgradeImpactsUseRMUser/{aliasDB} |
| Inicia o processo de atualização sendo que "environment" refere-se à homologação ou produção | UpgUpgradeWebServer/atualizador/ExecuteUpgrade/{aliasDB}/{environment} |
| Inicia o processo de atualização retornando quantidade de erros que ocorreram na atualização | UpgUpgradeWebServer/atualizador/ExecuteUpgrade/{aliasDB}/{environment}/{noJSON} |
| Inicia o processo de atualização ( login com usuário aplicação ) | UpgUpgradeWebServer/atualizador/ExecuteUpgradeUseRMUser/{aliasDB}/{environment} |
| Retorna informações relativas à atualização sendo executada no momento | UpgUpgradeWebServer/atualizador/GetUpgradeProgressCloud/{aliasDB} |
| Retorna informações relativas à atualização sendo executada no momento  ( login com usuário aplicação ) | UpgUpgradeWebServer/atualizador/GetUpgradeProgressCloudUseRMUser/{aliasDB} |
