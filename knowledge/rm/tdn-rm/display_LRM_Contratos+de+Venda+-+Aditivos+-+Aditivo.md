---
content_hash: 850215b35486385f736c26411acebaff402466e57f3d333ee6834d34278140e2
fetched_at: '2026-06-29T00:09:48.475856+00:00'
page_id: '435105164'
product: rm
source: tdn-rm
title: Contratos de Venda - Aditivos - Aditivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Aditivos+-+Aditivo
version: 14
---

Atenção

Atenção, todos os aditivos serão reajustados independente se usa ou não o reajuste on-line, isso evitará que as parcelas sejam aditivadas com valores indevidos  na data base do aditivo. Caso precise que os valores sejam congelados em uma data, acesse venda=> lançamentos financeiros, processos => congelar reajuste ou descongelar caso precise voltar com o reajuste novamente

Aditivo é uma opção do sistema para correção e alteração de contratos já efetivados devido a modificações solicitadas pelo cliente ou pela empresa.

Este processo deverá ser acessado através do Anexo do menu Vendas / Alugueis. Vale lembrar que só podemos criar Aditivos para vendas efetivadas. Para maiores informações sobre como Cadastrar um Aditivo, .

Após a efetivação de qualquer Aditivo, além de atualizar os Lançamentos Financeiros no TOTVS Gestão Financeira, o usuário poderá visualizar um histórico onde trará todas as alterações efetuadas. Este histórico está disponível como uma aba na edição do Aditivo.  
O Aditivo terá etapas para a sua conclusão. Poderemos criar um Aditivo e o mesmo ficar em Preparação até que seja aprovado por um fluxo de aprovação e posteriormente ser concluído. O Aditivo será um anexo da Venda/Aluguel. O Fluxo de Aprovação é um recurso do produto RM e é opcional a sua utilização.

As etapas do Aditivo são:

* **Em Preparação**: Ao criar o Aditivo, o mesmo ficará com o status "Em Preparação", onde iremos cadastrar as Informações básicas como data do Aditivo, Descrição e selecionar o Tipo de Aditivo a ser executado. Poderemos selecionar mais de um tipo de Aditivo para ser executado simultaneamente e iremos cadastrar as informações de cada tipo de Aditivo.
* **Efetivado**: Ao efetivar o Aditivo o sistema verifica se algum lançamento do contrato de venda foi securitizado, encontrando não será possível concluir a efetivação do aditivo. A efetivação do Aditivo consiste em realizar as alterações contratuais de cada tipo de Aditivo selecionado, efetuar a contabilização e incluir o histórico do Aditivo. Caso o Aditivo seja efetivado, não será possível desfazê-lo ou cancelá-lo.
* **Desfazer Aditivo** - As Parcelas que foram baixadas , devem ser feito os cancelamentos das baixas e desfeitas as contabilizações antes de se efetuar o processo de Desfazer e este processo de se Desfazer Aditivo não foi implementado para **2 Aditivos** ( *Troca de Comprador e Troca de Lote* )  
  **Processo não liberado para Integração com Protheus**  
  O aditivo deve estar na versão 4 e efetivado para que possa se realizar o processo. O processo deve ser desfeito em ordem **decrescente** do número do Aditivo.
* **Cancelado**: Caso o Aditivo esteja Efetivado, basta desfazer Aditivo primeiramente e ai sim, depois processar o cancelamento.

Ao criar um novo Aditivo, será aberta a janela de Aditivos onde o usuário informa a Data do Aditivo, descrição e terá a sua disposição todos os tipos de aditivos, para que possam ser usados no processo.   
Poderemos selecionar mais de um Tipo de Aditivo para execução. Logo abaixo, segue uma descrição de cada tipo.

Caso o parâmetro "Plano de financiamento reajustado em memória na exibição de aditivos" , que se encontra no seguinte caminho: Ambiente|Parâmetros|TOTVS Incorporação|Contrato|Aditivo Parâm do Aditivo por coligada,  esteja marcado. Os Aditivos que tenham alterações de parcelas, sofrerão Reajuste do Plano de Financiamento em Memória até a data informada no Aditivo. Também será calculado os Juros de Mora e Multa de Atraso sobre este valor atualizado das Parcelas.Contabilização

Não é mais necessário abrir o TOTVS Gestão Contábil para visualizar a contabilização dos Aditivos.

Basta selecionar o Aditivo e ao editar , Anexo | Consultar Operação Contábil

Em seguida é aberto a tela de Contabilização do Aditivo.

Importante!

Não cancele o Processo ***Sincronizar parcelas do aditivo com a venda***, pois o mesmo é essencial para a correta parametrização do Aditivo.

Caso esta ação seja executada, o sistema retornará à tela inicial do Aditivo e será necessário refazer toda a parametrização, até que o processo acima seja executado em sua completude.

Processos:



A seguir estão listados os tipos de Aditivos do TOTVS Incorporação:

false

Como Fazer

---

* [Desfazer Aditivo](https://tdn.totvs.com/display/LRM/Desfazer+Aditivo)



false

Veja Também

---
