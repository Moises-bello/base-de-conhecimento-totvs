---
content_hash: 799a2c2effa1108ccce0f01770316715659641eef59abec2a0bc1f1ee3fae571
fetched_at: '2026-06-29T00:06:15.514775+00:00'
page_id: '211058859'
product: rm
source: tdn-rm
title: ER_PCREQ-7809_Administradora Financeira / Forma de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=211058859
version: 143
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Faturamento |
| **Segmento Executor** | TOTVS Construção e Projetos | | |
| **Projeto1** | Integração BackOffice RM x PDV Protheus | **IRM1** | PCREQ-7769 |
| **Requisito1** | PCREQ-7809 | **Subtarefa1** | PDR\_CP\_MOV008-54 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Implementação do adapter de integração via Mensagem Única TOTVS do cadastro de Forma de Pagamento viabilizando assim o CRUD completo do cadastro por envio de mensagem de integração no padrão de Mensageria Única TOTVS.

## Definição da Regra de Negócio

Considera-se como escopo deste requisito a implementação do adapter de envio de Mensagens Únicas TOTVS para integração do cadastro de Forma de Pagamento, estando o adapter de recebimento desta mesma mensagem fora do escopo do requisito, ou seja , o cadastro de Forma de Pagamento será realizado somente no BackOffice RM.

A análise e o desenvolvimento do adapter será efetuado considerando a integração do BackOffice RM com PDV Protheus, mas também viabilizará a integração com outros destinatários desde que respeitado o layout da mensagem e os campos especificado para envio. 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Meio Pagamento | Inclusão \ Alteração \ Exclusão | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \  Mais \ Tabelas Auxiliares \ Meio Pagamento | - |

### **Tabelas Utilizadas**

* TFORMAPAGTO – Meio de Pagamento

**Entidades de Integração**

* DataServer de Gatilho
  + MovFormaPagtoData
* Transformação
  + Id: PAYMENTMETHOD
  + Versão: 1.000
* SourceCode (Evento)
  + GUID: ac6342d3-d879-4d02-9654-7bcbed6ae0eb
  + Nome: PaymentMethod\_1\_000

**Regras de Integridade**

**Integridade de registros entre RM e Protheus**

Visto que a base Protheus possui carga com formas de pagamento padrão (obrigatoriamente constam na base de dados), deve-se efetuar o cadastro destas Formas de Pagamento no RM respeitando o mesmo código do Protheus para viabilizar a integração de registros que utilizem estas como parâmetro. A lista de forma de pagamentos padrão no Protheus (até a presente data) e devem ser cadastradas no RM com o mesmo código de descrição são:

| Código | Descrição |
| --- | --- |
| BOL | BOLETO BANCARIO |
| CC | CARTAO DE CREDITO |
| CD | CARTAO DE DEBITO AUTOMATICO |
| CH | CHEQUE |
| CO | CONVENIO |
| CR | CREDITO |
| DC | DEBITO EM CONTA CORRENTE |
| FI | FINANCIADO |
| FID | FIDELIDADE |
| R$ | DINHEIRO CX |
| VA | VALES |
| VP | VALE PRESENTE |

**Obs.: Caso hajam outras formas de pagamento já cadastradas no Protheus as mesmas também deverão ser incluídas no BackOffice RM com mesmos códigos.**

****Compartilhamento de registros por Coligada e Filial****

Visto que o registo no BackOffice RM não considera a Filial como parte da Chave e existe a restrição na Mensagem Única TOTVS para envio do 'CompanyInternalId' completo (Coligada + Filial), é necessário que o sistema destinatário possua este cadastro exclusivo por Coligada e compartilhado por Filial.

Em resumo, o sistema de destino não deve considerar a informação de Filial enviada, pois caso no BackOffice RM este campo esteja nulo será enviada a Filial do contexto de integração, que e a primeira filial da empresa disponível na tabela De-Para.

Em relação ao Protheus deve seguir o seguinte compartilhamento:

* + Empresa:  Exclusivo
  + Unidade:   Deve ser equivalente à entidade relacionada no De-Para de integração (Empresa ou filial)
  + Filial:        Compartilhado

**Cenários de integração com Ponto de Venda Protheus**

****Cenário 1 - Formas de pagamento Padrão****

Algumas formas de pagamento são utilizadas atualmente no SigaLoja de forma rígida, ou seja, mantendo sempre o mesmo código para as modalidades de pagamento.

Com intuito de viabilizar o uso das formas de pagamento cadastradas previamente no BackOffice RM serão disponibilizados parâmetros para alterar estas formas de pagamento para a desejada. 

Assim sendo, o usuário terá a opção de trabalhar das seguintes formas:

