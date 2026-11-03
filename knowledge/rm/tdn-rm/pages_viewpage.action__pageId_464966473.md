---
content_hash: 19b37fc4048b928302f6153ab1f5318302585275e4ae0db1fca2495d511c1fd4
fetched_at: '2026-06-29T00:10:15.397779+00:00'
page_id: '464966473'
product: rm
source: tdn-rm
title: Como validar os erros 724 e 726 apresentados no S-1210?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=464966473
version: 7
---

Ao realizar a transmissão do S-1210, podem ocorrer o retorno do RET com as seguintes mensagens de erro:

***"Código do Erro: 724. Descrição: Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento. Ação Sugerida:Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202 ou S-1206 no campo quot;Identificador de Recibo de Pagamentoquot;, obedecendo a relação:.Se Tipo de Pagamento = [1], em S-1200;.Se Tipo de Pagamento = [5], em S-1202;.Se Tipo de Pagamento = [7], em S-1206."***

***"Código do Erro: 726. Descrição**:**Não foi localizado um evento de rescisão contratual para o trabalhador com mesmo recibo de pagamento. Ação Sugerida: Deve ser um identificador de recibo de pagamento atribuído pela empresa em um dos eventos rescisórios (S-2299 ou S-2399), no campo quot;identificador de recibo de pagamentoquot;..Se Tipo de Pagamento = [2] deve ser um valor atribuído pela empresa em S-2299;.Se Tipo de Pagamento = [3], deve ser um valor atribuído pela empresa em S-2399."***

Observação

*Como premissa, devemos entender que:*

***S-1200** considera as verbas lançadas na competência relacionada ao período de apuração a ser gerado. Exemplo: Período de apuração 1/2019 - O S-1200 irá gerar todas as verbas lançadas na competência de janeiro/2019 (envelope, distribuição SEFIP, recibo de férias).*

***S-1210** considera as verbas cuja data de pagamento está compreendida dentro do período de apuração a ser gerado, independentemente da competência que se encontra. Exemplo: Período de apuração 1/2019 - O S-1210 irá considerar todas as verbas cuja data de pagamento esteja dentro do mês de janeiro/2019, independente em qual competência esteja.*

Seguem as validações a serem feitas no intuito de sanar o erro apresentado:

ValidaçõesRegime de COMPETÊNCIA

**• Tipo de Pagamento**

Deve-se validar no XML (RM e TAF) se a TAG <tpPgto> (tipo de pagamento) está sendo gerada corretamente relacionando o evento de remuneração (S-1200, S-1202, S-2299, etc) conforme Layout do eSocial.

Exemplo - Tipo de Pagamento

**Exemplo:** Enviado a remuneração do funcionário no evento S-1200 da competência 03/2020. Tag <tpPgto> deverá ser levada com registro "1" (1 - Pagamento de remuneração, conforme apurado em {dmDev} do S-1200).

**S-1200 - Período de Apuração 03/2020**

**S-1210 - Período de Apuração 03/2020**

**• Período de pagamento**

Deve-se verificar se todas as verbas estão corretamente relacionadas ao <perRef> (mês de referência do pagamento) e ao <ideDmDev> (período de pagamento informado no envelope) informados no evento de remuneração em <perApur> (período de apuração) e <ideDmDev>.

Exemplo - Período de Pagamento

**Exemplo:** Funcionário desligado em 01/2019, tendo X verbas no período1 e Y no período 2 (data de pagamento dentro da competência de Jan/2019). No S-1210 do período de apuração 01/2019, devem constar o <perRef> 2019-01 e <ideDmDev> 1 e 2, com seus respectivos líquidos e demais informações. Os <ideDmDev> deverão corresponder aos mesmo enviados no evento de pagamento correspondente (neste exemplo, S-2299).

**S-2299 - Desligamento em 01/2019**

**S-1210 - Período de Apuração 01/2019**

**• Parametrizador**

Em casos de <tpPgto> relacionado ao evento S-2299, deve-se verificar também se a data preenchida no parametrizador do eSocial para não periódicos está correta.

**Atenção!** *A obrigatoriedade de envio sempre inicia-se no primeiro dia do mês informado no cronograma do governo. Não se deve confundir a data de disponibilização do ambiente do governo para recebimento dos dados com a data de início de obrigatoriedade.*

Exemplo - Parametrizador

***Exemplo:***  
*Obrigatoriedade dos eventos periódicos para empresas com faturamento menor que 78Mi*

*I*nício da Obrigatoriedade (que deve ser preenchida no parametrizador)*:*   
 *01/01/2019*  
*Disponibilização do RET para recebimento de dados:*   
 *10/01/2019*

**• TAG <nrRecArq>**

A TAG <nrRecArq> é preenchida pelo TAF com o número do recibo do arquivo que contém as informações da rescisão contratual que originou o pagamento. Assim, deve-se validar se o XML gerado pelo TAF apresenta corretamente esta informação.

Segue documento do TAF relacionado à este item: [Inconsistência no evento S-1210, não cria a TAG nrRecArq](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018331952-TAF-TAF-eSocial-S-1210-nrRecArq-Inconsist%C3%AAncia-no-evento-S-1210-n%C3%A3o-cria-a-TAG-nrRecArq-)

Exemplo - nrRecArq

**Exemplos**

No exemplo abaixo foi feito a demissão de um funcionário cujo data de demissão e data de pagamento foi em 01/03/2020 no período 1 do envelope. Como é de conhecimento prévio, para funcionários que possuem verbas rescisórias no mês o XML S-1210 será gerado da seguinte forma:

Tag <tpPgto> = 2 ( Rescisão )

Tag <ideDmDev> = 1 ( Período do envelope )

O código da ocorrência 723 e 726 é apresentado quando essas informações entre o S-2299 e S-1210 estão divergentes. Logo, o evento S-2299 deve ser gerado da seguinte forma:

Tag <ideDmDev> = 1 ( Período do envelope ) juntamente com as verbas de rescisão em seguida.

Para o código da ocorrência 723 e 724, demos seguir a mesma lógica diferenciando apenas a tag <tpPgto> que por se tratar de folha mensal, deve ser gerado com o valor igual a 1 (Folha Mensal). No exemplo a seguir utilizado as seguintes parametrizações:

Envelope de pagamento lançado no período 2 no envelope, com data de pagamento em 20/03/2020. Neste caso, o XML S-1210 deve ser gerado da seguinte forma:

Tag <tpPgto> = 2 ( Rescisão )

Tag <ideDmDev> = 1 ( Período do envelope )

Caso estas informações não estejam corretas entre o XML S-1200 e S-1210 será apresentado a mensagem de erro 723 e 724.

Regime de CAIXA

**• Mês de início da obrigatoriedade**

Neste caso deve-se verificar se a TAG <tpPgto> está com o tipo de pagamento"9 - Pagamento relativo a competências anteriores ao início de obrigatoriedade dos eventos periódicos para o contribuinte", visto que existem verbas no mês anterior com pagamento pro mês de início de vigência da obrigatoriedade.

***Exemplo:** Início de obrigatoriedade dos eventos Periódicos: 01/01/2019. Existem verbas lançadas em Dez/2018 (fora da obrigatoriedade) com data de pagamento em Jan/2019 (dentro da obrigatoriedade). Deve-se gerar o S-1210 com <tpPgto> como 9 (9 - Pagamento relativo a competências anteriores ao início de obrigatoriedade dos eventos periódicos para o contribuinte).*

Deve-se observar também se a TAG <dtPgto> (data de pagamento) está compreendida dentro do período de apuração selecionado para geração.

***Exemplo:** Lançamento das verbas em Dez/2018 com pagamento em 10/01/2019. Para o <perApur> (período de apuração) 2019-01 serão geradas as verbas com <dtPgto> (data de pagamento) 2019-01-10 relacionadas ao <perRef> (período de referência) 2018-12.*

**• Admissão dentro da obrigatoriedade**

O evento S-1210, para funcionários admitidos posteriormente ao início da obrigatoriedade dos eventos não periódicos, só será gerado no próximo período de apuração. Isto porque as verbas pagas no mês de admissão terão datas de pagamento para o próximo mês. Assim, para o período de apuração posterior ao da admissão, será gerado o S-1210 com <perRef> relacionado ao mês da admissão.

***Exemplo:** Admissão do funcionário: 10/01/2019. Verbas referentes à Janeiro pagas em Fevereiro. Para o período de apuração 01/2019 não será gerado S-1210 pois não existem verbas com pagamento dentro do período.*

**• Período de pagamento**

Deve-se verificar se todas as verbas estão corretamente relacionadas ao <perRef> (mês de referência do pagamento) e ao <ideDmDev> (período de pagamento informado no envelope) informados no evento de remuneração em <perApur> (período de apuração) e <ideDmDev>.

***Exemplo:** No período de apuração 1/2019 foram informadas X verbas no período 1 e Y no período 2 (pagamento em 02/2019). Essa movimentação será levada no S-1210 do período de apuração 2/2019, que deve constar o <perRef> 2019-1 e <ideDmDev> 1 e 2, com seus respectivos líquidos e demais informações.*

**• Parametrizador**

Em casos de <tpPgto> relacionado ao evento S-2299, deve-se verificar também se a data preenchida no parametrizador do eSocial para não periódicos está correta.

**Atenção!** *A obrigatoriedade de envio sempre inicia-se no primeiro dia do mês informado no cronograma do governo. Não se deve confundir a data de disponibilização do ambiente do governo para recebimento dos dados com a data de início de obrigatoriedade.*

***Exemplo:***  
*Obrigatoriedade dos eventos periódicos para empresas com faturamento menor que 78Mi*

*Início da Obrigatoriedade (que deve ser preenchida no parametrizador):*   
 *01/01/2019*  
*Disponibilização do RET para recebimento de dados:*   
 *10/01/2019*

**• TAG <nrRecArq>**

A TAG <nrRecArq> é preenchida pelo TAF com o número do recibo do arquivo que contém as informações da rescisão contratual que originou o pagamento. Assim, deve-se validar se o XML gerado pelo TAF apresenta corretamente esta informação.

Segue documento do TAF relacionado à este item: [Inconsistência no evento S-1210, não cria a TAG nrRecArq](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018331952-TAF-TAF-eSocial-S-1210-nrRecArq-Inconsist%C3%AAncia-no-evento-S-1210-n%C3%A3o-cria-a-TAG-nrRecArq-)

Trechos do Layout do S-1210

**- perApur**

**- dtPgto e tpPgto**

**- perRef e ideDmDev**

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.24 |
| 12.1.23 |
| 12.1.22 |
| 12.1.21 |

falsefalse

**Status:** Em andamento

false

**Data:**

false

**Autores:**

Joyce Rodrigues Nereu

Christian Ribeiro de Oliveira Soares
