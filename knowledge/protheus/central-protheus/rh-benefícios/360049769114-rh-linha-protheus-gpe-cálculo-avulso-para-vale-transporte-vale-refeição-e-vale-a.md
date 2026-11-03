---
article_id: 360049769114
category: RH - Benefícios
content_hash: f576b901a7ad9108f4acbd9d1e226e1ffba4b33763f26cf4ccbd2e01eec36e49
fetched_at: '2026-06-28T22:44:03.414938+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE -  Cálculo avulso para Vale Transporte, Vale Refeição
  e Vale Alimentação
type: support-article
updated_at: '2025-09-12T13:04:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049769114-RH-Linha-Protheus-GPE-C%C3%A1lculo-avulso-para-Vale-Transporte-Vale-Refei%C3%A7%C3%A3o-e-Vale-Alimenta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32735536493719) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como realizar cálculo avulso para benefícios como Vale Transporte, Vale Refeição e Vale Alimentação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**

Além de realizar o cálculo mensal padrão dos benefícios, considerando os vales vinculados ao funcionário na rotina de atualização e os dias do período ativo para o benefício, é possível calcular mais de um pedido dentro do mesmo período, realizando um cálculo avulso.

**Atenção:** Para realizar o cálculo de mais de um pedido, é necessário que o pedido anterior esteja concluído. O sistema verifica o campo R0\_PEDIDO e caso esteja em aberto, o cálculo irá sobrepor o registro. Para alterar o status do pedido, basta gerar o [Arquivo de Integração - BENEFARQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015541491-RH-Linha-Protheus-GPE-Como-gerar-arquivo-de-integra%C3%A7%C3%A3o-de-benef%C3%ADcios-utilizando-a-rotina-BENEFARQ) ou alterar o campo manualmente.   
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32735502277911)**

Abaixo, alguns exemplos de utilização do cálculo avulso para Vale Transporte, Vale Refeição e Vale Alimentação:

**1. Aumentar a quantidade de vales em um determinado período**

Nesse exemplo, já temos um Vale transporte vinculado ao funcionário, com um vale por dia. O cálculo mensal já foi realizado e o arquivo de integração foi gerado, portanto o pedido está concluído.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075169794)

Durante uma semana, o funcionário precisou de mais um vale por dia para chegar ao trabalho. Para calcular esses vales adicionais, é realizado um **Cálculo Periódico** do vale transporte.  
Como o vale que será calculado é o mesmo que já está vinculado ao funcionário, não será necessário realizar nenhuma alteração na rotina de Atualização de Benefícios.  
  
No momento do cálculo, após preencher o processo e roteiro que será calculado, será apresentado um grupo de perguntas específico para vale transporte. Na primeira pergunta **Calcular Para?***,*é informado **Periódico,** como na imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075169874)

Um novo grupo de perguntas será apresentado e deve-se informar a quantidade de vales por dia que será calculada e o período. A pergunta Somente Avulso? deve ser preenchida com Não:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075170014)

Após o processamento do cálculo, um novo pedido é gerado com a quantidade de vales e dias informados nos parâmetros:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075170094)

**2. Calcular vales diferentes dos relacionados ao funcionário, para um determinado período**

Nesse exemplo, o funcionário já possui um benefício Vale Refeição, sendo um vale por dia. O cálculo mensal já foi realizado e o arquivo de integração foi gerado, concluindo assim o pedido:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075170434)

Durante uma semana do período, foi necessário adicionar um vale diferente do que está cadastrado com a quantidade de um vale por dia.  
Para realizar esse cálculo, é necessário acessar a rotina de atualização de benefícios em **Atualizações> Benefícios> VT/VR/VA> Atualização**, incluir um novo registro com o vale desejado e informar a quantidade de vales por dia. O campo Avulso ( M7\_COMPL ) deve ser gravado com Sim:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075170554)

Na rotina de cálculo, após informar o Processo e o Roteiro, será apresentada uma tela com as perguntas específicas para o cálculo de Benefícios ( VA e VR ).  
Nessa tela, a pergunta **Calcular Periódico?** deve ser preenchida com **Sim:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075170674)

Uma nova tela será apresentada com as perguntas referentes ao cálculo periódico. Nessa tela, deve ser informado o intervalo que o benefício será calculado.  
A quantidade de vales dia **não deve ser informada**, pois cadastramos na rotina de atualização.  
Caso a pergunta **Somente Avulso?** seja preenchida com **Não**, os dois vales cadastrados serão calculados para o período informado. Informando Sim na pergunta, apenas o vale com o campo M7\_COMPL = Sim será calculado:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076374113)

* Resultado do cálculo com a pergunta **Somente Avulso=Não**

Foram calculados 5 dias para cada vale cadastrado para o funcionário e o registro referente ao vale avulso foi excluído da tabela SM7:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075170954)

* Resultado do cálculo com a pergunta **Somente Avulso=Sim**

Foram calculados 5 dias apenas para o vale com o campo M7\_COMPL com Sim e esse registro foi excluído, para que não seja calculado novamente:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076374313)

**Saiba Mais**[RH - Linha Protheus - GPE - Como Cadastrar e Calcular o Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029037011-RH-Linha-Protheus-GPE-Como-Cadastrar-e-Calcular-o-Vale-Transporte?source=search)  
[RH - Linha Protheus - GPE - Controle de saldo de benefício ou compra da diferença faltante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051035414-RH-Linha-Protheus-GPE-Controle-de-saldo-de-benef%C3%ADcio-ou-compra-da-diferen%C3%A7a-faltante?source=search)  
[RH - Linha Protheus - GPE - Como descontar valor Fixo de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406270401047-RH-Linha-Protheus-GPE-Como-descontar-valor-Fixo-de-Vale-Transporte?source=search)  
[RH - Linha Protheus - GPE - Como calcular percentual de desconto de Vale transporte inferior a 6% para todos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059488853-RH-Linha-Protheus-GPE-Como-calcular-percentual-de-desconto-de-Vale-transporte-inferior-a-6-para-todos-funcion%C3%A1rios?source=search)
