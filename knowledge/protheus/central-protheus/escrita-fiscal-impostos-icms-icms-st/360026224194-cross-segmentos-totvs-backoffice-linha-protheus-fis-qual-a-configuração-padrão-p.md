---
article_id: 360026224194
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 4bab7a478361d02dca8b9e33a4e4b6ed1c8263e0a7eb3b8b82fe7f4002c2b5ac
fetched_at: '2026-06-28T22:39:20.513946+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual a configuração
  Padrão para o cálculo do ICMS-ST, Margem de Lucro no produto ou exceção fiscal?
type: support-article
updated_at: '2021-12-10T14:59:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026224194-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-Padr%C3%A3o-para-o-c%C3%A1lculo-do-ICMS-ST-Margem-de-Lucro-no-produto-ou-exce%C3%A7%C3%A3o-fiscal
---

**Dúvida**Qual a configuração Padrão para o cálculo do ICMS-ST, Margem de Lucro no produto ou exceção fiscal?  
   
 **Ambiente**Protheus - Fiscal - A partir da versão 11.80  
  
**Solução**Configuração padrão do ICMS-ST:

***Cliente:***

**Tipo (A1\_TIPO)** = Este campo têm relação com o parâmetro **MV\_TPSOLCF**,onde são informados os tipos de cliente/fornecedores que possuem cálculo de ICMS Solidário.

 ***Parâmetro:***

**MV\_TPSOLCF**– Indica quais os tipos de cliente devem ser considerados para cálculo do ICMS-ST. Lembrando que é realizado o  vínculo com o campo **Tipo (A1\_TIPO).**

**MV\_MKPICPT**- Indica se há margem de lucro nas operações de venda para o consumidor final.            

***TES:***

**Mkp ICM Comp. (F4\_MKPCMP)** = **Não;**

**Marg. Solid. (F4\_MKPSOL)** = **Configuração.**

Obrigatoriamente a Margem de lucro deve ser configurada no cadastro do produto ou na exceção fiscal:

***Produto:***

**Solid. Saída (B1\_PICMRET)** - informe o MVA do produto para saída;

**Solid. Entr. (B1\_PICMENT)** - informe o MVA do produto para entrada.

Ou

## Exceção Fiscal:

É aconselhável o uso de Exceção Fiscal quando o mesmo produto possui mais de uma margem de Lucro em diferentes estados.

**Grupo de Tributação**- Deve ser criado um grupo de tributação na tabela 21 do módulo Configurador;

**Estado** - Deve ser criada uma linha para cada Estado, considerando sempre o Estado de destino da mercadoria;

**Tipo -**Tipo de cliente no qual aplica-se a regra;

**Margem Lucro**- Margem de lucro a ser considerada no produto;

**GRP. Cli/For**- Somente deve ser preenchido caso a regra não se aplique a todos os clientes do Estado e tipo de cliente selecionado;

**Al. ICMS Dest**. - Informe a alíquota do ICMS-ST, caso não seja a padrão. Por padrão o Sistema considera a alíquota interna do Estado de destino da operação, verificando no parâmetro **MV\_ESTICM**.

Os demais campos somente devem ser preenchidos caso a regra não esteja no padrão.

Para que seja calculado o ICMS-ST o tipo do cliente deve estar contido no parâmetro **MV\_TPSOLCF**.

A TES deve ser configurada com os campos **MKP ICM Comp.** = **Não,**eo campo **Marg Solid**= **Configuração**.

Caso a Exceção Fiscal não funcione, verifique o tamanho dos campos abaixo:

**F7\_GRTRIB**= CARACTER, 6

**F7\_GRPCLI**= CARACTER, 3

**A1\_GRPTRIB**= CARACTER, 3

**A2\_GRPTRIB =**CARACTER, 3

**B1\_GRTRIB**= CARACTER, 6

Se o tamanho de algum detes campos estiver diferente do indicado, a exceção não funciona corretamente, pois como existe amarração entre os campos, eles devem possuir o mesmo tamanho.

**Observação**:

O sistema considera no padrão a UF da Exceção Fiscal como destino, sendo assim a entrada da NF deve ser preenchida com o Estado no qual a empresa está localizada.**(MV\_ESTADO)**
