---
article_id: 8549061841431
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 53c40072c32a4b495aa8318e336ee73b9915845815e440cb267cf3643f85e8b1
fetched_at: '2026-06-28T22:42:06.640671+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Registro 0111
type: support-article
updated_at: '2024-05-21T15:13:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549061841431-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Registro-0111
---

**Dúvida**Como gerar o **Registro 0111 do EFD Contribuições**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para o **Método Rateio Proporcional**, com base nas vendas tributada no mercado interno, não tributada e exportação, é necessário que o parâmetro **MV\_RATPROP** (Desabilita o cálculo do crédito PIS/COFINS feito por Rateio Proporcional) esteja igual a **F ou em branco**.  
**Nesse caso os valores para o rateio serão considerados através do registro 0111**.  
O valor do rateio é calculado conforme a proporcionalidade dele em relação ao total.  
  
Estrutura do **registro 0111**.

**Campo 01 REG** Texto fixo contendo “0111”  
**Campo 02** **REC\_BRU\_NCUM\_TRIB\_MI** (Receita Bruta Não-Cumulativa -Tributada no Mercado Interno)  
**Campo 03 REC\_BRU\_ NCUM\_NT\_MI** (Receita Bruta Não-Cumulativa – Não Tributada no Mercado Interno (Vendas com suspensão, alíquota zero, isenção e sem incidência das contribuições)  
**Campo 04** **REC\_BRU\_ NCUM\_EXP** (Receita Bruta Não-Cumulativa – Exportação)  
**Campo 05** **REC\_BRU\_CUM** (Receita Bruta Cumulativa)  
**Campo 06** **REC\_BRU\_TOTAL** (Receita Bruta Total)  
  
Exemplo:  
No **campo 02** do **registro 0111** tenho um valor de 1000,00 e no **campo 04** um valor de 500,00, **o campo 06** será o totalizador então teremos o valor de 1500,00.  
Com esses campos podemos saber a proporcionalidade de cada receita com o seguinte calculo:  
**P=(VR/VT)\*100**

**VR** é o **valor da receita do registro 0111.**  
**VT** é o **campo 06**, **Valor total da Receita.**

Aplicando o exemplo acima ficaria

**P=** (1000/1500)\*100  
**P=**66,66%.

Assim temos a **proporcionalidade do campo 02.**

Com relação aos créditos essa proporcionalidade será aplicada entre os grupos do **registro M100.**

No **registro M100** temos **3 tipos de grupo**:

**GRUPO 100 - CÓDIGOS VINCULADOS À RECEITA TRIBUTADA NO MERCADO INTERNO**  
**GRUPO 200 - CÓDIGOS VINCULADOS À RECEITA NÃO TRIBUTADA NO MERCADO INTERNO**  
**GRUPO 300 - CÓDIGOS VINCULADOS À RECEITA DE EXPORTAÇÃO**

Cada grupo é subdividido em outros códigos para mais detalhes consultar a **tabela 4.3.6** do **EFD Contribuições**.  
Para a geração dos créditos é informada a **CST** de entrada de **PIS/COFINS** e essa **CST** está vinculada a um **grupo de credito** ou mais de 1. Conforme abaixo:  
  
**CST 50** é exclusiva do **grupo 100**, **CST 51** é exclusiva do **grupo 200** e **CST 52** exclusiva do **grupo 300**  
**CST  53 a 56** pertencem aos **grupos 100, 200, 300**.

Os **CSTs** que possuem mais de um grupo são utilizadas no rateio proporcional as outros **CSTs** que são exclusivas a um grupo não sofrem o **rateio**.

Utilizando o exemplo acima de receita e considerando uma nota um credito de 1000,00 vinculada a **CST** **56** (lembrando que a **CST 56 pertence aos 3 grupos de credito**) o rateio dos credito ficaria dessa forma.

Seriam geradas 2 linhas para o **registro M100** uma para cada grupo conforme abaixo.

**M100|1|101|**  
**M100|1|301|**  
  
Como temos receita apenas no **campo 02 e 04** os valores ficariam dessa forma:

M100|1|101|666,66(o valor seria os 1000 da entrada aplicando os 66,66 % da proporcionalidade do **campo 02**)  
M100|1|301|333,33(o valor seria os 1000 da entrada aplicando os 33,33 % da proporcionalidade do **campo 02**)

O **grupo 201** não foi gerado pois eu não tenho receita para o campo 03 do **registro 0111**.

Com o mesmo exemplo utilizado, incluindo mais uma nota de credito de 1000,00 reais com a **CST 50** o registro **M100** ficariam conforme abaixo:

M100|1|101|1666,66 (Foi acrescentado o valor total do credito da segunda nota, pois o **CST 50 é exclusiva para o grupo 100**.)  
M100|1|301|333,33

Importante:  
Por padrão o valor do **ICMS ST** e **IPI** são considerado na composição da **Receita Bruta do 0111**, para que o **ICMS ST** seja **desconsiderado** do total da Receita Bruta, deverá informar **.T.**no parâmetro **MV\_DSTRB** e para que o **IPI** seja **desconsiderado** do total da **Receita Bruta**, deverá informar **.T.**  no parâmetro **MV\_DIPIRB**.

**O Registro 0111**, não é gerado quando o tipo de regime for **exclusivamente Cumulativo**, e o **campo 05 REC\_BRU\_CUM** é gerado zerado quando o regime for **exclusivamente Não Cumulativo**.  
**São consideradas como Receitas as Notas de Saídas que tiverem os seguintes CFOPs:**

**Estadual:**  
5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354,5355,5356,5357,5359,5401,5402,5403,5405,5651,5652, 5653,5654,5655,5656.

**Interestadual:**  
6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302,6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359,6401,6402,6403,6404,6501,6502,6651,6652,6653,6654, 6655,6656.

**Exterior:**  
7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.

Se o**CFOP da NF de saída**, **não constar na relação acima**, informe no parâmetro **MV\_CFAREC**.  
Exemplo de preenchimento do parâmetro:  
**MV\_CFAREC = 5925,6933,5933**

Importante:  
Foi criado o **Ponto de Entrada SPDRECBRUT** que possibilita ao cliente informar valores de **Receita Bruta Cumulativa, Receita Bruta Não Cumulativa – não tributada e receita bruta não cumulativa – tributada,** para mais detalhes consulte o **TDN**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=706917512>

Caso a operação lançada através da **rotina Demais Docs. PIS COF. (FISA048) tabela Demais Docs. PIS COFINS (CF8)** não tenha que ser considerada no **Registro 0111**, informe a **opção 2-Não no campo Rec. Bruta (CF8\_RECBRU)**, desta forma o valor da operação não será considerado neste registro.  
Se este campo estiver com **opção 1-Sim ou vazio** os valores serão considerados no **Registro 0111** normalmente.

As **Notas Fiscais de Serviços** que configuram Receita serão sempre consideradas no **Registro 0111**, independente do tratamento de CFOP já citados para considerar ou não valores no **Registro 0111**.

**Método de Apropriação Direta.**

Nesse caso **não temos o registro 0111** para calcular a proporcionalidade das receitas pois a proporcionalidade do rateio é indicada diretamente no parâmetro **MV\_PERCAPD**.

No parâmetro temos 3 campos dentro de chaves conforme abaixo  
**{00,00,00}**.

**1º Campo receita tributada no mercado interno**  
**2º Campo receita não tributada no mercado interno**  
**3º Campo receita de exportação.**

**A somatória dos 3 campos tem que ser 100%**.  
Um exemplo utilizando esse rateio:  
Parâmetro **MV\_PERCAPD** preenchido dessa forma {50,50,00}:  
  
Considerando uma nota de entrada no valor de 1000,00 utilizando a **CST 56** o **registro M100** ficaria conforme abaixo:

M100|1|101|500,00 (Porcentagem de 50% conforme informado no parâmetro)  
M100|1|201|500,00 (Porcentagem de 50% conforme indicado pelo parâmetro)

O **grupo 300** não será gerado, pois no parâmetro não foi informado porcentagem para exportação.  
O restante dos cálculos permanecerá da mesma forma do rateio proporcional.

Utilização dos créditos entre **regime Cumulativo** e **regime Não Cumulativo.**  
  
Quando o cliente pertence ao **regime misto** de tributação (**Cumulativo** e **Não Cumulativo**), antes da aplicação dos métodos de rateio (**apropriação direta** ou **rateio proporcional**) é necessário verificar a **proporção dos créditos que está passível de apropriação**.

No **regime Cumulativo** não existe a apropriação de credito, então caso exista **Receitas** **Cumulativas,** a proporcionalidade referente a essa receita, indicara o valor de créditos que não serão apropriados.

Exemplo:

Voltando a estrutura do **registro 0111**.

O **campo 05** refere-se a **receitas no regime Cumulativo,** então para calcularmos o quanto de crédito poderemos apropriar será com base no cálculo abaixo:  
**PNC=(VRNC/VT)\*100**

**PNC** é aplicado ao **total de credito**

Onde, **VRCN** é a **soma dos campos 02, 03 e 04 do registro 0111** e o **VT** é o **campo 06** do **registro 0111** e **PNC** percentual **Não Cumulativo.**

Exemplo:  
**Campo 02 do registro 0111** = 200,00  
**Campo 03 do registro 0111** = 300,00  
**Campo 05 do registro 0111** = 500,00  
**Campo 06 do registro 0111** =1000  
  
Aplicando a fórmula acima temos o seguinte resultado:

**PNC=**(500/1000)\*100  
**PNC=**50%

Com o percentual do **regime Não Cumulativo,** é possível calcular os créditos para apropriação.  
Considerando uma nota e compra no valor de 1000,00 utilizando a **CST 56**, pode-se apropriar dos 1000,00, pois é necessário excluir a parte da **receita Cumulativa**, assim será possível a apropriação apenas de 500,00 já que o percentual **Não Cumulativo** é de 50%.

Nesse cenário o **registro M100** ficaria da seguinte forma.

M100|1|101|200,00 (considerando rateio proporcional)  
M100|1|201|300,00 (considerando rateio proporciona)

Para o **rateio proporcional** é considerado apenas as **receitas Não Cumulativas** para o cálculo, então o **total da receita** **não pode estar incluso o valor Cumulativo**.  
  
Importante:  
Foi removida a opção **Método de Apropriação de Créditos Comuns**, pois como o **ERP** trata somente **Apropriação por Rateio Proporcional**, o arquivo é gerado com a opção 2 no **campo 04 COD\_TIPO\_CONT** do **registro 0110**.  
  
Links:

[Cross Segmentos - Backoffice Protheus - FIS - Como gerar o Registro 0110 do EFD Contribuições.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7629425846423-Cross-Segmentos-Backoffice-Protheus-FIS-Como-gerar-o-Registro-0110-do-EFD-Contribui%C3%A7%C3%B5es-?source=search)  
  
Apuração EFD Contribuições:   
<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>  
  
Arquivo EFD Contribuições:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=212895074>
