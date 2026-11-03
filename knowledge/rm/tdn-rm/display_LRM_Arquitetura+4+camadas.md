---
content_hash: 11187f5e826832286cc0fff6eb772187aa257be60247193c21641c4c26cffdd2
fetched_at: '2026-06-29T00:11:13.470043+00:00'
page_id: '66126305'
product: rm
source: tdn-rm
title: Arquitetura 4 camadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Arquitetura+4+camadas
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.52 |
| **Processo** | **:** | Arquitetura 4 Camadas |
| **Subprocesso** | **:** | Estruturando ambiente 4 camadas |
| **Data da publicação** | **:** | 09/07/2013 |

**Resumo:**

Permitir a inclusão de servidores que atenderá com exclusividade os processos gerados por Jobs. Desta forma cada máquina irá realizar seu devido processo até retorno das informações a visão do operador.

A estrutura  4 camadas se assemelha ao ambiente em 3 camadas,  contudo se diferencia por obter 1 servidor de Jobs responsável por processar os Jobs que entram na fila de execução.

De forma técnica, a solicitação do job é disparada pela máquina cliente ao solicitar informações na tela, neste momento a Action [Ação da tela] é disparada junto ao processo ”job“  que entra na fila de execução no banco de dados.

De forma simultânea o “Servidor de aplicação” irá processar a action, enquanto o “Servidor de Jobs” realiza verificações no banco de dados [Tabela GJOBXEXECUCAO] coletando os processos que aguardam para execução e processando os demais.

**Utilizamos a ilustração abaixo para exemplificar cada camada:**

**CONFIGURANDO O AMBIENTE 4 CAMADAS**

**4º Camada – Servidor de Jobs:**

O objetivo do "Servidor de Jobs" é realizar uma verificação na fila de processos (Tabela GJOBXEXECUCAO) a cada 10 segundos por default, caso exista algum "job" aguardando para execução, ele assume a execução, processa o JOB e conclui o trabalho.

Habilitando o ambiente 4 camadas é possível obter melhor desempenho do sistema, visto que o processamento dos recursos estão divididos em cada estrutura. Em casos de lentidão é possível pontuar o empecilho com detalhes.

De acordo com a quantidade de processos executados pelo cliente é possível que seja inserido vários servidores de Job Server que poderá ser visualizado na tabela GJOBSERVER.

**Instalando o Servidor de Jobs:**

- Instale a Biblioteca RM, escolhendo a opção Ambiente 3 camadas / Server

- Após instalação execute o RM.AliasManager.exe (C:\totvs\CorporeRM\RM.Net) e configure a comunicação com o base de dados

Na aba Serviços, **HABILITE** o processamento de Jobs definindo a quantidade de processos simultâneos que será executada, lembrando que esta quantidade é ajustada de acordo com a necessidade e estrutura física do cliente.

Após concluir as configurações, reinicie o serviço **RM.Host.Service.exe**, desta forma a tabela **GJOBSERVER**, **responsável por guardar as informações dos servidores de Jobs ativos** será preenchida com informações da máquina no qual foi habilitado o processamento, veja abaixo:

Obs: O campo **DATAULTATIV** irá informar qual data/hora o servidor informado realizou o último processamento dos Jobs, assim é possível observar se o servidor encontra-se em operação.

**3º Camada – Servidor de banco de dados**

    O Servidor de banco é muito importante obter bom desempenho de qualquer aplicação, contudo se faz necessário realizar a manutenção do banco de forma periódica realizando processos para controlar/aumentar o desempenho

 irá hospedar a base de dados para utilização do sistema, lembrando que não é aconselhável virtualisar  o servidor de banco conforme especificações no documento de portabilidade disponível no link abaixo:

<http://tdn.totvs.com/display/rm/Portabilidades>

**2º Camada – Servidor de aplicação**

O Servidor de aplicação possui a função de processar as operações solicitadas na tela e retornar a visão do usuário, mas com exceção dos processos gerados por Job que serão processados pela 4º camadas (Servidor de JobServer) citado acima, desta forma o servidor de APP realiza o processamento da tela, enquanto o servidor de JOBS processa os demais.

A arquitetura do servidor de APP é similar ao servidor de Jobs, diferenciado pela flag **“Habilitar processamento de Jobs”** que deve estar DESABILITADA, caso contrário o servidor de aplicação além de processar as telas, também ira trabalhar como servidor de jobs, sendo preenchido na tabela GJOBSERVER como servidor ativo.

* + Instale a Biblioteca RM, escolhendo a opção Ambiente 3 camadas / Server.
  + Acesse a ferramenta RM.AliasManager.exe e defina a conexão a base de dados

Efetuando esta configuração, o servidor está pronto para enviar informações ao banco de dados e executar as requisições de tela.

OBS: É importante que os servidores de aplicação e jobs sempre estejam na mesma biblioteca específica.

**1º Camada – Ambiente clientes:**

O ambiente cliente será responsável por efetuar as solicitações de tela/jobs, podendo ser utilizado em terminais cliente ou servidores de TS para acesso compartilhado.

A instalação da biblioteca RM se resume na seleção da opção “3 Camadas – Modo Cliente” direcionando a comunicação ao servidor de aplicação, com isso toda estrutura para utilização dos aplicativos será instalada e os processos solicitados aos servidores, lembrando que os aplicativos devem ser instalados nas estações clientes.

Visando melhor entendimento, segue tela da instalação onde será definido o direcionamento.

* **Gerenciamento de Jobs**  
  Para verificar com mais detalhes cada job processado incluindo informações do usuário que solicitou o processo, qual servidor de JOBS realizou o processamento dentre outras informações, pode ser utilizada a tela "Gerenciamento de Jobs"  disponível nos menus:

**Aplicativos:** Sistema > Server > Gerenciamento de Jobs

**MDI:**Ambiente > Gerenciamento de Jobs

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
