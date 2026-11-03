---
article_id: 360028136232
category: Comércio Exterior - Easy Siscoserv - Exportação
content_hash: 04f80eece5ab14e22482ac31b7a1c6c2a5d12a3a56ae3d6d0e87826e0bf8ce86
fetched_at: '2026-06-28T22:39:38.952740+00:00'
product: protheus
section_id: 1500001549402
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS- Integração de despesas
  do exportação com o módulo Easy Siscoserv
type: support-article
updated_at: '2022-06-21T18:54:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028136232-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Integra%C3%A7%C3%A3o-de-despesas-do-exporta%C3%A7%C3%A3o-com-o-m%C3%B3dulo-Easy-Siscoserv
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:08:00 min  
  
Dúvida**Como integrar despesas do Easy Export Control (SIGAEEC) com o módulo Easy Siscoserv (SIGAESS)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 11.80  
  
**Solução****Pré-Requisitos da integração:**Para executar os procedimentos a seguir, a integração entre os módulos Easy Export Control e Easy SISCOSERV deverá estar habilitada, através dos parâmetros MV\_AVG0131 e MV\_ESS0014.

**Geração dos Pedidos a partir da Despesa**

* **Inclusão**

Ao possuir uma Despesa internacional no processo de Embarque no SIGAEEC integrado ao SIGAFIN, é gerado o câmbio da despesa no Controle de Câmbio e também são criados os títulos financeiros no SIGAFIN. No SIGAESS, será gerado o Pedido de Aquisição com os dados da despesa e também o Registro de Aquisição (MV\_ESS0003 = T) com os dados iguais aos informados no Pedido.

* **Alteração**

Quando o valor de alguma parcela é alterado no câmbio, o valor restante é integrado à próxima parcela da sequência.  
Também são excluídos todos os títulos da despesa a qual pertencia à parcela, exceto parcelas liquidadas, e gerados novos títulos para todas as parcelas com valores alterados.  
No SIGAESS, serão mantidas no câmbio as referências ao Pedido e Registro de Aquisição.

* **Exclusão**

Quando uma parcela é excluída no câmbio, o valor é integrado a uma das outras parcelas da mesma despesa.  
Também são excluídos todos os títulos da despesa a qual pertencia à parcela, e gerados novos títulos para todas as parcelas com os novos valores.  
No SIGAESS, serão mantidas no câmbio as referências ao Pedido e Registro de Aquisição.

* **Liquidação**

Quando uma parcela é liquidada no câmbio, é feito a baixa do título no SIGAFIN.  
No SIGAESS, será incluído o registro de pagamento com os dados da liquidação.  
O envio do registro de Pagamento deverá ser feito no SIGAESS.

* **Estorno da liquidação**

Quando é feito o estorno da liquidação no câmbio, é feito o estorno da baixa do título no SIGAFIN.  
No SIGAESS, será incluído o cancelamento do pagamento.  
O envio do registro de Cancelamento do Pagamento deverá ser feito no SIGAESS.nto para Utilização.

**Sequência 000 -****Integração de Despesas SIGAEEC e SIGAESS****Observação:** Neste exemplo utilizaremos a despesa Frete.  
**Pré-Requisitos:**

1. Possuir os parâmetros MV\_AVG0131 = T e MV\_ESS0014 = T.
2. Possuir um fornecedor estrangeiro.
3. Possuir uma condição de pagamento com o campo C. Pagto SIGA preenchido.
4. No cadastro de produtos, incluir o produto Frete.
5. Nos dados complementares do produto, vincular uma NBS.
6. Vincular o produto Frete ao fornecedor estrangeiro cadastrado anteriormente.
7. Possuir uma empresa cadastrada e vinculada ao fornecedor estrangeiro cadastrado anteriormente.
8. No cadastro de despesas, vincule o produto Frete na despesa 102.
9. Na pasta Outros, preencha o campo Cod. Produto.
10. Possuir um pedido de exportação com INCOTERM que contemple frete, e preencher o valor de frete.
11. Possuir um embarque para este pedido, preencher todas as informações do frete nas Despesas Internacionais e informar a Data de Embarque.

