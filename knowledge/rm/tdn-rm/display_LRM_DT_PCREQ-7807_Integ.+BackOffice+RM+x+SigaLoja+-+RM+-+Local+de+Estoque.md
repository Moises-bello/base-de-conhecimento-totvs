---
content_hash: 2fd34324141fd16ccd87923a2899bf5e28f4dfddb8c56b14e243d6ff08cd8c2a
fetched_at: '2026-06-29T00:06:27.861486+00:00'
page_id: '233736409'
product: rm
source: tdn-rm
title: DT_PCREQ-7807_Integ. BackOffice RM x SigaLoja - RM - Local de Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PCREQ-7807_Integ.+BackOffice+RM+x+SigaLoja+-+RM+-+Local+de+Estoque
version: 121
---

# Integração BackOffice RM x SigaLoja - RM - Local de Estoque

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  |  | | --- | --- | --- | | **Rotina** | **Nome Técnico** | **Mensagem Única TOTVS** | | Locais de Estoque | EstLocAction | Warehouse (1.000) |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Configuração da Integração | ConConfiguraIntegracaoAction | | Integrações de Mensagem Única. | ConIntegracaoAction | | De-Para | ConIntegracaoIdAction | |
| **Cadastros Iniciais:** | Cadastrar Filial no De-Para da Integração. |
| **Parâmetro(s):** | N/A. |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Estoque, Compras e Faturamento \ Locais de Estoque. |
| **Chamados Relacionados** | N/A. |
| **Requisito (ISSUE):** | PCREQ-7807 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE. |
| **Tabelas Utilizadas:** | * TLOC- Locais de Estoque |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Este requisito tem por objetivo possibilitar a integração do cadastro de Locais de Estoque com o PDV PROTHEUS através do protocolo de Mensagem Única TOTVS.

Para maiores detalhes sobre a integração de Local de Estoque, acesse a Especificações de Requisitos .

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No módulo de **Integração**, acesse **Ferramentas/Configurar**. Informe **Usuário/Senha** do banco de dados, teste a conexão. Avance até a **Projetos de Integração** e selecione o item **BackOffice RM x PDV Protheus (Novo Modelo)** e execute o processo.
2. Acesse **Integração/Mensagem Única/Integrações**, selecione a opção de filtro. Na visão de **Integrações** editar a integração de **Identificador 1016** e verifique se está informado a **URL WebService** do Protheus.
3. Verifique em **Anexos/Mapeamento de Entidades** se a mensagem **Warehouse** **versão 1.000** está mapeada.

**IMPORTAÇÃO DE FÓRMULA VISUAL**

1. Acesse **Gestão\Fórmula Visual\Fórmula visual\Processo\Importação de Fórmula Visual.** Clique em **Adicionar Objetos** e localize o arquivo a ser importado que encontra-se disponível na pasta **Fórmulas Visuais**, interna à pasta **ObjetosGerencias** no ambiente instalado do sistema (**../CorporeRM/ObjetosGerencias/Fórmulas Visuais**). Deverá ser marcado o parâmetro **Importar Gatilho**.
2. Visando oferecer facilidade para clientes que já possuam a base de dados com Locais de Estoque, foi disponibilizado também uma Fórmula Visual para sincronização dos registros existentes, que é responsável por filtrar somente os registros não enviados ou desatualizados no Protheus. Esta fórmula visual pode ser utilizada para carga inicial, novo sincronismo em casos onde o gatilho tenha sido desabilitado ou como forma de integração assíncrona.

## Procedimento para Utilização

1. No módulo **Gestão de Estoque, Compras e Faturament****o**, acesse **Cadastros/Estoque, Compras e Faturamento/Locais de Estoque** e selecione um filtro.

O sistema apresenta a janela de Locais de Estoque cadastrados.

2. Na visão clique em **Incluir**.

O sistema apresenta a janela de edição Locais de Estoque. Informe a  **Filial, Estoque** (código)e a **Descrição**.

4. Confira os dados e confirme.

divs
