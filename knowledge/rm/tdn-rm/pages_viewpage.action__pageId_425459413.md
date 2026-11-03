---
content_hash: c2d8ea0a209695f97cff2674cd16df6d68678dcd88a44150c1ad2f913f6b0de2
fetched_at: '2026-06-29T00:09:35.886769+00:00'
page_id: '425459413'
product: rm
source: tdn-rm
title: Configurando a integração Backoffice TOTVS Protheus X TOTVS Incorporação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459413
version: 9
---

**Configurando a integração Backoffice TOTVS Protheus X TOTVS Incorporação**

---

1- Acesse: TOTVS RM/Integração/ Ferramentas/ Configurar

2- Clique em \*\[Avançar\]\* para iniciar o processo

3- Informe o usuário e senha do usuário rm do banco de dados qual a integração será criada

4- Clique no botão \*\[Testar Conexão\].\* Se ocorrer com sucesso, o botão \*\[Avançar\]\* será habilitado

5- Clique em \*\[Avançar\]

6- Selecione o checkBox \*\[TOTVS Incorporação x Backoffice Protheus\]\*

7- Clique no botão \*\[Avançar\]\* e depois no botão \*\[Executar\]\* para iniciar o processo de criação da Integração entre os sistemas.

Os scripts abaixo serão executados com sucesso, confirmando a criação da integração, parâmetros, tabelas e entidades.

**Sql Server**

• SQL.00\_PARAMETROS\_GERAL

• SQL.01\_DEFAULT

• SQL.02\_HCTRANSFORMACAO

• SQL.03\_HCINTEGRACAOID\_HCPARAMETROS

• SQL.04.1\_SOURCECODE

• SQL.04.2\_SOURCECODE\_FinancialNature

• SQL.0401\_SOURCECODE\_ORDER

• SQL.00\_COLIGADA

• SQL.01\_SOURCECODE

• SQL.02\_PACOTEPADRAO

• SQL.03\_PARAMETROS

**Oracle**

• Oracle.00\_PARAMETROS\_GERAL

• Oracle.01\_DEFAULT

• Oracle.02\_HCTRANSFORMACAO

• Oracle.03\_HCINTEGRACAOID\_HCPARAMETROS

• Oracle.04.1\_SOURCECODE

• Oracle.04.1\_SOURCECODE\_CustomerVendor

• Oracle.04.1\_SOURCECODE\_Item2001

• Oracle.04.2\_SOURCECODE\_FinancialNature

• Oracle.0401\_SOURCECODE\_ORDER

• Oracle.00\_COLIGADA • Oracle.01\_SOURCECODE • Oracle.03\_PARAMETROS

**Tabelas criadas**

• HCFILAEXECUCAO

• HCFILAINTEGRACAO

• HCFILAMENSAGEM

• HCINTEGRACAO

• HCINTEGRACAOID

• HCPARAMETROS

• HCTRANSFORMACAO

• HCFILAEXECUCAO

• HCFILAINTEGRACAO

**Entidades criadas**

8- Para acessar o cadastro das entidades pertencentes a integração, acesse: Integração/ Integração/ Mensagem Única/ Integrações

9- Selecione o cadastro da integração e acesse: Anexos/ Mapeamento de Entidades

• ACCOUNTPAYABLEDOCUMENTDISCHARGE

• ACCOUNTRECEIVABLEDOCUMENTDISCHARGE

• BANK

• BRANCH

• COSTCENTER

• CUSTOMERVENDOR

• FINANCIALNATURE

• FINANCING

• ORDER

• REVERSALOFACCOUNTPAYABLEDOCUMENTDISCHARGE

• REVERSALOFACCOUNTRECEIVABLEDOCUMENTDISCHARGE

• UPDATECONTRACTPARCEL

• UPDATECONTRACTSTATUSPARCEL
