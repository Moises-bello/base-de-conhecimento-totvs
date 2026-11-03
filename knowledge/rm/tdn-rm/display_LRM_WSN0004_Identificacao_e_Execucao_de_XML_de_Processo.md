---
content_hash: 3baebc8be5c3711b2468ea4c5821fee747cdf594bb41bee533a5a2014cf244b1
fetched_at: '2026-06-29T00:08:49.485227+00:00'
page_id: '330835559'
product: rm
source: tdn-rm
title: WSN0004_Identificacao_e_Execucao_de_XML_de_Processo
type: documentation
url: https://tdn.totvs.com/display/LRM/WSN0004_Identificacao_e_Execucao_de_XML_de_Processo
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compra e Faturamento |
| **Versões:** | 11.82 e Superiores |
| **Ocorrência:** | Identificação e Execução de XML de Processos do RMNucleus |
| **Ambiente:** | WebService RM |
| **Passo a passo:** | Este documento tem por finalidade ensinar aos usuários do RM identificar e extrair do sistema um XML exemplo de Processo, além de executa-lo via SoapUi.  Como exemplo, utilizaremos o processo de Processar Grupo de Movimentos      Para obtermos o XML de exemplo, precisaremos executar ou procurar por um Job já executado deste processo.    Caso seja necessário executar, o primeiro passo é realizar a inclusão de um movimento que tenha parametrizado o processo de "Criar com Status Não-Processados". Caso não tenha, vá aos parâmetros do tipo de movimento, etapa Mov - Identificação, e marque o campo destacado no print abaixo:      Após a parametrização, faça a inclusão do movimento como de costume. Feita a inclusão do movimento, marque-o e vá até o menu Processos e execute o processo de Processar Grupo de Movimentos        Concluído o processo, vá até o menu Ambiente - Gerenciamento de Jobs.      Crie um filtro que possibilite a identificação do Job criado para o processo. Neste caso, foi criado um filtro utilizando o campo "Criado Em".      De posse do ID Job, será necessário abrirmos o aplicativo TOTVS Web Service Client (TOTVSWSCliente.exe) para extração do XML. Para mais informações do aplicativo, acesse o link ().      Abra o aplicativo e preencha os dados:  Nome do Processo;  IDJob;  Endereço do Servidor;  Usuário;  Senha;    Informando os dados necessários e clicando em Carregar, caso os dados estejam válidos, será carregado o registro do JOB criado no RM. Dê um duplo clique sobre o registro para que sejam carregados os dados.    Vá até a aba XML e copie todo o conteúdo.      Inicie o aplicativo SoapUi.  Caso não tenha configurado o SoapUi para execução de processos do RM, abra o painel de WS (geralmente pelo link <http://localhost:8051/wspageindex/>) e copie o endereço do link de Processos (WsProcess).    Inicie o SoapUi, vá a opção File e escolha a opção New Soap Project.  Informe o link copiado no campo Initial WSDL e informe o nome do projeto.        Após criado o projeto, expanda a lista RM\_IwsProcess, e crie uma nova Request sobre o método ExecuteWithXmlParams.  Na tag <tot:ProcessServerName> preencha o nome do Processo conforme coluna Classe do Processo do gerenciamento de Jobs (RM). Neste exemplo, o processo é o MovProcessarMovProc.  Para a tag <tot:strXmlParams> adicione **<![CDATA[** ao inicio, cole o XML obtido pelo WsClient e adicione **]]>** ao final.    Preencha as colunas Usarname e Password localizadas na aba de Request Properties.  Após estas configurações, execute o Submit da request (Identificado pelo ícone verde na parte superior esquerda).  Neste momento o sistema tentará executar o processo conforme XML passado. Sendo executado com sucesso, o retorno do Soap será a numeração 1.    Caso seja apresentado erro, gentileza verificar a mensagem apresentada |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
