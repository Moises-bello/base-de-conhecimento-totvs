---
content_hash: 873c4969258f71bd8cd20742866d965e9722c649400892cfbd78e0fc06ac21be
fetched_at: '2026-06-29T00:05:47.717857+00:00'
page_id: '1015558328'
product: rm
source: tdn-rm
title: Tempo de Processamento na Rotina do Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1015558328
version: 46
---

## **01. DADOS GERAIS**

| Linha de Produto: | RM |
| --- | --- |
| Segmento: | RH |
| Módulo: | Automação de Ponto |
| Função: | Gravar o total de funcionários e o tempo de execução do cálculo da movimentação |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHJORNRM-8757](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-8757) |

## **02.** **VERSÕES**

O recurso estará disponível a partir das versões:

* 12.1.2506.198
* 12.1.2510.129 e superiores

## **03. SITUAÇÃO/REQUISITO**

Permitir gravar o total de funcionários e o tempo total da execução do cálculo da movimentação.

## **04. SOLUÇÃO**

Criada a tabela APONTOLOG que irá armazenar o total de funcionários e o tempo de execução do cálculo da movimentação de todos os funcionários.

## **05. EXEMPLOS**

Exemplo 1: Cálculo com Fracionamento - Avisos 

Quando não existir a tabela APONTOLOG na base de dados ou ao tentar Inserir os dados na tabela  tiver algum impedimento, será demonstrada uma mensagem para o usuário , conforme segue:

Executando o cálculo com Fracionamento, temos dois processos executados com Avisos.

No log será demonstrada a seguinte mensagem para ambos os Avisos.

Se o cálculo for executado sem fracionamento , será demonstrada a tela

O usuário deverá verificar a existência da tabela APONTOLOG na base de dados ou executar o RMAtualizador , realizando o cálculo em seguida.

Exemplo 2: Cálculo com Fracionamento - Avisos e Erros

Será gravada na tabela apenas os  ID Jobs com status Avisos-Ressalva ou Sucesso. Os erros não serão gravados.

Na tela temos dois processos. Status Finalizado e  Erro.

Verificando na tabela APONTOLOG, teremos apenas o ID Job 103144. Esse IDJOB é referente o Statur Finalizado.

Exemplo 3: Cálculo com Fracionamento - Sucesso no cálculo

Cálculo realizado com sucesso. Será gravadona tabela APONTOLOG.

Será visualizado na tabela APONTOLOG todos os Status com o tipo 02-FINALIZADO .

Exemplo 4: Cálculo com Fracionamento - Mais de uma Coligada

Cálculo agendado para mais de uma coligada.

Fracionamento Coligada 6:

Fracionamento Coligada 1:

Será visualizado na tabela APONTOLOG todos os Status com o tipo 02-FINALIZADO .

Exemplo 5: Cálculo sem Fracionamento - Apenas uma Coligada

Cálculo para uma coligada.

Gerou o ID JOB

Será visualizado na tabela APONTOLOG todos os Status com o tipo 02-FINALIZADO .

Importante

1. Os dados serão gravados na tabela APONTOLOG, quando o cálculo for finalizado com Avisos, sucesso ou ressalva.
2. O Status ERRO , não será gravado na tabela  .
3. A tabela APONTOLOG possui as seguintes informações: Quantidade de Registros Processados,Data da Execução,Hora início e Hora Fim,Tempo gasto na execução e IdJob

**06. ASSUNTOS RELACIONADOS**

**[Movimento - Calcular Movimentação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719089)**
