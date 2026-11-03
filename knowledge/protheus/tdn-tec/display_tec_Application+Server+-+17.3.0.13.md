---
content_hash: 3af6b9fa36788c58b6331b8c4ce8e4b5c615cc360c68b8bd84a5b5a05a1ec7c1
fetched_at: '2026-07-02T19:24:24.970468+00:00'
page_id: '493624709'
product: protheus
source: tdn-tec
title: Application Server - 17.3.0.13
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.13
version: 9
---

GreenEXPEDIDO

# Implementação

 SMARTERP - Implementar log de tempo na inicialização do AppServer

Referente ao chamado: TTEC-3175

# Melhoria

 Acréscimo do método SetSuppressHeaderExpect envolvendo WSDL e Post

Incidente: Problemas de requisição envolvendo o uso do campo de header expect no contexto de uso da classe tWsdlManager.  
  
  
Solução: Foram feitas correções e orientações quanto ao uso dos métodos "SetSuppressHeaderExpect" e "AddHttpHeader" da classe tWsdlManager.

Referente ao chamado: TTEC-3070

# Correção

 A função ProcSource , não retorna corretamente, quando a posição no stack passada é um CodeBlock ou Method de classe.

Referente ao chamado: TTEC-1520

 (LOBO GUARA) Função duplicada em PRW qdo a função existe em fonte 4gl

Incidente: Ao compilar uma função em fonte ADVPL de mesmo nome de uma função em fonte 4gl, o Server acusa erro de função duplicada.  
  
Solução: No fonte appmap.cpp, há uma comparação entre fontes 4gl e ADVPL que protege o Server de acusar função duplicada quando as funções compiladas nesses fontes têm o mesmo nome.

Referente ao chamado: TTEC-3043

 FINR350 - Error.log ao Personalizar Relatório

Incidente: Bloco bEnd() nao estava sendo chamado no encerramento da janela.  
  
  
Solução: Removido referencia adicional a janela que fazia com que o bloco de encerramento não fosse chamado.

Referente ao chamado: TTEC-3068

 Falha do componente WsdlManager no uso do método SendSoapMsg tendo como parâmetro o XML-SOAP a ser enviado.

Problema: Incompatibilidade entre mensagem XML-SOAP montada e submetida por requisição POST e a composição de alguns campos do header da requisição (elementos usados pertinentes à versão 1.1 do SOAP que não era o default - 1.2).   
  
Solução: Acréscimo da propriedade nSOAPVersion à classe WsdlManager para forçar o uso interno do protocolo SOAP efetivamente usado.

Referente ao chamado: TTEC-3182

 Queda e mau funcionamento na execução das funções pfxcert2pem e fclose nos testes automatizados no Astra-Linux.

Referente ao chamado: TTEC-3183

 Access Violation - BMPTOJPG

Incidente: Access Violation ao ser informado Bitmap de 16 bits  
  
  
Solução: Corrigido tratamento de erro que gerava a queda no appserver.

Referente ao chamado: TTEC-3184

 Access Violation - ADVPL Run

Incidente:  
  
  
Solução:

Referente ao chamado: TTEC-3187

 Quando é compilado um fonte vazio apresenta problema de compilação

Incidente: A compilação de um fonte vazio não remove o fonte da lista e causa erros de função duplicada.  
  
  
Solução: Correção na compilação para atualizar mapa de funções no repositório.

Referente ao chamado: TTEC-3191

 Access Violation - TXMLMANAGER

Incidente: Access violation no uso do método XPathHasAtt.  
  
  
Solução: Correção no método XPathHasAtt.

Referente ao chamado: TTEC-3193

[WARNING] Changed VarNameLen <FROM> to <TO>

Incidente: Mensagem [WARN ][SERVER] [Thread <ID>] Changed VarNameLen <FROM> to <TO>

Solução: A partir desta release pode aparecer esta mensagem no console do Application Server. Para detalhes clique .
