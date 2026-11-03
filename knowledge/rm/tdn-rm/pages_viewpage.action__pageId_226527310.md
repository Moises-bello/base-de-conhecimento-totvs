---
content_hash: 8f2e3dd2ab50803a3fe6b1b072c62480f873bf97b661f37245e88655c20b14f1
fetched_at: '2026-06-29T00:06:26.680850+00:00'
page_id: '226527310'
product: rm
source: tdn-rm
title: DT_PCREQ-7798_Integ. BackOffice RM x SigaLoja - RM - Código de Barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=226527310
version: 119
---

# Integ. BackOffice RM x SigaLoja - RM - Código de Barras

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  |  | | --- | --- | --- | | **Rotina** | **Nome Técnico** | **Mensagem Única TOTVS** | | Produto | EstPrdAction. | Item (3.004) |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Unidades de Medida | EstUndAction. | | Configuração da Integração | ConConfiguraIntegracaoAction | | Integrações de Mensagem Única. | ConIntegracaoAction | |
| **Cadastros Iniciais:** | Cadastrar Unidade de Medida.  Cadastrar Produto. |
| **Parâmetro(s):** | N/A. |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Produto \ Código de Barras |
| **Chamados Relacionados** | N/A. |
| **Requisito (ISSUE):** | PCREQ-7798 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE |
| **Tabelas Utilizadas:** | * TPRDCODIGO – Cadastro de Código Genérico de Produtos. * TPRODUTO – Produtos Globais. * TUND – Unidades. |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Este requisito tem por objetivo possibilitar a integração do cadastro de Códigos de Barras do Produto com o PDV PROTHEUS através do protocolo de Mensagem Única TOTVS.

Os dados de Código de Barras são cadastrados através do cadastro de Produto do RM e serão sincronizados na mensagem única Item (Produto) através da tag **ListOfBarCode**.

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No módulo de **Integração**, acesse **Ferramentas/Configurar**. Informe **Usuário/Senha** do banco de dados, teste a conexão. Avance até a **Projetos de Integração** e selecione o item**BackOffice RM x PDV Protheus (Novo Modelo)** e execute o processo.
2. Acesse **Integração/Mensagem Única/Integrações**, selecione a opção de filtro. Na visão de **Integrações** editar a integração de **Identificador 1016** e verifique se está informado a **URL WebService** do Protheus.
3. Verifique em **Anexos/Mapeamento de Entidades** se a mensagem **Item versão 3.004** está mapeada.

**IMPORTAÇÃO DE FÓRMULA VISUAL**

1. Acesse **Gestão\Fórmula Visual\Fórmula visual\Processo\Importação de Fórmula Visual.** Clique em **Adicionar Objetos** e localize o arquivo a ser importado que encontra-se disponível na pasta **Fórmulas Visuais**, interna à pasta **ObjetosGerencias** no ambiente instalado do sistema (**../CorporeRM/ObjetosGerencias/Fórmulas Visuais**). Deverá ser marcado o parâmetro **Importar Gatilho**.
2. Visando oferecer facilidade para clientes que já possuam a base de dados com Produtos com Códigos de barras, foi disponibilizado também uma Fórmula Visual para sincronização dos registros existentes, que é responsável por filtrar somente os registros não enviados ou desatualizados no Protheus. Esta fórmula visual pode ser utilizada para carga inicial, novo sincronismo em casos onde o gatilho tenha sido desabilitado ou como forma de integração assíncrona.

## Procedimento para Utilização

1. No módulo **Gestão de Estoque, Compras e Faturament****o**, acesse **Cadastros/Produtos** e selecione um filtro.

O sistema apresenta a janela de produtos cadastrados.

2. Na visão clique em **Editar**.

O sistema apresenta a janela de edição Produto.

3. Na **Pasta Código de Barras** clique em **Incluir**:

O sistema apresenta a janela de inclusão de Código de Barras. Informe o **Código** e a **Unidade****.**

4. Confira os dados e confirme.

divs
