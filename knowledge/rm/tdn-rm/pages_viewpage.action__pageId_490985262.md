---
content_hash: 9d9e6150f4ab6059fda87bb75698a4c30c265b633f8b4c659655c68930e273a3
fetched_at: '2026-06-29T00:10:21.317780+00:00'
page_id: '490985262'
product: rm
source: tdn-rm
title: Edição de Dados de Coleta/Entrega com Vínculo de Cliente/Fornecedor.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490985262
version: 28
---

# Características do Requisito

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Dados de Coleta/Entrega |
| Ticket: | MATFATCMPCRM01-7729 |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATFATCMPCRM01-7729 |

## Descrição

Edição de Dados de Coleta/Entrega com Vínculo de Cliente/Fornecedor.

Atendimento NT 2018.005 e legislação do ES referente a retorno simbólico de remessa para formação de lote de exportação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.23.*

Será necessário a execução do Script **Coleta\_e\_Entrega,**disponívelna central de downloads.

## Procedimento para Utilização

## Parametrização:

1. Para se utilizar a**Edição de Dados de Coleta/Entrega**, é necessário acessar os Parâmetros do tipo de movimento em **Parâmetros → Gestão de Estoque, Compras e Faturamento → Tipo de Movimento → Etapa Mov Transporte 2/3** e selecionar a opção **Usa** no campo **Utilizar Endereço de Coleta e Entrega como Destinatário.**

2. Após parametrização do tipo de movimento, serão exibidos os campos para informar Endereço de Coleta e Entrega na guia de Transporte do movimento. 

3. Deverá ser criado o campo complementar "**LOCDESPACHO**" no cadastro de Cliente/Fornecedor, o qual representa o **r****ecinto aduaneiro** na NF-e. Segue configuração:

Foram criados novos campos para atender a NT 2018.005.

* **CEP**
* **País**
* **Telefone**
* **E-mail**
* **Cliente/Fornecedor**

O usuário poderá preencher os dados manualmente ou selecionar um cliente/fornecedor para preenchimento dos campos de coleta e/ou entrega de forma automática a partir do endereço principal, entrega ou pagamento. 

**Importante:**

1. Caso o cliente/fornecedor seja preenchido e o seu tipo de movimento esteja parametrizado para afetar estoque DE/COM terceiros, seguirá as seguintes regras para controle de estoque DE/COM terceiros:

**Cliente/Fornecedor Emitente/Destinatário:** Caso tenha Cliente e Fornecedor informado.

**Cliente/Fornecedor de Coleta ou de Entrega:**

=> Será considerado o cliente/fornecedor informado nos campos de entrega quando o tipo de movimento estiver parametrizado para aumentar o estoque COM terceiros ou quando estiver parametrizado para diminuir o estoque DE terceiros.

=> Será considerado o cliente/fornecedor informado nos campos de coleta quando o tipo de movimento estiver parametrizado para diminuir o estoque COM terceiros ou quando estiver parametrizado para aumentar o estoque DE terceiros.

**Cliente/Fornecedor de Origem/Destino:** Campo disponível no movimento na guia Integração Fiscal

2. Caso o tipo de movimento esteja parametrizado para afetar Saldo DE/COM Terceiros será obrigatório informar:

**Cliente/Fornecedor Origem/Destino ou;**

**Endereço de Coleta e Entrega como destinatário ou;**

**Cliente/Fornecedor nos campos emitente/destinatário.**

3. A origem do campo complementar "**LOCDESPACHO**" será baseada no Tipo de Movimento 2.X.XX (Exportação), onde o sistema preencherá a Tag correspondente na NF-e com a informação cadastrada no campo complementar do Cliente/Fornecedor, informado no grupo "**Local de Entrega**".
