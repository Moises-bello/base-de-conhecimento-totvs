---
content_hash: 0a92fe26a32e89bff3e31b47806ef396f7bf99444f853c9559497b29ab62c872
fetched_at: '2026-06-29T00:06:24.385690+00:00'
page_id: '224117757'
product: rm
source: tdn-rm
title: TTVHEA_DT_Faturamento_Parcial_Automatico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVHEA_DT_Faturamento_Parcial_Automatico
version: 126
---

# Faturamento Parcial Automático

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Faturamento de Movimento* | *Informe o nome técnico da rotina.* | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *Opções de Faturamento: TTMV.GERAMOVAUTOPED Marcar os itens que farão parte do movimento gerado: TTMV.MARCARITENSFATPED* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *TMOV, TITMMOV, TMOVRELAC e TITMMOVRELAC* |
| **Sistema(s) Operacional(is):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

## Descrição

O Objetivo desta implementação é permitir o faturamento parcial do movimento de forma automática, esta opção estará disponível tanto no processo de faturamento quando na chamada do mesmo através de WebService.

**Restrições**:

O faturamento automático parcial  não pode ser executado quando se utiliza agrupamento.

## Parametrização:

O campo Opção de Faturamento deverá ser preenchido com uma das opções de Faturamento Automático, ex:

O Campo Marcar os itens que farão parte do movimento gerado deverá estar marcado.

## Execução do Processo:

Durante o processo de faturamento, será exibida uma tela onde o usuário poderá selecionar os itens que farão parte do faturamento, assim como alterar a quantidade de cada um dos itens.

Durante a execução do processo, o sistema verifica as informações preenchidas nesta tela e aplica o faturamento parcial.

**Importante**:

* Apenas os campos [ X] e Quantidade podem ser alterados.
* Caso algum Item não seja selecionado, o mesmo não será faturado.

## Utilização do WebService:

Este recurso está disponível também através de WebService, segue abaixo um exemplo de utilização do mesmo:

**Nome do Processo:** MovFaturamentoProc  
**XML's exemplo:**

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
         <TipoFaturamento>0</TipoFaturamento>  
         <dataBase>2016-02-01T00:00:00-02:00</dataBase>  
         <dataEmissao/>  
         <dataSaida/>  
         <efeitoPedidoFatAutomatico>2</efeitoPedidoFatAutomatico>  
        **<listaMovItemFatAutomatico>**  
 **<MovItemFatAutomatico>**  
 **<CodColigada>1</CodColigada>**  
 **<Checked>1</Checked>**  
 **<IdMov>3074</IdMov>**  
 **<NSeqItmMov>1</NSeqItmMov>**  
 **<Quantidade>0,5</Quantidade>**  
**</MovItemFatAutomatico>**  
**<MovItemFatAutomatico>**  
 **<CodColigada>1</CodColigada>**  
 **<Checked>1</Checked>**  
 **<IdMov>3074</IdMov>**  
 **<NSeqItmMov>2</NSeqItmMov>**  
 **<Quantidade>0,5</Quantidade>**  
 **</MovItemFatAutomatico>**  
         </listaMovItemFatAutomatico>  
         <numeroMov></numeroMov>  
         <realizaBaixaPedido>true</realizaBaixaPedido>  
     </movCopiaFatPar>  
</MovFaturamentoProcParams>

**Importante:** As informações em Negrito se referem aos itens do movimento, caso seja atribuído o valor 1 a TAG "Checked", o sistema considera que aquele item será faturado e, a quantidade utilizada será a informada através da TAG "Quantidade".

**Informando os Lotes a serem faturados (Disponível apenas através de WEBService):**

