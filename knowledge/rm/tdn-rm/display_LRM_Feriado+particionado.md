---
content_hash: a3bf94917a5a5e020f36f79f532ed71010a584b7f1da099f2276917663a97493
fetched_at: '2026-06-29T00:11:29.357166+00:00'
page_id: '736190526'
product: rm
source: tdn-rm
title: Feriado particionado
type: documentation
url: https://tdn.totvs.com/display/LRM/Feriado+particionado
version: 29
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Automação de Ponto (CHRONUS) |
| Função: | Ajuste para considerar apenas o intervalo do feriado |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHJORNRM-3744 |

## **02. SITUAÇÃO/REQUISITO**

Que o sistema considere apenas o intervalo do feriado sem a necessidade de alterar o horário dos funcionários.

## **03. SOLUÇÃO**

Quando o feriado não for cadastrado para o dia todo ***(Exemplo: quarta-feira de cinzas 00:00 às 12:00)***, o sistema irá considerar apenas o intervalo do feriado como horas de feriado.

**04. EXEMPLO DE UTILIZAÇÃO**

12Exemplo Horário Diurno

***Feriado:*** *Dia 22/02/2022- Início: 00:00 Fim: 12:00*

***Horário Planejado:** 08:00-12:00-14:00-18:00*

3Exemplo Horário Noturno

***Feriado:** Dia 22/02/2023 - Início: 00:00 Fim: 12:00*

***Horário Planejado:** 22:00-05:00*

**Obs:** Para que as extras realizadas após a jornada planejada sejam consideradas respeitando o intervalo do feriado particionado, o parâmetro **"Considera início da jornada para definir tipo de extra"** disponível em **Parametrizar Sindicato > Extra** deve estar desmarcado.   
Documentação do parâmetro: <https://tdn.totvs.com/display/public/LRM/Extra>

**05. ASSUNTOS RELACIONADOS**

**[Solução Conflito-Sindicato-Feriado](https://tdn.totvs.com/display/LRM/Feriados)**
