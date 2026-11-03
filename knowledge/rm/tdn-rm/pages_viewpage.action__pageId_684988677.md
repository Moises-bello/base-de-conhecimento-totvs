---
content_hash: 87f1a331f89e476a63138adb479d427c6c46782effba4c79b1b268016d6362ca
fetched_at: '2026-06-29T00:11:18.296682+00:00'
page_id: '684988677'
product: rm
source: tdn-rm
title: Histórico de Ocorrências do Trabalhador Rural
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684988677
version: 30
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Processos**
4. **Tabelas Utilizadas**

## **01. VERSÕES**

* 12.1.33.257
* 12.1.34.156
* 12.1.2205.101
* e superiores

## **02. VISÃO GERAL**

Através desse processo será possível alimentar o Histórico de Ocorrências do Trabalhador Rural dos funcionários rurícolas e sequeiros nas unidades de produção referentes a um determinado período, seja na safra ou entressafra.

ATENÇÃO:

Esse processo é exclusivo para clientes que utilizam Folha Agrária.

O sistema verifica se o parâmetro “Usa Folha Agrária" existente em Parametrizador | Folha Agrária | Configurações Gerais está marcado e se o campo “Tipo de Funcionário” existente no cadastro do funcionário é “R-Rural”.

## **03. PROCESSOS**

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true2Tipo de Ocorrência Trabalhador RuralTipo de Ocorrência Trabalhador Rural

Acessar o menu Folha Agrária | Cadastros | Tipo de Ocorrência do Trabalhador Rural e cadastrar os tipos necessários para utilização na inclusão e importação dos dados de ocorrência do trabalhador Rural.

  
ATENÇÃO:

No cálculo de produção da folha agrária, ao executar o cálculo do dia da produção será lido a tabela do histórico do funcionário de ocorrências, verificando se o flag “Impede Complemento de Diária” está marcado.

Esta validação é utilizada para calcular o complemento de diária mínima do trabalhador rural.

true4Histórico de Ocorrências do Trabalhador RuralHistórico de Ocorrências do Trabalhador Rural

Acessar o menu Funcionários | Anexos | Histórico de Ocorrências do Trabalhador Rural e cadastrar os dados necessários, conforme tela abaixo:

OBSERVAÇÕES:

1) Esse anexo somente esta acessível quando o tipo de funcionário for  "R-Rural".

2) Essa tabela não tem vinculo com as demais tabelas dos produtos de RH (FOLHA, PONTO, HCM) e deverá ser preenchida pelo usuário.

true3Importação Histórico de Ocorrências do Trabalhador RuralImportação Histórico de Ocorrências do Trabalhador Rural

Acessar o menu Folha Agrária | Importações | Importação Histórico de Ocorrência do Trabalhador Rural e importar o arquivo desejado, lembrado que o arquivo .TXT deverá estar conforme formatação abaixo:

COLIGADA;CHAPA;DATA;TIPO DE OCORRENCIA;JUSTIFICATIVA

## **04. TABELAS UTILIZADAS**

* PFTIPOOCORRENCIATRABRURAL
* PFHSTOCORRENCIATRABRURAL
