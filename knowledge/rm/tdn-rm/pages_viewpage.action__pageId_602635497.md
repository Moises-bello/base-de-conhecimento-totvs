---
content_hash: f785283cbf1819cf69bd653a8b692da7e6a69e6106c7ae968a0ccfb525abaefb
fetched_at: '2026-06-29T00:10:58.026742+00:00'
page_id: '602635497'
product: rm
source: tdn-rm
title: Integração TOTVS Folha de Pagamento RM x TOTVS Moda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=602635497
version: 59
---

**Totvs Folha de Pagamento Linha RM x Totvs Moda**

---

## Contexto de negócio (Introdução)

A partir do release 12.1.29, está disponível aos clientes TOTVS a oferta de Integração do Folha de Pagamento RM ao TOTVS Moda. A integração possibilita a realização de todos os processos de uma folha de pagamento de forma simples e segura, gerando os compromissos a pagar diretamente no financeiro do TOTVS Moda, assim também os lançamentos contábeis diretamente no módulo contábil do ERP. Além dos lançamentos financeiros e contábeis, também são integrados os cadastros que sustentam estas operações. O funcionamento da integração ocorre de forma “síncrona” entre os sistemas, utilizando a tecnologia EAI, ou seja, sempre que ao cadastrar ou alterar uma informação no TOTVS Folha de Pagamento e esta estiver dentro do contexto da integração, a informação será replicada para os dois sistemas integrados (TOTVS Moda e TOTVS Folha de Pagamento).

A integração entre TOTVS Folha de pagamento RM e TOTVS Moda possibilitará a realização dos procedimentos relacionados à folha de pagamento compartilhando entidades do TOTVS Moda e TOTVS Folha de pagamento RM, reportando e processando cálculos e cadastros relacionados a rotina de folha de pagamento, lançamentos financeiros e contábeis.

## Sistemas Envolvidos

* **TOTVS Moda:** O TOTVS Moda é o produto TOTVS responsável por enviar via EAI, as mensagens de Cliente/Fornecedor, Banco/Agência,  Centro de Custo e Plano de Contas.
* **TOTVS Folha de Pagamento RM:** O RM Folha de Pagamento é o produto RM responsável por receber as mensagens enviadas pelo TOTVS Moda, e enviar as mensagens de lançamentos contábeis , lançamentos financeiros, cadastro de funcionários, seção (unidade funcional), função (Cargo) e transferência de funcionários.

## Integração

O objetivo do projeto é integrar o TOTVS Moda com o TOTVS Folha de Pagamento RM, por meio das mensagens únicas 'EAI'. Desta forma, será disponibilizado aos clientes do ERP a possibilidade de trabalhar a sua gestão de backOffice de forma integrada entre os sistemas TOTVS.

## Escopo

O escopo da integração é a sincronização entre os cadastros de backOffice de ambos sistemas. Para fazer esse controle, as seguintes entidades foram integradas:

* Clientes/Fornecedor: Ambos enviam e recebem;
* Banco/Agência: TOTVS Moda envia;
* Histórico de situação do funcionário: Ambos enviam e recebem;
* Calendário Contábil: TOTVS Moda envia;
* Histórico de Contas: TOTVS Moda envia;
* Centro de Custo: TOTVS Moda envia;
* Conta Contábil: TOTVS Moda envia;
* Lançamento Contábil: Folha de Pagamento RM envia;
* Lançamento Financeiro: Folha de Pagamento RM envia;
* Pagamentos de autônomos: TOTVS Moda envia;
* Folha de pagamento mensal - Comissões: TOTVS Moda envia;
* Cargo (Função): Ambos enviam e recebem;
* Unidade Funcional (Seção): Folha de Pagamento RM envia);
* Funcionário: Folha de Pagamento RM envia;
* Transferência de funcionário: Folha de Pagamento RM envia.

**Atenção:**

Antes de iniciar a instalação/implantação e utilização é extremamente necessário ler e entender o funcionamento do EAI 2.0 . Clique no [Linha RM - EAI 2.0](https://tdn.totvs.com/display/INT/EAI+2.0+-+Linha+RM) e leia a documentação.

## Pré-requisitos instalação/implantação/utilização

Para o correto funcionamento da integração é necessário parametrizar o RM e também verificar a parametrização necessária no TOTVS Moda antes de realizar a integração nos sistemas envolvidos. 

Para realizar a configuração/parametrização do RM deverá seguir os seguintes passos:

**a) Para realizar a integração entre RM e TOTVS MODA, é necessário executar o Script de Integração por meio do RM.Script.Executor. Solicite este script à equipe de desenvolvimento da squad de ROTINAS, abrindo uma issue de apoio e informando o número do CNPJ da coligada 1 do cliente.**

**Observação 1:  Este script foi desenvolvido para criar as configurações necessárias para integração do TOTVS Folha de Pagamento RM com o TOTVS Moda sem que tenha sido efetuada nenhuma parametrização referente a integração, sendo necessária a configuração no RM para a utilização da Gestão Contábil e Financeira.**

