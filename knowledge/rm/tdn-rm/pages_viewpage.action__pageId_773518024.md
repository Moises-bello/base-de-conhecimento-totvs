---
content_hash: e3a8a1cbfb7e99676eee851d605d693e28828fad647f7b4efeda234eb7802398
fetched_at: '2026-06-29T00:11:36.797099+00:00'
page_id: '773518024'
product: rm
source: tdn-rm
title: TCGI - Comissão - Modalidade de Equipe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518024
version: 7
---

### **Cadastro de Modalidade de Modalidades de Equipe da Comissão**

Venda | Contratos | Comissões | Modalidades de Equipe da Comissão

O cadastro de modalidade de comissão é para definir as regras para o pagamento de uma comissão,  desta forma, poderá criar várias modalidades, seja global , por empreendimento, por unidade, por subunidade, por equipe/imobiliária ou até por imóvel, permitindo assim que as regras cheguem até um nível com granularidade baixa, bem específico. O conceito é similar ao de modalidades da  venda. Nesse momento não será definido a sua vigência,  apenas a composição da modalidade da regra.

Empreendimento

**Configuração de Modalidade por Empreendimento**

Somente deverá realizar a associação de modalidades com empreendimento quando deseja pagar comissão com taxas diferentes entre empreendimentos

**Exemplo:**

| Modalidade - Empreendimento Alfa | Modalidade - Empreendimento Beta |
| --- | --- |
| 1. Corretor 1,5%; 2. Supervisor 0,4%; 3. Gerente 0,20% | 1. Imobiliária 2%; 2. Supervisor 0,5%; 3. Gerente 0,25% |

**Ordem de Prioridade de busca de modalidade por Empreendimento**

1. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote, Equipe/Imobiliária
2. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote,
3. Modalidade, Empreendimento, Bloco/Quadra, Equipe/Imobiliária
4. Modalidade, Empreendimento, Bloco/Quadra,
5. Modalidade, Empreendimento, Equipe/Imobiliária
6. Modalidade, Empreendimento
7. Modalidade, Equipe/Imobiliária
8. Modalidade
Equipe/Imobiliária

