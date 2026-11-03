---
content_hash: c9fea182e09fd26c908a67d3085f7ad4c14befa07fdf5721dd2ce353405c4d60
fetched_at: '2026-06-29T00:10:50.820078+00:00'
page_id: '563435392'
product: rm
source: tdn-rm
title: Validação Honorário Cirurgião Indevido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563435392
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Condições Contratuais com Convênios**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Ao executar o processo "Encerramento de Parcial", será retornada a mensagem "Honorário cirurgião indevido! Honorários de consulta hospitalar do Cirurgião somente podem ser cobrados após "x" dias de internação do paciente, rever o lançamento do honorário. Código: "x"." caso:

* A função do prestador é cirurgião;
* Houver um procedimento de honorário que está dentro da faixa de codificação de Consulta Hospitalar ou Visita Hospitalar do Padrão de Faturamento e Codificação do Convênio;
* A data de realização do honorário com prestador cirurgião é anterior à data de realização do honorário dentro da faixa;
* E o tempo em dias entre o início e encerramento da parcial é menor que o número de dias parametrizado no "Visitas Hospitalares após Ato Cirúrgico".

## **02. EXEMPLO DE UTILIZAÇÃO**

## **03. TELA CONDIÇÕES CONTRATUAIS COM CONVÊNIOS**

Padrão de Faturamento e Codificação do Convênio: 

Dias de Visitas Hospitalares após Ato Cirúrgico:

Faixas de codificação:

## **04. TABELAS UTILIZADAS**

* SZATENDHONORARIO
* SZATENDIMENTO
* SZPARCIALATEND
* SZFAIXACODIFICACAO

]]>
