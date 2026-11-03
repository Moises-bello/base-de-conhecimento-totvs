---
article_id: 360025518774
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 838a87ed1e8caab93a4b65f59fe9d49fb333291c7d302b33cfd86472f43a5b0a
fetched_at: '2026-06-28T22:38:54.157243+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina MATA175 - Instruções
  padrões sobre Controle de Qualidade no Estoque
type: support-article
updated_at: '2026-06-08T20:33:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque
---

O Controle de Qualidade (CQ) no Protheus é usado para inspecionar produtos antes do armazenamento padrão, com produtos podendo ser liberados ou rejeitados no almoxarifado CQ, definido pelo parâmetro MV\_CQ. Movimentações no CQ devem ser feitas pela rotina BAIXAS DO CQ (MATA175). Produtos são enviados ao CQ por nota fiscal, transferências, produção, movimentos internos, entre outros. O sistema registra as movimentações no arquivo SD7 e permite relatórios específicos para controle e análise.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21158943857687) Tempo aproximado para leitura: **00:10:00 min**

**Dúvida**  
O que é preciso saber sobre o Controle de Qualidade e Baixa de C.Q no *Protheus?*

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
**Veja um exemplo simulado de Baixa de CQ abaixo:**

**"CQ" (Controle de Qualidade)** é um método utilizado para verificação da qualidade de determinado produto. Quando determinado produto precisa ser inspecionado, verificado e/ou testado, o mesmo deve ser enviado ao CQ antes do Armazém padrão.

Quando um produto estiver no CQ poderá ser "Liberado" ou "Rejeitado". Quando "Liberado" o produto é transferido para outro almoxarifado (como "*default*" é enviado ao local padrão - B1\_LOCPAD), e se for "Rejeitado" fica aguardando sua devolução (como "*default*" fica no almoxarifado CQ, mas também pode ser rejeitado e enviado a outro almoxarifado).

**POR PADRÃO:**O local 98 não é um armazém que já EXISTE nativamente no Protheus, ele apenas existe como referencia no parâmetro MV\_CQ, dessa forma é obrigatório a criação desse armazém fisicamente, que pode ser realizada pela rotina AGRA045 (Locais de estoque), uma vez que o cliente pode definir qual o código de armazém ele prefere para o controle, não é obrigatório ser exatamente código 98. **Após definido uma vez, só será possível alterar o armazém CQ, após zerar todo o saldo do do armazém.**

***Informações importantes*** **sobre a Baixa de C.Q**

