---
content_hash: e7ef6abc8b9be5d3579dbf0815a48f3c4fc81d9cd395c78057b33eb11f52cf0b
fetched_at: '2026-06-29T00:12:02.744050+00:00'
page_id: '904042998'
product: rm
source: tdn-rm
title: DeleteRecord via Webservice nas tabelas PFFINANC E PFMOVCC
type: documentation
url: https://tdn.totvs.com/display/LRM/DeleteRecord+via+Webservice+nas+tabelas+PFFINANC+E+PFMOVCC
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Documento Técnico**

## **01. VISÃO GERAL**

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Webservice |
| Função: | Webservice |
| País: | Brasil |
| Ticket: | [DRHCALCRM-7489](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7489) |

## **02. EXEMPLO DE UTILIZAÇÃO**

Tomando como base o MDI, observa-se na Ficha Financeira, Mês 12, Ano 2022, da Chapa 00001, os registros com os Períodos 3, 4 e 5

Adentrando ao SoapUI para fazer o DeleteRecord via XML, primeiramente será configurado o método ReadRecord, com os parâmetros na tag <tot:DataServerName> na seguinte ordem: DataServer/Ano;Mês;CodColigada;Chapa;CodUsuario;Periodo. O Período não é obrigatório, porém, caso seja utilizado ele irá apagar registros pontuais em mesmos Ano/Mês. Caso contrário, caso o período não seja informado, serão deletados todos os períodos do Ano/Mês informados. Outro ponto de atenção é o Auth, localizado abaixo do quadro de XML, que deve estar corretamente logado, caso contrário não haverá comunicação e não gerará as informações necessárias para repassar ao DeleteRecord. No exemplo abaixo, pode-se visualizar um exemplo da tag, objetivando apagar o registro que contém o Período=3:

" <tot:DataServerName>FopFichaFinancData/2022;12;1;00001;mestre;3</tot:DataServerName> "

Ao gerar o ReadRecord com sucesso, copia-se o conteúdo do XML gerado para dentro da tag <tot:XML> do método DeleteRecord, mantendo os mesmos parâmetros nas outras tags

Ao acionar o método DeleteRecord, se toda a parametrização estiver correta, o resultado trará a mensagem "Exclusão de registro(s) realizado com sucesso"

Ao atualizar e verificar novamente o MDI, é possível verificar que o registro que continha o Período 3 foi apagado corretamente, mantendo os outros dois períodos

## **03. DOCUMENTAÇÃO RELACIONADA**

[DRHCALCRM-7489](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-7489)

[Documento Técnico - DeleteRecord via Webservice nas tabelas PFFINANC e PFMOVCC](https://tdn.totvs.com.br/display/LRM/DT+-+DeleteRecord+via+Webservice+nas+tabelas+PFFINANC+E+PFMOVCC)
