---
article_id: 360051999634
category: SIGAEST - CUSTOS
content_hash: b65fca0c7c0ece46ce3b06c3698bdb0ecb2a4349a81cd05a6dfea16bbfb97a0b
fetched_at: '2026-06-28T22:39:00.469803+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Refaz Custo de Entrada
  (MATA190) - Conceito e Exemplos
type: support-article
updated_at: '2026-05-05T17:59:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos
---

**Dúvida**

O que é e como configurar o sistema para apurar o Custo de Entrada corretamente?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

# Custo de entrada

A rotina Refaz Custo de Entrada tem o objetivo de "ajustar" custos de entrada quando algum(ns) documento(s) de entrada foram gerados com custo incorreto. O custo de entrada é apurado com base nas despesas e impostos recuperáveis.

Para configurar estes impostos de forma que o custo fique conforme a necessidade do usuário, podemos modificar o TES ou, em alguns casos, os parâmetros (SX6) do configurador.

Um dos parâmetros mais importantes é o **MV\_A190REF** para que o custo de entrada seja o mesmo calculado pela rotina refaz custo de entrada (MATA190 - função A103CUSTO). Aconselhamos deixar este parâmetro habilitado. [Para mais detalhes deste parâmetro, clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=187829990)

A rotina Refaz Custo de Entrada pode ser executada sempre que necessário ou para ajustes do custo que não ficou correto.

**CUSTO DE ENTRADA COM VALOR ZERADO? Valide se sua TES não é de bonificação:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como fazer uma nota de Bonificação que atualiza somente quantidade sem atualizar custo ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411958726935-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-fazer-uma-nota-de-Bonifica%C3%A7%C3%A3o-que-atualiza-somente-quantidade-sem-atualizar-custo)

**Vídeos explicativos, com configurações dos impostos mais simples, para calculo no custo de entrada.**

