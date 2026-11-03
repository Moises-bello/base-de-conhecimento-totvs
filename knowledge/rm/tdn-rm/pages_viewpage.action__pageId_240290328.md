---
content_hash: e155af4d4eb7bcccc1cbef24fcc6c089c7add0aeb34e090acfc9a7e83e8aaf49
fetched_at: '2026-06-29T00:08:09.844891+00:00'
page_id: '240290328'
product: rm
source: tdn-rm
title: TUWEL5_DT_Alterar_Lancamento_Financeiro_Através_de_Conceito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240290328
version: 124
---

## ALTERAR LANÇAMENTO FINANCEIRO ATRAVÉS DA IMPORTAÇÃO DE MOVIMENTO VIA CONCEITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Alterar Lançamento Financeiro através de Conceito* | *MovMovImportacao* | |
| **Cadastros Iniciais:** | Gerador de Saídas e Conceito |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *FLAN* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

O objetivo desta implementação é fazer com que a rotina responsável pela inclusão de movimento através de conceito permita alterar os lançamentos financeiros de acordo com os dados de um arquivo TXT. Com base no Layout de Exportação do Movimento(Gerador de Saídas), foi desenvolvida via conceito a possibilidade de alterar os lançamentos financeiros após a inclusão do movimento.

**Parametrização**

* O tipo de movimento deve utilizar um meio de pagamento que gere lançamento financeiro.

## Exemplo de uso:

1 - Apos incluir um movimento com lançamento financeiro, acesse o modulo Integração >> Gerador de Saídas >> Layouts

2 - Selecione o Layout >> Processos >> Geração de Saídas (filtrando o movimento criado anteriormente)

* Após a execução com sucesso, o arquivo TXT será criado dentro do diretório C:\totvs\CorporeRM\RM.Net\Saidas

3 - Acesse o modulo Integração >> Conceito

4 - Selecione o Layout >> Processos >> Processar novo conceito

5 - Selecione o parâmetro "Atualizar Movimento Cadastrado"

6 - Informar o arquivo para execução do conceito (Arquivo gerado através do gerador de saídas)

* Após a execução com sucesso, todos os campos passiveis de alteração do movimento serão atualizados, inclusive os lançamentos financeiros identificado com a letra "L" dentro do arquivo TXT

Campos passíveis de alteração do lançamento financeiro via conceito:

DATAVENCIMENTO  
DATAPREVBAIXA  
HISTORICO  
VALORORIGINAL  
VALOROP1  
VALOROP2  
VALOROP3  
VALOROP4  
VALOROP5  
VALOROP6  
VALOROP7  
VALOROP8  
SEGUNDONUMERO  
DATAOP1  
DATAOP2  
DATAOP3  
CNABCOMANDO  
CNABACEITE  
CNABINSTRUCAOCOD1  
CNABINSTRUCAOCOD2  
CNABNOSSONUMERO  
CNABSTATUS  
CAMPOALFAOP1  
CAMPOALFAOP2  
CAMPOALFAOP3  
CODIGOBARRA  
CONVENIO

## 

divs
