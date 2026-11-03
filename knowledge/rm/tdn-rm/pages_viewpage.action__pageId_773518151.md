---
content_hash: 42298412e263913cb1620401981baea4f909b10ff0eea8d62ce8bf5db39ba2ef
fetched_at: '2026-06-29T00:11:36.812409+00:00'
page_id: '773518151'
product: rm
source: tdn-rm
title: TCGI - Comissão - Visão de Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518151
version: 5
---

Parâmetro Editar Comissão na Mesa

### Parâmetro: Permitir Edição de Comissão após Venda Efetivada

Este parâmetro permite que o valor da comissão seja editado diretamente na Mesa de Vendas mesmo após a venda estar **efetivada** (ou seja, após a geração do plano de financiamento).

> ⚠️ **Atenção:** A utilização deste recurso pode ocasionar **inconsistências nos valores da venda**, uma vez que a comissão ajustada **não será automaticamente recalculada ou descontada** do valor total da negociação.

Se for necessário alterar o valor da comissão **após o pagamento ter sido realizado**, recomenda-se **refazer a venda**, garantindo que os valores estejam corretos e não ultrapassem o montante originalmente calculado na efetivação.

> ❗ **Importante:** O uso deste parâmetro é de inteira responsabilidade do cliente. A TOTVS **não se responsabiliza** por divergências nos valores resultantes de alterações manuais.

Após realizar os ajustes necessários, é fundamental **desmarcar o parâmetro** para evitar novos ajustes indevidos e garantir a integridade das informações no processo de comissão.

### Cadastro da Comissão

O cadastro de comissão tem a finalidade de realizar os cálculos dos valores da comissão de um contrato de Venda ou Aluguel para seus comissionados.

No menu de Comissões é possível criar campos complementares para o cadastro

1 : Para utilizar o cadastro de comissão, é preciso primeiro liberar acesso para o Perfil do usuário em:  
clique na aba "Acesso a Menus" em 'Gestão de Imóveis >> Venda >> Contratos >> Comissões' então terá as opções de Incluir, Editar e Excluir.

2 : Clicar sobre Comissões

3 : Cadastro de Comissão ( Venda e Aluguel )

Menu Identificação:

Selecione o contrato comissionado e a modalidade que buscará os dados de cálculos associados a ela e os parâmetros de integração da coligada do contrato.

Ao utilizar o tipo de controle para o valor máximo da comissão, o sistema limitará a comissão total de seus comissionados com esse valor/percentual, trazendo uma maior segurança na gestão de pagamentos.

Menu Parâmetros Integração:

Selecione os parâmetros integração que serão utilizados nessa comissão com os outros produtos da Linha RM.

Menu Itens da Comissão - Comissionados:

O cadastro de itens da Comissão tem como objetivo informar as regras da modalidade e seus comissionados, preparando assim para realizar os cálculos de seus comissionados.

Ao selecionar a regra da comissão, o sistema preencherá os campos de valores associados a ela,  podendo ser alterados somente na situação de "Em Preparação" ou "Calculados".

#### Alterando um Item de Comissão

