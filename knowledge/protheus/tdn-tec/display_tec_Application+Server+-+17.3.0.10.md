---
content_hash: 43781b024844a4cd1e7f08024327b59be5470d1fb1fd8a37c3119d89b8b210b7
fetched_at: '2026-07-02T19:24:24.245687+00:00'
page_id: '469459164'
product: protheus
source: tdn-tec
title: Application Server - 17.3.0.10
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.10
version: 6
---

GreenEXPEDIDO

# Melhoria

Registrar hora de aplicação de patch no console.log do Appserver

Solução: No console.log apresentará as informações:

RPO apply date: : 25/04/2019 15:34:19...  
updating: UPLOADCOVER.PRW...

(...)  
[DEBUG][SERVER] [Thread 17160] [25/04/2019 15:34:21]Updating RPO.

Referente ao chamado: MTEC-2562

# Correção

HTTPPARSER - Erro quando o conteúdo HTTP tem zero binário

Problema: Quando o corpo de uma requisição HTTP possui zero binário, o server parseava a mensagem de maneira incorreta e atribuía o tamanho incorreto à variável de tamanho (len) do corpo da requisição  
  
Solução: A solução é atribuir o valor original do tamanho total original do corpo da requisição a esta variável len. Assim, não parseamos novamente o corpo da requisição, todos os caracteres são corretamente transmitidos independente de ter zero binário no meio.

Referente ao chamado: TTEC-3000

Erro "Invalid Structured Data" ao ativar a chave de ini globalSyslog

Problema: Ao utilizar a chave de ini globalSyslog=val="valor", o appserver apresenta o erro "Invalid Structured Data" na sua inicialização.  
  
Solução: Em um caso onde é informado colchetes, foi corrigido o problema da leitura da variável.

Referente ao chamado: TTEC-3129

Coverage - Diferença na contagem de linhas

Problema: Ao executar o coverage em um arquivo, aparece linhas diferentes do que realmente tem.   
  
Solução: O problema ocorria por cache de macro com soma. Um dos elementos estava com o valor da linha da primeira execução, que era uma linha diferente do arquivo atual de sua execução.

Referente ao chamado: TTEC-3130

PFXCA2PEM - Access violation

Problema: Quando da execução da função PFXCA2PEM ocorre access violation após a falha na abertura do certificado.   
  
Solução: Correção da função PFXCA2PEM para verificar a falha na abertura do arquivo de certificado.

Referente ao chamado: TTEC-3145

Criar a propriedade bNoCheckPeerCert na classe TWSDLManager

Problema: Propriedade bNoCheckPeerCert não disponível no binário Lobo-Guará   
  
Solução: Criação da propriedade bNoCheckPeerCert na classe TWSDLManager.

Referente ao chamado: TTEC-3074

Access Violation na compilação TLPP com annotation

Incidente: Erro de exceção do Application Server quando do uso de Annotation.

Solução: Correção na deleção de annotations durante a compilação.

Referente ao chamado: TTEC-3128
