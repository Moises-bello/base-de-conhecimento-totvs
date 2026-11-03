---
content_hash: 5a695ad1608240c2aeb50a6d847d14710577a8b35b0c2f6f3aa9fca79d5869bb
fetched_at: '2026-06-29T00:11:56.993706+00:00'
page_id: '873232738'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz - Concatenação de Coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=873232738
version: 8
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Feedz - Concatenação de Coligada |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11313](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11313 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.235
* 12.1.2406.164
* 12.1.2410.101 e superiores

## **03. SITUAÇÃO/REQUISITO**

Possibilitar o envio do mesmo TOKEN para várias coligadas sem sobrescrever os dados dos Registros Auxiliares (Departamento, Função/Cargo e Unidade).

## **04. SOLUÇÃO**

Implementamos o parâmetro "**Concatenar o Código da Coligada no Cargo/Departamento/Unidade**", permitindo que a empresa utilize o mesmo Token para várias coligadas, sem sobrescrever informações. Ao ativar esse parâmetro, o sistema concatenará o código da coligada no ID e na descrição dos campos de Cargo, Departamento e Unidade, garantindo uma distinção clara entre as coligadas.

### Passo 1:

* Acesse o menu Configurações | Parametrizador | Integrações | Feedz
* Marque o parâmetro **'Concatenar o Código da Coligada no Cargo/Departamento/Unidade'**.

**Passo 2:**

* Acesse o menu Administração de Pessoal | TOTVS RH Performance e Meta / Feedz e realize o envio das informações.

**Passo 3:**

* Demonstração do recebimento da informações na plataforma da Feedz:

**ATENÇÃO:** Caso já esteja integrado os dados com a Feedz, não é recomendado marcar este parâmetro sem alinhamento prévio com o suporte da Feedz. A marcação irá gerar novos códigos (ID's) e podendo danificar a base de dados.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)
