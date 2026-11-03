---
content_hash: eaa731493bff4fab36ff1e987587be79d87d11d414147e42e50560332cc4d5b8
fetched_at: '2026-07-02T19:24:27.730159+00:00'
page_id: '678581430'
product: protheus
source: tdn-tec
title: Application Server - 20.3.1.0
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.1.0
version: 42
---

Application Server - 20.3.1.0

Implementação da classe tGrpc

Ocorrência: Suporte ao protocolo gRPC para o SmartLink

Solução: Implementação da biblioteca gRPC com suporte ao SmartLink através da classe .

Referente ao chamado: DTAPPSRV-5122

Ordenação de objeto JSON

Ocorrência: Ao utilizar JSonObject() e posteriormente recuperar o json a partir de oJson:ToJson(), o retorno gerado perde toda a sequência que foi incluída no objeto json.

Solução: Implementação para manter a ordem original do objeto JSON em memória.

Referente ao chamado: DTAPPSRV-2718

Broker Agent

Ocorrência: Automação para escalabilidade horizontal dos serviços do **true**.

Solução: Implementação do Broker Agent. Detalhes para uso: .

Referente ao chamado: DTAPPSRV-5216

Implementar função TCSqlToArr

Solução: Implementar uma função  da RDD TOPConn, que execute uma Query, e retorne um array de resultados.

