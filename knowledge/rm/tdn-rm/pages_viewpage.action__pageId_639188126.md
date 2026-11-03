---
content_hash: 250cdf23af7d5928c9d28f6d75804449ec2460c1fa6c0e5aefebec91697a8c77
fetched_at: '2026-06-29T00:11:07.084231+00:00'
page_id: '639188126'
product: rm
source: tdn-rm
title: FISCAL01-16569 - DT DMA-BA - QUADRO 01 - INSCRIÇÃO ESTADUAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=639188126
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DMA-BA |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16569 |

## **02. SITUAÇÃO/REQUISITO**

Implementar o QUADRO 01 - INSCRIÇÃO ESTADUAL

## **03. SOLUÇÃO**

Origem dos Dados:  
Tela de Geração e Cadastro da Filial

Quadro 00:

TipoRegistro             00  
Doc\_Entregue           DMA  
Meio\_Magnetico      'O'  
CPF\_Responsavel     CPF - Representante Legal da Filial  
Nome\_Responsavel Nome - Representante Legal da Filial  
AnoVersao               2010  
  
Quadro 01:

TipoRegistro                  01  
AnoReferencia               Ano Base - Data Inicial da Geração  
MesReferencia               Mes Base - Data Inicial da Geração  
InscricaoEstadual          INSCRICAOESTADUAL da Filial  
DMARetificadora          Motivo Preenchimento - Retificadora - Tela  
MotivoBaixa                 Motivo Preenchimento - Motivo Baixa - Tela  
ContribuinteInscUnica Preenchimento CS DMA - Regime Especial/Inscrição Única/Atividade Transporte - Tela  
MudouCondicao          Motivo Preenchimento - Mudança Condição - Tela  
DataBalanco                 DATA ENCERRAMENTO BALANCO - Tela  
RazaoSocial                  Nome da Filial  
CodigoMunicipio          CODMUNICIPIO da Filial  
CodigoAtivEconomica CODATIVIDPRINC da Filial  
CodigoInspetoria         CODIGO INSPETORIA Fazendária - Tela  
ConsolidacaoAnual       Motivo Preenchimento - Consolidada - Tela
