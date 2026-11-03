---
content_hash: b61f2494325a4937a0dc59a03b4105777ab09ff22439cfae14eb4f9cdadc8cd2
fetched_at: '2026-06-29T00:11:36.829240+00:00'
page_id: '773518647'
product: rm
source: tdn-rm
title: TCGI - Comissão - Gerar Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773518647
version: 8
---

### Processo - Gerar  Comissão

Sobre o Processo de Calcular a Comissão no TOTVS Gestão de Imóveis, antigamente a comissão era calculada ao salvar, com o novo processo , agora é possível calcular todos os itens de comissões e todas as comissões.  
Esse processo está disponível no menu em: 'Comissões | Gerar Comissão'.

Será também disponibilizado dentro da visão da comissão aberta a chamada do processo de Gerar Comissão para melhor usabilidade do usuário.

O cálculo seguirá a ordem dos valores da comissão e posteriormente as regras da comissão ordenado pela ordem de cálculo.

Importante!

Quando o valor da comissão é calculado via fórmula, o sistema permite recalcular o Valor Base desta comissão.

Esta característica é muito útil, principalmente quando há desconto na venda/proposta, ou seja, quando o valor da subunidade na venda está diferente do valor da subunidade na Tabela de Preço.

Tela da Venda

**Comissão:**

* Calcular o Valor Base da Comissão se for via fórmula e jogar no campo Valor Comissão Base;
* Calcular o Valor Máximo da Comissão se o tipo definido o for Fórmula e jogar o seu valor para o campo valor ou percentual ;  
  Armazenar o log de cálculo das fórmulas em sues campos correspondentes

**Item de Comissão:**

* Calcular na Ordem de Cálculo;
* Calcular o valor do item comissão e jogar seu valor para percentual ou valor e armazena a memória de cálculo da fórmula;
* Calcular a Fórmula de % máximo somente quando for implementado outro serviço de criar as parcelas vinculado ao recebimento.

Se o tipo comissão empresa for "Não vinculado a baixa", deverá gerar as parcelas das comissões e jogar o valor do arredondamento na última parcela, definir a data de vencimento de cada parcela. Se o tipo for vinculado a baixa, existirá um outro processo para gerar as parcelas e as baixas vinculadas as parcelas.

### **Exemplo da Geração de Comissão:**

**01 ) Cadastro da Modalidade de Calculo da Comissão**

Informo quantidade de Parcelas , pago pela empresa ou cliente... Se é fixo ou vinculado ao recebimento de parcelas.

**02) Cadastro de Regra de Comissão.**

Exemplo do cadastro de Corretor Padrão

Neste exemplo de Regra ( Corretor Padrão ) , encontra-se de forma Hibrido ( 50 % para Empresa e 50 % Cliente ).

50% dos 2% = 1% pela Empresa

50% dos 2% = 1 % pelo Cliente.

**03) Cadastro da Modalidade  de Equipe**

Cadastro da Modalidade de Comissão - Inserir as regras que irão fazer parte da Modalidade , e neste exemplo , existem 4 regras cadastradas.

* Corretor Padrão
* Imobiliária
* SDR
* Diretor

**04) Imóveis x Modalidades de Equipe de Comissão**

