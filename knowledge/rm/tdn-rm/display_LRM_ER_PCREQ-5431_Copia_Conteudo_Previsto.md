---
content_hash: 1587f423f08029a7f3a477bff594e41060f337ee40fc9ebc744d5660b1c0ccb6
fetched_at: '2026-06-29T00:06:18.978596+00:00'
page_id: '219694459'
product: rm
source: tdn-rm
title: ER_PCREQ-5431_Copia_Conteudo_Previsto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5431_Copia_Conteudo_Previsto
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | WBS\_R\_EDU016\_1219 | **IRM1** | PCREQ-5430 |
| **Requisito1** | PCREQ-5431 | **Subtarefa1** | PDR\_EDU\_EDU011-511 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Incluir na funcionalidade de cópia de conteúdo da tela de digitação de plano de aula do Portal Educacional as opções de:

* Copiar o conteúdo previsto para a próxima aula;
* Copiar o conteúdo previsto para as aulas em sequência;

## Definição da Regra de Negócio

#### Cenário atual:

```
A tela de digitação de plano de aula do Portal Educacional permite ao usuário realizar as seguintes operações:
```

* Copiar o conteúdo previsto para o realizado;
* Copiar o conteúdo (previsto, realizado, lição de casa e arquivos associados) para outra turma/disciplina;
* Copiar o conteúdo realizado para a próxima aula;
* Copiar o conteúdo realizado para as aulas em sequência;
* Associar arquivos às aulas;
* Desassociar arquivos das aulas;

#### Cenário proposto:

```
Incluir na tela de digitação de plano de aula do Portal Educacional as 2 (duas) opções a seguir:
```

* Copiar o conteúdo previsto para a próxima aula - deve copiar  conteúdo previsto da aula selecionada para a próxima aula, desde que a data da próxima aula seja igual ou posterior à data atual;
* Copiar o conteúdo previsto para as aulas em sequência - deve copiar o conteúdo previsto para as aulas em sequência, desde que essas aulas sejam no mesmo dia da aula de origem;

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Copiar conteúdo previsto para próxima aula | [Criação] | [Portal Educacional -> Professor-> Diário de Classe -> Plano de Aula] | - |
| Copiar conteúdo previsto para aulas em sequência | [Criação] | [Portal Educacional -> Professor-> Diário de Classe -> Plano de Aula] | - |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
