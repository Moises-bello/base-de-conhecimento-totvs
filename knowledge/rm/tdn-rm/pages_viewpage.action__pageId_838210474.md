---
content_hash: d466e13823204c28c2adec5083168c3e4022b0958b718684f6fd479d53de4e94
fetched_at: '2026-06-29T00:11:49.773413+00:00'
page_id: '838210474'
product: rm
source: tdn-rm
title: Folha de Produção de Prestadores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=838210474
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de Utilização**
3. **Filtro Prestador do Repasse**
4. **Configuração do Relatório**
5. **Tabelas Utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

A Folha de produção de prestadores consiste em listar todos os lançamentos com repasse, para o prestador informado. A funcionalidade consiste em diversos filtros para flexibilizar a localização dos repasses do **prestador que receberá os valores**.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

1. Acesse o menu **Faturamento > Gestão de Repasse > Outros > Folha de Produção Prestadores**

2. Informe o período e demais filtros e clique em **Visualizar.**

3. O relatório será exibido no navegador padrão.

Filtro Prestador do Repasse

## **03. FILTRO PRESTADOR DO REPASSE**

Segue uma breve explicação das combinações do filtro **Prestador do Repasse** e os seus resultados.

| Grupo de prestador/Prestador | Prestador do Grupo | Inclui procedimento dos grupos de prestadores | Resultado |
| --- | --- | --- | --- |
| Informado prestador | Não informado | Não informado | Exibirá os lançamentos que o prestador receberá o repasse |
| Informado prestador | Não informado | Informado | Exibirá os lançamentos em que o prestador receberá o repasse ou é o executante |
| Informado grupo | Não informado | Não informado | Exibirá os lançamentos que o grupo receberá o repasse |
| Informado grupo | Não informado | Informado | Exibirá os lançamentos para o grupo ou que o grupo receberá o repasse |
| Informado grupo | Informado | X | Exibirá os lançamentos em que o prestador informado atuou pelo grupo e foi o executante do procedimento |

Importante!

O campo "Prestador do repasse", corresponde a quem receberá o repasse e não o prestador executante.

Configuração do Relatório

## **04. CONFIGURAÇÃO DO RELATÓRIO**

O produto disponibiliza o relatório padrão **SAUTRP0001 - Folha de Produção de Prestadores** e pode ser instalado através da ferramenta [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento) ou [Smart View](https://tdn.totvs.com/pages/viewpage.action?pageId=747329327)

Para configurar o relatório que será utilizado pela rotina, acesso os parâmetros através do menu Ambiente > Configuração  > Parâmetros > Gestão Hospitalar > Integrações > Integração Backoffice > Gestão de Estoque, Compras e Faturamento > Configurações gerais 2/5

No campo "**Relatório de Folha de Produção de Prestadores**, informe o relatório que deverá ser utilizado pela rotina.

Dica

É possível customizar nosso relatório, no caso deverá ser feita um cópia do relatório padrão e em seguida alterar a sua cópia utilizando a ferramenta RM Reports ou Smart View.

Tabelas Utilizadas

## **05.** **TABELAS UTILIZADAS**

* + SZCADGERAL
  + SZATENDIMENTO
  + SZATENDIMENTOREC
  + SZFOLHAPRODPREST
  + SAVW004
  + SAVW005
  + SAVW006
  + SAVW007
  + SAVW008
  + SAVW009
  + SAVW017
