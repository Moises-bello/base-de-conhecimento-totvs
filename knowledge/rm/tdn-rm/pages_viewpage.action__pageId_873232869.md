---
content_hash: 369993a9c352b9daa8c95c935ade1c0185dbe76a00822a0cdc8db8813cd4debe
fetched_at: '2026-06-29T00:11:56.999469+00:00'
page_id: '873232869'
product: rm
source: tdn-rm
title: DT - Integração RM x Feedz - Filial utilizar o NOME FANTASIA ao invés do NOME
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=873232869
version: 6
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Feedz - Filial utilizar o NOME FANTASIA ao invés do NOME |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11398](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11398 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.235
* 12.1.2406.164
* 12.1.2410.101 e superiores

## **03. SITUAÇÃO/REQUISITO**

Possibilitar utilização do campo "Nome Fantasia" da filial ao invés de utilizar o campo "Nome" para o envio das informações da integração RM X Feedz.

## **04. SOLUÇÃO**

Foi criado o parâmetro "**Considerar Nome Fantasia para a Unidade**". Com esse parâmetro, na integração RM X Feedz, o TOTVS Folha de Pagamento RM passará a enviar o "Nome Fantasia" da Filial ao invés do "Nome" ao transmitir as informações da tabela "Unidade".

**Passo 1:** Acesse o menu Configurações | Parametrizador | Integrações | Feedz e marque o parâmetro "**Considerar Nome Fantasia para a Unidade**".

**Passo 2:** Acesse o menu Administração de Pessoal | Cadastros Globais | Filiais.

**Passo 3:** Acesse o menu Administração de Pessoal | TOTVS RH Performance e Meta / Feedz e realize o envio das informações. 

**Passo 4:** Demonstração de recebimento na base de dados da Feedz.

**ATENÇÃO:** Caso já esteja integrado os dados com a Feedz, não é recomendado marcar este parâmetro sem alinhamento prévio com o suporte da Feedz. A marcação irá gerar novos códigos (ID's) e podendo danificar a base de dados.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Feedz](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)
