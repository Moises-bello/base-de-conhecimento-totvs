---
article_id: 360022393931
category: Gestão de Transportes (TMS)
content_hash: 35787e3c50666913436ac8aa8d27652852091e91de5b7b4d6cf83eaac900cb07
fetched_at: '2026-06-28T22:45:27.543978+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Conferência de Coleta
type: support-article
updated_at: '2022-09-02T16:58:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022393931-Log%C3%ADstica-Linha-Protheus-TMS-Confer%C3%AAncia-de-Coleta
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:50 min**

**Dúvida**Como utilizar e para que serve o processo de **Conferência de Colet**a?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**

Esta rotina efetua um pré-lançamento das coletas efetuadas sem a necessidade de informar o peso e a quantidade de volumes coletados, uma vez que essas informações serão automaticamente preenchidas na digitação de uma nota fiscal vinculada à solicitação de coleta.  É possível realizar o apontamento da ordem de coleta que está diretamente relacionada à uma solicitação de coleta, pra vários destinatários.  
  
Desta forma, ao informar uma solicitação de coleta na entrada de notas fiscais que seja informada na conferência de coletas, a solicitação de coleta somente será finalizada mediante ao *status* **documento informado** quando a quantidade de notas fiscais digitadas atingir a quantidade informada em conferência.   
  
Com isso, é possível utilizar a solicitação de coleta em vários lotes e para vários destinatários, pois o controle do encerramento da coleta é feito pela quantidade de notas fiscais informadas na conferência de coletas.

Para utilizar a ferramenta, basta seguir os itens a seguir:  
  
**Cadastrar Solicitação de Coleta**  
  
1. Gerar uma ordem de **Coleta** através da rotina **TMSA460 - Solicitação de Coleta.**1.1. É importante se atentar aos *Status* da Coleta conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019301551/mceclip0.png)

1.2. Quando gerada a coleta, o *Status* apresentado será **Em Aberto**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019431112/mceclip1.png)

**Cadastrar Viagem de Coleta**2. Criar uma **Viagem de Coleta** apontando a coleta criada através da rotina **TMSA144 - Viagem de Coleta**, no nosso exemplo, **Coleta** 000000070.  
2.2. É importante se atentar aos *Status* da **Viagem de Coleta** conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019301831/mceclip2.png)

2.3. Quando gerada a viagem, o *Status* apresentado será **Em Aberto**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019432132/mceclip3.png)

2.3. Realize o Fechamento da Viagem em **Outras Ações>Manutenção>Fechamento>Fechar**. Após procedimento, *Status* da **Viagem** irá mudar para **Fechada**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019432172/mceclip4.png)

2.4. Realize o Processo de informar Operações em **Outras Ações>Manutenção>Operações**. Após procedimento, *Status* da Viagem irá mudar para **Chegada em Filial**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019303611/mceclip8.png)

**Cadastrar Conferência de Coleta**3. Com a **Viagem** nesse *Status*, já é possível criar a **Conferência de Coleta** através da Rotina **TMSA461 - Conferencia de Coletas**. Na tela de Inclusão, informar a viagem, no nosso exemplo a viagem 000079, data e hora de **Coleta** informado no item **2.4.**, a **Coleta** criada, no nosso exemplo, **Coleta** 000000070, e a quantidade de **Notas Fiscais** que serão utilizadas com a **Coleta**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019433692/mceclip10.png)

3.1. É importante se atentar ao *Status* da **Conferência de Coleta** conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019304631/mceclip12.png)

3.2. Quando gerada a **Conferência**, o *Status* apresentado será **Em Aberto**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019304611/mceclip11.png)

3.3. A partir desse momento, a Coleta mudará o *Status* para **Em Conferência**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019433992/mceclip13.png)

**Parâmetros**4. Antes de iniciar o processo de vincular a coleta a **Notas Fiscais**, é preciso ajustar 2 parâmetros para que o processo ocorra corretamente sendo eles:  
4.1. **MV\_OCORCOL:** Deve ser preenchido com o código da **Ocorrência** cadastrada na rotina **TMSA020 -** **Tabela de Ocorrências** do tipo **01 - Encerra Processo - DT2\_TIPOCO** para o Serviço de Transporte **1 - Coleta -** **DT2\_SERTMS**.  
4.2. **MV\_ENCVIAG:**. O mesmo encerra a viagem após apontamento do última nota informada na conferência. Quando está com o valor 1, encerrar a viagem automaticamente, quando 2, não encerra.  
  
**Vincular Notas Fiscais a Coleta**5. Criar lote informando a **Coleta** e os dados para transporte, como remetente, destinatário, pagador do frete, serviços e dados da **Nota Fiscal**, através da Rotina **TMSA050 - Entrada Documentos de Clientes**.  
5.1. Executar o processo informando a Coleta a mesma quantidade de vezes informada no campo **Quantidade de Documentos definidos -** **F6\_QTDENF**, no nosso exemplo, informamos a quantidade 2.  
5.2. Após gerar lotes com a quantidade de coletas informada, a Coleta já não fica mais disponível para seleção, mudando seu *Status* para **Documento Informado**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019439692/mceclip14.png)

5.3. Perceba que a Conferência mudou de *Status* para **Encerrada**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019439892/mceclip15.png)

5.4. Conforme os parâmetros informados nos itens 4.1 e 4.2, a **Viagem de Coleta** também estará com o *Status* **Encerrada**, terminando o processo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019310091/mceclip16.png)

Caso seja necessário utilizar mais notas para a coleta após encerrado, ao preencher o campo **F6\_QTDENF** com o novo valor, o Sistema estorna a operação de encerramento de processo e libera a coleta até que o novo valor seja atingido, executando novamente o passo 5.2 até 5.4.
