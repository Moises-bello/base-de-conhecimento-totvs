---
article_id: 360028429351
category: Comércio Exterior - Easy Siscoserv - Importação
content_hash: 12a6702892d70bf1c183ac2f54a4917c71953c162d3279d0d192f85a9c2f8ed1
fetched_at: '2026-06-28T22:39:39.631657+00:00'
product: protheus
section_id: 1500001538321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS- Integração de despesas
  do Easy Import Control (SIGAEIC) com o módulo Easy Siscoserv (SIGAESS)
type: support-article
updated_at: '2021-08-24T19:55:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028429351-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Integra%C3%A7%C3%A3o-de-despesas-do-Easy-Import-Control-SIGAEIC-com-o-m%C3%B3dulo-Easy-Siscoserv-SIGAESS
---

**Dúvida**Como integrar despesas do Easy Import Control (SIGAEIC) com o módulo Easy Siscoserv (SIGAESS)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

**Pré-Requisitos da integração:**

Para executar os procedimentos a seguir, a integração entre os módulos Easy Import Control e Easy SISCOSERV deverá estar habilitada, através dos parâmetro MV\_ESS0022.

**Geração dos Pedidos a partir da Despesa**

* **Inclusão**

Ao possuir uma Despesa internacional no processo de Desembaraço no SIGAEIC, é gerado no SIGAESS um Pedido de Aquisição com os dados da despesa e também o Registro de Aquisição (MV\_ESS0003 = T) com os dados iguais aos informados no Pedido.

* **Alteração**

Ao alterar o desembaraço, caso haja alteração no valor da despesa e não tenha pagamento realizado para uma ou mais parcelas no financeiro, o sistema realizará a alteração no Pedido de Aquisição.

* **Exclusão**

Em virtude do Siscoserv, não disponibilizar a ação de “Excluir” um registro, quando o processo de desembaraço for excluído no SIGAEIC e conter despesas lançadas como serviço no SIGAESS, neste último módulo nada ocorrerá.

**Manutenção de Despesas Integrada – SIGAEIC X SIGAFIN**

**Pré-Requisitos:**

* Possuir os parâmetros MV\_EASYFIN e MV\_EASYFDI = T.
* Possuir o parâmetro MV\_AVG0226 = F.

* **Geração**

Ao ser gerado o título da despesa no SIGAFIN, será incluído o câmbio de serviço. Serão informados também os dados do Pedido de Serviço de Registro de Serviço gerados automaticamente no SIGAESS anteriormente a esta execução atual.

* **Baixas**

Ao serem realizadas baixas totais ou parciais de uma ou mais parcelas no SIGAFIN referente à despesa não ocorrerá nenhuma ação no SIGAEIC. No módulo SIGAESS, no entanto, na fase de Pedido ou Registro de Serviço, é possível efetuar a importação das baixas efetuadas no SIGAFIN para o SIGAESS observando todo o tipo de baixa (Baixa Manual, Borderô, entre outros). Apurará o exato valor baixado de cada parcela em moeda estrangeira.

A data da baixa no SIGAFIN irá representar a data de pagamento no SIGAESS.

* **Cancelamento das Baixas**

Ao serem realizados cancelamentos das baixas totais ou parciais de uma ou mais parcelas no SIGAFIN referente à despesa, não ocorrerá ação no SIGAEIC. No módulo SIGAESS, no entanto, na fase de Pedido ou Registro de Serviço, é possível efetuar a importação dos cancelamentos de baixa efetuada no SIGAFIN para o SIGAESS observando todo o tipo de baixa (Baixa Manual, Borderô, entre outros). Apurará o exato valor de cancelamento da baixa de cada parcela em moeda estrangeira.

**Manutenção do Câmbio Integrada com Câmbio Serviço**

**Pré-Requisitos:**

* Possuir os parâmetros MV\_EASY, MV\_EASYFIN e MV\_FIN\_EIC = F.

* **Geração**

Ao serem geradas no SIGAEIC as parcelas de câmbio incluído o câmbio de pagamento do serviço no SIGAESS. Ao alterar as parcelas no SIGAEIC de forma que gere uma nova parcela ainda não integrada, o sistema incluirá a nova parcela e alterar as parcelas já integradas.

* **Liquidação**

Ao serem realizadas liquidações no controle de câmbio do SIGAEIC de uma ou mais parcelas da despesa, o sistema verifica se houve alteração na quantidade de parcelas originais no câmbio de importação. Havendo a diferença, o sistema gera câmbio de serviço para registrar as novas parcelas. E, em seguida, realiza a baixa de pagamentos por serviço passando as parcelas liquidadas e o valor em moeda estrangeira.

