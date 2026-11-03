---
content_hash: 9ec086e5b8697a55d387a88ddd471f9fa4d0bcfb9ea856486efd23a954dd7179
fetched_at: '2026-06-29T00:05:49.137293+00:00'
page_id: '1037965223'
product: rm
source: tdn-rm
title: FAQ - Como ajustar os valores das tags <codIncCP> e <codIncIRRF> para Conferência
  da DIRF no eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1037965223
version: 61
---

false

**A partir das Versões:**

* Releases de mercado

# Objetivo:

---

Em 2023, a TOTVS comunicou a necessidade de realização de um procedimento para ajuste das tags `<codIncCP>` e `<codIncIRRF>` no evento S-1010, em decorrência da adequação ao layout 1.1 do eSocial.

Essa comunicação foi realizada a todos os clientes por meio dos canais **RHInforma, TOTVS News,** **Novidades da Release** e **TDN**. O principal objetivo do procedimento era evitar divergências entre os valores apurados na folha de pagamento e aqueles retornados pelos sistemas do governo.

Entretanto, identificamos que alguns clientes não realizaram o procedimento indicado. Como consequência, esses clientes passaram a identificar, apenas em janeiro de 2026, divergências entre os valores do TOTVS RH Folha de Pagamento e os retornos oficiais do governo.

Ressaltamos que as divergências identificadas em janeiro de 2026 estão diretamente relacionadas à não execução do procedimento divulgado pela TOTVS em 2023.

**Com foco em apoiar nossos clientes, a TOTVS está reforçando essa comunicação e apresentando o passo a passo para a correta tratativa nesse momento.**

IMPORTANTE:

* Este cenário não se aplica a todos clientes, apenas os clientes que não realizaram o procedimento que foi divulgado em 2023 - [RHInforma](https://informa.totvs.com/rh/rm/esocial-leiaute-s-1-1-adequacao-na-incidencia-de-irrf/).
* O cálculo dos valores no ERP foram realizados adequadamente, porém se faz necessária a atualização das incidências destas rubricas (evento S-1010 - Tabela de Rubricas) e também a geração da retificação do evento  S-1210 para sensibilizar a base gerada pelo governo.
* As guias da previdência que foram conferidas e pagas ao longo de 2025 não sofrerão nenhum tipo de alteração ou reflexo por conta deste procedimento, visto que não será realizado nenhum processamento de valores/folha.
* Reforçamos a importância de cada cliente realizar as conferência de valores entre a Folha e Governo, através do [Relatório de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=787841747) e do [Relatório de Conferência IRRF S-5002](https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938).

---

## **EXEMPLO DE UTILIZAÇÃO**

 

11Etapa 1 - Como ajustar os valores das tagsComo ajustar os valores das tags

**PASSO 1**

Acesse o menu eSocial | Fila de Eventos Complementar | Restauração da Fila de Eventos do eSocial e faça a [restauração dos eventos](https://tdn.totvs.com/pages/releaseview.action?pageId=506143967#1-5) da Fila Complementar. Esse processo permitirá o retorno dos eventos S-1010 para a Fila de Eventos padrão.

Deverá ser utilizada nos campos **Competência Inicial** e **Competência Final** a data inicial e final que consta informada no campo **Data do Evento**, dos S-1010 a serem restaurados.

**PASSO 2**

Acessar o menu eSocial | Outros processos | [Comparativo de Incidências de Rubricas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519195285).

**PASSO 3**

Executar o relatório marcando a opção "Exibir a comparação do campo<codIncCP> e <codIncIRRF>" e comparar somente as tags <codIncCP> e <codIncIRRF>, conforme demonstrado abaixo:

Após a execução do processo, serão listados os registros das rubricas que possuem as tags com divergência ao clicar no botão "**Exibir Visão do Resultado**".

Esta listagem será apresentada conforme a seleção realizada no passo 1.

**PASSO 4**

Através do menu processos, é possível gerar o gatilho na fila de eventos para as rubricas que foram apresentadas com divergências.

**PASSO 5**

Acessar a fila de eventos e gerar o XML dos eventos ajustados através do processo citado anteriormente e enviar para o governo.

**PASSO 6**

Para que a atualização seja realizada corretamente, **será necessário editar os gatilhos** (gerados através do processo) e ajustar o início de validade da verba. Para isso **basta alterar o campo "Competência" dentro do gatilho para o mês/ano desejado e, após isso, executar o processo de gerar o XML e transmitir ao governo.**

**Exemplo:**

Após a execução da rotina [Comparativo de Incidências de Rubricas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519195285), foram listados registros com inconsistência de tags.

Foi executado o processo "Gera gatilho de rubricas divergentes entre último XML e base".

Os registros dos gatilhos do evento S-1010 foram gerados da Fila de Eventos com o status de "Pendente".

Editando o gatilho, é possível alterar a data de vigência do mês/ano.

### **O que será** **ajustado após o processo?**

O XML do evento S-1010 para os códigos de cálculos abaixo sofrerá as seguintes alterações:

**Observação: Estas alterações de incidências não afetam os valores já calculados no envelope do funcionário, trata-se de uma alteração de incidências das rubricas já enviadas para o governo.**

|  |  |  |
| --- | --- | --- |
| CÓDIGO DE CÁCULO | **CODINCIRRF ANTES DO AJUSTE** | **CODINCIRRF DEPOIS DO AJUSTE** |
| [3 - I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718215) | 9 | 41 |
| [11 - I.N.S.S. de 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718209) | 9 | 42 |
| [68 - INSS DE DIFERENÇA SALARIAL](https://tdn.totvs.com/pages/viewpage.action?pageId=452718219) | 9 | 41 |
| [82 - I.N.S.S. Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452718205) | 9 | 43 |
| [85 - I.N.S.S. calculado pelo usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718201) | 9 | 41 |
| [92 - Restituição de I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452719626) | 0 | 41 |
| [103 - I.N.S.S. 2ª parc. 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718233) | 9 | 42 |
| [108 - INSS DE DIF SALARIAL DE 13º](https://tdn.totvs.com/pages/viewpage.action?pageId=452718958) | 9 | 42 |
| [110 - INSS DE DIF SALARIAL DE FÉRIAS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718218) | 9 | 43 |
| [141 - INSS Férias no mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718223) | 9 | 43 |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | 9 | 42 |
| [159 - INSS de férias outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718222) | 43 | 9 |
| [171 - INSS 13º Sal descontado p/ previd ref lic maternide](https://tdn.totvs.com/pages/viewpage.action?pageId=452718206) | 9 | 42 |
| [185 - INSS DE FÉRIAS PROXIMO MÊS OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719942) | 43 | 9 |
| [193 - INSS DE FÉRIAS MÊS ANTERIOR OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719896) | 9 | 9 |
| [205 - INSS Descontado RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718220) | 41 | 9 |
| [209 - INSS Descontado RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719900) | 43 | 9 |
| [213 - INSS Descontado RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719681) | 42 | 9 |
| [89 - I.N.S.S. com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718204) | 41 | 9 |
| [90 - I.N.S.S. Férias com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718959) | 43 | 9 |
| [91 - I.N.S.S. 13º c/ alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718212) | 42 | 9 |
| [137 - I.N.S.S. Fér. Próx. mês c/ alíq. normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718228) | 43 | 9 |

|  |  |  |
| --- | --- | --- |
| **CÓDIGO DE CÁLCULO** | **CODINCP ANTES DO AJUSTE** | **CODINCP DEPOIS DO AJUSTE** |
| [142 - INSS Férias próx. mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718227) | 31 | 0 |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | 0 | 32 |

Parametrizador do eSocial, etapa [Configurações Gerais 6/7](https://tdn.totvs.com/pages/viewpage.action?pageId=540899121)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **CAMPOS PARAMETRIZADOR** | **CODINCCP ANTES DO AJUSTE** | **CODINCCP DEPOIS DO AJUSTE** | **CODINCIRRF ANTES DO AJUSTE** | **CODINCIRRF DEPOIS DO AJUSTE** |
| Evento INSS Férias envelope |  | 31 |  | 9 |
| Evento INSS Férias Próximo Mês envelope |  | 00 |  | 9 |
| Evento INSS Antecipação de Férias (Desconto) | 00 | 00 | 9 | 43 |

|  |  |  |
| --- | --- | --- |
| CÓDIGO DE CÁCULO | **CODINCIRRF ANTES DO AJUSTE** | **CODINCIRRF DEPOIS DO AJUSTE** |
| [Código de Cálculo 130 - INSS Férias Próximo Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718229) | 9 | 43 |
| [Código de Cálculo 131 - INSS Férias Desconto Mês Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452718225) | 43 | 9 |
| [Código de Cálculo 349 - INSS Férias no Terceiro Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719459) | 9 | 43 |

2Etapa 2 - Reabertura e Retificação da Folha Reabertura da Folha

**PASSO 1**

IMPORTANTE:

Concluída a transmissão do evento S-1010 para fins de recálculo das bases de cálculo, é imprescindível proceder com a retificação do evento S-1210 em todos os períodos de apuração afetados, a partir da competência de início de vigência indicada no S-1010.

Acesse o menueSocial | Gerar XML Eventos Periódicos.

Selecione somente o evento S-1298 e a competência que deseja reabrir.

Caso já tenha enviado um S-1298 anteriormente no mesmo período de apuração, selecione também o parâmetro **Regerar eventos S-1298 e S-1299**.

Após a execução acesse a fila de eventos e integre o evento S-1298 com o governo.

**PASSO 2**

Realizar a retificação do evento S-1210 através do menu eSocial | Eventos Periódicos.

Selecione o período de apuração que seja realizada a retificação do evento S-1210, e marque os registros a serem retificados e execute o processo "Gerar Retificação Arquivo eSocial".

OBSERVAÇÃO:Após realizar o envio da retificação do evento S-1210, será necessário o envio do evento S-1299 de fechamento da folha. Recomendamos a conferência dos valores do período de apuração retificado e, após a conferência, replicar a retificação dos próximos períodos.

## **Documentações**

* [S-1010 - Adequação da tag <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770940423)
* [S-1010 - Como ajustar os valores das tags <codIncCP> e <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770941181)
* [S-1010 - Adequação das tags <codIncCP> e <codIncIRRF> para os eventos INSS de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=806754750)
* [RHInforma - eSocial Leiaute S-1.1 – Adequação na Incidência de IRRF](https://informa.totvs.com/rh/rm/esocial-leiaute-s-1-1-adequacao-na-incidencia-de-irrf/)
* [Relatório de Conferência de IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=787841747)
* [Relatório de Conferência IRRF S-5002](https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938).
* <https://tdn.totvs.com/display/LRM/Release+notes+dos+patches+12.1.2302+-+por+produto>