***How To Como calcular PIS COFINS no custo de entrada#TOTVS Backoffice (linha Protheus)***  
***Link:*** [***https://youtu.be/PCp\_9tDG\_ts***](https://youtu.be/PCp_9tDG_ts)

***How To Como calcular IPI no custo de entrada#TOTVS Backoffice (linha Protheus)***  
***Link:*** [***https://youtu.be/3C0Vpqz0uz0***](https://youtu.be/3C0Vpqz0uz0)

***How To Como calcular ICMS ST no custo de entrada#TOTVS Backoffice (linha Protheus)***  
***Link:*** [***https://youtu.be/tJ-WjdME5Qk***](https://youtu.be/tJ-WjdME5Qk)

***How To Como calcular ICMS no custo de entrada#TOTVS Backoffice (linha Protheus)***  
***Link:*** [***https://youtu.be/\_7d0LZEpFPI***](https://youtu.be/_7d0LZEpFPI)

Nesta documentação não abordaremos a parte fiscal, utilizamos apenas as configurações mínimas para podermos apurar o custo, o ideal é que sempre seja ajustada primeiramente a parte fiscal e, somente após isso, ajustar o custo.

**Para o cálculo de custo, o TES, independentemente de atualizar ou não o estoque (F4\_ESTOQUE), terá o custo apurado, exceto nos casos de entrada por bonificação.**

**É importante compreender que:**

* Quando **F4\_ESTOQUE = 'NÃO'**, a movimentação não atualiza o estoque, o que significa que essa operação não será exibida no relatório **KARDEX, o calculo do custo ira ocorrer normalmente, mas não sera considerado no ESTOQUE do ITEM, porque a TES não atualizou ESTOQUE.**
* No entanto, o custo da movimentação será devidamente apurado no campo **D1\_CUSTO**.

Quando não atualiza estoque, o efeito dos calculos serão apenas **FISCAIS**.

**Custo com entrega futura:**

[Como funciona o cálculo do custo de entrada no processo de compra com entrega futura](https://tdn.totvs.com/x/X_QuHg)

**Configurações e parametrizações quando impostos agregam ou não ao Custo**

Veja abaixo as Configurações ou também no link da FAQ abaixo:

[**Backoffice (Linha Protheus) - SIGAEST - Como configurar o custo de entrada com impostos na TES?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19509172274455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-custo-de-entrada-com-impostos-na-TES)

# ICMS

O cálculo do ICMS pode ser feito deixando o campo **F4\_ICM = Sim**, no nosso exemplo vamos utilizar uma nota com Valor Total de 1000 e alíquota de 12%. Podemos definir esta alíquota através do campo **B1\_PICM** ou através de configurações específicas do Fiscal.

O custo sempre parte do Valor Total da nota conforme imagem abaixo:

![1_-_TOTAL_NOTA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084384313)

Nos exemplos utilizaremos a entrada de um produto com quantidade 1 e custo unitário 1000. Utilizaremos esta métrica em todos os casos.

O ICMS (12%) já está embutido no custo portanto temos três possibilidades:

- Manter ICMS sem descontar do valor da nota;

- Fazer o ICMS abater do valor da nota;

- Somar o ICMS no custo do produto.

**1° Exemplo - Mantendo o ICMS sem descontar do valor da nota;**

Vamos verificar primeiro o custo sem o desconto do ICMS, ou seja, 1000 reais.

Então, configuraremos o TES da seguinte forma, **F4\_CREDICM = Não** e **F4\_ICM = Sim**, detalhes abaixo:![2_-_ICMS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084385073)

Agora veja detalhes da nota e posteriormente o Kardex por período (MATR900) com o custo da nota.

![MATA103_ICMS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360083214134)

![MATR900_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084385753)

**2° Exemplo - ICMS descontando do valor total da nota (e consequentemente o custo também):**

Agora vamos abater o valor do ICMS do custo através do campo **F4\_CREDICM = Sim**.

Veja que é a mesma nota que geramos o Kardex anteriormente, apenas alteramos o TES e executamos a rotina Refaz Custo de Entrada (MATA190). Desta forma, o custo passou de 1000,00 para 880,00

![MATR900_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083214334)

Também podera utilizar do parametro [MV\_CREDICM](https://tdn.totvs.com/pages/releaseview.action?pageId=235594540).

*(**ATENÇÃO**: Se sua TES possuir configuração de CREDITAR o ICMS, considere não usar através do parametro, porque assim podera haver duplicidade de calculo, use pela TES ou pelo Parametro).*

**3° Exemplo - Somar o ICMS no custo do produto:**

Para somar o ICMS no custo do produto precisa ter a configuração de TES nos campos F4\_CREDICM = N , F4\_ICM = SIM e F4\_AGREG = I, conforme exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406608589591)

Ao analisar na rotina de Documento de Entrada irá validar na aba impostos o **valor do imposto** que somará no custo do produto:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406614778519)

Ao analisar no Kardex (MATR900) irá verificar que o ICMS somou no custo do produto:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406614854679)

# DIFAL/ICMS Complementar

Para o cálculo do DIFAL entre no custo do produto, basta configurar os campos do TES da seguinte forma: Calcula ICMS **(F4\_ICM) = Sim**, Material de Consumo **(F4\_CONSUMO) = Sim**, Calc Dif ICM **(F4\_COMPL) = Sim,** Livro Fiscal de ICMS **(F4\_LFICM) <> Não** e **F4\_DIFAL = SIM** e o parametro **MV\_BASDENT** configurado de acordo com a UF do fornecedor.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411515802007)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411515814167)**

Após ter feito a configuração acima da TES, favor incluir um novo Documento de Entrada referenciando a TES alterada e validar a aba impostos que irá informar o imposto e o valor que será acrescentado no custo da nota fiscal para o produto:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411523682199)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411524158359)

Para maiores informações sobre o DIFAL favor verificar na documentação abaixo:

[MP - FIS - Configuração para calcular o diferencial(DIFAL) de alíquota nas operações de compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027020251-MP-FIS-Configura%C3%A7%C3%A3o-para-calcular-o-diferencial-DIFAL-de-al%C3%ADquota-nas-opera%C3%A7%C3%B5es-de-compras?source=search)

# IPI

Com o IPI temos três possibilidades:

- Mantermos o custo;

- Somar no custo;

- Em casos específicos abater do custo.

**1° Exemplo - Mantendo o custo**

Os campos para que possamos calcular o IPI são: **F4\_CREDIPI** e **F4\_IPI**. Utilizaremos uma alíquota de 8%, veja abaixo a imagem do TES:

![5_-_IPI-TES.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083215234)

Veja os detalhes no Documento de Entrada:

![MATA103_IPI.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360083215414)

Veja abaixo no Kardex onde o custo do produto com o campo F4\_CREDIPI = Sim, o sistema mantém o custo do produto.

![MATR900_03_IPI.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083215634)

**2° Exemplo - Fazendo o IPI somar no custo do produto**

Para somarmos o IPI no custo será necessário colocar o campo **F4\_CREDIPI = Não**, veja abaixo o resultado.

![MATR900_04_IPI.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083215834)

**3° Exemplo - IPI abatendo do custo total da nota.**

Em alguns casos o cliente precisa abater o IPI do custo.  Neste caso, podemos configurar o campo **F4\_IPI = R** e o campo **F4\_CREDIPI = Sim**. Também será necessário informar a porcentagem do IPI que será abatido através do campo **F4\_IPIPECR**  (no nosso exemplo colocaremos100%), veja abaixo que o sistema realizou o abatimento de 80 reais do IPI do custo.

