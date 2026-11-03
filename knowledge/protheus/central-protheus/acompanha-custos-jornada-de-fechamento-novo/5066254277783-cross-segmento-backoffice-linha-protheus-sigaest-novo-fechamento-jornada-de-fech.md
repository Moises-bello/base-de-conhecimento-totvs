---
article_id: 5066254277783
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: eb5b8808243f40fd46cfa90d014f98799d951f2818df637b9f1060ea09bd799f
fetched_at: '2026-06-28T22:38:48.260434+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Novo Fechamento (Jornada
  de Fechamento)
type: support-article
updated_at: '2025-05-26T18:00:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5066254277783-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Novo-Fechamento-Jornada-de-Fechamento
---

**Dúvida**Qual procedimento para Jornada de Fechamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.

**Introdução**

Novo Fechamento, recurso que permite iniciar a jornada de fechamento basta definir a forma de contabilização e clicar em Novo Fechamento.

**Aviso.**

* Devido a necessidade da jornada de fechamento não poder utilizar a execução exclusiva através do parâmetro **MV\_CUSTEXC**, foi implementado o recurso de [Controle automático de bloqueio de movimentação - **MV\_CMDBLQV**](https://tdn.totvs.com/x/4zrjIg)para impedir movimentações no sistema que interfiram no cálculo do fechamento.
* Se o [Controle automático de bloqueio de movimentação - **MV\_CMDBLQV**](https://tdn.totvs.com/x/4zrjIg) for configurado como compartilhado, as alterações feitas no parâmetro serão refletidas em todas as filiais. Caso esse não seja o comportamento esperado, será preciso criar o parâmetro para cada filial de forma exclusiva.

|  |
| --- |
| **IMPORTANTE:**  O uso do parâmetro **MV\_CMDBLQV** é **opcional**. Sua finalidade é restringir movimentações no sistema após a última data de processamento do custo médio, conforme data definida automaticamente.  Ao habilitar esse parâmetro, quaisquer movimentações com data anterior à informada no processamento do custo serão bloqueadas, como forma de garantir a integridade dos dados já consolidados e calculados no periodo.  Caso não deseje aplicar esse bloqueio e permitir movimentações retroativas, recomenda-se manter o parâmetro desativado. |

**Demonstração**

**![](https://tdn.totvs.com/download/attachments/572501579/novo_fechamento.gif?version=1&modificationDate=1643217063200&api=v2)**

**Fluxo do Processo**

A- Utilizando configuração de custo off-line **(****MV\_CUSMED = 'M')**

**![](https://tdn.totvs.com/download/attachments/572501579/image2021-5-4_16-32-38.png?version=1&modificationDate=1620156758270&api=v2)**

B- Utilizando configuração de custo online **(MV\_CUSMED = 'O')**

**![](https://tdn.totvs.com/download/attachments/572501579/image2021-5-4_16-34-19.png?version=1&modificationDate=1620156859507&api=v2)**

**Etapas Jornada de Fechamento**

**1 - Predefinição de cálculo**

Ao iniciar o processo de Fechamento de Estoque, o sistema automaticamente verifica qual configuração de custo está sendo utilizada: se custo online (O) ou custo off-line (M) através do parâmetro MV\_CUSMED.  

Na etapa de predefinição de cálculo, será apresentada a configuração para ser realizada para a jornada de fechamento do período, que deve ser preenchida seguindo as especificações na seção de Informações Adicionais >> Parâmetros do Configurador, abaixo.

Após a definição, o processamento já pode ser iniciado através do botão "Próximo passo", que passará para a próxima etapa e será iniciado o Cálculo de custo/Virada de saldo e os passos do processamento serão atualizados em tempo real que ocorre no sistema.

Será possível realizar o cancelamento da jornada em andamento ou refazer o Cálculo de custo após a finalização do processamento.

![](https://tdn.totvs.com/download/attachments/572501579/calculo_custo.gif?version=1&modificationDate=1643219408713&api=v2)

**2 - Análise e Revisão**

Na etapa de Análise e Revisão é possível verificar se os custos calculados para o período selecionado estão corretos, caso seja identificado algum erro nas movimentações dos produtos é possível realizar um novo Cálculo de custo/Virada de saldo no fluxo de fechamento de estoque que está sendo realizado, através do botão de "Refazer cálculo".

É necessário escolher se o novo cálculo será feito com uma nova predefinição ou se será utilizada a predefinição já preenchida anteriormente, após confirmar o refazer cálculo, será direcionado novamente para o passo 1 para confirmar ou alterar as informações e seguir com fechamento.

![](https://tdn.totvs.com/download/attachments/572501579/analise_revis%C3%A3o.gif?version=1&modificationDate=1643219992083&api=v2)

### **Filtro de análise e resultados**

* **Campos:**Todos os campos relacionados o analise de resultados.
* **Operador:**Opções para realizar as condições do filtro, com as opções de "Igual a,  Diferente de, Menor ou igual a, Menor que, Maior que ou igual a, Maior que e Contém.
* **Expressão:**Deve ser informado a expressão (texto ou numero)
* **Filtros:** Após colocar a expressão pressione ENTER ou TAB  incluir o filtro que será apresenta de forma previa em um pequena caixa abaixo dos campos.
* **Botão** **Aplicar Filtros:**Ao clicar no botão aplicar filtro automaticamente ele fecha e volta para tela de analise de resultados aonde o sistema vai processar os resultados e gerar em tela.
* **Múltiplos filtros**: Após adicionar um filtro pressionando ENTER ou TAB é possível adicionar uma nova expressão para consulta, a mesma será intercalada com a condição de OR(OU) para campos e iguais, exemplo:  "filial igual a D MG 01" colocar novamente "filial igual a D MG 02" a query será montado com filial igual a D MG 01  OR (OU) filial igual a D MG 02.       caso insira condições diferente serão tratadas como AND(E) entre parênteses exemplo:  "filial igual a D MG 01" AND  " Tipo igual  a PA", lembrando que esse comportamento é realiza de forma automática pelo componente de filtro.
* ##

**3 - Contabilização**

**Pré-Condição**

Para que a jornada de fechamento possua a etapa de contabilização, é necessário que o parâmetro de Gerar Lançamento Contábil esteja configurado como "Sim", e o ambiente precisa estar configurado como custo off-line (M) através do parâmetro MV\_CUSMED.

![](https://tdn.totvs.com/download/attachments/572501579/image2021-1-19_9-27-33.png?version=1&modificationDate=1611059253317&api=v2)

Após a configuração do parâmetro, a rotina de contabilização (MATA331) será incluída na jornada de fechamento.

Após a etapa de Análise e Revisão referente o recálculo das movimentações do período, ao clicar para a próxima etapa, será iniciado a Contabilização através da rotina de**Contabilização do Custo Médio - MATA331**, sendo atualizado em tempo real a situação da rotina que ocorre no sistema. Após a execução da Contabilização, caso haja necessidade, é possível refazer o processamento da rotina, através do botão "Refazer contabilização".

![](https://tdn.totvs.com/download/attachments/572501579/contabilizao.gif?version=1&modificationDate=1643224652067&api=v2)

**Contabilização por consumo e produção**

**Pré-Condição**

Para que a jornada de fechamento possua a etapa de contabilização por consumo e produção , é necessário que o parâmetro de Gerar Lançamento Contábil esteja configurado como "Sim" e que o parâmetro de Forma de Contabilização esteja configurado como "Contabilização por consumo e produção" , e o ambiente precisa estar configurado como custo off-line (M) através do parâmetro MV\_CUSMED.

![](https://tdn.totvs.com/download/attachments/572501579/image2021-1-19_9-27-33.png?version=1&modificationDate=1611059253317&api=v2)

![](https://tdn.totvs.com/download/attachments/572501579/image2021-5-13_13-58-7.png?version=1&modificationDate=1620925087920&api=v2)

Após a configuração dos parâmetros, a rotina de contabilização (MATA331) será incluída na jornada de fechamento e após a finalização do cálculo do custo e contabilização por consumo, será executado o fluxo de cálculo e contabilização por produção.

![](https://tdn.totvs.com/download/attachments/572501579/consumo_e_producao.gif?version=1&modificationDate=1643225910543&api=v2)

Após a etapa de Análise e Revisão referente o recálculo das movimentações do período, ao clicar para a próxima etapa, será iniciado a Contabilização através da rotina de**Contabilização do Custo Médio - MATA331**, sendo atualizado em tempo real a situação da rotina que ocorre no sistema. Após a execução da Contabilização, caso haja necessidade, é possível refazer o processamento da rotina, através do botão "Refazer contabilização".

![](https://tdn.totvs.com/download/attachments/572501579/refazer_contabilizacao.gif?version=1&modificationDate=1643226342137&api=v2)

**4 - Fechamento**

Após a contabilização do estoque, é possível realizar o fechamento do mesmo, bloqueando assim qualquer movimentação de estoque com data inferior a data deste último fechamento realizado. Essa ação, até o momento, é uma ação irreversível,  assim o usuário é alertado desse fato, apresentando a ele um modal de confirmação antes da realização dessa etapa.

A data utilizada no processo de fechamento é a data selecionada no campo Data Fechamento de Custo da etapa de Predefinição de cálculo.

![](https://tdn.totvs.com/download/attachments/572501579/fechamento.gif?version=4&modificationDate=1643227076567&api=v2)

**Saldos à Distribuir**

Caso exista algum item pendente de endereçamento que possa comprometer o fechamento o sistema apresentará no fechamento uma tela de Saldos à Distribuir, onde serão listados todos os itens com pendencias para que seja possível finaliza-las e realizar o fechamento. Caso necessário, também é possível cancelar o fechamento nessa etapa.

**Aviso**

Atenção, essa etapa será apresentada durante a jornada de fechamento, apenas se o ambiente estiver com a configuração de exibir relatório de Saldo a Distribuir (MV\_A280SDA) habilitada.

![](https://tdn.totvs.com/download/attachments/572501579/sados_distribuir.gif?version=1&modificationDate=1645017724637&api=v2)

**Fechamento**

Caso o fechamento não tenha saldos à distribuir, o sistema irá para a última etapa do fechamento.

Nesta etapa ocorre a preparação de ambiente, onde é verificada se todas as filiais selecionadas podem ser processadas. Se alguma filial tiver inconsistência, a virada de saldo não é iniciada e é exibida uma janela com as filiais inconsistentes e as informações necessárias, assim é possível analisar as inconsistências para depois prosseguir com a virada de saldo; e caso esteja tudo certo é feita a virada de saldo para todas as filiais em processamento.

![](https://tdn.totvs.com/download/attachments/572501579/fechamento.gif?version=4&modificationDate=1643227076567&api=v2)

**Itens com inconsistência**

Após finalizar o processo da virada de saldo, caso seja encontrada alguma inconsistências entre os itens, com relação ao saldo físico e financeiro com o saldo da movimentação por lote ou de endereço, será apresentado uma opção na etapa do fechamento para visualizar essas informações, podendo também ser exportado para planilha.

![](https://tdn.totvs.com/download/attachments/572501579/saldos_distribuir.gif?version=2&modificationDate=1643287218997&api=v2)

**Informações Técnicas**

Foi desenvolvido uma classe REST de controle para entrada e saída de dados através da linguagem TLPP, sendo responsável por gerações e gravações de registros nas tabelas de perfil de usuário do Framework

Especificações de Serviços, [Clique Aqui](https://tdn.totvs.com/display/PROT/Novo+Fechamento+-+Jornada+de+Fechamento#:~:text=Informa%C3%A7%C3%B5es%20T%C3%A9cnicas)

**Saiba mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de parâmetros Acompanha Custos - Jornada de Fechamento*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065941471767)