<![CDATA[   
 <MovFaturamentoProcParams>  
     <movCopiaFatPar>  
         <CodColigada>1</CodColigada>  
         <CodSistema>T</CodSistema>  
         <CodTmvDestino>1.1.08</CodTmvDestino>  
         <CodTmvOrigem>1.1.06</CodTmvOrigem>  
         <CodUsuario>mestre</CodUsuario>  
         <GrupoFaturamento></GrupoFaturamento>  
         <IdExercicioFiscal>22</IdExercicioFiscal>  
         <IdMov>  
             <int>5132</int>  
         </IdMov>  
         <TipoFaturamento>0</TipoFaturamento>  
         <dataBase>2016-02-01T00:00:00-02:00</dataBase>  
         <dataEmissao/>  
         <dataSaida/>  
         <efeitoPedidoFatAutomatico>2</efeitoPedidoFatAutomatico>  
         <listaMovItemFatAutomatico>  
             <MovItemFatAutomatico>  
                 <CodColigada>1</CodColigada>  
                 <Checked>1</Checked>  
                 <IdMov>5132</IdMov>  
                 <NSeqItmMov>5</NSeqItmMov>  
                 <Quantidade>3</Quantidade>  
                 **<listaItemLote>**  
 **<MovItemLoteFatAutomatico>**  
 **<CodColigada>1</CodColigada>**  
 **<IdMov>5132</IdMov>**  
 **<NSeqItmMov>5</NSeqItmMov>**  
 **<IdLote>140</IdLote>**   
 **<Quantidade>3</Quantidade>**   
 **</MovItemLoteFatAutomatico>**  
 **</listaItemLote>**  
             </MovItemFatAutomatico>   
         </listaMovItemFatAutomatico>  
         <numeroMov></numeroMov>  
         <realizaBaixaPedido>true</realizaBaixaPedido>  
    </movCopiaFatPar>  
 </MovFaturamentoProcParams>]]>

**Informando Número de Série **(Disponível apenas através de WEBService)**:**

<![CDATA[   
 <MovFaturamentoProcParams>  
     <movCopiaFatPar>  
         <CodColigada>1</CodColigada>  
         <CodSistema>T</CodSistema>  
         <CodTmvDestino>1.1.08</CodTmvDestino>  
         <CodTmvOrigem>1.1.06</CodTmvOrigem>  
         <CodUsuario>mestre</CodUsuario>  
         <GrupoFaturamento></GrupoFaturamento>  
         <IdExercicioFiscal>22</IdExercicioFiscal>  
         <IdMov>  
             <int>5142</int>  
         </IdMov>  
         <TipoFaturamento>0</TipoFaturamento>  
         <dataBase>2016-02-01T00:00:00-02:00</dataBase>  
         <dataEmissao/>  
         <dataSaida/>  
         <efeitoPedidoFatAutomatico>2</efeitoPedidoFatAutomatico>  
         <listaMovItemFatAutomatico>  
         <MovItemFatAutomatico>  
             <CodColigada>1</CodColigada>  
             <Checked>1</Checked>  
             <IdMov>5142</IdMov>  
             <NSeqItmMov>1</NSeqItmMov>  
             <Quantidade>3</Quantidade>  
           **<listaNumSerie>**  
**<MovItemNumSerieFatAutomatico>**

**<CodColigada>1</CodColigada>**  
 **<IdMov>5142</IdMov>**  
 **<NSeqItmMov>1</NSeqItmMov>**  
 **<IdPrd>39</IdPrd>**   
 **<NumSerie>0777</NumSerie>**  
 **</MovItemNumSerieFatAutomatico>**  
 **<MovItemNumSerieFatAutomatico>**  
 **<CodColigada>1</CodColigada>**  
 **<IdMov>5142</IdMov>**  
 **<NSeqItmMov>1</NSeqItmMov>**  
 **<IdPrd>39</IdPrd>**   
 **<NumSerie>0888</NumSerie>**  
 **</MovItemNumSerieFatAutomatico>**  
 **<MovItemNumSerieFatAutomatico>**  
 **<CodColigada>1</CodColigada>**  
 **<IdMov>5142</IdMov>**  
 **<NSeqItmMov>1</NSeqItmMov>**  
 **<IdPrd>39</IdPrd>**   
 **<NumSerie>0999</NumSerie>**  
 **</MovItemNumSerieFatAutomatico>**  
 **</listaNumSerie>**  
         </MovItemFatAutomatico>   
         </listaMovItemFatAutomatico>  
         <numeroMov></numeroMov>  
         <realizaBaixaPedido>true</realizaBaixaPedido>  
     </movCopiaFatPar>  
 </MovFaturamentoProcParams>]]>

divs
