---
content_hash: 64ed7e5ed9d5fbfb073a45157bf7b4247a4e6353b33bdd6742f4169d20e8b704
fetched_at: '2026-06-29T00:10:56.932131+00:00'
page_id: '593726427'
product: rm
source: tdn-rm
title: Condomínio - Fechamento do Condomínio - Taxa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593726427
version: 15
---

### **Taxas no Fechamento Integral**

---

#### **Introdução**

A partir da versão 12.1.32, quando o Gestor do condomínio informa uma cobrança direta envolvendo uma taxa percentual o sistema fará com que essa taxa seja cobrada quando houver o fechamento do condomínio.

#### **Procedimento para utilização**

Para utilizar o cadastro de taxas, devemos primeiramente dar a permissão adequada ao usuário no Perfil, na opção: ***Gestão de imóveis [03]Condomínio [03.03]Fechamento do Condomínio [03.03.05]Taxa***

Deste modo poderemos acessar este cadastro em *Condomínio / Fechamento do Condomínio / Taxa.*

Os campos disponíveis para o cadastro de Taxa são:

* **Item de Cobrança:** Informe o item de cobrança que será utilizado para o fechamento das despesas;
* **Descrição:** Informe a descrição desta taxa;
* **Data Inicial:**A data inicial da cobrança. Esta informação é obrigatória;
* **Data Final:** A data final da cobrança. Esta informação não é obrigatória dado que uma cobrança pode ser recorrente sem data final definida;
* **Aplicada Sobre:** Define se no fechamento o percentual da taxa será aplicado sobre o valor do condomínio ou sobre o valor do contrato de locação;
  + Ao aplicar sobre o valor do condomínio a taxa será aplicada de acordo com o valor total do condomínio dentro do período cadastrado da taxa.
  + Ao aplicar sobre o valor do contrato de locação, a taxa irá incidir sobre o valor do lançamento gerado para este contrato de locação e que esteja dentro da competência do fechamento.
* **Percentual:** Percentual total a ser cobrado como taxa;
* **Ordem de Prioridade:** Deve ser utilizado pelo usuário para informar a prioridade de uma determinada taxa quando ocorre conflito de períodos entre cobranças. Este campo é numérico e o maior valor tem a maior prioridade. Quando não estiver definida a prioridade, ou seja, quando existirem taxas num mesmo período com um mesmo valor para esse campo, o sistema irá sempre usar o primeiro cadastro para realizar os cálculos.
* Associar por:

**Tipos de associações das cobranças**

Também é possível definir se a taxa será associada a empreendimento, unidade ou subunidade. O sistema não permite associação em níveis diferentes. Após a escolha do tipo de associação então o usuário deve definir os empreendimentos/unidades/subunidades.  
No caso de associação de um conjunto de unidades, o sistema permite unidades de diferentes empreendimentos. No caso de associação de um conjunto de subunidades, o sistema permite subunidades de diferentes unidades e empreendimentos.

#### **Exemplo de aplicação no sistema**

Cadastro de três taxas distintas, dentro de uma mesma competência e diferentes prioridades:

Cada taxa está associada à um item de cobrança e cada um destes itens está associado ao valor de integração específico:

Taxa Prioridade 1

* Item de cobrança: Taxa Prioridade 1
* Valor de integração: "Taxa Prioridade 1"
* Prioridade: 1
* Percentual: 5%

Taxa Prioridade 2

* Item de cobrança: Taxa Prioridade 2
* Valor de integração: "Taxa Prioridade 2"
* Prioridade: 2
* Percentual: 10%

Taxa Prioridade 3

* Item de cobrança: Taxa Prioridade 3
* Valor de integração: "Taxa Prioridade 3"
* Prioridade: 3
* Percentual: 2%

Ao realizar o fechamento do condomínio para esta competência, teremos um lançamento que possuirá os valores de integração dos itens de cobrança das taxas e seus respectivos percentuais:

Importante

Quando a taxa é definida para "Contrato de Locação" e o contrato possui vários imóveis associados, o sistema irá realizar o rateio proporcional aos valores dos imóveis associados.

Exemplo do cálculo:

*Percentual: 15,0000%*  
*Prioridade: 0*  
*Item de cobrança: TAXA MANUTENÇÃO PREVENTIVA / Valor de integração: TAXA MANUTENÇÃO PREVENTIVA*  
*Aplicada sobre: Contrato de Locação*

*A taxa irá aplicar sobre o valor: R$17.151,52 (referente a Valor do lançamento financeiro (Ref 11196) do contrato de locação (Cód. 56) O contrato de locação possui 220,0000 m² ocupados para o período do fechamento, e 200,0000 m² são referentes ao imóvel. Valor proporcional: 200,0000 / 220,0000 x R$18.866,67. )*  
*15,0000% de R$17.151,52 = R$2.572,73*

Neste caso o contrato de locação possui dois imóveis, um com 200m² locados e outro com 20m² locados, totalizando 220 m² locados.   
A taxa irá incidir apenas no imóvel de 200m² do contrato.

Sendo assim o sistema faz o cálculo proporcional 200,0000  / 220,0000 x R$18.866,67 )

15,0000% de R$17.151,52 = R$2.572,73 calculados de taxa para o imóvel locado.

#### **Histórico de cálculo**

E possível visualizar o histórico de calculo dos valores das taxas de condomínio, após realizar a geração de lançamentos, basta acessar a opção *Anexos > Histórico de Cálculos,*logo após selecionar uma taxa para ser visualizada será demonstrado, o valor cobrado da taxa por unidade e a Memoria de calculo de como chegou ao resultado do valor retornado.

### Taxas no Fechamento Individualizado (v12.1.2410+)

---

Na versão 12.1.2410 disponibilizamos o cálculo de taxas individual, possibilitando o cálculo de taxa para uma determinada subunidade**.**

O processo de cálculo e cobranças de taxas, quando o condomínio é individualizado, segue as mesmas premissas do processo integral, entretanto, há algumas diferenças no momento do surgimento do cálculo das taxas e de seus percentuais, visto que a cobrança incidirá não sobre o total do condomínio, mas sim sobre a apuração individual.

Neste sentido, o cálculo das taxas será realizado e observado primeiramente na apuração individual, onde, nos registros de apuração serão listados os cálculos e percentuais relacionados a cobrança de taxas em determinada competência ou apuração.

Toda a cobrança é individualizada, ou seja, os percentuais incidirão somente a subunidade em questão e seus processos apurados.

Caso existam dois processos apurados para uma mesma subunidade, as taxas serão cobradas duplamente. Uma vez para o primeiro processo e outra vez para o segundo e assim sucessivamente.

Quando existe mais de uma taxa cadastrada o sistema irá agrupá-las de acordo com o parâmetro do item de cobrança, caso seja "Considerar no valor original" ou caso possuírem os mesmos valores de integração.

#### Cancelamento de apuração com taxas calculadas

Mesmo o cálculo de taxa surgindo após a apuração de determinada competência, não poderemos apenas excluir o cálculo da taxa individualmente. Para cancelar a apuração de uma taxa já calculada, deverá ser cancelado o processo que foi apurado, exemplo:
