---
article_id: 4402769734295
category: NFe - Nota Fiscal Eletrônica
content_hash: a8010be5cdbb79a88d32ffc7d8eda1a817ce5c8e4ffa9974b87993e547650c40
fetched_at: '2026-06-28T22:40:05.694725+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como exportar o
  xml de inutilização no layout procInutNFe
type: support-article
updated_at: '2021-06-16T21:05:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402769734295-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-exportar-o-xml-de-inutiliza%C3%A7%C3%A3o-no-layout-procInutNFe
---

**Dúvida**Como exportar o xml de inutilização no layout procInutNFe?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.17  
Cross Segmentos - TSS - a partir da versão 12

**Solução**Para que seja exportado o xml de inutilização no modelo de schema procInutNFe, foi criado um parâmetro para que seja possível exportar tanto neste modelo, como da maneira antiga (xml's de envio e retorno separadamente), de acordo com a configuração do parâmetro **MV\_AGLEXP**.

**Passo a passo:**

**1.** Criando o parâmetro:  
**a)** Acessar o módulo **SIGACFG.****b)** Acessar o caminho **Base de Dados** \ **Dicionário** \ **Base de Dados** ou **Ambiente** \ **Cadastros** \ **Parâmetros**.

Vamos utilizar o caminho **Ambiente** \ **Cadastros** \ **Parâmetros**.

![](https://tdn.totvs.com/download/attachments/558252766/image2020-8-10_10-49-48.png?version=1&modificationDate=1597179958203&api=v2)

**c)** Selecionar **Parâmetros** e em seguida acesse **Incluir**.

![](https://tdn.totvs.com/download/attachments/558252766/image2020-8-10_10-51-57.png?version=1&modificationDate=1597179958173&api=v2)

**d)** Informar os dados da criação do parâmetro.  
Na aba **Informações**, para os campos:  
**Filial:** pode ser específico por filial ou em branco.  
**Nome da Var.:** nome do parâmetro: **MV\_AGLEXP**.  
**Tipo:**deve ser **Numérico**.  
**Cont. Por**: 1  
**Cont. Ing**: 1  
**Cont. Esp**: 1

![](https://tdn.totvs.com/download/attachments/558252766/image2020-8-11_17-50-47.png?version=1&modificationDate=1597179958147&api=v2)

**e)** Na aba **Descrição**, para os campos:  
**Descrição**: Descrição do parâmetro,   
**Cont. Descriç**: continuação da descrição, caso necessário.  
**Cont. Descriç**: continuação da descrição, caso necessário.  
Caso necessário, informar a descrição em outros idiomas, possuem os mesmos campos para inglês e espanhol.

![](https://tdn.totvs.com/download/attachments/558252766/image2020-8-11_17-55-25.png?version=1&modificationDate=1597179958120&api=v2)

**2.** Exportando o xml:  
**a)** Acesse a rotina **SPEDNFE**.  
**b)** Vá em **Outras Ações > Exportar.  
c)** Preencher os campos com as informações da nota e informar o caminho em que o xml será salvo, em seguida acione **Ok**.  
  
![](https://tdn.totvs.com/download/attachments/558252766/image2020-8-11_18-3-34.png?version=1&modificationDate=1597179958063&api=v2)  
  
d) O xml gerado deverá estar na estrutura conforme abaixo, contendo no mesmo arquivo, o xml enviado para a Sefaz e o xml retornado pela mesma:  
Parte do xml que contém o envio:  
![](https://tdn.totvs.com/download/attachments/558252766/image2020-8-11_18-4-40.png?version=1&modificationDate=1597179958033&api=v2)  
  
Parte do xml que contém o retorno:  
![](https://tdn.totvs.com/download/attachments/558252766/image2020-8-11_18-5-23.png?version=1&modificationDate=1597179957963&api=v2)
