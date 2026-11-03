---
content_hash: fd0d1b662ba023ae9558af41191c1b2ca46e13436c65704b03412514d857700f
fetched_at: '2026-06-29T00:09:12.308388+00:00'
page_id: '416851131'
product: rm
source: tdn-rm
title: DT Envio de Solicitação de Compra Automático Paradigma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416851131
version: 11
---

# PARADIGMA - SOLICITAÇÃO DE COMPRAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Tipos de Movimento. | RMSParamsWizardAction. | |
| **Cadastros Iniciais:** | Não se aplica. |
| **Parâmetro(s):** | Código do Tipo de Movimento = Pedido de Compra (1.1)  Tipo do Movimento de Compras = Solicitação de Compras (Etapa - Compra/Venda - Outros Dados)  Inclusão automática de Cotação = Marcado |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-3512. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | TTMVEXT - Tipos de Movimento. |
| **Sistema(s) Operacional(is):** | Windows 10. |

## Descrição

Permitir que o usuário possa integrar automaticamente a Solicitação de Compras do BackOffice RM com o Portal de Compras Paradigma.

### Incluir Cotação

A inclusão automática da Solicitação de Compras do BackOffice RM acontecerá de forma transparante para o comprador, porém será necessário realizar algumas configurações no sistema para que isso aconteça.

**Configuração de Tipo de Movimento**

* Tipo de movimento deve ser configurado para utilizar Funcionário (Etapa Mov - Tab - Funcionários - Edição de Funcionário diferente de Não Edita);
* Tipo de movimento de deve ser configurado como Inclusão automática de cotação (vide item Configurações e Parâmetros);

Após realizar as configurações acima, quando o comprador criar uma nova solicitação de compras será criado uma Cotação no BackOffice RM do tipo Integrado com Paradigma. A cotação que será criada receberá as seguintes informações: Coligada do movimento, Código do usuário logado, Filial do movimento, Data de criação do movimento será a data da cotação, Data Limite de Resposta da cotação receberá o valor de 31/12/2099, Código do Comprador, Data de entrega, Observação (que será preenchido com valor "Integração automática com Paradigma")  e Integrado com paradigma igual a verdadeiro. Os itens da cotação serão compostos pelos itens de movimento da solicitação que está sendo gravada.

**Consistências**

* O funcionário deve ser do tipo Comprador ou Vendedor e Comprador
* O usuário logado deve ter permissão por tipo de movimento para a geração automática de cotação.

### Envio de Solicitação de Compra com Portal Paradigma

A Solicitação de Compras do BackOffice RM poderá ser integrada automaticamente com portal Paradigma. Para isso deve-se realizar a inclusão de movimento via webservice, informando no campo TMOV.INTEGRADOAUTOMATICOPARADIGMA o valor "true". Desta forma além de ser criado o movimento, será criado uma Cotação e a Requisição com base na Cotação no portal Paradigma. Quando for passado o valor "false" será criado apenas o movimento e sua cotação, e a integração com o paradigma precisará ser realizada manualmente através da visão de Cotação processo Integrar Requisições com Portal de Compras.

### **Retorno de Cotações orçadas no Portal Paradigma**

Como na criação da Cotação a Data Limite de Resposta foi criada com a mesma data de emissão do movimento, no processo de Retorno de Cotações orçadas no Portal Paradigma, esta data deve ser atualizada com a data informada no Paradigma.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações Biblioteca RM versão 12.1.23.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Gestão de Estoque, Compras e Faturamento**, acesse **Ambientes/Parâmetros/Gestão de Estoque, Compras e Faturamento/04.06 - Gestão de Compras/04.06.01 - Solicitação de Compra**. Selecione um tipo de movimento e clique em **Parametrizar**. Na **Etapa Compra/Venda - Outros Dados**configure o(s) parâmetro(s) a seguir:

   |  |  |  |
   | --- | --- | --- |
   | **Parâmetro** | **Valor** | **Observação** |
   | **Tipo do Movimento de Compra:** | Solicitação de Compras |  |
   | **Inclusão automática de Cotação:** | Marcado | Este parâmetro ficará disponível somente quando existir integração com Paradigma habilitada para a coligada logada. |
2. Em **Serviços Globais**, acesse **Segurança/Usuários/Anexos/Permissões por Tipo de Movimento**, selecione o tipo de movimento previamente parametrizado e marque a opção **Gerar Cotação Automática.**

**Obs**: A opção **Gerar Cotação Automática** será exibida apenas em coligadas integradas ao paradigma.