![MATR900_05_IPI_R.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083215974)

# ICMS ST/ICMS RETIDO

Para o cálculo do ICMS ST/ ICMS RETIDO temos algumas combinações possíveis devido aos ajustes da parte fiscal.

No caso do ICMS ST/ ICMS RETIDO podemos:

- Manter no custo;

- Somar no custo;

- Abater do custo.

**1° Exemplo - Mantendo  com o ICMS ST/ICMS RETIDO o valor do custo total da nota**

Com o campo do Cadastro de Produtos **B1\_PICMENT = 12** e campo do TES **F4\_CREDST = 1**, irá manter no custo, veja a imagem abaixo:

![MATR900_06_ST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084387273)

**2° Exemplo - Somando o ICMS ST/ICMS RETIDO no custo do Produto**

No caso o valor do ICMS ST é de 60, conteúdo do campo **D1\_ICMSRET**.

Para somar o ICMS ST no custo, basta configurar o campo **F4\_CREDST** com o conteúdo **2, 3 ou 4**, qualquer uma destas opções irá somar no custo do produto, detalhes na imagem abaixo:

![MATR900_07_ST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083216054)

**OBS:** Outra forma de somar o ICMS ST no custo é com parâmetro **MV\_ICMRCUS** habilitado e os campos do TES **F4\_ANTICMS** **= 1** e **F4\_CREDST = 4**.

*(**ATENÇÃO**: Se sua TES possuir configuração de Calculo do ICMS ST, considere não usar através do parametro, porque assim podera haver duplicidade de calculo, use pela TES ou pelo Parametro).*

**3° Exemplo - Abatendo o ICMS ST/ICMS RETIDO do custo total da nota**

Para abater o ICMS ST do custo do produto pode ser feita a seguinte configuração: **F4\_CREDST** **= 1** e **F4\_INCSOL = A** ou **D**, veja abaixo como ficou o custo:

![MATR900_08_ST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084387413)

# **ICMS MONOFASICO**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como lançar a nota fiscal de entradas de Óleo diesel tag15 no mata103?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14558273258007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-lan%C3%A7ar-a-nota-fiscal-de-entradas-de-%C3%93leo-diesel-tag15-no-mata103)

Esse imposto não esta contemplado na TES (MATA080), somente mediante configuração dentro do CONFIGURADOR DE TRIBUTOS.

Existe uma exceção já mapeada sobre o ICMSST e STMONO, onde caso existe divergência nos custos com a utilização do configurador de tributos, valide a configuração do campo:

**TES Agreg. Solid F4\_INCSOL deve ter seu conteudo igual a S-Sim.**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Complemento ICMS ST para compra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023274691-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Complemento-ICMS-ST-para-compra)

# 

# **PIS/COFINS**

Para o cálculo do PIS/COFINS utilizaremos alíquotas 0,65% e 2%, o campo do TES "Pis/Cofins" (**F4\_PISCOF)** = **Ambos**, os campos da tabela SD1 que serão alimentados são: **D1\_VALIMP5** (COFINS) e **D1\_VALIMP6** (PIS).

O PIS/COFINS pode ser usado e manter ou abater do custo total da nota. O campo chave para isso é o **F4\_PISCRED.**

**1° - Exemplo - Abatendo do custo total**

Com campo **F4\_PISCRED = 1**, o Protheus abaterá do custo, conforme imagem abaixo:

![MATA103_PIS-COF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360083220274) ![MATR900_09_PIS-COF.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083220694)

