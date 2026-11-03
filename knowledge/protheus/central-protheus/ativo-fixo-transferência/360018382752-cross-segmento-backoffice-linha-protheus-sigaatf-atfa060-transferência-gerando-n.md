---
article_id: 360018382752
category: Ativo Fixo - Transferência
content_hash: fa8c028bf8104497262e84f7f5a7a708c05297cec6903f489cf651b0b1ee9af3
fetched_at: '2026-06-28T22:41:52.238749+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF -ATFA060:  Transferência
  gerando nota Fiscal (aba Nota FISCAL FN9_GERNF = SIM)'
type: support-article
updated_at: '2022-05-18T17:52:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018382752-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Transfer%C3%AAncia-gerando-nota-Fiscal-aba-Nota-FISCAL-FN9-GERNF-SIM
---

**Dúvida**Transferência gerando nota Fiscal (aba Nota FISCAL FN9\_GERNF = SIM)

**Ambiente**Protheus – Ativo Fixo – A partir da versão 11.80  
  
  
**Solução**

**Premissas:**

* Para transferência do bem com emissão de nota fiscal é necessário, além do preenchimento padrão, preencher as seguintes informações:
  + Fornecedor;
  + Número da Nota Fiscal;
  + Série;
  + Produto vinculado.

**Observação:**O bem pode ser incluso a partir do cadastrado de **Documentos de Entrada (MATA103**) ou manualmente pela rotina de **Ativos (ATFA012).**

* **Cadastro de Produto (MATA010)**   
  **Importante:** Se a tabela de **Produtos (SB1)** estiver exclusiva, deve-se cadastrar os dados em ambas as filiais.  
  ![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-10-8.png?version=1&modificationDate=1537996208790&api=v2)

* **Cadastro de TES (MATA080)**   
   No TES de Entrada/Saída utilizado para transferência, além dos campos padrões, também é necessário preencher os campos abaixo:   
  + Gera Dupl. (**F4\_DUPLIC**) = NÃO
  + Atual.Ativo (**F4\_ATUATF**) = NÃO
  + Atu.Estoque (**F4\_ESTOQUE**) = NÃO

**Importante:** Se a tabela**Tipos de Entrada e Saída (SF4)** estiver exclusiva, deve-se cadastrar os dados em ambas as filiais.

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-12-15.png?version=1&modificationDate=1537996335727&api=v2)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-13-27.png?version=1&modificationDate=1537996407863&api=v2)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-19-25.png?version=1&modificationDate=1537996766157&api=v2)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-19-40.png?version=1&modificationDate=1537996780493&api=v2)

**Parâmetro**: A transferência somente será efetuada com data superior à data contida no parâmetro**MV\_ULTDEPR**.  **Importante:** Verificar o parâmetro nas filiais de **ORIGEM** e **DESTINO**.  
![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-21-19.png?version=1&modificationDate=1537996879780&api=v2)  
  
**Atenção**: Caso o cadastro de Cliente/Fornecedor não esteja correto, o sistema apresentará mensagens de alerta conforme abaixo:

* A filial de **DESTINO** não está cadastrada como cliente na filial de **ORIGEM**. Efetue o cadastro utilizando o CNPJ da filial de **DESTINO**;
* A filial de **ORIGEM** não está cadastrada como fornecedor na filial de **DESTINO**. Efetue o cadastro utilizando o CNPJ da filial de **ORIGEM**.

Neste caso, corrija o cadastro indicado na mensagem conforme a solução apresentada.

* Para verificação do CNPJ das filiais de **ORIGEM** e **DESTINO**, acesse o módulo **Configurador (SIGACFG)**:  
  Ambiente → Empresas → Filial  
    
  **D MG 01** - Filial Belo Horizonte (filial de **ORIGEM**)   
  ![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-26-51.png?version=1&modificationDate=1537997211490&api=v2)  
    
  **D MG 02** - Filial Uberaba (filial de **DESTINO**)  
  ![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-8-59.png?version=1&modificationDate=1538046539563&api=v2)
* A filial de **DESTINO** não está cadastrada como cliente na filial de **ORIGEM**. Efetue o cadastro utilizando o CNPJ da filial de **DESTINO**.  
  Acessar a rotina **Clientes (MATA030)** na filial de **ORIGEM** e efetuar o cadastrado com CNPJ da filial de **DESTINO**:  
  ![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-29-35.png?version=1&modificationDate=1537997375797&api=v2)

