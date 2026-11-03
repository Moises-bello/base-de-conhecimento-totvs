---
article_id: 4418030442775
category: Escrita Fiscal - Impostos - ICMS
content_hash: 7d4b5aaca0a4e1eff3a1ee3097f3023c3d625dc59c6d5ef919d5a8f1ad3a2963
fetched_at: '2026-06-28T22:39:24.347442+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cálculo de Diferimento
  de ICMS
type: support-article
updated_at: '2023-07-06T18:58:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS
---

**Dúvida**

Como realizar o cálculo de diferimento de ICMS?

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

## **01. VISÃO GERAL**

O Diferimento se trata do adiamento da responsabilidade tributária para outro contribuinte/sujeito passivo que estará em outra etapa posterior a circulação da mercadoria, e que por sua vez será responsável pelo recolhimento.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para utilização do Diferimento de ICMS no Protheus deve se realizar as configurações abaixo:

Tabela **SF4 – Tipos de Entrada e Saída**

| **Campo** | F4\_ICMSDIF |
| --- | --- |
| **Tipo** | Caracter |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | ICM Diferido |
| **Descrição** | Diferimento de ICMS |
| **Opções** | 1=Diferido;2=Nao Diferido;3=Diferimento de Redução;4=Diferimento Incentivo;5=Diferimento com ST;6=Deduz NF e Duplicata;7=Ded. ICMS BC. Composta |
| **Valid** | Pertence("1234567") |
| **Inic.Padrão** | "2" |
| **Help** | Informar se nesta operação o ICMS deve ser tratado como diferido. As opções validas são:  1-O ICMS é calculado e diferido.  2=Não há calculo do ICMS diferido.  3=O ICMS é calculo e reduzido.  4=O ICMS é calculado, reduzido do ICMS a recolher e somado ao total do título e da nota fiscal (Incentivo Fiscal).  5=Diferimento com ST Diferimento do ICMS é calculado mas não é reduzido do ICMS. Deve ser utilizado exceção fiscal para reduzir alíquota do ICMS Próprio conforme percentual de diferimento. Este tratamento é utilizado quando nota possuir ICMS com diferido e ICMS ST sem diferimento.  6=Deduz NF e Duplicata;  7=Ded. ICMS BC. Composta |

