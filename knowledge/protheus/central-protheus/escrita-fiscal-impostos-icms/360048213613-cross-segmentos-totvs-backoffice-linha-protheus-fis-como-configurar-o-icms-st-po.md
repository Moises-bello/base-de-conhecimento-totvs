---
article_id: 360048213613
category: Escrita Fiscal - Impostos - ICMS
content_hash: 7899768bd548e78f8af5e03f15bab0b2181556b168a409e0e824a2a36ee9ff51
fetched_at: '2026-06-28T22:39:24.396006+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o
  ICMS ST por exceção fiscal ? '
type: support-article
updated_at: '2021-07-20T13:17:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048213613-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-ICMS-ST-por-exce%C3%A7%C3%A3o-fiscal
---

**Dúvida** **MP - FIS - Como configurar o ICMS ST por exceção fiscal ?**  
   
 **Ambiente**Protheus - Protheus - Fiscal  – A partir da versão 11.80  
  
**Solução**

É aconselhável o uso de Exceção Fiscal quando o mesmo produto possui mais de uma margem de Lucro em diferentes estados.

**Grupo de Tributação**- Deve ser criado um grupo de tributação na tabela 21 do módulo Configurador;

Exceção fiscal - SF7

**Estado** - Deve ser criada uma linha para cada Estado, considerando sempre o Estado de destino da mercadoria;

**Tipo -**Tipo de cliente no qual aplica-se a regra;

**Margem Lucro**- Margem de lucro a ser considerada no produto;

**GRP. Cli/For**- Somente deve ser preenchido caso a regra não se aplique a todos os clientes do Estado e tipo de cliente selecionado;

**Al. ICMS Dest**. - Informe a alíquota do ICMS-ST, caso não seja a padrão. Por padrão o Sistema considera a alíquota interna do Estado de destino da operação, verificando no parâmetro **MV\_ESTICM**.

**UF busca** = origem ( entradas ) destino ( saídas )

Os demais campos somente devem ser preenchidos caso a regra não esteja no padrão.

Para que seja calculado o ICMS-ST o tipo do cliente deve estar contido no parâmetro **MV\_TPSOLCF**.

A TES deve ser configurada com os campos **MKP ICM Comp.** = **Não,**eo campo **Marg Solid**= **Configuração**.

Caso a Exceção Fiscal não funcione, verifique o tamanho dos campos abaixo:

**F7\_GRTRIB**= CARACTER, 6

**F7\_GRPCLI**= CARACTER, 3

**A1\_GRPTRIB**= CARACTER, 3

**A2\_GRPTRIB =**CARACTER, 3

**B1\_GRTRIB**= CARACTER, 6

Se o tamanho de algum destes campos estiver diferente do indicado, a exceção não funciona corretamente, pois como existe amarração entre os campos, eles devem possuir o mesmo tamanho.

**Observação**:

O sistema considera no padrão a UF da Exceção Fiscal como destino, sendo assim a entrada da NF deve ser preenchida com o Estado no qual a empresa está localizada.**(MV\_ESTADO).**
