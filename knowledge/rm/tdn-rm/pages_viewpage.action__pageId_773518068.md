---
content_hash: 80d8d3559f53bfea21d02be6fdfc4c640f428bafc48e5df1681861ceeedea94e
fetched_at: '2026-06-29T00:11:36.803806+00:00'
page_id: '773518068'
product: rm
source: tdn-rm
title: TCGI - Comissão - Imóveis X Modalidade de Equipe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518068
version: 7
---

### **Associação dos Imóveis X Modalidades de Equipe da Comissão**

Venda | Contratos | Comissões | Imóveis X Modalidades de Equipe da Comissão

Esse processo também poderá ser acessada nas visões de Modalidades de Equipe da Comissão, Empreendimento, Unidade, Subunidade e Imóveis

O cadastro de associação de imóveis a modalidade de equipe da comissão é para definir as regras para o pagamento de uma comissão para um Empreendimento, Unidade, Subunidade, Imobiliária / Responsável da Equipe ou imóvel, permitindo assim que as regras cheguem até um nível com granularidade baixa, bem específico. O conceito é similar ao de tabelas de preço. Além disso, será possível trabalhar com a vigência da modalidade de comissão, para permitir a utilização de regras para um período específico, com a finalidade de permitir ações promocionais de comissionamento.

Ao cadastrar uma associação, os campos de Tipo de Contrato, Prioridade, Id Modalidade e Data de Início são campos obrigatórios

Um empreendimento /unidade /subunidade/Imobiliária ou Responsável da Equipe/imóvel poderá ter várias modalidades, mas com prioridades diferentes quando houver interseção de datas para aquele nível de associação.

Quando associamos uma modalidade sem selecionar nenhum outro campo específico, isso que dizer que a modalidade é global e será usado para todas as coligadas, todos os empreendimentos e suas unidades,  a partir da data de início e até o seu término. O mesmo vale se o tipo de contrato fosse Aluguel .

***Dica:***

Se desejarmos fazer uma liquidação de carnaval, para incentivar os corretores a vender nesse período, para uma empreendimento específico ou um lote, devemos preencher os campos das imagens abaixo.

Note que essa modalidade é diferente da anterior e nela aumentamos o percentual de comissão pago ao corretor.

Após esses cadastros teremos três modalidades associadas na base, sendo que o empreendimento '*Terra Nova'*, terá duas modalidades, o *Lote 18* do empreendimento *'Loteamento Sem Nome'* terá duas modalidades,  o empreendimento *'Loteamento Sem Nome'*  terá somente uma modalidade, que é o Modelo Padrão e o Empreendimento '29 - Bella Vista', também terá uma modalidade, que é o Modelo Padrão.

**A partir desses associações, vamos fazer alguns cenários de Geração de Comissão:**

1. Vou fazer uma venda para o Empreendimento '27 - Loteamento Sem Nome', Quadra 6 e Lote 18
   1. Na data de venda  01/01/2022, o sistema utilizará a modalidade 1- Padrão de Venda, pois ela está no período da venda;
   2. Na data de venda 27/02/2022, o sistema encontrará duas modalidades para o mesmo período, mas utilizará a modalidade 5- Queima de Estoque, pois ela é a mais específica (Definiu até a subunidade) ;
      1. Caso houvesse duas modalidades diferentes para o mesmo período e para a mesma subunidade, o sistema irá desempatar com a prioridade;
2. Vou fazer uma venda para o Empreendimento '28 - Terra Nova', Quadra 1 e Lote 1
   1. Na data de venda  01/01/2022, o sistema utilizará a modalidade 1- Padrão de Venda, pois ela está no período da venda;
   2. Na data de venda 27/02/2022, o sistema encontrará duas modalidades para o mesmo período, mas utilizará a modalidade 5- Queima de Estoque, pois ela é a mais específica (Definiu até o empreendimento) ;
      1. Caso houvesse duas modalidades diferentes para o mesmo período e para o mesmo empreendimento, o sistema irá desempatar com a prioridade;
3. Vou fazer uma venda para o Empreendimento '29 - Bella Vista', Quadra 2 e Lote 2
   1. Na data de venda  01/01/2022, o sistema utilizará a modalidade 1- Padrão de Venda, pois ela está no período da venda;
   2. Na data de venda 27/02/2022, o sistema encontrará apenas uma modalidade para o período, pois não foi definido nenhuma regra específica para esse empreendimento, então  utilizará também a modalidade '1- Padrão de Venda';

Empreendimento

**Configuração de Modalidade por Empreendimento**

Somente deverá realizar a associação de modalidades com empreendimento quando deseja pagar comissão com taxas diferentes entre empreendimentos

**Exemplo:**

| Modalidade - Empreendimento Alfa | Modalidade - Empreendimento Beta |
| --- | --- |
| 1. Corretor 1,5%; 2. Supervisor 0,4%; 3. Gerente 0,20% | 1. Imobiliária 2%; 2. Supervisor 0,5%; 3. Gerente 0,25% |

**Ordem de Prioridade de busca de modalidade por****Empreendimento**

1. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote, Imobiliária / Responsável da Equipe
2. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote,
3. Modalidade, Empreendimento, Bloco/Quadra, Imobiliária / Responsável da Equipe
4. Modalidade, Empreendimento, Bloco/Quadra,
5. Modalidade, Empreendimento, Equipe/Imobiliária
6. Modalidade, Empreendimento
7. Modalidade, Equipe/Imobiliária
8. Modalidade
Equipe/Imobiliária

**Configuração de [Imobiliária / Responsável da Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=784771846)**

**Processo - Associação dos Imóveis X Modalidades de Equipe da Comissão**

Através desse processo, a forma de comissionamento será mais flexível e vai ser definida em vários níveis diferentes.

Nesse processo, a modalidade, data de início e prioridade são campos obrigatórios.

O tipo de contrato vem da Modalidade, ou seja se for venda, só posso selecionar dados da Venda e se for aluguel, só pode selecionar dados do aluguel.

**Se a Modalidade for Contrato de Venda, poderá associar :**

1. Global;
2. Empreendimento;
3. Unidade:
4. Subunidade

**Se a Modalidade for Contrato de Aluguel, poderá associar :**

1. Global;
2. Imóvel;

Atenção

Uma Modalidade poderá ser associada em vários empreendimentos / unidades / subunidades / Equipe(Imobiliária)  ou a um Imóvel do Aluguel. 

Um empreendimento / unidade / subunidade/ Equipe(Imobiliária) / imóvel poderá ter várias modalidades, mas com prioridade diferente quando houver interseção de datas;

As regras de validação sãos as mesmas do cadastro de Imóveis X Modalidades de Equipe da Comissão 

Associação da modalidade com os empreendimentos

Associação da modalidade e empreendimentos anteriores com as equipes/imobiliárias, sendo que essa associação não é obrigatória, pois a empresa pode trabalhar com modalidades gerais, com mesma taxas de comissão.

Somente deverá realizar essa associação  de modalidades com equipes/imobiliárias quando deseja pagar comissão com taxas diferentes entre a empresa e a imobiliária parceira, ou até mesmo com equipes diferentes