A data de Liquidação no SIGAEIC representa a data de pagamento no SIGAESS.

* **Estorno da Liquidação**

Ao ser realizado o estorno da liquidação de uma ou mais parcelas no controle de Câmbio do SIGAEIC o sistema altera o câmbio de serviços informando os dados das parcelas que teve a liquidação estornada. E, em seguida, serão cancelados os pagamentos por serviço, com os dados dos pagamentos estornados. O registro do cancelamento no Siscoserv deverá ser feito diretamente no módulo SIGAESS.

**Sequência 000: Integração de Despesa**

**Observação:** Neste exemplo utilizaremos a despesa Frete.

**Pré-Requisitos:**

* Aplicar o update USSIGAESS.PRW liberado no chamado THQTGL.
* Possuir os parâmetros MV\_EASYFIN = T e MV\_ESS0022 = T.
* Possuir o parâmetro MV\_ESS0023 = T para enviar informações de frete e seguro informados na invoice para o SIGAESS.
* Possuir um fornecedor estrangeiro.
* Possuir uma condição de pagamento com o campo C. Pagto SIGA preenchido.
* No cadastro de Produtos, incluir o produto Frete e nos dados complementares do produto, vincular uma NBS.
* Vincular o produto Frete ao fornecedor estrangeiro cadastrado anteriormente.
* Possuir uma empresa cadastrada e vinculada ao fornecedor estrangeiro cadastrado anteriormente.
* No cadastro de Despesas, vincule o produto Frete na despesa 102 e na pasta Outros preencha o campo Cod.Produto.
* Possuir um Purchase Order com INCOTERM que contemple frete collect; um frete pago pelo importador.
* Possuir um embarque para este Purchase Order; preencher todas as informações do frete na capa do embarque na pasta Transporte; informar a data de embarque na pasta Embarque.

1. No Easy Siscoserv Control (SIGAESS), acesse Atualizações/ Importação/ Processo Aquisição.
2. Veja que o processo de aquisição para a despesa foi gerada. Clique em Visualizar.
3. Observe as informações do processo.
4. Selecione o processo e em Ações Relacionadas clique em Invoices.
5. Veja que as informações da Invoice foram geradas.

**Sequência 001: Cadastro de Vias de Transporte**

1. No Easy Import Control (SIGAEIC), acesse Atualizações / Cadastros / Vias de Transporte.
2. O sistema apresenta a lista de vias de transporte cadastradas
3. Posicione o cursor em uma Via de Transporte e clique em Alterar.
4. Será exibido o campo “Prd. SISCOS.”
5. Ao informar um produto neste campo, ele será considerado na integração de frete com o SISCOSERV, quando habilitada.

**Sequência 002: Processo de Embarque/Desembaraço (Frete contratado pelo importador)**

1. No Easy Import Control (SIGAEIC), acesse Atualizações / Desembaraço / Manutenção (EICDI500).
2. Inclua um processo de embarque, relacionando os dados do Frete Internacional e Seguro na capa do embarque.
3. Verifique os campos “For.Fre.Int.” e “Loj.Fre.Int.”, “For.Seg” e “Loj.Seg” na aba “Transporte”.
4. Estes campos são inicializados com o mesmo conteúdo dos campos “Forn. Frete” e “Loja Frete”.
5. Caso deseje alterar o Fornecedor que será registrado no “Pedido de Aquisição” no módulo Easy SISCOSERV, basta alterar os campos “Forn. Frete” e “Loja Frete”, e “Forn. Seg.” e “Loja Seg”.
6. Os Pedidos de Aquisição de Serviço serão identificados pelo seguinte código: EMBARQUE\DESPESA. Exemplo: Para o valor de Frete (Despesa 102) registrada no Processo “PROC-1”, o Pedido de Aquisição de Serviço será identificado por “PROC-1/102”; para o valor de Seguro (Despesa 103) registrada no Processo “PROC-1”, o Pedido de Aquisição de Serviço será identificado por “PROC-1/103”;
7. O Produto/NBS a ser considerado para o Pedido criado serão os mesmos informados no cadastro da Via de Transporte do processo ou cadastro da despesa referente ao frete “102” ou seguro “103”, nesta ordem. Importante: Caso não tenha sido informado o produto em nenhuma das opções a integração não será executada;
8. Acessar o módulo Easy SISCOSERV e verificar que os “Pedidos de Aquisição” de frete e seguro foram criados/alterados para o fornecedor informado nos campos correspondentes do processo de embarque.