* % Quem paga - Define a proporção da comissão paga por cada parte envolvida (Cliente ou Empresa) aos comissionados definidos na [Regra](https://tdn.totvs.com/pages/viewpage.action?pageId=773517977) da comissão. A seguir, estão as regras e orientações para preenchimento e edição deste campo:
  + - **Intervalo permitido:**O campo "% Quem Paga" só aceita valores numéricos **maiores que 0** e **menores ou iguais a 100**.
      * Se for digitado um valor fora desse intervalo, o sistema exibirá uma mensagem de erro e **não permitirá salvar o registro**.
    - **Edição e exclusão de registros:**A comissão paga ao corretor padrão **sempre soma 100%**, podendo ser dividida entre dois pagadores: **Empresa** e **Cliente**.
      * Caso deseje que **apenas uma parte arque com 100% da comissão** do corretor, é necessário **excluir o outro comissionado**.
      * Exemplo: se a comissão deve ser paga apenas pela empresa, exclua o registro do cliente comissionado.
      * Em cenários em que o botão de excluir a comissão do corretor não está habilitado, pode-se informar o valor de  0% no campo "% Quem Paga", da comissão paga pela empresa ou da comissão paga pelo cliente, para que o sistema (PI) recalcule automaticamente a comissão e atribua 100% da responsabilidade para a empresa, ou para o cliente.
    - **Distribuição parcial entre Empresa e Cliente nas comissões pagas ao corretor:**Ao alterar o percentual de um dos pagadores, o sistema **recalcula automaticamente** o percentual do outro, de forma que a **soma sempre permaneça em 100%**.
      * **Exemplo**: Se atualmente a empresa paga 50% e o cliente os outros 50%, e o usuário altera o percentual da empresa para 15%, o sistema ajustará automaticamente o percentual do cliente para 85%, após o salvamento desta edição.
    - **Prioridade de cálculo:**Alterações neste campo têm **prioridade sobre o valor ou percentual da comissão**.
      * Ao alterar "% Quem Paga", os campos **% Comissão** e **Valor da Comissão** serão **recalculados automaticamente** com base na nova proporção.
    - **Bloqueio temporário de campos:**Durante a edição deste campo, os campos relacionados ao valor da comissão ficam **temporariamente bloqueados**. Eles são reabilitados somente após o salvamento da alteração.
* Pagar a Imobiliária; (Está bloqueado nesse momento , não iremos liberar)
  + só pode alterar se não for imobiliária  e for quem paga empresa
    - se passar diferente será ignorado a alteração
* Tipo de Cálculo;
  + Se quem paga for empresa,  pode alterar conforme o tipo de cálculo para 0 e 1
    - se passar diferente será ignorado a alteração;
  + Se quem paga for cliente, pode alterar para o tipo 0, 1 e 2;
    - se passar diferente será ignorado a alteração
* Nro de Parcelas;
  + Só pode alterar se quem paga for empresa e cliente;
    - se passar diferente será ignorado a alteração
* % Comissão;
  + só pode alterar se o tipo valor for Percentual e não tiver alterado o percentual de quem paga;
    - se passar diferente será ignorado a alteração
    - Exemplo:  Corretor quem paga é 50% empresa  e 50% cliente, o tipo valor da comissão é PERCENTUAL, que tem o valor total de 2%, sendo 1% para cliente e 1% para empresa.
      * Vou alterar o percentual da comissão do corretor empresa para 2% e a parte cliente ficará com 1%, dessa forma o percentual de quem paga não é mais 50% para cada, vou recalcular a proporção de ambos que ficará com 66,6667% parte empresa e  33,3332% parte cliente%;
      * Vou criar o corretor quem paga cliente que ficará com o restante de 40%, dessa forma ficará com o resto do percentual 0,8%;
    - o mesmo raciocínio valerá para o tipo Tipo de valor quando for valor comissão;
    - Serão bloqueados os campos de percentual de quem paga a comissão e liberados após salvar os dados
* Valor Comissão.
  + Só pode alterar se o tipo valor for valor comissão e não tiver alterado o percentual de quem paga.
    - se passar diferente será ignorado a alteração
  + Serão bloqueados os campos de percentual de quem paga a comissão e liberados após salvar os dados.

#### Deletando um item de comissão

Caso seja deletado um comissionado que tem comissão paga pela empresa e pelo cliente, o valor da comissão/percentual fica para uma das duas situações.

Sendo assim, caso apague o comissionado cliente, então o valor/percentual da comissão vai para comissionado empresa e vice-versa.

Se for um comissionado comum é apagada normalmente o registro

#### Incluindo um item de comissão

Caso seja incluindo um comissionado que tem comissão paga pela empresa com percentual menor que 100%, então será criado o comissionado cliente com o a diferença desse percentual e calculando a nova proporção do percentual da comissão em cima dessa proporção de cliente e empresa.

Se for criado um comissionado com regra quem paga 100%, regra padrão, então cria apenas o próprio registro.

Importante!

O botão para Adicionar Comissionado somente será habilitado na interface de Comissões da Proposta do PI, se a Modalidade de Comissão tiver uma Regra de Comissão com o Tipo Pessoa Quem Recebe configurado para Comissionado Avulso Portal de Imóveis.

Menu Parcelas da Comissão:

O cadastro tem como objetivo definir o parcelamento da comissão, vencimento e seus valores,  bem como controlar a integração de cada parcela com outros produtos da linha RM.

As parcelas podem ser fixas ou oriundas das baixas de lançamentos financeiros com o seu percentual de comprometimento
