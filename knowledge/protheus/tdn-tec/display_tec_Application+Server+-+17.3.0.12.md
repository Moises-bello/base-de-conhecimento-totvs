---
content_hash: ae93244c5a154d4dc60a655fee42402d8ff303ed8973632857249c562653345d
fetched_at: '2026-07-02T19:24:24.838594+00:00'
page_id: '490331274'
product: protheus
source: tdn-tec
title: Application Server - 17.3.0.12
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.12
version: 7
---

GreenEXPEDIDO

# Correção

Queda Appserver após compilar arquivo .PER (4gl Logix)

Problema: Queda Appserver após compilar arquivo .PER (4gl Logix).  
  
Solução: Correção na compilação de arquivos com extensão PER.

Referente ao chamado: TTEC-3042

 A função SerialNumber no binário 32 bits estava retornando número serial para unidades "não prontas" (unidade DVD/ROM)

Problema: A função SerialNumber no binário 32 bits estava retornando número serial para unidades "não prontas" (unidade DVD/ROM).   
  
Solução: Alterado método  (windows) para que em situações de falha o número serial retornado seja zero, como já é feito na versão x64.

Referente ao chamado: TTEC-3156

Exception na função HSMFinalize

Problema: Exception na função HSMFinalize na versão debug.   
  
Solução: Correção da função .

Referente ao chamado: TTEC-3172

Access Violation na impressão de rescisão 

Problema: Access Violation na impressão de rescisão.   
  
Solução: Inserido proteção para valores nulos.

Referente ao chamado: MTEC-2480

Access Violation na após tentativa de conexão de dispositivo telnet

Problema: Access Violation na após tentativa de conexão de dispositivo telnet.   
  
Solução: Inserido proteção para valores nulos.

Referente ao chamado: MTEC-2600

Access Violation em diversas rotinas

Problema: Access Violation em diversas rotinas.   
  
Solução: Implementado proteção para que objeto de interface.

Inserido proteção para macros quando criadas via codeblock não sejam deletadas antes do que deveriam.

Inserido proteção para que não seja permitido criar mais de um RPO Auxiliar simultaneamente.

.

Referente ao chamado: MTEC-2025

Mensagem: Failed to read status of inifile [appserver.ini][75][Value too large for defined data type]

Problema: Mensagem: Failed to read status of inifile [appserver.ini][75][Value too large for defined data type].   
  
Solução: Inserido globalmente suporte ao large file suporte.

Referente ao chamado: MTEC-2452

Access Violation durante Parser WSDL Serasa

Problema: Access Violation durante Parser WSDL Serasa.   
  
Solução: Corrigido para que Schemas já parseados não sejam reparseados o que gerava recursão infinita.

Referente ao chamado: MTEC-2498

Problema na função Directory para quando utilizada para RootPath "C:/" ou para diretórios mapeados "\\path-mapeado\"

Problema: Problema na função Directory para quando utilizada para RootPath "C:/" ou para diretórios mapeados "\\path-mapeado\" .   
  
Solução: Corrigido para que Schemas já parseados não sejam reparseados o que gerava recursão infinita.

Referente ao chamado: MTEC-2530

Erro HTTPGet - 400 Bad Request e 302 Found

Problema:  Erro HTTPGet - 400 Bad Request e 302 Found.  
  
Solução: Correção na função .

Referente ao chamado: MTEC-2546
