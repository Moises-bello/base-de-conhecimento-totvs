---
content_hash: 5c992d682b63dea32f70ce1664dcda8c6978770adf9e5da20a6e2d1dd4b4d107
fetched_at: '2026-06-28T21:35:19.723775+00:00'
page_id: '221555408'
product: fluig
source: tdn-fluig
title: BPM 102 - Problemas com o envio de notificação em processos, como resolver?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221555408
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** 2.0, 1.6 ou inferior

# Ocorrência

O fluig está com problemas no envio de notificações de movimentação de tarefas por e-mail ao responsável da tarefa. Isto ocorre mesmo com tudo configurado corretamente, opção de notificação selecionada no processo, configuração do SMTP e enviando e-mails de outras funcionalidades. Como resolvo?  
  
No log é apresentado um erro parecido com este:

javaErro

# Causa

Está faltando o parâmetro <jms-queue> referente ao 'ECMNotificationQueue' em um arquivo de configuração da plataforma.

# Solução

Para realizar o procedimento abaixo, os serviços do fluig devem estar parados.

0.5falsesamplefade3A partir da 2.0

Para resolver siga os passos abaixo:

1. Adicione o trecho de parametrização abaixo no arquivo **standalone.xml**, localizado em [Instalação fluig]/appserver/standalone/configuration. Este parâmetro deve ser acrescentado dentro da *tag* <jms-destinations>, junto com as outras configurações de "*queues*".

xmlEclipsestandalone.xml



true
]]>

2. Apague as pastas temporárias 'data' e 'tmp' em [Instalação fluig]/appserver/standalone/log;

3. Limpar o cache do navegador para realizar os testes;

4. Inicie os serviços do Fluig.

true11.6 até 1.8.2

Para resolver siga os passos abaixo:

1. Adicione o trecho de parametrização abaixo no arquivo **domain.xml**, localizado em [Instalação fluig]/appserver/domain/configuration. Este parâmetro deve ser acrescentado dentro da tag <server>, no subsystem <subsystem xmlns="urn:jboss:domain:messaging-activemq:1.0">.

xmlEclipsedomain.xml]]>

2. Apague as pastas temporárias 'data' e 'tmp', localizadas em [Instalação fluig]/appserver/domain/servers, de todos os *servers;*

3. Limpar o cache do navegador para realizar os testes;

4. Inicie os serviços do Fluig.

21.5.13 e anteriores

Para resolver siga os passos abaixo:

1. Adicione o trecho de parametrização abaixo no arquivo **standalone.xml**, localizado em [Instalação fluig]/jboss/standalone/configuration. Este parâmetro deve ser acrescentado dentro da *tag* <jms-destinations>, junto com as outras configurações de "*queues*".

xmlEclipsestandalone.xml



true
]]>

2. Apague as pastas temporárias 'data' e 'tmp' em [Instalação fluig]/jboss/standalone;

3. Limpar o cache do navegador para realizar os testes;

4. Inicie os serviços do Fluig.
