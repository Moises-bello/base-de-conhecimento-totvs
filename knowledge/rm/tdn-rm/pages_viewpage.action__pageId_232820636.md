---
content_hash: 9f4956f3568b7a6ac4d1c56e0c4ea858469b327b0c50e02aabf93f7b8c722bf2
fetched_at: '2026-06-29T00:06:27.368469+00:00'
page_id: '232820636'
product: rm
source: tdn-rm
title: DT_PCREQ-7799_Integ. BackOffice RM x SigaLoja - RM - Estação PDV
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232820636
version: 121
---

# Integração BackOffice RM x SigaLoja - RM - Estação PDV

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  |  | | --- | --- | --- | | **Rotina** | **Nome Técnico** | **Mensagem Única TOTVS** | | Ponto de Venda | MovGrpPontoVendaAction | ListOfStationSalePoint (1.000) |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Grupos de Pontos de Venda | MovGrpPontoVendaAction | | Configuração da Integração | ConConfiguraIntegracaoAction | | Integrações de Mensagem Única. | ConIntegracaoAction | |
| **Cadastros Iniciais:** | Cadastrar Filial. A filial que for utilizada no Ponto de Venda deve existir na tabela de De-Para da Integração.  Definir Tipo de Movimento de Venda. Este tipo de movimento será utilizado na inclusão de Cupom Fiscal.  Cadastrar Grupo de Pontos de Venda. |
| **Parâmetro(s):** | N/A. |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \  Estoque, Compras e Faturamento \ Mais \ Tabelas Auxiliares \ Ponto de Venda. |
| **Chamados Relacionados** | N/A. |
| **Requisito (ISSUE):** | PCREQ-7799 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE |
| **Tabelas Utilizadas:** | * TGRPPONTOVENDA – Grupamento de Pontos de Venda * TPONTOVENDA – Ponto de Venda |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Este requisito tem por objetivo possibilitar a integração do cadastro de Pontos de Venda com o PDV PROTHEUS através do protocolo de Mensagem Única TOTVS.

Para maiores detalhes sobre a integração de Ponto de Venda, acesse a Especificações de Requisitos .

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No módulo de **Integração**, acesse **Ferramentas/Configurar**. Informe **Usuário/Senha** do banco de dados, teste a conexão. Avance até a **Projetos de Integração** e selecione o item**BackOffice RM x PDV Protheus (Novo Modelo)** e execute o processo.
2. Acesse **Integração/Mensagem Única/Integrações**, selecione a opção de filtro. Na visão de **Integrações** editar a integração de **Identificador 1016** e verifique se está informado a **URL WebService** do Protheus.
3. Verifique em **Anexos/Mapeamento de Entidades** se a mensagem **ListOfStationSalePoint** **versão 1.000** está mapeada.

**IMPORTAÇÃO DE FÓRMULA VISUAL**

1. Acesse **Gestão\Fórmula Visual\Fórmula visual\Processo\Importação de Fórmula Visual.** Clique em **Adicionar Objetos** e localize o arquivo a ser importado que encontra-se disponível na pasta **Fórmulas Visuais**, interna à pasta **ObjetosGerencias** no ambiente instalado do sistema (**../CorporeRM/ObjetosGerencias/Fórmulas Visuais**). Deverá ser marcado o parâmetro **Importar Gatilho**.
2. Visando oferecer facilidade para clientes que já possuam a base de dados com Pontos de Venda, foi disponibilizado também uma Fórmula Visual para sincronização dos registros existentes, que é responsável por filtrar somente os registros não enviados ou desatualizados no Protheus. Esta fórmula visual pode ser utilizada para carga inicial, novo sincronismo em casos onde o gatilho tenha sido desabilitado ou como forma de integração assíncrona.

## Procedimento para Utilização

1. No módulo **Gestão de Estoque, Compras e Faturament****o**, acesse **Cadastros/Estoque, Compras e Faturamento/Mais/Tabelas Auxiliares/Ponto de Venda** e selecione um filtro.

O sistema apresenta a janela de grupos de pontos de venda cadastrados.

2. Na visão clique em **Incluir**.

O sistema apresenta a janela de edição Grupo de Pontos de Venda.

3. Na **Pasta Ponto de Venda** clique em **Incluir**:

O sistema apresenta a janela de inclusão de Ponto de Venda. Informe o **Ponto de Venda, Descrição, Filial, Local de Estoque, Série,** **Tipo de Movimento de Venda**e o **CRO Default****.**No campo **Tipo** marque a opção **Impressora Fiscal.**

4. Confira os dados e confirme.

divs
