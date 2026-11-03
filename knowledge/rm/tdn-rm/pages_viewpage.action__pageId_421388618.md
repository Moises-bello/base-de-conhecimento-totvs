---
content_hash: c7833112a3b82942079ecccb67da81eb5404f00191b7b3a4a37481f0c713007d
fetched_at: '2026-06-29T00:09:17.686950+00:00'
page_id: '421388618'
product: rm
source: tdn-rm
title: Cadastro da Aplicação Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388618
version: 5
---

**Pasta Identificação**

Referência

O número inicial de referência que aparece na tela da inclusão é 0. Porém, ao gravar a aplicação, esse número será atualizado para o valor posterior ao da última aplicação.

Ativo

Mesmo quando um tipo de aplicação financeira estiver "inativo", é possível realizar movimentações. O objetivo desta opção é que se possam separar os tipos de aplicações financeiras que estão em andamento dos que já foram encerrados.

Natureza

Informe a natureza da aplicação. Após a realização da primeira aplicação, esse campo ficará indisponível para alteração.

Indexador

Selecione a moeda que será utilizada como indexador do tipo de aplicação. As moedas são cadastradas através do menu Cadastros | Moedas.

Filial/Conta Caixa

Filial e conta caixa onde ocorrerá as movimentações da aplicação.

Código da Receita

Código de receita utilizado para recolhimento de IRRF na fonte. Utilizado pelas rotinas SPED Contribuições e ECF do TOTVS Gestão Fiscal.

Valores

Os valores mínimos para a movimentação da aplicação financeira são fornecidos pela instituição financeira.

Carência do IOF

Dado fornecido pelo Banco, que corresponde ao número de dias em que a aplicação não está sujeita ao IOF sobre os rendimentos. Para aplicações de Poupança este campo não ficará disponível para edição.

Número de Casas Decimais

Informe com quantas casas decimais o tipo de aplicação financeira irá operar. Para aplicações de Poupança, CDC Pós Fixado e CDC Pré-Fixado este campo não ficará disponível para edição.

Taxa de Administração (%)

É uma taxa cobrada pela instituição financeira pela administração do fundo de investimento. O valor diário das cotas dos fundos já é líquido desta taxa, ou seja, esta taxa já está embutida no valor da cota. Para as aplicações dos tipos Fundo Curto Prazo, Fundo Médio Prazo e Poupança este campo não ficará disponível para edição.

Eventos Contábeis

Nesta pasta são selecionados os eventos contábeis que irão realizar a contabilização dos lançamentos gerados no tipo de aplicação financeira. Os Eventos Contábeis são cadastrados através do menu: Cadastros/Eventos Contábeis. Só serão apresentados para seleção, os eventos contábeis que possuírem a opção "Aplicação Financeira" selecionada no campo "Aplicar no" da pasta "Identificação" dos "Itens do Evento Contábil".

Defaults

Nesta pasta você deverá informar a natureza orçamentária financeira que será utilizada como default nos registros equivalentes à aplicação financeira, como por exemplo: valor da aplicação, resgate, etc. Dessa forma, esses registros serão selecionados no Fluxo de Caixa.

Rendimento do último dia do período come-cotas não será considerado no come-cotas posterior

Essa opção tem como objetivo principal alinhar o sistema às práticas adotadas pelas instituições financeiras que optam por desconsiderar o rendimento do último dia do período do come-cotas no cálculo do próximo período de come-cotas . Ela é disponível apenas para aplicações do **tipo fundo** e, por padrão, permanece desmarcada. Quando marcada, ela tem **impacto no valor do imposto de renda no momento de um resgate feito após esse período**, dependendo do rendimento acumulado no dia.  
  
**Exemplo:** Para o cálculo do come-cotas no período de maio, se a opção estiver **desmarcada**, são considerados os meses desde o início de **dezembro até o último dia de maio**. Caso a opção esteja **marcada**, o cálculo considera o período desde o início de **dezembro até o dia anterior ao último dia de maio**.
