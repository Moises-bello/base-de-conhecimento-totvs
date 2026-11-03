---
article_id: 360007572691
category: Ativo Fixo - Ampliação
content_hash: f2ae1392caf31e04ebe78f3fe28864bed1726b6c0fd22d731681f3903a823598
fetched_at: '2026-06-28T22:41:58.162184+00:00'
product: protheus
section_id: 1500001535321
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA155 AMPLIAÇÃO DO
  BEM COM OU SEM AUMENTO DA VIDA UTIL
type: support-article
updated_at: '2024-09-05T13:50:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007572691-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA155-AMPLIA%C3%87%C3%83O-DO-BEM-COM-OU-SEM-AUMENTO-DA-VIDA-UTIL
---

**Dúvida**

**Ampliação do bem com ou sem aumento de vida útil.**

**Ambiente**PROTHEUS – Ativo fixo – A partir da versão 12  
  
  
**Solução**

A rotina Ampliação (ATFA155) possibilita a ampliação do valor do bem, com ou sem impacto na vida útil. Desta maneira é realizada a normalização da tabela de Saldos e Dados Contábeis do ativo com a criação do tipo de Ativo 11 – Ampliação.No conceito de Ampliação pode-se entender que é possível alterar o valor e ampliar a vida útil em pelo menos um ano, podendo ser lançado como despesa e amortizado integralmente no exercício vigente. No conceito de Incorporação é a adição de bens na estrutura já existente com as mesmas características, porém utilizando um novo código de item sequencial no mesmo código base. Para esta melhoria é necessário ter cadastrado um Ativo (ATFA012) e Lançamentos Padrões (CTBA080). Na ficha já existente do tipo 821 – Ampliação de valor do bem e 822 – Estorno da Ampliação do valor do bem. Para ampliação por incorporação os tipos são 801 – Inclusão de ficha de ativo tipo 01 e 805 – Estorno de ficha de ativo tipo 01.ATENÇÃO!A atual rotina de Ampliação, ATFA150, ainda existe, todavia será disponibilizada uma nova FNC e boletim quando a mesma for descontinuada. As funcionalidades da rotina de ampliação somente são executadas no mês posterior a ultima data de cálculo de depreciação, sendo definida no parâmetro MV\_ULTDEPR, no formato AAAAMMDD.O parâmetro MV\_CALCDEP define os valores para aumento de vida útil, podendo ser: Em meses = 0; Em Anos = 1.

Procedimentos para utilização

**Ação**

Vida Útil: Determina que a única ação tomada pelo sistema seja de aumento de vida útil do item tipo 01. Para este caso os campos Método e Tipo de Vida Útil e a grid Dados do Bem: Incorporacao são desabilitados para edição e seus valores ignorados.

Valor: Determina se as ações executadas do sistema são de Ampliação ou de incorporação. Para este caso deve ser informado em Dados do Bem a opção Incorporação o valor na moeda 1 (Val Orig M1).

Ambos: Ambas as ações são executadas pelo sistema.

**Método**

Mesmo Bem (Tipo 11): Ampliação como item, da ficha de ativo já existente. É criado um item do tipo 11 – Ampliação.

Novo Bem (Incorporação): Inclui uma nova ficha de ativo tipo 01 com o mesmo código base e item seqüencial. É vinculada por meio dos campos N1\_BASESUP e N1\_ITEMSUP que indicam todos os bens que compõe a mesma estrutura.

Mesmo Bem (Tipo 01): Valor atribuído ao campo método automaticamente e usado apenas quando o campo Ação receber o valor 1= Vida Util e neste caso o campo sera desabilitado para edição.

**Tipo de vida útil**

Vinculada: Usa-se como base a taxa de depreciação anual do item tipo 01. Com as movimentações de cálculo de depreciação são geradas taxas de depreciação anual, em que a vida útil do bem termina junto com o item tipo 01. Esta opção calcula a taxa de depreciação do novo item 11 ou da nova incorporação com base na vida útil do bem original.

Própria: Ao escolher essa opção, deve-se informar em Dados do Bem a opção Incorporação, a taxa de depreciação anual estar na moeda 1 e a moeda de calculo do ativo. Esta taxa é usada para o novo item ou incorporação.

**Vida Útil**

Este campo só é considerado caso o campo Ação esteja preenchido com o valor de Vida Útil ou Ambos. O valor a ser informado nesse campo deve ser de ao menos um período (12 meses ou 1 ano de acordo com o parametro MV\_CALCDEP) a mais que o valor da Vida Útil Atual (Campo Somente Visualização).

**Exemplo:**

* Vida Util Atual 60 Meses
* Valor a ser informado em Vida Util 72 Meses
* Vida Util Atual 3 Anos
* Valor a ser informado em Vida Util 4 Anos

Link com a documentação  da Ampliação

<https://tdn.totvs.com/pages/viewpage.action?pageId=527393818>

 [ATFA155 - Rotina de Ampliação de Bens](https://tdn.totvs.com/pages/releaseview.action?pageId=527393818)

Impossibilidade de ampliação do Tipo 10(Gerencial)

<http://tdn.totvs.com/pages/releaseview.action?pageId=286513879>

 Veja Também:

* Tipo    10 ou 12 é gerado pela rotina ATFA380  conforme   descrito :[MP - SIGAATF - ATFA038 Ganho ou perda referente a avaliação de ativo com base no valor justo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014264292-MP-SIGAATF-ATFA038-Ganho-ou-perda-referente-a-avalia%C3%A7%C3%A3o-de-ativo-com-base-no-valor-justo)

* Tipo 11 é gerado através da rotina ATFA155 Conforme descrito [Ativo 11 – Ampliação](https://tdn.totvs.com/pages/releaseview.action?pageId=527393818)[(veja mais)](https://tdn.totvs.com/pages/releaseview.action?pageId=527393536)

* Tipo 01 é gerado através da rotina ATFA150 Conforme descrito :[Ativo 01 - Ampliação](https://tdn.totvs.com/pages/viewpage.action?pageId=640681088)

Saiba mais :

[ATFA380 Valor recuperável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014264292-Cross-Segmento-Backoffice-Linha-Protheus-ATFA012-ATFA380-Valor-recuper%C3%A1vel?source=search)

[ATFA155/ ATFA150 - Contabilização rotinas de ampliação lançamento padrão 821](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037713794-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA155-ATFA150-Contabiliza%C3%A7%C3%A3o-rotinas-de-amplia%C3%A7%C3%A3o-lan%C3%A7amento-padr%C3%A3o-821?source=search)

[ATFA155 : AO REALIZAR A AMPLIAÇÃO TAXA DE DEPRECIAÇÃO NÃO É REGISTRADA CORRETAMENTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023372311-MP-SIGAATF-ATFA155-AO-REALIZAR-A-AMPLIA%C3%87%C3%83O-TAXA-DE-DEPRECIA%C3%87%C3%83O-N%C3%83O-%C3%89-REGISTRADA-CORRETAMENTE-?source=search)

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=6067597>

<https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa150_ampliacao.htm>

relatório : <https://tdn.totvs.com/pages/releaseview.action?pageId=312159937>
