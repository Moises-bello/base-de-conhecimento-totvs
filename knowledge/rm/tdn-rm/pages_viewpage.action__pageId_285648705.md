---
content_hash: 806d42cc74c993e2a9dcd30d6e50f9fb51bab2c1f31f04ced50fbc41b24f3903
fetched_at: '2026-06-29T00:08:38.341316+00:00'
page_id: '285648705'
product: rm
source: tdn-rm
title: "1.\tMódulo PVI – Portal de Venda Imobiliária"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285648705
version: 3
---

Para que o PVI possa atender ao mercado de venda de casas e apartamentos Sociais no México serão necessários os seguintes desenvolvimentos.

**1.1.****Cadastro do Cliente / Prospect**

*PROSPECTO é a pessoa que tem um contato com a empresa, se simula duas condiciones de uma venda mas não reserva uma subunidade .A reserva de uma subunidade só ocorre com o pagamento do valor de adiantamento estabelecido em cada empreendimento.*

Criação dos campos a seguir que devem ser preenchidos pelo usuario no PVI:

* NSS (Número do Seguro Social)
* CURP (Chave Única de Registro da População)
* RFC (Registro Federal do Contribuinte)
* Será necessário criar dois novos status: “em espera” e “ cancelado”. Para os dois status a proposta de venda fica supensa e perdem a reserva da subunidade.

O status “em espera” é aplicado para prospects que não cumprem os prazos para a entrega de documentos, atualmente fixado em 4 dias.

O status “cancelado” deve solicitar um motivo e pode ser aplicado a prospects que depois de um tempo determinado de espera não concluem a venda.

Os dois status devem permitir a reativação do prospect e caso isso aconteça a proposta de venda deve ser ativada e seu valor atualizado, bem como uma nova subunidade associada.

Os novos campos devem ser criados e registrados também no TIN.

Avaliar a possibilidade de emissão de Relatório por status de cliente e processos, clientes em atraso e cliente com parcelas em aberto.

**1.2.****Promoções**

Atualmente o PVI permite a criação de promoções que tem seu Valor aplicado a um empreendimento e determinadas subunidades. Além desde modelo de promocação deve permitir também:

* **Valores por periodos e por condicões**

Além da possibilidade de aplicar a promoção de valor a um empreendimento / subunidade, o sistema deberá permitir que sejam criadas faixas de desconto, que poderiam ser aplicadas em um periodo terminado, se atender a situações como: valor de antecipação pagas em menos parcelas, valor de antecipação menor que X.

*Ex: no mes de maio pague de uma só vez e tenha um descontó de Mil Pesos!*

 O TIN deve permitir ainda que a promoção, seja ela qual for, se aplicque a Unidades (Quadras).

* **Produtos**

 Permitir a criação de promoções onde serão fornecidos “brindes” aos clientes que comprarem determinadas vivendas. Estes “brindes” são produtos, como por exemplo, ar condicionado, grade de proteção, etc.

Atende a Hipoteca verde

