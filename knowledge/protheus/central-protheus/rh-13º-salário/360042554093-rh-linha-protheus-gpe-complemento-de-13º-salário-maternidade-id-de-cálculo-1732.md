---
article_id: 360042554093
category: RH - 13º salário
content_hash: 9a9e85c0f9cbc153ca6cad0d669ee24d51d540d808b4d31e402c1e676fd61a41
fetched_at: '2026-06-28T22:44:00.738580+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Complemento de 13º Salário Maternidade - Id de
  Cálculo 1732 e 1733
type: support-article
updated_at: '2025-08-13T14:00:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042554093-RH-Linha-Protheus-GPE-Complemento-de-13%C2%BA-Sal%C3%A1rio-Maternidade-Id-de-C%C3%A1lculo-1732-e-1733
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29312989804567) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como funciona o Cálculo de **Complemento de 13º Salário Maternidade**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O cálculo do Complemento de 13º salário em Dezembro não separava os valores de 13º salário referente ao período de licença maternidade, gerando toda a diferença na verba com Id de Cálculo 0028, que gerava inconsistência no arquivo enviado ao eSocial por não conter a Natureza 4051.

Foi realizado um ajuste no cálculo de folha, para que a apuração do complemento de 13º salário na folha de Dezembro separe a diferença do 13º salário de maternidade da diferença do 13º salário.  Para isso, foram criados os Ids de cálculo abaixo:

- ID de cálculo **1732 - Diferença 13o. - Maternidade**: irá conter o valor da diferença do 13 salário relativo a licença maternidade **(Provento)**. Para facilitar o cadastro, copiar a configuração da verba de ID de cálculo **0028**;

- ID de cálculo **1733 - Diferença de 13o. negativa - Maternidade**: irá conter o valor negativo da diferença do 13 salário relativo a licença maternidade **(Desconto)**. Para facilitar o cadastro, copiar as incidências da verba de ID de cálculo **0348;**

Exemplo de Cálculo Atual:

Em dezembro, a diferença do complemento de 13º salário foi de R$ 500,00. No entanto, R$ 100,00 dessa diferença é relativo à maternidade.  
Abaixo segue resumo de como ficou o cálculo do complemento de 13º salário, após o ajuste:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056933493)

**Importante:**

- Os Ids de cálculo são obrigatórios.  
- A separação dos valores é efetuada através da verificação da configuração do campo **RV\_NATUREZ**: a diferença das verbas configuradas com natureza **4051** serão geradas nos novos Ids de cálculo, já a diferença das demais verbas serão geradas nos Ids antigos (0028 ou 0348).  
- Não houve alteração na geração do evento S-1200.

**Saiba Mais**  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>

[RH - Linha Protheus - GPE - Como cadastrar o ID 0028 Diferença 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11222463484439-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-0028-Diferen%C3%A7a-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar o ID 0348 Diferença Negativa 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11222354283927-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-0348-Diferen%C3%A7a-Negativa-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar o ID de Cálculo 1732 - Diferença 13° Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042331013-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-de-C%C3%A1lculo-1732-Diferen%C3%A7a-13-Maternidade-?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar o ID de Cálculo 1733 - Diferença 13º Maternidade Negativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042332013-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-de-C%C3%A1lculo-1733-Diferen%C3%A7a-13%C2%BA-Maternidade-Negativo?source=search)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=528450030#c%C3%A1lculo--526372601>
