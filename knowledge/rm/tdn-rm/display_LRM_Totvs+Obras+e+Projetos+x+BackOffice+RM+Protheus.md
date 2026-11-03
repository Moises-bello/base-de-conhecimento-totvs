---
content_hash: 323440f081d078c17468dfbdb0a68b3a04c2742baa5cd61994b6bb8a00b44bde
fetched_at: '2026-06-29T00:10:51.628306+00:00'
page_id: '569486197'
product: rm
source: tdn-rm
title: Totvs Obras e Projetos x BackOffice RM Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/Totvs+Obras+e+Projetos+x+BackOffice+RM+Protheus
version: 10
---

Este documento tem objetivo detalhes com relação a utilização da apropriação com BackOffice Protheus, informações gerais sobre o processo no TCOP disponíveis em: <https://tdn.totvs.com/x/MkLnHg>

**PARÂMETROS DE PROJETO:**

Para parametrizar o processo vá em:***"Parâmetro de Projetos | Apropriação | Apropriação BackOffice”***e preencha os seguintes campos: 

**Apropriar liberação de período de contratos em:**

* **Medição**: O sistema considera como valor apropriado o valor informado na medição do período do contrato. Ao solicitar os valores apropriados no BackOffice sendo desconsideradas as movimentações originadas destas medições.
* **Nota Fiscal**: O sistema considera como valor apropriado o valor retornado pelo BackOffice para os documentos de entrada, desconsiderando os valores de medição.

**Moeda Documento de Entrada SD1**:

Se a moeda do Projeto for diferente da moeda da movimentação SD1, e uma das cinco moedas MV\_SIMB1,MV\_SIMB2,MV\_SIMB3,MV\_SIMB4,MV\_SIMB5, será automaticamente considerado o CUSTO referente a moeda do Projeto.

Campos considerados: D1\_CUSTO1,D1\_CUSTO2,D1\_CUSTO3,D1\_CUSTO4,D1\_CUSTO5

**Considerar o valor do seguro**:

Se marcado, o sistema soma o valor de seguro no total do item. Default: 1.

Campo: MPARAMETRO - APROPSEGURO

**Considerar o valor da despesa**:

Se marcado, o sistema soma o valor de despesa no total do item. Default: 1.

Campo: MPARAMETRO - APROPDESPESA

**Considerar o valor de IPI**:

Se marcado, o sistema soma o valor de IPI no total do item. Default: 1.

Campo: MPARAMETRO - APROPIPI

**REGRA DE NEGOCIO:**

Fluxos

# Analise de Log de Consulta SQL de Apropriação:

1 - Obter a URL de consulta de Apropriação ao Final do Processo de importação  
2 - Informar a URL no navegador com o complemento "&LOG=TRUE"

3 - No resultado é retornado a tag command com a consulta SQL que foi utilizado na busca da apropriação.

## **Para Backoffice Protheus :**

## Criado o parâmetro “CONSWSAPROPRIACAOPROTHEUS” que habilita a pesquisa da apropriação diretamente no PROTHEUS.

## Este parâmetro é inserido automaticamente na integração EAI 2.0. Sendo validado em conjunto com o parâmetro “VERSAOPROTHEUS” que define a versão do PROTHEUS no cliente.

## Quando informado “11” não será habilitada esta modalidade de integração devido a versão 11 do PROTHEUS não atender às necessidades do processo.
