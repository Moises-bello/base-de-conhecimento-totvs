---
article_id: 360029174591
category: RH - Definições de Cálculo
content_hash: 90ffe5f189bc0cfd9b33794baa4ec3694211a63fb507919299598ac48c052de0
fetched_at: '2026-06-28T22:43:22.276993+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro tipos de ausência
type: support-article
updated_at: '2026-06-26T17:46:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029174591-RH-Linha-Protheus-GPE-Cadastro-tipos-de-aus%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32798259273751) Tempo aproximado para leitura: 00:01:00 min

**Dúvida**  
Como funciona o cadastro do tipo de ausência?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
O Cadastro de Tipo de Ausências (GPEA430) armazena e controla todas as ausências que poderão ser lançadas na rotina de Ausências (GPEA240), sejam elas utilizadas ou não para os cálculos da Folha de Pagamento.  
  
Na rotina são definidos as parametrizações para o cálculo de afastamento, folha de pagamento, férias, rescisão e provisão, onde é possível configurar a quantidade de dias pago pela empresa, a verba que deverá ser calculada para esse pagamento, informação para pagamento de FGTS, encargos patronais, informações para férias, 13º salario, provisão, eSocial, entre outras configurações.   
  
1. Acesse **Atualizações > Definições Cálculo > Tipo de Ausência**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844571482775)**

2. Clique em **Incluir** e preencha as informações conforme a necessidade

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844627128983)

**Informações Gerais**

* **TP. AUSÊNCIA:** destinado a estabelecer o tipo de Ausência, podendo ser 1 - Afastamento / 2 - Outras Ausências / 3 - Informativo / 4 - Controle de Dias de Direito
* **MOTIVO AFAST:** informe o motivo de afastamento para integração com o **eSocial**

**Informações de Cálculo**

* **DIAS PG EMPR:** Deve ser informado a quantidade de dias que a empresa efetuará o pagamento e desconto do salário do funcionário. Ressaltando que alguns afastamentos como Auxílio Doença (15 dias), Licença Maternidade (120 Dias) e Ausência por Adoção (0 dias) tem suas quantidades de dias pagos pela empresa definidos por legislação, devendo desta forma ser preenchido de acordo.
* **TIPO DE DIA:** definição de os dias do campo anterior devem contados por dias CORRIDOS ou dias ÚTEIS
* **COD. VERBA:** Informar a verba que será feito o pagamento ou desconto referente aos dias pagos/descontados pela empresa.
* **DIAS REINC:** utilizado em caso de reincidência de afastamento pelo mesmo CID, exemplo, para pagamento do auxilio enfermidade, doença, caso funcionário após seu retorno se afaste novamente pelo mesmo motivo dentro de 60 dias, não é devido o pagamento dos 15 dias parte empresa, apenas o saldo restante, caso tenha ficado. Neste caso, informar neste campo o valor de 60 dias.
* **SOBREPOSIÇÃO**: Informe se haverá sopreposição
* **DEPOS. FGTS:** definição se o FGTS deverá ser pago integralmente ou apenas pelos dias Pagos, definido no campo Dias Pg Empr.
* **ENCARG. EMPR.**: mesma definição que o campo anterior.
* **PAG. SAL. FAM.**: para o pagamento do salário família, são 4 opções: 1 - Inicio do Afastamento / 2 - Retorno do Afastamento / 3 - Paga (integralmente durante todo o afastamento) / 4 - Não Paga.
* **D. EESTAB.:** dias de estabilidade do funcionário assim que retorna do afastamento.
* **DES. CON. SIND.**: deve ser indicado se o desconto da contribuição sindical deverá ocorrer, deve ser usado em conjunto com o parâmetro MV\_DTRSIND.
* **N. MES. C. MED.**: informe o número de meses para o cálculo de médias.
* **CAT. CALD. MED**.: selecione as categorias de funcionários que devem ter a média calculada.

**Informações sobre Férias**