**Sequência 003: Visualização das Invoices**

1. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
2. Selecione o processo gerado e clique em Visualizar.
3. Verifique que os “Pedidos de Aquisição” de frete e de seguro foram criados  para o fornecedor informado.
4. Em Ações Relacionadas clique em Invoices.
5. Veja que além da inclusão do Pedido de Aquisição de Serviço, foram incluídas as Invoice relacionadas ao desembaraço de forma automática.

**Sequência 004: Visualização das parcelas de Câmbio**

1. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
2. Selecione o processo gerado e clique em Invoices.
3. Veja que além da inclusão da Invoice, foram incluídas as parcelas de câmbio correspondentes de forma automática.

**Sequência 005: Baixa de parcelas de Câmbio (Frete contratado pelo importador)**

- Caso os parâmetros MV\_CAMBFRE e MV\_CAMBSEG estiverem habilitados.

1. No Easy Import Control (SIGAEIC), acesse Atualizações/Financeiro/Controle Câmbio. (EICAP100).
2. Selecione o processo e clique em Alterar.
3. Selecione a parcela referente ao frete e em Ações Relacionadas clique em Liquidação.
4. Informe os dados e clique em Confirmar.
5. Selecione a parcela referente ao seguro e em Ações Relacionadas clique em Liquidação.
6. Informe os dados e clique em Confirmar
7. Clique em Confirmar.
8. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
9. Selecione o processo gerado referente ao frete e clique em Invoices.
10. Verifique que a parcela de câmbio foi liquidada.
11. Retorne a tela anterior
12. Selecione o processo gerado referente ao seguro e clique em Invoices.
13. Verifique que a parcela de câmbio foi liquidada.

- Caso os parâmetros MV\_CAMBFRE e MV\_CAMBSEG estiverem desabilitados e o parâmetro MV\_EASYFIN estiver habilitado.

1. No Financeiro (SIGAFIN), acesse Atualizações/Contas a Pagar/Baixas Pagar Man. (FINA080.PRX).
2. Selecione o título referente ao processo de desembaraço e clique em Baixar.
3. Informe os dados para baixa e clique em Confirmar.
4. Verifique que o título foi baixado.
5. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
6. Selecione o processo gerado referente ao frete e clique em Invoices.
7. Verifique que a parcela de câmbio foi liquidada.
8. Retorne a tela anterior.
9. Selecione o processo gerado referente ao seguro e clique em Invoices.
10. Verifique que a parcela de câmbio foi liquidada.

**Sequência 006: Estorno de parcelas de Câmbio (Frete contratado pelo importador)**

- Caso os parâmetros MV\_CAMBFRE e MV\_CAMBSEG estiverem habilitados.

1. No Easy Import Control (SIGAEIC), acesse Atualizações/Financeiro/Controle Câmbio. (EICAP100).
2. Selecione o processo e clique em Alterar.
3. Selecione a parcela referente ao frete e em Ações Relacionadas clique em Est. Liquidação.
4. Informe os dados e clique em Confirmar.
5. Selecione a parcela referente ao seguro e em Ações Relacionadas clique em Est. Liquidação.
6. Informe os dados e clique em Confirmar
7. Clique em Confirmar.
8. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
9. Selecione o processo gerado referente ao frete e clique em Invoices.
10. Verifique que a liquidação da parcela de câmbio foi estornada.
11. Retorne a tela anterior.
12. Selecione o processo gerado referente ao seguro e clique em Invoices.
13. Verifique que a liquidação da parcela de câmbio foi estornada.

- Caso os parâmetros MV\_CAMBFRE e MV\_CAMBSEG estiverem desabilitados e o parâmetro MV\_EASYFIN estiver habilitado.

1. No Financeiro (SIGAFIN), acesse Atualizações/Contas a Pagar/Baixas Pagar Man. (FINA080.PRX).
2. Selecione o título referente ao processo de desembaraço e clique Em Ações Relacionadas e em Canc Baixa.
3. Informe os dados para do cancelamento de baixa e clique em Confirmar.
4. Verifique que a baixa do título foi cancelada.
5. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
6. Selecione o processo gerado referente ao frete e clique em Invoices.
7. Verifique que a liquidação da parcela de câmbio foi estornada.
8. Retorne a tela anterior.
9. Selecione o processo gerado referente ao seguro e clique em Invoices.
10. Verifique que a liquidação da parcela de câmbio foi estornada.