| **Campo** | F4\_PICMDIF |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 6 |
| **Decimal** | 2 |
| **Formato** | @E 999.99 |
| **Título** | [Perc.do](http://perc.do/) ICMS Diferido |
| **Descrição** | ICMS Diferido |
| **Valid** | Positivo() |
| **Inic.Padrão** | 100 |
| **Help** | Informe o percentual do ICMS DIFERIDO (Valor do ICMS que será recolhido na operação posterior). |

Tabela **SD1 – Itens das Notas de Entrada**

| **Campo** | D1\_ICMSDIF |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 999,999,999.99 |
| **Título** | Vlr.ICMS Dif |
| **Descrição** | Valor do ICMS Diferido |
| Valid | Positivo().And.MaFisRef("IT\_ICMSDIF","MT100",M->D1\_ICMSDIF) |
| Help | Valor do ICMS diferido. |

**Atenção:**Este campo é preenchido automaticamente pelo sistema.

| **Campo** | D1\_VOPDIF |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 999,999,999.99 |
| **Título** | Vlr.OP.Dif |
| **Descrição** | Valor da Operação |
| **Valid** | Positivo().And.MaFisRef("IT\_VOPDIF","MT100",M->D1\_VOPDIF) |
| **Help** | Valor como se não tivesse o diferimento. |

Tabela **SD2 – Itens das Notas de Saída**

| **Campo** | D2\_ICMSDIF |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 999,999,999.99 |
| **Título** | Vlr.ICMS Dif |
| **Descrição** | Valor do ICMS Diferido |
| **Valid** | Positivo().And.MaFisRef("IT\_ICMSDIF","MT100",M->D2\_ICMSDIF) |
| **Help** | Valor do ICMS diferido. |

**Atenção:**Este campo é preenchido automaticamente pelo sistema.

| **Campo** | D2\_VOPDIF |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 999,999,999.99 |
| **Título** | Vlr.OP.Dif |
| **Descrição** | Valor da Operação |
| **Valid** | Positivo().And.MaFisRef("IT\_VOPDIF","MT100",M->D2\_VOPDIF) |
| **Help** | Valor como se não tivesse o diferimento. |

Tabela **SFT– Livro Fiscal por Item de NF**

| **Campo** | FT\_ICMSDIF |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 999,999,999.99 |
| **Título** | Vlr.ICMS Dif |
| **Descrição** | Valor do ICMS Diferido |
| **Valid** | MaFisRef("LF\_ICMSDIF","MT100",M->FT\_ICMSDIF) |
| **Help** | Valor do ICMS diferido. |

**Atenção:**Este campo é preenchido automaticamente pelo sistema.

| **Campo** | FT\_VOPDIF |
| --- | --- |
| **Tipo** | Numérico |
| **Tamanho** | 16 |
| **Decimal** | 2 |
| **Formato** | @E 999,999,999.99 |
| **Título** | Vlr. Op. Dif. |
| **Descrição** | Valor da Operação |
| **Valid** | Positivo().And.MaFisRef("IT\_VOPDIF","MT100",M->FT\_VOPDIF) |
| **Help** | Valor como se não tivesse o diferimento. |

**\*Atenção:**Este campo é preenchido automaticamente pelo sistema.

IMPORTANTE

Os campos **F4\_ICMSDIF** e **F4\_PICMDIF** precisam ser configurados corretamente de acordo com a necessidade. A seguir está detalhado o funcionamento de cada uma das opções existentes.

Atenção

Quando definido como 100% no campo **F4\_PICMDIF**significa que haverá o diferimento total do ICMS, caso seja informado um valor diferente de 100 o cálculo será realizado de acordo com o Percentual informado.

**1 - ICMS Diferido**

**Configurações necessárias:**

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 1 

**F4\_PICMDIF:**Informar o Percentual de Diferimento

**Exemplo com Percentual de Diferimento igual a 33,33%**

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 33,33% 

**Valor do ICMS Diferido**

**Fórmula:** Valor x Percentual de ICMS x Percentual de Diferimento

**ICMS Próprio** R$ 100,00 x 0,18 = R$ 18,00

**ICMS Diferido** R$ 18,00 x 0,3333 = R$ 5,9994 (R$6,00)

**Valor do ICMS Devido**

R$ 18,00 (ICMS Próprio)  - R$6,00 (ICMS Diferido)  = R$ 12,00

**Demais Informações**

Valor Total: R$ 100,00

Valor do Título: R$ 100,00 - R$ 6,00 = R$ 94,00

**Exemplo com Percentual de Diferimento igual a 100%**

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 100% 

**Valor do ICMS Diferido**

**Fórmula:**Valor x Percentual de ICMS x Percentual de Diferimento

**ICMS Próprio** R$ 100,00 x 0,18 = R$ 18,00

**ICMS Diferido** R$ 18,00 x 1 = R$ 18,00

**Valor do ICMS Devido**

R$ 18,00

**Demais Informações**

Valor Total: R$ 100,00

Valor do Título: R$ 100,00 - R$ 18,00 = R$ 82,00

**2 - Sem diferimento**

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 2

**F4\_PICMDIF:**Em branco

**3 - Diferimento com redução**

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 3

**F4\_PICMDIF:**Informar o Percentual de Diferimento

**Exemplo com Percentual de Diferimento igual a 33,33%**

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 33,33%

**Valor do ICMS Diferido**

**Fórmula:**Valor x Percentual de ICMS x Percentual de Diferimento

**ICMS Próprio** R$ 100,00 x 0,18 = R$ 18,00

**ICMS Diferido** R$ 18,00 x 0,3333 = R$ 5,9994 (R$6,00)

**Valor do ICMS Devido**

R$ 18,00 (ICMS Próprio)  - R$6,00 (ICMS Diferido)  = R$ 12,00

**Demais Informações**

Valor do Título: R$ 100,00

Valor Total: R$ 100,00

**Exemplo com Percentual de Diferimento igual a 100%**

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 100%

**Valor do ICMS Diferido**

**Fórmula**: Valor x Percentual de ICMS x Percentual de Diferimento

**ICMS Próprio** R$ 100,00 x 0,18 = R$ 18,00

**ICMS Diferido** R$ 18,00 x 1 = R$18,00

**Valor do ICMS Devido**

R$ 18,00 (ICMS Próprio)  - R$ 18,00 (ICMS Diferido)= R$ 0,00

**Demais Informações**

Valor do Título: R$ 100,00

**4 - ICMS reduzido do valor a recolher e somado ao total do Título e da Nota Fiscal**

**Observação:**O tipo 4 foi criado antes da NF-e, logo ao utilizar essa opção, ao transmitir a nota fiscal, pode acontecer erros, pois a soma dos itens não será igual ao total da NF, uma vez que o ICMS diferido é somado apenas ao total da nota fiscal**.**

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 4

**F4\_PICMDIF:**Informar o Percentual de Diferimento

**Exemplo com Percentual de Diferimento igual a 33,33%**

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 33,33%

**Valor do ICMS Diferido**

**Fórmula**: Valor x Percentual de ICMS x Percentual de Diferimento

**ICMS Próprio** R$ 100,00 x 0,18 = R$ 18,00

**ICMS Diferido** R$ 18,00 x 0,3333 = R$ 5,9994 (R$6,00)

**Valor do ICMS Devido**

R$ 18,00 (ICMS Próprio)  - R$6,00 (ICMS Diferido)  = R$ 12,00

**Demais Informações**

Valor Total: Valor + Diferimento = R$ 100,00 + R$ 6,00 = R$ 106,00

Valor do Título: R$ 106,00

**Exemplo com Percentual de Diferimento igual a 100%**

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 100%

**Valor do ICMS Diferido**

**Fórmula:**Valor x Percentual de ICMS x Percentual de Diferimento

**ICMS Próprio** R$ 100,00 x 0,18 = R$ 18,00

**ICMS Diferido** R$ 18,00 x 1 = R$18,00

**Valor do ICMS Devido**

R$ 18,00 (ICMS Próprio)  - R$ 18,00 (ICMS Diferido)= R$ 0,00

**Demais Informações**

Valor Total:  Valor + Diferimento = R$ 100,00 + R$ 18,00 = R$ 118,00

Valor do Título: R$ 118,00

**5 - Diferimento com ST**

**Observação**: A opção 5 se refere ao diferimento parcial do ICMS próprio previsto no artigo 108 do RICMS-PR/2012, para maiores informações verifique o parecer tributário disponível no link: [http://tdn.totvs.com/x/E5lICw](https://tdn.totvs.com/x/E5lICw). Ao utilizar essa opção o diferimento só se aplicará ao cálculo do ICMS próprio, não se estendendo ao ICMS-ST.

A regra de cálculo do Diferimento do ICMS não prevê a geração de uma alíquota diferida, e sim da aplicação do % de Diferimento sobre o ICMS total calculado, desta forma o cálculo será realizado da seguinte forma.

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 5

**F4\_PICMDIF:**Informar o Percentual de Diferimento

É necessário cadastrar exceção fiscal com alíquota interna do ICMS com valor da alíquota reduzida pelo Diferimento, e para calculo do ICMS ST informe alíquota do destinatário. Por exemplo:

**F7\_ALIQINT**   = 12 - alíquota com Diferimento.

**F7\_ALIQDST** =18  - Alíquota do destinatário para cálculo do ICMS ST

**Exemplo com Percentual de Diferimento igual a 33,33%**

**Dados complementares:**

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 33,33%

**Alíquota com Diferimento**

**Fórmula**: Alíquota de ICMS x (Alíquota de ICMS + Percentual de Diferimento)

Alíquota com diferimento : 18 - (18 \* 0,3333) = (18 - 5,994) = 12,00

**Valor do ICMS Devido** 

R$ 100,00 x 0,12 = R$ 12,00 

**Valor ICMS Diferido**

**Fórmula:**Valor do ICMS - Valor do ICMS Devido

R$ 18,00 - R$ 12,00 = R$ 6,00

**Base do ST**

Base de ST: Valor x (1+(Margem/100))

Base de ST: 100,00 \* (1+(71,78/100)) = R$ 171,78

**Valor do ST**

Valor de ST: (Base \* Alíquota (F7\_ALIQDST )) - ICMS Devido

Valor de ST: (171,78 \* 18%)) - 12,00 = R$ 18,92

**Demais Informações**

Valor do Título: R$ 118,92

Valor Total: R$ 118,92

**7 - Dedução ICMS e Base Composta**

Observação: O cálculo implementado nesta opção está baseada na ***[Resolução 13/2019](http://www.fazenda.rj.gov.br/sefaz/faces/oracle/webcenter/portalapp/pages/navigation-renderer.jspx;jsessionid=9w8fclyJHn12QbgY1c3QJVDS7nLJTB1WvMqndcCTGpHRBJ2hbpLL!704060084?datasource=UCMServer%23dDocName%3AWCC342616&_adf.ctrl-state=u578mtlxt_1&_afrLoop=14637283456622964&_afrWindowMode=0&_afrWindowId=null)*** do Estado do Rio de Janeiro, mas está disponível para utilização por qualquer estado de destino ou origem em que seja necessário realizar o cálculo do ICMS Diferido com base composta, conforme orientações abaixo: 

*§ 1ºNos casos de diferimento total, o campo "Valor do ICMS diferido" deverá ser preenchido com o resultado da seguinte fórmula*

*Valor do ICMS diferido = (Preço na Nota Fiscal / (1 - Alíquota)) \* Alíquota*

*§ 2º Nos casos de diferimento parcial, para o preenchimento do campo "Valor do ICMS diferido" o resultado da fórmula referida no § 1º deverá ser multiplicado pelo percentual de diferimento aplicável.*

**F4\_ICM:**Definido como SIM.

**F4\_ICMSDIF:**Definido como 7

**F4\_PICMDIF:**Informar o Percentual de Diferimento

**Exemplo com Percentual de Diferimento igual a 70%**

Valor: R$ 1000,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 70%

**Valor do ICMS Diferido com Base Composta**

**Fórmula**: (((Valor/ (1 - Percentual de ICMS)) \* Percentual de ICMS) \* Percentual de Diferimento)

Valor do Diferimento: (((1000,00 /( 1 - 18%)) \* 18% )\*70%)

Valor do Diferimento: (((1000,00 /( 0,82)) \* 18% )\*70%) 

Valor do Diferimento: ((1.219,51 \* 18% )\*70%)

Valor do Diferimento: (219,51\*70%)= 153,66

Valor do ICMS Tributado = 219,51 - 153,66 = 65,85

**Documento de Entrada / Saída**

**![](https://tdn.totvs.com/download/attachments/244917288/image2019-12-20_11-46-22.png?version=1&modificationDate=1576856783017&api=v2)**

**Exemplo com Percentual de Diferimento igual a 100%**

Valor: R$ 1000,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 100%

**Valor do ICMS Diferido com Base Composta**

**Fórmula**: (((Valor  / (1 - Percentual de ICMS)) \* Percentual de ICMS) \* Percentual de Diferimento)

Valor do Diferimento: (((1000,00 / 1 - 18%)) \* 18%)\*100%)

Valor do Diferimento: ((1.219,51 \* 18% )\*100%)

Valor do Diferimento: (219,51\*100%)= 219,51

**Atenção:** Caso seja utilizado um percentual igual a 100 o valor de ICMS ficará zerado, pois ao definir como 100% significa que ocorreu um diferimento do Valor Total. 

**Documento de Entrada / Saída**

![](https://tdn.totvs.com/download/attachments/244917288/image2019-12-20_16-27-18.png?version=1&modificationDate=1576873638597&api=v2)

Importante!

Na planilha financeira do Pedido de Venda e aba de impostos dos documentos de entrada e saída a base de cálculo do ICMS Próprio não será gravada com valor da base composta utilizada para o cálculo do ICMS Diferido, considerando a orientação do Manual de Preenchimento de Notas Fiscais publicado juntamente com a Resolução 13/2019 do Rio de Janeiro, que define que os valores devem ser apresentados da seguinte forma no XML da Nota Fiscal:

* ***Valor da BC do ICMS:** valor da BC;*
* ***Alíquota:** alíquota padrão aplicada à mercadoria;*
* ***Valor do ICMS da Operação, campo vICMSOp:** valor do imposto como se não houvesse diferimento;*
* ***Percentual do diferimento, campo pDif:** informar o percentual. No caso de diferimento total, informar o percentual de diferimento "100".*
* ***Valor do ICMS diferido, campo vICMSDif:** informar o valor diferido.*
* ***Valor do ICMS, campo vICMS:** Informar o valor realmente devido, caso se trate de diferimento parcial.*

## **03. TABELAS UTILIZADAS**

* **SF4** - Tipo de Entrada e Saída
* **SD1**- Itens das Notas de Entrada
* **SD2**- Itens das Notas de Saída
* **SFT**- Livro Fiscal por Item de NF
