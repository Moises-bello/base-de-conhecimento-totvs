---
article_id: 360061648474
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 0cceb58d61dcf4bde168f9987aba61ca6214419b5771320b1116a87a3c145521
fetched_at: '2026-06-28T22:38:54.057844+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA242 - Processo
  de Desmontagem de Produtos
type: support-article
updated_at: '2025-11-18T21:57:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061648474-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA242-Processo-de-Desmontagem-de-Produtos
---

O processo de Desmontagem de Produtos (MATA242) no Protheus consiste em transferir o saldo de um produto seja do tipo acabado, matéria prima, e etc. E para seus componentes, gerando movimentações internas (RE7/DE7). É necessário informar manualmente o rateio do custo, que não pode ultrapassar 100%. O procedimento inclui selecionar produto, armazém e quantidade, e confirmar a desmontagem para atualizar os saldos.

Esse processo, pode ser realizado também para cenários em que precisa destinar o Saldo de 01 Produto para outro produto mas com quantidades diferentes da origem.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34461570881047) Tempo aproximado para leitura: **00:02:00 min**  
   
**Dúvida**

Como é realizado o processo de **Desmontagem de Produtos (MATA242)** no Protheus?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

No Protheus o processo de Desmontagem de produtos é equivalente a Transferência de Saldo de **um Produto** para **vários produtos.** Por exemplo a **Desmontagem de Produtos** realiza um Movimento Interno (RE7/DE7) ao **D****esmontar por exemplo de um Produto Acabado (PA)** e devolver aos componentes que fazem parte da Estrutura desse Produto Acabado (PA).

**Importante:** Esse processo, pode ser realizado também para cenários em que precisa destinar o Saldo de 01 Produto para outro produto mas com quantidades diferentes da origem. Veja nesse [***link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6027746860567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-tratar-quando-efetuada-a-compra-de-produto-em-Caixa-por%C3%A9m-vendo-consumo-as-unidades-da-caixa) esse exemplo onde compro um produto em Caixa e preciso movimentar as unidades compostas na Caixa.

### **Exemplo prático**

Considere a seguinte estrutura: **1:1 entre o PA44 e o MP44**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003274781)

**PA44** com Saldo 10:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003231842)

**MP44** sem saldo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102101894)

### 

### **Procedimento**

 - 1 - Acesse a rotina **MATA242 – Desmontagem de Produtos. Vá em** **Atualizações > Movimentações > Internas > Desmontagem** e clique em "Incluir;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104269973)

 - 2 - Selecione o Produto, Armazém, Quantidade a ser desmontada e Documento. Após isso, clique em **"Outras Ações" -> "1° Nivel"**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003279481)

 - 3 - Neste momento será alimentada a linha do produto componente com a quantidade da estrutura (1:1). Então, como estamos desmontando 10 unidades do PA44, elas voltarão a ser quantidade 10 do MP44

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102102474)

### 

### **Observações**

* O **rateio** deve ser informado **manualmente**, considerando o percentual do custo do produto na desmontagem.
* Independentemente da quantidade de componentes (produtos filhos), o **rateio total não pode ultrapassar 100%**.
* Para mais detalhes sobre o preenchimento do rateio, consulte a documentação específica [**nesta documentação**](https://tdn.totvs.com/pages/releaseview.action?pageId=235592716)

Com isso, é gerada a movimentação DE7 para o MP44 e RE7 para o PA44, onde invertem-se seus saldos neste exemplo.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104270433)

### **HELPS que podem ser ocasionados**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34461570882583)

Valide os campos obrigatorios, bem como se preencheu o valor minimo de rateio 00,01% para demonstagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34461602146199)

O HELP é claro, a somatoria dos itens que vão receber a desmontagem **ultrapassam 100%**, **e isso não é permitido**, voce deve inserir um total de **100% no rateio com a soma de todos os itens, essa é uma validação MANUAL**, não é tratado no padrão o calculo do rateio a cada distribuição, caso queira, podera customizar uma validação nesse contexto.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA242 - Pontos de entrada na rotina Desmontagem de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6936591821975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA242-Pontos-de-entrada-na-rotina-Desmontagem-de-Produtos)

## **EXEMPLO DE CUSTO COM RATEIO NA DESMONTAGEM**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA242 - Campo D3\_RATEIO, qual cálculo efetuar para produtos com estrutura?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23608602938519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA242-Campo-D3-RATEIO-qual-c%C3%A1lculo-efetuar-para-produtos-com-estrutura)

***Saiba mais:***

[SIGAEST - Como tratar quando efetuada a compra de produto em Caixa, porém, vendo/consumo as unidades da caixa?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6027746860567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-tratar-quando-efetuada-a-compra-de-produto-em-Caixa-por%C3%A9m-vendo-consumo-as-unidades-da-caixa)

[SIGAEST - Utilizando a desmontagem para controle de saldo na segunda unidade de medida](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410189373591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilizando-a-desmontagem-para-controle-de-saldo-na-segunda-unidade-de-medida)

[*Exemplo prático de Desmontagem de Produção com rateio*](https://tdn.totvs.com/pages/releaseview.action?pageId=235592716)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
