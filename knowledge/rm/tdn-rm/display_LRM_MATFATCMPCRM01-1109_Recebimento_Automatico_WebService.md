---
content_hash: 0a410b7acad18f725bd2d89a779179ed424de023d5c65b644dc17f7e62fa847d
fetched_at: '2026-06-29T00:08:41.746031+00:00'
page_id: '286746862'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-1109_Recebimento_Automatico_WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-1109_Recebimento_Automatico_WebService
version: 101
---

# Recebimento Automático via WebService

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MovFaturamentoProc* | *Faturamento de Movimento* | |  |  | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *Opções de Faturamento: TTMV.GERAMOVAUTOPED Marcar os itens que farão parte do movimento gerado: TTMV.MARCARITENSFATPED* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-1109 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SqlServer e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

O Objetivo desta implementação é, permitir que alguns campos do movimento gerado sejam alterados durante processo de faturamento automático via WebService, segue a lista:

* Serie
* DataExtra1
* DataExtra2
* CodTipoDocumento
* ChaveAcessoNFe
* CodCondicaoPagamento
* Historico

**Exemplo de XML:**

<MovFaturamentoProcParams>  
    <movCopiaFatPar>  
        <CodColigada>1</CodColigada>  
        <CodSistema>T</CodSistema>  
        <CodTmvDestino>1.2.01</CodTmvDestino>  
        <CodTmvOrigem>1.1.03</CodTmvOrigem>  
        <CodUsuario>mestre</CodUsuario>  
        <GrupoFaturamento></GrupoFaturamento>  
        <IdExercicioFiscal>22</IdExercicioFiscal>  
        <IdMov>  
            <int>3074</int>  
        </IdMov>

**<Serie>001<Serie>**  
**<DataExtra1>2016-02-01T00:00:00-02:00<DataExtra1>**  
**<DataExtra2>2016-02-01T00:00:00-02:00<DataExtra2>**  
**<CodTipoDocumento>55<CodTipoDocumento>**  
**<ChaveAcessoNFe>42150653113791001790550350000200071000263660<ChaveAcessoNFe>**  
**<CodCondicaoPagamento>001<CodCondicaoPagamento>**  
**<Historico>Texto do Histórico<Historico>**

        <TipoFaturamento>0</TipoFaturamento>  
        <dataBase>2016-02-01T00:00:00-02:00</dataBase>  
        <dataEmissao/>  
        <dataSaida/>  
        <efeitoPedidoFatAutomatico>2</efeitoPedidoFatAutomatico>         
        <numeroMov></numeroMov>  
        <realizaBaixaPedido>true</realizaBaixaPedido>  
    </movCopiaFatPar>  
</MovFaturamentoProcParams>

Faturamento Parcial Automático: 

divs