Também pode ser utilizado o campo **F4\_PISCRED = 1** com os parâmetros [**MV\_CREDCOF**](https://tdn.totvs.com/display/public/PROT/TRY340_DT_PARAMETROS_CREDITA_NO_CUSTO_PIS_COFINS) e [**MV\_CREDPIS**](https://tdn.totvs.com/display/public/PROT/TRY340_DT_PARAMETROS_CREDITA_NO_CUSTO_PIS_COFINS) habilitados para abater o PIS/COFINS do custo.

*(**ATENÇÃO**: Se sua TES possuir configuração de CREDITAR o PIS E COFINS, considere não usar através do parametro, porque assim podera haver duplicidade de calculo, use pela TES ou pelo Parametro).*

**2° Exemplo - Mantendo o custo do produto**

Vejamos agora a configuração para manter no custo do produto mesmo com o PIS e COFINS. Neste caso podemos configurar o campo **F4\_PISCRED = 2, 3, 4 ou 5**.

![MATR900_10_PIS-COF.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083220834)

# PIS/COFINS Majorado

Para apuração do custo do PIS/COFINS Majorado temos que configurar os campos conforme a documentação abaixo, lembrando que não estamos validando a parte fiscal.

<https://tdn.totvs.com/pages/viewpage.action?pageId=6076840>

Caso tenha o cálculo do ICMS e IPI, deve-se configurar o campo do TES **F4\_ICM e F4\_IPI = Sim.**

Veja um exemplo com:

- Alíquota de PIS (**MV\_TXPIS** ) = **0,65;**

- COFINS (**MV\_TXCOFIN**) **=** **2;**

- Alíquota majorada PIS (**F4\_MALQPIS**) **1,65;**

- COFINS (**F4\_MALQCOF**) **7,60** e

 - Crédito PIS/COFINS (**F4\_PISCRED**) **= 1**.

**Ficara dessa forma na "APURAÇÃO FISCAL", isso não quer dizer que é exatamente esses valores de apuração dos impostos para o CUSTO, como vamos ver adiante.**

**![Screenshot_10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30761496328215)**

**Vlr.Imposto:**  
ICMS = 269,78  
IPI= 100,00  
PS2/PISMAJ= 23,00  
CF2/COFMAJ= 106,00

**O custo, sera agregado nos campos após as apurações calculadas, que vai ficar dessa forma aqui: Veja agora como ficou o custo, neste caso será:**

D1\_TOTAL(Valor total) + D1\_ICM(Valor do ICMS) + D1\_IPI(Valor do IPI) + D1\_VALPMAJ(Valor PisMaj) + D1\_VALCMAJ(Valor CofMaj) = D1\_CUSTO(Custo do produto)

![Screenshot_12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30761496329751)

![Screenshot_11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30761508008343)

Pode surgir a seguinte duvida sobre a formação do custo e apuração fiscal, pois na apuração fiscal os valores majorados ficaram dessa forma no documento de entrada:

PS2/PISMAJ= 23,00  
CF2/COFMAJ= 106,00

**Mas a apuração foi de:**

PS2/PISMAJ= 16,50  
CF2/COFMAJ= 76

Para duvidas sobre a apuração fiscal, sugerimos validar pontualmente com o time "**Protheus FISCAL**"

**IMPORTANTE:** Os exemplos apresentados têm o único propósito de simular o cálculo de custo. Qualquer dúvida referente às alíquotas de impostos, incluindo quais devem ou não ser aplicadas conforme seu estado, município e demais regulamentações, deve ser tratada como uma questão estritamente fiscal. **Não se baseie nas alíquotas e valores demonstrados, pois são meramente ilustrativos para exemplificar o cálculo de custo.**

# Imposto de Importação, frete e despesas.

O Imposto de Importação, assim como Despesas, podem ser digitados na aba "Descontos/Fretes/Despesas" da rotina documento de entrada (MATA103) conforme imagem abaixo, desta forma estes impostos serão agregados ao custo automaticamente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083223214)

O imposto de importação também pode ser gravado no campo D1\_II, para agregar ao custo, quando gravado no campo D1\_II, será necessário habilitar o parâmetro **MV\_EIC0064**.

As notas de frete também podem ser gravadas através da rotina Conhecimento de Frete (MATA116) ou mesmo pela rotina Documento de Entrada (MATA103), para isto basta que configurar os camposdo TES **F4\_ESTOQUE = Sim** e o **F4\_QTDZERO = Sim** para que possamos digitar apenas custo não sendo necessário digitar quantidade.

**O que normalmente solicitamos em caso de problemas/duvidas relacionados ao Custo de Entrada?**

É sempre importante enviar a memória de cálculo para podermos entender como é composto o custo do cliente, segue abaixo exemplo de memória de cálculo.

Total da Nota – ICMS + IPI + PIS/COFINS.

**É possível agregar o imposto de INSS e outros impostos ao Custo do Produto?**

Sim. Para configuração do imposto de INSS, segue usar a referência do artigo a seguir:  
[**MP - SIGAFIN - Configuração e parâmetros do imposto INSS**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019175871-MP-SIGAFIN-Configura%C3%A7%C3%A3o-e-par%C3%A2metros-do-imposto-INSS?source=search)

O valor de INSS é tratado de forma contábil. Para agregar a valor do imposto do INSS ao custo do produto somente é possível por customização e poderá ser usado o ponto de entrada [**A103CUST - Manipula Custo de Entrada**](https://tdn.totvs.com/display/public/PROT/A103CUST+-+Manipula+Custo+de+Entrada)

**É possível abatimento de crédito presumido no custo?**

[Como funciona o Abatimento do Crédito Presumido no Custo](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=520652244)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Qual a configuração para o sistema não somar o Crédito Presumido no Total da nota fiscal?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026147114--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-para-o-sistema-n%C3%A3o-somar-o-Cr%C3%A9dito-Presumido-no-Total-da-nota-fiscal-?source=search)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Como configurar o custo de entrada com impostos na TES?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19509172274455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-custo-de-entrada-com-impostos-na-TES)
