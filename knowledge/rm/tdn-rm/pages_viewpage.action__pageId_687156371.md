---
content_hash: 0460acd397043e3dae3662a0efd1dd804b2b31ab83e68cdb8b9ada07ca1dcfed
fetched_at: '2026-06-29T00:11:20.615195+00:00'
page_id: '687156371'
product: rm
source: tdn-rm
title: Pausa remunerada do cálculo da folha agrária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687156371
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela Cálculo de Produção Agrária****
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O serviço denominado “PAUSA”, onde o trabalhador faz “N” pausas (descanso) ao longo do dia, faz parte de itens que constam em normas Segurança do Trabalho em sintonia com a legislação. A fim de cumprir a legislação (NR 15, anexo III) e TAC que se referem a períodos de parada do trabalhador rural.

No sistema de Automação de Ponto foi criado o anexo Pausa Remunerada no cadastro de horários que deve ter permissão de acesso para o usuário.

No espelho do funcionário que será verificado para quais dias o índice é relacionado e se dentro do espelho esse dia tem batida, essa premissa deve ser verdadeira para o lançamento da pausa remunerada. Ou seja, deve cadastrar o índice no cadastro de horário e esse índice deve ter batida no espelho de ponto.

Para o processamento da pausa remunerada o usuário deve incluir uma Regra de Cálculo para a Tarefa Agrária com o tipo de cálculo “Pausa Remunerada”, associar a uma tarefa em “Associação de Regra de Cálculo e Tarefa Agrária” e inserir no Parametrizador / Folha Agrária / Parâmetros da Filial / Cálculo campo “Tarefa para Pausa Remunerada”. Caso essas parametrizações não sejam feitas o cálculo da pausa remunerada não será processado.

## **02. EXEMPLO DE UTILIZAÇÃO**

Funcionário com 2 pausas de 15 minutos registrados no cadastro de horário.

Lançamento pelo gestor com número de horas que ultrapassam a jornada trabalhada.

* Tarefa A - 120 minutos R$ 30,91 (diária)
* Tarefa B - 280 minutos R$ 20,00 (empreita)
* Tarefa C - 130 minutos R$ 16,00 (empreita)

Tarefa: 90304 - PAUSAS Regra: 16 - PAUSA REMUNERADA - Prioridade: 10

Programa: 1 Unidade: 01 Fração: 1 Finalidade: 04 Tipo: Empreita Evento: 9304

Quantidade de pausas: 2

Minutos das pausas : 30

Tarefa: 00002 - Implantação de sistemas TAREFA PREÇO INFORMADO 280 minutos 20,00 (Empreita)

Tarefa: 00003 - Investimentos Financeiros TAREFA SEM CÁLC INT FORM 130 minutos 16,00 (Empreita)

Tarefa: 00001 - Análise de sistemas TAREFA DIÁRIA 120 minutos 30,91 (Diaria)

Denominador: 530,00 maior entre Jornada Planejada: 480,00 Soma das Horas de Produção: 530,0000

Indice: (280,00 / 530,00) = 0,5283

Jornada Sem Pausa: (480,00 - 30,00 ) = 450,0000

Pausa: (20,00 / 0,53) \* (0,5283 / 450,0000 \* 30,0000) = 1,3333 (Empreita)

Indice: (130,00 / 530,00) = 0,2453

Jornada Sem Pausa: (480,00 - 30,00 ) = 450,0000

Pausa: (16,00 / 0,25) \* (0,2453 / 450,0000 \* 30,0000) = 1,0667 (Empreita)

Indice: (120,00 / 530,00) = 0,2264

Valor Diaria: (850,00 / 13.200,00 \* 480,00) = 30,9091

Jornada Sem Pausa: (480,00 - 30,00 ) = 450,0000

Pausa: (30,91 / 0,22) \* (0,2264 / 450,00 \* 30,0000) = 2,1205 (Diaria)

Soma das pausa das tarefas de produção: 4,5205

Preço Unitário: (4,5205 / 2) = 2,26025

Quantidade \* Preço Unitário) = Valor Ganho

(2,0000 \* 2,26025) = 4,5205

Tarefa incluida na produção.

**Observação:** Quando ocorrer tarefa de produção com valor de horas zerado apresentará mensagem de aviso como no exemplo abaixo:

 “Indice esta com valor zero, pausa não pode ser calculada para tarefa: 00002 No dia: 18/05/2021 00:00:00 Chapa: 00034”

## **03.** **TELA Cálculo de Produção Agrária**

**Principais Campos e Parâmetro**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |

## **04. TABELAS UTILIZADAS**

* + - PPRODUCAOAGRARIA
