---
content_hash: aa1119c068d553727af7e92d0f22ba02924017e9fb476aa4d06a4622de125fc0
fetched_at: '2026-07-02T19:24:27.974060+00:00'
page_id: '701002525'
product: protheus
source: tdn-tec
title: Application Server - 20.3.0.11
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.0.11
version: 3
---

# Correções

Erro no LockServer relacionado a problemas na configuração da chave SpecialKey no Linux.

Incidente: Falso negativo de erro "Problemas na configuração da chave SpecialKey, entre em contato com o Administrador! ",  usando AppServer em ambiente Linux, mesmo que a configuração estivesse correta e o  LockServer estivesse configurado corretamente.  
  
Solução: Melhorias e proteções adicionais nos mecanismos de criação e abertura de arquivo no Linux.

Referente ao chamado: DTAPPSRV-5791

Falha no HTTPS - Error on exec Rest Server Function. Invalid Rest Port. Error -107

Incidente: Casos específicos onde o HTTPS não funciona na versão 12.1.33 com a mensagem de erro: Error on exec Rest Server function. Invalid REST Port. Error: -107  
  
Solução: Foi implementada uma correção envolvendo um dos componentes da biblioteca de comunicação que atua no REST.

Referente ao chamado: DTAPPSRV-5812

WSCLIENT não priorizando RPO Custom

Incidente: Classes filhas da WSCLIENT não estavam sendo carregadas prioritariamente do RPO Custom.  
  
Solução: Correção na leitura da classe errada, carregando a classe do RPO Custom primeiro, caso exista.

Referente ao chamado: DTAPPSRV-5877

Encode64 e Decode64 falhando em execução a partir da ferramenta por linha de comando

Incidente: Funções Encode64 e Decode64 quando chamada via ADVPL Command Line estavam falhando.  
  
Solução: O problema tinha origem no tratamento do path passado para as funções. Correção aplicada no tratamento do path.

Referente ao chamado: DTAPPSRV-6093

Função APPEND FROM falhando ao importar arquivos externos.

Incidente: Função APPEND FROM falhando ao importar arquivos externos.  
  
Solução: Foram realizadas os devidos ajustes no Application Server.

Referente ao chamado: DTAPPSRV-6205

Retenção de memória com string e Substr()

Incidente:  Função substr() com retenção de memória a cada execução.  
  
Solução: Correção aplicada no cache interno da função que mantinha em memória as strings retornadas pelo comando SubStr(). Isso é imperceptível quando as strings são pequenas, porém, quando são grandes, isso torna-se visível. 

Referente ao chamado: DTAPPSRV-6223

Queda no Application Server durante parser no WSDL

Incidente:  Queda do Application Server (Access Violation / Segment Fault) no final da thread, após utilizar a classe tWSDLManager.  
  
Solução: Revisada e corrigida a limpeza de memoria da classe tWSDLManager.

Referente ao chamado: DTAPPSRV-6231 e DTAPPSRV-6182

Serviço Rest não estava aceitando query strings no formato "?&var1=val1&var2=val2...".

Incidente:  O serviço REST não estava aceitando query strings da forma "?&var1=val1&var2=val2...", que são aceitas pelo REST ADVPL (notar o '&' inicial logo após o '?").  
  
Solução: Alteração no parsing das query strings para aceitar esse '&' inicial.

Referente ao chamado: DTAPPSRV-6240

Função unzip falhando na descompactação de arquivo

Ocorrência: Função FUnzip() retorna 0 (sucesso) sem descompactar todos os arquivos do ZIP.

Solução: Mecanismo de tratamento de retorno de erro da compactação corrigido.

Referente ao chamado: [DTAPPSRV-6308](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6308)

Serviço do AppServer não para de maneira esperada

Ocorrência: O AppServer fica travado ao tentar finalizar.

Solução: Correção no gerenciamento dos contextos bloqueados do Vader e com isso, libera a continuidade do processo e o encerramento do AppServer.

Referente ao chamado: [DTAPPSRV-6280](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6280)

Erro ao sincronizar app "Minha Coleta de Fardões".

Ocorrência: O aplicativo "Minha Coleta de Fardões" não estava funcionando corretamente.

Solução: Correção no tratamento das query strings utilizadas pelo aplicativo.

Referente ao chamado: [DTAPPSRV-63](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6280)24

Erro na função FwMsExcelXlsx em ambiente Linux.

Ocorrência: Ao utilizar a função File2Printer para verificar a versão do executável da printer via AppServer Linux, o executável não é encontrado pela chamada do SO.

Solução: Isto acontecia pois o comando enviado para o SO não continha o prefixo de execução "./",  foi aplicada correção na chamada dentro da File2Printer.

Referente ao chamado: [DTAPPSRV-](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6280)6082

Mensagens repetidas de erro na monitoração ativa do Broker.

Ocorrência: Monitoração ativa do broker em ambiente Linux estava gerando repetidas mensagens "erro 0 na readNumber: Success" no console.log

Solução: Correção para essas mensagens não serem gravadas no console.log.

Referente ao chamado: [DTAPPSRV-](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6280)6206

Rest error, the handle status is closing, the new message will be discarded and the handle will be closed.

Ocorrência: Transações com REST 2.0 e header "Connection: close" poderiam apresentar mensagens de erro indevidas "Error, the handle status is closing, the new message will be discarded" no console.log.

Solução: Correção no tratamento das mensagens.

Referente ao chamado: [DTAPPSRV-](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6280)6261