**Observação 2 : A integração é realizada em ambos os sistemas. Para que a integração funcione corretamente, será necessário configurar o sistema TOTVS Moda  de acordo com as instruções passadas pela equipe do TOTVS Moda.**

**b) Tela Aplicativos (Caminhos para acesso aos serviços de integração do ambiente Folha de Pagamento RM e TOTVS Moda  - Rest e Web Service):**

**Após executar o script, deverão ser verificados os dados da tela de Aplicativos:**

1 - **Id/Nome:** Este é um campo meramente informativo, recomendamos uma descrição curta, mas clara, para este pacote de integração. **Exemplo:** **App: [RHRMBACKOFFICE] - [TOTVS\_MODA]**

2 - **Descrição:** Informa a descrição criado para a integração. Trata-se de um campo meramente informativo.  
3 - **Código do Produto:** Informa o código do produto criado para a integração. Para essa integração deverá ser **TOTVS\_MODA**.  
4 - **Código do SourceAplication:** Informa o código do SourceAplication criado para a integração. Para essa integração deverá ser **TOTVS\_MODA**.  
5 - **Endereço do Monitor:** Informe o endereço do monitor da integração.  
6 - **Aplicativo Interno:** Informe se é integração com aplicativo interno.  
7 - **Ativo:** Informe se a integração está ativa.  
8 - **Canal de comunicação:** Na integração entre TOTVS Folha de Pagamento RM X TOTVS MODA, utilizamos o tipo de comunicação REST.  
9 - **SOAP:** Informe o endereço do Endpoint no formato http://\[servidor\]:\[porta\] (opcional) para comunicação pelo webservice entre os sistemas.  
     **REST:** Informe o endereço do Endpoint no formato http://\[servidor\]:\[porta\] para comunicação pelo webservice entre os sistemas.  
10 - **Endereço do Endpoint:** informe o endereço do endpoint para comunicação entre os sistemas.  
11 - **Usuário:** Informe o usuário para comunicação/autenticação pelo webservice entre os sistemas.  
12 - **Senha:** Informe a senha para comunicação/autenticação pelo webservice entre os sistemas.  
13 - **Configuração de integração:** Informe o tipo de integração da coligada. Define qual o limite da identificação da coligada, se representa a companhia ou a unidade de negócio.

**d) Associação De/Para entre Totvs Folha de Pagamento RM x TOTVS Moda(Coligada RM com Empresa TOTVS Moda):**

O primeiro cadastro que deve ser realizado para operação dos sistemas é o de Empresa (Coligada) e suas Filiais. No RM estas entidades são cadastros comuns. Mas no TOTVS Moda a Empresa e as Filias deverão ser definidos de acordo com as configurações existentes no TOTVS Moda.

A maioria das mensagens de integração fará referências ao cadastro de Empresa/Coligada. Então será necessário a criação do De/Para, conforme exemplo abaixo:

|  |  |  |  |
| --- | --- | --- | --- |
| **De-para RM (Empresa)** | | **De-Para TOTVS MODA (Empresa)/(FILIAL)** | |
| **Tabela RM** | GCOLIGADA | **Referência** | RM |
| **Chave Primária RM** | CODCOLIGADA | **Company** | <Valor da Empresa RM> |
| **Valor Chave Primária RM** | <Valor CODCOLIGADA> | **Branch** | <Valor da Coligada RM> |
| **Sistema Integrado** | TOTVS\_MODA | **Emp. TOTVS MODA** | <Empresa do TOTVS MODA> |
| **Valor Chave Integração** | <Valor CODCOLIGADA> | **Fil. TOTVS MODA** | <Filial do TOTVS MODA> |

**Exemplo:**

Vamos supor as seguintes configurações de Empresa e Filial nos dois sistemas:

**RM**

**Coligada = 1**

**Codfilial = 1**

**TOTVS MODA**

**Empresa  = 1**

**Filial =1**

**O De/para ficará conforme o print abaixo no Totvs Folha de Pagamento RM:**

|  |  |
| --- | --- |

**g) Em RM | Integrações | EAI 2.0 | Integrações | Transações, verificar os adapters criados, conforme tabela abaixo:**