**Configuração de [Equipe/Imobiliária](https://tdn.totvs.com/pages/viewpage.action?pageId=784771846).**

**Tipo de Contrato**

Definir se é contrato de Venda ou Aluguel

**Ativo**

Permite associar a modalidade a um empreendimento, unidade, subunidade ou imóvel.

Este parâmetro não desvincula a sua associação as entidades acima.

**Tipos de Controle para o valor máximo da comissão:**

Percentual:

Habilita percentual para que o usuário possa informar.

Valor Fixo:

Habilita o campo valor para que o usuário possa informar.

Fórmula percentual ou Fórmula valor:

Habilita Código da Fórmula : Para calcular o valor ou percentual máximo que será utilizado no cálculo da comissão de cada regra.

Não Controla:

Valor ou Percentual Máximo (esse campo **não deverá ser preenchido** se a opção do tipo de controle for "não controla". Caso contrário, deverá ser preenchido com valor, percentual ou fórmula, dependendo do tipo selecionado)

Código da Fórmula do valor base:

Fórmula valor Base - Fórmula para cálculo do valor base para calcular a Comissão, na integração com Portal de Imóveis o valor será calculado automaticamente, não precisando do uso de fórmulas  
Valor Base - Valor Calculado pela Fórmula ou Enviado do Portal de Imóveis

Regras de Vencimentos das Parcelas

* **1ª Regra - Dias Mínimo 1º Pagamento:** Dias mínimo para realizar o 1º pagamento da parcela não atrelado a baixa ou dias mínimo para realizar o pagamento a partir da data de baixa;
* **2ª Regra - Dias de Vencimento:** Dias de vencimentos permitidos para realizar o cálculo da data de pagamento da comissão, o não preenchimento utilizará apenas as informações dos campos anteriores para o cálculo.
* **3ª Regra - Periodicidade:** Periodicidade para cálculo dos vencimentos das parcelas não atrelado a baixa, pois na regra do atrelado sempre depende da data do pagamento;

**Exemplos: Data da Comissão = Data da Venda = Data Base do Vencimento = 12/01/2022 , Valor da Comissão R$ 3000,00 em 3X para o corretor, não atrelado a baixa .**

* Aplicando a regra do 1º vencimento:
  + 1ª Regra =  12/01/2022 + 10 dias = 22/01/2022;
  + 2ª Regra = o dia 22 não está nos dias permitidos, então utilizarei o próximo dia a esta data que é 25/01/2022
  + 3ª Regra =o primeiro vencimento não utiliza essa regra, somente para as próximas parcelas
* Aplicando a regra do 2º vencimento:
  + 3ª Regra = Aplica somente esta regra adicionado a periodicidade cadastra 1 em relação a data de vencimento anterior
* Aplicando a regra do 3º vencimento:
  + 3ª Regra =Aplica somente esta regra adicionado a periodicidade cadastra 1 em relação a data de vencimento anterior

1º parcela, R$ 1000,00 Vencimento dia 25/01/2022

2º parcela, R$ 1000,00 Vencimento dia 25/02/2022

3º parcela, R$ 1000,00 Vencimento dia 25/03/2022

**Exemplos: Data da Comissão = Data da Venda = Data Base do Vencimento = 18/01/2022 , Valor da Comissão R$ 3000,00 em 3X para o corretor, não atrelado a baixa .**

* Aplicando a regra do 1º vencimento:
  + 1ª Regra =  18/01/2022 + 10 dias = 28/01/2022;
  + 2ª Regra 28/01/2022 não está nos dias permitidos, então utilizarei o próximo dia a esta data, mas não existe neste caso. Então, utilizarei o primeiro dia disponível 5 do próximo mês que é 05/02/2022
  + 3ª Regra =o primeiro vencimento não utiliza essa regra, somente para as próximas parcelas
* Aplicando a regra do 2º vencimento:
  + 3ª Regra = Aplica somente esta regra adicionado a periodicidade cadastra 1 em relação a data de vencimento anterior
* Aplicando a regra do 3º vencimento:
  + 3ª Regra =Aplica somente esta regra adicionado a periodicidade cadastra 1 em relação a data de vencimento anterior

1º parcela, R$ 1000,00 Vencimento dia 05/02/2022

2º parcela, R$ 1000,00 Vencimento dia 05/03/2022

3º parcela, R$ 1000,00 Vencimento dia 05/04/2022

**Exemplos: Data da Comissão = Data da Venda = Data Base do Vencimento = 12/01/2022 , Valor da Comissão R$ 3000,00 para o corretor, atrelado a baixa 50% do valor da parcela.**

* 1º Baixa da Parcela do Plano de Financiamento  no dia 13/01/2022, no valor de R$ 2000,00:
  + 1ª Regra =  13/01/2022 + 10 dias = 23/01/2022;
  + 2ª Regra = o dia 23 não está nos dias permitidos, então utilizarei o próximo dia a esta data que é 25/01/2022
  + 3ª Regra = não utiliza essa regra, pois depende sempre da baixa as próximas parcelas
* 2º Baixa da Parcela do Plano de Financiamento  no dia 15/02/2022, no valor de R$ 5000,00  
  + 1ª Regra =  15/02/2022 + 10 dias = 25/02/2022;
  + 2ª Regra = o dia 25 está nos dias permitidos, então utilizárei-lo 25/01/2022
  + 3ª Regra = não utiliza essa regra, pois depende sempre da baixa as próximas parcelas

1º parcela, R$ 1000,00 Vencimento dia 25/01/2022

2º parcela, R$ 2000,00 Vencimento dia 25/02/2022

Exemplo de uma Modalidade da Comissão Global, que poderia ser também uma para o empreendimento, uma para subunidade e até mesmo uma para o imóvel se a modalidade fosse de Aluguel.

Menu Regras da Modalidade

Objetivo de associar as regras da comissão a modalidade

Menu Parâmetros de Integração

Objetivo de associar os parâmetros de integração com outros sistemas, Financeiro, Movimento e Folha de Pagamento, para as coligadas que a modalidade impactará .

Associar Parâmetro Integração na Modalidade

O processo  de Associar Modalidades aos Parâmetros de Integração encontra-se na visão de modalidade da Comissão, onde o usuário poderá selecionar várias modalidades, e o wizard terá quatro etapas:   
1 :  Para selecionar as coligadas que serão configuradas  
2:   Outra para selecionar os parâmetros de movimento de todas as coligadas configuradas na 1 etapa;  
3:   Outra para selecionar os parâmetros do Financeiro de todas as coligadas configuradas na 1 etapa  
4:   Por fim selecionar os parâmetros de evento da Folha de Pagamentos e o centro de custo da coligada centralizadora, onde será associada para todas as coligadas da 1 etapa.  
**Não pode selecionar mais de um parâmetro da mesma coligada** e, se **não existir o parâmetro da coligada desejada**, selecione um **parâmetro como padrão** de acesse o processo desse parâmetro e realize a cópia entre coligadas desse parâmetro

No final do Processo é feita a cópia dos parâmetros de Integração para Modalidade.
