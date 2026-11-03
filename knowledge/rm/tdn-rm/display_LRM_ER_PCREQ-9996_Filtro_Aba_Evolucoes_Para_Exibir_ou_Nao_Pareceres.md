---
content_hash: 341e2a47cf1af5315aec497a240e9b67645f468c2abd81acc3d41b8999a8c960
fetched_at: '2026-06-29T00:06:27.449589+00:00'
page_id: '232822143'
product: rm
source: tdn-rm
title: ER_PCREQ-9996_Filtro_Aba_Evolucoes_Para_Exibir_ou_Nao_Pareceres
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9996_Filtro_Aba_Evolucoes_Para_Exibir_ou_Nao_Pareceres
version: 122
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Novo Filtro na aba de Evoluções para ver ou não os Pareceres

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Prontuário |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-9991 |
| **Requisito1** | PCREQ-9996 | **Subtarefa1** | SAU\_DEV-4212 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

O objetivo desta implementação é disponibilizar um novo filtro onde o médico possa filtrar as evoluções que deseja visualizar. Ele poderá visualizar todos as evoluções ou visualizar somente os pareceres de determinada especialidade.

### (Obrigatório)

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Evolução Médica | [Alteração] | Prontuário | Criar um checkbox com o texto "Exibir parecer de especialistas" cujo valor default é marcado e incluir um combo que listará as especialidades médicas.  Com o checkbox marcado, o sistema exibirá todos as evoluções, tanto de pareceres solicitados quanto as evoluções dos médicos. Ao selecionar uma especialidade, o sistema exibirá somente os pareceres daquela especialidade. Para exibir os pareceres de todas as especialidades, basta pressionar a tecla Backspace que limpará o item selecionado e sair do campo.  Com checkbox desmarcado o sistema exibirá somente as evoluções médicas que não são os pareceres de especialistas. |

**Tabelas Utilizadas**

* SZEVOLUCAO – Evolução médica
* SZPARECERPEP– Parecer de especialistar

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
