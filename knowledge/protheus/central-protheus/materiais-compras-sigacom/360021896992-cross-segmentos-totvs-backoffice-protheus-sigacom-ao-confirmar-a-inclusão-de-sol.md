---
article_id: 360021896992
category: Materiais - Compras (SIGACOM)
content_hash: 551c13bfe24c591af6fb0a0c08f321cb461e86ce2704cf7778c1b16a04e70d35
fetched_at: '2026-06-28T22:41:07.425698+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao confirmar a inclusão
  de Solicitação de Compras, Pedido de Compra ou Documento de Entrada ocorre o Help
  REGNOIS no alias NNR
type: support-article
updated_at: '2026-05-26T14:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021896992-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-confirmar-a-inclus%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-Compras-Pedido-de-Compra-ou-Documento-de-Entrada-ocorre-o-Help-REGNOIS-no-alias-NNR
---

**Ocorrência**  
Ao finalizar a inclusão do documento (inclusão de Solicitação de Compras, Pedido de Compra ou Documento de Entrada) o sistema exibe a mensagem de **HELP: REGNOIS no alias NNR**  
Problema: Não existe registro relacionado a esse código.

Porém a mensagem não informa qual campo não está de acordo com os registros.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406587501591)

**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17

**Causa**  
Esta mensagem ocorre quando no cadastro do produto utilizado existe vinculado um código de armazém padrão que não existe cadastrado na tabela **NNR (Locais de Estoque - AGRA045.PRW)** para a Filial em questão.

Exemplo1:

* Armazem criado na filial 01
* Vincula ao produto que é compartilhado
* Ao realizar o teste com pedido na filial 02, ocorrerá o HELP porque esse armazem não existe na filial 02

Exemplo 2:

* Cadastro de Produto incluido através de uma importação de registros de um sistema legado, com o campo de "Armazém Padrão" já gravado no registro importado.
* E este armazém que já veio com o produto não existe cadastrado para a Filial que está sendo incluido o documento ocorrendo assim o Help.

**Solução**  
Para solucionar essa ocorrência, podem-se realizar os seguintes passos:

*Solução 1:*

1. Ao inserir uma linha com o produto direcionar o cursor até o carpo Armazém;
2. Pressionar a tecla F3 e escolher um armazém existente no cadastro.

*Solução 2:*

1. Acessar a rotina de Locais de Estoque (AGRA045.PRW) na filial que se está incluindo o documento.
2. Cadastrar para esta filial que se está incuindo o document, o Armazém que está vinculado ao Produto em questão em seu no "Armazém Padrão".

***Obs:***

Nos casos de outros processos que envolvam a geração automática de Pedido de Compras, é possível acessar o sistema pela filial onde a mensagem ocorre e realizar o cadastro do código de armazém informado no produto para a respectiva filial (Solução 2).

***Saiba Mais***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
