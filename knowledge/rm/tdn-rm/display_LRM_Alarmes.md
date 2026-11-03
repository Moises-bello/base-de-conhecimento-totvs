---
content_hash: a8b93c6b960cd2cf4998c9c685e5e115cd33d0d73727dfe0d0ce824ce3394e85
fetched_at: '2026-06-29T00:09:30.351282+00:00'
page_id: '425458437'
product: rm
source: tdn-rm
title: Alarmes
type: documentation
url: https://tdn.totvs.com/display/LRM/Alarmes
version: 3
---

**Alarmes**

---

O atendimento é uma atividade que precisa ser executada e dada uma resposta ao cliente (FeedBack). Para evitar a falta de resposta, existe o serviço de alarmar atendimentos que avisa o superior imediato (via e-mail) da situação dos atendimentos com prazos vencidos.    
   
**Critérios de Alarme**  
   
A parametrização é utilizada para configurar em quanto tempo o atendimento será considerado como alarmado. Envolve três características do atendimento e três condições.  Os tempos, para considerar o atendimento alarmado, devem ser parametrizados para cada uma das possíveis combinações (se assim desejar o cliente) entres as três características do atendimento:   
Status;   
Classificação;   
Prioridade.

* **Condição 1: Número máximo de horas em aberto com o responsável atual**

Número de dias ou minutos (se assim parametrizado em Gerais, conforme descrito abaixo) em que um atendimento com a combinação X (explicação dada logo acima) pode ficar com o mesmo atendente. Vencendo este prazo, o alarme será disparado.

* **Condição 2: Tempo máximo de resposta (em horas desde a data de abertura)**

Número total de dias ou minutos (se assim parametrizado em Gerais, conforme descrito abaixo) em que um atendimento pode ficar aberto sem ser totalmente finalizado, ou seja, com a combinação X (explicação dada logo acima).

* **Condição 3: Considerar todos os atendimentos com "Prazo limite" vencido**

Se o campo prazo limite estiver preenchido no atendimento e o mesmo vencer, também será disparado o alarme  
   
   
**Gerais**

* Utilizar a unidade em minutos ao invés de horas para calcular os alarmes

Indicativo se o tempo para que o atendimento passe para a condição de alarmado pode ser definida em horas ou então em minutos.
