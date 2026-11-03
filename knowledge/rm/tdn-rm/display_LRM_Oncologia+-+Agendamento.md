---
content_hash: 0b59bf896f7286c0e6097df5a6a199779e1790cf565ef1bc0fae9ecc38a7a52e
fetched_at: '2026-06-29T00:05:48.764809+00:00'
page_id: '1028942917'
product: rm
source: tdn-rm
title: Oncologia - Agendamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Oncologia+-+Agendamento
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parametrizações no RM**
3. **Exemplo de utilização**

Tratamento1. Visão Geral

## **01. VISÃO GERAL**

##### **Funcionalidade disponível a partir da versão 12.1.2602.**

A nova tela de "Agendamento" no modulo de Oncologia no PEP tem como objetivo permitir que a equipe assistencial visualize, gerencie e confirme os agendamentos dos ciclos e dias de tratamento oncológico, garantindo controle operacional, rastreabilidade e integração com a dispensação de medicamentos.

Nesta tela, o usuário acompanha todos os ciclos e dias dos protocolos do paciente, visualizando status, datas previstas e profissionais responsáveis, com foco exclusivo na gestão do agendamento sem realizar novas prescrições ou suspensões no tratamento já planejado.

2. Parametrização

## **02. PARAMETRIZAÇÕES NO RM**

A utilização do agendamento dos dias de realização da quimioterapia estão vinculados a parametrização por unidade de atendimento. O cadastro deve ser realizado através do caminho: RM → Cadastro → Oncologia → Motivos de agendamento.

O cadastro de **Motivos de Agendamento/Reagendamento** tem como objetivo padronizar e registrar as justificativas utilizadas pela equipe assistencial ao:

* Alterar datas previstas
* Remover datas previstas
* Reagendar ciclos/dias de protocolos oncológicos

Essas informações são fundamentais para:

* Rastreabilidade
* Auditoria
* Segurança assistencial
* Análise de indicadores operacionais

O cadastro deve ser realizado através do caminho: RM → Cadastro → Oncologia → Motivos de agendamento

3. Exemplo de utilização

## **03. EXEMPLO DE UTILIZAÇÃO - A partir da versão 2602.**

A tela apresenta uma tabela única, onde cada linha representa um dia de um ciclo do protocolo de tratamento oncológico.

### Colunas exibidas na tabela:

* **Status** **do agendamento**
* **Status da prescrição**
* **Protocolo**
* **Fase**
* **Ciclo**
* **Dia**
* **Data prevista**
* **Responsável**

Essa estrutura permite que a equipe visualize rapidamente:

* Quais dias já estão confirmados
* Quais prescrição estão pendentes de liberação pelo médico
* Quais ainda aguardam confirmação
* Quais estão sem data prevista e precisam de ação

Cada linha da tabela pode assumir um dos seguintes status de agendamento:

| **Status** | **Descrição** |
| --- | --- |
| **Não utiliza** | Indica que a unidade não utiliza o agendamento |
| **Aguardando confirmação** | Indica que o ciclo/dia possui uma **data prevista cadastrada**, porém o agendamento **ainda não foi confirmado** pela equipe assistencial. |
| **Confirmado** | Indica que o **agendamento foi confirmado** pelo profissional responsável. |
| **Sem data prevista** | Utilizado quando o ciclo/dia **possuía data prevista**, mas ela foi removida por algum motivo, como:• Paciente internado• Necessidade de reagendamento• Intercorrência clínica. **Exige justificativa obrigatória**. |
| **Liberado para a farmácia** | Data prevista confirmada e dispensação dos medicamentos solicitada |

Cada linha da tabela pode assumir um dos seguintes status da prescrição:

| **Status** | **Descrição** |
| --- | --- |
| **Liberado** | Indica que a prescrição foi liberada e está pronta para realização da dispensação |
| **Pendente** | Indica que a prescrição está pendente de liberação pela equipe médica |
| **Suspenso** | Prescrição suspensa pela equipe médica |

Ao expandir uma linha da tabela, é aberto uma telalateral, que centraliza todas as ações permitidas para aquele ciclo/dia. O comporto pelas informações relacionadas ao Protocolo, finalidade, status do tratamento e a data prevista do ciclo.

A gestão do agendamento é realizada através das ações:

| Ação | Descrição | Regras / Observações |
| --- | --- | --- |
| **Alterar data prevista** | Permite informar uma nova data para o ciclo/dia selecionado. | Justificativa obrigatória - A alteração fica registrada para fins de auditoria e rastreabilidade |
| **Marcar como “Sem data prevista”** | Utilizado quando não é possível definir uma data naquele momento. | Justificativa obrigatória - O ciclo/dia passa para o status "Sem data prevista" e o campo referente a data prevista na tabela fica vazio. |
| **Confirmar agendamento** | Confirma oficialmente o agendamento do dia. | Atualiza o status da tabela para "Confirmado" |
| **Solicitar dispensação da medicação** | Solicita o envio das medicações vinculadas ao ciclo/dia. | Disponível somente se a prescrição estiver liberada pelo médico - As medicações são enviadas para o painel de dispensação, respeitando a data confirmada. A ação depende da configuração da unidade para uso de agendamento |

**Logs de alterações** na aba de Agendamento:

Para garantir a segurança assistencial e a rastreabilidade das ações realizadas, o sistema registra automaticamente as interações realizadas nos agendamentos.

Ao clicar na opção "Log de alterações", o sistema listará a data e hora da alteração, usuário responsável e justificativa (quando aplicável) dos seguintes eventos:

* Tratamento adicionado e iniciado
* Confirmação e alterações da data prevista
* Solicitação dedispensação da medicação

## **3.1** **INTEGRAÇÃO ENTRE TRATAMENTO, PRESCRIÇÃO E AGENDAMENTO**

### Quando a unidade **UTILIZA agendamento**

Os dias do ciclo podem assumir diferentes estados, que impactam diretamente a possibilidade de alteração de datas:

| Ação | Com agendamento |
| --- | --- |
| Dia de tratamento não liberado | A data ainda pode ser alterada. |
| Dia de tratamento liberado pelo médico | A data ainda pode ser alterada. |
| Dia de tratamento com agendamento confirmado | Não pode ser alterada na aba de tratamento e qualquer ajuste deve ser feito via reagendamento, com justificativa. |
| Dia de tratamento liberado para farmácia | A data não pode mais ser alterada. |

A data do ciclo continua respeitando a regra de não ser maior que os dias já liberados.

### Quando a unidade NÃO utiliza agendamento

Ao liberar um dia de tratamento na tela de "Quimioterapia", a requisição com os medicamentos é enviada no mesmo momento para a farmácia.

Nesse cenário:

| Ação | Sem agendamento |
| --- | --- |
| Dia de tratamento não liberado | A data pode ser alterada, respeitando a ordem cronológica definida no protocolo adicionado. |
| Dia de tratamento liberado | Não pode ter a data alterada. |

A data do ciclo segue a mesma regra geral: não pode ser posterior a dias já liberados.

### Impacto prático para o usuário

* A data inicial do ciclo define o limite mínimo para todos os dias.
* O sistema impede datas incoerentes automaticamente.
* Quanto mais avançado o status do dia (liberação ou confirmação), menor a flexibilidade para alteração de datas.

Essas regras garantem alinhamento entre:

* Planejamento clínico
* Prescrição médica
* Agendamento
* Dispensação pela farmácia
