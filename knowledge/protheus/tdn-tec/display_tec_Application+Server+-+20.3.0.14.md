---
content_hash: 220c00b4c1d35aa51d51e6ec46da4dd64c4383ad3eba0c7ecdd85661c5c99c88
fetched_at: '2026-07-02T19:24:28.487819+00:00'
page_id: '707386436'
product: protheus
source: tdn-tec
title: Application Server - 20.3.0.14
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+20.3.0.14
version: 11
---

# Correções

RPO Custom corrompendo quando está vazio e aplica-se um patch.

Incidente: Ao realizar a aplicação de um patch, caso ainda não tenha sido criado um RPO Customizado, o ambiente cria um RPO Customizado corrompido.  
  
Solução: A geração da aplicação de patch passa agora a não criar mais o RPO Customizado, somente se necessário, como um patch a ser aplicado diretamente no RPO Customizado.

Referente ao chamado: DTAPPSRV-6471

O retorno da função 4GL DBTableExists() via interop não é avaliado corretamente no AdvPL.

Incidente: Ao executar a função 4GL DBTableExists via INTEROP, o seu retorno não é avaliado corretamente no AdvPL devido a diferença entre as linguagens.  
  
Solução: Correção aplicada para que o retorno seja compatível com a linguagem.

Referente ao chamado: DTAPPSRV-6456

Falha na GetApoRes quando resource possui 6 caracteres.

Incidente: Ao compilar um resource com nome contendo 6 caracteres, a função falha e retorna Nil.  
  
Solução: Correção para que a função trate corretamente resources com 6 caracteres.

Referente ao chamado: DTAPPSRV-6419

Erro ao utilizar o lockserver client com app\_environment ativa

Incidente: Para para que o LockServer conseguisse estabelecer conexão, era necessário configurar a chave SecureConnection=1 na seção LockServer. Ou seja, o módulo da porta Multi Protocolo estava falhando. O esperado era que não fosse necessário configurar nada, a porta multiprotocolo deveria se encarregar disso.  
  
Solução: Foi realizado um ajuste pontual no Application Server, agora não é mais necessário habilitar a chave SecureConnection.

Referente ao chamado: DTAPPSRV-6249

Erro conflito de encoding "Subject e cBody "da classe TMailMessage ao visualizar o e-mail

Incidente: Ao receber email pelo Appserver, o "subject" estava vindo com caracteres estranhos.  
  
Solução: Na recepção de email pelo appserver foi implementado o tratamento de codificação "quoted printable" e "base 64" no "subject" das mensagens.

Referente ao chamado: DTAPPSRV-6159

Falha na inicialização do AppServer com Rest 2.0 e Rest MPP ativados

Incidente: Ao tentar utilizar Rest 2.0 em conjunto com o Rest Porta MultiProtocolo configurados no mesmo appserver.ini, ocorria o erro "[ERROR][SERVER] [MPPORT] Error on exec Rest Server function. Invalid REST Port. Error: -107".  
  
Solução: Foi realizado ajustes na inicialização de ambos os serviços, agora é possível utilizá-los em simultâneo.

Referente ao chamado: DTAPPSRV-5605

Não é possível utilizar autenticação OAuth2 com as classes TMailManager e TMailMng.

Incidente: Não é possível utilizar autenticação OAuth2 com as classes TMailManager e TMailMng.  
  
Solução: Foi Implementado na classe TMailManager o método SetOAuthToken, que define o token OAuth2 que será utilizado para os protocolos IMAP, POP e SMTP; e implementada na classe TMailMng a propriedade cOAuthToken, que permitirá definir e ler o token OAuth2 que será utilizado.

Referente ao chamado: DTAPPSRV-6277

Alto volume de threads concorrentes poderia causar uma falha na camada que obtém dados como IP e HOST NAME do servidor, gerando uma queda da aplicação.

Incidente: Um cenário com alto volume de threads concorrentes poderia causar uma falha na camada que obtém dados como IP e HOST NAME do servidor, gerando uma queda da aplicação.  
  
Solução: Ajuste realizado no TOTVS | Application Server para que essa camada seja thread-safe e assim não ocorram problemas de queda da aplicação.

Referente ao chamado: DTAPPSRV-6232

Licenças presas quando thread finalizada via TOTVS Monitor

Incidente: Ocorrência: Processo finalizado pelo Totvs Monitor continua consumindo licença e mantendo locks nomeados no license server (LockByName).  
  
Solução: Mesmo que um processo ( SmartClient ou JOB Advpl ) esteja em loop ou bloqueado aguardando um retorno de uma API, utilizar a opção "Derrubar imediatamente" o processo via Totvs Monitor vai liberar e encerrar imediatamente a conexão com o License Server -- liberando licenças e locks nomeados (LockByName) do processo em questão. 

Referente ao chamado: DTAPPSRV-6473
