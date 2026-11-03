---
content_hash: 18cd068d514b518f5fbea16a7b8a4863c07c0fbfa4b6e70036040749c5b5581f
fetched_at: '2026-06-29T00:10:26.066133+00:00'
page_id: '510508458'
product: rm
source: tdn-rm
title: Código de cálculo 418 - Base de INSS Autônomo outro Emprego
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=510508458
version: 7
---

Evento do tipo base, valor.

Este evento deverá ser utilizado quando o parâmetro **Calcula INSS conforme eSocial** existente em **Configurações | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral**estiver marcado.

Deverá ser lançado manualmente no envelope do autônomo/funcionário para que o sistema considere o valor da base tributada de maneira que não ultrapasse o teto no cálculo do INSS, quando o mesmo possuir outro vinculo empregatício que não esteja na base de dados do Labore.

Lembrando que, o sistema considera este valor apenas para a tributação da base de cálculo de INSS, não utiliza para definir a alíquota de desconto do INSS, conforme explica o manual do eSocial: "A observância do limite máximo do salário de contribuição, com relação à retenção da contribuição previdenciária do segurado, também se impõe aos serviços prestados por segurados cooperados a vários tomadores.".

Exemplo MOS:

**Atenção:**

A criação deste código de calculo foi necessária para atender o manual do eSocial na geração do S-1200.

| **Tabela de INSS:** | |
| --- | --- |
| Até 2000,00 | 8% |
| Até 3500,00 | 9% |
| Até 5000,00 | 11% |

   
**Exemplo 1**

 Coligada 1- Chapa 001 -  Funcionário Autônomo -  Base de INSS   1.000,00

 Coligada 2- Chapa 002 -  Funcionário Autônomo -  Base de INSS   1.500,00 // Cadastro de outro vinculo em **anexo | Folha de pagamento | Vinculo****Empregatícios****com outras empresas terceiros**  categoria 701-  Salário de contribuição de 3.000,00.

O cálculo ocorrerá da seguinte forma:

* Quando lança o movimento para a chapa 001, o evento calculado com CC 85 (INSS Calculado pelo Usuário) será calculado considerando o CC46  até que se realize o recalculo após o lançamento da movimentação na coligada 2.
* Quando lança o movimento para a chapa 002, deverá ser digitado o CC418 com o valor de 3.000,00, após o recalculo, é lançado o evento com [CC417](http://tdn.totvs.com/pages/viewpage.action?pageId=492700190) (Base tributada de INSS autônomos Múltiplos vínculos) no valor de 1.000,00 (valor restante para chegar ao teto) e o INSS será calculado conforme formula informada no evento com CC85.

**Exemplo 2**

Coligada 1-  Chapa 001 -    Funcionário Normal      -   Base de INSS  1.000,00

Coligada 2-  Chapa 002 -    Funcionário Autônomo -   Base de INSS  1.500,00 // Cadastro de outro vinculo em **anexo | Folha de pagamento | Vinculo****Empregatícios****com outras empresas terceiros**  categoria 701-  Salário de contribuição de 3.000,00.

 O cálculo ocorrerá da seguinte forma:

* Quando lança o movimento para a chapa 001 é calculado o CC 3 com o valor de (80,00) considerando a base de INSS.
* Quando lança o movimento para a chapa 002, deverá ser digitado o CC418 com o valor de 3.000,00, após o recalculo, é lançado o evento com [CC417](http://tdn.totvs.com/pages/viewpage.action?pageId=492700190) (Base tributada de INSS autônomos Múltiplos vínculos) no valor de 1.000,00 (valor restante para chegar ao teto) e o INSS será calculado conforme fórmula informada no evento com CC85.

**Observação:**

O valor do CC418 irá compor a base total tributada para verificar o teto, mas não será considerado para definir a alíquota utilizada no desconto do INSS.

**Atenção 1:**

Após lançar o movimento mensal de todas as coligadas, que possuem múltiplos vínculos, é necessário realizar um recálculo para ajustar o cálculo do INSS todos os vínculos da pessoa. A consulta dos recálculos pendentes pode ser visualizada em:**Folha Mensal | Consulta | Múltiplos Vínculos que Necessitam de Recálculo**

**Observação**

Quando é informada a Base de INSS do externo, utilizando os CC's 72 ou 181 para CLT ou o CC 418 para autônomo, o sistema calcula o desconto de INSS do externo, e não considera o valor informado pelo usuário no CC 29.   
Para utilizar o desconto do INSS do externo como referência do cálculo o correto é informar somente o CC 29.   
O CC 29 pode ser utilizado para informar o desconto do INSS de qualquer vinculo externo, seja CLT ou autônomo.  
Somente no caso de informar a Base de INSS do externo, onde o sistema que irá calcular do valor descontado, que é necessário diferenciar o número do código de cálculo, CC 418 para autônomo e CC's 72 e 181 para CLT.

---

Códigos de Cálculo
