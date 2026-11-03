---
content_hash: a774127094b16c7db186ec6e6b253b764afe6b8648996bf6fbd0ff242c414ff2
fetched_at: '2026-06-29T00:12:06.917793+00:00'
page_id: '918390035'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz - Concatenação de Coligada - Inclusão do separador
  (-)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=918390035
version: 3
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Feedz - Concatenação de Coligada - Inclusão do separador (-) |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-12800](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12800) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.241
* 12.1.2410.178
* 12.1.2502.105 e superiores

## **03. SITUAÇÃO/REQUISITO**

Possibilitar o envio do mesmo TOKEN para várias coligadas sem sobrescrever os dados dos Registros Auxiliares (Cargo (Função), Departamento (Seção) e Unidade (Filial)).

## **04. SOLUÇÃO**

A partir dessa versão o parâmetro "**Concatenar o Código da Coligada no Cargo / Departamento / Unidade**" passou adicionar o código da Coligada (GCOLIGADA.CODCOLIGADA) seguido de um separador (- ) no campo "IntegrationId" dos registros auxiliares de Cargo (Função), Departamento (Seção) e Unidade (Filial). Permitindo que a empresa utilize o mesmo Token para várias coligadas, sem sobrescrever informações. 

### Passo 1:

* Acesse o menu Configurações | Parametrizador | Integrações | Feedz e marque o parâmetro **'Concatenar o Código da Coligada no Cargo / Departamento / Unidade / Matrícula'**.

**Passo 2:**

* Acesse o menu Administração de Pessoal | TOTVS RH Performance e Meta / Feedz e realize o envio das informações.

**Passo 3:**

* Json do envio com o o campo ID's concatenados

* Demonstração do recebimento da informações na plataforma da Feedz:

**ATENÇÃO:** Caso já esteja integrado os dados com a Feedz, não é recomendado marcar este parâmetro sem alinhamento prévio com o suporte da Feedz. A marcação irá gerar novos códigos (ID's) e podendo danificar a base de dados.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)
