---
content_hash: 10d4148845668d37d9964c188be1aeaf7a144e7c23026bda0176807c50513406
fetched_at: '2026-06-29T00:10:01.920986+00:00'
page_id: '452718795'
product: rm
source: tdn-rm
title: Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718795
version: 8
---

Nesta etapa o usuário irá definir como será feito o Lançamento Financeiro da folha de pagamento.

**Bloquear Recalculo do Envelope após Lançamento Financeiro**

Com o parâmetro marcado será bloqueado o envelope que tenha liquido de:

* Liquido Salarial
* Liquido Rescisão

Na geração do Lançamento serão validados, a seleção dos funcionários, competência e período para fazer o bloqueio do recalculo. Para liberar o envelope de pagamento para recálculo execute o processo de Desbloqueia Recálculo que está em Folha Mensal - Lançamentos, onde também é possível verificar quais envelopes foram bloqueados.

Caso o funcionário esteja na seleção e não possuir lançamento de liquido, o envelope não será bloqueado.

**Observação:**Não é possível realizar o bloqueio de envelopes de competências anteriores.

**Bloquear Geração de Lançamentos Financeiros Duplicados**

Com o parâmetro marcado, ao gerar o lançamento financeiro para o mesmo tipo de lançamento, mesma coligada, mesma chapa, mesmo ano, mês e período será verificado se já existem os lançamentos de liquido salarial, liquido de rescisão e liquido de férias. Caso já existam estes lançamentos,  será gerada mensagem de aviso ao final da execução do processo informando que já foi gerado um lançamento semelhante e não será gravado. O usuário deverá excluir este lançamento para conseguir gerar um novo.

Com o parâmetro desmarcado, ao gerar o lançamento financeiro para o mesmo tipo de lançamento, mesma coligada, mesma chapa, mesmo ano, mês e período, os campos mês, ano e período na tabela PFITEMLAN não serão preenchidos. Caso já existam estes lançamentos,  será gerada mensagem de aviso ao final da execução do processo informando que já foi gerado um lançamento semelhante e será duplicado.

**Observações:**

1. Ao marcar o parâmetro "Bloquear Geração de Lançamentos Financeiros Duplicados", o parâmetro "Bloquear Lançamento Financeiro do mesmo fato gerador" será desconsiderado para os lançamentos de liquido salarial, liquido de rescisão e liquido de férias.
2. Para correto funcionamento o parâmetro "Usar histórico padrão" no cadastro do lançamento financeiro deve estar marcado.
3. Somente o lançamento de liquido de férias que não preenche o período porque é gerado com o recibo de férias**.**
4. Para esse parâmetro funcionar existem campos (MESCOMP, ANOCOMP e NROPERIODO) na tabela PFITEMLAN que precisam estar preenchidos e somente serão preenchidos com o parâmetro marcado.   
   Como dito acima com o **parâmetro desmarcado**, ao gerar o lançamento financeiro para o mesmo tipo de lançamento, mesma coligada, mesma chapa, mesmo ano, mês e período, os campos mês, ano e período na tabela PFITEMLAN **não** serão preenchidos. Então nesse caso se gerar o lançamento com o parâmetro desmarcado e logo após marcar o parâmetro, o usuário deverá cancelar e excluir o lançamento feito antes da marcação do parâmetro e executar a geração do lançamento financeiro novamente para que os campos  mês, ano e período sejam preenchidos e com isso passar a validar o parâmetro de bloquear lançamentos duplicados.

---

<<Voltar para tela anterior **Folha Normal**
