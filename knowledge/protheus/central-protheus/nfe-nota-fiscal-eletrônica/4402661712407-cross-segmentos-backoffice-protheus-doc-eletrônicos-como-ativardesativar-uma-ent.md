---
article_id: 4402661712407
category: NFe - Nota Fiscal Eletrônica
content_hash: 627745d4e809c87ce7c20777381d856f76c9c52a5159d8dddd032cd06707eeda
fetched_at: '2026-06-28T22:40:05.629878+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como ativar/desativar
  uma entidade do TSS, a partir do Protheus
type: support-article
updated_at: '2021-06-14T22:11:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402661712407-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-ativar-desativar-uma-entidade-do-TSS-a-partir-do-Protheus
---

**Dúvida**Como ativar/desativar uma entidade do TSS, a partir do Protheus?

**Ambiente**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.17  
Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1.** Criando o parâmetro:  
**a)** Acessar o módulo **SIGACFG;****b)** Acessar o caminho **Base de Dados**\ **Dicionário** \**Base de Dados** ou **Ambiente**\ **Cadastros**\ **Parâmetros**.

No exemplo a seguir, vamos utilizar o caminho **Ambiente** \ **Cadastros** \ **Parâmetros**.![](https://tdn.engpro.totvs.com.br/download/attachments/560647309/image2020-8-10_10-49-48.png?version=1&modificationDate=1598300472597&api=v2)

**c)** Selecionar **Parâmetros** e em seguida, acesse a opção **Incluir**.![](https://tdn.engpro.totvs.com.br/download/attachments/560647309/image2020-8-10_10-51-57.png?version=1&modificationDate=1598300472567&api=v2)

**d)** Informando os dados para a criação do parâmetro. Na aba **Informações**, preencha o os campos com:  
**-Filial:** pode ser específico por filial ou em branco.  
**-Nome da Var.:** nome do parâmetro **MV\_SPEDENT**.  
**-Tipo:** deve ser **Caractere**.  
**-Cont. Por**: S  
**-Cont. Ing**: S  
**-Cont. Esp**: S

![](https://tdn.engpro.totvs.com.br/download/attachments/560647309/image2020-8-24_17-10-47.png?version=1&modificationDate=1598300472363&api=v2)

**e)** Na aba **Descrição**, preencha os campos:  
**Descrição**: Descrição do parâmetro.  
**Cont. Descriç**: continuação da descrição, caso necessário.  
**Cont. Descriç**: continuação da descrição, caso necessário.  
  
Se necessário, informar a descrição em outros idiomas, possuem os mesmos campos para inglês e espanhol.

![](https://tdn.engpro.totvs.com.br/download/attachments/560647309/image2020-8-24_17-12-5.png?version=1&modificationDate=1598300472323&api=v2)

Quando a entidade estiver configurada como ativa, o acesso à rotina SPEDNFE ocorrerá normalmente. Caso esteja configurada com desativada, será exibida a seguinte mensagem ao tentar acessar a rotina:![](https://tdn.engpro.totvs.com.br/download/attachments/560647309/image2020-8-24_17-17-57.png?version=1&modificationDate=1598300472220&api=v2)
