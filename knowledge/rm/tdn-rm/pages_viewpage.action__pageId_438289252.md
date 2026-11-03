---
content_hash: 03547968de05f110af636bf5915f45c9bc594d476b9a8c9ff4680151a837912b
fetched_at: '2026-06-29T00:09:52.310117+00:00'
page_id: '438289252'
product: rm
source: tdn-rm
title: Como gerar a retificação da folha de pagamento de meses anteriores?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438289252
version: 65
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplos de utilização**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2306.212
* 12.1.2310.143
* 12.1.2402 e Superiores

## **02. VISÃO GERAL**

Através deste processo é possível realizar a retificação de meses anteriores a folha de pagamento. A retificação será através da digitação de evento(s) que se deseja acrescentar, alterar valor, e/ou quando houver um aumento salarial que não seja por dissidio.

**Observação:**

* O processo de retificação fará o cálculo dos valores de INSS conforme tabela da época. Serão gerados os eventos (S-1200 e S-1210) de retificação no período corrigido.
* Os valores do liquido da diferença calculada serão lançados no período e competência atual para cálculo de IRRF. Os eventos de liquido serão informados normalmente conforme incidência nos eventos  (S-1200 e S-1210) do período atual.
* O cálculo do rateio do centro de custo será feito conforme o rateio atual informado no cadastro do funcionário.
* A distribuição do tomador de serviço deverá ser feita para o período retificado.

Importante

Veja mais informações em: [Retificação da Folha de Pagamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719911)

## **03. EXEMPLOS DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 02.01.05.09 Retificação da Folha de Pagamento

Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/7

Cadastre o período inicial que será apresentado na tela do processo de retificação da folha de pagamento.

Cadastre os eventos com os novos código de calculo criados.

[382 - Estorno Base IRRF Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718661) 

[383 - Líquido Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718720) 

[384 - Pagamento Líquido Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718780)

 

[386 - Pensão Alimentícia Judicial Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718807) 

[392 - Estorno Base IRRF 13 Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465178948) 

[393 - Base IRRF 13 Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465178458)

[402 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Estorno Base IRRF Férias Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179595)

[403 - Base IRRF Férias Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179614)

[404 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Estorno Base IRRF Partic. Lucros Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179628)

[405 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Base IR](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718347)[R](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718347)[F](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718347)[Partic. Lucros Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179659)

[406 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Pensão Alimentícia Férias Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179669)

[407 -](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)[Pensão Alimentícia 13° Salário Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179681)

[408 - Pensão Alimentícia Partic. Lucros Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=465179696)

[424 -Valor Pensão Alimenticia Judicial Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725850)

[425 -Valor Pensão Alimenticia Férias Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725867)

[426 -Valor Pensão Alimenticia 13º Salário Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725880)

[427 - Valor Pensão Alimenticia Partic Lucros Retificação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=519725884)

2Retificação da FolhaRetificação da Folha23-1Informando evento que não existe no movimento origemPasso 1

Envelope original - Não existe lançamento de hora extra

Retificando 10 horas extras que não foram pagas no envelope original

Envelope 10000 com a retificação

Pagamento da retificação no mês atual

Os períodos de lançamento da retificação serão criados sempre na competência a ser retificada e seu cadastro será a partir do numero 10000 ou conforme parametrizado no campo "Período Inicial" existente em: Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/7.

Caso tenha mais de um período a ser retificado, será necessária a realização do processo novamente, assim como a mudança do número de período de lançamento da retificação (Exemplo: 10001).

3-2nformando evento que existe no movimento origemPasso 2

Envelope original - Existe lançamento de Faltas

Retificando 1 dia de falta porque no caso o funcionário deveria ter sido lançado  3 dias de faltas e foram lançados apenas 2 dias de faltas

Envelope 10000 com a retificação

Pagamento da retificação no mês atual

Atenção

Caso o evento já exista no envelope de pagamento, este entrará com o comportamento de "Adicionar" valor.

**Exemplo:** No envelope de pagamento do mês de Abril de 2018 consta o evento "0344 - HORA EXTRA 80%" com a quantidade de 10:00 horas.

Porém será necessário retificar este evento, pois a quantidade de horas corretas são 15:00 horas.

Neste caso deverá digitar quantidade de 05:00 horas, ou seja, somente o complemento, assim após o calculo da retificação a quantidade de horas no evento"0344 - HORA EXTRA 80%" será de 15:00 horas.