* **TIPO AUS. FERI:** neste campos será informado se a quantidade de dias de ausência terá impacto no pagamento das férias, existem 4 opções:

**1 - Perda após 180 dias:** os dias de afastamentos ocorridos durante o período aquisitivo do funcionário serão somados, e ao atingirem 180 dias será iniciando um novo período aquisitivo  
**2 - Suspensão do Período:**os dias afastados deverão ser somados ao final do período aquisitivo do funcionário, para finalização do período aquisitivo e calculo das férias.  
**3 - Perda após 30 dias:** os dias de afastamentos ocorridos durante o período aquisitivo do funcionário serão somados, e ao atingirem 30 dias será iniciando um novo período aquisitivo.   
**4 - Não perde:** o total de dias deste afastamento não será considerado no calculo das férias.

* **DIAS AFA. FER.**: preenchido automaticamente com o mesmo conteúdo do campo **DIAS PG. EMPR.**

**Informações sobre 13º**

* **ABAT. AVOS 13:** se deve ou não considerar o período de afastamento para o abatimento dos avos de direito para o 13º Salário, sendo que a cada 15 dias afastados o funcionário perde 1/12 avos de direito, este campo substitui os Parâmetros **MV\_PDCALAC**e**MV\_PDCADOC**.
* **PROV. 13º**: neste campo deve ser optado se a Provisão do 13º Salário será **CONGELADA OU NÃO** a partir do mês de afastamento, este campo substitui o Parâmetro **MV\_TCONGAF**

**Informações sobre PLR**

* **ABT. AVOS PLR:** se deve ou não considerar o período de afastamento para o abatimento dos avos de direito para o pagamento do PLR, sendo que a cada 15 dias afastados o funcionário perde 1/12 avos de direito, o período para análise será do primeiro até o último dia do Ano Ref. Cálculo do PLR
* **DIAS AFA. PLR**: inserir a quantidade de dias a partir dos quais a situação informada influi no calculo do PLR.

**Obrigações**

* **COD. AUT. SEFIP:**informe o código de movimentação para**SEFIP,** conforme a **Tabela S046** localizada na**Rotina Manutenção de Tabelas - GPEA320.**
* **COD. AU. RAIS:**informe o código de movimentação para a **RAIS**.
* **CD. HOMOLOGNE:**informe o código de movimentação para o**Homolognet**conforme a**Tabela S032**localizada na**Rotina Manutenção de Tabelas - GPEA320.**

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como cadastrar estabilidade após retorno de Ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048518013-RH-Linha-Protheus-GPE-Como-cadastrar-estabilidade-ap%C3%B3s-retorno-de-Aus%C3%AAncia?source=search)  
[RH - Linha Protheus - GPE - Campos no cadastro de Tipos de Ausência desabilitados/bloqueados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406434448023-RH-Linha-Protheus-GPE-Campos-no-cadastro-de-Tipos-de-Aus%C3%AAncia-desabilitados-bloqueados?source=search)  
[RH - Linha Protheus - GPE - Cadastro tipo de ausências configuração do campo Calc. Pr. Adic.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052941593-RH-Linha-Protheus-GPE-Cadastro-tipo-de-aus%C3%AAncias-configura%C3%A7%C3%A3o-do-campo-Calc-Pr-Adic-?source=search)  
[RH - Linha Protheus - GPE - Como deve ser preenchido o novo campo RCM\_PDSUP (Verba Susp.) no cadastro do tipo de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007496002-RH-Linha-Protheus-GPE-Como-deve-ser-preenchido-o-novo-campo-RCM-PDSUP-Verba-Susp-no-cadastro-do-tipo-de-aus%C3%AAncia?source=search)  
[RH - Linha Protheus - GPE - Cálculo de provisão com Tipo de ausência Perda após 180 dias e Congela após 6 meses (por período)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6217068180631-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-provis%C3%A3o-com-Tipo-de-aus%C3%AAncia-Perda-ap%C3%B3s-180-dias-e-Congela-ap%C3%B3s-6-meses-por-per%C3%ADodo-?source=search)
