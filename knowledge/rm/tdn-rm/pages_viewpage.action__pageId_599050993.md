---
content_hash: 7cd13bc6ebb2b2d9165d19f457ab25a0ea08717a85fcede324a44f3b7a6cee09
fetched_at: '2026-06-29T00:10:57.640018+00:00'
page_id: '599050993'
product: rm
source: tdn-rm
title: Nota Técnica 2020.006
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=599050993
version: 21
---

A Nota Técnica 2020.006 divulga novos campos e regras de validação para a NF-e e NFC-e, visando a adequação ao disposto no Ajuste SINIEF 21/202 e 22/2020, envolvendo a identificação do intermediador ou agenciador da operação.

falseVersoes1100VERSAO 1.10

## Cronograma

Este evento entra em vigor:

* Homologação a partir de 01/02/2021
* Produção a partir de 05/04/2021.

## Legislação

Este documento foi elaborado com base na [Nota Técnica 2020.006 - v.1.10](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s= "Follow link") disponível no portal da NF-e.

### Tela de aviso

Será exibida uma tela de aviso sobre a mudança da NT2020.006, essa tela de aviso será exibida somente no dia 05/04/2021 de 00:00 até 13:00.   
Caso no período de intermitência o usuário queira utilizar a nova NT, ele deve clicar em SIM e o XML será gerado com a tag do Intermediador, caso clique em Não a tag não será gerada.

**Importante:** Não é possível desativar esse aviso, o mesmo não será mais exibido após às 13:00 do dia  .

## Implementações:

false

### Parametrização:

**Módulo: TOTVS Gestão de Estoque, Compras a Faturamento**

**Cadastro de Intermediador:** Cadastros | Estoque, Compras e Faturamento | Mais | Tabelas Auxiliares | Intermediador 

**Grupo B:** Foi acrescentado novo campo (**indIntermed**) correspondente ao Indicador de Intermediador/Marketplace 

Imagem

**Grupo YB:** Corresponde ao Grupo de Informações do Intermediador da Transação (**infIntermed**) 

ImagemfalseRegras no Movimento

**Para as Operações:**

**2** = Operação não presencial, pela Internet;  
**3** = Operação não presencial, Tele atendimento;  
**4** = NFC-e em operação com entrega a domicílio;  
**9** = Operação não presencial, outros.

* Se Informado indicativo de presença (TAG: **indPres**) ***IGUAL**a**:* **2, 3, 4** ou **9**
  + Obrigatório o preenchimento do campo indicativo do **Intermediador** (TAG: **indIntermed**).

* Se Informado indicativo de presença (TAG: **indPres**) ***DIFERENTE** de:* **2, 3, 4** ou **9**
  + Proibido o preenchimento do campo Indicativo do **Intermediador** (TAG: **indIntermed**).

Obs.: [Identificador do Intermediador](https://tdn.totvs.com/x/SABcIw)

falseRegras no Envio da NF-e

* Se informado indicador do **Intermediador** ***IGUAL*** a **1 - Operação em site ou plataforma de terceiros (intermediadores/marketplace)**
  1. TAG **indIntermed** do XML será igual a **1** (Um)
  2. Obrigatório o preenchimento das informações do Intermediador da Transação (TAG: **infIntermed**)

* Se informado indicador de presença do comprador no estabelecimento comercial no momento da operação ***DIFERENTE*** de **1 - Operação em site ou plataforma de terceiros (intermediadores/marketplace)**
  1. TAG **indIntermed do XML**será diferente de **1** (Um)
  2. Não é permitido o preenchimento das Informações do Intermediador da Transação (TAG: **infIntermed**)
falseNovos Meios de Pagamento

Grupo YA. Informações de Pagamento

Criação dos Novos Meios de Pagamento

16=Depósito Bancário  
17=Pagamento Instantâneo (PIX)  
18=Transferência bancária, Carteira Digital  
19=Programa de fidelidade, Cashback, Crédito Virtual

Obs.: 

Notas

 - Caso esteja com a opção desabilitada basta dar permissão de acesso ao menu para seu usuário.

 - [Grupo B](https://tdn.totvs.com/x/TakBGQ)

 - [Grupo YB](https://tdn.totvs.com/x/ZRy9Gg)

Atenção

Disponível a partir da biblioteca **12.1.28**

Base de dados deverá estar atualizada devido as novas marcações TMOV.IDINTERMEDIADOR  e TINTERMEDIADOR

1201VERSAO 1.20

## Cronograma

Este evento entra em vigor:

* Homologação a partir de 03/05/2021.
* Produção a partir de 01/09/2021.

## Legislação

Este documento foi elaborado com base na [Nota Técnica 2020.006 - v.1.20](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=) disponível no portal da NF-e.

## Patches

Os ajustes estão disponíveis a partir dos patches:

12.1.29.300  
12.1.31.218  
12.1.32.154

falseRegras de Validação

#### **Ajustes**:

Para os **meios de pagamento** parametrizados com um **tipo primitivo** que faça referência a 99 = Outros, a TAG **<<xPag>>** será preenchida com o conteúdo do campo **descrição** do meio de pagamento.

[Clique aqui](https://tdn.totvs.com/display/LRM/Meio+Pagamento), para consultar o **De/Para** entre o **tipo primitivo** do ERP com o tipo de meio de pagamento da TAG **xPag.**

#### **Ajustes**:

* Clientes que usam meio de pagamento
  + Os tipos de meio de pagamento informados na TAG <<**tPag**>> vão respeitar os meios de pagamentos informados no movimento.

* Clientes que usam condição de pagamento
  + Criado no cadastro de [condição de pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=423938175), um campo para informar o meio de pagamento default que será utilizado para preenchimento da TAG <<**tPag**>> e da tag <<**xPag**>>, dependendo do tipo primitivo cadastrado.

    Atenção

    Para que o campo fique disponível no cadastro é necessário exectuar o atualizador na base de dados.
