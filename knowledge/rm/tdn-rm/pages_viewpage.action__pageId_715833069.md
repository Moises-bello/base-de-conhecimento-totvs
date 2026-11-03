---
content_hash: ce7902dec108fc9fa631827a5df2bfc6d3744cc664ff413a1b84fb5a76aca74c
fetched_at: '2026-06-29T00:11:26.260087+00:00'
page_id: '715833069'
product: rm
source: tdn-rm
title: Constantes TOTVS Aprovações e Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715833069
version: 5
---

As constantes do sistema são caracteres simples ou numerais que são usados para representar o status de um movimento, cotação, produto ou outros registros no sistema, quando este é gravado no banco de dados. Em alguns casos uma mesma constante pode representar status distintos, dependendo da parametrização do recurso ou processo do sistema. Conhecer o significado de cada um dos status e quando eles são atribuídos é importante na execução de algumas tarefas, como ao criar um filtro, executar uma sentença ou gerar um relatório gerencial.

Constantes de atendimento - Tabela HATENDIMENTOBASE

* **Prioridade do atendimento**

Define a prioridade do atendimento, gravando na tabela **HATENDIMENTOBASE**, e no campo **PRIORIDADE.**

| Constantes | Representação |
| --- | --- |
| 10 | Baixa |
| 100 | Normal |
| 1000 | Alta |
| 10000 | Urgente |

* **Grau de dificuldade**

Define o grau de dificuldade do atendimento, gravando na tabela **HATENDIMENTOBASE**, e no campo **GRAUDIFICULDADE.**

| Constantes | Representação |
| --- | --- |
| 10 | Baixo |
| 100 | Médio |
| 1000 | Alto |

* **Situação do atendimento**

Define a situação do atendimento, gravando na tabela **HATENDIMENTOBASE**, e no campo **CODSTATUS.**

| Constantes | Representação |
| --- | --- |
| A | Em andamento |
| R | Concluído a responder |
| O | Concluído respondido |
| F | Concluído confirmado |
| U | Concluído automático (pelo sistema) |
| V | Avaliado |
| G | Agendado responder |
| E | Agendado respondido |
| T | Agendado terceiros |
| C | Cancelado |
| D | Despertado |

Constantes Tipo de Atendimento - Tabela HTIPOATENDIMENTO

* **Status de validação**

Status de validação do tipo de atendimento para o uso do APP Minhas Aprovações, gravando na tabela **HTIPOATENDIMENTO**, no campo **STATUSAPP.**

| Constantes | Representação |
| --- | --- |
| 0 | Não validado |
| 1 | Validado com sucesso |
| 2 | Tipo de atendimento com inconsistência |

* **Notificar o responsável**

Notificar o responsável em todas as etapas do atendimento - APP Minhas Aprovações, gravando na tabela **HTIPOATENDIMENTO**, no campo **NOTIFICARAPP.**

| Constantes | Representação |
| --- | --- |
| 0 | Não notificar |
| 1 | Notificar |

* **Tipo de exibição**

Determina onde atendimentos desse tipo serão exibidos, gravando na tabela **HTIPOATENDIMENTO**, e no campo **TIPOEXIBIÇÃO.**

| Constantes | Representação |
| --- | --- |
| 0 | Não exibe |
| 1 | Exibe |

Constantes das Rotinas do Marketing - Tabela HPROSPECT e HPARAMMARKETING

* **Tipo de cliente**

Define o tipo de cliente gravando na tabela **HPROSPECT**, e no campo **TIPOCLIENTE.**

| Constantes | Representação |
| --- | --- |
| 0 | Inativo |
| 1 | Suspect |
| 2 | Prospect |

* **Categoria pessoa**

Indica se é Pessoa Física ou Jurídica, gravando na tabela **HPROSPECT**, e no campo **PESSOAFISOUJUR.**

| Constantes | Representação |
| --- | --- |
| F | Pessoa Física |
| J | Pessoa Jurídica |

* **Tipo do parâmetro**

Define o tipo do parâmetro, gravando na tabela **HPARAMMARKETING**, e no campo **TIPO.**

| Constantes | Representação |
| --- | --- |
| Inteiro | Inteiro |
| String | String |
| Real | Real |
| Data | Data |
| Texto | Texto |
| Boleano | Boleano |
| Link | Link |
| Tabela | Tabela |

* **Tipo de link**

Define o tipo de link do parâmetro (depende do tipo do parâmetro), gravando na tabela  **HPARAMMARKETING**, e no campo **TIPOLINK.**

| Constantes | Representação |
| --- | --- |
| Email | Email |
| URL | URL |
| SkypeLink | SkypeLink |

* **Exibir parâmetro**

Opções para exibição do tipo do parâmetro,  gravando na tabela **HPARAMMARKETING**, e no campo **EXIBIR.**

| Constantes | Representação |
| --- | --- |
| 0 | Nome |
| 1 | Descrição |
| 2 | Nome +Descrição |
