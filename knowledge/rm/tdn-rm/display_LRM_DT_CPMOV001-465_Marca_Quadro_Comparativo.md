---
content_hash: a6c260fcdfa3324566f375fd162a7041940bf425d2368dda32c6ec5dc176e81b
fetched_at: '2026-06-29T00:08:21.029392+00:00'
page_id: '268808869'
product: rm
source: tdn-rm
title: DT_CPMOV001-465_Marca_Quadro_Comparativo
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-465_Marca_Quadro_Comparativo
version: 114
---

# MARCA NO QUADRO COMPARATIVO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Quadro Comparativo | CmpQuadroComparativoAction |        |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cotação | CmpCotacaoAction | |
| **Cadastros Iniciais:** | Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao) |
| **Parâmetro(s):** | Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao) |
| **Ponto de Entrada:** | Não se aplica. |
| **Chamados Relacionados** | Não se aplica. |
| **Requisito (ISSUE):** | CPMOV001-465. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | Não se aplica. |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Permitir que o comprador possa visualizar a Marca Negociada no Quadro Comparativo.

## Procedimento para Configuração

Consultar procedimentos para configuração no documento [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao)

## Procedimento para Utilização

### **Cadastro de Marca e Vinculo de Marcas ao Produto**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca)

### Solicitações**de Compras com Item de Movimento usando marca.**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca\_Movimento](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Movimento)

**Marca no Quadro Comparativo**

O Quadro Comparativo fica disponível na Cotação após a execução do processo **Calcular Quadro Comparativo** e também quando a Cotação está com status **Negociação da Melhor Oferta**. O procedimento de utilização abaixo será realizado para quando status da cotação for Negociação da Melhor Oferta.

1. Na visão de Cotação selecione um registro com status igual a Negociação da Melhor Oferta e clique em Editar.
   1. O sistema apresenta a janela de edição da Cotação.
2. Na janela edição de Cotação acesse **Quadro Comparativo** na barra de funções.
   1. O sistema apresenta a pasta Quadro Comparativo. A **Marca Negociada** será apresentada na coluna após a unidade de medida do produto.
   2. Execute o comando ***Ctrl + clique.*** O sistema irá apresentar a janela de **Item Detalhado** onde será permitido visualizar as marcas solicitada e negociada para o produto.
   3. Na pasta **Últimas Compras** será exibida a marca das movimentações do tipo 1.2.XX

divs
