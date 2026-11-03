---
content_hash: 019b66dd9f086e93c6730ecc30257409d58533120422b86f147c0de7ac562045
fetched_at: '2026-06-29T00:09:49.248759+00:00'
page_id: '435105267'
product: rm
source: tdn-rm
title: Plano - Modalidades
type: documentation
url: https://tdn.totvs.com/display/LRM/Plano+-+Modalidades
version: 23
---

Ao copiar uma modalidade, caso os valores das regras não batem com o valor da venda, o valor da última regra receberá a diferença de valores.

Nesta opção de menu serão inseridos as Modalidades de Vendas que serão utilizados no cadastro de Vendas.  
Através do cadastro é possível controlar:  
  
**Dados Gerais /****Identificação**  
Ao cadastrar ou editar uma Modalidade de Venda, abrirá a janela de edição, na pasta Identificação, onde será possível cadastrar os seguintes campos:

* **Global**: Informe se a Modalidade de Venda é visível a todas as coligadas ou somente a coligada corrente;

Quando uma modalidade global for associada à um empreendimento, tabela de preço ou uma venda, elas não poderão ser alteradas para local em nenhuma coligada.

* **Tipo de Modalidade:**Informe o Tipo da Modalidade. O sistema dispõe de 4 tipos, segue:
  + Todas: A modalidade será apresentada em todas as entidades que tenha Plano de Financiamento (Venda, Aditivo e Distrato);
  + Venda: A modalidade será apresentada apenas na venda;
  + Aditivo: A modalidade será apresentada apenas no aditivo;
  + Distrato: A modalidade será apresentada apenas no distrato;
* **Tipo de Restrição no PI**:
  + **Não Restringe** deixará o usuário alterar a modalidade dentro do PI livremente.
  + **Restringe Novos Componentes** impedirá o usuário de criar novos componentes dentro do PI.
  + **Não Visível** a modalidade dentro do PI
* **Modalidade**: Informe o código para a Modalidade de Venda;
* **Descrição Modalidade**: Informe a descrição da Modalidade de Venda. Ex.: Financiamento Padrão.
* **Dias de Vencimento Ex. 5;10;15**: Se configurado esse campo com as datas que a empresa aceita no seu vencimento de parcelas, o sistema ao copiar a modalidade da venda, o sistema utilizara a data da venda para definir o dia de vencimento posterior e igual a essa data, que será armazenado na venda, campo dia de vencimento do contrato. Se o campo ficar em branco, seguirá a regra existente da data da venda como base.  
  + Ex: Data Venda 22/11/2022, dias configurados na modalidade "5;10;20;25", então o sistema irá verificar a primeira data após esse dia que será o dia 25.  Dessa forma, o dia do vencimento será sempre no dia 25 e a data base do primeiro vencimento será o dia 25/11/2025.
  + Ex: Data Venda 26/11/2022, dias configurados na modalidade "5;10;20;25", então o sistema irá verificar a primeira data após esse dia. Como não tem, ele utilizará a primeira data do próximo mês, que nesse caso será o dia de vencimento 5 e a a data base para o primeiro vencimento será o dia 05/12/2022.
* **Data de Início**: Informe a data de início para a vigência desta Modalidade de Venda;
* **Data de Término**: Informe a data de término para a vigência desta Modalidade de Venda;
* **Efeito Financeiro**: Este campo é usado para definir qual será a opção de contabilização informada nos Lançamentos Financeiros gerados para o TOTVS Gestão Financeira. Os lançamentos serão provenientes das vendas do TOTVS Incorporação respeitando a configuração feita na modalidade associada na venda. Os Efeitos Financeiros disponíveis são: "Não Contabilizar", "Efeito Contábil", "Baixa Contábil" ou "A Contabilizar".

A opção selecionada irá influenciar no momento da baixa do lançamento financeiro no sistema TOTVS Gestão Financeira. Por exemplo, um Lançamento Financeiro com o Efeito Financeiro "Não Contabilizar", poderá ser baixado sem a necessidade de informar um Evento Contábil no momento da baixa no TOTVS Gestão Financeira.

Ao cadastrar uma nova venda, só irá aparecer as modalidades que estiverem o campo início da vigência informado e dentro do início da validade do tempo;

Ao cadastrar uma nova venda, só irá aparecer as modalidades que estiverem dentro do limite de tempo informado no campo término da vigência;

**[**Dados Gerais /**Eventos Contábeis](https://tdn.totvs.com/display/public/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Contabilidade)**   
Nesta opção, será possível cadastrar os eventos contábeis padrões/default que serão realizados nesta Modalidade de Venda.

* **Venda/Aluguel:** Informe o Evento Contábil que será utilizado para contabilizar a **inclusão** do Contrato de Venda. Ao parametrizar um Evento Contábil para este fim, deve-se levar em consideração que o Imóvel deverá ser retirado do estoque da empresa e registradas as contabilizações para recebimento a curto e longo prazo, conforme a política de cada empresa
* **Entrega de chave:** Informe o Evento Contábil para contabilizar a **Entrega de Chaves** e também o **Valor dos Custos** relativos a esta ação. É importante ressaltar que a contabilização deste evento só é possível após a efetivação da Venda/Aluguel.
* **Eventos no reajuste:** Informe os Eventos Contábeis que serão utilizados para a contabilizar os valores calculados pelo **Processo de Reajuste da Venda**.

**Reajuste Inflacionário**

**Reajuste Deflacionário**

* **Distrato:** Informe o Evento Contábil será utilizado para contabilizar as movimentações relativas ao **Distrato** do Contrato de Venda..
* **Seguro por Empreendimento:** Informe o Evento Contábil que será utilizado para contabilizar os valores Seguro por Empreendimento, calculados pelo Processo **Gerar Seguro Por Empreendimento**, disponível no menu de Processos da Venda.
* **Eventos no Aditivo:** Informe os Eventos Contábeis que serão utilizados ao se efetivar um Aditivo para o Contrato de Venda.

**Aditivo Inflacionário**

**Aditivo Deflacionário**

* **Evento de Transferência:** Informe um Evento Contábil para tratar as movimentações realizadas pela transferência de Saldo entre [**Longo Prazo e Curto Prazo**](https://tdn.totvs.com/pages/viewpage.action?pageId=519726472), conforme a parametrização do período de cada um desses eventos.

Sabia Mais

Para maiores detalhes sobre o porquê desses Eventos Contábeis, acesse o link abaixo:

# [Contratos de Venda - Dados Gerais - Contabilidade](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Contabilidade)

****Dados Gerais /**Valores Tipo de Parcela**  
Nesta opção, será possível cadastrar os Tipos de Parcelas que serão utilizados nesta Modalidade de Venda. Se necessário pode ser preenchido o valor da Taxa Juros Mora % ou % Multa Atraso e ainda associar a Conta/Caixa ao tipo de parcela.  
  
**Integração / Portal de Imóvel**A fim de atender a demanda do Portal de Imóveis (PI) e de outros eventuais portais de venda que possam vir a integrar com o TOTVS Incorporação, existem os seguintes campos:

* **% Mínimo de Desconto:** Define o percentual mínimo de desconto que pode ser aplicado na proposta, não permitindo que seja aplicado um percentual inferior ao parametrizado;
* **% Máximo de Desconto:** Define o percentual máximo de desconto que pode ser aplicado na proposta, não permitindo que seja aplicado um percentual superior ao parametrizado;
* **% Mínimo de Sinal:** Define o percentual mínimo que a parcela de sinal pode ter em relação ao valor total da proposta, não permitindo parcelas com um valor percentual inferior ao parametrizado;
* **% Máximo de Sinal:** Define o percentual máximo que a parcela de sinal pode ter em relação ao valor total da proposta, não permitindo parcelas com um valor percentual inferior ao parametrizado;
* **% Mínimo de Arrecadação:** Define o percentual mínimo de arrecadação, que é calculado com base nos juros prefixados dos modelos PRICE, SAC e SACRE, quando a proposta utilizar essas modalidades de venda;
* **% Máximo de Arrecadação:** Define o percentual máximo de arrecadação, que é calculado com base nos juros prefixados dos modelos PRICE, SAC e SACRE, quando a proposta utilizar essas modalidades de venda;
* **% Taxa TMA - VPL:** Define o percentual da Taxa Mínima de Atratividade, que indica um retorno mínimo para que um investimento valha a pena para um investidor. Este percentual é verificado no momento da descapitalização das parcelas da proposta.
* **% de Perda VPL:** Define o percentual de VPL aceitável, quando o Plano de Financiamento da proposta é trazido a valor presente. Este cálculo é realizado para validar as alterações nos valores das parcelas e datas de vencimento, que são realizadas pelo corretor ao montar a proposta. O sistema considera o Percentual de Perda VPL, que estiver parametrizado na entidade mais específica, ou seja, na que for mais detalhada em relação à proposta.

  Ou outras palavras, o sistema respeitará  a seguinte ordem de verificação, partido da entidade mais específica, para a mais genérica, caso aquela não tenha esta informação parametrizada:

  1° - [Alçada de Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=641678463), localizado no Portal do Imóvel;

  2º - Modalidade, localizado no TCGI; ou

  3º - [Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=744469090), localizado no TCGI.

  Assim, por exemplo, caso haja uma Alçada de Aprovação parametrizada no Portal de Imóvel, ela irá prevalecer sobre o percentual de perda VPL, parametrizado na Modalidade, que por sua vez, prevalece sobre este mesmo percentual parametrizado no Empreendimento.

* **Nro Máximo Meses Após Entrega:** Se configurado esse campo, a proposta da venda (Portal de Imóveis) será aprovada se não houver parcelas com vencimentos posterior a data de entrega mais o número de meses configurado nesse parâmetro. 
  + Ex: Data de Entrega 01/01/2024, configurei 3 meses após a entrega, como o limite para existir parcelas, então a proposta da venda não poderá ter nenhuma parcela com vencimento a partir da data 01/04/2024;
* **Fórmula de Validação de VPL:**  **A partir da versão 12.1.2506.** Valida um regra específica que permite aprovação do gestor quando não aprovada na proposta do PI. Com por exemplo, só aceito um sinal de R$ 5000,00 independente do valor da venda; A fórmula deve retornar 1 (verdade) ou 0 (falso);

Estes campos são destinados ao controle de Desconto, Perda VPL, Sinal, Arrecadação ou Taxa VPL na proposta no portal, onde o usuário deverá indicar o percentual mínimo e/ou máximo sobre o valor total da proposta que o componente da venda deve representar.  
  
**Plano de Financiamento /****Condições de Financiamento Modalidade**  
É possível incluir as Condições de Financiamento da Modalidade que serve de parâmetro para geração do plano de financiamento. O sistema disponibiliza que os  podem ser separados por grupo de acordo com cada necessidade especificamente.

false

Informações Complementares

---
