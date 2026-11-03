---
article_id: 11899851782423
category: RH - Provisão
content_hash: 00a48191791629852841ae7051d5e032764c3838e36dd60b7aa1fa763dac6cd7
fetched_at: '2026-06-28T22:43:55.869317+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Conceito do Parâmetro MV_CSALINC
type: support-article
updated_at: '2025-06-13T21:33:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11899851782423-RH-Linha-Protheus-GPE-Conceito-do-Par%C3%A2metro-MV-CSALINC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26321569448471) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Conceito do parâmetro MV\_CSALINC.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
  
**Solução**O parâmetro MV\_CSALINC foi criado com dois objetivos:

1. Diminuir o tempo de processamento do cálculo, pois ocorre busca do salário mensal gerado no cálculo de folha na verba vinculada ao ID de cálculo 0318. Dessa forma, não ocorre a execução do roteiro INC para apuração do salário e adicionais sobre o salário;
2. Permitir cálculo retroativo de provisão com base no salário da época, ao invés de considerar o salário atual do cadastro.

Para ativar o parâmetro, basta preenchê-lo com a competência inicial em que será utilizado esse conceito. Dessa forma, todos os cálculos de provisão a partir dessa competência irão utilizar o conceito explicado nessa página.

No entanto, é necessário observar que para o correto funcionamento é necessário que tenha sido cadastrado verbas para os IDs de cálculo abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11899872636055)

**Observação:**

Tal configuração é necessária porque o sistema irá gravar o valor integral correspondente a cada adicional sobre salário nas verbas vinculadas aos IDs acima ao realizar o cálculo da folha, que posteriormente será utilizado no cálculo da provisão.

Dessa forma, se for informado uma competência no parâmetro MV\_CSALINC que não possuía o cadastro das verbas acima, o cálculo da provisão ficará incorreto pois não irá encontrar o valor dos adicionais.  
  
Ao iniciar o cálculo da provisão, o sistema irá buscar inicialmente pela verba de ID 0318 - Salário do Mês no cálculo da folha. Como na verba vinculada a esse ID pode haver verbas incorporadas ao salário mensal do funcionário, será efetuado uma dedução desses valores incorporados para considerar apenas o salário base do funcionário para a gravação no campo RT\_SALARIO.

Os valores dos adicionais sobre salário serão identificados através do valor gravado nas verbas vinculadas aos IDs de cálculo da tabela acima, e serão considerados no cálculo dos adicionais de provisão de férias e de 13º salário.

**Exemplos:**  
  
Em 07/2021, há funcionário com salário mensal de R$ 3.000,00 que recebe periculosidade com configuração para incorporar ao salário. Dessa forma, os seguintes valores foram gravados resumidamente no recibo do funcionário:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11899981039255)  
  
Cálculo da provisão de Julho irá ter o resultado abaixo:  
  
**MV\_CSALINC em branco:**Salário mensal: R$ 3.000,00

Periculosidade: R$ 900,00

**MV\_CSALINC preenchido com 202107:**  
Salário mensal: R$ 3.000,00

Periculosidade: R$ 900,00  
  
**Observação:**Nessa situação, não há diferença no cálculo.

Em 08/2021, o funcionário teve reajuste salarial, passando ao salário mensal de R$ 4.000,00. Caso a empresa decida reprocessar as provisões ou ainda não tenha ocorrido o cálculo de Julho, o cálculo terá o resultado abaixo:

**MV\_CSALINC em branco:**

Salário mensal: R$ 4.000,00

Periculosidade: R$ 1.200,00

**MV\_CSALINC preenchido com 202107:**

Salário mensal: R$ 3.000,00

Periculosidade: R$ 900,00

**Observação:**

Houve diferença no cálculo, pois quando o parâmetro MV\_CSALINC não está preenchido, é utilizado o salário atual do cadastro e não o que foi calculado na época.

**Saiba Mais:**  
[MV\_CSALINC](https://tdn.totvs.com/pages/viewpage.action?pageId=632518547)   
[Página Centralizadora da Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
