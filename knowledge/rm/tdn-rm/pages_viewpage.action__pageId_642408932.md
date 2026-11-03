---
content_hash: d0744a1516754d92f90d2b82037386ac6609d0e12c07fe2874ac434334a6c555
fetched_at: '2026-06-29T00:11:10.197676+00:00'
page_id: '642408932'
product: rm
source: tdn-rm
title: Cópia de Dados - Entidades do TOTVS Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642408932
version: 22
---

## **01. Visão Geral**

Utilizando a funcionalidade de Cópia de Dados é possível copiar parâmetros e entidades entre Coligadas. Pode ser utilizado tanto para a primeira configuração de uma nova Coligada ou para replicar dados entre Coligadas existentes. 

É possível criar **templates** determinando quais entidades do sistema devem ser copiadas. Para mais informações sobre este processo .

Disponível a partir da release **12.1.34.**

## **02. Entidades**

**Extremamente importante** seguir a **ordem** para plena execução da cópia. A não execução na ordem ocasionará em **erro** de **chave** **estrangeira**.

| Ordem | Id interno | Tabela | Entidade |
| --- | --- | --- | --- |
| 1 | 120 | STIPOCURSO | Nível de ensino |
| 2 | 141 | SCURSOHISTORICO | Curso do histórico |
| 3 | 147 | SSERIEHISTORICO | Série do histórico |
| 4 | 143 | SGRUPOHIST | Grupos de histórico |
| 5 | 144 | SGRUPOSERIE | Série do grupo |
| 6 | 142 | SDISCIPLINAHIST | Disciplina do histórico |
| 7 | 146 | SPARTEHIST | Parte do histórico |
| 8 | 145 | SMODELOLAYOUT | Layout de importação |
| 9 | 122 | SDISCIPLINA | Disciplina |
| 10 | 121 | SCURSO | Curso |
| 11 | 124 | SHABILITACAO | Habilitação / Série |
| 12 | 123 | SGRADE | Matriz curricular |
| 13 | 125 | SPERIODO | Período da matriz curricular |
| 14 | 127 | SDISCGRADE | Disciplina da matriz curricular |
| 15 | 129 | STURNO | Turno |
| 16 | 126 | SHABILITACAOFILIAL | Matriz aplicada |
| 17 | 130 | STIPOALUNO | Tipo do aluno |
| 18 | 131 | STIPOMATRICULA | Tipo de matrícula |
| 19 | 132 | SAREACONHECIMENTO | Área do conhecimento |
| 20 | 128 | SSTATUS | Situação de matrícula |
| 21 | 133 | SPLETIVO | Período letivo |
| 22 | 134 | SMODETAPAPLETIVO | Modelo de etapa por período letivo |
| 23 | 135 | SMOTIVOALTMAT | Motivo de alteração de matrícula |
| 24 | 136 | SOCORRENCIAGRUPO | Grupo de ocorrências |
| 25 | 137 | SOCORRENCIATIPO | Tipo de ocorrência |
| 26 | 153 | SSERVICO | Serviços |
| 27 | 148 | SBOLSA | Bolsas |
| 28 | 154 | SBOLSAPLETIVO | Bolsas por período letivo |
| 29 | 149 | SBOLSAFILIAL | Bolsas por filial |
| 30 | 152 | SPLANOPGTO | Plano de pagamento |
| 31 | 151 | SPARCPLANO | Parcelas do plano de pagamento |
| 32 | 158 | SHABILITACAOFILIALPL | Parametrização por curso |
| 33 | 150 | SHABMODELOPGTO | Séries/habilitações do plano de pagamento |
| 34 | 159 | SPARAM | Parâmetros da secretaria |
| 35 | 160 | SPARAM | Parâmetros da tesouraria**¹** |
| 36 | 161 | SPARAM | Parâmetros da matrícula**¹** |
| 37 | 162 | SPARAM | Parâmetros da integração contabilidade**¹** |
| 38 | 163 | SPARAM | Parâmetros da integração financeiro educacional**¹** |
| 39 | 164 | SPARAM | Parâmetros da integração folha |
| 40 | 165 | SPARAM | Parâmetros da integração ponto |
| 41 | 166 | SPARAM | Parâmetros do portal gerais |
| 42 | 167 | SPARAM | Parâmetros do portal matrícula**¹** |
| 43 | 168 | SPARAM | Parâmetros da geração de usuário**¹** |

Cópia de parâmetros

**Não** serão copiados os campos de **Relatório** e **Fórmula Visual** dos parâmetros.

**¹**Estas entidades possuem campos de outros módulos, caso o registro não exista na coligada destino o mesmo não será copiado e registro no log do processo. Exemplo: nos parâmetros de integração financeiro educacional existem campos que recebem os eventos contábeis. Se na origem estiver com algum evento contábil preenchido, o processo irá verificar se na coligada de destino este evento contábil existe, caso afirmativo o processo procederá com a cópia, caso não exista o campo não será copiado e tal informação será registrada em log. Vale lembrar que o fato de não copiar **não** irá bloquear a execução do processo.

Observações

Caso as informações abaixo estejam cadastradas o sistema não permite a realização da cópia.

* Na matriz curricular (SGRADE) quando tem o próximo curso cadastrado.
* No período letivo (SPLETIVO) quando tem o período letivo anterior e/ou calendário informado(s).
* No modelo de etapa do período letivo (SMODETAPAPLETIVO) quanto tem formula cadastrada.
