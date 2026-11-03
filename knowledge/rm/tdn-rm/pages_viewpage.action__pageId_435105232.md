---
content_hash: be1c680b2c0e9d244a2523108e66f74ab9a3b35ba921a9220def1511f6325a99
fetched_at: '2026-06-29T00:09:49.097600+00:00'
page_id: '435105232'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Integral - Processo - Gerar Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105232
version: 21
---

# **Introdução**

---

Esse processo permite a geração de Lançamentos Financeiros para os Cálculos realizados em um Fechamento do Condomínio.    
Ao  Gerar Lançamento, a situação das despesas relacionadas com o mesmo, serão atualizadas de "Calculada" para "Integrado". Além disso, o Fechamento também terá seu "Status" atualizado para "Integrado".  
Nesse processo é possível selecionar 1 ou mais Fechamentos para a geração de lançamentos.

# **Pré-Condições**

---

* Empreendimento com Parâmetros de Integração Financeira associado;
  + Para essa associação é necessário entrar no seguinte caminho: TOTVS Incorporação >> Condomínio >> Empreendimento >> Fechamento >> Parâmetros de Integração Financeira, selecione um parâmetro desejado.
* Fechamento com "Status" igual à "Em cálculo";
  + Para que o Fechamento possua o "Status" referido, é necessário que seja executado pelo menos um dos Cálculos.
* As despesas calculadas precisam ter associado Item de Cobrança ativos e com valores de integração para a Coligada do Empreendimento;

# **Como utilizar**

---

1. Selecione um fechamento desejado;
2. Em processos selecione "Gerar Lançamentos Financeiro";
3. Será exibida uma tela com o campo "Data de Vencimento", onde é possível determinar a Data de Vencimento de todos os lançamentos que serão gerados pelo processo;
4. Informe a data desejada de Vencimento e avance o processo;
5. O processo irá gerar os lançamentos conforme o resultado dos Cálculos de Fechamento;
6. O Fechamento terá seu "Status" igual à "Integrado", indicando que já foi gerado os Lançamentos Financeiros;
7. As despesas relacionadas associadas a Geração de Lançamentos, terão seu "Status" atualizado para "Integrado";

# **Observações**

---

