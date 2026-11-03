---
article_id: 360044297654
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: af56d38244484068ceb2eecaf57192a63000a9aaf6156cd130eb14a8ad3c0786
fetched_at: '2026-06-28T22:39:57.441323+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - FLORIANOPOLIS
  - Mensagem de Envio Token --->  Vazio
type: support-article
updated_at: '2025-07-08T19:42:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044297654-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-FLORIANOPOLIS-Mensagem-de-Envio-Token-Vazio
---

**Dúvida**Como corrigir para FLORIANOPOLIS - Mensagem de Envio Token ---> Vazio  
 **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**

Ao transmitir uma nota para Florianópolis-SC, o status da nota no monitor fica "Aguardando Transmissão do Lote" e no console do TSS ocorre o erro abaixo:

Mensagem de Envio Token --->

Parametros de acesso

-------------------------------------------------------------------------------

WSCERRINT / type mismatch on +

ADVPL WSDL Client 1.120703 / TOTVS MSSQL Sped on 20200207 10:05:27

-------------- CallStack --------------

Called from ENVIARLOTE ( 124)

Called from { || oWS2:EnviarLote ( 39)

Called from TSSEXECWSRET ( 40)

Called from ENVNFSE017 ( 379)

Called from TSSNFSETRANSMISSAO ( 756)

Called from {|aRecProc|tssNfseTr ( 183)

Called from EXECUTE ( 236)

Called from TSSNFSEEMISSAO ( 95)

Called from TSSPROCEXEC ( 277)

Called from PREPAREIPCWAIT ( 103)

-------------------------------------------------------------------------------

A prefeitura de Florianópolis exige algumas informações para autenticação na comunicação com o webservice.  
Todas essas informações devem ser preenchidas na ultima tela do wizard.config da rotina FISA022.  
O conteúdo para cada campo deve ser solicitado para a prefeitura.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060247554/mceclip0.png)

O conteúdo de cada campo é gravado na tabela SPED000 conforme a regra abaixo:

**Parâmetro na SPED000 - Campo Wizard.cfg - Conteúdo à ser informado:**  
  
MV\_NFSUSER - Usuário - CMC do Contribuinte  
MV\_NFSPASS - Senha - Senha  
MV\_AUTORIZ  - Autorização - AEDFe  
MV\_CHVAUTE  - AEDFe - AEDFe  
MV\_CLIENID - Client ID - Client ID  
MV\_CLIENSC - Client Secret - Client Secret  
  
**Observação**I. Para obter o AEDF, clique [aqui](http://www.pmf.sc.gov.br/sites/fiac/index.php?cms=informacoes+basicas&menu=3)  
II. Para obter o client\_id e client\_secret, clique [aqui](https://nfps-e.pmf.sc.gov.br/faq/index.html) (Menu 'Como uma aplicação pode realizar o acesso aos serviços junto ao Sistema?')  
  
**IMPORTANTE**Quando solicitado para a prefeitura algum tipo de credencial, deverá SEMPRE se identificar com as nomenclaturas citadas na última coluna: 'Conteúdo à ser informado', caso contrário eles não saberão informar, visto que são campos próprios do Protheus.
