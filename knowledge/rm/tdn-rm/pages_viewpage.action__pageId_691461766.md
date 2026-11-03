---
content_hash: ecec4956650b504a0bb5de1c0de90ddf868913dfa8f9f5a7b4143e5abad2514d
fetched_at: '2026-06-29T00:11:21.299713+00:00'
page_id: '691461766'
product: rm
source: tdn-rm
title: DT - Cancelamento de Movimento - Demitido no mês
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=691461766
version: 11
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | Plataforma RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Cancelar Movimento |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHCALCRM-2508 |

## **02. SITUAÇÃO/REQUISITO**

Ao cancelar o movimento de demitido do mês o funcionário continua com a situação Demitido e com a informação de rescisão calculada igual a verdadeiro (PFUNC>RESCISAOCALCULADA =1). Para alterar essa informação de rescisão calculada via processo, é necessário fazer o cancelamento da rescisão. Porém todos os dados da rescisão são excluídos e retornado o mesmo para Ativo. Cliente necessita que o mesmo permaneça como Demitido, porém com a informação de rescisão não calculada, para que o mesmo possa ser visualizado no portal para ajustes de informações no ponto antes do cálculo da rescisão.

## **03. SOLUÇÃO**

Foi criado o parâmetro 'Habilita controle de rescisão não calculada' no processo de cancelamento de movimento, que quando marcado, irá cancelar a movimentação do demitido no mês, sem alterar sua situação e retornando a informação de rescisão calculada para falso (PFUNC>RESCISAOCALCULADA =0).

Cancelamento de Movimento - Parâmetro marcado, Cancelamento de Movimento - Parâmetro desmarcado, Passo 03, Passo 04passo1,passo2yespasso1

Movimentação excluída:

O campo RESCISAOCALCULADA = 0

nopasso2

Processo de Cancelamento sem marcar o controle:

Movimentação excluída:

O campo RESCISAOCALCULADA = 1

## **04. DEMAIS INFORMAÇÕES**

Atenção

O parâmetro estará disponível a partir da versão 12.1.2205.111 ou superior.

O Parâmetro 'Habilita controle de rescisão não calculada' só ficará habilitado para uso caso o parâmetro 'Cancela movimento de demitido no mês' estiver marcado. Este controle não será feito em caso de rescisão calculada no próximo mês.

Quando existir algum evento de valor forçado e o campo 'Cancela eventos alterados manualmente' estiver desmarcado, caso o parâmetro 'Habilita controle de rescisão não calculada' estiver marcado não irá cancelar os eventos de valores forçados, porém irá mudar a informação de rescisão calculada para falso.

## **05. ASSUNTOS RELACIONADOS**