* A filial de **ORIGEM** não está cadastrada como fornecedor na filial de **DESTINO**. Efetue o cadastro utilizando o CNPJ da filial de **ORIGEM**.  
  Acessar a rotina**Fornecedores (MATA020)** na filial de **DESTINO**e efetue o cadastrado  com o CNPJ da filial de **ORIGEM**:  
  ![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-26_18-30-22.png?version=1&modificationDate=1537997422393&api=v2)

**LEMBRE-SE :**

* Os campos informados abaixo devem estar, obrigatoriamente, preenchidos no bem que será transferido.
* A inclusão do Bem pode ser realizada a partir da rotina de**Documentos de Entrada (MATA103)** ou por inclusão manual via rotina de **Ativos (ATFA012).**  
    
  Na aba **Dados do Bem** , preencher os campos:
  + Nota Fiscal (**N1\_NFISCAL**);
  + Serie N.F. (**N1\_SERIE**);
  + Cod. Fornec. (**N1\_FORNEC**);
  + Loja (**N1\_LOJA**).  
  Na aba **Dados Complementares**, preencher o campo:   
  + Cód Produto (**N1\_PRODUTO**)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_9-6-1.png?version=1&modificationDate=1538049961480&api=v2)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-11-39.png?version=1&modificationDate=1538046700277&api=v2)

* **Transferências (ATFA060**)

Botão Transferir→ Preencher os parâmetros:

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-45-21.png?version=1&modificationDate=1538048721283&api=v2)

Informar a filial **DESTINO**no campo Filial Dest. (**FN9\_FILDES**).   
Neste exemplo será preenchido com a filial **D MG 02**.

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-50-11.png?version=1&modificationDate=1538049011317&api=v2)

Informar a quantidade a ser transferida no campo Quant. Dest. (**FN9\_QTDDES**). Este campo permite informar a quantidade total ou parcial.  
Neste exemplo será transferida a quantidade total (quantidade = 1).

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-55-31.png?version=1&modificationDate=1538049331753&api=v2)

* Na aba **Nota Fiscal**preencher os campos abaixo:
  + Gera NF (**FN9\_GERNF**) = SIM;
  + Serie (**FN9\_SERIE**) = Informar a Série;
  + Class NF (**FN9\_CLSNF**) = Informar 1- A Classificar ou 2- Classificada (A classificar deve posteriormente classificar a nota);
  + TES Saída (**FN9\_TESSAI**) = Informar o TES de saída;
  + TES Entrada (**FN9\_TESENT**) = Informar o TES de entrada;
  + Valor da NF (**FN9\_VALNF**) = Informar o valor da nota.

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-56-47.png?version=1&modificationDate=1538049407277&api=v2)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_9-2-29.png?version=1&modificationDate=1538049750147&api=v2)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_9-3-37.png?version=1&modificationDate=1538049817697&api=v2)

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-5-38.png?version=1&modificationDate=1538046339087&api=v2)

**Importante :** O processo de transferência atualiza as seguintes tabelas do Ativo Fixo:

* **FNR - Ativos Transferidos;**
* **FNS - Tipos de Saldo Transferidos;**
* **SN1 - Ativo Imobilizado;**
* **SN3 - Saldos e Valores;**
* **SN4 - Movimentações do Ativo Fixo.**

* Filial de **ORIGEM** (**D MG 01**): Alimenta as tabelas de Notas Fiscais de Saída:
  + **SF2 - Cabeçalho das NF de Saída**;
  + **SD2 - Itens de Venda da NF**.

Acessar o módulo Faturamento → Consulta → Cadastro → **Consulta de Notas Fiscais de Saída (MATC090).**

**![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_8-0-19.png?version=1&modificationDate=1538046019867&api=v2)**

* Filial de **DESTINO** (**D MG 02** ): Alimenta as tabelas Notas Fiscais de Entrada:
  + **SF1 - Tabelas Cabeçalho das NF de Entrada;**
  + **SD1 - Itens das NF de Entrada.**

Acessar o módulo Compras → Atualizações → Movimentos → Nota Fiscal → **Documento de Entrada (MATA103).**

![](http://tdn.totvs.com/download/attachments/416848333/image2018-9-27_7-53-37.png?version=1&modificationDate=1538045618097&api=v2)

Link TDN

[Transferência gerando nota Fiscal (aba Nota FISCAL FN9\_GERNF = SIM)](https://tdn.totvs.com/pages/viewpage.action?pageId=416848333)