1. Continuar utilizando o PDV com as Formas de Pagamento padrão, devendo assim garantir que todas estas formas de pagamento (listadas abaixo) constam com mesmo código no BackOffice RM.
   * R$ - Dinheiro
   * CC - Cartão de Crédito
   * CD - Cartão de Débito
   * CH - Cheque
3. Utilização de mapeamento de Formas de Pagamento integradas. Sendo assim, deve ser parametrizado no Protheus qual será a forma de pagamento utilizada para cada opção. Segue abaixo lista de parâmetros:
   * MV\_LJMUDIN: parâmetro de forma de pagamento para Dinheiro.
   * MV\_LJMUCH: parâmetro de forma de pagamento para Cheque.
   * MV\_LJMUFI: parâmetro de forma de pagamento para Financiado.

Nesta opção antes de enviar Cupom Fiscal ao BackOffice RM o SigaLoja buscará no parâmetro correspondente qual é a forma de pagamento a ser enviada ao RM.  

**Cenário 2 - Administradora Financeira** 

Para utilizar o Ponto de Venda com pagamento em Cartão de Crétido ou Cartão de Débito, deve-se cadastrar a Administradora Financeira no Protheus e vincular qual será a forma de pagamento utilizada. Nenhuma das informações de Administradora Financeira será integrada com o BackOffice RM, sendo utilizado somente para identificação da forma de pagamento do Cupom Fiscal e demais controles de uso do Pinpad.

No cadastro de Administradora Financeira do Protheus será criado um campo que irá guardar o código da forma de pagamento do RM. Esta opção é necessária, pois quando as formas de pagamento são CC - Cartão de Crétido ou CD - Cartão de Débito, o processo de Vendas do Protheus utiliza de forma fixa os códigos CC e CD para recuperar a Administradora Financeira. Assim ao cadastrar a Administradora Financeira o usuário deverá selecionar qual é a forma de pagamento do RM que ficará associada ao registro.

Os dados de comissionamento e demais informações não precisam ser cadastradas no Protheus, visto que estes controles serão efetuados no BackOffice RM.

**Restrições e Ponto de Atenção**

* **Formas de Pagamentos Padrão Protheus:** visto que a base Protheus possui carga com formas de pagamento padrão (obrigatoriamente constam na base de dados) estes registros não poderão ser alterados e excluídos, sendo adotadas as seguintes ações abaixo:
  + **Alteração:** ao alterar uma forma de pagamento no RM, o Protheus realizará a alteração no cadastro. Caso a alteração seja em uma forma de pagamento padrão do Protheus, a alteração será aplicada no RM e será enviada uma mensagem de alteração para o Protheus, porém o registro não será atualizado por ser um registro padrão. A alteração será aplicada apenas no RM.
  + **Inativação:**  
    1. Ao inativar uma forma de pagamento no RM e a mesma não for uma forma de pagamento padrão do Protheus, serão excluídos o registro no cadastro do Protheus e na tabela De-Para.  
    2. Caso seja uma forma de pagamento que pertence aos cadastros padrões do Protheus, será excluído apenas o registro da tabela De-Para.
  + **Exclusão:** após a exclusão da Forma de Pagamento no RM o registro será excluído no Protheus. Caso seja uma forma de pagamento padrão do Protheus a exclusão será realizada apenas no RM e no Protheus será realizada exclusão da tabela De-Para.

* **Cadastro de Condição de Pagamento:**visto que o PDV envia ao RM o parcelamento definido (meio de pagamento) não será necessário integrar a condição de pagamento e esta informação também não deverá ser enviada na mensagem de Cupom Fiscal.

## Fluxo do Processo

## Mapeamento dos campos

**Mensagem:** PaymentMethod 1.000

 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mensagem Padrão** | **Descrição** | **RM** | | |
| **Tabela** | **Campo** | **Observação** |
| **CompanyId** | Código da empresa. | TFORMAPAGTO | CODCOLIGADA | Código da Coligada é obtido a partir do De-Para de Filial. |
| **BranchId** | Código da filial | TFORMAPAGTO | CODFILIAL |
| **CompanyInternalId** | InternalId da chave completa de empresa do produto | TFORMAPAGTO | CODCOLIGADA|CODFILIAL |
| **Code** | Código do Forma de Pagamento | TFORMAPAGTO | CODFORMAPAGTO |  |
| **InternalId** | InternalId de Integração | TFORMAPAGTO | CODCOLIGADA|IDFORMAPAGTO |  |
| **Name** | Nome da Forma de Pagamento | TFORMAPAGTO | DESCFORMAPAGTO |  |
| **Active** | Forma de Pagamento Ativa/Inativa | TFORMAPAGTO | INATIVO |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
