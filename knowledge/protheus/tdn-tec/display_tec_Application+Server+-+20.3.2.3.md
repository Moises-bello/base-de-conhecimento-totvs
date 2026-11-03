---
content_hash: ab5c44a419ab7666f97b6934219e398ca727dd0b77aac92f7e468a61f1292740
fetched_at: '2026-07-02T19:24:28.713368+00:00'
page_id: '814529045'
product: protheus
source: tdn-tec
title: Application Server - 20.3.2.3
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.2.3
version: 16
---

Application Server - 20.3.2.3

# Correções

4GL - Compilador 4GL não informa a falta de definição de variável 

Incidente: compilador não informa a falta de definição de variável 4GL em uma expressão utilizando o comando Return.

Solução: ajustes no processo de compilação da linguagem 4GL para a correta identificação de variáveis não declaradas.

Referente ao chamado: DTAPPSRV-7545

Erro no acesso a dispositivo de impressão

Incidente: Quando do acesso, através do objeto tMSPrinter, a um dispositivo de impressão indisponível e/ou inacessível pelo sistema operacional, pode ocasionar encerramento inesperado do Application Server.

Solução: Inclusão de tratamento de exceção quando da ocorrência de falha no acesso a um dispositivo de impressão.

Referente ao chamado: DTAPPSRV-7645

Correção no tratamento da configuração SSLCheckClientCert

Incidente: Ao configurar no REST TLPP usando JSON a chave SSLCheckClientCert usando um valor númerico em vez de lógico, o Application server mostrava a mensagem "HTTP Server - error, invalid check client cert value" e não iniciava o REST. Se a chave fosse configurada via INI, o REST iniciava normalmente.

Solução: Corrigido o tratamento da chave SSLCheckClientCert do REST TLPP para aceitar também valores numéricos. Se tiver o valor zero na chave, será considerado FALSE; qualquer outro valor será considerado como TRUE.

Referente ao chamado: DTAPPSRV-7643

Access Violation - Objeto tTimer

Incidente: Usar FreeObj no objeto tTimer pode causar encerramento  da aplicação.

Solução: Correção no destrutor do tTimer para retirá-lo da lista de componentes da janela.

Referente ao chamado: DTAPPSRV-7632

Bloquear conexões pelo webmonitor impede novo login (do próprio webmonitor)

Incidente: Ao bloquear conexões pelo WebMonitor, não era mais possível realizar o login no mesmo, retornando mensagem no console de que o servidor estava bloqueado

Solução: Começou a acontecer após adicionar um job GetCodePage, para correção foi adicionado o GetCodePage na exceção de bloqueio

Referente ao chamado: DTAPPSRV-7611

Falha HSMPrivVery - routines:int\_rsa\_verify:wrong signature length

Ocorrência: função HSMPrivVery estava falhando ao tentar verificar assinaturas com mais de 256 bytes, e apresentava o erro "wrong signature length".

Solução: Implementação na função HSMPrivVery para  suporte de assinaturas com mais de 256 bytes.

Referente ao chamado: DTAPPSRV-7604

Access violation no método tSFTPClient:ReceiveFile() e Comportamento incorreto no método tSFTP:Directory()

Incidente: Listagem de diretórios do servidor remoto sendo feita incompleta na Classe SFTP ao utilizar a função Directory. Access violation no Application Server durante a execução da função ReceiveFile().

Solução: Corrigido o comportamento e mantido de acordo com o atual no TDN referente à classe tSFTPClient.   
Ajuste no método ReceiveFile para evitar access violation .

Referente ao chamado: DTAPPSRV-7600

Access violation Application Server após erro Stack Depth Overflow

Ocorrência: Finalização anormal (queda) do APPServer, após uma ocorrência de erro de limite de pilha de chamadas AdvPL "Stack Depth Overflow", quando está configurado um INACTIVETIMEOUT para o SmartClient, e a janela que mostra o erro "Stack Depth Overflow" seja fechada automaticamente por inatividade.

Correção: Corrigido o mecanismo de fechamento por inatividade.

Referente ao chamado: DTAPPSRV-7595

Erro de falha na carga dbsrv.dll em Job ADVPL

Ocorrência : Carga indevida da dbsrv.dll após finalização de JOB ou Thread em AdvPL, usando DBACCESS com SGDB ORACLE, onde o último driver ou RDD usada pelo processo antes da finalização não foi o driver TOPCONN

Correção: Alterada e corrigida uma rotina de limpeza interna que somente deveria ser disparada em ambientes 4GL / Logix.

Referente ao chamado: DTAPPSRV-7592

tSFTPClient: Uso da sessão [SFTP] no appserver.ini e propriedades simultâneamente

Incidente: Uso das propriedades da classe SFTP (tSFTPClient) não funcionando corretamente quando utilizado em conjunto com as configurações existentes no arquivo de configurações do Application Server, no mesmo fonte TLPP.

Solução: Corrigido o tratamento interno das propriedades da classe tSFTPClient para permitir o uso do arquivo de configurações e/ou das propriedades desta classe.

Referente ao chamado: DTAPPSRV-7591

Consumo exagerado de contextos pelo Broker Smartclient

Incidente: em certas situações o Broker Para Smartclient poderia não mais aceitar conexões, ocorrendo na prática um travamento; quando isso ocorria, eram gravadas mensagens "error in accept" no console.log.

Solução: Correção na biblioteca básica de comunicação do broker.

Referente ao chamado: DTAPPSRV-7584

# Melhorias

Atualizar informação sobre tabelas globais e hash map

Ocorrência: A informação de consumo de memória mostrada nos objetos de hashmap do Application Server não considera o consumo de cada objeto.

Correção : Quando mostrada a informação de consumo de memória do Application Server, mediante configuração ServerMemoryInfo=1 na seção GENERAL do appserver.ini, a quantidade de memória consumida por cada lista existente será contabilizada na informação " Total (X + A + extras) ..."

Referente ao chamado: DTAPPSRV-7641

# Novas Implementações

Função para descriptografia utilizando algoritmo RSA

Solicitação: necessidade de implementar uma nova função AdvPL que faz descriptografia RSA, complementando o recurso de encriptação fornecido pela função EncriptRSA.

Solução: implementada função DecryptRSA.

Documentação:

Referente ao chamado: DTAPPSRV-7525

Broker Agent - Implementar configuração para os logs

Solicitação: Permitir alterar o caminho onde os logs do Broker Agent serão gravados.   
  
Solução: Criação da parâmetro na linha de comando para definir caminho onde os logs serão gravados. Mais detalhes na documentação

Referente ao chamado: DTAPPSRV-7640

Implementar Classe para criptografia com algoritmo PBKDF2

Solicitação: Necessidade de criptografia PBKDF2 para linguagem TLPP.

Solução: Implementado classe  para suporte a criptografia PBKDF2 na linguagem TLPP.

Referente ao chamado: DTAPPSRV-7566
