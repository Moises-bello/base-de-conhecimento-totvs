---
content_hash: 7ca68341622bd47af312b4207c96ab658fdceb482732f85f974e7489eb970adc
fetched_at: '2026-06-29T00:09:47.999115+00:00'
page_id: '435105119'
product: rm
source: tdn-rm
title: Modalidades - Anexo - Condições de Financiamento da Modalidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105119
version: 12
---

Para acessar os Componentes da Modalidade, ao cadastrar ou editar uma Modalidade de Venda, clique em Anexo e depois em Componente da Modalidade.  
  
Nesta opção, serão inseridos os Componentes da Modalidade de Venda que serão utilizados no cadastro de Vendas.  
Através do cadastro é possível controlar:  
  
**Identificação**  
Ao cadastrar ou editar um Componente da Modalidade de Venda, abrirá a janela de edição, na pasta Identificação, onde iremos cadastrar os seguintes campos:  
  
Grupo:  
Informe o número do grupo que este componente fará parte.

Os componentes de reajustes somente terão efeito sobre os componentes do tipo principal de mesmo grupo. Uma modalidade de venda pode conter vários grupos de financiamento, ou seja, um mesmo componente poderá ser usado em grupos distintos, com regras diferentes.

Componente:  
Informe o componente a ser cadastrado. O sistema apresentará uma lista de opções de Componentes já previamente cadastrados no sistema TOTVS Incorporação no menu Cadastro | Condições de Venda | Componente.  
  
Observação: Ao preencher estes campos mencionados acima, dependendo do Tipo de Componente do Componente escolhido, será apresentado outros campos para o devido preenchimento. Sendo eles:

Tipos de Componentes geradores de Parcelas:

* : Será apresentado se o Tipo de Componente for Entrada;
* : Será apresentado se o Tipo de Componente for Principal;
* : Será apresentado se o Tipo de Componente for Financiamento CEF, Terreno CEF, Subsídio CEF, Recurso Mutuário CEF e FGTS CEF;
* : Será apresentado se o Tipo de Componente for Seguro;
* : Será apresentado se o Tipo de Componente for Entrada, Principal, Resíduo, Seguro ou Alíquota;

Aviso:

Para a integração com o **novo** ***Portal de Imóveis (PI), nova proposta, novo reajuste, nova comissão, versão 12.1.2306***, , os Tipos de Componentes acima, que são geradores de Parcelas, apresentam os campos abaixo:

No agrupador *Vencimento*:

* *Tipo Data Base Vencimento*: nesta opção, será possível definir o tipo de data que será utilizado pelo PI para cálculo do vencimento da primeira Parcela deste Tipo de Parcela. As opções disponíveis são:
  + Data da Venda/Processo  (valor padrão do sistema): utiliza a data corrente do sistema, no momento da criação da Proposta, para calcular a data de vencimento inicial das parcelas;
  + Data do Componente Anterior: acrescenta 1 mês à data de vencimento do componente anterior, das Condições de Financiamento para calcular a data de vencimento da parcela;
  + Data de Entrega: utiliza a data de entrega do imóvel para calcular o primeiro vencimento da parcela;
  + Data do Habite-se utiliza a data do Habite-se do imóvel para calcular o primeiro vencimento da parcela; e

Para o Tipo de Componente 50 Financiamento CEF, do Modelo de Cálculo Minha Casa Minha Vida

* + Data do Cronograma MCMV: utiliza a data do Cronograma do Minha Casa Minha Vida para calcular o primeiro vencimento da parcela.

* *Nro Meses Data Base Vencimento*: ao definir o valor neste campo, o sistema ao copiar a modalidade para a venda incrementará ou decrementará a data base calculada com o *Tipo Data Base Vencimento* e  atualizará a data de vencimento da primeira parcela da regra. Este campo aceita valores numéricos positivos e negativos. Temo como valor padrão 0 meses.
* Se o nro de meses data base for zero e o tipo principal, o sistema sempre colocará um mês a mais que a data da venda, isso para manter o comportamento do RM.exe que já trabalhava assim.

**No agrupador *Portal de Imóveis*:**

* **Nro Mínimo de Parcelas**: quando parametrizado, o sistema irá validar essa quantidade na edição das Condições de Pagamento da Proposta, no PI, não permitindo um número de parcelas inferior ao valor configurado. Se estiver nulo/sem preenchimento não será realizada nenhuma validação.
* **Nro Máximo de Parcelas**: quando parametrizado, o sistema irá validar essa quantidade na edição das Condições de Pagamento da Proposta, no PI, não permitindo um número de parcelas superior ao valor configurado. Se estiver nulo ou sem preenchimento não será realizada nenhuma validação.
* **% Mínimo Valor**: quando parametrizado, o sistema irá validar o percentual mínimo, da soma das parcelas desse Tipo, na edição das Condições de Pagamento da Proposta, no PI em relação ao Valor da Proposta, não permitindo que esse percentual fique inferior ao valor configurado. Este Percentual é sempre calculado sobre o valor da venda na Proposta. Uma vez definido este percentual, não será permitido a sua exclusão na Proposta, pois a regra está exigindo um valor mínimo para o mesmo. Quando configurado com valor nulo ou sem preenchimento, não será realizada nenhuma validação.
* **% Máximo Valor**: quando parametrizado, o sistema irá validar o percentual máximo, da soma das parcelas desse Tipo, na edição das Condições de Pagamento da Proposta, no PI em relação ao Valor da Proposta, não permitindo que esse percentual fique superior ao valor configurado. Este Percentual é sempre calculado sobre o valor da venda na Proposta. Quando configurado com valor nulo ou sem preenchimento, não será realizada nenhuma validação.
* **Permite Alterar Vencimento**: se marcado permite ao usuário do PI alterar a data de vencimento da parcela, no momento da edição da Proposta, no PI;
* **Permite Alterar Qtde Parcelas**: se marcado permite ao usuário do PI alterar a quantidade de parcelas do Plano de Financiamento, no momento da edição da Proposta, no PI. Para o Modelo de Cálculo MCMV este campo estará sempre bloqueado;
* **Permite Alterar Valor Parcela**: se marcado permite ao usuário do PI alterar o valor das parcelas, no momento da edição da Proposta, no PI. Para os Modelos de Cálculo pré-fixados (Price, SAC, SACRE, MCMV e uso de Fórmulas) este campo está sempre bloqueado;
* **Permite Alterar Valor Total**: se marcado permite ao usuário do PI alterar o valor total do Plano de Financiamento do imóvel, no momento da edição da Proposta, no PI;
* **Permite Calcular VPL**: se marcado o PI irá considerar os valores deste Tipo de Parcela no cálculo da validação da VPL da Proposta, no PI;
* **Fórmula para validar a manipulação do componente:**  **A partir da versão 12.1.2506.** Valida um regra específica que **não** permite aprovação do gestor, é desfeito a alteração imediatamente a após não atender a condição da fórmula. Com por exemplo, só aceito um sinal de R$ 5000,00 independente do valor da venda; A fórmula deve retornar 1 (verdade) ou 0 (falso);

Tipos de Componentes complementares aos geradores de Parcelas:

* : Será apresentado se o Tipo de Componente for Juros Fixo;
* : Será apresentado se o Tipo de Componente for Correção Monetária;
* : Será apresentado se o Tipo de Componente for Encargos Financiamento;
* : Será apresentado se o Tipo de Componente for Desconto de Juros de Contrato / Correção Monetária
* : Será apresentado se o Tipo de Componente for Descontos;
* : Será apresentado se o Tipo de Componente for Resíduo;

Informações Complementares

---
