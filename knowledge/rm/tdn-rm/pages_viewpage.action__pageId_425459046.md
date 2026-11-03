---
content_hash: 3b3f822899df275c4ef9f3a6e1b93fff38e920199109845e7317283ba283a192
fetched_at: '2026-06-29T00:09:33.772521+00:00'
page_id: '425459046'
product: rm
source: tdn-rm
title: BackOffice Protheus x TOTVS Incorporação - Configuração e Parâmetros BackOffice
  Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459046
version: 6
---

**Configuração e Parâmetros BackOffice Protheus**

---

**Configurar appserver.ini**

* O appserver.ini carrega as configurações do Protheus e deve ser configurado.

**Configurar o EAI**

* Módulo SigaCFG > Ambiente > Schedule > Schedule

**Configurar agendamento (Scheduler)**

* Múdulo SigaCFG > Ambiente > Schedule

**Configurar Integração**

Na integração BackOffice Protheus x TOTVS Incorporação, existem parâmetros necessários para serem configurados no Protheus:

* Módulo SigaCFG > Ambiente > Cadastros > Parâmetros.

Localize os parâmetros e configure conforme solicitado abaixo:

* MV\_EAIURL2= Endereço WebService que Receberá os Dados Enviados (Exemplo: <http://10.31.8.90/TBC/wsEAIService.asmx?wsdl>).
* MV\_EAIWS= Informe o nome do Client WebService do EAI para envio a outro EAI. (WSEAISERVICE).
* MV\_EAIUSER= <Nome de usuário> (Opcional em caso do Servidor precisar de Autenticação).
* MV\_EAIPASS= <Senha de usuário> (Opcional em caso do Servidor precisar de Autenticação).
* MV\_EAIMETH= Informe o método de envio do EAI para envio a outro EAI. (RECEIVEMESSAGE).

**Obs**: verificar o firewall (desabilite-o)
