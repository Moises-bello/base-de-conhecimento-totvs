---
content_hash: 54837b94429ac8dfa5347c8a6a177e79add4d0b83139a8f431a4d117ebb4254a
fetched_at: '2026-06-29T00:12:15.428748+00:00'
page_id: '979016840'
product: rm
source: tdn-rm
title: DT - TAE - Utilização de E-mail pessoal no processo de integração de relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979016840
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | TAE - Utilização de E-mail pessoal no processo de integração de relatórios |
| País: | Brasil |
| Épico | [DRHCALCRM-9024](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9024) |

## **02. SITUAÇÃO/REQUISITO**

Disponibilizar a opção de utilizar o e-mail pessoal do colaborador para o envio de relatórios pelo TAE sempre que o e-mail corporativo registrado em “Identificação do Funcionário” não estiver configurado como “E-mail principal”.

## **03. SOLUÇÃO**

Foi então disponiblizado uma nova flag no cadastro de **Tipo de Relatório** do TAE para que utilizemos o email pessoais nestes casos onde o e-mail não está preenchido na aba de **Identificação**, em casos como este onde o e-mail não esta preenchido na aba identificação, será utilizado o e-mail cadastrado em **Endereço Principal**, no campo **EMAILPESSOAL.**  
Este exemplo citado acima, só será utilizado quando a flag "**Utilizar e-mail pessoal caso o e-mail principal não esteja preenchido**"  esteja ativa, no cadastro de Tipo de Relatório:

###### **04. DEMAIS INFORMAÇÕES**
