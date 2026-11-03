---
content_hash: 598396bdd76fa140aa1fc710caed8994a932eecaf4d8ab0f38545d5ad935c515
fetched_at: '2026-06-29T00:09:52.441603+00:00'
page_id: '439363960'
product: rm
source: tdn-rm
title: Orientações para realizar o pagamento do 13º Salário - eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439363960
version: 81
---

false

**Versões:**

* + Todas as versões vigentes no mercado

O 13º salário é concedido anualmente, em duas parcelas. Porém, é possível realizar o pagamento do adiantamento do 13º salário integral antes do mês de dezembro. Caso o empregador decida pagar o beneficio em duas parcelas, a primeira parcela (adiantamento do 13º salário) deve ser paga ao trabalhador entre os meses de fevereiro e novembro (até o dia 30/11). Já a segunda parcela deve ser paga até o dia 20 de dezembro, considerando o valor da remuneração de dezembro e descontando o adiantamento recebido durante o ano corrente.

Quanto aos encargos, devem ser observadas as seguintes regras de incidência:

* **FGTS** – incide quando é pago qualquer valor referente ao 13º salário, no adiantamento ou  na quitação do 13º salário através da 2ª parcela. O recolhimento é realizado na guia da competência de pagamento.
* **Contribuição Previdenciária** – incide sobre o valor total do 13º salário. O recolhimento é realizado na guia exclusiva de 13º salário em dezembro, quando refere-se a 2ª. parcela. Em caso de rescisão o recolhimento é realizado na guia da competência de pagamento.
* **IRRF** – incide sobre o total do 13º salário. O recolhimento é realizado juntamente com a guia da competência de pagamento.

Em dezembro o empregador deverá gerar e efetuar o pagamento de duas guias de recolhimento de INSS (uma referente a folha mensal de dezembro e outra referente a folha de 13º  Salário).

A empresa pode optar em realizar o pagamento do 13º salário de acordo com os cenários abaixo:

13º Salário - Cenários Pagamento do 13º salário em duas parcelas:

* **Pagamento da 1ª parcela de 13º salário**

Conforme citado anteriormente, a primeira parcela deve ser paga ao trabalhador entre os meses de fevereiro e novembro (até o dia 30/11). Iremos demonstrar a seguir, quais são os passos necessário para realizar o pagamento do 13º salário atendendo a rotina do eSocial:

Partimos do principio de que o usuário já possui o seu ambiente parametrizado com todas as verbas, com os seus respectivos códigos de cálculo e fórmulas. Lembrando que esta parametrização é padrão da folha de pagamento e já era realizada em anos anteriores, a única novidade na parametrização das verbas seria a inclusão das rubricas do eSocial.

Obs.: Para o correto funcionamento dos processos do eSocial relacionados ao 13º, é necessário lançar o pagamento das verbas em um período especifico de 13º.