| Id | Descrição | Transação | Modo Suportado | Tipo de Entrega | Recebimento Assíncrono | Versão |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Cliente Fornecedor | CUSTOMERVENDOR | Ambos | Síncrona | Não Permite | 2.003 |
| 2 | Banco Agência e conta | BANK | Recebimento | Síncrona | Não Permite | 2.002 |
| 3 | Título Financeiro à pagar | ACCOUNTPAYABLEDOCUMENT | Envio | Síncrona | Não Permite | 2.002 |
| 4 | Centro de Custo | COSTCENTER | Ambos | Síncrona | Não Permite | 2.000 |
| 5 | Calendário Contábil | ACCOUNTINGCALENDAR | Recebimento | Síncrona | Não Permite | 1.000 |
| 6 | Histórico de Contas | ACCOUNTANTDEFAULTHISTORY | Recebimento | Síncrona | Não Permite | 1.000 |
| 7 | Conta Contábil | ACCOUNTANTACCOUNT | Recebimento | Síncrona | Não Permite | 2.001 |
| 8 | Lançamento Contábil | ACCOUNTINGENTRY | Envio | Síncrona | Não Permite | 2.002 |
| 9 | Unidade Funcional (Seção) | DEPARTAMENT | Envio | Síncrona | Não Permite | 1.000 |
| 10 | Cadastro de Funções | ROLE | Ambos | Síncrona | Não Permite | 1.000 |
| 11 | Cadastro de Funcionários | EMPLOYEE | Ambos | Síncrona | Não Permite | 2.003 |
| 12 | Transferência de funcionários | SETEMPLOYEEBRANCHTRANFER | Ambos | Síncrona | Não Permite | 1.000 |
| 13 | Folha de Pagamento Mensal - Comissões | MONTHLYPAYROLL | Recebimento | Síncrona | Não Permite | 1.000 |
| 14 | Histórico de Situação do(s) funcionário(s) | GETEMPLOYEESITUATIONS | Ambos | Síncrona | Não Permite | 1.000 |
| 15 | Pagamento autonômos externos | EXTERNALAUTONOMOUSPAYMENT | Recebimento | Síncrona | Não Permite | 1.000 |

**h) Em RM | Integrações | EAI 2.0 | Integrações | Rotas, verificar as rotas criadas, conforme tabela abaixo:**

| Aplicativo | Transação | Versão | Modo habilitado | Mensagem Original | Código Fonte Customizado |
| --- | --- | --- | --- | --- | --- |
| TOTVS\_Moda | ACCOUNTANTACCOUNT | 2.001 | Recebimento | Inclui | - |
| TOTVS\_Moda | ACCOUNTANTDEFAULTHISTORY | 1.000 | Recebimento | Inclui | - |
| TOTVS\_Moda | ACCOUNTINGCALENDAR | 1.000 | Recebimento | Inclui | - |
| TOTVS\_Moda | ACCOUNTINGENTRY | 2.002 | Envio | Inclui | - |
| TOTVS\_Moda | ACCOUNTINGITEM | 1.000 | Ambos | Inclui | - |
| TOTVS\_Moda | ACCOUNTPAYABLEDOCUMENT | 2.002 | Ambos | Inclui | - |
| TOTVS\_Moda | BANK | 2.002 | Recebimento | Inclui | - |
| TOTVS\_Moda | COSTCENTER | 2.000 | Recebimento | Inclui | - |
| TOTVS\_Moda | CUSTOMERVENDOR | 2.003 | Ambos | Inclui | - |
| TOTVS\_Moda | DEPARTAMENT | 1.000 | Envio | Inclui | - |
| TOTVS\_Moda | EMPLOYEE | 2.003 | Envio | Inclui | - |
| TOTVS\_Moda | GETEMPLOYEESITUATIONS | 1.000 | Ambos | Inclui | - |
| TOTVS\_Moda | MONTHLYPAYROLL | 1.000 | Recebimento | Inclui | - |
| TOTVS\_Moda | ROLE | 1.000 | Ambos | Inclui | - |
| TOTVS\_Moda | SETEMPLOYEEBRANCHTRANFER | 1.000 | Ambos | Inclui | - |

**i) Para a integração é necessário criar manualmente um novo registro de-para para coligada, em RM | Integrações | EAI 2.0 | Integrações | De/Para e criar também o De/Para, entre as tabelas do TOTVS Folha de Pagamento RM e TOTVS Moda, conforme modelo abaixo:**

Deverá ser mapeada a tabela do RM, campo da tabela, valor do RM, nome do aplicativo que irá utilizá-lo, valor externo (valor que será levado/recebido do outro sistema integrado),  transação que irá utilizá-la e o Identificador Global (será gravado ao ser incluído automaticamente pelo sistema).

Abaixo estão disponíveis informações das entidades integradas. Clique nos links abaixo para maiores detalhes:

**[Integração processos contábeis e financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=604520959)**  
**[I](http://wikihelp.totvs.com.br/WikiHelp/CON3/INT.FolhadepagamentoxLogixFuncoes.aspx)[ntegração cadastro de funções](https://tdn.totvs.com/pages/viewpage.action?pageId=604520722)**  
**[Integração cadastro de funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=604520617)**  
**[Integração cadastro de seções](https://tdn.totvs.com/pages/viewpage.action?pageId=604521153)**  
**[Integração processo de transferência de funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=604521295)**  
**[Integração pagamento de comissões](https://tdn.totvs.com/pages/viewpage.action?pageId=604526686)**  
**[Integração Situação de Funcionários](https://tdn.totvs.com/pages/viewpage.action?pageId=604529141)**

---

**Veja também:**

**[EAI 2.0](https://tdn.totvs.com/display/INT/Adapters+RM+-+EAI+2.0)**

**[Conversor EAI 1.0\_EAI 2.0](http://tdn.totvs.com/display/LRM/DT_ConversorEAI1_EAI2)**
