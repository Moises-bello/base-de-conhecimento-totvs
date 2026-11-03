---
content_hash: 6913c15bac1b4955bb36c482adb1ca99f3cd59d149c4243af95ddeb123337de2
fetched_at: '2026-06-29T00:11:34.018567+00:00'
page_id: '766946895'
product: rm
source: tdn-rm
title: Regras de Cobrança de Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=766946895
version: 14
---

## **01. VISÃO GERAL**

Essa rotina é responsável por realizar o calculo dos exames de **tomografia, ressonância e ultrassom** com a mesma incidência do dia.

Dica

Essa rotina possui duas formas de realizar o processamento dos percentuais de incidência, uma pontualmente por parcial e outra através de um processamento em lote, mais detalhes estão informados no documento abaixo.

## **02.** **CONFIGURAÇÃO DOS PERCENTUAIS**

A configuração dos percentuais de incidência não é obrigatória, ela só deve ocorrer nos cenários onde a negociação com a operadora foram acordados percentuais diferentes das tabelas padrão AMB ou CHPM, caso nenhum percentual seja configurado configurado o sistema irá utilizar os percentuais conforme valores definidos por essas tabelas.

Caso os percentuais forem informados, os mesmos deverão ser configurados na condição contratual, conforme descrito nesse documento mais adiante.

A configuração dos percentuais é realizada a partir da segunda incidência, pois a primeira sempre será de 100% e aplicado para o exame de **maior valor** ou de **maior porte**.

Segue abaixo um resumo dos percentuais definidos no padrão de cada tabela:

**Tabela AMB:**

**Tomografia**

| Incidência | Percentual |
| --- | --- |
| Primeira | 100% |
| Segunda | 70% |
| Terceira e demais | 50% |

**Ressonância**

| Incidência | Percentual |
| --- | --- |
| Primeira | 100% |
| Segunda e demais | 80% |

**Ultrassonografia**

| Incidência | Percentual |
| --- | --- |
| Primeira | 100% |
| Segunda e demais | 50% |

**Tabela CBHPM:**

**Tomografia**

| Incidência | Percentual |
| --- | --- |
| Primeira | 100% |
| Segunda e demais | 70% |

**Ressonância**

| Incidência | Percentual |
| --- | --- |
| Primeira | 100% |
| Segunda e demais | 70% |

**Ultrassonografia**

| Incidência | Percentual |
| --- | --- |
| Primeira | 100% |
| Segunda e demais | 70& |

O sistema irá utilizar o padrão **AMB** quando o campo CBHPM estiver **desmarcado**, e irá utilizar **CBHPM** quando o mesmo estiver **marcado**,

Para cadastrar os percentuais de incidência, acessar a tela de **Condições Contratuais** e informar o valor do percentual da incidência para cada uma das faixas.

A faixa utilizada para cada uma dos grupos de exames, deve ser configurada na tela de **Padrões de Faturamento e Codificações** dentro do seu respectivo grupo de exame.

## **03. PROCESSAMENTO DOS PERCENTUAIS POR PARCIAL**

Para executar as regras dos percentuais por parcial, acessar a tela de **Elaboração de Contas** > **Diagnose e Terapia** e executar o do processo **Regras de Cobrança de Exames**.

Na tela de processamento, serão exibidos os exames da mesma faixa por dia, será exibido seu valor original sem considerar o valor do Filme.

Caso alguma parcial precise ter um percentual diferenciado, é possível alterar os valores do campo Percentual diretamente na grid para que o sistema considere esses novos valores.

Informações

Caso o exame possua **valor de filme somado ao valor do exame**, esse valor **não é considerado para o cálculo da redução**. Assim, o cálculo ocorre da seguinte forma:

**(Valor do exame – Valor do filme) \* Percentual de redução = Valor com redução**

Após a aplicação da redução, **o valor do filme é novamente somado**, resultando em:

**Valor com redução + Valor do filme = Valor unitário final**

**CBHPM:**

O cálculo de **CBHPM**, quando o parâmetro **CBHPM** estiver marcado na tabela de preço utilizada, é realizado considerando a composição do valor do exame pelos componentes **UCO, Custo Operacional (CH), Porte e Filme**.

**UCO \* Custo Operacional (CH) \* Percentual de redução = Valor com redução**

Após a aplicação da redução, **os demais componentes são somados novamente**, resultando em:

**Valor com redução + Valor do filme + Porte = Valor unitário final.**

## **04. PROCESSAMENTO DOS PERCENTUAIS POR LOTE**

Para executar a rotina, vá no menu **Faturamento > Atualização de Preços > Regra de Cobrança de Exames em Lote** e clique em executar para que todas as parciais com status **Elaboração** da coligada corrente, com exceção aos convênios que utilizam os padrões de faturamento SUS e Particular sejam processados.

A rotina irá pesquisar nas parciais dos últimos 90 dias exames que podem ter regras de incidências no mesmo dia, nesse processo os percentuais utilizados serão os configurados no contrato ou caso não estejam configurados, serão utilizados os percentuais das tabelas AMB e CBHPM conforme já explicado anteriormente no inicio desse documento.

**Importante!** Se alguma parcial precisar receber um percentual diferenciado, a mesma deverá deverá ser reprocessada através da rotina de processamento **por parcial** antes do **Encerramento da Parcial**, conforme explicado no tópico anterior.