Referente ao chamado: [TPGW-348](https://jiraproducao.totvs.com.br/browse/TPGW-348)

Broker HTTP não exibe a tela de status

Ocorrência: Broker HTTP não exibe tela de status.

Solução: Correção para o travamento da tela de Status.

Referente ao chamado: [DTAPPSRV-6318](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6318)

Função unzip falhando na descompactação de arquivo

Ocorrência: Função FUnzip() retorna 0 (sucesso) sem descompactar todos os arquivos do ZIP.

Solução: Mecanismo de tratamento de retorno de erro da compactação corrigido.

Referente ao chamado: [DTAPPSRV-6308](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6308)

Serviço do AppServer não para de maneira esperada

Ocorrência: O AppServer fica travado ao tentar finalizar.

Solução: Correção no gerenciamento dos contextos bloqueados do Vader e com isso, libera a continuidade do processo e o encerramento do AppServer.

Referente ao chamado: [DTAPPSRV-6280](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6280)

Erro no tratamento das query strings utilizadas pelo aplicativo "Minha Coleta de Fardões"

Ocorrência: Erro no tratamento das query strings causa mau funcionamento do aplicativo "Minha Coleta de Fardões".

Solução: Correção no tratamento das query strings utilizadas pelo aplicativo.

Referente ao chamado: DTAPPSRV-6324

Rest não estava aceitando query strings formato "?&var1=val1&var2=val2..."

Ocorrência: REST não estava aceitando query strings da forma "?&var1=val1&var2=val2..." que são aceitas pelo REST ADVPL (notar o '&' inicial logo após o '?").

Solução: Alteração no parsing das query strings para aceitar esse '&' inicial.

Referente ao chamado: [DTAPPSRV-6240](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6240)

Função APPEND FROM falhando ao importar arquivos externos.

Ocorrência: Função APPEND FROM falhando ao importar arquivos externos.

Solução: Foram realizadas os devidos ajustes no Application Server.

Referente ao chamado: [DTAPPSRV-6205](https://jiraproducao.totvs.com.br/browse/DTAPPSRV-6205)

Erro -100 no Rest 2.0

Ocorrência:  Erro -100 em transações com REST 2.0.

Solução: Correções realizadas no Rest 2.0 para o caso do erro -100.

Referente ao chamado: DTAPPSRV-5832

Erro na geração de relatórios em Planilha Excel no Linux

Ocorrência:  Erro na geração de Relatórios padrões do ERP impressos no modo Planilha/Excel em servidores Linux onde o arquivo final gerado, somente continha o cabeçalho e definições da planilha Excel, ou seja, sem os dados e assim, gerando um arquivo incompleto que não era possível ser aberto pelo Excel.

Solução: Correção aplica na camada de manipulação de arquivo.

Referente ao chamado: DTAPPSRV-6703

Função GetRpoLog não retorna dados do Patch (\*.PTM) customizado aplicado

Ocorrência:  Função GetRpoLog não retorna os patchs que estão aplicados no RPO Custom.

Solução: Foram realizados ajustes pontuais na função GetRpoLog.

Referente ao chamado: DTAPPSRV-6681

4GL - Access Violation e4GLBlockStmt

Ocorrência:  Ao executar o comando de SQL em bloco, sem realizar a conexão com o banco dinamicamente ou via comando DATABASE no mesmo fonte, o server aborta a execução. 

Solução: O modelo de conexão com o banco tinha a falha onde não encontrava o fonte na chamada fora da execução do bloco SQL

* Esta ocorrência afeta somente a Linguagem 4GL.

Referente ao chamado: DTAPPSRV-6668

Falha ao desfragmentar RPO Default

Ocorrência:  O recurso de desfragmentação de RPO passou a apresentar problemas e não está realizando a desfragmentação do RPO Default.

Solução:  Foram realizados ajustes na camada responsável pela desfragmentação e o problema foi solucionado.

Referente ao chamado: DTAPPSRV-6667

AppServer Command Line apresentando alto consumo de memória

Ocorrência:  A ferramenta de compilação por linha de comando (AppServer Command Line) está apresentando alto consumo de memória ao realizar compilação de um grande número de fontes, resultando em erros de alocação de memória.

Solução:  A ferramenta foi ajustada para realizar a compilação por blocos de até 1000 arquivos sequencialmente.

Referente ao chamado: DTAPPSRV-6665

Funções GetResArray e GetSrcArray não retornam elementos com extensão .app do RPO Custom

Ocorrência:  Funções GetResArray e GetSrcArray não retornam elementos com extensão .app do RPO Custom

Solução:  Foram realizados ajustes e correções para que as funções AdvPL passem a retornar corretamente elementos com extensão .app.

Referente ao chamado: DTAPPSRV-6565

4GL - Função SubString em atribuição e teste condicional IF de CHAR em posição inválida não apresentam erros.

Ocorrência:  Função SubString em atribuição e teste condicional IF de CHAR em posição inválida não apresentam erros.

Solução:  Foram realizadas correções para em situação de erros, abortar e informar a linha de código fonte 4GL onde o problema ocorreu.

* Esta ocorrência afeta somente a Linguagem 4GL

Referente ao chamado: DTAPPSRV-6559

Permitir a compilação de Web Functions sem token de compilação

Ocorrência:  Permitir a compilação de Web Functions sem token de compilação

Solução:  Ajustes para compilação de HTML function e Web Function sem token de compilação.

Referente ao chamado: DTAPPSRV-6554

Requisição com proxy ativo falhando na função HTTPQuote

Ocorrência:  Cliente relatava que ao tentar realizar uma requisição com Proxy ativo, a função HTTPQuote falhava para qualquer um dos métodos disponíveis (GET, POST, PUT, PATCH, DELETE).

Solução:  Foram realizados ajustes relacionados ao serviço de Proxy e as requisições com a função HTTPQuote passaram a se comportar corretamente.

Referente ao chamado: DTAPPSRV-6537

Aplicação de patch não esta checando a data de elementos do tipo Resource e está substituindo os arquivos mesmo que a opção para NÃO aplicar arquivos mais antigos esteja habilitada.

Ocorrência:  Aplicação de patch não esta checando a data de elementos do tipo Resource e está substituindo os arquivos mesmo que a opção para NÃO aplicar arquivos mais antigos esteja habilitada.

Solução:  Foi corrigido a checagem da opção para o tipo resource.

Referente ao chamado: DTAPPSRV-6535

4GL - Access Violation com SQL PREPARE

Ocorrência:  Access Violation quando é feito um SQL PREPARE dentro de uma REPORT FUNCTION.

Solução:  Foi corrigido o parâmetro que pega o nome da função que compõe a query que define o cursor interno, como é report e não função, ele se perdia.

* Esta ocorrência afeta somente a linguagem 4GL.

Referente ao chamado: DTAPPSRV-6087

TMailMessage:Clear não limpa o último campo que foi definido

Ocorrência: O método Clear da TMailMessage não limpa o último campo definido no objeto.

Solução: Corrigido a limpeza feita pelo método Clear da TMailMessage.

Referente ao chamado: DTAPPSRV-5981

Erro ao compilar fonte por linha de comando no linux com seção LockServer

Ocorrência: Ao executar o Application Server Command Line no Linux, com o LockServer ativo, ele fica aguardando e/ou procurando o Lockserver indicado

Solução: Para Application Server Command Line, compilação e execução, a procura pela conexão ao Lockserver é ignorada.

Referente ao chamado: DTAPPSRV-6129

Desativar a autenticação para envio de e-mail seção [MAIL]

Ocorrência: Ao desativar as chaves SMTPAuthLogin, SMTPAuthPLAIN ou SMTPAuthNTLM no appserver.ini, o Application Server continuava realizando as autenticações. Os valores que eram impostos as chaves em questão eram desconsiderados pelo Application Server, que considerava como se essas estivessem desabilitadas.

Solução: Foram realizadas as devidas correções e agora Application Server considera o valor das chaves SMTPAuthLogin, SMTPAuthPLAIN e SMTPAuthNTLM.

Referente ao chamado: DTAPPSRV-6227

Erro ao utilizar o lockserver client com app\_environment ativa

Ocorrência: para que o LockServer conseguisse estabelecer conexão, era necessário setar a chave SecureConnection=1 na seção LockServer. Ou seja, o módulo da porta Multi Protocolo estava falhando. O esperado era que não fosse necessário configurar nada, a porta multiprotocolo deveria se encarregar disso.

Solução: Realizado correção no Application Server, agora não é mais necessário habilitar a chave SecureConnection.

Referente ao chamado: DTAPPSRV-6249

MPUPDATEPACK não aplica o pacote da forma esperada

Ocorrência: Foi reportado um problema na utilização do MPUPDATEPACK, durante a copia de arquivos via FTP.

Solução: Correção na listagem de arquivos via FTP.

Referente ao chamado: DTAPPSRV-6279

Instrução RETURN <variavel> CLIPPED não acusa falha quando não declarada

Ocorrência: Ao compilar um fonte com uma variavel indefinida seguida do comando CLIPPED, a compilação passa e o programa falha.

Solução: Corrigindo a compilação para validação da variável; necessário recompilação.

* Esta ocorrência afeta somente a linguagem 4GL.

Referente ao chamado: DTAPPSRV-6283

TAF/TSS Configuração Certificado A3 ERRO Marca VALID

Ocorrência: Falha na carga de chave privada usando certificado A3, marca VALID com HSM, quando o nome do label da chave privada é menor que o nome original do label do certificado.

Correção: A comparação para a busca do label da chave privada passa a considerar como iguais o label procurado e o label encontrado, quando o nome do label existente no certificado, mesmo menor que o label procurado, considerando a igualdade pela menor string na comparação.

Referente ao chamado: DTAPPSRV-6286

Bloqueio em compilação e execução de fontes com mesmo nome

Ocorrência: Existiam diversos erros de execução que poderiam ocorrer caso exista conflitos de nomes de fonte entre os RPOs Default e Custom.

Solução: Foi ajustado o bloqueio das compilações e/ou execuções de fontes e/ou resources com o mesmo nome, para que não ocorram esses problemas.

Para mais informações acesse: [RPOs Segregados](https://tdn.totvs.com/display/tec/Application+Server+-+RPOs+Segregados)

Referente ao chamado: DTAPPSRV-6301

Método ParseURL da classe TWSDLManager apresenta erro durante parser de Schemas que não possuem nameSpace definido

Ocorrência: O método ParseURL pode apresentar falha caso haja imports de Schemas e/ou outros WSDL sem NameSpace definido

Solução: Fizemos um ajuste na lib de WSDL para prever cenários como esse, fazendo assim com que o parser ocorra com sucesso e que as mensagens sejam montadas de acordo com suas definições.

Referente ao chamado: DTAPPSRV-6406

GetApoRes - Erro no acesso a resources com 6 caracteres

Ocorrência: Mal funcionamento da função GetApoRes, retorna Nil (nada) ao utilizar um resource que possua o nome que contenha seis caracteres.

Solução: Este situação ocorria em uma condição de validação interna na função, os ajustes necessários foram aplicados na função GetApoRes.

Referente ao chamado: DTAPPSRV-6419

Suporte a 4GL no Application Server Command Line

Ocorrência: Indisponibilidade do Application Server Command Line para a linguage 4GL   
  
Solução: Suporte ao Application Server Command Line na compilação de fontes 4GL e execução de funcções via parametro run. Mais informações em:

Referente ao chamado: DTAPPSRV-6439

Tipagem de função 4GL que retorna valor booleano não é entendida no ADVPL (interop) com o valor inteiro

Ocorrência: A função getLastErrSQLInfo() estava retornando o último erro somente no banco SQL Server.

Solução: Foi corrigida o retorno no banco Informix e Oracle agora todos os bancos homologados retornam o último erro.

Referente ao chamado: DTAPPSRV-6456

CURSOR Informix - FRT0006 - Inclusão de registro acusa falha de CEP não cadastrado

Ocorrência: Problema na localização do cursor no banco informix.

Solução: Alterado a busca por cursores no banco Informix.

Referente ao chamado: DTAPPSRV-6459

Broker - Exibir o número máximo de conexões na interface de status

Ocorrência: Exibir na tela de status do Broker o número máximo de conexões global e para cada REMOTE\_SERVER, se for configurado.

Solução: Adicionado na tela de status do Broker o número máximo de conexões global e para cada REMOTE\_SERVER, se for configurado.

Referente ao chamado: DTAPPSRV-5422

Invalid self class Interface ao executar \_Super em codeblock

Ocorrência: Ao inserir uma chamada de \_Super: e depois aciona-lo em outro ponto em um componente, ele apresenta o erro Invalid self class.

Solução: Correção para tratar essa chamada no codeblock.

Referente ao chamado: DTAPPSRV-6140

Query String - Erro no tratamento de parâmetros sem conteúdo

Ocorrência: o REST 2.0 estava ignorando parâmetro de "query string" com conteúdo vazio (p.ex.: "....aaa=&aaa=bbb...", notar que "aaa" tem conteúdo vazio).

Solução: Correção no parse de query strings para tratar parâmetros com conteúdo vazio.

Referente ao chamado: DTAPPSRV-6516

Adequar comportamento de TCUniqe() do SQLITE com o DBACCESS

Ocorrência:  Falha de criação de índice único usando TCUnique() com SQLITE -- RDD TOPCONN usando RPODB=SQLITE, quando existe um registro marcado para deleção ( D\_E\_L\_E\_T\_ = '\*' ) onde o valor do campo R\_E\_C\_D\_E\_L\_ está 0 (zero).

Solução: A execução da TCUnique() executa uma etapa anterior de ajuste, para garantir que todos os registros marcados para deleção estejam com o valor do campo R\_E\_C\_D\_E\_L correto.

Referente ao chamado: DTAPPSRV-6173

Application Server Command Line não gera erro quando o token está em branco

Ocorrência: Na utilização do Application Server Command Line para compilação caso seja informado um token e o mesmo estiver inválido ou em branco, atualmente é apresentado apenas uma mensagem de Warning.

Solução: Alterado para apresentar um erro e encerrar o processo de compilação.

Referente ao chamado: DTAPPSRV-6516

Função GETLASTERRSQLINFO não retorna o último erro para Informix e Oracle

Ocorrência: A função getLastErrSQLInfo() estava retornando o último erro somente no banco SQL Server.

Solução: Foi corrigida o retorno no banco Informix e Oracle agora todos os bancos homologados retornam o último erro.

Referente ao chamado: DTAPPSRV-6485

Erro na inicialização do Applicatin Server quando MPP e REST 2.0 ativos

Ocorrência: Ao tentar utilizar Rest 2.0 em conjunto com o Rest MPP configurados no mesmo appserver.ini, ocorria o erro "[ERROR][SERVER] [MPPORT] Error on exec Rest Server function. Invalid REST Port. Error: -107".

Solução: Foi realizado ajustes na inicialização de ambos os serviços, agora é possível utilizá-los em simultâneo.

Referente ao chamado: DTAPPSRV-5605

Erro conflito de encoding "Subject e cBody "da classe TMailMessage ao visualizar o e-mail

Ocorrência: ao receber email pelo Application Server, o "subject" estava com caracteres estranhos.

Solução: na recepção de email pelo Application Server foi implementado o tratamento de codificação "quoted printable" e "base 64" no "subject" das mensagens.

Referente ao chamado: DTAPPSRV-6159

Broker HTTP - Erro na tela de status

Ocorrência: Broker HTTP não exibe a tela de status.

Solução: Correção no Broker HTTP para exibir a tela de status.

Referente ao chamado: DTAPPSRV-6318

RPO Custom corrompendo quando está vazio e aplica-se um patch

Ocorrência: Ao realizar a aplicação de um patch, caso ainda não tenha sido criado um RPO Customizado, o ambiente cria um RPO Customizado corrompido.

Solução: A geração da aplicação de patch passa agora a não criar mais o RPO Customizado, somente se necessário, como um patch a ser aplicado diretamente no RPO Customizado.

Referente ao chamado: DTAPPSRV-6471

Limite no uso de portas LPT/COM

Ocorrência: Na função IsPrinter os uso de porta LPT e COM era limitado até LPT6.

Solução: Ampliado o limite na função IsPrinter de portas para até LPT9 e COM9.

Referente ao chamado: DTAPPSRV-6636

Aplicação de patch com artefatos do tipo resource mais antigos sempre são substituídos

Ocorrência: Na função IsPrinter os uso de porta LPT e COM era limitado até LPT6.

Solução: Ampliado o limite na função IsPrinter de portas para até LPT9 e COM9.

Referente ao chamado: DTAPPSRV-6535

ORACLE - NATIVE ERROR : -1036 - ORA-01036: ILLEGAL VARIABLE NAME/NUMBER

Ocorrência: O erro ocorre em situações específicas de processamento da tradução com a query com o simbolo de interrogação

Solução:  Correção na checagem do símbolo antes do processamento da tradução da query para o banco Oracle.

Referente ao chamado: DTAPPSRV-6281

4GL - FOREACH não funciona conforme esperado

Ocorrência: Utilizando FOREACH no 4GL, está ocorrendo falha nos resultados pois existia um problema na localização de cursores já criados e reutilizados.

Solução:  Melhorado a busca por cursores, buscando em todas as listas existentes.

* Esta ocorrência afeta somente a linguagem 4GL.

Referente ao chamado: DTAPPSRV-6457

Descontinuação do LockServer no Linux

Ocorrência: Criação, abertura, fechamento e deleção de arquivos no File System Linux por meio das funções AdvPL FCreate, FOpen, FClose e FErase

Solução:  A camada de acesso a disco foi melhorada, com proteções e otimizações adicionais para concorrência e sincronismo de dados em disco. Por isso, não é mais necessário o uso do LockServer em ambientes Linux.

Mais informações:

Referente ao chamado: DTAPPSRV-6518

Broker HTTP funcionando apenas com broker e AppServer na mesma máquina.

Ocorrência: Broker HTTP funcionando apenas com broker e AppServer na mesma máquina.

Solução:  Correção na resolução de nomes DNS do Broker HTTP, que estava retornando sempre 127.0.0.1 (localhost).

Referente ao chamado: DTAPPSRV-6449

Trim feito indevidamente em items de ComboBox

Ocorrência: Trim feito indevidamente em itens de ComboBox.

Solução:  Removido a instrução de trim() para itens de ComboBox.

Referente ao chamado: DTCLIENT01-3691

Biblioteca CTREECB descontinuada

Solução:  A biblioteca CTREECB.DLL ou LIBCTREECB.SO estão descontinuadas. Mais informações em: .
