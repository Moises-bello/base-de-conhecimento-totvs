---
article_id: 360058814693
category: NFe - Nota Fiscal Eletrônica
content_hash: 937ea46c1f8398cd678786f51a394d7e3449a2000e34e9ec4c77ba47fb62ef5c
fetched_at: '2026-06-28T22:40:06.775864+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como habilitar a
  referencia tag <NFref> de uma Nota Fiscal Eletrônica emitida anteriormente de outro
  cliente para nota do tipo normal (N)
type: support-article
updated_at: '2024-07-29T21:01:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058814693-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-habilitar-a-referencia-tag-NFref-de-uma-Nota-Fiscal-Eletr%C3%B4nica-emitida-anteriormente-de-outro-cliente-para-nota-do-tipo-normal-N
---

**Dúvida**

Como habilitar a referencia tag<NFref>de uma Nota Fiscal Eletrônica emitida anteriormente de outro cliente para nota do tipo normal (N) ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Para implementar segue o link da **documentação abaixo:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=562482672>

O parâmetro MV\_VINCNF tem o objetivo de habilitar a possibilidade de referenciar uma Nota Fiscal Eletrônica emitida anteriormente de outro cliente para nota do tipo normal (N) 

O preenchimento do parâmetro MV\_VINCNF funciona das seguintes formas:

* Por padrão MV\_VINCNF ele vem desabilitado(.F.);
* Para habilitar a possibilidade de referenciar uma Nota Fiscal Eletrônica emitida anteriormente de outro cliente para nota do tipo normal(N), altere o parâmetro MV\_VINCNF = .T..

***Aviso: Caso não exista o parâmetro a rotina considera como desabilitado.***

03. CRIAÇÃO DO PARÂMETRO:

**1.** Criando o parâmetro.

**a)**Acessar o módulo**SIGACFG;**

**b)** Acessar a rotina **Base de Dados** \ **Dicionário** \ **Base de**

**Dados** ou **Ambiente** \ **Cadastros** \ **Parâmetros;**

Vamos utilizar a rotina **Ambiente** \ **Cadastros** \ **Parâmetros**.

![](https://tdn.totvs.com/download/attachments/562482672/image2020-8-10_10-49-48.png?version=1&modificationDate=1599847837020&api=v2)

**c)** Selecionar **Parâmetros**, e em seguida, clicar na opção **Incluir**.

![](https://tdn.totvs.com/download/attachments/562482672/image2020-8-10_10-51-57.png?version=1&modificationDate=1599847837163&api=v2)

**d)** Informar os dados da criação do parâmetro.

Na aba **Informações**, para os campos:

**Filial:** pode ser específico por filial ou em branco (genérico para todas as filiais).

**Nome da Var.:** nome do parâmetro: **MV\_VINCNF**.

**Tipo:**deve ser **Logico**.

**Cont. Por**: Preencher conforme orientações do tópico 

**Cont. Ing**:

**Cont. Esp**:

![](https://tdn.totvs.com/download/attachments/562482672/image2020-9-11_15-32-19.png?version=1&modificationDate=1599849140063&api=v2)

**e)** Na aba **Descrição**, para os campos:

**Descrição**: .T. Habilitar a referencia de uma Nota Fiscal

**Cont. Descriç**: Eletrônica emitida anteriormente de outro cliente

**Cont. Descriç**: para nfe do tipo normal (N)

Caso necessário, informar a descrição em outros idiomas, possuem os mesmos campos para inglês e espanhol.

![](https://tdn.totvs.com/download/attachments/562482672/image2020-9-11_15-33-24.png?version=1&modificationDate=1599849205387&api=v2)

Obs: Quando estiver fazendo o documento do tipo N precisa informar os 3 campos **NF Ori, Serie Ori e Item NF. Ori** na linha do item para vincular a nota de origem a qual deseja que vincule a chave na tag **refnfe.**
