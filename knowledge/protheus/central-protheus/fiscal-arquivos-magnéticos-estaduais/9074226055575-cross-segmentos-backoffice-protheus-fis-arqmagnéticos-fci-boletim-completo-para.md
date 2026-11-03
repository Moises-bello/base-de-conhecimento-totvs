---
article_id: 9074226055575
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 8266c391dbaea2d952f64ba5a701f474bff97c8cc8714adbc7e8fb366674a44b
fetched_at: '2026-06-28T22:42:10.892786+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - FCI Boletim
  completo para a geração do FCI.
type: support-article
updated_at: '2024-10-16T14:20:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9074226055575-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FCI-Boletim-completo-para-a-gera%C3%A7%C3%A3o-do-FCI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27109464525079) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**- Como calcular a Parcela Importada, as vendas Interestaduais e o conteúdo/faixa de Importação do FCI? - Como processar o FCI e gerar o arquivo txt?  
- Importação Arquivo de retorno com o código de FCI, utilização código FCI no mês e em outros meses.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**O método 3 (**MV\_FCICALC = 3**) é o mais indicado. Neste caso, o mais recomendado é o método de cálculo 3, pois ele irá buscar suas notas fiscais de entrada e saída automaticamente.  
Nesse caso, o sistema irá pegar do campo **A8\_VLRVI**. A tabela **SA8** será alimentada com os valores das matérias primas encontradas na sua **SD3** utilizadas na produção do produto final.  
A tabela **SA8** irá gerar uma linha para cada matéria prima e para cada produto final e irá apresentar o valor da parcela importada calculado para cada produto.

**Observação: O Método 2 (MV\_FCICALC = 2) foi descontinuado.**  
  
Os valores da tabela **CFD** só serão atualizados se houver mudança na origem do produto, pois se o valor do conteúdo de importação alterar, porém permanecer na mesma faixa, o sistema não irá atualizar os valores.

O sistema busca o conteúdo do parâmetro **MV\_FCICALC = 3** para realizar os cálculos abaixo.  
Neste método, cada produção tem seu **Valor de Importação** calculado conforme as requisições realizadas, de acordo com a matéria-prima utilizada em cada uma delas. O valor de importação apurado para o produto acabado é obtido pela média ponderada do valor obtido para cada ordem de produção e armazenada na tabela **SA8**. O valor de importação das matérias primas é calculado sobre a média ponderada das Notas Fiscais de entrada e também são armazenados na tabela **SA8**.  
  
**CÁLCULO PARCELA IMPORTADA:** Fórmula de Cálculo

A **Parcela Importada** será o valor da mercadoria mais os valores de frete e seguro, retirado os impostos que possam ter sido somados ao total do documento. Dependendo do campo **F4\_AGREG** a fórmula irá ser alterado. Abaixo um exemplo de cálculo quando o campo **F4\_AGREG = S**:  
**(D1\_TOTAL+D1\_VALFRE+D1\_SEGURO) - (D1\_II)**

De acordo com o **artigo 6º** da **Portaria CAT 64/2013**, os valores da **parcela importada** deverão ser calculados mensalmente, utilizando-se os valores unitários, que serão calculados pela média aritmética ponderada, praticados no penúltimo período de apuração. Para cálculo do Conteúdo de Importação de Outubro/13 deverão ser tomados como base os valores praticados em Agosto/13 (penúltimo mês).

EXEMPLO 01:

