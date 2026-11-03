---
article_id: 11735592546583
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: e800b9a243ca588387dc4684c5fdd9c5f0b4cbc14024edc18a7e847f6add196f
fetched_at: '2026-06-28T22:37:20.315330+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Adiantamento em Contratos
  (Nova Funcionalidade) x Compensação Automática do Título PA do Contrato com Título
  do Documento de Entrada
type: support-article
updated_at: '2026-04-08T13:26:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11735592546583-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Adiantamento-em-Contratos-Nova-Funcionalidade-x-Compensa%C3%A7%C3%A3o-Autom%C3%A1tica-do-T%C3%ADtulo-PA-do-Contrato-com-T%C3%ADtulo-do-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17916428486935) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Adiantamento em Contratos (Nova Funcionalidade) x Compensação Automática do Título PA do Contrato com Título do Documento de Entrada.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Para o módulo de Gestão de Contrato, no passo a passo abaixo será demonstrado como Cadastrar o Adiantamento com a Nova funcionalidade de Compensação Automática do Título gerado pelo Adiantamento de Contratos com o Título do Documento de Entrada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11735085989271)

**Importante:** Por enquanto esse processo só está disponível para contratos de Compra e para rotina nova medição(CNTA121)

* Para utilizar a Nova funcionalidade de Adiantamento de Contratos é necessário que na Inclusão do Contrato selecione uma Condição de Pagamento com o campo **Adiantamento = Sim.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11735243755799)

* Para que o sistema realize a compensação automática é necessário que os parâmetros **(F12) da rotina Contas a Pagar (FINA050)**, a qual é executada internamente no Contrato para a inclusão do título PA , para que, na inclusão do título PA seja gerado o movimento bancário de pagamento desse PA, para que aí sim, na inclusão do documento de entrada com esse PC de Contratos vinculado, possa haver a compensação automática do PA e do título NF ( gerado pelo documento de entrada ) :

**Gerar Chq. p/Adiant.?= NÃO**  
**Mov. Banc. sem Cheque?= SIM**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11735471259031)

- Acessar a Rotina Manutenção(CNTA300) "**Outras Ações> Adiantamento"**preencher os dados para inclusão do Adiantamento > Salvar.

- Incluir a Nova Medição (CNTA121) e na Aba "Adiantamentos" verificar o Adiantamento incluido para o contrato, e informar o valor no campo **"Vl.Adiant" (CZY\_VALOR)** na Medição informando o valor que será vinculado a medição para ser vinculado ao Pedido gerado e compensado ao se gerar a NF deste Pedido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39598903738391)

- Encerrar a Medição para que o Pedido de Compras possa ser gerado com o vinculo na Tabela "FIE" com o PA do Adiantamento do Contrato.

**Obs1:**

Nesse momento Será criado a tabela FIE com a amarração do PA com o Pedido de Compras gerado pela Medição.

- Vincular o Pedido de Compra (MATA120) gerado pelo Contrato no Documento de Entrada (MATA103) com uma Condição de Pagamento que gera Duplicata, e preencher as informações da nota. Ao "Salvar" a Nota, o Título dessa NF será compensado com o título do adiantamento do Contrato Automaticamente.

**Obs2:**

**Pergunta:** Esta nova funcionalidade da compensação automática é disponível quando a medição é feita em uma Filial diferente da FIlial origem do Contrato ?

**Resposta (Conf. DTEXPRO-1961):** Não. Com o compartilhamento nativo da tabelas de Contas a Pagar de forma Exclusiva a compensação automática da funcionalidade é desabilitada caso seja feita medição em filial diferente da filial do Contrato.

No padrão do sistema do processo de Adiantamento gera a amarração do pedido (SC7) com os títulos (SE2) do Adiantamento na filial de origem do contrato (CND\_FILCTR), dessa forma, a possibilidade existente para se utilizar o processo adiantamento com a medição em filial distinta a do contrato é apenas estando a tabela dos títulos (SE2) de forma Compartilhada.

**Obs3:** Caso ocorra o **Help Vl.Adiant**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36382703122711)**

**Valor limite de adiantamento:**  
A soma dos adiantamentos em aberto (ainda não utilizado em medições), vinculados ao contrato não pode ultrapassar ao saldo do contrato (CN9\_SALDO). Caso o valor do adiantamento que está sendo incluído somado aos adiantamentos em aberto ultrapasse o saldo do contrato, o sistema emitirá o aviso: "Valor do Adiantamento superior ao saldo do Contrato.

**Obs4:**

O Help A120TOTLIB verifica se o valor de um adiantamento pode ser vinculado a um pedido de compra ou venda sem exceder o saldo disponível no contrato. Ela checa os adiantamentos já feitos, compara com o novo valor, e decide se o adiantamento é permitido. Se o valor do novo adiantamento, somado aos anteriores, for maior que o saldo permitido no contrato, o sistema alerta e bloqueia o processo. Se tudo estiver correto, o sistema permite a inclusão do adiantamento. Isso garante que os adiantamentos estejam dentro dos limites financeiros definidos no contrato.

**Obs5:**

O Help A120NOSDADT valida a parte financeira somando os títulos PA para que não sejam excedidos os limites financeiros associados a um pedido

**Obs6:**

Existe algum parâmetro ou funcionalidade para  alteração do número do título de adiantamento que será gerado no financeiro?

**R:** No padrão não existe nenhum parâmetro ou funcionalidade , caso tenha interesse em personalização do sistema segue abaixo os pontos de entrada do processo de adiantamento.

[CN100ANT - Gravação de Campos Customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089710)

[CN100ADI - Gravação dos campos customizados](https://tdn.totvs.com/pages/releaseview.action?pageId=6089624)

**How To:**

Saiba como cadastrar Adiantamento em Contratos (Nova Funcionalidade) x Compensação Automática do Título PA do Contrato com Título do Documento de Entrada acessando nossa pagina no YouTube:

[How To | MP-SIGAGCT - Adiantamento x Compensação Automática|](https://www.youtube.com/watch?v=c-gCU9JXZmU)

***Saiba Mais:***

[GCT0025\_Adiantamento\_GCT](https://tdn.totvs.com/display/PROT/GCT0025_Adiantamento_GCT)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar Adiantamentos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034126414-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-Adiantamentos-no-Gest%C3%A3o-de-Contratos)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Adiantamento no Pedido de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Adiantamento-no-Pedido-de-Compras?source=search)

[MP - SIGACOM - Documento de Entrada atrelado a título do tipo PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567072-MP-SIGACOM-Documento-de-Entrada-atrelado-a-t%C3%ADtulo-do-tipo-PA-)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
