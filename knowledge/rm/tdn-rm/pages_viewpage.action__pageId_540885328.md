---
content_hash: fe10bf06443de322b6e8049d035400d6d589a7328b179bfe55b62a52c9963c8f
fetched_at: '2026-06-29T00:10:37.725338+00:00'
page_id: '540885328'
product: rm
source: tdn-rm
title: FISCAL01-12187 DT Encerramento da Sub-Apuração - Origem Lançamentos Fiscais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540885328
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Encerramento da Sub-Apuração - Origem Lançamentos Fiscais |
| Ticket | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12187 |

## **02. SITUAÇÃO/REQUISITO**

Criação do processo de Encerramento da Sub Apuração, com base nos Lançamentos Fiscais

## **03. SOLUÇÃO**

Criado um novo processo na visão do anexo de Sub Apuração do Período de Apuração, que efetuará o Encerramento do mesmo e o cálculo dos valores, conforme detalhamento abaixo:

## **Encerramento da Sub Apuração**

Os períodos de apuração das sub-apurações também devem ser encerrados e os valores calculados e isso deve ocorrer antes do encerramento do tributo principal. Por exemplo, para encerrar o período de apuração do ICMSST é preciso, primeiro, encerrar suas sub-apurações.

**ATENÇÃO: As regras descritas abaixo se aplicam somente à apuração com base nos Lançamentos Fiscais. A apuração com base em Lançamentos de Outros Débitos\Créditos ainda não foi realizada e, quando for, deverá atualizar essa documentação. Os trechos referentes a Outros Débitos\Créditos estão destacados nos comentários.**

#### **Validações realizadas para o Encerramento**

1. O Período de Apuração deve estar Aberto;
2. O período de Sub Apuração imediatamente anterior, de mesmo Identificador, deve estar encerrado;
3. O Lote Fiscal (caso seja utilizado) deve estar Aberto.

#### **Seleção dos Lançamentos Fiscais**

No Encerramento serão selecionados Lançamentos Fiscais de Entrada e Saída, que atendam aos seguintes critérios:

1. Possuam Ajuste vinculado ao Lançamento ou ao Item;
2. Pertençam à Coligada\Filial do Período de Apuração;
3. Cuja DATALF esteja dentro do período da Sub Apuração;
4. Com Status Normal ou Estornado;
5. Associados a CFOP Fiscal;
6. Cujo Lote Fiscal esteja Liberado (caso utilize Lote Fiscal);

No processo de encerramento, os seguintes valores devem ser calculados pelo sistema:

#### **Valor total dos débitos por Saídas**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* **Se o identificador for “3” devem ser considerados os lançamentos de ajuste onde o 3º e 4º caracteres forem “2” e “3”, respectivamente. Por exemplo: *MG**23**000999***
* **Se o identificador for “4” devem ser considerados os lançamentos de ajuste onde o 3º e 4º caracteres forem “2” e “4”, respectivamente. Por exemplo: *MG**24**000999***
* **E assim sucessivamente.**
* **Resumindo, o 3º caracter deve ser “2” e o 4º caracter deve ser igual ao código do Identificador;**

Normalmente estes ajustes estão associados a Lançamentos Fiscais de Saída, porém, não iremos restringir isto.

#### **Valor total de Ajustes a débito**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0**”. Por exemplo: *MG****00****9999*.

Normalmente estes ajustes estão associados a Lançamentos Fiscais de Saída, porém, não iremos restringir isto.

* Lançamentos de Outros Débitos e Créditos do Tipo "Debito" onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0**”. Por exemplo: *MG****00****9999*.

#### **Valor total de Ajustes Estornos de créditos**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0**” e “**1**”, respectivamente. Por exemplo: ***MG******01******9999.***

Normalmente estes ajustes estão associados a Lançamentos Fiscais de Saída, porém, não iremos restringir isto.

* Lançamentos de Outros Débitos e Créditos do Tipo "Estorno de Crédito" onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0 e 1**”. Por exemplo: *MG**01****9999*.

#### **Valor total dos créditos por Entradas**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* **Se o identificador for “3” devem ser considerados os lançamentos de ajuste onde o 3º e 4º caracteres forem “5” e “3”, respectivamente. Por exemplo: *MG**53**000999***
* **Se o identificador for “4” devem ser considerados os lançamentos de ajuste onde o 3º e 4º caracteres forem “5” e “4”, respectivamente. Por exemplo: *MG**54**000999***
* **E assim sucessivamente.**
* **Resumindo, o 3º caracter deve ser “5” e o 4º caracter deve ser igual ao código do Identificador;**

Normalmente estes ajustes estão associados a Lançamentos Fiscais de Entrada, porém, não iremos restringir isto.

Não iremos tratar Lançamentos Extemporâneos neste primeiro momento.

#### **Valor total de Ajustes a crédito**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0**” e “**2**”, respectivamente. Por exemplo: ***MG******02******9999.***

Normalmente estes ajustes estão associados a Lançamentos Fiscais de Entrada, porém, não iremos restringir isto.

* Lançamentos de Outros Débitos e Créditos do Tipo "Crédito" onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0 e 2**”. Por exemplo: *MG**02****9999*.

#### **Valor total de Ajustes Estornos de Débitos**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0**” e “**3**”, respectivamente. Por exemplo: ***MG******03******9999.***

Normalmente estes ajustes estão associados a Lançamentos Fiscais de Entrada, porém, não iremos restringir isto.

* Lançamentos de Outros Débitos e Créditos do Tipo "Estorno de Débito" onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0 e 3**”. Por exemplo: *MG**03****9999*.

#### **Saldo credor do período anterior**

Este campo recebe o saldo credor do período de Sub Apuração imediatamente anterior, de mesmo Identificador.

#### **Valor total das Deduções**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos Fiscais/Itens se o 3º caracter do Código de Ajuste for igual “**6**” e o 4º caractere for igual à  **“3”, “4” “5”, “6”, “7” ou “8”**.
* Lançamentos de Outros Débitos e Créditos do Tipo "Deduções" onde 3º e 4º caracteres do Código de Ajuste informado forem iguais à “**0 e 4**”. Por exemplo: *MG**04****9999*.

**Saldo apurado no período**

Corresponde à expressão:

Se o resultado for menor que “0” (zero), representa valor de imposto a pagar.

Já o resultado positivo corresponde a Saldo Credor a transportar para o próximo período.

#### **Valor total dos débitos especiais**

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos Fiscais/Itens se o 3º caracter do Código de Ajuste for igual “**7**” e o 4º caractere for igual à  **“3”, “4” “5”, “6”, “7” ou “8”**.

Ao final dos cálculos os valores são armazenados na tabela e o Status da Sub Apuração é atualizado para “**Encerrado**”.
