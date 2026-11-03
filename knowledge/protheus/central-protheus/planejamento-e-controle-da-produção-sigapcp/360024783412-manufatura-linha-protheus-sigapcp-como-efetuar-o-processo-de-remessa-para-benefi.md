---
article_id: 360024783412
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3ad5940d827ac9a3a5acca6921c2c7d2ca691d24d7b4466e06ff7e34397821f1
fetched_at: '2026-06-28T22:42:41.094110+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como efetuar o processo de remessa
  para beneficiamento
type: support-article
updated_at: '2024-10-29T16:25:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024783412-Manufatura-Linha-Protheus-SIGAPCP-Como-efetuar-o-processo-de-remessa-para-beneficiamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27412580801303)***Tempo aproximado para leitura: **00:05:30 min****Dúvida**Qual é o processo **macro de beneficiamento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Abaixo há o exemplo referente a um processo genérico de**BN - Beneficiamento**. Neste exemplo vamos enviar um fio, que possui bitola de 8mm, para que um fornecedor o processe e retorne com nova bitola de 1mm.

1. Cadastramento de produtos:  
   **FIO 1mm** - Tipo **PA - Produto acabado**: este código representará o produto após ser beneficiado.  
   **FIO 8mm** - Tipo **BN**: este código representará o produto antes de ser beneficiado.  
   **BENEFICIAMENTO** – Qualquer tipo, exceto **BN**, exemplo: **SV**: este código representará a contratação e aquisição do **Serviço** de beneficiamento junto ao fornecedor.
2. Cadastramento da estrutura:  
   **FIO 1mm**  
   |\_ **FIO 8mm**: Quantidade = 1, Qtd. Fix/Var = Variável  
   |\_ **BENEFICIAMENTO**: Quantidade = 1, Qtd. Fix/Var = Fixa
3. Cadastramento de **TES - Tipos de entrada e saída**:  
   **501 – Saída, Controle Terceiros = Remessa e Estoque = Sim**: esta **TES** será utilizada para realização da remessa para beneficiamento do produto **FIO 8mm**.  
   **001 – Entrada, Controle Terceiros = Não e Estoque = Sim**: esta **TES** será utilizada para registro da compra do serviço de beneficiamento.  
   **002 – Entrada, Controle Terceiros = Devolução e Estoque = Sim**: esta **TES** será utilizada para realização do retorno referente a remessa de beneficiamento do produto **FIO 8mm**.  
   Lembrando que os números para as **TES** são apenas sugestões.
4. Saldos Iniciais:  
   Inclusão de saldos iniciais para o produto **FIO 8mm** de 10 unidades.
5. Abertura da **OP - Ordem de Produção**:  
   Inclusão de **OP** para o produto **FIO 1mm** de 10 unidades. Neste momento, se o parâmetro **MV\_GERASC - Gera Solicitacao de Compra a partir da inclusão da Ordem de Produção** estiver ativo, será gerada solicitação de compra de 1 unidade do produto **BENEFICIAMENTO**, indicando a necessidade de contratação do serviço de beneficiamento, e, se o parâmetro **MV\_EMPBN** - **Indica se devem ser gerados empenhos de Ordens de Produção para componentes do tipo BN** estiver ativo, o empenho de 10 unidades do produto **FIO 8mm**.
6. Geração do pedido de compra:  
   A partir da solicitação de compra gerada para o produto **BENEFICIAMENTO**, realizar processo de compra de modo a determinar o fornecedor que realizará o serviço de beneficiamento. Este processo resultará na geração de um pedido de compra para o produto **BENEFICIAMENTO**.
7. Geração de documento de saída, remessa para beneficiamento:  
   Inclusão de documento de saída **tipo B**, utiliza fornecedor, com **TES** **501** para o produto **FIO 8mm** com quantidade 10. Se o parâmetro **MV\_EMPBN** estiver ativo, na geração do pedido de venda, deve ser utilizada a opção **Beneficiamento** para vínculo com a **OP**. Caso contrário não ocorrerá a liberação de estoque do pedido impedindo assim a emissão do documento de saída.
8. Entrada da nota fiscal:  
   Inclusão de documento de entrada tipo normal com dois itens conforme a seguir:  
   Item 1: Produto **BENEFICIAMENTO**, **TES** **001**, **OP** deve ser preenchida, se utilizado **PC** será carregado automaticamente.  
   Item 2: Produto **FIO 8mm**, **TES 002**, **OP** deve ser preenchida.  
   Se o parâmetro **MV\_EMPBN** ativo e a remessa de beneficiamento foi feita através da opção **Beneficiamento**, pode ser utilizada a opção **Retorno Ben**. para preenchimento dos itens do documento de entrada de forma automática a partir dos dados da remessa. Para isto, devem ser configurados os parâmetros **MV\_PRNFBEN** **- Habilita funcionalidade para automação do processo** e **MV\_TMPAD - Tipo de movimentação padrão para produção PCP**. Se utilizado este recurso, ao confirmar a inclusão do documento de entrada, a **OP** que transforma **FIO 8mm** em **FIO 1mm** será realizada automaticamente, sem a necessidade de execução do passo seguinte.
9. Apontamento da **OP**:  
   Inclusão de apontamento de produção para o produto **FIO 1mm** de 10 unidades, representando a transformação do produto **FIO 8mm** em **FIO 1mm** e, assim, encerrando o processo.

**Importante**Considerações sobre os parâmetros citados no processo:

* **MV\_EMPBN**: o produto tipo **BN** tem como característica, na instalação padrão do Sistema, não gerar empenhos para ordens de produção e assim possibilitar a emissão dos documentos de saída referente a remessa para beneficiamento, do contrário ocorreria bloqueio de estoque. Este fato pode gerar ônus aos clientes que se baseiam na lista de empenhos para trabalharem requisições. Assim, o referido parâmetro habilita a geração de empenhos para os produtos deste tipo. Em complemento, para que seja possível a confecção de um pedido de venda para remessa de beneficiamento sem o bloqueio de estoque em função do empenho para a **OP**, deverá ser utilizada a opção **Beneficiamento** no ato da confecção do pedido. Desta forma o Sistema permitirá a saída de material empenhado para a **OP**, uma vez que se trata de remessa para beneficiamento.
* **MV\_PRNFBEN**: este parâmetro habilita a utilização do recurso **Retorno Ben.** na inclusão de documentos de entrada. Este recurso pode ser utilizado para automatizar a digitação do documento de retorno de beneficiamento e o apontamento da **OP** utilizada para tal processo.
* Necessária também a configuração do parâmetro **MV\_TMPAD**, com o tipo de movimento a ser utilizado para esta produção.
* Como o processo automatiza o apontamento da OP, os itens envolvidos nesta OP precisam estar disponíveis no estoque, ou seja, os itens precisam ter estoque suficiente para que o apontamento ocorra com sucesso.
* Lembrando que esta documentação se trata de um processo macro. Cada situação ou dúvida deve ser tratada no módulo correspondente.

**Saiba mais**Para saber sobre o recebimento de beneficiamento acesse: [Processo para recebimento de Beneficiamento com MP de Terceiros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025818694--MP-SIGAEST-Processo-para-recebimento-de-Beneficiamento-com-MP-de-Terceiros?source=search)
