---
content_hash: cc6bd8e3d1778cbf9ac79812ff92f16a8d1f1b319f2dcc2639d405c63efa820d
fetched_at: '2026-06-29T00:08:20.776878+00:00'
page_id: '268588290'
product: rm
source: tdn-rm
title: DT_CPMOV001-461_Marca_Assistente_Inclusao_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CPMOV001-461_Marca_Assistente_Inclusao_Cotacao
version: 112
---

# TRATAMENTO DE MARCA NO ASSISTENTE DE INCLUSÃO COTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Assistente de Cotação | CmpAssistenteCotacaoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cotação | CmpCotacaoAction | |
| **Cadastros Iniciais:** | *Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao)* |
| **Parâmetro(s):** | *Consultar documento: [DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao)* |
| **Ponto de Entrada:** | Não se aplica. |
| **Chamados Relacionados** | Não se aplica. |
| **Requisito (ISSUE):** | CPMOV001-461. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | Oracle ou SQL Server. |
| **Tabelas Utilizadas:** | TCCOTACAOITMMOV - Itens de Movimento Cotados. |
| **Sistema(s) Operacional(is):** | Windows 7 SP1 ou superior. |

## Descrição

Permitir que o comprador possa definir se o fornecedor poderá realizar a troca de marca de produtos na cotação.

## Procedimento para Configuração

Consultar procedimentos para configuração no documento *[DT\_CPMOV001-452\_Marca\_Cotacao](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Cotacao)*

## Procedimento para Utilização

**Cadastro de Marca e Vinculo de Marcas ao Produto**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca)

### Solicitações**de Compras com Item de Movimento usando marca.**

1. Consulte o documento técnico: [DT\_CPMOV001-452\_Marca\_Movimento](http://tdn.totvs.com/display/LRM/DT_CPMOV001-452_Marca_Movimento)

### **Incluir Cotação.**

1. No módulo Gestão de Estoque, Compras e Faturamento acesse **Compras / Cotação.**  
   O sistema apresenta a janela de Filtros - Cotação - Composição.
2. Selecione um filtro clique em Executar.
3. Na visão de Cotação clique em Incluir  
   O sistema apresenta a janela de Assistente de Cotação.
4. No passo **Filtro de Produto**, clique em Incluir  
   O sistema apresenta a janela de pesquisa de itens de solicitação de compras.
5. Após a escolha dos produtos será apresentado no grid a coluna **Permite Forn. trocar Marcas.** Por padrão esta coluna será apresentada marcada quando o sistema estiver configurado para **Usar Marca de Produto na Cotação**e o comprador possuir permissão para **Permite trocar marca dos produtos na cotação.** A coluna **Permite Forn. trocar Marcas** poderá ser desmarcada, no exemplo abaixo foi desmarcado para o produto 10.50.
6. Após o preenchimento dos demais passos, execute o Assistente para conclusão da inclusão da cotação.

**Editar Cotação.**

Caso o usuário deseje alterar a permissão do fornecedor para trocar marca do produto, ele poderá executar esta alteração através da janela de edição da Cotação na pasta Itens de Movimento.

1. No módulo Gestão de Estoque, Compras e Faturamento acesse **Compras / Cotação.**  
   O sistema apresenta a janela de Filtros - Cotação - Composição.
2. Selecione um filtro clique em Executar.
3. Na visão de Cotação clique em Editar  
   O sistema apresenta a janela de edição da Cotação.
4. Na pasta **Itens de Movimento selecione** o(s) item(ns) que serão ajustados e clique em ****Permite Forn. trocar Marcas**.**Os produtos que estão marcados ficarão desmarcados e os desmarcados ficarão marcados.

divs
