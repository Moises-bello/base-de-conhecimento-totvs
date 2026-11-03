---
content_hash: 991d96be93cbd67eb952d0e30ae47a4e2f9cc57990ac603d0ad31091af8e8949
fetched_at: '2026-06-29T00:11:16.169249+00:00'
page_id: '663594324'
product: rm
source: tdn-rm
title: Concurso de Bolsa
type: documentation
url: https://tdn.totvs.com/display/LRM/Concurso+de+Bolsa
version: 28
---

Versão disponível

Esta funcionalidade está disponível a partir da versão 12.1.2205

# Descrição

O concurso de bolsa permite que sejam cadastradas para o processo seletivo ou área de interesse ofertada, bolsas que poderão ser concedidas ao candidato conforme o critério de classificação ou pontuação.

O cadastro do concurso de bolsa poderá ser acessado através da MDI principal ou através do anexo do processo seletivo ou área de interesse ofertada.

**Concurso de bolsa por processo seletivo**

Nesta modalidade a bolsa cadastrada no anexo do Processo Seletivo terá validade para todas as áreas de interesse cadastradas no processo. Ou seja, caso defina o range para as 3 primeiras posições, os três primeiros colocados de cada área de interesse serão vinculados à bolsa do concurso.

Quando houver um concurso de bolsa cadastrado no processo seletivo não será permitido cadastrar concurso de bolsa separado para área de interesse ofertada do processo seletivo recebeu o cadastro.

**Concurso de bolsa por área de interesse ofertada**

Será permitido cadastrar concurso de bolsa por área de interesse ofertada desde que não exista concurso de bolsa cadastrado para o processo seletivo da área de interesse ofertada.

Nesta modalidade a bolsa cadastrada no anexo da área ofertada terá validade somente para esta área do processo seletivo. Ou seja, caso defina a range para as 3 primeiras posições, os três primeiros colocados da área de interesse onde a bolsa está vinculada serão vinculados à bolsa do concurso.

Informações do cadastro:

| Campo | Informação |
| --- | --- |
| Bolsa | Bolsa que será concedida |
| Tipo de critério para aplicação da bolsa | Tipo do critério utilizado no concurso de bolsa ( classificação ou pontuação) |
| Filtrar por serviço | Se esta opção for marcada será habilitada a aba "Serviço", na qual deverá ser identificado qual(is) serviço(s) a bolsa será aplicada.  Caso esta opção não seja marcada a bolsa será aplicada a todos os serviços processados pelo plano de pagamento. |
| Aplicar por: Parcela | Indica que a bolsa será aplicada nas parcelas conforme os campos "Parcela inicial" e "Parcela final" |
| Aplicar por: Data | Indica que a bolsa será aplicada somente para as parcelas com data vencimento entre a "Data início" e "Data final" |

Informações

O Concurso de Bolsas não permite alterações quando já possui candidatos classificados.   
Somente os campos de aplicação da bolsa podem ser alterados:

# Range

O range é o cadastro que define em quais regras a bolsa deverá ser concebida.

Informações do cadastro:

| Campo | Informação |
| --- | --- |
| Tipo de critério  - Classificação inicial e final | Quando o tipo de critério for por classificação deverá se informado qual é a classificação inicial e final que será considerada para conceder a bolsa |
| Tipo de critério  - Pontuação inicial e final | Quando o tipo de critério for por pontuação deverá se informado qual é a pontuação inicial e final que será considerada para conceder a bolsa |
| Tipo de desconto | Indica se o desconto da bolsa vai ser em percentual ou valor |
| Valor | Valor a ser aplicado (conforme o tipo de desconto) |

Será permitido cadastrar mais de uma bolsa no concurso de bolsa somente se o range definido para as bolsas não entrarem em conflito.

**Exemplo permitido:**

1º Concurso de Bolsa A | Bolsa X | Critério: pontuação | pontuação 90 a 100

2º Concurso de Bolsa B | Bolsa Y | Critério: pontuação | pontuação 70 a 80

**Exemplo NÃO permitido:**

1º Concurso de Bolsa A | Bolsa X | Critério: pontuação | pontuação 90 a 100

2º Concurso de Bolsa B | Bolsa Y | Critério: pontuação | pontuação 70 a 100

**ATENÇÃO**

A partir da versão **12.1.2310**, será possível cadastrar concurso de bolsas diferentes com o mesmo range, desde que ofertem bolsas diferentes entre si, assim permitindo que um candidato acumule mais de uma bolsa.

**Exemplo permitido:**

1º Concurso de Bolsa A | Bolsa X | Critério: pontuação | pontuação 90 a 100

2º Concurso de Bolsa B | Bolsa Y | Critério: pontuação | pontuação 70 a 80

**-------------------------------------------------------------------------------------------**

1º Concurso de Bolsa A | Bolsa X | Critério: pontuação | pontuação 50 a 100

2º Concurso de Bolsa B | Bolsa Y | Critério: pontuação | pontuação 80 a 90

A partir da versão **12.1.2410**, será possível alterar o tipo de critério para aplicação da bolsa, só poderá ser alterado caso não haja candidato classificado e associado a bolsa.

Para saber mais sobre como é realizada a apuração do concurso de bolsa [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=663602469).

##
