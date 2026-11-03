---
content_hash: 779901e0cecfd297f6f214bfb90775864bd174a63e40fed51449d903b64e4018
fetched_at: '2026-06-29T00:05:49.116878+00:00'
page_id: '1037963844'
product: rm
source: tdn-rm
title: MEMO -FAQ - Como ajustar os valores das tags <codIncCP> e <codIncIRRF> para
  Conferência da DIRF no eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1037963844
version: 21
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Como ajustar os valores das tags <codIncCP> e <codIncIRRF> para Conferência da DIRF no eSocial |
| País: | Brasil |
| Ticket: |  |
|  |  |

## **02. VERSÕES**

Versões de mercado.

## **03. SITUAÇÃO/REQUISITO**

Com a substituição definitiva da DIRF e a consolidação do IRRF no eSocial, se faz necessário a correta parametrização do evento **S-1010 (Tabela de Rubricas)**  para evitar divergências nos débitos apurados pelo governo.

**Cenário:** Para sanar inconsistências identificadas na conferência do valor da previdência utilizada na base da DIRF/eSocial,  é necessário realizar a atualização das tags <codIncCP> e <codIncIRRF>. A medida visa garantir a exatidão tributária, assegurando que os valores calculados pelo sistema de folha coincidam com os retornos oficiais do governo.

## **04. SOLUÇÃO**

Com a inclusão do IRRF no eSocial no ano de 2023, foi necessário realizar ajustes nos valores de incidência de INSS (tag <codIncCP>) e IRRF (tag <codIncIRRF>)no evento S-1010.

Essa adequação tem como objetivo evitar qualquer discrepância entre a folha de pagamento e os valores retornados pelo governo.

O produto TOTVS Folha de Pagamento, possui  o processo Comparativo de Incidências de Rubricas  ( eSocial | Outros processos ) que permite identificar com maior facilidade as possíveis diferenças entre as incidências marcadas no cadastro de eventos e o XML gerado - S1010  já com o Status 10- (aceito RET). 

Este pode ser gerado considerando todas as incidências ou individualmente por tipo de incidência (INSS ,IRRF, FGTS e Contribuição Sindical).

Foi desenvolvido um passo a passo detalhado para realização deste processo.

Esta solução será aplicada em duas etapas.

### ETAPA 1  - Como ajustar os valores das tags <codIncCP> e <codIncIRRF>

**PASSO 1**

Acessar o menu eSocial | Outros processos | [Comparativo de Incidências de Rubricas](https://tdn.totvs.com.br/pages/releaseview.action?pageId=519195285).

**PASSO 2**

Executar o relatório marcando a opção "Exibir a comparação do campo<codIncCP> e <codIncIRRF>" e comparar somente as tags <codIncCP> e <codIncIRRF>, conforme demonstrado abaixo:

Após a execução do processo, será listados os registros das rubricas que possuem as tags com divergência ao clicar no botão "**Exibir Visão do Resultado**".

Esta listagem será apresentada conforme a seleção realizada no passo 2.

**PASSO 3**

Através do menu processos,  é possível gerar o gatilho na fila de eventos  para as rubricas que foram apresentadas com divergências.

**PASSO 4**

Acessar a fila de eventos e gerar o XML dos eventos ajustados através do processo citado anteriormente e enviar para o governo.

**PASSO 5**

Para que a atualização seja realizada corretamente,  **será necessário editar os gatilhos** (gerados através do processo) e ajustar o início de validade da verba, para isso, **basta alterar o campo "Competência" dentro do gatilho para o mês/ano desejado e, após isso, executar o processo de gerar o XML  e transmitir ao governo.**

**Exemplo:** Após a execução da rotina Comparativo de Incidências de Rubricas, foram listados registros com inconsistência de tags.

Foi executado o processo "Gera gatilho de rubricas divergentes entre último XML e base"

Os registros dos gatilhos do evento S-1010 foram gerados da Fila de Eventos com o status de "Pendente".

Editando o gatilho, é possível alterar a data de vigência do mês/ano.

### **O que será** **ajustado após o processo**

O XML do evento S-1010 para os códigos de cálculos abaixo sofrerão as seguintes alterações:

**Obs.: Estas alterações de incidências não afeta os valores já calculados no envelope do funcionário, trata-se de uma alteração de incidências das rubricas já enviadas para o governo.**

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
| [131 - I.N.S.S. Férias desc. mês ant.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718225) | 9 | 43 |
| [141 - INSS Férias no mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718223) | 9 | 43 |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | 9 | 42 |
| [159 - INSS de férias outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718222) | 43 | 9 |
| [171 - INSS 13º Sal descontado p/ previd ref lic maternidade](https://tdn.totvs.com/pages/viewpage.action?pageId=452718206) | 9 | 42 |
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
| CÓDIGO DE CÁCULO | **CODINCP ANTES DO AJUSTE** | **CODINCP DEPOIS DO AJUSTE** |
| [142 - INSS Férias próx. mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718227) | 31 | 0 |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | 0 | 32 |

### **ETAPA  2 - Reabertura da Folha:**

Importante

Concluída a transmissão do evento S-1010 para fins de recálculo das bases de cálculo, é imprescindível proceder com a retificação do evento S-1210 em todos os períodos de apuração afetados, a partir da competência de início de vigência indicada no S-1010.

**PASSO 1**

Acesse o menu**eSocial | Gerar XML Eventos Periódicos**

2. Selecione somente o evento S-1298, e a competência que deseja reabrir.

3. Caso já tenha enviado um S-1298 anteriormente no mesmo período de apuração, selecione também o parâmetro **Regerar eventos S-1298 e S-1299**;  
4. Avance o processo para execução;  
5. Acesse a fila de eventos e integre o evento S-1298 com o governo.

**PASSO 2**

Realizar a retificação do evento S-1210 através do menu TOTVS Folha de Pagamento | Esocial |Eventos Periódicos.

Selecione o período de apuração que seja realizada a retificação do evento S-1210.

Marque os registros a serem retificados e execute o processo "Gerar Retificação Arquivo eSocial".

ObservaçõesApós realizar o envio da retificação do evento S-1210, será necessário o envio do S-1299 de fechamento da folha. Recomendamos a conferência dos valores do período de apuração retificado e após a conferência, replicar a retificação dos próximos períodos.

## **05.****ASSUNTOS RELACIONADOS**

* **[S-1010: Adequação da tag <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770940423)**
* **[S-1010: Como ajustar os valores das tags <codIncCP> e <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770941181)**
* **[S-1010 - Adequação das tags <codIncCP> e <codIncIRRF> para os eventos INSS de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=806754750)**