![](https://totvssuporte.zendesk.com/attachments/token/cMKGLKupnQgWS4pHAmV1SxTky/?name=inline-1866371714.png)  
  
São utilizadas 1,9 toneladas do produto importado para a produção de cada unidade de mercadoria industrializada.  
A média ponderada em relação às quantidades poderá então ser calculada: Média ponderada das importações = (1500x1+750x4)/(1+4)=R$ 900,00precisamos saber quanto há de importado (R$) em uma unidade de mercadoria vendida.  
O valor da parcela importada deste produto será de:  
Parcela importada= 900 x 1,9=R$ 1.710,00EXEMPLO 02:Cálculo efetuado quando possui matéria prima importada e nacional

Indústria produz Produto Final C (PC) com a seguinte composição:  
Insumo B (IB) + Mercadoria A (MA) = Produto Final C (PC)  
  
Sendo:   
Insumo B: Importado diretamente do exterior pelo estabelecimento B. Valor aduaneiro = R$ 30,00.   
Mercadoria A: Adquirida no mercado nacional. CST = 5 (CI menor ou igual a 40%) = R$ 0,00.  
Produto Final C: Produto que será fabricado na empresa para comercialização. Será utilizado apenas um IB e um MA para a produção do PC.

A média ponderada em relação às quantidades poderá então ser calculada:  
Média ponderada das importações (IB) = (30\*1)/(1)=R$ 30,00

Com o valor das importações encontrado, iremos calcular o valor da parcela importada. Devido a MA não possuir conteúdo de importação, o Produto Final C ficará com a parcela importada igual ao Insumo B:  
O valor da parcela importada deste produto será de:  
Parcela importada= 30 x 1=R$ 30,00

Quando **MV\_FCICALC = 3**, o sistema irá gravar na tabela **SA8** os valores de importação de cada matéria prima e de seu produto final.  
Na tabela **SA8**: **A8\_PROCOM = C**, indica que o produto é um insumo.  
**A8\_PROCOM = P**, indica que o produto foi produzido.  
O valor importado calculado para o produto final será gravado também no campo **CFD\_VPARIM**.

**CÁLCULO VENDA INTERESTADUAL:** Fórmula de Cálculo

**D2\_VALBRUT - (D2\_ICMSRET + D2\_VALICM + D2\_VALIPI)**  
  
Serão consideradas todas as vendas interestaduais que:  
•Estiverem com o conteúdo do campo **D2\_CLASFIS** informado no parâmetro **MV\_FCICL**  
•Estiverem com o conteúdo do campo **D2\_CF** informado no parâmetro **MV\_FCIVE** ou **MV\_FCIVI**  
•Estiverem com o conteúdo do campo **D2\_PICM** informado no parâmetro **MV\_FCIALIQ**  
•Caso não seja encontrado **Venda Interestadual** (**CFOP** iniciado por 6) no período informado na rotina **FISA061**, o sistema irá buscar as **vendas internas** (**CFOP** iniciado por 5).  
  
Para **Produtos Novos**, o sistema não irá buscar vendas, desta forma será necessário configurar os parâmetros:  
•**MV\_FCINWPR**: Preencher com o mesmo conteúdo do parâmetro **MV\_ESTADO**  
•**MV\_FCIPRV**: Define de qual campo do sistema será informado o preço estimado de venda. Opções Válidas: **1 = B1\_PRV1, 2 = B5\_FCIPRV, 3 = BZ\_FCIPRV**  
•Se tratando de produtos novos, informar no campo apontado no parâmetro **MV\_FCIPRV** o preço unitário da venda interestadual, retirando o **ICMS**, **IPI** e **ICMS ST**.

Link Documentação:

[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Cálculo do FCI para Produtos Novos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027019831-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-C%C3%A1lculo-do-FCI-para-Produtos-Novos?source=search)  
  
De acordo com o **artigo 6º da Portaria CAT 64/2013**, os valores das **vendas interestaduais** deverão ser calculados mensalmente, utilizando-se os valores unitários, que serão calculados pela média aritmética ponderada, praticados no penúltimo período de apuração. Para cálculo do Conteúdo de Importação de Outubro/13 deverão ser tomados como base os valores praticados em Agosto/13 (penúltimo mês)

*EXEMPLO 01*:![](https://totvssuporte.zendesk.com/attachments/token/32rlwSexEV3AUtEZb4hzagknY/?name=inline-1397396553.png)  
  
São utilizadas 1,9 toneladas do produto importado para a produção de cada unidade de mercadoria industrializada.  
A média ponderada em relação às quantidades poderá então ser calculada:  
Média ponderada das saídas: = (2.850,00 x1+3.225,50x1)/ (1+1)=R$ 3.037,75, neste caso o valor unitário das saídas interestaduais será igual a R$ 3037,75.   
O valor da venda interestadual será gravado no campo **CFD\_VSAIIE**. O sistema irá gravar a tabela **CFD**: **CFD\_PERVEN** = mês informado na *wizard*.  
**CFD\_PERCAL** = 2 meses subsequentes ao informado na *wizard*.  
Se tratando de produtos novos os campos **CFD\_PERVEN** e **CFD\_PERCAL** serão gravados com a data que está na *wizard*

**CONTEÚDO DO CONTEÚDO/ FAIXA DE IMPORTAÇÃO**: Fórmula de Cálculo

O conteúdo de Importação será utilizado para definição da Origem da Mercadoria do Produto Acabado. A fórmula de cálculo do conteúdo de Importação é esta:

**CI = (Parcela Importada / Valor das saídas interestaduais) \* 100**  
A Origem da Mercadoria será utilizada para definir a alíquota de ICMS utilizada nas próximas vendas

EXEMPLO 01:  
Cálculo do CI:  
Para efetuarmos o cálculo do CI, precisamos saber quanto há de importado (R$) em uma unidade de mercadoria vendida.  
O exemplo informa que são utilizadas 1,9 ton do produto importado para a produção de uma unidade de mercadoria industrializada.  
  
![](https://totvssuporte.zendesk.com/attachments/token/sxOInY6q34VCWzde7Iw4qunAt/?name=inline876553250.png)

São utilizadas 1,9 toneladas do produto importado para a produção de cada unidade de mercadoria industrializada.  
Parcela importada= 900 x 1,9=R$ 1.710,00Valor das Saídas IE: = (2.850,00 x1+3.225,50x1)/(1+1)=R$ 3.037,75Conteúdo de Importação= 1.710,00/3.037,75=0,5629 \* 100Conteúdo de Importação= 56,29%EXEMPLO 02:

Cálculo efetuado quando possui matéria prima importada e nacional

Indústria produz Produto Final C (PC) com a seguinte composição:  
Insumo B (IB) + Mercadoria A (MA) = Produto Final C (PC)Sendo:  
Insumo B: Importado diretamente do exterior pelo estabelecimento B. Valor aduaneiro = R$ 30,00.Mercadoria A: Adquirida no mercado nacional. CST = 5 (CI menor ou igual a 40%) = R$ 0,00.Produto Final C: Produto que será fabricado na empresa para comercialização. Será utilizado apenas um IB e um MA para a produção do PC. O valor comercializado retirando ICMS e IPI do Produto Final PC = R$ 100,00Valor da parcela importada(IB) = (30\*1)/(1)=R$ 30,00Valor da Saída IE (PC) = R$100,00Conteúdo de Importação= 30/100=0,3 \* 100Conteúdo de Importação= 30%>>> O valor do conteúdo importado é gravado no campo **CFD\_CONIMP**, o conteúdo deste campo irá definir o conteúdo do campo **CFD\_ORIGEM**, o conteúdo de Importação não deve ultrapassar 100%.  
Com o Conteúdo de Importação em mãos, podemos definir qual a Origem da Mercadoria.

**Origem = 0**

Quando o conteúdo de importação igual a 0 **(CFD\_CONIMP = 0)**, a origem da mercadoria também será 0. Quando a Origem do produto igual a 0, não haverá código de FCI e o cliente não irá gerar o arquivo.  
  
**Origem = 3**

Quando o conteúdo de importação for **maior que 40% e menor ou igual a 70% (CFD\_CONIMP >40 e CFD\_CONIMP <=70),** a origem da Mercadoria será 3. Neste cenário, o campo **CFD\_ORIGEM será alimentado com 3** e o cliente deverá entregar o arquivo para a receita para receber o código da FCI. **As vendas futuras serão realizadas com ICMS a 4%.**

**Origem = 5**

Quando o conteúdo de importação **for menor ou igual a 40% (CFD\_CONIMP <=40)**, a origem da Mercadoria será 5. Neste cenário, o campo **CFD\_ORIGEM será alimentado com 5 e** o cliente deverá entregar o arquivo para a receita para receber o código da FCI. **As vendas futuras não podem ser realizadas com 4% de ICMS.**

**Origem = 8**

Quando o conteúdo de importação **for maior que 70% (CFD\_CONIMP >70)**, a origem da Mercadoria será 8. Neste cenário, o campo **CFD\_ORIGEM será alimentado com 8** e o cliente deverá entregar o arquivo para a receita para receber o código da FCI. **As vendas futuras serão realizadas com ICMS a 4%.**

**Origem = 1/2**

**Essas origens não são gravadas na tabela CFD em nenhum cenário. As origens 1 e 2 indicam que o produto é 100% importado e normalmente são utilizadas na compra das matérias primas.**

**APURAÇÃO FCI**

No **Protheus**, a rotina da **FCI** é a **FISA061**. Esta rotina é responsável por apurar, gerar o arquivo e importar os códigos da FCI enviados pelo Governo.  
A apuração dentro do sistema deve ser feita mensalmente para produtos já vendidos anteriormente ou em caso de produtos novos, a apuração deverá ser realizada antes de efetuar a primeira venda. A apuração irá gravar os valores nas tabelas **SA8** e **CFD** para todos os produtos que ainda não foram apurados e copiar os dados dos períodos anteriores para utilização nos períodos seguintes **ARQUIVO txt.**Esta opção será utilizada para geração do arquivo .txt que será exportado para a receita federal. **Somente serão considerados os produtos com conteúdo de importação maior que 0 e que não possuam código de FCI (CFD\_FCICOD = “ “)**

**IMPORTAÇÃO ARQUIVO DE RETORNO COM CÓDIGO DE FCI**  
Para importar o arquivo de retorno com o código de **FCI**, é necessário acessar a Rotina da **FCI (FISA061)** e utilizar o **botão IMPORTAR**.  
Esta opção irá importar os arquivos .txt enviados pelo Governo para gravação do campo **CFD\_FCICOD**. É importante que o período informado na *wizard* da rotina seja correspondente ao arquivo enviado.  
  
**UTILIZAÇÃO CÓDIGO FCI**No **Protheus**, o código da **FCI** ficará gravado na tabela **CFD (CFD\_FCICOD)**. Ao realizar um pedido de venda, o sistema irá verificar a data de emissão deste pedido (Tabela **SC5**) e irá buscar o código da **FCI** da tabela **CFD** para o mesmo mês **(CFD\_PERCAL)** que o pedido está sendo emitido.

É regra do sistema para buscar o código da **FCI** no pedido de venda que exista uma linha na tabela **CFD** com o campo **CFD\_PERCAL** com o mesmo período da emissão do pedido.  
  
Link Documentação:

[Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como carregar o código de FCI automaticamente no Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497451-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-carregar-o-c%C3%B3digo-de-FCI-automaticamente-no-Pedido-de-Vendas?source=search)

**CÓDIGO DA FCI EM OUTROS MESES**

Devido a esta necessidade de informar o código da **FCI** em todas as vendas, é necessário que o cliente execute a apuração da **FCI** (**FISA061**) mensalmente para que o sistema copie os dados da **CFD** dos períodos anteriores para o período atual.

Não será necessário gerar um novo arquivo para estes meses seguintes, o sistema irá copiar a linha inteira da **CFD**, alterando apenas os campos **CFD\_PERVEN** e **CFD\_PERCAL**. Somente será gerada uma nova linha para o produto na tabela **CFD** se o conteúdo de importação alterar a origem.   
Exemplo: um produto foi calculado com origem 5 no mês 07/2022, **o código de FCI deste produto será copiado nos meses seguintes até que a origem seja alterada para 3, 8 ou 0.**

Link Boletim Técnico:  
<https://tdn.totvs.com/display/public/PROT/ARQ0079_-_Funcionamento_FCI>

Mais Informações:

<https://tdn.totvs.com/pages/releaseview.action?pageId=632836444>
