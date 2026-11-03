---
content_hash: 151e6cba59e971f876023acf2d9241190e50927d71bc6bc5fbdd8f80a0a8711a
fetched_at: '2026-06-29T00:10:42.878151+00:00'
page_id: '547865478'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Renegociação de Dívidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547865478
version: 25
---

# **1) Introdução**

---

Visando simplificar o processo de renegociação de parcelas em atraso, foi criada a funcionalidade de aditivo de Renegociador de dívidas do Aluguel.

Com este aditivo é possível renegociar várias parcelas de um contrato de aluguel e redistribuí-las em uma ou mais parcelas futuras. Ao selecionar este tipo de Aditivo, será apresentado todas as parcelas em aberto do contrato de aluguel na visão e o sistema permitirá que os valores destas parcelas sejam editados. Ao efetivar o aditivo, o sistema irá cancelar as parcelas antigas e refazer novas parcelas, com os valores definidos no aditivo.

# **2) Procedimentos para utilização**

---

Para a correta utilização do aditivo de renegociação de parcelas do aluguel, devemos primeiramente habilitar a permissão **[02.03.01.19]** do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis:* 

Habilitando a permissão do aditivo de renegociação de dívidas

Após a permissão concedida, poderemos acessar o aditivo na lista de aditivos de contratos de aluguel.

**3) Utilizando o processo**

---

Atenção: O sistema sempre irá se basear no retrato dos valores líquidos na data do sistema, independente da data do aditivo. Dessa forma, recomendamos uma revisão dos valores de multa e juros dos lançamentos financeiros vencidos, caso o aditivo seja realizado com uma data de aditivo retroativa a data do sistema.

**Pré-condições**

* Ter efetivado o Contrato de Locação
* Ter incluído um Locatário
* Ter incluído um Motivo do Aditivo

**Incluindo um Aditivo de Renegociação de Parcelas**

* O cadastro do aditivo pode ser feito em ***Contratos de locação / Anexos / Aditivos / Renegociação de dívidas,*** bastando clicar em Incluir.

Tela do aditivo de renegociação de dívidas

* Como visto acima, a tela do aditivo de renegociação de dívidas possui os seguintes campos:  
  + Código do Aditivo: Campo de preenchimento automático
  + Data do Aditivo: Data do cadastro do aditivo.
  + Tipo do Aditivo: Preenchido automaticamente
  + Situação do Aditivo: Preparação
  + Motivo do Aditivo: Informar um Motivo do Aditivo
  + Número do Aditivo no Cliente: Campo onde o cliente informar o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.
  + Nesta mesma tela no box de renegociação, poderemos então selecionar as parcelas que estão em débito e que deverão ser renegociadas.

* **Parâmetros**
  + Pode ser definido que na negociação não serão considerados Multa e Juros, bastando desmarcar a caixa de seleção **Negociar sem Multa e Juros**
  + Uma vez que se define que não serão utilizados juros e multa na negociação, é possível informar percentuais ou valores a acrescentar ou descontar por meio dos campos **Taxa** e **Valor** dentro dos grupos **Acrescentar** ou **Descontar**. Apenas um dos campos poderá ser informado.
  + É possível definir também a data de primeiro vencimento indicando se será usado o **dia** da regra de vencimento do contrato por meio da caixa de seleção **Usar dia da regra de vencimento do contrato**. Se desmarcar este campo, será possível informar um dia para o vencimento por meio do campo **Dia.** Para complementar é necessário escolher a **Competência inicial**, que irá definir o mês do **1° Vencimento.**
  + Por fim, selecionar a quantidade de parcelas a serem geradas na negociação através do campo **Quantidade de Parcelas**.

