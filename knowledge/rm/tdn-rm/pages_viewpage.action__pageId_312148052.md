---
content_hash: f2c3f7ac068ff9480e423aa949207a9f0f1f3564bde37d6baf29705681ae8f39
fetched_at: '2026-06-29T00:08:45.636040+00:00'
page_id: '312148052'
product: rm
source: tdn-rm
title: DT Permitir Parametrizar serviços que podem ser pagos com cartão de crédito
  e/ou débito.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=312148052
version: 2
---

# PERMITIR PARAMETRIZAR SERVIÇOS QUE PODEM SER PAGOS COM CARTÃO DE CRÉDITO E/OU DÉBITO

**Essa funcionalidade está disponível apenas para o Novo Portal do Aluno**.

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | * Geração de lançamentos * Pagamento com Cartão | Pagamento com Cartão | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [PORTALMOBILE01-1794](http://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-1794 "View this issue") |
| **País(es):** | BRA |
| **Banco(s) de Dados:** | SQL e Oracle |
| **Tabelas Utilizadas:** | SSERVICO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

No cadastro dos serviços financeiros do TOTVS Educacional foram criadas duas novas opções para cada serviço onde o usuário poderá marcar quais serviços que ele desejam que sejam pagos com cartão de crédito e quais poderão ser pagos com cartão de débito.

Para efetuar a parametrização, é necessário que o usuário, acesse: Totvs Gestão Educacional | Financeiro/Contábil | Formação de Preço | Serviços.

Como padrão, o sistema manterá  a configuração predominante, caso o usuário deseja parametrizar algum serviço em específico, basta desmarcar o checkBox referente ao tipo de pagamento.

Aviso!

Caso o parâmetro esteja desmarcado para os dois tipos de pagamento com Cartão, o portal não irá exibir o botão referente ao pagamento com Cartão.

Atualmente, existem dois tipos de modalidades de pagamento, sendo BuyPage Cielo e CheckOut Cielo

* **BuyPage**: Ao visualizar a permissão de pagamento no cadastro do serviço, o sistema irá exibir os dois tipos, sendo: Pagamento com Cartão de Crédito e Cartão de Débito.

* **CheckOut** : Ao visualizar a permissão de pagamento no cadastro do serviço, o sistema irá exibir apenas uma opção de pagamento, sendo: Pagamento com Cartão de Crédito / Débito.

Onde a parametrização deverá ser realizada na Cielo conforme os critérios de pagamento.
