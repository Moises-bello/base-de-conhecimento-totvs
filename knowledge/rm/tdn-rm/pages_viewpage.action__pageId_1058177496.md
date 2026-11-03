---
content_hash: 11e0c11eeb69a187a903183646f4c2b848fcf02e377cef6f6fc9f5d320f2fccb
fetched_at: '2026-06-29T00:05:52.176184+00:00'
page_id: '1058177496'
product: rm
source: tdn-rm
title: DT - Integração RM X Quírons - Mudança da Chapa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058177496
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Integração RM X Quírons - Mudança da Chapa |
| País: | Brasil |
| Épico: | [DRHROTRM-14849](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14849) |

## **02. VERSÃO**

* 12.1.2506.290
* 12.1.2510.212
* 12.1.2602.131 e Superiores

## **03. S****ITUAÇÃO/REQUISITO**

Sempre que houver alteração da **chapa do funcionário**, seja por meio do processo de **Troca de Chapa** ou pela **Transferência do tipo “5 - Transferência sem ônus”**, é necessário que essa alteração seja enviada ao produto **Quírons**, garantindo a consistência das informações entre os sistemas.

## **04.****SOLUÇÃO**

Foi implementado o envio das tags **"newRegistration"** e **"newEmployeeId"** para garantir que alterações de matrícula sejam corretamente refletidas na integração com o **Quírons**.

A partir dessa melhoria, sempre que houver mudanças por **Troca de Chapa** ou **Transferências (tipo 5)**, a matrícula será automaticamente atualizada no Quírons.

**Exemplo:**

Colaborador cadastrado com a matrícula 65465.

Colaborador na Quírons.

Executado o processo "Trocar Chapa do Funcionário" existente em Administração de Pessoal | Funcionários | Processos :

Mensagem gerada com as tags "newRegistration" e "newEmployeeId".

Após o envio, o colaborador assumiu a nova matrícula na Quírons.

## **05. DEMAIS INFORMAÇÕES**
