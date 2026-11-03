---
content_hash: 8d48c3796979a83695d6a920f6537bdf8f1b20f7ae39ab195b711ded43317d05
fetched_at: '2026-06-29T00:12:09.143299+00:00'
page_id: '939253408'
product: rm
source: tdn-rm
title: Processo de Atualização de Período na Matrícula do Período Letivo (Corrente)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939253408
version: 57
---

Será disponível a partir da 12.1.2410.

O processo está disponível no menu **Assistentes**, dentro da seção **Atividades Acadêmicas**, com o nome **"Validação e atualização do período".**

Leia com atenção antes de executar o processo!

Este documento descreve, passo a passo, como o sistema calcula e persiste o **período sugerido** de cada matrícula no período letivo vigente durante a execução do processo.

---

## Objetivo

Alguns registros de matrícula do período letivo podem apresentar o campo **período** em branco ou preenchido de forma incorreta.

Este processo tem como objetivo identificar os alunos com essa informação ausente ou inválida e, em seguida, atualizá-la automaticamente com o período sugerido pelo sistema. O período é identificado a partir de uma análise curricular do aluno e parâmetros que você pode definir antes da execução do cálculo. 

Essa atualização é essencial para a correta execução do **Planejamento de Ofertas:** .

No próximo tópico, são apresentadas as validações iniciais necessárias para a execução do processo.

---

## Validações

Este processo considera apenas matriculas no *período letivo corrente*, conforme definido nos parâmetros do sistema - .  
A data de execução do processo deve estar dentro do intervalo de datas definido para o período letivo corrente (data de início e data de fim, ou previsão de fim).  
Caso a data de execução esteja fora desse intervalo, o sistema exibirá uma mensagem informando qual é o período letivo corrente e alertando que a data atual não está compatível com ele.

O momento ideal para a execução deste processo é após a finalização das matrículas e cerca de um, dois, meses após o início das aulas do período letivo corrente, desde que este período esteja devidamente informado nos parâmetros do sistema. A execução deve ocorrer antes do início do planejamento da próxima oferta (próximo período letivo).  
Exemplo:  
Se o período letivo corrente for 2026/1 (1º semestre de 2026), o momento ideal para a execução do processo será por volta do final de março, quando as matrículas de 2026/1 já estiverem encerradas e o planejamento de 2026/2 estiver prestes a começar.  
O período a ser atualizado será de 2026/1.

Exemplo

🗓 **Período Letivo Corrente**

* **Dt. Início:** 01/02/2025
* **Dt. Fim:** 30/06/2025

| **Data de Execução** | **Pode executar processo** |
| --- | --- |
| 01/02/2025 | ✅ Válido |
| 15/03/2025 | ✅ Válido |
| 30/06/2025 | ✅ Válido |
| 31/01/2025 | ❌ Inválido |
| 01/07/2025 | ❌ Inválido |
| 15/01/2025 | ❌ Inválido |
| 01/08/2025 | ❌ Inválido |

---

true

## Visão do processo

### Filtro

Após a etapa de introdução do processo, com o respectivo resumo e validação do período letivo corrente, você será direcionado para a tela de seleção de alunos.

Nessa tela, será possível aplicar filtros para pré-selecionar os alunos que deseja visualizar. Em um segundo momento, você poderá escolher, linha por linha, quais alunos deseja atualizar com o período sugerido.

O filtro disponível é genérico, permitindo que você defina os critérios conforme sua necessidade.

Importante

Independentemente dos filtros aplicados, o sistema sempre adicionará automaticamente o filtro do período letivo corrente. Isso garante que somente os alunos com matrícula nesse período letivo  sejam exibidos nos resultados.

### Pré-visualização

Ao marcar o checkbox **"Desejo pré-visualizar sugestão do período"** e realizar a consulta, será possível visualizar no grid os valores calculados do período para cada um dos modelos de cálculo disponíveis, sem alterar o período do aluno na matrícula.

Ao utilizar essa funcionalidade, com base na análise curricular individual de cada aluno, o sistema aplicará os dois modelos de cálculo disponíveis e apresentará duas sugestões de período. A partir dessas sugestões, você poderá avaliar e decidir qual delas deseja salvar posteriormente.

Cuidado

Ao marcar esta opção, você poderá enfrentar um tempo maior de espera, pois será necessário buscar informações curriculares detalhadas para cada registro filtrado antes de exibir a sugestão de período.

