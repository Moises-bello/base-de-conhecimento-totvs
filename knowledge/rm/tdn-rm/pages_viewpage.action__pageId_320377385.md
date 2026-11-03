---
content_hash: bb13f1d10ccc005146bf6abd63179879b73a22b0f5207f39d4c16f240f986ccf
fetched_at: '2026-06-29T00:08:47.801368+00:00'
page_id: '320377385'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-1009 DT Geração de movimento de NFS-e utilizando percentual
  de dedução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320377385
version: 5
---

# GERAÇÃO DE MOVIMENTOS UTILIZANDO PERCENTUAL DE DEDUÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Movimentos por Competência e por Regime de Caixa* | **Geração de Movimentos por Competência e por Regime de Caixa** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Geração de Movimento por Competência** | ***Geração de Movimento por Competência*** | | **Geração de Movimento por Caixa (Boleto)** | **Geração de Movimento por Caixa** | |
| **Cadastros Iniciais:** | *Tipo de Movimento, Contrato, Parcelas, Bolsas* |
| **Parâmetro(s):** | ***Parâmetro do TOTVS Educacional**: "Usar campo dedução para informar valor de desconto no item de movimento" em "Assistente de Implantação → TOTVS Educacional → Integração → Fiscal 2/2"*  ****Parâmetro do TOTVS Gestão Fiscal**:** "Dedução" do tipo de movimento disponível em "TOTVS Gestão de Estoque, Compras e Faturamento → Vendas → Tipo de Movimento XXX → Item - Valores Financeiros 2/2" |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *DEDUINTEGRACOES-1009, DEDUINTEGRACOES-1221* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *TMOV, TITMMOV, SCONTRATO, SPARCELA, SBOLSAALUNO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Criação do parâmetro "Usar campo dedução para informar valor de desconto no item de movimento" em "Assistente de Implantação → TOTVS Educacional → Integração → Fiscal 2/2".

Na configuração desse novo parâmetro na geração de movimento os valores de bolsas e descontos INCONDICIONAIS serão gravados no campo "Percentual Deduzido" conforme configuração do parâmetro "Dedução" no tipo de movimento usado na geração do movimento. E o somatório dos valores deduzidos serão gravados no campo "Dedução de ISS" na aba "Fiscal" do movimento.

Somente os tipos de movimentos configurados com "Usar Percentual" no parâmetro "Dedução" ficaram disponíveis para o usuário selecionar na geração de movimento via TOTVS Educacional, quando o parâmetro "Usar campo dedução para informar valor de desconto no item de movimento" estiver marcado

## Procedimento para Utilização

       1.            No TOTVS Educacional, marcar o parâmetro "Usar campo dedução para informar valor de desconto no item de movimento" em "TOTVS Educacional → Integração → Fiscal 2/2"  
       2.            No TOTVS Gestão Fiscal, escolher a opção "Usar Percentual" do parâmetro "Dedução" do tipo de movimento disponível em "TOTVS Gestão de Estoque, Compras e Faturamento → Vendas → Tipo de Movimento XXX → Item - Valores Financeiros 2/2"

       3.            Gerar movimento por competência ou por regime de caixa

       4.            Após a geração de movimentos, o campo "Percentual Deduzido" do item de movimento e o campo "Dedução de ISS" do movimento conterão respectivamente o percentual e o somatório dos valores de descontos incondicionais dos itens de movimento.

**OBSERVAÇÃO**:

     Dúvidas sobre os processos de Geração de Movimentos poderão ser encontrados nos links abaixo:

[http://tdn.totvs.com.br/pages/releaseview.action?pageId=4815200  
http://tdn.totvs.com.br/pages/viewpage.action?pageId=66617411](http://tdn.totvs.com.br/pages/viewpage.action?pageId=66617411)<http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.nfe.aspx><http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.notaFiscalEletronicaporcompetencia.aspx>

## Vídeo

500500