**Observação**: Para os casos em que o frete e seguro for informado na invoice, é necessário preencher os campos Seguro e Int’l Freigh. Independente do incoterm utilizado no processo, serão geradas as despesas no Easy Siscoserv.

1. No Easy Siscoserv Control (SIGAESS), acesse Atualizações/ Importação/ Processo Aquisição.
2. Veja que o processo de aquisição para a despesa foi gerada. Clique em Visualizar.
3. Observe as informações do processo.
4. Selecione o processo e em Ações Relacionadas clique em Invoices.
5. Veja que as informações da Invoice foram geradas.

* Sempre que houver manutenção no processo de Embarque/ Desembaraço, a integração será executada, de acordo com os passos abaixo:

1. Inclusão de Pedidos de Aquisição de Serviço:
2. Para todas as Invoices relacionadas ao processo de Embarque/Desembaraço em que houver valor de Frete ou Seguro registrado, será criado um Pedido de Aquisição de Serviços no módulo Easy SISCOSERV.
3. Os Pedidos de Aquisição de Serviço serão identificados pelo seguinte código:
4. EMBARQUE\INVOICE\DESPESA. Exemplo: Para o valor de Frete (Despesa 102) da Invoice “INV-A” registrada no Processo “PROC-1”, o Pedido de Aquisição de Serviço será identificado por “PROC-1/INV-A/102”.
5. O Produto/NBS a ser considerado para o Pedido criado serão iguais aos informados no cadastro da Via de Transporte do processo ou cadastro da despesa referente ao frete “102”, nesta ordem.

**Importante****:** Caso não tenha sido informado o produto em nenhuma das opções, a integração não será executada.

* O valor da aquisição do serviço será igual ao informado na Invoice para a despesa.
* O Fornecedor do serviço será igual ao fornecedor da Invoice.

1. Inclusão de Invoices (SISCOSERV):
2. Depois da inclusão do Pedido de Aquisição de Serviço, será incluída uma Invoice relacionada a este Pedido (no módulo Easy SISCOSERV), relacionada à Invoice correspondente no Easy Import Control.
3. Esta Invoice será identificada pelo mesmo código da Invoice informada no Easy Import Control.
4. Inclusão de Parcelas de Câmbio (SISCOSERV):
5. Caso exista alguma parcela de câmbio relacionada à Invoice informada no Embarque\Desembaraço, será criada uma parcela de Câmbio correspondente no módulo Easy SISCOSERV, relacionada à Invoice integrada de acordo com o item “B”.

**Importante**: O valor da Parcela de Câmbio no Easy SISCOSERV será igual ao valor da Parcela de Câmbio no Easy Import Control. Desta forma, o valor a ser registrado no SISCOSERV (valor da despesa) será registrado no campo “Valor SISCOSERV”, rateado de acordo com a quantidade de parcelas.

1. Exclusão/Alteração de Processos/Invoices/Câmbio (SISCOSERV):
2. Sempre que o processo de Embarque/Desembaraço for alterado ou excluído a integração será executada, desta forma, caso tenha ocorrido alguma alteração ou inclusão de Invoice as informações serão replicadas ao Easy SISCOSERV. Caso alguma informação tenha sido excluída, ela também será excluída no Easy SISCOSERV (de acordo com as regras deste módulo. Exemplo: Não é possível excluir informações já registradas no SISCOSERV).

* Sempre que houver manutenção nas parcelas de câmbio do processo, elas serão replicadas para o módulo Easy SISCOSERV, de acordo com os passos abaixo:

a)       Ao Alterar/Liquidar/Estornar uma Parcela de Câmbio:

* Caso a parcela de Câmbio tenha alguma informação alterada no Easy Import Control, as informações serão replicadas para o Easy SISCOSERV.
* Caso a parcela de Câmbio tenha sido liquidada, a parcela correspondente no Easy SISCOSERV também será liquidada.
* Caso ocorra estorno da liquidação, também será feito o estorno na parcela correspondente.

