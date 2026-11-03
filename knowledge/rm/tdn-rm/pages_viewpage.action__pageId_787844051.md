---
content_hash: 9e72f084c7f11f594c543dfde1e7fc8615ef4b0060d75a82109795c7355cbf10
fetched_at: '2026-06-29T00:11:39.039827+00:00'
page_id: '787844051'
product: rm
source: tdn-rm
title: Excluir / Cancelar - Bolsa Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=787844051
version: 11
---

---

Temos as opções para que as bolsas selecionadas sejam excluídas ou canceladas dentro do contrato do aluno em *Anexo |* *Bolsas |* *Processos | Excluir/Cancelar bolsas.*

Caso realize o procedimento de excluir, as bolsas serão excluídas do contrato dos alunos e as bolsas utilizadas em lançamentos ou contabilizações não serão excluídas.

* Caso realize o procedimento de cancelar, as bolsas serão canceladas do contrato dos alunos e os lançamentos anteriores ao cancelamento das bolsas não sofrerão alterações.

Caso deseje realizar os procedimentos de excluir ou incluir bolsas que já foram utilizadas na geração de contabilização por competência o processo irá se comportamento da seguinte forma:

* Não será possível realizar o procedimento de exclusão de bolsas que possuam contabilização por competência. O processo exibirá a seguinte mensagem "*Não foi possível excluir a bolsa  '4 - GRUPO BMG', do contrato '661'. Bolsa já utilizada na geração de lançamentos do contrato ou na contabilização por competência"*

* Caso realize o procedimento de cancelamento de bolsa onde a bolsa foi contabilizada em lançamentos e competências anteriores, o sistema permitirá a cancelamento e fechará o valor da bolsa até o momento do cancelamento, gerando um estorno de cancelamento no contrato. Além disso, o sistema permitirá contabilizar os períodos após o cancelamento da bolsa

Bolsa de Crédito

Não é permitido cancelar Bolsas de Crédito, para cancelar a bolsa de crédito o lançamento tenta regerar a parcela e isso não é permitido.  
  
Ao executar o processo é exibido a mensagem: "Não é permitido regerar lançamentos quando existem lançamentos de bolsa de crédito e os lançamentos associados a parcela não estão todos cancelados".

 Informações Complementares

---
