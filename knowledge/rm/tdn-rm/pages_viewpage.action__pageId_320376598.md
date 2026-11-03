---
content_hash: 6a86aac279c14bbe10c4895b1eed17588360bc5895180234f14573f9125fef8e
fetched_at: '2026-06-29T00:08:47.761791+00:00'
page_id: '320376598'
product: rm
source: tdn-rm
title: 1331649 MATESTCNTFTOF01-1147 DT Campo tributação do CF no Cadastro de Produto
  por filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320376598
version: 5
---

# Campo tributação do CF no Cadastro de Produto por filial

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque Compras e Faturamento |
| **Rotina:** | Integração produto BackofficeRM x PDV Protheus através de mensagem única. |
| **Cadastros Iniciais:** | No cadastro de produto, anexo "Informações por Filial" informar "Tributação do cupom fiscal" |
| **Parâmetro(s):** | *.* |
| **Ponto de Entrada:** | Não se aplica. |
| **Tickets relacionados:** | 1331649. |
| **Requisito/S****tory/Issue(informe o requisito relacionado):** | MATESTCNTFTOF01-812. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQLServer e Oracle. |
| **Conversores e Parâmetros:** | É necessário executar o atualizar de base para ativação dos recursos;  Versões 12.1.17 à 12.1.19 é necessário entrar em contato com suporte TOTVS para liberação do script. |
| **Tabelas Utilizadas:** | TPRODUTODEF / TPRDFIL. |
| **Sistema(s) Operacional(is):** | Windows. |

## Descrição

Devido a possibilidade legal de informar tributo do cupom fiscal por filial, é feito os ajustes necessários no cadastro do produto para que tenha a inclusão dessa informação e a integração desses dados através de mensagem única para PDV Protheus.

## Definição da Regra de Negócio

Para atender a necessidade de informar Tributação ECF do Produto por Filial, será necessário realizar alteração no cadastro de Informação de Produto por Filial, adicionando o campo **Tributação Cupom Fiscal**. Este campo não será obrigatório e ficará loclizado na área destacada na imagem abaixo.

  

O campo **Tributação Cupom Fiscal** do cadastro de Produtos continuará sendo utilizado. Quando não for preenchido informação de tributo por filial então será utilizado o do produto.

  

**Restrição:**

* Os dados de Tributação Cupom Fiscal por Filial não será considerado nos layouts de Importação/Exportação de produtos.

### **Integração com PDV Protheus**

A mensagem única de produto (Item) deverá contemplar o envio desta nova informação a nível de filial.

**Pré-Requisitos:**

1. Estar utilizando o novo modelo de integração **BackOffice RM x PDV Protheus (Novo Modelo).**Se não tiver acesso a essa opção como mostra a imagem abaixo é necessário entrar em contato com o Suporte Totvs para liberação do novo modelo.

**Observação:** após a execução do configurador de integração, alterar o parâmetro de integração para trabalhar com Tributação ECF do Produto por Filial.

2. Configurar a tabela de Produtos no Protheus para ser Exclusivo por Filial.

3. Atualizar a base de dados RM para que seja criado o novo campo na tabela de Informação de Produto por Filial (TPRDFIL).

4. Importar a nova fórmula visual de integração de produto.

5. Utilizar TOTVS linha RM versão 12.1.18 ou superior e TOTVS linha PROTHEUS versão 12.1.10.17 ou superior.

**Adapter/Transformação: [Item\_Send\_4005.xslt]**:

Cria o XSLT de saída para considerar a lista de Tributos ECF por Filial. Quando o produto possui Tributação ECF por Filial deve-se preencher a tag ListOfBranchInformation.

**SourceCode – ITEM – Versão 4.005**

No SourceCode do Item é realizado uma alteração no DataSet, para que seja considerado somente as filiais que possuem integração com o Protheus, ou seja, as demais filiais que não possuem integração não serão consideradas no escopo da mensagem enviada. As filiais integradas estão definidas na tabela De-Para HCINTEGRACAOID onde campo TABELARM = "GFILIAL".

**Atividade - RM.Mov.FormulaVisual.Activities**

MovProdutoIntegradoProtheus : MovActivity

Quando o parâmetro de integração estiver usando tributação por filial, ao selecionar informação de TPRDFIL é necessário considerar o De-Para existente para tabela de filiais.

**Tabelas Utilizadas**

* TPRODUTODEF - Definições do produto
* TPRDFIL- Informação do produto por filial

## Procedimento para Utilização

Estar utilizando o novo modelo de integração “BackOffice RM x PDV Protheus (Novo Modelo)” se não tiver acesso a essa opção no "Assistente de Configuração" entre em contato com o Suporte Totvs para liberação do novo modelo.

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No **RM**, acesse **Integração/Ferramentas/Configurar**.   
   1. Na janela **Assistente de Configuração de Integração** avance para a etapa **Configuração do banco de dados** e informe Usuário e Senha para conectar ao banco. Teste a conexão e avance.
   2. Na etapa **Projetos de Integração** selecione a integração que será configurada, avance e execute o assistente.
2. No **PROTHEUS**acesse **Configurador (SIGACFG)**, acesse **Ambiente/Schedule/Adapter E.A.I**.   
     
   Crie/Altere o adapter ITEM conforme dados a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| ****Mensagem Única:**** | Sim |
| ****Rotina:**** | MATA010 |
| ****Mensagem:**** | ITEM |
| ****Envia:**** | Não |
| **Recebe:** | Sim |
| **Método:** | Síncrono |
| **Operação:** | Todas |
| **Canal Envio:** | EAI |
| **Versão Envio:** | 4.005 |

**IMPORTAÇÃO DE FÓRMULA VISUAL**

No **RM,** acesse menu **Gestão\Fórmula Visual** e execute o processo de **Importação de Fórmula Visual.**

Selecione a fórmula visual de integração de Produto  "**MOVWKF0013 - Item**", que encontra-se disponível na pasta "...CORPORERM | Objetos Gerenciais | Fórmulas Visuais e realize a importação conforme apresentado no documento [Importação\Exportação de fórmula visual](http://tdn.totvs.com/pages/viewpage.action?pageId=63278047), com atenção à importação dos gatilhos (caso contrário a mesma não será acionada).
