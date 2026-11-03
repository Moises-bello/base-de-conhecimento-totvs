---
article_id: 19509172274455
category: SIGAEST - CUSTOS
content_hash: a7d83d850687cf3bf8252df624f9e3633f2c852e207632cd28e1c64d496305a5
fetched_at: '2026-06-28T22:39:00.680497+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como configurar o
  custo de entrada com impostos na TES?
type: support-article
updated_at: '2026-03-03T19:22:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19509172274455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-custo-de-entrada-com-impostos-na-TES
---

O artigo explica como configurar o cálculo de impostos no custo de entrada de mercadorias no TOTVS Protheus, abordando ICMS, ICMS/ST, Crédito Presumido, IPI, PIS/COFINS, Imposto de Importação, DIFAL, entre outros. Destaca a importância das configurações fiscais corretas e orienta sobre procedimentos para dúvidas, solicitações e casos específicos, como compra com entrega futura e impostos não contemplados no sistema. Links e vídeos complementam o conteúdo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19509294716183) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**

Como configurar o calculo de impostos no custo de entrada das mercadorias?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Antes de ser abortada as questões para calculos dos impostos no custo da mercadoria, é importante ressaltarmos, que **essas configurações vão de acordo com a necessidade de calculo aqui informadas**, e dúvidas sobre o porque o campo da TES é X,Y,Z deverá ser tratada diretamente com o time FISCAL.

O cálculo do custo de entrada de uma mercadoria envolve a determinação **precisa do total no documento fiscal, considerando a inclusão ou exclusão de impostos**. Este processo requer **configurações fiscais adequadas** para refletir os impostos desejados no custo de entrada da nota, o que tem implicações legais e fiscais significativas. **A documentação abordará os principais impostos e métodos de configuração para os cálculos mais comuns, e ja condizentes de necessidade de acordo legislações vigentes.**

Caso algum imposto específico não esteja abordado, é possível solicitar uma avaliação por meio de um ticket. **Se o sistema atual não suportar o cálculo, podera ser fornecido pelo cliente um embasamento legal para que seja analisado pelo time de segmentos**. Se o cálculo estiver de acordo com a legislação, será submetido à avaliação do time de produto para a devida incorporação no sistema, e acresicdo ao boletim.

**DOCUMENTAÇÃO REFERENCIA HISTÓRICA:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Refaz Custo de Entrada (MATA190) - Conceito e Exemplos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos)

**Tópicos Apresentados**

1. **Calculo de ICMS no custo de entrada**
2. **Calculo de ICMS/ST no custo de entrada**
3. **Calculo de Crédito Presumido no Custo**
4. **Calculo de IPI no custo de entrada**
5. **Calculo de PIS/COFINS no custo de entrada**
6. **Calculo de PIS/COFINS Majorado no custo de entrada**
7. **Calculo de Imposto de Importação, frete e despesas no custo de entrada**
8. **Calculo de DIFAL no custo de entrada**
9. **Cálculo do custo de entrada no processo de compra com entrega futura**
10. **ICMS Monofasico no custo**
11. **Outros IMPOSTOS não contemplados**
12. **Valor de Frete no custo de entrada?**

**IMPORTANTE:**

Sempre que abrir uma solicitação ao suporte, com questionamento sobre o custo de entrada não condizer com oque espera, por favor nos informe, qual é o calculo desejado por você, por exemplo:

O custo deveria ser (Valor - ICMS)  
D1\_TOTAL - D1\_VALICM = D1\_CUSTO

**Se possivel por favor, enviar os dados seguintes, peça ao seu T.I**

* SB1 filtrada por um produto apenas em formato SQLITE/SQLSERVER
* SF4 filtrada pela TES usada no documento de entrada em formato SQLITE/SQLSERVER
* SD1 filtrada pelo produto ou documento .em formato SQLITE/SQLSERVER
* [Central de diagnostico Atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)
* Print da aba de impostos do documento de entrada
* Se acaso usar Configurador de tributos, enviar print também da aba de tributos

Assim podemos tentar validar internamente uma nota com as mesmas configurações que você, e identificar o calculo efetivado.

**1 - Calculo de ICMS no custo de entrada.**

Para o Imposto de ICMS (Imposto sobre Circulação de Mercadorias e Serviços), temos 3 tipos de operações para calculo no custo da nota de entrada, sendo elas:

**-Manter ICMS sem descontar do valor da nota, para efeito somente fiscais.**

(Credita ICMS)**F4\_CREDICM** = Não e (Calcula ICMS)**F4\_ICM** = Sim

**-Fazer o ICMS abater do valor da nota;**

