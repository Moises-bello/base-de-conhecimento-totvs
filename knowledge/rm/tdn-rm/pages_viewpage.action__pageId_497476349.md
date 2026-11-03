---
content_hash: a5ef54c97d9b60fc858d690e963eaaeb696220073517873a2478a6150f93dd77
fetched_at: '2026-06-29T00:10:22.587802+00:00'
page_id: '497476349'
product: rm
source: tdn-rm
title: Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497476349
version: 24
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Grupos de Convênios**
3. **Padrão de Informação**
4. **CNES**
5. **Registro ANS**
6. **Tipo Faturamento**
7. **Fonte Remuneração**
8. **Código Singular**
9. **Geração de movimento financeiro/caixa no ato do registro de atendimento**
10. **Permitir atendimento externo (BPA/APAC) simultâneo à internação no registro de atendimento**
11. **Dados de Faturamento**
12. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Esse documento tem objetivo de apresentar os principais campos do cadastro do convênio utilizado no TOTVS Gestão Hospitalar.

Grupos de Convênios

## **02. GRUPOS DE CONVÊNIOS**

Especifica o grupo em que o convênio será classificado, essencial para diferenciar convênios privados, particulares e do SUS, cada um com regras próprias. A definição correta do grupo garante o correto funcionamento dessas regras no sistema.

Padrão de Informação

## **03. PADRÃO DE INFORMAÇÃO**

Alguns convênios utilizam seus próprios padrões para o Faturamento Eletrônico, o que impacta diretamente os seguintes pontos do sistema:

* + **Registro de atendimento:** devido às informações específicas exigidas por cada padrão informado.
  + **Elaboração de contas:** influenciando validações durante o encerramento das parciais e regras de cálculo de valores.
  + **Faturamento para convênios:** alterando a geração dos arquivos de faturas que serão enviados aos convênios.

Alterações nesse padrão podem impactar os pontos acima, pois determinados campos podem tornar-se visíveis ou obrigatórios, conforme o padrão selecionado. Assim, é fundamental que essas definições estejam corretas para garantir a adequada geração das faturas para o convênio.

CNES

## **04. CNES**

Esse campo deve ser preenchido para atender às legislações que exigem sua presença na geração do arquivo. O número do CNES é composto por sete dígitos: os seis primeiros são sequenciais e o último é um dígito verificador.

Informações

**CNES** é a sigla para **Cadastro Nacional de Estabelecimentos de Saúde.** A gestão desse número é feita pelo sistema do Ministério da Saúde do Brasil que registra e mantém informações sobre todos os estabelecimentos de saúde no país, sejam eles públicos, privados ou filantrópicos.

Registro ANS

## **05. REGISTRO ANS**

Código de registro da operadora junto à ANS (Agência Nacional de Saúde Suplementar), responsável pelo acompanhamento e regulamentação dos planos de saúde no Brasil. Esse campo identifica a operadora responsável pela internação no **arquivo de Exportação para o Ministério da Saúde - Comunicação de Internação Hospitalar (CIH)**. Além disso, esse campo também é utilizado no arquivo XML da TISS (Troca de Informação na Saúde Suplementar), que padroniza a comunicação entre prestadores e operadoras de saúde.

O número de registro da ANS é obrigatório para os convênios de saúde suplementar privados e garante que a operadora esteja devidamente credenciada junto à agência.

Tipo Faturamento

## **06. TIPO FATURAMENTO**

Define o tipo de faturamento que o convênio utiliza:

* + **Fatura**: Utilizado para convênios que realizam o faturamento por meio de documentação impressa ou em arquivo eletrônico.
  + **Nota Fiscal**: Exclusivo para convênios particulares do Prestador Principal.
  + **Sem ônus**: Tipo de convênio próprio do Prestador Principal que não gera cobrança (ônus).

Quando o "**Grupo de Convênios"** selecionado for "**Particular"**, o tipo de faturamento **não** poderá ser configurado como "**Fatura**". Caso essa parametrização seja realizada, o sistema exibirá uma mensagem informativa para alertar o usuário.

Para convênios do tipo Particular, os tipos de faturamento permitidos são "**Nota Fiscal**" ou "**Sem ônus**".

Fonte Remuneração

## **07. FONTE REMUNERAÇÃO**

Indica a origem dos recursos utilizados para financiar a internação. Essa informação é requerida no **arquivo de Exportação para o Ministério da Saúde – Comunicação de Internação Hospitalar e Ambulatorial (CIHA)**.

Esse campo é utilizado exclusivamente na rotina do CIHA e, portanto, não possui impacto no faturamento das contas.

Código Singular

## **08. CÓDIGO SINGULAR**

Para todos os prestadores de serviços de saúde que utilizam o padrão de faturamento Unimed-BH, o preenchimento deste campo é obrigatório para o faturamento das contas.

