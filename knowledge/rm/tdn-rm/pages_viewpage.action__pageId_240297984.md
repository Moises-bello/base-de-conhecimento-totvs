---
content_hash: 18ba02dea0dcf420f86f473a0767fccaf27604fbaa9e36c172062ab41b1d17c1
fetched_at: '2026-06-29T00:08:09.972870+00:00'
page_id: '240297984'
product: rm
source: tdn-rm
title: Demonstrativo do Cálculo - Reprogramação Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240297984
version: 7
---

**1) Atividade Extra**

Log de Cálculo da Reprogramação Salarial:

Atividade Extra: [1]   
 CompõeSalário = Sim, Carga Horária = 33, EquivalênciaHoraAula = 1, ValorHora = 20,00, ValorHoraTitulacao = 35,00, SalárioHoraDoProfessor = 25,00  
 [Período da Atividade] - Início:01/01/2016 - Fim 31/12/2016  
 \* Atividade contempla todo o período da competência  
 [Horas] = (CargaHorária(33) \* EquivalênciaHoraAula(1)) \* FatorCalculoMensal(1)  
 [Horas] = 033:00  
 [Valor] valorConsiderado = ValorHoraDaAtividade(20,0000)  
 [Valor] = valorConsiderado(20,0000) \* Horas(33)  
 [Valor] = 660,00

Verificando se o Grupo de atividade da Atividade Extra Compõe ou não o salário.

Na atividade extra é considerado a carga horário, equiv. hora/aula e o valor da hora para o cálculo.

O sistema busca as atividades no período informado em Data inicial e Data Final.

Nos parâmetros da Folha de Pagamento é verificado o Fator para cálculo da atividade extra.

**2) Turma Disciplina**

Log de Cálculo da Reprogramação Salarial:

Atividade Turma/Disciplina: [TOTVS\_INT/A9313]

CompõeSalário = Sim, NºAulas = 5,00, ValorHoraDaAtividade = 25,00, ValorFixo = 0,00, SalárioHoraDoProfessor = 25,00, ValorHoraTitulacao = 35,00

[Período da Atividade] - Início:01/01/2016 - Fim 31/12/2020  
 [Horas] = Número Aulas Semanais(5,00) \* FatorCalculoMensal(4,50)  
 [Horas] = 022:30  
 [Valor] valorConsiderado = ValorHoraDaAtividade(25,0000)  
 [Valor] = (valorConsiderado(25,0000) \* Horas(22,5))  
 [Valor] = 562,50

Fator considerado para o cálculo do salário na turma/disciplina.

Valor da hora na titulação.

Nos parâmetros do Educacional é verificado se o valor da hora/aula considerado será do professor na tuma/disciplina ou na titulação.

**3) Atividades Ofertadas**

Atividade Complementar: [2]   
 CompõeSalário = Não, Carga Horária = 150, EquivalênciaHoraAula = 1, ValorHora = 19,00, ValorHoraTitulacao = 0,00, SalárioHoraDoProfessor = 22,03  
 [Período da Atividade] - Início:01/01/2016 - Fim 01/01/2020  
 \* Atividade contempla todo o período da competência  
 [Horas] = (CargaHorária(150) \* EquivalênciaHoraAula(1)) \* FatorCalculoMensal(1)  
 [Horas] = 150:00  
 [Valor] valorConsiderado = ValorHoraDaAtividade(19,0000)  
 [Valor] = valorConsiderado(19,0000) \* Horas(150)  
 [Valor] = 2.850,00

Deve cadastrar o grupo de atividade como atividade extra do professor, mesmo sendo atividade ofertada.

Será verificado no cálculo a Carga Horária, Equiv. hora aula, Valor da hora e se a atividade compõe salário.

Após a reprogramação salarial o sistema cadastrada o evento definido no grupo de atividades no código fixo:
