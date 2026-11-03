---
content_hash: bae3fcf86c3c1281a7191371c4614665becb4cbe42ea80ceb424733a03ce3a2e
fetched_at: '2026-06-29T00:09:17.402204+00:00'
page_id: '421388581'
product: rm
source: tdn-rm
title: Importação extrato bancário - Formato CNAB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388581
version: 3
---

Antes de realizar o processo de Reconciliação Bancária você deve preencher as informações do Layout de Reconciliação. Para que os campos sejam preenchidos corretamente verifique o manual para Conciliação Bancária, fornecido pelo banco. Através das informações deste layout, o sistema buscará no arquivo bancário, os dados necessários para a realização da Reconciliação. Para os bancos que utilizam o padrão Febraban (Federação Brasileira das Associações de Bancos) 240 posições, não é necessário o preenchimento deste layout.

**Atenção:**

Para os bancos:  
Banco do Brasil S.A. – 001  
Banco Bradesco S.A. – 237  
Banco do Nordeste do Brasil S.A. – 004

Não é necessário o preenchimento do layout de Reconciliação, o layout para estes bancos já foi cadastrado internamente no sistema. Caso o layout seja preenchido, o sistema respeitará este layout e não o layout interno.

Posição do Número do Banco:  
Informe a posição inicial onde é informado o Código do Banco. O código será buscado da linha Header do arquivo.

Código do Registro Tipo Header:   
Informe em qual posição ficam armazenados os códigos de registro acima especificados (Header, Detalhe e Trailer).

Código do Registro Tipo Detalhe:  
Informe o código que determina que a linha é do tipo Detalhe.

Código do Registro Tipo Trailer:  
Informe o código que determina que a linha é do tipo Trailer.

Posição do Tipo de Registro:  
Informe a coluna onde ficam armazenados os códigos de registro acima especificados (Header, Detalhe e Trailer)

Código do Tipo de Inscrição CNPJ:  
Informe o código que identifica o tipo de inscrição CNPJ.

Código do Tipo de Inscrição CPF:  
Informe o código que identifica o tipo de inscrição CPF.

Posição do Tipo de Inscrição:  
Informe em qual posição fica armazenado o código que identifica o tipo de inscrição (CNPJ e CPF).

Número de Inscrição:  
Informe a posição inicial e final de onde fica armazenado á inscrição (CNPJ ou CPF).

Número da Agência:  
Informe a posição inicial e final de onde fica armazenado o código da agência.

Conta Corrente:  
Informe a posição inicial e final de onde fica armazenado á conta corrente.

Dígito Verificador:  
Informe a posição inicial e final de onde fica armazenado o dígito verificador da conta corrente.

Código do Saldo Débito:  
Informe o código que identifica que a situação do saldo da conta corrente é débito.

Exemplo: Devedor = D

Código do Saldo Crédito:  
Informe o código que identifica que a situação do saldo da conta corrente é crédito.

Exemplo: Credor = C

Posição do Tipo de Registro Detalhe:  
Informe a posição de onde fica armazenado o código que identifica o tipo de registro "detalhe" (Lançamentos).

Código do Registro do Saldo Anterior:  
Informe o código do registro onde fica armazenado o saldo anterior (ou saldo inicial).  
Este é o saldo da conta corrente antes dos lançamentos serem efetuados.

Exemplo:

O Saldo Anterior (ou saldo inicial) está armazenado no "registro header do lote", e o código deste registro é "1".  
Você deve informar "1".

Data do Saldo Anterior:  
Informe a posição inicial e final de onde está armazenada a data do saldo anterior (ou saldo inicial).

Estado do Saldo Anterior:  
Informe a posição de onde fica armazenado o estado (ou situação) do saldo anterior (credor ou devedor).

Valor do Saldo Anterior:  
Informe a posição inicial e final de onde fica armazenado o valor do saldo anterior (ou saldo inicial).

Código do Registro de Lançamento:  
Informe o código do registro onde ficam armazenados os dados do lançamento.

Categoria do Lançamento:  
Informe a posição inicial e final de onde fica armazenado o código da categoria do lançamento.

Exemplo:

Existem categorias para identificar um lançamento de "débito" e um de "crédito":

Débitos:  
101 – Cheques  
105 – Tarifas  
109 – CPMF  
112 – Pagamento Fornecedor

Créditos:  
201 – Depósitos  
202 – Líquido de Cobrança  
209 – DOC Recebido  
206 – Resgate de Aplicação

Data do Lançamento:  
Informe a posição inicial e final de onde fica armazenada a data do lançamento.  
Esta é a data em que o lançamento foi efetuado no banco.

Valor do Lançamento:  
Informe a posição inicial e final de onde fica armazenado o valor do lançamento.  
Este é o valor que foi efetuado no banco.

Histórico do Lançamento:  
Informe a posição inicial e final de onde fica armazenada a descrição do histórico do lançamento.

Documento Lançamento:  
Informe a posição inicial e final de onde fica armazenado o número do documento do lançamento.

Código do Registro do Saldo Atual:  
Informe o código do registro onde fica armazenado o saldo Atual (ou saldo final).  
Este é o saldo da conta corrente após os lançamentos serem efetuados.

Exemplo:

O Saldo Atual (ou saldo final) está armazenado no "registro trailer de lote", e o código deste registro é "5".  
Você deve informar "5".

Data do Saldo Atual:  
Informe a posição inicial e final de onde está armazenada a data do saldo atual (ou saldo final).

Estado do Saldo Atual:  
Informe a posição de onde fica armazenado o estado (ou situação) do saldo atual (credor ou devedor).

Valor do Saldo Atual:  
Informe a posição inicial e final de onde fica armazenado o valor do saldo atual (ou saldo final).

**Códigos de Categoria do Lançamento:**

**Débito**  
Informe os códigos válidos do banco para representar a categoria de débito do lançamento.  
Esses códigos estão disponíveis no manual de Conciliação Bancária do banco.  
Na importação do arquivo bancário, o sistema lê o código da categoria, armazenado na posição específica e compara com as informações cadastradas nesse campo.  
Exemplo:

O código de categoria que indica "CPMF", de acordo com o manual do banco, é 109 e o código de categoria que indica "Pagamento Fornecedor", é 112.  
Você informa no campo:  
109112.  
Na importação, o sistema identifica que os lançamentos que possuem o código "109", são lançamentos de "CPMF".

**Crédito**  
Informe os códigos válidos do banco para representar a categoria de crédito do lançamento.  
Esses códigos estão disponíveis no manual de Conciliação Bancária do banco.  
Na importação do arquivo bancário, o sistema lê o código da categoria, armazenado na posição específica e compara com as informações cadastradas nesse campo.

Exemplo:

O código de categoria que indica "Depósitos", de acordo com o manual do banco, é 201 e o código de categoria que indica "DOC Recebido", é 209.  
Você informa no campo:  
201209  
Na importação, o sistema identifica que os lançamentos que possuem o código "201", são lançamentos de "Depósito".

**Observação:**

Para os bancos que utilizam o padrão FEBRABAN já estão cadastrados internamente no sistema os seguintes códigos:

Débito: códigos 101 até 122  
Crédito: códigos 201 até 216
