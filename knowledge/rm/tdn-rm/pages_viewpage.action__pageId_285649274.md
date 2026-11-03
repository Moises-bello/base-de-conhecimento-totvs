---
content_hash: 230695e1f6dbeb7af86f6151692eb167bc1b5f15cdfb3ed8f5cdee22a5cbd1ef
fetched_at: '2026-06-29T00:08:38.356076+00:00'
page_id: '285649274'
product: rm
source: tdn-rm
title: "2.\tMódulo TIN – TOTVS Incorporação"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285649274
version: 1
---

**1.1.** **Cadastro do Cliente / Prospect**

 Criação dos campos a seguir que devem ser preenchidos pelo usuário no PVI e registrados também no TIN:

* NSS (Número do Seguro Social)
* CURP (Chave Única de Registro da População)
* RFC (Registro Federal do Contribuinte)

 Regla:

* + primeiro selecionar la primeira letra do primeiro sobenome:
  + luego la primera vocal del primer apellido, pero que no sea la primera letra
  + luego la primera letra del segundo apellido
  + luego la primera letra del primer nombre (si tiene dos o más se toma solo el primer nombre según acta de nacimiento)
  + luego se pone los dos últimos dígitos del año de nacimiento
  + luego en dos dígitos el mes de nacimiento
  + y luego en dos dígitos el día de nacimiento
  + Será necesario crear dos nuevos Status “En espera” y “Cancelado”. Para los dos status la propuesta de venta queda suspendida y pierde la reserva de la Subunidad.

**1.2.** **Cadastro de Subunidade**

Criação dos campos, abaixos que devem ser preenchidos pelo usuario ou via procesos TIN:

* Data DTU (DOCUMENTO TÉCNICO UNIFICADO): este documento é emitido pelo RUV que é o orgão responsável por liberar o Registro Unico de Vivienda.
* Data CVT (Certificado de Vivenda Terminada): este documento é emitido pela construtora, certificando que a subunidade pode ser entregue pois já está concluida. No Gupos Casitas a construtora é a propria empresa ou uma empresa do Grupo.
* Data DTC (Dictamen Técnico de Calidad): este documento é emitido pelo setor de qualidade do Grupo Casitas certifificando que a subunidade está dentro dos padrões de qualidades aceitos para a entrega.  Sem este documento a subunidade não pode ser entregue.

Permitir que todas as datas acima sejam informadas em Lote.

**1.3.** **Alteração da Tabela de Preço**

 Criação dos campos, abaixo que devem ser preenchidos pelo usuário ou via processo TIN:

* Valor Venal:  valor informado pelo usuário na formação de preço, mas que pode ser calculado via processo de geração de preço. Será utilizado no calculo do valor de Imposto no Simulador.
* Valor da Comissão:  campo informado pelo usuario. Permitir informar o valor ($) da comissão em lote para várias subunidades do mesmo modelo ou via fórmula (exceção).

Estes campos devem ser levados para o PVI, na proposta de venda e no simulador para INFONAVIT.

**1.4.** **Alteração do Processo de Comissão**

 O PVI deve enviar ao TIN o valor de Comissão já calculado, ou seja, a comissão deduzida de eventuais descontos e acrescida de possíveis bônus.

 As comissões podem ser agrupadas para que haja apenas um pagamento para o mesmo vendedor, num mesmo período. (ex: semanal ou mensal)

**1.5.** **Criação do processo de Adiantamento**

O PVI deve eviar ao TIN uma solcitação para gerar lançamentos financeiros de adiantamento, sem que tenha uma venda efetivada, ou seja será necessário criar um processo de suporte para adiantamento financiero da proposta de venda, para a geração de Títulos do TIPO RA (Recibo de Antecipação)

**1.6.** **Faturamento**

 A venda deve gerar um faturamento referente ao valor da venda.

 Para casos de **FIDEICOMISO** será necessário emitir o faturamento no valor a que compete apenas ao Grupo Casitas.

 Para que o sistema saiba que parte compete a cada parceiro do **FIDEICOMISO** deve ser criado uma tabela que identifique o valor de cada entidade parceira na venda de cada subunidade, este pode ser um valor fixo ou %, mas o mais comum pe valor fixo e este valor pode ser estabelecido por subunidade ou empreendimento. Os parceiros podem ser empresas do próprio Grupo Casitas ou uma pessoa física ou jurídica externa.

 Os valores informados para cada parceiro não necessariamente devem fechar no valor total de venda da tabela de preço, e quando isso ocorre significa que a entidade que não tem valor informado receberá a diferença residual pois não sabem por qual valor a subunidade será vendida.

 Em caso de atualização da tabela de preço para valores fixos, os valores já estabelecidos não se alteram e as diferenças será atribuídas a empresa que não tem valor pre- fixado.

 No momento não haveria a necessidade de gerar o faturamento para as outras empresas que fazem parte do projeto, mas haverá necessidade num futuro ainda não determiando.

Permitir que o valor do faturamento seja montando por formula onde teremos funções de formula para valores padrões, como:

* Valor Total da Venda
* Valor Venal da Tabela de Preço
* Valor Proporcional da Empresa

Os lançamentos financeiros gerados pelo FIDEICOMISO devem corresponder a parte de recebimento da própria empresa.

Em virtude do FIDEICOMISO o valor da escritura poderá ser o Valor Venal, o Valor Total da Venda PVI ou o Valor Proporcional da Empresa. A data da escritura deve ser associada a data indicada no processo do PVI.

Criar campo na venda para registrar o Número de Registro do INFONAVIT.