Importante: As parcelas de Câmbio originadas de integração não podem ser alteradas ou liquidadas no Easy SISCOSERV, sendo somente informativas. Todas as operações serão executadas no Easy Import Control, sendo o Easy SISCOSERV responsável somente pelo registro das informações no SISCOSERV (Registro de Pagamento).

**Sequencia 001 – Informações das despesas no processo de embarque do SIGAEEC para geração dos pedidos de aquisição de serviço no SIGAESS**

1. No Easy Export Control (SIGAEEC), acesse **Atualizações / Embarque / Manutenção**, posicione sobre o processo de embarque requisitado e clique no botão **Alterar**.
2. Clique no botão **Ações relacionadas/Despesas** Internacionais e posteriormente na despesa **“Frete Intl.”**
3. Verifique que o sistema irá exibir os campos adicionais **“NBS”**(EXL\_NBSFR), **“For.Fre.Int”**(EXL\_FINTFR), **“Loj.Fre.Int”**(EXL\_FLOJFR), **“Moe.Ped.Ser.”**(EXL\_SMOEFR),  **“Tax.Ped.Ser.”**(EXL\_STAXFR), **“Par.Ped.Ser.”**(EXL\_SPARFR) e **“Val.Ped.Ser.”**(EXL\_SVALFR) onde:

**“NBS”** – Código de NBS utilizada para a despesa que será informado ao Siscoserv. Caso haja produto relacionado na via de transporte utilizada no processo onde este produto esteja associado à uma NBS, será considerada esta NBS proveniente da via de transporte em primeiro caso para a despesa.  
**“For.Fre.Int”** – Fornecedor principal da despesa internacional para os casos em que haja uma empresa representante deste fornecedor. Neste caso, o Pedido de Aquisição de Serviço gerado no Siscoserv deverá conter a moeda deste fornecedor (a informar no campo “Moe.Ped.Ser.”) e corresponder ao valor convertido na moeda utilizada por este fornecedor.  
**“Loj.Fre.Int”** – Código da Loja do Fornecedor principal da despesa internacional.  
**“Moe.Ped.Ser.”** – Moeda utilizada pelo Fornecedor principal da despesa internacional e que será utilizada como moeda do Pedido de Aquisição de Serviço no SIGAESS.  
**“Tax.Ped.Ser.”** – Taxa da moeda utilizada pelo Fornecedor principal da despesa internacional  
**“Par.Ped.Ser.”** – Paridade entre o valor da despesa na moeda utilizada pelo Representante do Fornecedor (moeda informada no campo “Moeda Desp.” com a qual será gerado o faturamento – câmbio de serviço – no SIGAESS) e o valor da despesa na moeda do Fornecedor principal da despesa internacional com a qual será gerado o Pedido de Aquisição de Serviço.  
**“Val.Ped.Ser.”** – Valor da despesa na moeda do Fornecedor Internacional principal (Valor do Pedido de Aquisição de Serviço) convertido conforme a Paridade com a moeda da Despesa Internacional no processo de embarque de Exportação.

1. Considerando que temos os cadastros pré-requisitados de fornecedor e empresa utilizados neste processo de embarque e que temos como exemplo na data-base da despesa as taxas de conversão para R$ cadastradas na rotina de cotação de moedas como:

```
Dóllar > US$  -  3,6725  
EURO > EUR  -  4,1367  (Paridade US$ > EUR = 0,897784)  
IENE   > JPY  -  0,03060 (Paridade EUR > JPY = 135,186274)
```

Ao informarmos a moeda da despesa internacional no campo **“Moeda Desp”**(EXL\_MDFR) o sistema automaticamente calcula o valor da despesa informado na capa do processo (para os casos de frete e seguro) conforme a paridade obtida entre a moeda do processo e a moeda informada para a despesa, atualizando o valor da despesa na moeda informada que será considerado no Faturamento – Câmbio de Serviço – do SIGAESS.  
Ao informar a empresa, o fornecedor desta é admitido como o fornecedor principal do serviço e com isto seus dados são carregados nos campos relativos ao fornecedor do Pedido de Aquisição de Serviço da despesa. Estes campos podem ser alterados.  
Ao informar a moeda do Fornecedor internacional, o sistema automaticamente calcula o valor da despesa na moeda do fornecedor internacional conforme a taxa da database da despesa para esta moeda e atualiza a paridade obtida entre a moeda da despesa (valor do faturamento – câmbio de serviço) e a moeda informada para a fornecedor internacional, atualizando o valor da despesa a ser considerado no Pedido de Aquisição de Serviço do SIGAESS.

