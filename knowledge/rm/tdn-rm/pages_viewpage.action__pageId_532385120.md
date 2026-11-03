---
content_hash: 266a21755c9863205f3fa05e4aa0472a8428b9f21f5297a7441fd37e74ac36f1
fetched_at: '2026-06-29T00:10:36.471051+00:00'
page_id: '532385120'
product: rm
source: tdn-rm
title: 'FISCAL01-11889 DT EFD-Contribuições 2020 - Reg. 1011: 8- Cálculo dos tributos
  discutidos'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532385120
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| Ticket: | FISCAL01-11889 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11889 |

## **02. SITUAÇÃO/REQUISITO**

Nesta issue deverá ser implementado a tarefa abaixo observando a definição de pronto da squad 

● Tratar a Inclusão/Alteração de Lançamento Fiscal para realizar o cálculo dos tributos discutidos.

## **03. SOLUÇÃO**

Foi realizado a implementação do Cálculo do Tributo Discutido no serviço de Inclusão, que será utilizado na Escrituração Fiscal e Inclusão de Lançamento manual. O cálculo é realizado de acordo com a fórmula de Base  
Cálculo informando cadastro do Tributo Discutido, observando que o valor só será calculado no momento que o Lançamento for Salvo (Inclusão Manual).

Quando algum dos campos  (Base de Cálculo, Alíquota, CST e Valor)  for alterado no  cadastro do Tributo Discutido, o calculo não será realizado, caso nenhum valor default seja informado o Serviço de Inclusão calculara automaticamente.
