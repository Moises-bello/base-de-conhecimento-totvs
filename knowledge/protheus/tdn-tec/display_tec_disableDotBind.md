---
content_hash: e75a47e46ef1122ab9f98346f9588372ac18b2401497f46a4e79092f6c18cbde
fetched_at: '2026-07-02T19:24:20.525752+00:00'
page_id: '256311359'
product: protheus
source: tdn-tec
title: disableDotBind
type: documentation
url: https://tdn.totvs.com/display/tec/disableDotBind
version: 9
---

disableDotBind

Permite alterar o comportamento para **"BIND"** de variáveis do tipo decimal independente do que está definido na variável de ambiente **DBMONEY**. A chave pode ser definida na seção **[General]** ou em qualquer seção de **configuração de banco**.

Esta configuração é disponibilizada a partir do build **7.00.131227A** version **1.0.0** e aplica-se somente a ambientes que utilizem versões **Informix SDK Client 3.70 ou superiores.**

A ordem de prioridade da leitura da chave é:

* Seção da conexão (DSN)
* Seção do SGBD
* Seção General

Recurso criado como solução a um problema identificado a partir de versões de **Informix SDK Client 3.70** e por isso, por default, o **"bind"** de variáveis será feito com **ponto**. Caso ocorra comportamentos inesperados referente a valores decimais, recomenda-se que retorne ao comportamento padrão (**disableDotBind = 1**), onde o **"bind"** será feito respeitando a definição da variável de ambiente **DBMONEY**.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (Padrão) | Por default, **"bind"** de variáveis do tipo decimal será feito com ponto e não virgula. |
| 1 | Desliga o recurso e o **"bind"** volta a ser feito de acordo com a configuração da variável de ambiente **DBMONEY.** |

## Exemplos

Definição da chave na seção [General]:

Definição da chave para seção de configuração do banco:
