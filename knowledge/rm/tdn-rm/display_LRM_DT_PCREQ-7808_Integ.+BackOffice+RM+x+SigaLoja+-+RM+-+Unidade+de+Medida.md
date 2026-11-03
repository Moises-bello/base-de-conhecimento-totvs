---
content_hash: d496f145450d39d7ad8a75504d01c6c5ef9733ae4945db00a1fd1456dfe5807c
fetched_at: '2026-06-29T00:06:27.891776+00:00'
page_id: '233737030'
product: rm
source: tdn-rm
title: DT_PCREQ-7808_Integ. BackOffice RM x SigaLoja - RM - Unidade de Medida
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PCREQ-7808_Integ.+BackOffice+RM+x+SigaLoja+-+RM+-+Unidade+de+Medida
version: 117
---

# Integração BackOffice RM x SigaLoja - RM - Unidade de Medida

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  |  | | --- | --- | --- | | **Rotina** | **Nome Técnico** | **Mensagem Única TOTVS** | | Unidades de Medida. | EstUndAction. | UnitOfMeasure (2.000) |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Configuração da Integração | ConConfiguraIntegracaoAction | | Integrações de Mensagem Única. | ConIntegracaoAction | | De-Para | ConIntegracaoIdAction | |
| **Cadastros Iniciais:** | Cadastrar o De-Para manual das Unidades base do Protheus com as Unidades base do RM. |
| **Parâmetro(s):** | N/A. |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Mais\ Tabelas Auxiliares \ Unidade. |
| **Chamados Relacionados** | N/A. |
| **Requisito (ISSUE):** | PCREQ-7808 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE. |
| **Tabelas Utilizadas:** | * TUND - Unidades |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Este requisito tem por objetivo possibilitar a integração do cadastro de Unidades de Medida com o PDV PROTHEUS através do protocolo de Mensagem Única TOTVS.

Para maiores detalhes sobre a integração de Unidade de Medida, acesse a Especificações de Requisitos .

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No módulo de **Integração**, acesse **Ferramentas/Configurar**. Informe **Usuário/Senha** do banco de dados, teste a conexão. Avance até a **Projetos de Integração** e selecione o item **BackOffice RM x PDV Protheus (Novo Modelo)** e execute o processo.
2. Acesse **Integração/Mensagem Única/Integrações**, selecione a opção de filtro. Na visão de **Integrações** editar a integração de **Identificador 1016** e verifique se está informado a **URL WebService** do Protheus.
3. Verifique em **Anexos/Mapeamento de Entidades** se a mensagem **UnitOfMeasure versão 2.000** está mapeada.

**IMPORTAÇÃO DE FÓRMULA VISUAL**

1. Acesse **Gestão\Fórmula Visual\Fórmula visual\Processo\Importação de Fórmula Visual.** Clique em **Adicionar Objetos** e localize o arquivo a ser importado que encontra-se disponível na pasta **Fórmulas Visuais**, interna à pasta **ObjetosGerencias** no ambiente instalado do sistema (**../CorporeRM/ObjetosGerencias/Fórmulas Visuais**). Deverá ser marcado o parâmetro **Importar Gatilho**.
2. Visando oferecer facilidade para clientes que já possuam a base de dados com Unidades de Medida, foi disponibilizado também uma Fórmula Visual para sincronização dos registros existentes, que é responsável por filtrar somente os registros não enviados ou desatualizados no Protheus. Esta fórmula visual pode ser utilizada para carga inicial, novo sincronismo em casos onde o gatilho tenha sido desabilitado ou como forma de integração assíncrona.

## Procedimento para Utilização

**Cadastrar De-Para das Unidades Base**

Vamos utilizar como exemplo a unidade base UN-Unidade.

1. No módulo **Integração**, acesse **Integração/Mensagem Única/De-Para** e selecione um filtro.

O sistema apresenta a janela de **De-Para** com os registros cadastrados.

2. Na visão clique em **Incluir**.

O sistema apresenta a janela de edição **De-Para**. Informe os dados conforme abaixo:

* **Tabela RM:** TUnd
* **Chave Primária RM:** CODUND
* **Valor Chave Primária RM:**UN
* **Sistema Integrado:**PROTHEUS
* **Valor Chave Integração:** T1||UN.

**Atenção:** o valor da chave de integração deve respeitar a definição de Empresa configurado no Protheus.

4. Confira os dados e confirme.

**Cadastrar Unidade de Medida**

1. No módulo **Gestão de Estoque, Compras e Faturament****o**, acesse **Cadastros/Estoque, Compras e Faturamento/Mais/Tabelas Auxiliares/Unidade** e selecione um filtro.

O sistema apresenta a janela de Unidade de Medida com os registros cadastrados.

2. Na visão clique em **Incluir**.

O sistema apresenta a janela de edição **Unidade de Medida**. Informe o **Código**e a **Descrição**.

4. Confira os dados e confirme.

divs