(*Fonte:* <http://portal.infonavit.org.mx/wps/wcm/connect/a756761f-77a7-4e0d-bf8a-e2e532674568/Paquetes_de_instalacion_de_ecotecnologias.pdf?MOD=AJPERES&CVID=lySslSH> )

 Esta promoção pode ser aplicado concomitante com outra.

Quando a proposta de venda for fechada e estiver associada a uma promoção desde tipo, deve gerar uma  solicitação de compra no backoffice.

* **Promoção por modelo de subunidade**

O PVI deve permitir a aplicação de uma ou mais promoções por modelos de subunidades .

**1.3.****Desconto**

 O valor de desconto que pode ser dado a uma determinada venda, e por usuário deve ser limitado por modalidade de venda.

**1.4.****Proposta de Venda**

Na proposta de venda PVI, deve- se criar o campo para registro do **Folio INFONAVIT**.  Este dado é o registro de que o orgão governamental autorizou o financiamento e somente depois de marcado  a venda poderá ser enviada para o TIN.

**Criar Simulador** para calculo de subsidio do CONAVI e de pagamento da diferença residual que deverá ser feita pelo cliente (adiantamentos).

Este simulador deve permitir a entrada dos dados do INFONAVIT, tais como:

* Monto de Credito
* Descuento Preca
* Edad
* SSV saldo da subconta da vivenda

Permitir a entrada de dados pre fixados pelo governo como (serve para todas as simulações):

* % Imposto
* Custo de Avaliação
* Dias do Mes: média de días do mes (*365/12=**30,4**)*
* 1UMA: valor de uma  Diário. Este valor pode ser calculado ou infomado pelo usuario pois é publicado no site do governo *(*[*http://www.inegi.org.mx/est/contenidos/proyectos/uma/default.aspx*](http://www.inegi.org.mx/est/contenidos/proyectos/uma/default.aspx) ).
* 1UMA Mensal: (30,4\*1UMA). Este valor pode ser calculado ou infomado pelo usuario pois é publicado no site do governo *(*[*http://www.inegi.org.mx/est/contenidos/proyectos/uma/default.aspx*](http://www.inegi.org.mx/est/contenidos/proyectos/uma/default.aspx) ).
* 1 VSM: Vezes do salário minimo
* Tabela de Valores de Subsídio
* Data inicial e Data Final

*valor maximo subsidio regular :*

*$84.911,15                          $78.026,46           $75.731,57*

Permitir entrar com os valores que o cliente deve pagar como:

* GASTOS FIN MENOS
* Despesas com Cartório
* Contrato de Agua
* AHORRO VOLUNTARIO

Com todos os dados informados o simulador deve calcular

* VSMMDF = Monto de Crédito / Salario Mensal
* SALARIO CLIENTE (Indice)  = Descuento Preça/ 0,25/ Dias do Mês/ 1 VSM- 0,01
* SALARIO CLIENTE ($)= se o valor SALARIO CLIENTE (Indice)  for menor ou igual a 1,6 e a idade for menor que 45 anos, considera o salário de $4.589,79, se for menor que de 45 anos mas como salároio em índice maior que 1,6 considera o salário $10.607,01. Se a idade ficar entre 45 e 55 anos e o salário em índice for até 1,6 considera o salário $2.294,90.
* AVALUO MENOS = (MMC \* %Imposto)+ Valor de Avaliação
* MMC (Valor Máximo de Credito ) = ((VSMMDF \* SALARIO CLIENTE ($)) - GASTOS FIN MENOS -      AVALUO MENOS) + SSV+ AHORRO VOLUNTARIO
* Preco da Venda= carregado pelo sistema conforme subunidade escolhida
* DIFERENCIA DE CREDITO= MNC - Preco da Venda
* MONTO MAXIMO SUBSIDIO REGULAR=

*se o Preco da Venda <= 158 \* UMA mensal, e salário cliente Indice menor que 2, 7 então o máximo de sibisidio será de                $80.321,36 (HASTA 2.7 UMAS)*

*se o Preco da Venda <= 158 \* UMA mensal, e salário cliente Indice menor que 4 e maior que 2,7 então o máximo de sibisidio será de $22.948,96 (MAYOR 2.7 HASTA 4 UMAS)*

*Senão atender a nenhuma das condições acima o valor é Zero.*

*Esta é uma formula estabelecida pelo CONAVI e não tem apenas estas faixas mas estas são as faixas usadas pelo cliente de acordo com a faixa de preço dos seus imóveis e do seu público alvo em termos de salário.*

SUBSIDIO =

*se DIFERENCIA DE CREDITO <= MONTO MAXIMO SUBSIDIO REGULAR então o subisidio será igual a DIFERENCIA DE CREDITO*

*senão MONTO MAXIMO SUBSIDIO REGULAR*

* DIF DESPUES SUBSIDIO = DIFERENCIA DE CREDITO- SUBSIDIO
* DIFERENCIA TOTAL= DIF DESPUES SUBSIDIO - CONTRATO DE AGUA- GASTOS NOTARIO

*Fonte:*

 Se ainda houver diferença, a venda pode viabilizada aplicando as seguintes condições:

* O valor de diferença pode ser pago como adiantamento pelo Cliente
* O valor de diferença pode ser descontado da comissão do vendedor, limitado ao valor de comissão tabelado;
* Pode-se dar um descontó para zerar a diferença e assim viabilizar a venda.

As opções acima não são excludentes e podem ser aplicadas simultaneamente, sendo desejado que os valores de limite e saldo da diferença sejam apresentados para que o vendedor possa manejar a porposta.

 Os valores de adiantamento apresentados no simulador serão cobrados do cliente pelo vendedor, limitando a um número pre fixado de parcelas, que atualmente é 4 e sua periodicidade é semanal.

 São cobrados como adiantamentos os valores referentes a:

* Cartório
* Despesas Financeiras
* Contrato de Agua
* Diferença Total

A proposta de venda deve gerar uma reserva da subunidade, não permitindo assim que outro cliente se proponha a comprar a mesma subunidade. O Prospect deverá pagar todos os valores de antecipação. Caso não pague algum valor de antecipação, a proposta  será suspensa e a subunidade perde a reserva e volta para venda, podendo ser associada novamente para um novo prospect. Caso o prospect anterior pague o valor em aberto, será oferecido a ele uma nova subunidade, se não houver mais interesse do prospect,  o valor pago como antecipação poderá ser devolvido ou mantido como credito para outra venda. Se ao concluir o pagamento do adiantamento a subunidade escolhida não estiver mais disponivel uma nova subunidade deve ser selecionada, mas caso não haja mais nenhum subunidade disponível o dinheiro de adiantamento pode ser devolvido ou mantido como crédito para outra venda.

São passiveis de devoluções as seguintes situações:

* Indisponibilidade de subunidade após suspensão da proposta
* Recusa de financiamento pelo INFONAVIT e demais orgãos
* Desistência do cliente

Caso haja a necessidade de devolução, o valor a ser restituído será a diferença da antecipação descontado o valor prefixado de custos ($1.850,00) .

A devolução será um processo financeiro e a proposta deverá ter seu status alterado (ex: cancelado) e o motivo informado.

O PVI deve imprimir o recibo de pagamento para o cliente referente ao valor de adiantamento pago (cada uma das parcelas).

Para propostas de venda vinculadas a modalidade INFONAVIT, a venda só será efetivada quando o Folio INFONAVIT, for liberado.

O vendedor deve visualizar as parcelas de antecipação pagas para acompanhar a situação de sua proposta.

Criar **Agenda para assinatura de contratos**, onde o usuário possa visualizar todas as propostas que atendem pre- requisitos, como Folio INFONAVIT gerado, ou aprovações concluídas (controle de documentos) .

Listar vendas que já tiveram o recebimento do notário para que possa pagar o cartório (setor de expedição) .

Gerar relatório de “Aviso de Retenção”, este aviso deve ser enviado para o empregador do cliente, para torna-lo ciente de que o financiamento foi aprovado pelo INFONAVIT, e que o valor do financiamento deve ser descontado mensalmente do salário.

**1.5.****Comissão**

 Além da comissão por valor fixo estabelecido no PVI, será necessário buscar da tabela de preço do TIN o valor fixado para a subunidade. Este valor será enviado para a geração de Comissão do TIN .

 O vendedor pode ainda receber um valor de Bonus que estará condicionado a uma quantidade de vendas por periodo e/ ou um valor (meta) .

 O pagamento da comissão bem como eventual agrupamento de comissões por período deverá ser administrada pelo Financeiro do Backoffice.

**1.6.****Etapas de aprovação**

Em umas das etapas de aprovação do PVI pode haver um motivo para não se avançar, que é o caso das vendas que já foram escrituradas e enviadas para o INFONAVIT  mas por algum motivo não concluíram o processo de liberação de valor, e este passo é de suma importância a verificação, pois para vendas que não tem esta finalização do INFONAVIT não haverá receita.//
