---
article_id: 1500004328202
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5d509f8d23a1d32cd8f949503b93f307a0f525ab2543369361b384b3e23b0ce9
fetched_at: '2026-06-28T22:38:57.295343+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo de Solicitação
  de Compras para Solicitação ao Armazém
type: support-article
updated_at: '2023-05-30T13:04:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004328202-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-Solicita%C3%A7%C3%A3o-de-Compras-para-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

**Dúvida**Como funciona o fluxo para gerar Solicitação de Compras (MATA110) para atender a Solicitação ao Armazém (MATA105/MATA106)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Cenário para exemplificação do fluxo:

Produto: PA70

Quantidade atual: 0,00

Armazém: 01

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005363741/mceclip0.png)

**1° Passo - Criação da Solicitação ao Armazém (MATA105) - ou pelo caminho Atualizações -> Movimentações -> Internas -> Armazém - > Solicitar:**

* Criaremos uma Solicitação ao Armazém de quantidade 50, no armazém 01, para o produto PA70

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005278702/mceclip1.png)

**2° Passo - Agora vamos gerar a Pré Requisição (MATA106) - ou pelo caminho Atualizações -> Movimentações -> Internas -> Armazém - > Gerar Pré-Requisição:**

* Neste momento pressionamos o botão [F12] do teclado para gerar a tela de algumas perguntas. Dentre elas, selecionaremos a pergunta "**Gerar Solicitação de Compra/Aut de Entrega?**" = "**Sim**". Com isso, em caso de não termos quantidade para atender à Solicitação ao Armazém, será gerada automaticamente uma Solicitação de Compras.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005278862/mceclip2.png)

* Após isso, basta marcar a caixa com a Solicitação do nosso produto PA70 e clicar em "Gera":

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005363881/mceclip3.png)

* Aparecerá uma janela para confirmar com o OK ou clicar em 'Parâmetros". Os parâmetros em questão são os mesmos da tecla [F12].

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005364001/mceclip4.png)

**3° Passo - Via Módulo de Compras (SIGACOM), acessar à rotina MATA110 para conferirmos se foi gerada a Solicitação de Compras:**

* Vejamos que foi gerada com código 021592, conforme imagem abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005364121/mceclip5.png)

**4° Passo - Ainda no módulo de Compras (SIGACOM). acessaremos à rotina de Pedido de Compras (MATA121):**

* Acesse à rotina e clique em Incluir;
* Nesta rotina são obrigatórios os campos **Cond. Pagto**, **Fornecedor**, **Produto**, **Quantidade**, **Prc Unitário** e **Vlr. Total** indicados abaixo, mas neste procedimento vamos preencher apenas dos campos do cabeçalho **Cond. Pagto** e **Fornecedor:**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005279422/mceclip6.png)**

* Após o preenchimento dos campos no cabeçalho Cond. Pagto e Fornecedor, posicionar o cursor nos itens e utilizar a opção **Outras Ações > Solicit**:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005364421/mceclip8.png)

* Vamos chamar a Solicitação de Compras do nosso PA70:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005364501/mceclip9.png)

* Com isso é gerada a linha com o registro do nosso produto, bastando preencher os campos **Prc Unitário** e **Vlr. Total** e confirmar a inclusão do Pedido na opção **Salvar**:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005299762/mceclip3.png)

**5° Passo - Emissão do Documento de Entrada (MATA103):**

* Ao acessar à rotina, clique em "Incluir":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005299402/mceclip1.png)

* Preencher o cabeçalho da nota e em seguida clicar em "Outras Ações" -> "Pedido":

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005388281/mceclip4.png)

* Selecionaremos o Pedido de Compras do PA70, no caso, o de número 000005:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005299902/mceclip5.png)

* Com isso baixa preencher o TES que é um campo obrigatório e Salvar a nota.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005388381/mceclip6.png)

**6° Passo - Com isso, temos agora os 50 itens para atender à Solicitação ao Armazém. Vamos conferir se realmente estamos com 50 unidades do PA70:**

* Veja abaixo que automaticamente já empenhou o saldo para a SA (Solicitação ao Armazém)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005388561/mceclip7.png)

**7° Passo - Efetuar a Baixa da Pré-Requisição (MATA185) - ou caminho Atualizações -> Movimentações -> Internas -> Armazém - > Baixar Pré-Requisição:**

* Filtramos nossa Solicitação e clicamos em "Baixar"

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005388701/mceclip8.png)

* Escolha a quantidade à requisitar. No nosso exemplo, requisitaremos os 50 de uma vez só.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005388961/mceclip9.png)

* Insira os parâmetros para geração da Movimentação, inserindo o Tipo da Movimentação que é um campo obrigatório:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005300402/mceclip10.png)

Ao salvar, acontece a baixa e o saldo sai do Estoque.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005389041/mceclip11.png)

Com isso, finalizamos este artigo.

**Saiba mais:**

*[MP - SIGAEST - Solicitação, Pré-Requisição e Baixa da Pré-Requisição - MATA105 - MATA106 - MATA185](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018562511-MP-SIGAEST-Solicita%C3%A7%C3%A3o-Pr%C3%A9-Requisi%C3%A7%C3%A3o-e-Baixa-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o-MATA105-MATA106-MATA185)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
