---
content_hash: 3aa6b0f2d671ea798a23f314b49c260184899dda7f482a3aae48582567d98a80
fetched_at: '2026-06-29T00:08:21.048386+00:00'
page_id: '268809888'
product: rm
source: tdn-rm
title: DT_CPMOV001-732_Marca_Interferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-732_Marca_Interferencia
version: 114
---

# MARCA NA INTERFERÊNCIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Interferência | CmpQuadroComparativoAction |        |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cotação | CmpCotacaoAction | |
| **Cadastros Iniciais:** | Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao) |
| **Parâmetro(s):** | Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao) |
| **Ponto de Entrada:** | Não se aplica. |
| **Chamados Relacionados** | Não se aplica. |
| **Requisito (ISSUE):** | CPMOV001-732. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | Não se aplica. |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Permitir que o comprador possa visualizar a Marca Negociada na Interferência.

## Procedimento para Configuração

Consultar procedimentos para configuração no documento [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao)

## Procedimento para Utilização

### **Cadastro de Marca e Vinculo de Marcas ao Produto**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca)

### Solicitações**de Compras com Item de Movimento usando marca.**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca\_Movimento](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Movimento)

**Marca na Interferência por Fornecedor**

A **Interferência por Fornecedor** e acessada através do **Quadro Comparativo.**O procedimento de utilização abaixo será realizado para quando status da cotação for Negociação da Melhor Oferta.

1. Na visão de Cotação selecione um registro com status igual a Negociação da Melhor Oferta e clique em Editar.
   1. O sistema apresenta a janela de edição da Cotação.
2. Na janela edição de Cotação acesse **Quadro Comparativo** na barra de funções.
   1. O sistema apresenta a pasta Quadro Comparativo.
3. Na pasta Quadro Comparativo clique em **Interferência \ Fornecedor**
   1. O sistema apresenta a janela de **Interferência**.
4. Na janela de **Interferência**, selecione um Cliente / Fornecedor.
   1. O sistema apresenta os Produtos do Cliente / Fornecedor e a **Marca Negociada** é exibida após a coluna **Nome do Produto.**
   2. Caso a **Marca Negociada** não esteja visível, clique em **Configurar colunas** e marque a opção **Restaurar configuração padrão.**Lembre-se este campo ficará disponível somente se a Cotação Usar Marca.

**Marca na Interferência por Produto**

A **Interferência por Produto**e acessada através do **Quadro Comparativo.** Este tipo de Interferência fica disponível quando **Tipo de Julgamento da Melhor Oferta** **for diferente de Global**. O procedimento de utilização abaixo será realizado para quando status da cotação for Negociação da Melhor Oferta e Tipo de Julgamento da Melhor Oferta diferente de Global.

1. Na visão de Cotação selecione um registro com status igual a Negociação da Melhor Oferta e clique em Editar.
   1. O sistema apresenta a janela de edição da Cotação.
2. Na janela edição de Cotação acesse **Quadro Comparativo** na barra de funções.
   1. O sistema apresenta a pasta Quadro Comparativo.
3. Na pasta Quadro Comparativo clique em **Interferência \ Produto**ou clique duas vezes sobre grid.
   1. O sistema apresenta a janela de **Interferência** e a ****Marca Negociada****é exibida após a coluna ****Nome do Produto.****

divs