* Só pode ser gerado mais de um Fechamento em uma mesma Geração de Lançamentos, caso os Fechamentos possuam a mesma competência;
* Quando uma subunidade estiver integrada a um imóvel no módulo de aluguel, a cobrança será feita para o locador ou para o locatário, de acordo com os parâmetros definidos em TOTVS Incorporação>> Ambiente >> Parâmetros Totvs Incorporação >> Gestão de Condomínio >> Financeiro >> Prioridade de cobrança do condomínio, quando integrado à locação. O fechamento busca o responsável financeiro de acordo com o primeiro parâmetro marcado, caso ele não esteja vigente na competência em questão, a cobrança será feita de acordo com o segundo parâmetro marcado. Se houver somente um parâmetro marcado e este responsável não for encontrado (para o caso de fechamentos em competências em que o contrato de locação ou administração não estejam vigentes), não será gerada cobrança e uma mensagem de aviso será exibida. Se o contrato de administração ou o de locação estiverem vigentes na competência do fechamento e nenhum parâmetro estiver marcado, também não será gerada cobrança e o fechamento exibirá uma mensagem de erro. É possível alterar a prioridade da cobrança utilizando as setas à direita para trocar a ordem dos parâmetros.
* Os lançamentos gerados para as apurações de subunidades integradas ao imóvel, serão exibidos no anexo Lançamento Financeiro de Condomínio na visão do contrato de locação no módulo de Gestão de Aluguel.
* Caso não seja encontrado Responsável Financeiro para as despesas calculadas, não será possível gerar os Lançamentos Financeiros;
* Não é possível gerar Lançamentos Financeiros para Fechamentos que não estejam com o "Status" igual à "Em cálculo";
* Para que possa ser realizado a Geração de Lançamentos, é necessário que o Item de Cobrança das Despesas relacionadas esteja ativo e com Valores de Integração associado ao mesmo;
* Caso alguma Despesa (Reserva ou Medição) esteja com "Status" igual à "Em Preparação" tendo a mesma competência de um Fechamento, não poderá ser executado o processo. Para que possa ser feita a execução do processo, é necessário fazer o recálculo do Fechamento;
* Caso hajam duas subunidades no mesmo condomínio, associadas ao mesmo cliente, serão gerados dois lançamentos, um para cada subunidade. Entretanto, no processo de geração de lançamentos, há um parâmetro que, quando marcado, irá agrupar, gerando apenas um lançamento para a cobrança das duas subunidades.
* Caso o imóvel possua áreas fracionadas, o sistema irá utilizar os centros de custo cadastrados na área do imóvel para realizar os rateios dos lançamentos de reembolso.
* Caso o imóvel possua áreas fracionadas mas sem a informação de centro de custo, o sistema continuará buscando o centro de custo cadastrado no imóvel ou nos parâmetros de integração financeira do empreendimento para compor os devidos rateios.
* Não será possível integrar os lançamentos quando o centro de custo definido no imóvel não for encontrado na coligada do empreendimento (onde os lançamentos são gerados). Nestes casos, será preciso criar o centro de custo na coligada do empreendimento com o mesmo código do centro de custo cadastrado no imóvel.
* Quando os valores originais e de integrações forem iguais a zero, nenhum lançamento será gerado.
* É possível utilizar variáveis para incluir informações no histórico de lançamentos financeiros gerados. Quando o agrupamento é aplicado, o lançamento registrará no histórico os dados dos registros agrupados. Por exemplo, ao agrupar itens de cobranças diferentes e códigos de contratos de locação, o histórico do lançamento financeiro exibirá: Medição, Cobrança direta - 90 - 91. Neste exemplo, utilizamos as variáveis [COBR] (Item de Cobrança) e [CALG] (Contrato de Locação).
* Não há agrupamento quando o lançamento é gerado para sócios (vacância). Nesse caso, o histórico do lançamento financeiro apresentará apenas os dados referentes àquele imóvel.
* A partir da versão 12.1.2502 ao gerar os lançamentos financeiros de um fechamento, o sistema irá sempre preencher o campo *Mês/Ano da Competência*, com a data da competência do fechamento integrado. Este campo pode ser encontrado no próprio lançamento financeiro na aba *"Dados Adicionais".*
* É importante ressaltar que, quando os itens de cobrança possuem valores de integração com ação (acrescenta ou desconta) e a opção "Compõe Valor Original" desmarcada, o sistema irá gerar lançamentos financeiros com valores originais zerados, visto que todo o cálculo acontece nos valores de integração. Nesse cenário não é possível realizar rateios por centro de custo / natureza orçamentária financeira, visto que não há valores nos lançamentos para o correto rateio. Caso precise utilizar valores de integração nesse formato é necessário desmarcar a obrigatoriedade de rateio de centro de custo / natureza orçamentária financeira nos parâmetros globais do TOTVS Gestão Financeira.

# **Hierarquia de Centros de Custo**

---

A hierarquia dos centros de custo para geração dos devidos rateios dos lançamentos é a presente abaixo:

1. Centro de custo do rateio do contrato;
2. Centro de custo do imóvel. Observação: Caso existam áreas fracionadas o sistema irá buscar o centro de custo das áreas para compor o rateio.
3. [Centro de custo do item de cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=969141178)\*
4. Centro de custo dos parâmetros financeiros do empreendimento.

\*Importante: Para a utilização do rateio de centro de custo do item de cobrança será necessário gerar os lançamentos de condomínio selecionando o agrupamento por item de cobrança nas opções de agrupamento do processo. São elas:

* Cliente/Fornecedor e Item de Cobrança;
* Cliente/Fornecedor, Subunidade e Item de Cobrança;
* Cliente/Fornecedor, Subunidade, Cálculo e Item de Cobrança.

# **Geração de lançamentos quando existe adiantamento de cobrança direta**

---

* Quando existir um [adiantamento de cobrança direta](https://tdn.totvs.com/pages/viewpage.action?pageId=435104836) associado à um fechamento, e este adiantamento ainda não estiver integrado, não será possível gerar lançamentos até que o adiantamento de cobrança direta seja integrado e seu respectivo lançamento gerado.
* Quando existir um [adiantamento de cobrança direta](https://tdn.totvs.com/pages/viewpage.action?pageId=435104836) associado à um fechamento, com status integrado, isto é, já com seus respectivos lançamentos gerados, a tela de geração de lançamentos irá sofrer uma pequena modificação e obrigará o usuário a selecionar um valor de integração com ação "Nada", para que os respectivos valores já integrados através do adiantamento sejam abatidos nestes lançamentos.

Tela da geração de lançamentos quando existe adiantamento com status "Integrado".

**Veja Também**

---
