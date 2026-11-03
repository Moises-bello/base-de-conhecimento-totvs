---
article_id: 360027787971
category: Escrita Fiscal - Impostos - ICMS
content_hash: c828c3875d27a57e51b3c7c120ad123102f2a41ddae7539a5c66e08c06530200
fetched_at: '2026-06-28T22:39:24.399908+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o
  ICMS ST por meio de Exceção Fiscal?
type: support-article
updated_at: '2021-07-20T14:22:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027787971-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-ICMS-ST-por-meio-de-Exce%C3%A7%C3%A3o-Fiscal
---

**Dúvida**

Como configurar o ICMS ST por meio de Exceção Fiscal?

**Ambiente**

Protheus  – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

É aconselhável o uso de Exceção Fiscal quando o mesmo produto possui mais de uma margem de Lucro em diferentes estados.

**Grupo de Tributação** - Deve ser criado um grupo de tributação na tabela 21 do módulo Configurador;

**Estado** - Deve ser criada uma linha para cada Estado:  
  
Em operações de Entrada: Considerar sempre o estado de **Origem** da mercadoria;  
Em operações de Saída: Considerar sempre o estado de **Destino** da mercadoria;

**Tipo** - Tipo de cliente no qual aplica-se a regra;

**Margem Lucro** - Margem de lucro a ser considerada no produto;

**GRP. Cli/For** - Somente deve ser preenchido caso a regra não se aplique a todos os clientes do Estado e tipo de cliente selecionado;

**Al. ICMS Dest**. - Informe a alíquota do ICMS-ST, caso não seja a padrão. Por padrão o Sistema considera a alíquota interna do Estado de destino da operação, verificando no parâmetro MV\_ESTICM.

**Origem:**  
**Apenas para as notas fiscais de entrada**, esse campo irá indicar como o sistema deve se comportar no momento de selecionar a exceção fiscal. O padrão do sistema é buscar a exceção pela UF de destino da mercadoria (no caso das entradas, a UF a ser cadastrada deve ser a mesma do contribuinte, ou seja, a mesma informada no MV\_ESTADO).

Esse campo poderá mudar a lógica de composição da exceção, considerando a UF do remetente da mercadoria, ou seja, a UF do fornecedor. Portanto, utilize:

1=Destino, para que a UF a ser selecionada na exceção fiscal das notas de entrada seja a do destino da mercadoria (MV\_ESTADO)

2=Origem, para que a UF a ser selecionada na exceção fiscal das notas

de entrada seja a da origem da  mercadoria (cadastro do fornecedor).

Os demais campos somente devem ser preenchidos caso a regra não esteja no padrão.

Para que seja calculado o ICMS-ST o tipo do cliente deve estar contido no parâmetro **MV\_TPSOLCF.**

A TES deve ser configurada com os campos **MKP ICM Comp. = Não**, e o campo **Marg Solid = Configuração.**

Caso a Exceção Fiscal não funcione, verifique o tamanho dos campos abaixo:

F7\_GRTRIB = CARACTER, 6

F7\_GRPCLI = CARACTER, 3

A1\_GRPTRIB = CARACTER, 3

A2\_GRPTRIB = CARACTER, 3

B1\_GRTRIB = CARACTER, 6

Se o tamanho de algum destes campos estiver diferente do indicado, a exceção não funciona corretamente, pois como existe amarração entre os campos, eles devem possuir o mesmo tamanho.