Se o processo de retificação da folha for executado por causa de um aumento salarial que não seja por dissidio, o usuário deverá digitar o evento referente ao salário contratual.

3Retificar eventos de afastamento (CC's 145 e 445) pelo processo automático11Parametrização do Cadastro de Eventos

Para retificar os eventos de atestado médico deverá criar eventos de desconto com incidências contrárias às existentes para cada código de cálculo que será retificado e inserir no Cadastro de Eventos no campo “Evento de Diferença de Salário Negativo (eSocial)”, ou seja:

Criar evento desconto para os eventos de CC145 - ATESTADO MÉDICO, CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS, CC2 - DIAS TRABALHADOS E CC1 - HORAS NORMAIS com incidências nos respectivos estornos correspondentes aos eventos originais.

Exemplo com evento de código de cálculo 2 - DIAS TRABALHADOS

2Alterando automaticamente os CC’s 145 e 445Importante:

É imprescindível que tenha feito o cadastro dos eventos conforme explicado no link de Parametrização do Cadastro de Eventos.

Envelope original - Existe lançamento de CC 145 - ATESTADO MÉDICO

Marcado o parâmetro no histórico de afastamento alterando o atestado de  CC 145 - ATESTADO MÉDICO para CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS

Retificando o CC 145 - ATESTADO MÉDICO sendo alterado para CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS

Envelope 10000 com a retificação onde foi lançado o evento com CC92 - Restituição de I.N.S.S.

Pagamento da retificação no mês atual

3Alterando automaticamente os CC’s 445 e 145Importante:

É imprescindível que tenha feito o cadastro dos eventos conforme explicado no link de Parametrização do Cadastro de Eventos.

Envelope original - Existe lançamento de CC 445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS

Desmarcado o parâmetro no histórico de afastamento alterando o atestado de  CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS para CC 145 - ATESTADO MÉDICO

Retificando o CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS sendo alterado para CC 145 - ATESTADO MÉDICO

Envelope 10000 com a retificação onde foi lançado o evento com CC3 - I.N.S.S.

Pagamento da retificação no mês atual onde foi descontado o valor do INSS calculado no período 10000

4Alterando manualmente os CC’s 145 e 445 - Parâmetro Desmarcado

Caso opte por lançar manualmente os valores de atestado para retificação, o usuário deve acessar o processo em Lançamento / Retificação da Folha de Pagamento sem marcar o parâmetro "Retificar eventos de afastamento (CC's 145 e 445) pelo processo automático" e informar os eventos de provento e desconto que serão lançados no "Período lancto. de Retificação".

Caso não informe um desses eventos corretamente o cálculo ficará inconsistente.

**Atenção:**

1. Não deve  marcar o parâmetro  "Retificar eventos de afastamento (CC's 145 e 445) pelo processo automático" e informar os eventos de CC's 145 e 445 para cálculo manual para que um cálculo não interfira no outro.
2. No lançamento manual será acatado os dados digitados no grid mesmo que o funcionário não tenha o afastamento no histórico de afastamentos será lançado o evento que o usuário informar no grid.

Importante:

É imprescindível que tenha feito o cadastro dos eventos conforme explicado no link de Parametrização do Cadastro de Eventos.

Envelope original - Existe lançamento de CC 145 - ATESTADO MÉDICO

Marcado o parâmetro no histórico de afastamento alterando o atestado de  CC 145 - ATESTADO MÉDICO para CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS

Retificando o CC 145 - ATESTADO MÉDICO sendo alterado para CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS 

Atenção:

O evento de desconto deve ter o valor informado no grid caso não seja calculado por fórmula. Se não informar o valor e/ou não existir fórmula no evento, esse evento não será calculado.

Envelope 10000 com a retificação onde foi lançado o evento com CC92 - Restituição de I.N.S.S.

Pagamento da retificação no mês atual

4Cancelamento da RetificaçãoCancelamento da Retificação

Para o cancelamento da retificação da folha é necessário primeiramente cancelar o período atual onde foram lançados os valores dos líquidos da retificação.

Após o cancelamento do período atual, marque o parâmetro "Retificação folha/rescisão",  selecione o período em que foi lançada a retificação da folha de pagamento e informe a competência e o período que se quer cancelar.
