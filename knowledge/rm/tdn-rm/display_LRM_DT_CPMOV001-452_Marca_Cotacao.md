---
content_hash: 6ccfb17004e73461084efc9f11c72d5a711490f75d7d0bbcafdaef7835757a24
fetched_at: '2026-06-29T00:08:17.086757+00:00'
page_id: '253034834'
product: rm
source: tdn-rm
title: DT_CPMOV001-452_Marca_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao
version: 122
---

# MARCA NA COTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cotação | CmpCotacaoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Produto | EstPrdAction | | Parâmetros Gerais | RMSParamsWizardAction | | Cadastro de Marca | EstMarcaAction | | Marcas do Produto | EstPrdMarcaAction | | Item de Movimento | MovMovimentoAction | |
| **Cadastros Iniciais:** | Cadastrar marcas;  Vincular marcas ao produto.  Parametrizar tipo de movimento para usar marca.  Incluir itens em Solicitações de Compras que usam marca.  Parametrizar a cotação para Usar Marca. |
| **Parâmetro(s):** | Parâmetros Tabela de Marcas e Parâmetros de Cotação. |
| **Ponto de Entrada:** | Não se aplica. |
| **Chamados Relacionados** | Não se aplica. |
| **Requisito (ISSUE):** | CPMOV001-452 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | TPAR – Parâmetros Gerais  TITMTMV – Tipos de Movimento - Complemento  TCITMORCAMENTO – Itens de Orçamento  TITMMOV– Item de Movimento  TMARCA – Tabela de Marcas  TPRODUTODEF – Dados dos Produtos Globais por Coligada  TPRODUTODEFMARCA – Tabela de Produto x Marcas  TCPARAMETROS – Parâmetros da Cotação |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

 

Permitir que o usuário possa cadastrar marcas para um determinando produto, e no momento da cotação ter a possibilidade de utilizar escolher/trocar a marca do produto.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **BackOffice/Gestão de Estoque, Compras e Faturamento/Ambiente/Parâmetros/Gestão de Estoque, Compras e Faturamento**. Na janela de **Assistente de Implantação de Processos** acesse **Gestão de Compras/Cotação** selecione uma Filial e na **Etapa 2 – Definições Gerais** marque o parâmetro **Usar Marca de Produto na Cotação**:

**CONFIGURAÇÃO DE SEGURANÇA**

Para que o Comprador possa efetuar a troca de marca na cotação ao registrar orçamento/negociação, é preciso configurar a segurança. 

1. No RM acesse **Serviços Globais/Segurança/Perfis,** selecione o contexto **Gestão de Estoque, Compras e Faturamento.**Edite o perfil e em **[03] Compras/[03.01] Gestão de Compras/[03.01.02] Cotação** e permitir acesso à **[03.01.02.22] Permite Trocar Marca dos Produtos na Cotação**:

## Procedimento para Utilização

### **Cadastro de Marca e Vinculo de Marcas ao Produto**

1. Consulte o documento técnico:

### Solicitações**de Compras com Item de Movimento usando marca.**

1. Consulte o documento técnico:

### Substituição de Marca na Cotação

Quando o sistema for configurado para **Usar Marca de Produto na Cotação,** nas janelas de **Registrar Orçamento e Registrar Negociação**, pasta **Produtos** no grid de itens da cotação ficarão disponíveis os campos **Marca Solicitada**e **Marca Negociada.**

* **Marca Solicitada:** somente visualização, ou seja, não permite edição.
* **Marca Negociada:** permitirá edição quando o perfil do usuário possuir permissão para **Permite trocar marca dos produtos na cotação.**

**Substituição de Marca no Registro de Orçamento / Registro de Negociação**

1. Selecionar uma cotação com status igual a **Aguardando Resposta Fornecedores**  ou **Negociação da Melhor Oferta** clique em Editar  
   O sistema apresenta a janela de edição da Cotação:
2. Na pasta Orçamentos clique em Registrar Orçamento ou Registrar Negociação  
   O sistema apresenta a janela de registro de orçamento ou negociação do fornecedor selecionado.
3. Na pasta Produtos clique no campo Marca Negociada e selecione a marca.  
   Pode-se selecionar qualquer marca ativa que esteja vinculada ao produto.   
   Obs: O campo **Marca Negociada**  é único e será exibido em ambas as telas (**Registro de Orçamento e Registro de Negociação**). O mesmo se refere à coluna (**TCITMORCAMENTO.IDMARCANEG**) na base de dados.
4. Confira os dados e confirme.

divs