1. Ao finalizar a manutenção de cada despesa, Clique no botão  **Confirmar** para finalizar.
2. Acesse a rotina **Ações Relacionadas/ Agentes de Comissão** e informe agentes diferentes onde cada um deles receba um tipo de comissão. Ao final, acesse os itens do embarque e faça a associação dos agentes para cada item.

Observações:  
Para as despesas internacionais de frete, seguro, outras despesas e comissões, se informado para o processo de embarque uma via de transporte que possua produto relacionado e este por sua vez estar relacionado a um serviço e possua N.B.S no cadastro de produtos, a N.B.S relacionada a despesa será desconsiderada utilizando o sistema da N.B.S do produto relacionado na via de transporte.  
Para as despesas de comissões, será utilizada a N.B.S do produto relacionado no cadastro de evento contábil relacionado à cada despesa caso não seja informado a NBS na via de transporte.

1. Ao finalizar, informe a data de embarque e grave o processo. Neste momento o sistema irá disparar as integrações financeiras para o SIGAFIN no âmbito da geração de títulos e em seguida as integrações com o módulo SIGAESS no âmbito da geração dos Processo de Aquisição de Serviço para cada despesa bem como as invoices e o câmbio de  serviço para faturameno.

**Sequencia 002** – **Conferência de geração dos pedidos de aquisição de serviço no SIGAESS para as despesas informadas no processo de embarque do SIGAEEC.**

1. No Easy Siscoserv Control (SIGAESS), acesse  **Atualizações/ Importação/ Processo Aquisição**.
2. Veja que os processos de aquisição para as despesas foram gerados.
3. Selecione o processo de aquisição referente a despesa **FRETE** e clique no botão em **Visualizar**.

Observações:

* Observe que processo de aquisição de serviço foi gerado conforme a moeda do fornecedor internacional (Ex. IENE)
* Observe que a N.B.S utilizada para a despesa é a N.B.S referente ao produto relacionado na via de transporte do processo de embarque.

1. Retorne ao browser de Pedidos, posicione sobre o processo de aquisição gerado para a despesa **FRETE** novamente e clique no botão **Invoices**.

Observações: Observe que a moeda do Pedido é diferente da moeda do faturamento e que portanto o módulo SIGAESS recepcionou os dados de valores e taxas corretamente calculando a paridade entre as duas moedas.

1. Volte à tela anterior e na parte inferior da tela clique no botão **Visualizar** para ver as informações da parcela de câmbio de serviço gerada.
2. Retorne ao browser de Pedidos, posicione sobre o processo de aquisição gerado para a despesa **COMISSAO CONTA GRAFICA** e clique no botão **Visualizar**.
3. Retorne ao browser de Pedidos, posicione sobre o processo de aquisição gerado para a despesa **COMISSAO A DEDUZIR**e clique no botão Visualizar.
4. Retorne ao browser de Pedidos, posicione sobre o processo de aquisição gerado para a despesa **COMISSAO A DEDUZIR** e clique no botão **Visualizar**.
5. Veja que as informações foram geradas corretamente e amoeda corresponde à moeda do processo de embarque no SIGAEEC.
6. Retorne ao browser de Pedidos, posicione sobre o processo de aquisição gerado para a despesa **COMISSAO CONTA GRAFICA** novamente e clique no botão **Invoices**.
7. Veja que as informações da Invoice foram geradas.
8. Volte à tela anterior e na parte inferior da tela clique no botão Visualizar para ver as informações da parcela de câmbio de serviço gerada.
9. Veja que as informações foram geradas corretamente e amoeda corresponde à moeda do processo de embarque no SIGAEEC.
10. Retorne ao browser de Pedidos, posicione sobre o processo de aquisição gerado para a despesa **COMISSAO A DEDUZIR** novamente e clique no botão **Invoices**.
11. Veja que as informações da Invoice foram geradas.
12. Volte à tela anterior e na parte inferior da tela clique no botão Visualizar para ver as informações da parcela de câmbio de serviço gerada.
13. Veja que as informações foram geradas corretamente e a moeda corresponde à moeda do processo de embarque no SIGAEEC.
14. Retorne ao browser de Pedidos, posicione sobre o processo de aquisição gerado para a despesa **COMISSAO A DEDUZIR** novamente e clique no botão **Invoices**.
15. Veja que as informações da Invoice foram geradas.
16. Volte à tela anterior e na parte inferior da tela clique no botão Visualizar para ver as informações da parcela de câmbio de serviço gerada.