Cadastro de  [Imóveis X Modalidade de Equipe](https://tdn.totvs.com/pages/viewpage.action?pageId=773518068), esse cadastro irá definir a ordem que serão aplicadas as comissões.

Ao selecionar uma venda, o campo '*Valor Comissão Base*' será preenchido automaticamente com o valor padrão da venda. Se necessário, esse valor pode ser alterado pelo usuário para um valor específico.

IMPORTANTE : Versão 12.1.2306 em Diante !

**O que Mudou para se gerar Comissão :**  Em clientes que não possuem o Portal de Imóveis e o mesmo trabalha com vários modelos de comissionamentos , passou a ter a opção de selecionar qual modalidade de comissão ele quer utilizar em determinado contrato (venda) conforme print abaixo:

Através dessa melhoria o usuário , passa a não ter mais a  necessidade de preencher inúmeras telas manualmente independente da modalidade selecionada, não obrigando a trabalhar com uma única modalidade default, o que melhora muito sua experiência com o ERP com o controle de comissionamento.

A Modalidade associada  ao contrato, irá aparecer na tela de Id Modalidade e o usuário irá poder selecionar a Modalidade desejada.

Empreendimento

**Configuração de Modalidade por Empreendimento**

Somente deverá realizar a associação de modalidades com empreendimento quando deseja pagar comissão com taxas diferentes entre empreendimentos

**Exemplo:**

| Modalidade - Empreendimento Alfa | Modalidade - Empreendimento Beta |
| --- | --- |
| 1. Corretor 1,5%; 2. Supervisor 0,4%; 3. Gerente 0,20% | 1. Imobiliária 2%; 2. Supervisor 0,5%; 3. Gerente 0,25% |

**Ordem de Prioridade de busca de modalidade por****Empreendimento**

1. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote, Equipe/Imobiliária
2. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote,
3. Modalidade, Empreendimento, Bloco/Quadra, Equipe/Imobiliária
4. Modalidade, Empreendimento, Bloco/Quadra,
5. Modalidade, Empreendimento, Equipe/Imobiliária
6. Modalidade, Empreendimento
7. Modalidade, Equipe/Imobiliária
8. Modalidade
Equipe/Imobiliária

**Configuração de Modalidade por Equipe/Imobiliária**

**A partir da versão 12.1.2310**

Somente deverá realizar a associação de modalidades com equipes/imobiliárias quando deseja pagar comissão com taxas diferentes entre a empresa e a imobiliária parceira, ou até mesmo com equipes diferentes.

**Exemplo:**

Tenho uma empresa que deseja pagar comissão para os seus corretores próprios, gerentes e supervisores  de uma maneira e para os seus parceiros de imobiliária de outra maneira, e até por estado com comissões diferentes, então a configuração da modalidade deve ser por equipe/imobiliária

| Modalidade - Equipe Própria MG | Modalidade - Equipe Imobiliária MG | Modalidade - Equipe Própria SP | Modalidade - Equipe Imobiliária SP |
| --- | --- | --- | --- |
| 1. Corretor 2%; 2. Supervisor 0,5%; 3. Gerente 0,25% | 1. Imobiliária 2%; 2. Supervisor 0,5%; 3. Gerente 0,25% | 1. Corretor 2,5%; 2. Supervisor 0,6%; 3. Gerente 0,3% | 1. Imobiliária 3%; 2. Supervisor 0,6%; 3. Gerente 0,3% |

**Ordem de Prioridade de busca de modalidade por Equipe/Imobiliária**

1. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote, Equipe/Imobiliária
2. Modalidade, Empreendimento, Bloco/Quadra, Apto/Lote,
3. Modalidade, Empreendimento, Bloco/Quadra, Equipe/Imobiliária
4. Modalidade, Empreendimento, Bloco/Quadra,
5. Modalidade, Empreendimento, Equipe/Imobiliária
6. Modalidade, Empreendimento
7. Modalidade, Equipe/Imobiliária
8. Modalidade

Foi criado um parâmetro Geral  em Contrato => comissão => comissão para obrigar o preenchimento da equipe/imobiliária na geração da comissão

Gerando a Comissão:

Neste exemplo , informando um contrato de Venda ( **Data Comissão** ) onde irá pegar a Modalidade que se enquadra em seu cadastro de Prioridade.

Comissão gerada no valor total de 8 Mil Reais , encontra-se Calculada e correta , pois não ultrapassou o valor dos 10 Mil definidos para o valor de Comissão.

* Esses valores dos Itens da Comissão podem ser editados para se enquadrar no valor correto da Comissão.

**Recalculando Comissão:**

Neste exemplo, a Comissão foi gerada no valor de 11 Mil Reais , ultrapassando o valor da Comissão de 10 Mil reais , neste caso será editada um dos item de Comissão para que o valor possa se enquadrar dentro dos 10 Mil.

 Lembrando que o Status fica = Limite de Valor Extrapolado

Após editar o Valor do Item , pode clicar em Calcular no Item.

Calcular no cadastro da Visão de Comissão

Ou Recalcular Comissão.

Passando a ficar Correta a comissão  ( Calculada ).