---

true

## Período sugerido

O processo disponibiliza dois modelos de cálculo para sugerir o período do aluno.

Ao selecionar a opção **"Pré-visualizar o resultado do processo"**, o sistema exibirá duas colunas com as sugestões geradas: **Período Modelo 1** e **Período Modelo 2**, permitindo que você compare ambas as alternativas com base nos cálculos predefinidos.

Importante

Se ambos os valores sugeridos (Modelo 1 e Modelo 2) forem iguais ao período atual do aluno, o registro do respectivo aluno **não será exibido na listagem**. Isso ocorre porque, segundo os cálculos aplicados, o período atual já é considerado correto

O período sugerido será, **no máximo,** igual ao total de  da .

### 📘 Modelo 1 – Limiar de Conclusão (Baseado em Percentual)

Este modelo avalia o progresso do aluno com base na conclusão de disciplinas obrigatórias em cada período curricular, considerando um percentual mínimo pré-definido (**você pode alterar**, por padrão é: **80%**).

O sistema percorre, em ordem, os períodos curriculares do aluno — do 1º até o último — e verifica, em cada um, se o percentual de disciplinas obrigatórias concluídas atinge o limiar configurado. O processamento é interrompido no primeiro período em que o percentual não for atingido. Esse será o período sugerido.

**Exemplo de cálculo:**

* **Período 1**: 10 disciplinas obrigatórias, 8 concluídas → **80%** → Concluído
* **Período 2**: 10 disciplinas obrigatórias, 9 concluídas → **90%** → Concluído
* **Período 3**: 10 disciplinas obrigatórias, 5 concluídas → **50%** → **Não concluído**
* **Período 4**: 10 disciplinas obrigatórias, 2 concluídas → **20%** → **Não concluído**

👉 **Resultado sugerido:** Período **3**

**Exemplo 2 de cálculo:**

* **Período 1**: 10 disciplinas obrigatórias, 2 concluídas → **20%** → **Não concluído**
* **Período 2**: 10 disciplinas obrigatórias, 9 concluídas → **90%** → Concluído
* **Período 3**: 10 disciplinas obrigatórias, 5 concluídas → **50%** → **Não concluído**
* **Período 4**: 10 disciplinas obrigatórias, 2 concluídas → **20%** → **Não concluído**

👉 **Resultado sugerido:** Período **1**

### 📗 **Modelo 2 – Cálculo Aritmético Clássico (Baseado em Média)**

Este modelo define o período sugerido com base na média de disciplinas obrigatórias por período, considerando o total de disciplinas concluídas pelo aluno.

**Etapas do cálculo:**

1. *Calcular a média de disciplinas por período:*  
   *Média = Total de disciplinas obrigatórias / Total de períodos curriculares*
2. *Determinar o período sugerido:*  
   *Período sugerido = Truncar(Disciplinas obrigatórias concluídas / Média) + 1*

O período sugerido será o resultado obtido pelo truncamento (corte da parte decimal do número, removendo os dígitos após a vírgula, sem arredondar) da quantidade de disciplinas obrigatórias concluídas dividida pela média de disciplinas, somado mais 1.

**Exemplo 1 de cálculo:**

* Total de disciplinas obrigatórias: **40**
* Total de períodos curriculares: **8**
* **Média** = 40 / 8 = **5 disciplinas por período**
* Disciplinas obrigatórias concluídas pelo aluno: **29**
* **Período sugerido** = 29 / 5 =5,8 → Truncado para 5 → Somado + 1 = **6**

👉 **Resultado sugerido:** Período **6**

**Exemplo 2 de cálculo:**

* Total de disciplinas obrigatórias: **48**
* Total de períodos curriculares: **10**
* **Média** = 48 / 10 = **4,8 disciplinas por período → Truncado para 4 →  4 disciplinas por período**
* Disciplinas obrigatórias concluídas pelo aluno: **47**
* **Período sugerido** = 47 / 4 =11,75 → Truncado para 11 → Somado + 1 = **12 →** Atingiu o limite total de períodos que é igual a **10** → Portanto o período será **10**.

**👉 Resultado sugerido:** Período **10**

### **Resultado Detalhado**

Após a execução do processo, você poderá visualizar os valores utilizados no cálculo para cada aluno selecionado.

Essa funcionalidade permite uma **revisão detalhada** dos critérios considerados, oferecendo mais transparência sobre os resultados gerados.