* Enquanto o saldo do produto estiver no CQ **somente poderá ser movimentado pela rotina BAIXAS DO CQ (MATA175)**;
* O almoxarifado CQ é definido pelo parâmetro MV\_CQ, e como padrão é "98";
* Ao definir o parâmetro MV\_CQ  e efetuar movimentações, esse parâmetro não pode ser mais alterado;
* Caso precisar alterar o parâmetro MV\_CQ, deve efetuar todas as Baixas e/ou Rejeições pendentes, para em seguida alterar o parâmetro, ou seja, não pode ter saldo no Armazém de CQ para alteração do parâmetro
* **Não incluir** Saldos Iniciais diretamente pela **rotina MATA220**, o saldo não constará para Baixas na tabela SD7. Obs.: Nesse caso incluir em um Armazém padrão e transferir o Saldo pela rotina MATA261 ao CQ;
* As informações referentes ao CQ ficarão armazenadas no arquivo SD7;
* O campo B1\_TIPOCQ deverá conter o tipo de CQ a ser utilizado pelo sistema. Se for igual a "M" (Materiais) irá atualizar somente o arquivo SD7; se for igual a "Q" (SigaQuality) irá atualizar o arquivo SD7 e todos os arquivos necessários no SIGAQIE.
* Produtos que utilizam controle de Localização devem ser endereçados antes de serem movimentados no CQ (deverão ser criadas localizações físicas do almoxarifado CQ para a distribuição). Para estes produtos a Liberação ou Rejeição também deverá ser distribuída antes de qualquer outra movimentação (Ex.: para se fazer uma NF de devolução (NF de SAIDA) de um produto com localização rejeitado no CQ deve-se antes distribui-lo)
* Para os produtos que utilizam controle de Localização é possível utilizar o parâmetro MV\_DISTAUT para endereçar em um endereço automaticamente. [*Clique aqui e veja a FAQ.*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10668896901015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Armaz%C3%A9m-CQ-endere%C3%A7ar-automaticamente-MV-DISTAUT-Como-configurar-)
* **Qual o tipo de movimento gerado na baixa de qualidade:** Por padrão é gerado os movimentos de tipo RE6/DE6 para baixas com origem de uma nota de entrada, e RE4/DE4 para casos de origem de liberação de um processo de produção PR0, e caso queira alterar o tipo do movimento, pode-se utilizar o parametro [MV\_PROCQE6](https://tdn.totvs.com/pages/releaseview.action?pageId=312165251#:~:text=do%20Custo%20M%C3%A9dio.-,MV_PROCQE6,-Indica%20a%20utiliza%C3%A7%C3%A3o) para considerar os tipos RE6/DE6 na liberação de "produção".

**Um produto pode ser enviado para o CQ pelos seguintes processos:**

***1 - NF Entrada, através de "Insuficiência de Nota" ou "Skip-Lote":***

- **Insuficiência de Nota**: Através do campo B1\_NOTAMIN pode-se definir uma Nota Mínima ao Produto. Esta nota será utilizada como parâmetro de Qualidade deste Produto, e comparado com a nota atribuída no campo A5\_NOTA da Amarração Produto X Fornecedor (MATA061). Se a nota contida no campo A5\_NOTA for inferior a nota do campo B1\_NOTAMIN o sistema irá considerar que o produto em questão possui qualidade inferior quando é distribuída por este Fornecedor, e enviara o produto ao CQ. Deste modo pode-se enviar um produto ao CQ de acordo com seu fornecedor.

**Exemplo**:

***Produto A*** - Nota 08 (Exige armazenamento cauteloso, entrega rápida)  
***Fornecedor 1*** - Nota 10 (Qualidade no armazenamento e entrega no prazo)  
***Fornecedor 2*** - Nota 05 (Armazena ao ar livre e a entrega demora)

Se o Produto A for entregue pelo Fornecedor 1 não precisa passar pelo CQ, pois sua qualidade é comprovada, mas se o mesmo produto for entregue pelo Fornecedor 2 deve ser submetido ao controle de qualidade. Notas Fiscais com a combinação Produto X Fornecedor correta serão enviadas automaticamente ao CQ.

- **Para utilizar por Skip-Lote**: Configurar os seguintes campos: **A5\_TIPATU igual a (1) Skip Lote**, o campo **A5\_SKIPLOT** **deve conter o número de intervalos** a serem considerados para que o produto seja enviado ao CQ (Exemplo: Se desejar enviar o produto para o CQ a cada 2 NF's de entrada esse campo deve ser igual a 2 - se este campo for preenchido com 1 todas as NF's serão enviadas ao CQ) A cada vez que o intervalo de Skip-Lote for atingido em uma NF de entrada o produto será enviado para o CQ. Observações: A cada NF emitida para a Amarração Produto X Fornecedor será incrementado 1 ao campo A5\_ENTREGA. Quando o valor nesse campo for igual ao valor do A5\_SKIPLOT o produto será enviado ao CQ.

**Exemplo how to de configuração Skip-Lote:**

***2 - Transferências:***  
Sempre que um produto for transferido para o almoxarifado de CQ (Ex.: 98), o produto será enviado ao CQ e aguardar uma nova Liberação.

***Observações importantes.:*** Toda movimentação que foi enviada para o Armazém de CQ (MV\_CQ) somente poderá ser movimentada através da Baixa do CQ (MATA175). Não existe funcionalidade nas rotinas de Transferências (MATA260/MATA261) que permita transferir do Armazém de CQ para para um Armazém padrão. Ou seja, o produto será inspecionado pela Qualidade antes da movimentação. Salvo efetuar o estorno da movimentação original.

***3 - Produção:***  
Para que um produto seja enviado ao CQ quando da sua produção são necessários alguns passos:

**-** No Cadastro de Produtos o campo **B1\_NUMCQPR** ("Produções CQ") deve conter o número de intervalos a serem considerados para que a produção seja enviada ao CQ.

***Exemplo:*** Se desejar enviar o produto ao CQ a cada 2 produções este campo deve conter 2. Se o campo for preenchido com 1 todas as produções serão enviadas ao CQ.  
Obs.: A cada produção deste produto será incrementado 1 ao campo B1\_CONTCQP. Quando o valor deste campo for igual ao valor do campo **B1\_NUMCQPR** a produção será enviada ao CQ e o campo B1\_CONTCQP será zerado.

**-** O Tipo de Movimentação utilizado (F5\_CODIGO = <500 e F5\_TIPO = "P") deve ter o campo **F5\_ENVCQPR** ("Envia Produções ao CQ?") preenchido com "S"  
Será enviado ao CQ um produto com os campos supracitados preenchidos corretamente, e onde o Tipo de Movimentação-Produção indicado acima for utilizado.

***4 - Inclusão de Movimento Interno devolvendo saldo diretamente no Armazém de CQ (MV\_CQ):***  
Pelas rotinas de Movimentos Internos (MATA240/MATA241) pode incluir saldo devolvendo (ENTRADA) o produto no Armazém de CQ, o mesmo fica disponível para Baixa na rotina MATA175;

***Obs.:*** Não é possível requisitar pelas rotinas de Movimentos Internos (MATA240/MATA241) diretamente no Armazém de CQ (MV\_CQ)

***5 - Notas Fiscais tipo Beneficiamento (Cliente) somente podem ser incluídas através de customização com o Ponto de Entrada ENVCQMAT.***

ENVCQMAT - Envio de Material para o CQ  
<https://tdn.totvs.com/display/public/PROT/ENVCQMAT+-+Envio+de+Material+para+o+CQ>

***6 - Inventário incluindo saldo no Armazém de CQ (MV\_CQ):***  
Caso identificar diferença de saldo no Armazém de CQ, é possível efetuar o [*processo de inventário (MATA270/MATA340)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque) **apenas devolvendo (ENTRADA)** o produto no Armazém de CQ. O saldo devolvido ficará disponível para Baixa na rotina MATA175;

***Observações importantes******:*** Não é possível efetuar inventário diminuindo o saldo pelas rotinas de Inventário (MATA270/MATA340). Nesse cenário é obrigatório efetuar a Baixa do CQ para o Armazém padrão e inventariar diretamente no Armazém padrão.

***7 - Transferido de outra Filial pela rotina MATA310 com o parâmetro MV\_M310TRV configurado:***  
É possível receber o Saldos que constam no **Armazém de CQ** de outra Filial com a configuração como indicado nesse link ([clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5875115319447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-transfer%C3%AAncia-entre-filiais-MATA310-via-Controle-de-Qualidade-CQ)). Observações importantes: Essa funcionalidade esta disponível apenas na rotina MATA310 como indicado na FAQ.

***8 - Produto sucata configurado na estrutura com o quantidade negativa, sendo direcionado para a baixa do CQ, sendo que o mesmo não tem configuração de qualidade no cadastro do produto:***

Como configurar para que o **produto sucata** ***não seja enviado*** para baixa da qualidade, pela rotina MATA175. (ISSUE DMANMAT01-48461)

É necessário avaliar no configurador se o parâmetro MV\_QIPMAT = N, e também verificar no configurador se o parâmetro **MV\_PRAPONT configurado igual a 1** (**Tipo de Movimentação)** alterar parâmetro para o conteúdo igual 2 (**Cadastro de Produto)** dessa forma o produto sucata, negativo na estrutura não será enviado para baixa de qualidade(MATA175).

**Para mais informações sobre o parâmetro:**

[Manufatura - Linha Protheus - SIGAPCP - Parâmetro MV\_PRAPONT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046693993-Manufatura-Linha-Protheus-SIGAPCP-Par%C3%A2metro-MV-PRAPONT)

***Opções de Baixas do CQ:***

No menu Atualizar->Movimentos Internos existe a opção "Baixas do CQ". Esta é a opção utilizada para se movimentar os produtos que estão no CQ. Pode-se "Liberar/Rejeitar" ou "Estornar" as movimentações.

**\* Liberar/Rejeitar:** Ao se selecionar esta opção será mostrada uma tela com dados do produto e na GetDados um registro do tipo "0" (ZERO), que representa a entrada do produto no CQ. Para se Liberar ou Rejeitar deve-se incluir uma nova linha na GetDados, e preencher o campo "Tipo" com **1 (para Liberar)** ou **2 (para Rejeitar)**. Pode-se, por exemplo, incluir 1 linha para Liberar parte do produto e incluir mais 1 linha para Rejeitar outra parte.

**\* Estorno:** Só poderá ser acessada quando alguma movimentação no CQ tiver sido feita - Sobre a Movimentação de Liberação ou Rejeição pressiona-se [Enter] sobre o campo "Estorno" para que o campo seja marcado com um "X". As linhas marcadas terão as movimentações estornadas - e serão geradas novas linhas referentes aos estornos (Tipos 6 e 7 (\*)).

Para se EXCLUIR uma movimentação no CQ (deletando os registros referentes a ela no SD7) deve-se primeiramente estornar todas as movimentações feitas (se houver), e então excluir a movimentação que gerou o envio ao CQ (NF, Produção ou Transferência).

**\* Transferir pela rotina MATA310 para outra Filial** utilizando o **parâmetro MV\_M310TRV.** [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5875115319447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-transfer%C3%AAncia-entre-filiais-MATA310-via-Controle-de-Qualidade-CQ) e confira uma passo a passo sobre como utilizar essa funcionalidade.

***OBS:** Quando um produto é rejeitado (e assim mantido no Armazém de Qualidade - MV\_CQ) o mesmo fica aguardando que seja efetuada a **devolução de compra ao Fornecedor que o enviou o produto rejeitado**. Em caso de rejeição indevida, somente é possível efetuar o estorno da rejeição em um período aberto. Em casos de períodos fechados, é necessário efetuar a reabertura de Estoque, estornar a rejeição, e em seguida efetuar uma nova baixa ou rejeição para o Armazém correto. Somente é possível retirar do Armazém de CQ dessa forma (não há como transferi-lo ou estornar a rejeição para períodos fechados).*

***(\*) Os Tipos de Registros (D7\_TIPO) Possíveis são:***

**0 -** Movimentação Original (a que entrou primeiramente no CQ);  
***1 -*** Movimento de Liberação;  
***2 -*** Movimento de Rejeição;  
***3 -*** Transferido para outra Filial com o [**parâmetro MV\_M310TRV**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5875115319447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-transfer%C3%AAncia-entre-filiais-MATA310-via-Controle-de-Qualidade-CQ);  
***4 -*** Exclusão do Documento de Saída Transferido pelo parâmetro MV\_M310TRV;  
***5 -*** Alteração de data de validade pelo CQ quando o [**parâmetro MV\_A175VLD**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058472673-MP-SIGAEST-MV-A175VLD-habilitado-como-alterar-a-Data-de-Validade-de-Produtos-com-controle-de-Lote)habilitado  
***6 -*** Estorno da Liberação;  
***7 -*** Estorno da Rejeição;  
***8 -*** Despesas Agregadas (NF de Complemento de Frete ou Despesas de Importação);  
***9 -*** Estorno de Despesas Agregadas

**Tratamento de Custo no C.Q (para casos em que a NF de Entrada teve agregação de custo de frete, despesas, etc)**

É recomendado que seja criado um local (armazém) de rejeição, que pode ser um local físico onde a qualidade retira da área de qualidade e move para o setor de rejeições e devoluções ou mesmo um local fictício em que a qualidade rejeita naquele local mas fisicamente fica na área da qualidade para ser devolvido.

No caso de produtos que foram para a qualidade e **não tiverem nenhum custo agregado**, como valor de frete, **a rejeição pode ser mantida no local de CQ e ser feita a devolução diretamente do local de CQ**, isto porque no pedido de devolução será feita a amarração com a nota de entrada e o custo será referente somente a nota de entrada.

No Caso de produtos **que tenham custos agregados**, como valor de frete, este custo não pode ser devolvido e deverá ser pago, então este custo precisa fazer parte do custo do estoque. Para tanto **deve ser rejeitado para um local diferente de CQ,** assim todo o custo passa a fazer parte do custo de estoque, tanto o custo do produto como o custo de frete, e ao devolver o produto, o custo será referente a nota de entrada na amarração do pedido de devolução, mantendo o custo do frete no estoque.

Em ambos os casos o mais interessante seria ter um armazém (local) de rejeição e a partir dele ser devolvido ou até mesmo requisitado para refugo.

**Tratamento de Custo no C.Q referente a** **Movimentações Internas Valorizadas** **de Acerto de Custos**

No Armazém de Qualidade (MV\_CQ), as movimentações Internas Valorizadas, ***não*** ***geram registros (SD7)*** de **Despesas Agregada (D7\_TIPO=8)** na rotina Baixas do CQ (MATA175). Nesse cenário ***é recomendado*** que seja efetuado a Liberação ou Rejeição a um Armazém Padrão e o ajuste de custo deve ocorrer no Armazém padrão.

***Observações:*** Caso, seja efetuado movimentação de ajuste de Custos no Armazém de CQ, esse valor fica preso nesse Armazém, a menos que seja estornado o movimento em período aberto.

### **Existe relatorio para verificar as movimentações da Baixa?**

* MATR175 - Relação de Baixas do CQ
* [Smart View - Relação de Baixas do CQ](https://tdn.totvs.com/pages/releaseview.action?pageId=807213016)

### **Duvidas pontuais:**

* Na rotina de apontamento parcial de produção, para um mesmo código de produto e lote, são exibidas múltiplas ocorrências na tela de **liberação de CQ**.  
  Esse comportamento gera retrabalho para a área de qualidade, pois o mesmo lote precisa ser liberado várias vezes. É possível **aglutinar todos os apontamentos de um mesmo lote em uma única opção de liberação**?

  *R: No padrão do produto, **essa possibilidade não existe**, pois não há ponto de entrada específico para realizar a aglutinação de lotes na liberação da baixa de qualidade.*

  [*Cross Segmento – TOTVS Backoffice (Linha Protheus) – SIGAEST – MATA175 – Pontos de Entrada da rotina de Baixa de CQ.*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004325941-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-Pontos-de-Entrada-da-rotina-Baixa-de-CQ)

  *Caso haja interesse, a alternativa é utilizar o modelo de **desenvolvimento participativo**, no qual é possível solicitar a criação desse ponto de entrada mediante faturamento.*

  *Se desejar, podemos encaminhar um **script** para preenchimento e proceder com a abertura de uma **ISSUE de apoio ao desenvolvimento**, formalizando a proposta para análise de viabilidade e faturamento do ponto de entrada.*
* *Caso desejar desativar para o produto não ser mais enviado ao CQ de forma automática (por NF ou produção), basta alterar os campos* **B1\_NOTAMIN** *e* **B1\_NUMCQPR** para 0.

**Saiba mais:**

[*MP - SIGAEST - NF de frete não compõe o custo do produto rejeitado no Armazém de CQ após devolver ao fornecedor*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063880373-MP-SIGAEST-NF-de-frete-n%C3%A3o-comp%C3%B5e-o-custo-do-produto-rejeitado-no-Armaz%C3%A9m-de-CQ-ap%C3%B3s-devolver-ao-fornecedor)

[*SIGAEST - Configuração de transferência entre filiais (MATA310) via Controle de Qualidade (CQ)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5875115319447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-transfer%C3%AAncia-entre-filiais-MATA310-via-Controle-de-Qualidade-CQ)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