(Calcula ICMS)**F4\_ICM** = Sim e (Credita ICMS)**F4\_CREDICM** = Sim

Também pode-se utilizar do parametro [**MV\_CREDICM**](https://tdn.totvs.com/pages/releaseview.action?pageId=235594540)

**-Somar o ICMS no custo do produto.**

(Calcula ICMS)**F4\_ICM** = SIM e **F4\_AGREG** = I (ICMS + Mercadoria)

***How To Como calcular ICMS no custo de entrada#TOTVS Backoffice (linha Protheus)***  
***Link:***[***https://youtu.be/\_7d0LZEpFPI***](https://youtu.be/_7d0LZEpFPI)

Referencia FISCAL sobre o campo **F4\_AGREG**: 

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038657433-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-do-campo-Agrega-Valor-F4-AGREG->

**2 - Calculo de ICMS/ST no custo de entrada.**

Para o Imposto de ICMS ST (ICMS Substituição Tributária), temos 3 tipos de operações para calculo no custo da nota de entrada, o produto deve possuir o campo (Solid. Entr.)**B1\_PICMENT** com o percentual desejado, sendo elas:

**-Mantendo  com o ICMS ST o valor do custo total da nota**

(Crd.ICMS ST )**F4\_CREDST** = 1

**-Somando o ICMS ST no custo do Produto**

(ICMS Solid. )**D1\_ICMSRET** preenchido + (Crd.ICMS ST )**F4\_CREDST =** diferente de 1 (2,3 ou 4)

Outra forma de somar o ICMS ST no custo é com parâmetro [**MV\_ICMRCUS**](https://tdn.totvs.com/pages/releaseview.action?pageId=146179813)habilitado e os campos: (Antecip.ICMS)**F4\_ANTICMS** = 1 e (Crd.ICMS ST )**F4\_CREDST** = 4.

**-Abatendo o ICMS ST do custo total da nota**

(Antecip.ICMS)**F4\_CREDST** = 1 + (Agrega Solid)**F4\_INCSOL =** A ou D

***How To Como calcular ICMS ST no custo de entrada#TOTVS Backoffice (linha Protheus)***  
***Link:***[***https://youtu.be/tJ-WjdME5Qk***](https://youtu.be/tJ-WjdME5Qk)

**3 - Calculo de Crédito Presumido no Custo.**

Configuração e orientação fiscal:

[Como funciona o Abatimento do Crédito Presumido no Custo](https://tdn.totvs.com/x/1IUIHw)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Qual a configuração para o sistema não somar o Crédito Presumido no Total da nota fiscal?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026147114--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-para-o-sistema-n%C3%A3o-somar-o-Cr%C3%A9dito-Presumido-no-Total-da-nota-fiscal-?source=search)

**4 - Calculo de IPI no custo de entrada.**

Para o Imposto de IPI (Imposto sobre Produtos Industrializados), temos 3 tipos de operações para calculo no custo da nota de entrada.

**-Mantendo IPI no custo**

(Credita IPI )**F4\_CREDIPI** = Sim e (Calcula IPI )**F4\_IPI = Sim**

**- Fazendo o IPI somar no custo do produto**

(Credita IPI )**F4\_CREDIPI** = Nao e (Calcula IPI )**F4\_IPI = Sim**

**- IPI abatendo do custo total da nota.**

(Credita IPI )**F4\_CREDIPI** = Sim + (Calcula IPI )**F4\_IPI =** R **+** (% Crd.IPI)**F4\_IPIPECR =** Percentual desejado

***How To Como calcular IPI no custo de entrada#TOTVS Backoffice (linha Protheus)***  
***Link:***[***https://youtu.be/3C0Vpqz0uz0***](https://youtu.be/3C0Vpqz0uz0)

**5 - Calculo de PIS/COFINS no custo de entrada.**

Para o cálculo do PIS/COFINS utilizaremos SEMPRE> (**F4\_PISCOF)** = **Ambos**, os campos da tabela SD1 que serão alimentados são: **D1\_VALIMP5** (COFINS) e **D1\_VALIMP6** (PIS).

**- Abatendo PISCOFINS no custo da mercadoria**

(Cred.PIS/COF)**F4\_PISCRED = 1**

Também pode ser utilizado o campo **F4\_PISCRED = 1** com os parâmetros [**MV\_CREDCOF**](https://tdn.totvs.com/display/public/PROT/TRY340_DT_PARAMETROS_CREDITA_NO_CUSTO_PIS_COFINS)e [**MV\_CREDPIS**](https://tdn.totvs.com/display/public/PROT/TRY340_DT_PARAMETROS_CREDITA_NO_CUSTO_PIS_COFINS)habilitados para abater o PIS/COFINS do custo.

**- Mantendo PISCOFINS no custo da mercadoria**

(Cred.PIS/COF)**F4\_PISCRED = diferente de 1 (2,3,4 ou 5)**

*(****ATENÇÃO****: Se sua TES possuir configuração de CREDITAR o PIS E COFINS, considere não usar através do parametro, porque assim podera haver duplicidade de calculo, use pela TES ou pelo Parametro).*

**IMPORTANTE:** PIS/COFINS(D1\_VALIMP5/D1\_VALIMP6) são **agregados** no custo de entrada de IMPORTAÇÃO!!! 

Segue parecer legal: [PIS/COFINS - Importação - Custo de Importação com Cofins Majorado](https://tdn.totvs.com.br/pages/releaseview.action?pageId=394219633)

Configuração e orientação fiscal sobre o campo (Cred.PIS/COF)**F4\_PISCRED**

[Configuração do campo F4\_PISCRED](https://tdn.totvs.com/x/XDT6IQ)

**Comportamento de calculo, quando se utiliza dos campos:**

%B.C. COFINS(**F4\_BCRDCOF**) e %B.Cred PIS(**F4\_BCRDPIS**)

[Crédito de PIS/COFINS no Custo de Entrada](https://tdn.totvs.com/x/0tDqK)

**6 - Calculo de PIS/COFINS Majorado no custo de entrada.**

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

**![Screenshot_10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30761065398295)**

**Vlr.Imposto:**  
ICMS = 269,78  
IPI= 100,00  
PS2/PISMAJ= 23,00  
CF2/COFMAJ= 106,00

**O custo, sera agregado nos campos após as apurações calculadas, que vai ficar dessa forma aqui: Veja agora como ficou o custo, neste caso será:**

D1\_TOTAL(Valor total) + D1\_ICM(Valor do ICMS) + D1\_IPI(Valor do IPI) + D1\_VALPMAJ(Valor PisMaj) + D1\_VALCMAJ(Valor CofMaj) = D1\_CUSTO(Custo do produto)

![Screenshot_12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30761065399959)

![Screenshot_11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30761065401751)

Pode surgir a seguinte duvida sobre a formação do custo e apuração fiscal, pois na apuração fiscal os valores majorados ficaram dessa forma no documento de entrada:

PS2/PISMAJ= 23,00  
CF2/COFMAJ= 106,00

**Mas a apuração foi de:**

PS2/PISMAJ= 16,50  
CF2/COFMAJ= 76

Para duvidas sobre a apuração fiscal, sugerimos validar pontualmente com o time "**Protheus FISCAL**"

**IMPORTANTE:** Os exemplos apresentados têm o único propósito de simular o cálculo de custo. Qualquer dúvida referente às alíquotas de impostos, incluindo quais devem ou não ser aplicadas conforme seu estado, município e demais regulamentações, deve ser tratada como uma questão estritamente fiscal. **Não se baseie nas alíquotas e valores demonstrados, pois são meramente ilustrativos para exemplificar o cálculo de custo.**

Orientação fiscais sobre **credito majorado na importação vindas do SIGAEIC:**

[SIGAEST - Como creditar o PIS e COFINS do custo das notas fiscais de importação?](https://tdn.totvs.com/pages/releaseview.action?pageId=745741743)

**7 - Calculo de Imposto de Importação, frete e despesas no custo de entrada.**

O Imposto de Importação, assim como Despesas, podem ser digitados na aba "Descontos/Fretes/Despesas" da rotina documento de entrada (MATA103) conforme imagem abaixo, desta forma estes impostos serão agregados/creditado ao custo automaticamente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19510076242583)

O imposto de importação também pode ser gravado no campo D1\_II, para agregar ao custo, quando gravado no campo D1\_II, será necessário habilitar o parâmetro **MV\_EIC0064**.

As notas de frete também podem ser gravadas através da rotina Conhecimento de Frete (MATA116) ou mesmo pela rotina Documento de Entrada (MATA103), para isto basta que configurar os camposdo TES **F4\_ESTOQUE = Sim**e o **F4\_QTDZERO = Sim** para que possamos digitar apenas custo não sendo necessário digitar quantidade.

**Eu posso me creditar de PIS/COFINS no custo de entrada da mercadoria de importação?**

Não, conforme preve embasamento tributario: [PIS/COFINS - Estoque - Crédito de PIS e Cofins na composição do custo](https://tdn.totvs.com/x/KHijMg)

**8 - Calculo de DIFAL no custo de entrada.**

Para o cálculo do DIFAL entre no custo do produto, basta configurar os campos do TES da seguinte forma:

Calcula ICMS **(F4\_ICM) = Sim**,

Material de Consumo **(F4\_CONSUMO) = Sim**,

Calc Dif ICM **(F4\_COMPL) = Sim,**

Livro Fiscal de ICMS **(F4\_LFICM) <> Não**

(Difal) **F4\_DIFAL = SIM** e o parametro **MV\_BASDENT**configurado de acordo com a **UF do fornecedor**.

**Obs:** DIFAL **não abate do custo** (não credita, não é um imposto creditavel no custo, ele soma, uma vez que é um imposto condizente para realização de calculos na nota fiscal de saida).

Para maiores informações sobre o DIFAL favor verificar na documentação abaixo:

[MP - FIS - Configuração para calcular o diferencial(DIFAL) de alíquota nas operações de compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027020251-MP-FIS-Configura%C3%A7%C3%A3o-para-calcular-o-diferencial-DIFAL-de-al%C3%ADquota-nas-opera%C3%A7%C3%B5es-de-compras?source=search)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração para calcular o diferencial(DIFAL) de alíquota nas operações de compras base simples?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027020251-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-calcular-o-diferencial-DIFAL-de-al%C3%ADquota-nas-opera%C3%A7%C3%B5es-de-compras-base-simples?source=search)

**9 - Cálculo do custo de entrada no processo de compra com entrega futura.**

Compra com entrega futura é a venda de mercadoria já produzida ou adquirida pelo fornecedor, mas que, por conveniência ou interesse do comprador, continuará em poder do fornecedor (este se transformando em mero depositário da mercadoria vendida) até que a entrega ocorra ao cliente, em um segundo momento, conforme critérios definidos na negociação entre fornecedor e cliente.

Neste cenário de compra para entrega como é tratado o calculo do custo de entradas nas notas de simples faturamento e remessa de mercadoria?

**Detalhes com todas as configurações no tdn abaixo:**

[Como e calculado o custo com entrega futura](https://tdn.totvs.com/x/X_QuHg)

**10 - ICMS Monofasico no custo**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como lançar a nota fiscal de entradas de Óleo diesel tag15 no mata103?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14558273258007-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-lan%C3%A7ar-a-nota-fiscal-de-entradas-de-%C3%93leo-diesel-tag15-no-mata103)

Esse imposto não esta contemplado na TES (MATA080), somente mediante configuração dentro do CONFIGURADOR DE TRIBUTOS.

Atualmente (O CONFIGURADOR DE TRIBUTOS) não tem amarração com ESTOQUE CUSTOS, logo o custo utilizando o configurador, não pode alterar o CUSTO.

Existe uma exceção ja mapeada sobre o ICMSST e STMONO, onde caso existe divergencia nos custos com a utilização do configurador de tributos, valide a configuração do campo:

**TES Agreg. Solid F4\_INCSOL deve ter seu conteudo igual a S-Sim.**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Complemento ICMS ST para compra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023274691-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Complemento-ICMS-ST-para-compra)

**11 - Outros IMPOSTOS não contemplados.**

Caso a empresa entenda que se pode agregar um imposto no custo, onde nos foi enviado um embasamento legal, e o retorno da consultoria de segmentos informe ao cliente, que essa questão é incorreta, e se ainda sim o cliente e seu FISCAL entenda que podem ter o calculo, mesmo com a devolutiva da consultoria de segmentos informando que não é correto.

O cliente tem a total liberdade e responsabilidade, de efetuar o calculo desejado, mediante utilização de um ponto de entrada, o mais usado para esses caso se trata do PE:

[**A103CUST - Manipula Custo de Entrada**](https://tdn.totvs.com/display/public/PROT/PE+A103CUST+-+Manipula+Custo+das+moedas+do+Documento+de+Entrada)

**12 - Valor de Frete no custo de entrada? .**

O custo da nota de entrada é calculado com base no valor bruto. O frete, despesa e seguro são agregados nesse cálculo, que é realizado por funções fiscais.  
  
No módulo Estoque/Custos não há uma configuração específica para creditar/debitar esse valor. Nesse caso pode ser verificado junto a nossa equipe Fiscal a possibilidade de não considerar o frete no valor total da nota. Caso precise que esse valor seja considerado, pode ser utilizado o ponto de entrada A103CUST para realizar o tratamento desejado. Abaixo segue um link no TDN com maiores informações referente ao PE:  
<http://tdn.totvs.com/display/public/PROT/A103CUST+-+Manipula+Custo+de+Entrada>

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