Observações: A baixa do câmbio de comissão a deduzir é feita imediatamente após sua inclusão no SIGAEEC e portanto esta mesma baixa automática é refletida no câmbio de serviço no SIGAESS.  
  
**Sequência 003 – Baixa do Câmbio a pagar de despesa internacional no SIGAEEC e atualização da parcela de câmbio de serviço no SIGAESS**

1. No módulo Easy Export Control (SIGAEEC) acesse a rotina **Atualizações/ Financeiro / Câmbio**, posicione sobre o processo de embarque embarcado anteriormente e clique no botão **Alterar**. O sistema irá exibir as parcelas com seus respectivos número de título financeiro gravados.
2. Selecione novamente a parcela de evento **102- PROV.FRETE APÓS EMB** clique no botão **Ações relacionadas / Liquidar**.
3. Informe os dados da liquidação. Ao finalizar a informação nos campos clique no botão **Finalizar**. Verifique no browser de parcelas que os campos necessários à liquidação da parcela liquidada foram atualizados.
4. Confira os dados e confirme. Neste momento o sistema irá enviar os dados para baixa do título no módulo financeiro.
5. No Easy Siscoserv Control (SIGAESS), acesse **Atualizações/ Importação/ Processo Aquisição**. Posicione sobre o processo de aquisição gerado para a despesa FRETE novamente e clique no botão **Invoices**.
6. Na tela de Invoice, na parte inferior clique no botão **Visualizar** para verificar os dados da parcela de câmbio de serviço.

Observações: Verifique que os dados informados na liquidação da parcela de câmbio de despesa internacional no SIGAEEC foram atualizados na parcela de câmbio de serviço do SIGAESS.  
  
**Sequência 004 – Estorno da baixa do câmbio a pagar de despesa internacional no SIGAEEC e atualização da parcela de câmbio de serviço no SIGAESS**

1. No módulo Easy Export Control (SIGAEEC) acesse a rotina **Atualizações/ Financeiro / Câmbio**, posicione sobre o processo de embarque embarcado anteriormente e clique no botão **Alterar**. O sistema irá exibir as parcelas com seus respectivos número de título financeiro gravados.
2. Selecione novamente a parcela de evento **102- PROV.FRETE APÓS EMB**clique no botão **Ações relacionadas / Estorno da Liquidação**.
3. Verifique os dados da parcela que terá a liquidação estornada e confirme.
4. Ao confirmar os dados da parcela serão atualizados no browser das parcelas. Confirme para processar o estorno da liquidação.
5. Confira os dados e confirme. Neste momento o sistema irá enviar os dados para estorno da baixa do título no módulo financeiro.
6. No Easy Siscoserv Control (SIGAESS), acesse **Atualizações/ Importação/ Processo Aquisição**. Posicione sobre o processo de aquisição gerado para a despesa FRETE novamente e clique no botão **Invoices**.
7. Na tela de Invoice, na parte inferior clique no botão **Visualizar** para verificar os dados da parcela de câmbio de serviço.

Verifique que os dados informados no estorno da liquidação da parcela de câmbio de despesa internacional no SIGAEEC foram atualizados na parcela de câmbio de serviço do SIGAESS.
