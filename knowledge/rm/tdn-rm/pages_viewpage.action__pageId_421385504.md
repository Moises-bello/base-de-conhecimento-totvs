---
content_hash: 7471959a7f843efa3e9f82de017927a037aef8744e36165f84f6d6d7054cf167
fetched_at: '2026-06-29T00:09:16.289835+00:00'
page_id: '421385504'
product: rm
source: tdn-rm
title: Gerar Apropriação de Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385504
version: 14
---

---

O processo realiza a apropriação de mão de obra de apontamentos de mobilidade originados do coletor móvel confrontados com as horas registradas na folha de ponto. Para cada apontamento é gerado uma apropriação com o preço do insumo, obedecendo as regras de vigência e de preço ativo.

A funcionalidade está disponível em "Totvs Construção Obras e Projetos| Controle | Apropriações | Apropriações de Insumos / Serviços | Processos | Mobilidade | Gerar Apropriação de Mão de Obra".

Ao executar o processo o sistema solicita que seja informada uma data limite para apropriação e, de acordo com a data informada, são exibidas as tarefas que possuem apontamentos pendentes de apropriação.

Conforme detalhado no parâmetro Planilha para Apontamentos  [Mobilidade (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)

Quando o projeto estiver parametrizado para utilizar apontamentos na Planilha Executiva as informações exibidas na visão do porcesso de  Gerar Apropração de Mão de Obra  considerará os itens da Planilha Executiva.

Quando o projeto estiver parametrizado para utilizar apontamentos na Planilha de Atividades as informações exibidas na visão do pocesso Gerar Apropração de Mão de Obra considerará as tarefas na Planilha de Atividades.

 Caso não existam apontamentos validados, o sistema emitirá uma mensagem informando que não existem apontamentos validados até a data limite informada.

**Apropriação de Mão de Obra**

Os preços da apropriação de mão de obra podem variar entre o valor da mão de obra do funcionário e o valor do insumo no Totvs Obras e Projetos. A origem do preço pode ser definida nos parâmetros da apropriação que podem ser alterados em "Parâmetros do projeto (F6) | Apropriação | Apropriação de Serviços/Insumos".

* Caso a origem do preço seja definida para o insumo, o sistema verifica qual a lei social aplicada no grupo de custo do mesmo para realizar o cálculo do preço unitário da apropriação. O sistema realiza o cálculo com a seguinte fórmula: **PreçoInsumo x LeiSocial**.

* Caso a origem do preço seja definida para o valor de mão de obra do funcionário pelo módulo Folha de Pagamento, o usuário pode optar por aplicar ou não as leis sociais no valor da mão de obra utilizando o parâmetro de apropriação "Aplica leis sociais no preço do sistema de Folha de Pagamento". Caso o parâmetro de aplicação de lei estiver marcado, o cálculo do preço será semelhante ao cálculo do preço quando a origem é o insumo.

O sistema irá verificar qual a lei social aplicada no grupo de custo do insumo cujo funcionário está associado (funcionário é associado pela função do insumo) e realizará o seguinte cálculo para o preço da apropriação:

**ValorHoraFuncionario x LeiSocial**. Caso o parâmetro de utilização das leis esteja desmarcado o preço unitário da apropriação será o valor da hora do funcionário.

Será registrado na apropriação além das informações básicas, o funcionário/terceiro, a equipe, a origem e o motivo de improdutividade (somente apontamentos improdutivos).

**Observações:**

* Caso a moeda do projeto for diferente da moeda global, ao realizar a apropriação de mão de obra o sistema utilizará as fórmulas de cálculo para as origens definidas e também multiplicará pelo valor da cotação da moeda.
  + Origem valor insumo: **PreçoInsumo x LeiSocial x CotaçãoMoeda**
  + Origem valor funcionário: **ValorHoraFuncionario x LeiSocial x CotaçãoMoeda**
* Caso em Parâmetros do projeto (F6) | Mobilidade , o parâmetro "Confrontar Apontamento de Coletor X Ponto" esteja marcado, ao executar o processo, se o tempo do apontamento for maior que o número de horas registrado na folha de ponto, o apontamento será apropriado e na visão de apontamentos de mão de obra o status do mesmo será "Pendente de Ponto".
* Realiza a apropriação de mão de obra de apontamentos originados de coletor móvel do processo de mobilidade;
* Para cada apontamento é gerado uma apropriação com o valor do custo do funcionário ou terceiro originários da folha de pagamento, quando o parâmetro de projeto "Origem do Preço da Apropriação" estiver marcado como "Valor Mão de Obra do sistema de Folha de Pagamento" ou o preço do insumo, obedecendo a regra de vigência ou do preço ativo quando ocorrer a não identificação pela vigência;
* O usuário escolhe a(s) tarefa(s) e, somente após a escolha de pelos menos uma tarefa o sistema irá possibilitar avançar para execução;
* O sistema seleciona, para processamento, todos os apontamentos pendentes e pendentes de ponto até a data limite inclusive e, que sejam das tarefas escolhidas pelo usuário;
* Para a apropriação o sistema levará em consideração a regra de preço por vigência do insumo. Posteriores ajustes de preços não serão refletidos em apropriações efetivadas;
* Além das informações básicas para a apropriação, são gravadas no registro de apropriação a equipe, o membro, a origem e o motivo de improdutividade (quando apontamento improdutivo). O campo origem não ficará visível para o usuário, apenas armazenado na base de dados;
* O sistema grava no apontamento o identificador da apropriação e atualiza o status do apontamento para apropriação;
* Após a apropriação, o apontamento não estará mais pendente e não será considerado, caso seja executada novamente a rotina de apropriação, ou seja, um apontamento será apropriado uma única vez;
* No final do processo é exibida uma mensagem ao usuário informando o sucesso ou erro da execução do processo;
* À medida que for sendo executado o processo e as apropriações forem geradas, será possível acompanhar o custo da obra utilizando como base o preço do insumo. Somente após o processo de revaloração e rateio é que será possível verificar o custo real da obra.
* Outro ponto importante é que, ao utilizar a Planilha Executiva para apontamentos, caso uma apropriação seja excluída e existam outras apropriações de diferentes tarefas vinculadas ao mesmo item e no mesmo apontamento, todas essas apropriações também serão excluídas.

### **🔹 Importante**

Para que esse processo **considere funcionários/terceiros demitidos ou em férias**, é necessário que o usuário que irá executar o processo esteja com a permissão **“Considerar funcionários demitidos/férias na Apropriação de Mão de Obra”** liberada em seu perfil, conforme figura abaixo:

 

 Informações Complementares

---

[Apropriação de Mão de Obra](https://tdn.totvs.com/pages/viewpage.action?pageId=421385105)
