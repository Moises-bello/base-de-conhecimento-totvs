---
content_hash: 6d35ba51f24d124f5d0c52fe4dd24fe287f303e058ab3401d0d46bb26ffca58c
fetched_at: '2026-06-29T00:10:21.692373+00:00'
page_id: '492700190'
product: rm
source: tdn-rm
title: Código de Cálculo 417- Base Tributada de INSS Autônomos Múltiplos Vínculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=492700190
version: 16
---

Evento tipo base, valor.  
Este evento é calculado quando o parâmetro "**Calcula INSS conforme eSocial**' estiver marcado em: Configurações | Parâmetros | Parametrizador | Folha de Pagamento | Folha Normal | Geral.

A criação deste código de calculo foi necessária para atender o manual do eSocial na geração do evento **S-1200-Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social**.

Este código de cálculo é lançado na movimentação do autônomo que utiliza o código de cálculo **46-Honorário**.  
   
**Exemplo 1**

 Coligada 1- Chapa 001 -  Funcionário Autônomo -  Base de INSS   1.000,00

 Coligada 2- Chapa 002 -  Funcionário Autônomo -  Base de INSS   1.500,00

* Quando lança o movimento para a chapa 001, o evento calculado com CC 85 (INSS Calculado pelo Usuário) será calculado considerando o CC46  até que se realize o recalculo após o lançamento da movimentação na coligada 2.
* Quando lança o movimento para a chapa 002, é lançado o evento com CC417 (Base tributada de INSS autônomos Múltiplos vínculos) no valor de 1500 e o INSS será calculado conforme formula informada no evento com CC85.

**Exemplo 2**

Coligada 1-  Chapa 001 -    Funcionário Normal      -   Base de INSS  1.000,00

Coligada 2-  Chapa 002 -    Funcionário Autônomo -   Base de INSS  1.500,00

Tabela de INSS:

 Até 2000,00 - 8%  
 Até 3500,00 - 9%  
 Até 5000,00 - 11%  
   
O cálculo ocorrerá da seguinte forma:

* Quando lança o movimento para a chapa 001 é calculado o CC 3 com o valor de (80,00) considerando a base de INSS.
* Quando lança o movimento para a chapa 002, é lançado o evento com CC417 (Base tributada de INSS autônomos Múltiplos vínculos) no valor de 1500 e o INSS será calculado conforme fórmula informada no evento com CC85.

**Observação:**

O valor do CC417 irá compor a base total tributada para verificar o teto, mas não será considerado para definir a alíquota utilizada no desconto do INSS.

**Atenção 1:**

Após lançar o movimento mensal de todas as coligadas, que possuem múltiplos vínculos, é necessário realizar um recálculo para ajustar o cálculo do INSS todos os vínculos da pessoa. A consulta dos recálculos pendentes pode ser visualizada em: Folha Mensal | Consulta | Múltiplos Vínculos que Necessitam de Recálculo 

**Atenção 2:**

As formulas utilizadas para cálculo do evento com CC85 (INSS Calculado pelo Usuário) devem ser ajustadas para passar a considerar o valor do evento com CC417(Base tributada de INSS autônomos Múltiplos vínculos).

**Exemplo:**

Formula antes da alteração:

DECL MAXIMO;  
SETVAR(MAXIMO, TABCALCULO ('LIMITESUPERIOR','INSS',MTDATA (1, INCMES(MES,1), INCANO(MES,ANO,1)),3)\*0.11 );  
ENTAO MIN(MAXIMO,LI('xxxx')\*0.11)

Formula após a alteração:

 DECL MAXIMO;  
SETVAR(MAXIMO, TABCALCULO ('LIMITESUPERIOR','INSS',MTDATA (1, INCMES(MES,1), INCANO(MES,ANO,1)),3)\*0.11 );  
SE LI('yyyy')=0   
ENTAO MIN(MAXIMO,LI('xxxx')\*0.11)   
SENAO MIN(MAXIMO,LI(' yyyy')\*0.11)  
FIMSE

Onde:

XXXX= CC46

YYYY= CC417

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
