---
content_hash: 04a366c6fdc61714c0da9e15cec65e8b9ce852abedbac6b3179b2d473ed06ce0
fetched_at: '2026-06-29T00:06:21.844005+00:00'
page_id: '223182523'
product: rm
source: tdn-rm
title: DT_PCREQ-8782_Integração de Funcionários que não batem ponto e de Rescisão
  com o TSA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223182523
version: 120
---

# Integração de Funcionários que não batem ponto e de Rescisão com o TSA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Integração TOTVS Automação de Ponto x TSA* | *Integração TOTVS Automação de Ponto x TSA* | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Chamados Relacionados** | TSSNNE, TSYZGJ |
| **Requisito (ISSUE):** |  |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |
| **Versões/Release:** | *11.82.42, 12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** | *11.82.42, 12.1.9* |

## Descrição

#### Integração de funcionários que não utilizam ponto

Foi feita uma evolução na integração de funcionários do RM. A partir de agora, qualquer alteração de campo integrado do cadastro de funcionários irá enviar as informações atualizadas para o TSA.

Portanto um novo campo passa a ser informado ao webservice do TSA, para que ele saiba se o funcionário bate ou não bate ponto.

Ao enviar as informações do funcionário, o Chronus irá fazer o mapeamento através do campo **exceptionREP**. Se o funcionário não bater ponto, será definido como verdadeiro, caso contrário, será definido como falso.

#### Integração de rescisão dos funcionários

A partir de agora, toda vez que uma rescisão for cadastrada, alterada cancelada  para um funcionário, as informações do funcionário serão enviadas para o TSA.

Se um funcionário estiver demitido no RM, também estará demitido no TSA, assim como se ele tiver ativo no RM, estará ativo no TSA.

Portanto três novos processos passaram a ser considerados:

* Cadastro da rescisão: Para o cadastro de rescisão, foi feita uma evolução na fórmula visual **Funcionário - TSA**, adicionando o gatilho para o DataServer "**FopRescisaoData"**:
* Rescisão coletiva: Para a rescisão coletiva, foi colocado um gatilho interno no código, que chamará a fórmula visual **Funcionário - TSA** após a conclusão do processo, enviando as informações de todos os funcionários impactados.
* Cancelamento da rescisão: Para o cancelamento da rescisão, foi colocado um gatilho interno no código, que chamará a fórmula visual **Funcionário - TSA** após a conclusão do processo, enviando as informações de todos os funcionários impactados.

Como a fórmula visual **Funcionário - TSA** foi atualizada, o pacote que contém as fórmulas visuais **"Formulas\_Visuais\_TSA.TotvsWF"** também foi atualizado e disponibilizado junto a biblioteca RM, na pasta "ObjetosGerenciais/Fórmulas Visuais", sendo necessária uma nova importação por parte dos clientes para atualização do ambiente.

## Procedimento para Implantação

* Caso o cliente não tenha integração com o TSA, seguir o procedimento de implantação padrão da integração.
* Caso o cliente já esteja integrado com o TSA:
  + Deverá excluir a fórmula visual antiga **Funcionário - TSA**.
  + Deverá executar novamente a importação do pacote **Formulas\_Visuais\_TSA.TotvsWF**, e importar a fórmula visual****Funcionário - TSA**** com todos os gatilhos.

divs
