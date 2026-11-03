---
content_hash: 6484e00656dab761b15d11faec1da63a7e6414180b25e298b244d66268c26ef4
fetched_at: '2026-06-29T00:06:27.914564+00:00'
page_id: '233737593'
product: rm
source: tdn-rm
title: DT_PCREQ-7809_Integ. BackOffice RM x SigaLoja - RM - Administradoras Financeiras
  / Forma Pagto.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233737593
version: 120
---

# Integração BackOffice RM x SigaLoja - RM - Administradoras Financeiras / Forma Pagamento.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  |  | | --- | --- | --- | | **Rotina** | **Nome Técnico** | **Mensagem Única TOTVS** | | Meio Pagamento | MovFormaPagtoAction. | PaymentMethod (1.000) |        |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Configuração da Integração | ConConfiguraIntegracaoAction | | Integrações de Mensagem Única. | ConIntegracaoAction | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | N/A. |
| **Ponto de Entrada:** | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \  Mais \ Tabelas Auxiliares \ Meio Pagamento |
| **Chamados Relacionados** | N/A. |
| **Requisito (ISSUE):** | PCREQ-7809 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL SERVER, ORACLE. |
| **Tabelas Utilizadas:** | * TFORMAPAGTO – Meio de Pagamento |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Este requisito tem por objetivo possibilitar a integração do cadastro de Meio de Pagamento com o PDV PROTHEUS através do protocolo de Mensagem Única TOTVS.

A Administradora Financeira não será integrada. Ela deverá ser cadastrada no Protheus e ao cadastrá-la deve-se configurar as informações com PinPad e Forma de Pagamento. Para maiores detalhes sobre a integração, acesse a .

## Procedimento para Configuração

**CONFIGURAÇÃO DE INTEGRAÇÃO**

1. No módulo de **Integração**, acesse **Ferramentas/Configurar**. Informe **Usuário/Senha** do banco de dados, teste a conexão. Avance até a **Projetos de Integração** e selecione o item **BackOffice RM x PDV Protheus (Novo Modelo)** e execute o processo.
2. Acesse **Integração/Mensagem Única/Integrações**, selecione a opção de filtro. Na visão de **Integrações** editar a integração de **Identificador 1016** e verifique se está informado a **URL WebService** do Protheus.
3. Verifique em **Anexos/Mapeamento de Entidades** se a mensagem **PaymentMethod versão 1.000** está mapeada.

**IMPORTAÇÃO DE FÓRMULA VISUAL**

1. Acesse **Gestão\Fórmula Visual\Fórmula visual\Processo\Importação de Fórmula Visual.** Clique em **Adicionar Objetos** e localize o arquivo a ser importado que encontra-se disponível na pasta **Fórmulas Visuais**, interna à pasta **ObjetosGerencias** no ambiente instalado do sistema (**../CorporeRM/ObjetosGerencias/Fórmulas Visuais**). Deverá ser marcado o parâmetro **Importar Gatilho**.
2. Visando oferecer facilidade para clientes que já possuam a base de dados com Meios de Pagamento, foi disponibilizado também uma Fórmula Visual para sincronização dos registros existentes, que é responsável por filtrar somente os registros não enviados ou desatualizados no Protheus. Esta fórmula visual pode ser utilizada para carga inicial, novo sincronismo em casos onde o gatilho tenha sido desabilitado ou como forma de integração assíncrona.

## Procedimento para Utilização

1. No módulo **Gestão de Estoque, Compras e Faturament****o**, acesse **Cadastros/Estoque, Compras e Faturamento/Mais/Tabelas Auxiliares/Meio de Pagamento** e selecione um filtro.

O sistema apresenta a janela de **Meios de Pagamento** com os registros cadastrados.

2. Na visão clique em **Incluir**.

O sistema apresenta a janela de edição **Meios de Pagamento**. Informe o **Código,****Descrição** e selecione o **Tipo Primitivo.** Quando selecionar **Tipo Primitivo Cartão**, na pasta **Cartão de Crédito/Débito** selecione o **Tipo de Transação**.

4. Confira os dados e confirme.

divs