**Sequência 007: Processo de Embarque/Desembaraço (Frete contratado pelo exportador)**

- Para executar os procedimentos a seguir, a integração entre os módulos Easy Import Control e Easy SISCOSERV deverá estar habilitada, através do parâmetro MV\_ESS0023.

1. A integração de dados de Invoices do Easy Import Control para o Easy SISCOSERV possibilita a integração de valores de Frete e Seguro registrados nas Invoices do exportador para registro no SISCOSERV.
2. Inclua um processo de embarque, relacionando os dados do Frete Internacional e Seguro na capa da Invoice.
3. Para todas as Invoices relacionadas ao processo de Embarque/Desembaraço em que houver valor de Frete ou Seguro registrado, será criado um Pedido de Aquisição de Serviços no módulo Easy SISCOSERV.
4. Os Pedidos de Aquisição de Serviço serão identificados pelo seguinte código: EMBARQUE\INVOICE\DESPESA. Exemplo: Para o valor de Frete (Despesa 102) da Invoice “INV-A” registrada no Processo “PROC-1”, o Pedido de Aquisição de Serviço será identificado por “PROC-1/INV-A/102”; para o valor de Seguro (Despesa 103) da Invoice “INV-A” registrada no Processo “PROC-1”, o Pedido de Aquisição de Serviço será identificado por “PROC-1/INV-A/103”;
5. O Produto/NBS a ser considerado para o Pedido criado serão os mesmos informados no cadastro da Via de Transporte do processo ou cadastro da despesa referente ao frete “102” ou seguro “103”, nesta ordem. Importante: Caso não tenha sido informado o produto em nenhuma das opções a integração não será executada;
6. O valor da aquisição do serviço será o mesmo informado na Invoice para a despesa;
7. O Fornecedor do serviço será o mesmo fornecedor da Invoice.
8. Acesse o botão “Despesas” e identifique as despesas “102” (Frete) e “103” (Seguro).
9. Verifique o campo “Prd. SISCOS.”. Ele estará preenchido com o produto informado na via de transporte selecionada para o processo. Caso não tenha sido informado um produto para a Via de Transporte em questão, será exibido o produto cadastrado para a despesa “102” (Frete) e “103” (Seguro) no cadastro de despesas.
10. Caso este produto seja alterado diretamente na despesa, ele será atualizado no Processo de Aquisição correspondente no módulo Easy SISCOSERV.

Importante: As parcelas de Câmbio originadas de integração não podem ser alteradas ou liquidadas no Easy SISCOSERV, sendo somente informativas. Todas as operações serão executadas no Easy Import Control, sendo o Easy SISCOSERV responsável somente pelo registro das informações no SISCOSERV (Registro de Pagamento).

**Sequência 008: Baixa de parcelas de Câmbio (Frete contratado pelo exportador)**

1. No Easy Import Control (SIGAEIC), acesse Atualizações/Financeiro/Controle Câmbio. (EICAP100)
2. Selecione o processo e clique em Alterar.
3. Selecione a parcela referente à invoice e em Ações Relacionadas clique em Liquidação.
4. Informe os dados e clique em Confirmar.
5. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
6. Selecione o processo gerado referente ao frete e clique em Invoices.
7. Verifique que a parcela de câmbio foi liquidada.
8. Retorne a tela anterior
9. Selecione o processo gerado referente ao seguro e clique em Invoices.
10. Verifique que a parcela de câmbio foi liquidada.

**Sequência 009: Estorno de parcelas de Câmbio (Frete contratado pelo exportador)**

1. No Easy Import Control (SIGAEIC), acesse Atualizações/Financeiro/Controle Câmbio. (EICAP100).
2. Selecione o processo e clique em Alterar.
3. Selecione a parcela referente à invoice e em Ações Relacionadas clique em Est. Liquidação.
4. Informe os dados e clique em Confirmar.
5. No Easy Siscoserv Control (SIGAESS), acesse Atualizações / Importação / Processo Aquisição (ESSPS400).
6. Selecione o processo gerado referente ao frete e clique em Invoices.
7. Verifique que a liquidação da parcela de câmbio foi estornada.
8. Retorne a tela anterior.
9. Selecione o processo gerado referente ao seguro e clique em Invoices.

Verifique que a liquidação da parcela de câmbio foi estornada.
