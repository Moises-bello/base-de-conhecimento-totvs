---
content_hash: 8adce9d5a885fd23e3b51cf57bc4fab85b7418605b80974d5e13573387b7c1bf
fetched_at: '2026-06-29T00:10:43.999285+00:00'
page_id: '551451538'
product: rm
source: tdn-rm
title: 2.5.1 Portal do Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/2.5.1+Portal+do+Aluno
version: 14
---

Uma das opções de registro de cobrança online é pelo Portal do Aluno, o processo é bem simples, para isso, basta seguir os passos abaixo:

Acessar o Portal do Aluno | Ir no Menu | Clicar em Financeiro

Localizar o lançamento desejado | Selecioná-lo | clicar no ícone

Neste momento, ao clicar para *Avançar* o boleto no Portal o mesmo será registrado de forma online junto ao Banco correspondente.

O status remessa (*CNABSTATUS*) do boleto na tabela *FBOLETO* mudará para "*registrado online*". Abaixo todas as constantes dessa tabela.

* **FBOLETO - Status**

| Campo | Chave | Valor |
| --- | --- | --- |
| STATUS | 0 | Em aberto |
| STATUS | 1 | Baixado |
| STATUS | 2 | Cancelado |
| STATUS | 4 | Baixado Parcialmente |
| STATUS | 5 | Inativo |

* **FBOLETO - Status da Remessa**

| Campo | Chave | Valor |
| --- | --- | --- |
| CNABSTATUS | 0 | Não Remetido |
| CNABSTATUS | 1 | Remetido |
| CNABSTATUS | 2 | Registrado |
| CNABSTATUS | 3 | Recusado |
| CNABSTATUS | 4 | Baixado |
| CNABSTATUS | 5 | Registrado Online |
| CNABSTATUS | 6 | Cancelado |
| CNABSTATUS | 7 | Pendente Remessa |

falseVeja também

* [Constantes de Tabelas RM](https://www.lorencone.com.br/totvs-rm-constantes-de-tabelas/#tab-fboleto)
* [TOTVS Educacional - Educacional - PORTAL - Permitir imprimir boletos não registrados (válido para convênios de tipo de cobrança registrada)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031765853-RM-EDU-PORTAL-Permitir-imprimir-boletos-n%C3%A3o-registrados-v%C3%A1lido-para-conv%C3%AAnios-de-tipo-de-cobran%C3%A7a-registrada-)
* [TOTVS Educacional - Educacional - PORTAL - Registro online - Como funciona o registro online de boletos para lançamentos do TOTVS Educacional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052422893-TOTVS-Educacional-Educacional-PORTAL-Registro-online-Como-funciona-o-registro-online-de-boletos-para-lan%C3%A7amentos-do-TOTVS-Educacional)
* [Cross Segmentos - BackOffice Linha RM - FIN - Registro Online Banco do Brasil - Erro na tentativa de registrar online o boleto: Um ou mais erros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026396674-Cross-Segmentos-Backoffice-Linha-RM-FIN-Registro-Online-Banco-do-Brasil-Erro-na-tentativa-de-registrar-online-o-boleto-Um-ou-mais-erros)
* [RM - FIN - Erro na tentativa de registrar online o boleto: O boleto deve estar com o status da remessa como NÃO remetido ou Pendente Remessa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019863372-RM-FIN-Erro-na-tentativa-de-registrar-online-o-boleto-O-boleto-deve-estar-com-o-status-da-remessa-como-N%C3%83O-remetido-ou-Pendente-Remessa-)
