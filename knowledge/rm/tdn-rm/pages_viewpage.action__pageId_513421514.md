---
content_hash: e0da69fcb8b76d5f1885df7ad721c7a32f99ebb71c9c00af73aeef1303fbd458
fetched_at: '2026-06-29T00:10:26.169248+00:00'
page_id: '513421514'
product: rm
source: tdn-rm
title: Novidades 12.1.26 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=513421514
version: 14
---

**Venda**

* Nova opção no cadastro de empreendimento: **Deduzir FGTS com terreno permutado**: Indica que em um contrato de venda deste empreendimento que seja Minha Casa Minha Vida, ao gerar as parcelas de acordo com o andamento da obra, fará abatimento do valor do terreno no valor do FGTS. Maiores detalhes [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105154).
* Contabilização assíncrona: do TIN, Disponibilizados nesta versão os processos de contabilização assíncrona, permitindo que a contabilização dos contratos aconteça em momentos distinto, bem como após os processos de reajuste, distrato e aditivo.
* Criação de um novo modelo de cálculo para os planos de financiamento MCMV com terreno próprio. Maiores detalhes [aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105235)
* Criação do anexo [Dados Bancários do Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=514742343). A partir deste anexo, será possível associar os dados bancários ao empreendimento selecionado.
* Disponibilizado a .

**Aluguel**

* Está disponível o  para os Contratos de Locação. Este aditivo permite alterar a fórmula e a taxa de participação do aluguel complementar, já cadastrado previamente em um determinado contrato efetivado.
* Disponíveis os campos de "**Periodicidade reembolso",** no  e também o campo **"Primeiro Vencimento Reembolso"** no
* Estão disponíveis na  os campos Valor m² e Área locada.
* Melhoria na geração de lançamentos de [reembolso de despesas](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Cadastro+individual+de+despesas), quando o imóvel possui áreas fracionadas. O sistema passa a fazer os rateios de centro de custo a partir dos centros de custo cadastrados nas respectivas áreas do imóvel.
* Melhoria no processo de [geração de lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=435105232) no fechamento de condomínio, quando o imóvel possui áreas fracionadas. O sistema passa a fazer os rateios de centro de custo a partir dos centros de custo cadastrados nas respectivas áreas do imóvel.
* Melhoria nos aditivos de [alteração de garantia](https://tdn.totvs.com/pages/viewpage.action?pageId=435105106) e [alteração](https://tdn.totvs.com/pages/viewpage.action?pageId=435105257) / [exclusão de imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=435104951). Quando o contrato possui uma garantia associada com vinculo ao valor do contrato, o sistema passa a exigir, na efetivação dos aditivos de alteração / exclusão de imóveis se o contrato possui também um aditivo de garantia em preparação para ser aplicado. Este aditivo será automaticamente efetivado ao se efetivar o aditivo de alteração de imóvel / exclusão de imóvel.
* Melhorias no processo de escalonamento:

  + Criado no cadastro de [Tipo de Escalonamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105312), dois campos: Um para informar o tipo de valor do escalonamento (se será um desconto ou acréscimo) e o segundo, que possibilita informar o valor de integração que deverá ser utilizado.   
    Para os escalonamentos legados (já cadastrados no sistema, sem a definição de valor de integração) o comportamento será o mesmo, buscando o valor de integração do parâmetro do TIN.
  + No cadastro de [escalonamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105312), de acordo com o Tipo de Escalonamento, será possível definir se o mesmo terá um desconto ou acréscimo, bem como se este desconto ou acréscimo possuirá um valor fixo ou definido por percentual.  
    O reajuste do escalonamento passa também a reajustar os valores definidos de Desconto / Acréscimo, caso estes sejam valores definidos como fixos, através da opção "Reajusta valor principal e a diferença".
* Melhoria no processo de associação de despesas ao seguro. O sistema passa a permitir esta associação quando o seguro é de responsabilidade do locatário.
* Inclusão do campo **Periodicidade** no [cadastro de despesas](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Cadastro+individual+de+despesas), que poderá ser personalizado ou mensal.
* Inclusão do campo **Primeiro Vencimento** no [cadastro de despesas](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Cadastro+individual+de+despesas), que permitirá ao usuário informar a data do primeiro vencimento da parcela de despesa e também do reembolso.
* Inclusão do campo **Tipo Agregação** no [cadastro de eventos financeiros](https://tdn.totvs.com/pages/viewpage.action?pageId=435105273). O tipo de agregação só fica disponível quando o Tipo de cobrança do evento é Agregado. Ele define a referência de data que será usada para que as parcelas do evento se agreguem às parcelas do contrato de locação.
* Melhoria no [relatório de ficha de imóvel](https://tdn.totvs.com/pages/viewpage.action?pageId=496026781&draft=true), que passa a contar com os campos "Inscrição Municipal" e "Matrícula".
* Melhoria no cadastro de áreas do imóvel para permitir reduzir o m² total da área. O sistema passa a validar se o novo valor informado é menor que a área locada mais a área reservada.
* Melhoria no cadastro de área dos imóveis, para permitir parametrizar o número de casas decimais do valor do m² da área.
* Novo parâmetro "[Considerar valor reajustado quando](https://tdn.totvs.com/pages/viewpage.action?pageId=435105298)["](https://tdn.totvs.com/pages/viewpage.action?pageId=435105298) no contrato de aluguel, com as opções: "**Reajuste ocorrer até o início do período de locação**" e "**Reajuste ocorrer até o final do período de locação**".
* Criação de parâmetros para aperfeiçoar o tratamento na [geração de lançamentos do contrato de aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105008), para considerar mês civil no rateio e aplicação do valor rateado
* Inclusão dos campos de descrição e tipo de despesa no [cadastro de inscrição municipal.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105304)
* Melhoria nos rateios de centro de custo para [imóveis com áreas fracionadas](https://tdn.totvs.com/pages/viewpage.action?pageId=435105243): Ao gerar os rateios no contrato de locação, o sistema irá compor este rateio buscando os centros de custo cadastrados nas áreas dos imóveis.
* Criação de parâmetros de integração financeira no cadastro do encerramento / rescisão. O usuário pode definir um parâmetro específico para a geração dos lançamentos financeiros de rescisão. Caso este campo permaneça em branco, então o sistema irá utilizar os parâmetros definidos no contrato de locação.
* Criação do campo "[Multa Contratual](https://tdn.totvs.com/pages/viewpage.action?pageId=435104970)": que associará uma [multa](https://tdn.totvs.com/pages/viewpage.action?pageId=514432601) à rescisão do contrato. O valor do Evento Financeiro de Rescisão será a soma do valor da Rescisão com o valor da Multa.
* Criação do [cadastro de multas](https://tdn.totvs.com/pages/viewpage.action?pageId=514432601) (anexo ao contrato de locação) e sua associação com despesas.
* Criação do anexo para visualizar as [despesas associadas](https://tdn.totvs.com/pages/viewpage.action?pageId=515302926) ao contrato de locação.
* Melhoria no [cadastro de seguros](https://tdn.totvs.com/display/LRM/Outros+-+Controle+de+Seguro+-+Seguro): Disponibilizado o botão "**Somar Coberturas**" que calcula a soma do prêmio de todas as coberturas e salva automaticamente o valor no campo Prêmio total do seguro.

**Portal/APP**

* Criação do [parâmetro](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047) "**Número de Dias máximos para vencimento do Boleto**": Esse parâmetro indica até quantos dias futuros poderá ter o vencimento do Boleto gerado no portal.
