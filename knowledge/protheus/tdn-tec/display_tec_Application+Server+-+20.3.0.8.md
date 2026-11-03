---
content_hash: 6f74f5b804d7f563903bbeb2180bd9910413ade8dcf7447dd59060e33530465b
fetched_at: '2026-07-02T19:24:27.055689+00:00'
page_id: '655882400'
product: protheus
source: tdn-tec
title: Application Server - 20.3.0.8
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.0.8
version: 20
---

# Correções

Resource2File não recupera arquivos do RPO Custom

Ocorrência: A função Resource2File não retorna resources do RPO Custom

Solução: Correção da função Reosurce2File para busca de resources no RPO Custom.

Referente ao chamado: DTAPPSRV-5298

Problema na utilização de arquivos com senha na função FZIP

Ocorrência: Arquivos zip gerados com a função AdvPL () com senha não reconhecem a senha utilizada.  
  
Solução: Alterações para gerar CRC válido dos arquivos a compactar e quando usar senha.

Referente ao chamado: DTAPPSRV-5630

Requisição JSON com Encoding GZIP gera erro 400 Bad Request

Ocorrência: O servidor HTTP não fazia a descompressão de mensagens recebidas.  
  
Solução: Incluir do processo de descompressão das mensagens

Referente ao chamado: DTAPPSRV-5643

Process terminated by the administrator. on ERRORSYS

Ocorrência: Em jobs do tipo IPC, como os utilizados no Scheduler, a partir do AppServer Versao 20.3.0.4, começaram a aparecer mensagens de erro no log de console "Process terminated by the administrator. on ERRORSYS(APLIB240.PRW)" quando um processo era finalizado internamente pela aplicação.  
  
Correção: Esta mensagem estava sendo mostrada erroneamente, e não interfere no processamento. Com a correção realizada, essa mensagem será mostrada apenas quando um processo de IPC é finalizado manualmente ou intencionalmente, por exemplo quando o processo é finalizado pelo Monitor Electron.

Referente ao chamado: DTAPPSRV-5576

GetSrcArray - Suporte para leitura de múltiplos RPOs

Ocorrência: A função , por padrão, não retornava os fontes do RPO Custom.  
  
Correção: A função  alterada, por padrão, os fontes de todos os RPOs, vide documentação.

Referente ao chamado: DTAPPSRV-5521

Função Encode64 não funciona com arquivos na pasta StartPath (system)

Ocorrência: Erro fatal de execução da função Encode64(), informando o erro "[THROW] Assert at file ...stringz.hpp" quando usado o 2o parametro para informar um arquivo em disco no servidor, e ocorra um erro na abertura do arquivo, ou o smartclient seja executado em uma máquina remota.  
  
Correção da função Encode64(), usando usada para codificar um arquivo em disco através do 2o parâmetro.  
  
Correções:  
- A função Encode64() passa a funcionar corretamente quando informado arquivos a partir do rootpath do ambiente.  
- Revisão no tratamento de erro de abertura de arquivo, para que uma falha de abertura do arquivo informado faça a função retornar NIL, e a causa do erro possa ser recuperada pela função fError()

Referente ao chamado: DTAPPSRV-5559

Access Violation Application Server ao fazer a leitura de email

Incidente: Queda do AppServer ao fazer a leitura de um email.  
  
Solução: Corrigido a leitura de email na classe TMailMessage.

Referente ao chamado: DTAPPSRV-5624

HSMInitialize não lê a chave Module

Incidente: A função HSMInitialize não está carregando por padrão o valor da chave Module da seção SSLConfigure para o primeiro parâmetro.  
  
Solução: Corrigido a função HSMInitialize para fazer a carga do valor configurado na chave Module.

Referente ao chamado: DTAPPSRV-5712

TOTVS Application Server utilizado pelo License Server Virtual apresenta alto consumo de CPU

Incidente: O TOTVS | Application Server utilizado pelo License Server Virtual poderia apresentar um alto consumo de CPU durante a execução de uma integração nativa com o FTP da TOTVS.  
  
Solução: Realizamos uma correção para evitar que esse alto consumo de CPU ocorra durante o processamento do Response da camada de client FTP.

Referente ao chamado: DTAPPSRV-5335

TOTVS\_BROKER\_COMMAND Disable Server Broker com uso da chave SCHEDULE\_SERVER\_NN não bloqueia conexão

Incidente: no broker, cliente não estava conseguindo utilizar ao mesmo tempo as funcionalidades do scheduler ([https://tdn.totvs.com/pages/viewpage.action?pageId=563433831](https://tdn.totvs.com/pages/viewpage.action?pageId=563433831 "Follow link")) e da alteração temporária na tabela de balanceamento([https://tdn.totvs.com/pages/viewpage.action?pageId=521638009](https://tdn.totvs.com/pages/viewpage.action?pageId=521638009 "Follow link"))  
  
Correção: no broker, as funcionalidades do scheduler ([https://tdn.totvs.com/pages/viewpage.action?pageId=563433831](https://tdn.totvs.com/pages/viewpage.action?pageId=563433831 "Follow link")) e da alteração temporária na tabela de balanceamento([https://tdn.totvs.com/pages/viewpage.action?pageId=521638009](https://tdn.totvs.com/pages/viewpage.action?pageId=521638009 "Follow link")) foram compatibilizadas, conforme documentado nos links acima.

Referente ao chamado: DTAPPSRV-5537

Corrompimento de RPOs e mensagem de 'RPO in use'

Incidente:  
Esporadicamente, ou mediante a processos de compilação ou aplicação de patch, um ou mais RPOs se corrompem ou deixam o ambiente inacessivel com erro de RPO in use  
  
Solução:  
Melhorado algumas mensagens de erro (via console.log); correção no processo de abertura e fechamento dos RPOs para contagem de usuarios e controle de erros.

Alteração em conjunto com pluing TOTVS Developer Studio for VSCode, utilizar versão 1.3.11 ou superior.

Referente ao chamado: DTAPPSRV-5596

Falha em requisição WEBSERVICE ERROR : HTTP Content-length expected

Incidente: O recebimento de pacotes de dados via SSL com timeout igual a zero gera um pacote de dados menor do que o esperado quando as conexões tem alta latência.  
  
Solução: Adicionado timeout para aguardar recebimento de pacotes de dados via SSL. Se um timeout for definido pela camada AdvPL, é respeitado este timeout; Se vier zerado, é utilizado o valor de timeout configurado na seção SSLConfigure (default 2s).

Referente ao chamado: DTAPPSRV-5475

SaveAttach da TMailMessage não funciona com caminho de server

Inicidente: O método SaveAttach da classe TMailMessage não aceitava caminho relativo.  
  
Solução: Corrigido o método SaveAttach para aceitar caminho relativo (server).

Referente ao chamado: DTAPPSRV-5708

Fluig Identity - Erro: Invalid number of parameters

Incidente: O recebimento de pacotes de dados via SSL com timeout igual a zero gera um pacote de dados menor do que o esperado quando as conexões tem alta latência.  
  
Solução: Adicionado timeout para aguardar recebimento de pacotes de dados via SSL. Se um timeout for definido pela camada AdvPL, é respeitado este timeout; Se vier zerado, é utilizado o valor de timeout configurado na seção SSLConfigure (default 2s).

Referente ao chamado: DTAPPSRV-5733