[Novidades em relação ao 13º salário proporcional aos dias de licença maternidade.](http://tdn.totvs.com/pages/releaseview.action?pageId=440857942)

1. Realize o lançamento da 1ª parcela de 13º salário:

2. Verifique se está lançada no envelope de pagamento do funcionário a verba correspondente a 1ª parcela de 13º salário:

3. Nos meses em que o empregador efetuar o pagamento do adiantamento da 1ª parcela de 13ª salário, será necessário gerar os XMLs dos eventos S-1200 e S-1210 considerando somente o indicativo do período de apuração mensal:

Não é necessário gerar os eventos que correspondem a folha de pagamento com o indicativo de 13º salário (Está informação será enviada somente na competência de Dezembro).

* **Pagamento da 2ª parcela de 13º salário**

A segunda parcela deve ser paga até o dia 20 de dezembro, considerando o valor da remuneração de dezembro e descontando o adiantamento recebido durante o ano corrente.

O pagamento da 2ª parcela de 13º salário também segue o processo padrão da folha de pagamento que já era realizado nos anos anteriores, porém para atender o eSocial foram incluídas novas parametrizações que serão descritas a seguir:

1.Realize o lançamento da 2ª parcela de 13º salário:

2. Verifique se as verbas correspondentes a 2ª parcela de 13º salário estão lançadas no envelope de pagamento do funcionário:

3. No mês de dezembro é necessário gerar dois XMLs do evento S-1200. Um XML será gerado para enviar as verbas da folha de pagamento do mês, informando o indicativo do período de apuração mensal. Já o outro XML será gerado para enviar as verbas relativas ao 13º salário, informando o indicativo do período de apuração de 13º salário.

* Acesse o cadastro do Período de Apuração e realize a inclusão de dois períodos, um" Mensal " e o outro "Anual (13º Salário)":

* Após realizar o cadastro dos Períodos de Apuração, execute o processo de "Gerar XML para Eventos Periódicos" para o período "Mensal". Selecione os eventos S-1200 e S-1210:

* Em sequência execute o processo de "Gerar XML para Eventos Periódicos" para o período "Anual (13º Salário)". Selecione apenas o evento S-1200:

Para visualizar o evento S-1200 que corresponde ao 13º salário é necessário informar o período de apuração Anual (13º salário):

A coluna Indicativo de período de apuração só é visualizada no período Anual (13º salário):

DCTFWEB 13º SALÁRIO (ANUAL): De acordo com o Manual da DCTFWEB, a DCTFWeb 13º Salário, ou Anual, serve para declarar as contribuições previdenciárias incidentes sobre a Gratificação de Natal, instituída pela Lei 4.090/1962. É gerada a partir do envio do eSocial relativo ao 13º Salário. Essa categoria de declaração não recebe informações da EFD-Reinf, como ocorre com a DCTFWeb Geral:

**IMPORTANTE!\***Cabe destacar que os eventos S-1200 e S-1299 referentes ao período de apuração anual devem ser enviados entre os dias **01** e **20** de dezembro.

É importante lembrar que não há período de apuração anual para o evento S-1210, ou seja, no evento de pagamento (S-1210) referente a um período anual, o mês em que é efetuado o pagamento deve ser indicado no campo {perApur} e o prazo para seu envio segue a regra geral, ou seja, deve ser enviado até o dia 07 do mês seguinte ou até o fechamento da folha deste mês, o que ocorrer primeiro. No evento S-1210, quando se tratar de pagamento de folha anual, apenas a indicação do período de referência {perRef} deve ser informada no formado AAAA e não AAAA-MM.

\*Essa informação consta na [Nota Orientativa 2018.10](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-010-2018-adiantamento-integral-13o.pdf/view).

Adiantamento integral do 13º salário antes do mês de dezembro:

De acordo com a [Nota Orientativa 2018.10](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-010-2018-adiantamento-integral-13o.pdf/view) publicada pelo governo, se o empregador efetuar o pagamento integral antes do mês de dezembro, deve pagar o correspondente ao líquido devido, ou seja, valor obtido após a dedução da contribuição previdenciária e, quando for o caso, da retenção do imposto de renda.

Segue abaixo os cenários com os cálculos que podem ser aplicados no adiantamento integral do 13º Salário:

**Cenário 1:**

No eSocial, o empregador deve informar o adiantamento ***(correspondente ao valor líquido)*** no evento S-1200 referente a remuneração do mês em que esse adiantamento foi incluído e, em dezembro, deve enviar o evento S-1200 referente a competência anual com o valor do 13º salário devido e o valor dos descontos do adiantamento, de contribuição previdenciária e de retenção de imposto de renda.

Na competência em que o valor do adiantamento for declarado haverá a incidência do FGTS (nesse caso calculado sobre o valor do adiantamento) e na folha anual haverá a incidência da contribuição previdenciária e de imposto de renda, calculados sobre o valor total e, ainda, a do FGTS, calculado sobre a diferença entre o valor total e o adiantamento.

**Exemplo:**

**Salario do empregado:** R$ 1.000,00

**Verba lançada no mês do Adiantamento:**

* R$ 920,00 (Provento/ Incide em FGTS)

**OBS¹:** O empregador lança o evento de adiantamento integral para o funcionário considerando apenas o valor liquido a receber.

**Verbas lançadas no mês de Dezembro:**

No período de apuração anual, no mês de dezembro, o empregador deve lançar como vencimento o valor total do 13º devido (R$ 1.000,00) e como descontos: o valor do adiantamento do 13º pago em novembro (R$ 920,00) e o valor de contribuição previdenciária (R$ 80,00). A folha anual, portanto, ficaria com valor líquido zerado.

* 2ª Parcela de 13º - R$ 1.000,00 (Provento/ Incide em INSS,IRRF e FGTS)
* Desconto de Adiantamento do 13º - R$ 920,00 (Desconto/ Incide em Estorno de FGTS )
* Desconto de INSS - R$80,00 (Desconto)

No exemplo acima, a base de cálculo do FGTS que incidente sobre o 13º salário na competência do adiantamento será R$ 920,00 e o valor na competência anual será R$ 80,00.

**OBS²**: O desconto de IRRF será lançado automaticamente se o salário do funcionário entrar na faixa de desconto do imposto de renda.

**Cenário 2:**

Caso o empregador prefira recolher o FGTS integralmente no mês que o 13º salário foi adiantado, deve lançar o valor total ***(bruto)*** como rubrica de adiantamento de 13º com incidência fundiária *(FGTS)* e o desconto da provisão de contribuição previdenciária sem incidência

**Exemplo:**

**Salario do empregado:** R$ 1.000,00

**Verba lançada no mês do Adiantamento:**

* Adiantamento integral do 13º - R$ 1.000,00 (Provento/ Incide em FGTS)
* Provisão de INSS de 13º - R$80,00 (Desconto)

**OBS¹:** O empregador lança o evento de adiantamento integral para o funcionário considerando o valor bruto do 13º e lança os eventos de desconto da provisão do INSS/IRRF.

**Verbas lançadas no mês de Dezembro:**

* 2ª Parcela de 13º - R$ 1.000,00 (Provento/ Incide em INSS,IRRF e FGTS)
* Desconto de Adiantamento do 13º - R$ 1.000,00 (Desconto/ Incide em Estorno de FGTS )
* Desconto de INSS - R$80,00 (Desconto)

**OBS²**: O desconto de IRRF será lançado automaticamente se o salário do funcionário entrar na faixa de desconto do imposto de renda.

Para maiores informações em relação a criação do evento de adiantamento de 13º Salário e das fórmulas [clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=207357578).

**IMPORTANTE!**Cabe destacar que os eventos **S-1200** e **S-1299** referentes ao **período de apuração anual** (AAAA) devem ser enviados entre os dias **01** e **20** de dezembro.

É importante lembrar que não há período de apuração anual para o evento S-1210. As informações de pagamento são geradas no evento S-1210 junto com os dados da Folha de Pagamento. Falando de 13º, como o pagamento da 2ª parcela é até 20/12, os dados serão gerados no S-1210 de período de apuração 12/2023, que deve ser enviado até o dia 15/01.

\*Essa informação consta na [Nota Orientativa 2018.10](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-010-2018-adiantamento-integral-13o.pdf/view).

3Pagamento Vínculos Empregatícios com outras empresas (Terceiros)

Foi implementado no cadastro de Vínculos Empregatícios com outras empresas (terceiros) o campo "Anual (13º Salario)".

Este campo permite que o sistema leve as informações da remuneração do 13º salário para o evento S-1200 no período de apuração Anual (13º salario).

 Desta forma serão geradas as informações do 13º salário múltiplos vínculos no período de apuração Anual.

**Fontes para consultar maiores informações sobre o 13º:** [Perguntas Frequentes - Site Oficial do eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

[Nota Orientativa 2018.10](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-010-2018-adiantamento-integral-13o.pdf/view)

[DCTFWEB - Espaço Legislação](https://espacolegislacao.totvs.com/dctfweb/)
