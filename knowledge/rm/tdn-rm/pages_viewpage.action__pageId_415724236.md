---
content_hash: c028fcee9521e1184da7d93523ff6280c5adb8f95986a7b314accee0ac827f44
fetched_at: '2026-06-29T00:09:12.182350+00:00'
page_id: '415724236'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-3378 DT Tipo Contábil para Lançamentos de Bolsa de Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415724236
version: 9
---

# TIPO CONTÁBIL PARA LANÇAMENTOS DE BOLSA DE CRÉDITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração de Lançamentos* | *Geração de Lançamentos* | |
| **Cadastros Iniciais:** | *Contrato, Parcela, Bolsa de Crédito* |
| **Parâmetro(s):** | **Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4 | Tipo contábil Bolsa de Crédito** |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | **DEDUINTEGRACOES-3378** |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *N/A.* |

## Objetivo

Com o objetivo de flexibilizar a escolha do tipo contábil de lançamentos de bolsa de crédito, foi criado o parâmetro "Tipo Contábil Bolsa de Crédito" em Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin - Geral 2/4. Isso dá mais liberdade para contabilização desses lançamentos utilizando o regime de caixa já que o tipo contábil do lançamento de bolsa de crédito não fica mais preso ao tipo contábil do lançamento do aluno.

**Parâmetro**

**Descrição**

Anteriormente, o usuário só possuía duas opções de preenchimento do tipo contábil dos lançamentos de bolsa de crédito dependendo da marcação do parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil", ou seja, caso o parâmetro estivesse DESMARCADO, o lançamento de bolsa de crédito era gerado com o tipo contábil do lançamento do aluno e, caso esse parâmetro estivesse MARCADO, o tipo contábil do lançamento de bolsa de crédito era gerado como "Baixa Contábil".

Com a criação do parâmetro "Tipo Contábil Bolsa de Crédito", os lançamentos de bolsa de crédito serão gerados com o tipo contábil selecionado nesse parâmetro. Caso o mesmo não tenha um valor selecionado, o tipo contábil do lançamento de bolsa de crédito será o mesmo tipo contábil do lançamento do aluno, EXCETO, se o parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil" estiver MARCADO.

IMPORTANTE

A marcação do parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil" é mandatória no preenchimento do tipo contábil na geração do lançamento de bolsa de crédito, ou seja, caso o mesmo esteja MARCADO, o tipo contábil dos lançamentos de bolsa de crédito sempre será "Baixa contábil" independente do valor selecionado do novo parâmetro que está sendo criado.

Caso seja marcado o parâmetro citado, será exibida a seguinte mensagem para o usuário:

OBSERVAÇÃO

A partir da versão 12.1.23 o parâmetro "Gerar lançamento de bolsa de crédito como Baixa Contábil" **não existirá** no sistema.   
Para os contextos que tem esse parâmetro marcado o sistema irá definir o valor "Baixa Contábil" no parâmetro "**Tipo contábil Bolsa Crédito**".

O usuário deverá utilizar o parâmetro "**Tipo contábil Bolsa Crédito**" para definir o tipo contábil do lançamento, ou utilizar o valor padrão definido no parâmetro "**Tipo contábil padrão**".

**A seguir exemplos para as versões 12.1.20, 12.1.21, 12.1.22, 12.1.23 ou superior.**

---

**Segue os exemplos referente aos parâmetros "Gerar lançamentos de bolsa de crédito como Baixa Contábil", "Tipo contábil Bolsa Crédito" e "Tipo contábil padrão" para as versões 12.1.20, 12.1.21 e 12.1.22**

**Exemplos:**

(Exemplo 1)

Parcela: R$ 1000,00.  
Bolsa de Crédito: 50% (FIES)  
Parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil" DESMARCADO  
Parâmetro "Tipo contábil padrão": Contábil  
Parâmetro "Tipo contábil Bolsa Crédito": Nenhum

**RESULTADO ESPERADO** => Sistema irá gerar dois lançamentos contábeis (um lançamento para o aluno e outro para a bolsa de crédito)

Lançamento aluno: R$ 1000,00 (Contábil)  
Lançamento FIES: R$ 500,00 (Contábil)

---

(Exemplo 2)

Parcela: R$ 1000,00.  
Bolsa de Crédito: 50% (FIES)  
Parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil" MARCADO  
Parâmetro "Tipo contábil padrão": Contábil  
Parâmetro "Tipo contábil Bolsa Crédito": Nenhum

**RESULTADO ESPERADO** => Sistema irá gerar o lançamento do aluno como "Contábil" e o lançamento de bolsa de crédito como "Baixa Contábil"

Lançamento aluno: R$ 1000,00 (Contábil)  
Lançamento FIES: R$ 500,00 (Baixa Contábil)

---

(Exemplo 3)

Parcela: R$ 1000,00.  
Bolsa de Crédito: 50% (FIES)  
Parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil" MARCADO  
Parâmetro "Tipo contábil padrão": Contábil  
Parâmetro "Tipo contábil Bolsa Crédito": Não contábil

**RESULTADO ESPERADO** => Sistema irá gerar o lançamento do aluno como "Contábil" e o lançamento de bolsa de crédito como "Baixa Contábil"

Lançamento aluno: R$ 1000,00 (Contábil)  
Lançamento FIES: R$ 500,00 (Baixa Contábil)

---

(Exemplo 4)

Parcela: R$ 1000,00.  
Bolsa de Crédito: 50% (FIES)  
Parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil" DESMARCADO  
Parâmetro "Tipo contábil padrão": Contábil  
Parâmetro "Tipo contábil Bolsa Crédito": Não contábil

**RESULTADO ESPERADO** => Sistema irá gerar o lançamento do aluno como "Contábil" e o lançamento de bolsa de crédito como "Não Contábil"

Lançamento aluno: R$ 1000,00 (Contábil)  
Lançamento FIES: R$ 500,00 (Não Contábil)

---

**Segue os exemplos referente aos parâmetros  "Tipo contábil Bolsa Crédito" e "Tipo contábil padrão" para a versão 12.1.23 ou superior. Vale ressaltar que na versão 12.1.23 ou superior o parâmetro "Gerar lançamentos de bolsa de crédito como Baixa Contábil" não estará presente no sistema.**

**Exemplos:**

(Exemplo 1)

Parcela: R$ 1000,00.  
Bolsa de Crédito: 50% (FIES)  
Parâmetro "Tipo contábil padrão": Contábil  
Parâmetro "Tipo contábil Bolsa Crédito": Nenhum

**RESULTADO ESPERADO** => Sistema irá gerar dois lançamentos contábeis (um lançamento para o aluno e outro para a bolsa de crédito)

Lançamento aluno: R$ 1000,00 (Contábil)  
Lançamento FIES: R$ 500,00 (Contábil)

---

(Exemplo 2)

Parcela: R$ 1000,00.  
Bolsa de Crédito: 50% (FIES)  
Parâmetro "Tipo contábil padrão": Contábil  
Parâmetro "Tipo contábil Bolsa Crédito": Não contábil

**RESULTADO ESPERADO** => Sistema irá gerar o lançamento do aluno como "Contábil" e o lançamento de bolsa de crédito como "Não Contábil"

Lançamento aluno: R$ 1000,00 (Contábil)  
Lançamento FIES: R$ 500,00 (Não Contábil)
