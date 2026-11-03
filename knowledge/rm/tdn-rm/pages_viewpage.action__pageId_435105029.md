---
content_hash: 1600c8848cff848d291b870eaa4487d04b21b1a85b5da717ab5575021a20007c
fetched_at: '2026-06-29T00:09:47.617838+00:00'
page_id: '435105029'
product: rm
source: tdn-rm
title: Condomínio - Básicos - Item de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105029
version: 12
---

Este cadastro será utilizado para discriminar quais são os itens que irão compor uma Cobrança do Condomínio. Assim ao se realizar a cobrança discriminada de "Taxa de Administração" ou "Fundo de Reserva", por exemplo, cada um deve ser um Item de Cobrança.   
Um Item de Cobrança pode receber a referência de várias Naturezas Financeiras Orçamentárias, dessa forma fará  o agrupamento dos valores atribuídos a cada uma das Naturezas. A associação das naturezas será realizado pelo anexo Natureza Orçamentária/Financeira do Item de Cobrança, para maiores informações   
A tela de cadastro do Item de Cobrança, possui os seguintes campos:

* **Código**: Campo de controle que é gerado ao salvar o Item de Cobrança.
* **Descrição**: Campo no qual se pode descrever o Item de Cobrança.
* **Data Inicial**: data em que o Item de Cobrança poderá começar a ser faturado.
* **Data Final**: data a ser preenchida quando o Item de Cobrança não puder ser mais ser utilizado.
* **Compõe Valor Original:** Ao marcar essa opção, o Item de Cobrança irá compor o Valor Original de Lançamentos gerados pelo Fechamento do Condomínio, no qual o mesmo esteja associado.
* **Utiliza pró-rata:** Define se, para este item de cobrança os cálculos deverão considerar os parâmetros de pró-rata do sistema.
* **Utiliza subsídio:** Define se, para este item de cobrança os cálculos de fechamento deverão considerar a regra de subsídio.
  + O campo **prioridade no subsídio** define a ordem em que os itens de cobrança terão os valores subsidiados durante o cálculo. Quando houver múltiplos itens elegíveis para subsídio em uma mesma cobrança, o sistema seguirá os seguintes critérios para aplicar os descontos:

    1. **Ordem de prioridade numérica**: o sistema considerará primeiro os itens com o menor número de prioridade definido.
    2. **Empate na prioridade**: caso dois ou mais itens tenham a mesma prioridade, o sistema aplicará o subsídio primeiro ao item de **maior valor**.
    3. **Itens sem prioridade definida**: itens que não possuírem prioridade configurada serão considerados **por último** na aplicação dos descontos.
* **Ignorar vacância:** Define se este item de cobrança deve ter seus cálculos de vacância desconsiderados no fechamento de condomínio.
  + É importante frisar que, caso esta opção esteja habilitada, nenhum lançamento ou calculo será gerado no fechamento do condomínio. Este item ignorado pode ser observado na memória de cálculo da apuração do condomínio. Nos casos de pro-rata, onde parte do valor é direcionado ao sócio em períodos de carência ou vacância, somente o cálculo referente ao período ocupado será exibido na apuração.

Para que seja gerado os Lançamentos Financeiros do Item de Cobrança, é necessário que seja associado o Valor de Integração. Na tela de cadastro do Item de Cobrança temos a possibilidade de cadastrar o Valor de Integração para cada coligada.   
Ao associar um Valor de Integração é exibido os seguintes campos:

* **Coligada:** Define qual a coligada do Valor de Integração a ser associado.
* **Valor de Integração:** Define qual o Valor de Integração a ser utilizado pelo Item de Cobrança. Lembrando que os registros de Valores de Integração tem origem no **TOTVS Gestão Financeira** para obter mais informações sobre esse cadastro .

**Observações:**

* O sistema permite somente um Valor de Integração por Coligada.
* Quando o campo "Compõe Valor Original" for selecionado, então apenas os valores de integração com ação igual a nada serão permitidos.
* Quando o item de cobrança estiver vinculado a uma cobrança direta dentro de um fechamento de condomínio, ele ficará indisponível para edição. Qualquer alteração só poderá ser feita após desvinculá-lo do fechamento.

Informações Complementares

---
