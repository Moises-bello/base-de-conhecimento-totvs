---
content_hash: fe73347866a37ce4e09826c1708cc20fda094aa1d372516a0a17718e6acf8024
fetched_at: '2026-06-29T00:10:22.531478+00:00'
page_id: '497192399'
product: rm
source: tdn-rm
title: 'DEDUMOBILE-2125 DT Falta de Tags em: Notas de etapas, Notas de Avaliações
  e Ocorrências'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497192399
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Gestão Educacional |
| Módulo: | Central de Comunicações |
| Função: | Agendamento / envio de mensagens |
| Ticket: | DEDUMOBILE-2125 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUMOBILE-2125 |

## **02. SITUAÇÃO/REQUISITO**

Quando se cria uma mensagem com o objetivo de "Liberação ou digitação de nota de avaliação" existem várias tags que deveriam existir na mensagem com objetivo de "Liberação ou digitação de nota por etapa".

Nas mensagens de ocorrências também não colocamos as tags de Disciplina.

## **03. SOLUÇÃO**

Otimizado a inserção de novas TAGs para as mensagens:

* Matrícula e avaliação -  Cadastro de ocorrência;
* Matrícula e avaliação -  Liberação ou digitação de notas por etapa;
* Matrícula e avaliação -  Liberação ou digitação de faltas por etapa.

**CADASTRO DE OCORRÊNCIA**

Novas TAGs:

* CODDISC - Código da disciplina
* DISCIPLINA - Nome da disciplina

**LIBERAÇÃO OU DIGITAÇÃO DE NOTAS POR ETAPA**

Novas TAGs:

* CODDISC - Código da disciplina
* DISCIPLINA - Nome da disciplina
* MEDIA - Média da etapa
* PONTOSDIST - Pontos distribuídos na etapa
* NOTA - Nota que o aluno recebeu na etapa
* CONCEITO -  Conceito que o aluno recebeu na etapa

**LIBERAÇÃO OU DIGITAÇÃO DE FALTAS POR ETAPA**

Novas TAGs:

* CODDISC - Código da disciplina
* DISCIPLINA - Nome da disciplina
* FALTA -  Falta recebida na etapa
* FREQMIN - % da Frequência mínima a ser frequentada na etapa
