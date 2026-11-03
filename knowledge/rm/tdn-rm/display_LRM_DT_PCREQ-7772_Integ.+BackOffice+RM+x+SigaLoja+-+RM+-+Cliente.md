---
content_hash: 4598d06e78df8f88f42f07e9b07b4d228136b3d3d5b7d683dcd7348b3c4ebd20
fetched_at: '2026-06-29T00:06:26.433563+00:00'
page_id: '225265152'
product: rm
source: tdn-rm
title: DT_PCREQ-7772_Integ. BackOffice RM x SigaLoja - RM - Cliente
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PCREQ-7772_Integ.+BackOffice+RM+x+SigaLoja+-+RM+-+Cliente
version: 120
---

# Integ. BackOffice RM x SigaLoja - RM - Cliente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  |  | | --- | --- | --- | | **Rotina** | **Nome Técnico** | **Mensagem Única TOTVS** | | Cliente/Fornecedor. | FinCFOAction. | CustomerVendor (2.002) |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Configuração da Integração | ConConfiguraIntegracaoAction | | Integrações de Mensagem Única. | ConIntegracaoAction | | Parâmetros de Integração | ConParametrosIntegracaoAction | | Classificação de País | FisClassifPaisAction | | País | FisPaisAction | |
| **Cadastros Iniciais:** | No cadastro de **Classificação de País** incluir uma tabela de classificação.  No cadastro de **País** abrir o anexo **Codificação de País** e incluir a tabela de classificação informando o **Código País.**  Executar o Assistente de Configuração de Integração.  Configurar a URL WebService do PROTHEUS no cadastro de Integração de Mensagem Única  Informar no parâmetro de integração qual será o código da tabela de Classificação de País. |
| **Parâmetro(s):** | Nos **Parâmetros de Integração** informar no parâmetro "**CODCLASSIFICPAIS**" o código da tabela de classificação utilizada e associado ao país. |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Financeiros \ Clientes / Fornecedores |
| **Chamados Relacionados** | N/A. |
| **Requisito (ISSUE):** | PCREQ-7772 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE |
| **Tabelas Utilizadas:** | * FCFO – Cadastro de Clientes / Fornecedor. * DCLASSIFPAIS - Classificação do País. * DPAIS - País segundo Classificação. * HCINTEGRACAOID – Tabela de-para dos identificadores de cada integração. * HCFILAMENSAGEM – Armazena dados da fila de mensageria única. * HCPARAMETROS - Parâmetros do RM Conector |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Este requisito tem por objetivo possibilitar a integração do cadastro de Cliente com o PDV PROTHEUS através do protocolo de Mensagem Única TOTVS.

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No módulo de **Gestão Fiscal**, acesse **Cadastros/Globais/Mais/Endereço/Classificação de País** inclue uma tabela de classificação.
2. No módulo de **Gestão de Estoque, Compras e Faturamento**, acesse **Cadastros/Fiscais/Mais/Países**. Acesse **Anexos/Codificação de País** e inclua a tabela de classificação definida no passo 1.
3. No módulo de **Integração**, acesse **Ferramentas/Configurar**. Informe **Usuário/Senha** do banco de dados, teste a conexão. Avance até a **Projetos de Integração** e selecione o item **BackOffice RM x PDV Protheus (Novo Modelo)** e execute o processo.
4. Acesse **Integração/Mensagem Única/Integrações**, selecione a opção de filtro. Na visão de **Integrações** editar a integração de **Identificador 1016** e informar a **URL WebService** do PROTHEUS.
5. Na visão de **Integrações** abrir o anexo **Parâmetros de Integração** e informar o **Valor** para o parâmetro **CODCLASSIFICPAIS.** Neste parâmetro deve-se informar  o código da tabela definido no passo 1 acima.

**IMPORTAÇÃO DE FÓRMULA VISUAL**

1. Acesse **Gestão\Fórmula Visual\Fórmula visual\Processo\Importação de Fórmula Visual.** Clique em **Adicionar Objetos** e localize o arquivo a ser importado que encontra-se disponível na pasta **Fórmulas Visuais**, interna à pasta **ObjetosGerencias** no ambiente instalado do sistema (**../CorporeRM/ObjetosGerencias/Fórmulas Visuais**). Deverá ser marcado o parâmetro **Importar Gatilho**.
2. Visando oferecer facilidade para clientes que já possuam a base de dados com Clientes/Fornecedores foi disponibilizado também uma Fórmula Visual para sincronização dos registros existentes, que é responsável por filtrar somente os registros não enviados ou desatualizados no Protheus. Esta fórmula visual pode ser utilizada para carga inicial, novo sincronismo em casos onde o gatilho tenha sido desabilitado ou como forma de integração assíncrona.

## Procedimento para Utilização

1. No **Gestão de Estoque, Compras e Faturamento**, acesse **Cadastros/Financeiros/Clientes / Fornecedores** e selecione um filtro.

O sistema apresenta a janela de clientes/fornecedores cadastrados.

       2. Na visão clique em **Incluir**.

O sistema apresenta a janela de edição Cliente/Fornecedor. Informe os dados solicitados. Serão integrados ao PDV Protheus, somente os registros cuja a **Classificação** seja igual a **Cliente** ou **Ambos.**

       3. Na pasta **Endereço** informe os dados de Endereço do Cliente.

Os dados de Endereço são obrigatórios para integração com o PDV Protheus.

       4. Confira os dados e confirme.

divs
