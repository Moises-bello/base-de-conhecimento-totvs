---
content_hash: b7e0f3d0a15d05a4af1e1a0a1917b303f8064becc63b1cbe2581ce1a74e4e4cf
fetched_at: '2026-06-29T00:11:11.747590+00:00'
page_id: '648444013'
product: rm
source: tdn-rm
title: Importa Dados de Resilição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=648444013
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Importação do Movimento de Ensino**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Layout utilizado para importação dos dados de resilição que venham de outro sistema acadêmico e integra com TOTVS Folha de Pagamento.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Campo | Tipo Campo | Obrigatório | Formato | Descrição | Observações |
| 1 | CODCOLIGADA | Numérico | S |  | Código da Coligada | Deverá ter um arquivo para cada coligada, devido sistema validar a coligada corrente. |
| 2 | CHAPA | Alfanumérico | S |  | Chapa do Funcionário/Professor | Identifica o funcionário na folha de pagamento. |
| 3 | IdProfTurmaAtiv | Numérico | S |  | Campo Identificação do movimento de ensino importado | Identificação do movimento de ensino importado a que ser refere a importação da resilição |
| 4 | CodEvento | Alfanumérico | S |  | Código do evento | Evento da resilição |
| 5 | DataResilicao | Data | S |  | Data da Resilição | Data em que foi processada a Resilição |
| 6 | TipoResilicao | Alfanumérico | S |  | Tipo de resilição | Tipo de resilição que deve estar previamente cadastrado em Rescisão / Resilição / Tipos de Resilição |
| 7 | JornadaAtual | Hora | S | 000:00 | Jornada atual | Jornada atualizada |
| 8 | ValorFixoAtual | Numérico | S | 9999,99 | Valor fixo atual | Valor atualizado |
| 9 | CodFilial | Numérico | S |  | Código da filial | Código da filial |

## **02. EXEMPLO DE UTILIZAÇÃO**

Existindo o movimento de ensino importado para o funcionário 00045, conforme tela abaixo:

Foi criado um arquivo TXT de acordo com o layout informado acima:

1;00045;2;0255;01/11/2021;1;022:00;100;1

Realizada a importação conforme a parametrização abaixo:

**Observação:**Para o exemplo acima foi utilizada a base exemplo.

## **03.****TELA** **Importação do Movimento de Ensino**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Importa dados de Resilição | Parâmetro para habilitar a importação dos dados da resilição do movimento importado anteriormente |
| Arquivo de Importação | Localização do arquivo a ser importado |

## **05. TABELAS UTILIZADAS**

* PFMOVENSINOIMP
* PFMOVENSINOIMPRESILICAO