* **Resumo da Renegociação**
  + **Total das Parcelas**: Soma do valor de todas as parcelas abertas em atraso exibidas para o contrato
  + **Total Selecionado**: Soma das parcelas selecionadas
  + **Saldo Devedor**: Diferença entre o **Total das Parcelas** e **Total Selecionado**
  + **Total Juros de Mora**: Soma do total de Juros das parcelas selecionadas
  + **Total Multa Atraso**: Soma do total de Multa das parcelas selecionadas
  + **Valor da Parcela**: Valor da parcela, considerando as parcelas selecionadas, juros e multa levando em conta a opção de negociar sem multa e juros, taxa e/ou valor acrescentar/descontar e por fim o número de parcelas que serão geradas pelo aditivo
  + **Valor da Renegociação**: Valor total da renegociação, considerando as parcelas selecionadas, juros e multa levando em conta a opção de negociar sem multa e juros, taxa e/ou valor acrescentar/descontar

Após salvar o aditivo, ele será colocado **Em Preparação,** ficando disponível para **Efetivação.**

Atenção

Após salvar o aditivo, os lançamentos financeiros selecionados pelo usuário para o cancelamento serão bloqueados. Isto é realizado para evitar que operações financeiras como a baixa sejam feitas no lançamento e que podem impactar no aditivo. Para desbloquear esses lançamentos, o usuário terá que excluir o aditivo em preparação ou efetivá-lo.

**Efetivando o aditivo**

Estando o aditivo cadastrado e no status "Em Preparação" poderemos ir em ***Processos / Efetivar Aditivo***, para que o mesmo seja efetivado.

* Ao efetivar o aditivo o sistema irá cancelar os lançamentos que foram selecionados e se encontram na lista de lançamentos do aditivo com status de "Cancelado";
* Novos lançamentos serão incluídos, de acordo com o número de parcelas selecionadas e a data do primeiro vencimento.
* Estes lançamentos passarão a incorporar a visão de parcelas do aluguel, bem como passarão a estar integrados no evento financeiro gerado pelo aluguel.
* Para contratos de aluguel com imóveis de terceiros atrelados à contratos de administração, as seguintes regras para os lançamentos de repasse serão observadas:
  + **Repasse garantido**: Ao efetivar o aditivo de renegociação o sistema não irá gerar novas parcelas de repasse, independente das parcelas selecionadas para o aditivo.
  + **Repasse condicional**: Ao efetivar o aditivo de renegociação o sistema irá gerar novas parcelas de repasse, de acordo com o parcelamento do aditivo, respeitando a competência selecionada no cadastro do mesmo.

# **4) Informações adicionais**

---

Importante!

Podem ser usados no aditivo de renegociação:

* Lançamentos vencidos;
* Lançamentos em aberto;
* Somente a receber;
* Parcelas do evento financeiro integrado ou parcialmente integrado;
* Parcelas do evento financeiro do mesmo tipo de evento financeiro configurado no contrato de locação.

Não podem ser usados no aditivo de renegociação:

* **Eventos Avulsos:** Lançamentos de eventos financeiros avulsos (que não sejam o evento principal de locação) **não podem** ser incluídos ou selecionados no Aditivo de Renegociação.

  + **Importante:** Para renegociar eventos avulsos ou outras cobranças não relacionadas ao aluguel, utilize a funcionalidade de .

Ao gerar novos lançamento dos contratos ou criar novas despesa ou eventos financeiros, os processos ou cadastros feitos não afetarão os lançamentos de renegociação. Neste sentido valerão as seguintes regras para os lançamentos criados no processo:

* Não poderá ser agregado nenhum valor de despesa ou evento financeiro nas parcelas de renegociação;
* Caso seja cadastrado uma Despesa ou Evento financeiro  e a mesma se iniciar no período da renegociação, deverá acumular os valores para a próxima parcela aberta do contrato, que não faça parte da renegociação;
* Não exclui ou atualiza as parcelas canceladas da renegociação;
* Não considera escalonamento nas parcelas de renegociação.
* Não será possível, na renegociação, selecionar parcelas para locatários diferentes.
* Não será possível gerar negociação para contratos com dois vencimentos na mesma competência.
* O sistema irá sempre respeitar o locatário responsável pela parcela de origem (selecionada no aditivo) mesmo que, na data do aditivo este locatário não seja mais o locatário principal do contrato.

---
