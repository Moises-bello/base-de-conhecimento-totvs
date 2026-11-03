---
content_hash: 96b23d4f747a330eb818cc8f20efe5935d4a1af87dfd216c0a1ac56a8b9a3001
fetched_at: '2026-06-29T00:10:06.696058+00:00'
page_id: '452719330'
product: rm
source: tdn-rm
title: Fórmulas - PTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719330
version: 9
---

**Fórmulas**

---

Cadastro de Fórmulas  
   
**Funções Específicas do TOTVS Automação de Ponto**  
   
**Funções A**  
**Funções B**  
**Funções C**  
**Funções D**  
**Funções E**  
**Funções F**  
**Funções H**  
**Funções I**  
**Funções L**  
**Funções M**  
**Funções N**  
**Funções P**  
**Funções R**  
**Funções S**  
**Funções T**  
**Funções V**

*Observação :*

Devemos considerar que o uso de fórmula para o lançamento no banco de horas diário ou para o lançamento no movimento são processos distintos no qual a fórmula deverá ser construída considerando a sua finalidade.

Portanto a fórmula que é utilizada para o lançamento no banco de horas diário não terá o mesmo resultado quando adicionada nos eventos para o lançamento no movimento.

Quando se utiliza fórmula de lançamento para o movimento deverá ser levado em consideração que esta tem que tratar o intervalo de datas que deve ser considerado para o cálculo. Lembrando que existem funções que tratam intervalo de datas e as próprias funções de início e fim do período mensal (IPM /FPM).

Exemplo de fórmula: EXTRAEXEC(PAR).

Quando associada a um evento que contém o código de cálculo 0040 esta será considerada para o movimento.  A verificação da fórmula para o movimento é executada uma única vez e será considerado no lugar da função PAR a data início do Período que está sendo calculado, portanto ela só irá retornar a extra executada deste dia.

Ao ser utilizada no menu: fórmula de lançamento para o banco de horas, no momento de calcular a jornada dia a dia do período, a fórmula também será executada, gerando um resultado para cada data do período de cálculo.