Importante!

Esse padrão de faturamento foi descontinuado e substituído pelo padrão ANS TISS, que atualmente padroniza a troca de informações entre prestadores e operadoras de planos de saúde.

Geração de movimento financeiro/caixa no ato do registro de atendimento

## **09. GERAÇÃO DE MOVIMENTO FINANCEIRO/CAIXA NO ATO DO REGISTRO DE ATENDIMENTO**

Esse parâmetro realiza as seguintes rotinas:

1. 1. **Recebimento do paciente**  
      A primeira etapa trata do recebimento do paciente, que ocorre somente quando o registro de atendimento é feito pela tela de agendamento. Nesse momento, será criado um registro no financeiro/caixa para que o atendente efetue o recebimento.  
      Ao acessar o **Registro de Atendimento** no **Painel Eletivos**, aparecerá a mensagem: "Atendimento aguardando operação de caixa".
   2. **Criação de uma nova parcial**  
      Com a confirmação do recebimento, a parcial 1 é encerrada automaticamente, e o sistema gera a parcial 2, permitindo a inclusão de novos itens. Caso não haja itens a serem cobrados, a parcial 2 deve ser encerrada normalmente.

Importante!

Esse parâmetro está disponível exclusivamente quando o "**Grupo de Convênios"** selecionado for "**Particular**".

FV Caixa 2.0

Fluxo para alteração do status do agendamento e retirada "Atendimento aguardando operação de caixa".  
Configurar [fórmula visual](https://tdn.totvs.com/display/LRM/Importar+FV+caixa+2.0#ImportarFV-1906526480) para caixa 2.0

Permitir Atendimento Externo (BPA/APAC) simultâneo à Internação (AIH).

## **10.** **PERMITIR ATENDIMENTO EXTERNO (BPA/APAC) SIMULTÂNEO À INTERNAÇÃO NO REGISTRO DE ATENDIMENTO**

Esse parâmetro realiza as seguintes rotinas:

1. 1. **Permitir que seja criado atendimentos externos no registro de atendimento para que possa ser gerada faturas de diferentes atendimentos.**

Importante!

Esse parâmetro está disponível exclusivamente quando o "**Grupo de Convênios"** selecionado for "**SUS**".

Dados de Faturamento

## **11. DADOS DE FATURAMENTO**

Essa tela, acessada como um anexo do cadastro de convênios, tem a função de calcular a data de vencimento de uma fatura com base no dia em que o faturamento foi gerado. Caso nenhuma regra seja definida ou encontrada, a data de vencimento será a data atual.

O cadastro permite configurar o(s) dia(s) de entrega ou geração do faturamento. O sistema utiliza essas configurações para calcular a previsão de recebimento da fatura.

* **Dia de entrega:**

  + **Dia do mês**: Especifica que o dia informado corresponde ao mesmo dia do mês em que o faturamento foi gerado.
  + **Dia útil**: Especifica que o dia informado corresponde ao número de dias úteis do mês.

* **Tipo de entrega:**

  + **Único dia**: A fatura deve ser entregue em um dia específico ou após um número definido de dias úteis.
  + **Intervalo de dias**: A fatura pode ser entregue dentro de um intervalo de dias especificado.
  + **Intervalo de datas**: A fatura pode ser entregue dentro de um intervalo de datas específicas. Geralmente, o convênio fornece um calendário de envio das faturas.

**Antecipar se dia não útil**: Quando a opção “Dia do mês” é selecionada no campo "Dia de entrega" e o dia da entrega cai em um dia não útil, a seleção desta opção permite antecipar a entrega em um dia.

### Regra de Recebimento

Define as condições para o recebimento da fatura.

**Tipo de Regra:**

* + **Dia do mês/Dia útil**: É necessário informar o campo “Previsão de dia de recebimento”, que determina o dia (útil ou não, dependendo do campo Dia de entrega) em que a fatura será paga.
  + **Número de dias após a data de entrega**: O recebimento ocorrerá após a quantidade de dias indicada no campo "Número de dias".
  + **Data específica**: O recebimento será realizado na data específica informada.

**Mês de Controle:**

* + **Mês do faturamento**: O recebimento será realizado no mesmo mês do faturamento.
  + **Próximo mês**: O recebimento será feito no mês seguinte, no dia informado no campo “Previsão de dia de recebimento”.
  + **Meses à frente**: Define que o recebimento ocorrerá na quantidade de meses especificada no campo "Número de meses" e no dia informado em “Previsão de dia de recebimento”.

Tabelas Utilizadas

## **12. TABELAS UTILIZADAS**

* SZCADGERAL
* SZATENDIMENTO
* SZPARCIALATEND
* SZLOGATENDIMENTO
* SZCADGERALINFORFAT
