---
article_id: 360014866531
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 83402e526f4ea9087b8ae668cf4cd26bb3a77580450bfae1e0596ecaea39fd43
fetched_at: '2026-06-28T22:38:54.073218+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA265 - Como efetuar
  o Controle e Endereçar Produtos no Protheus?
type: support-article
updated_at: '2025-06-27T14:51:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014866531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA265-Como-efetuar-o-Controle-e-Endere%C3%A7ar-Produtos-no-Protheus
---

**Dúvida**  
Como fazer controle de localização (endereçamento) dos meus produtos no *Protheus*?

**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução:**

O controle de localização pode ser utilizado por empresas que criam em seus armazéns subdivisões para facilitar a localização dos itens, como por exemplo: Ruas, Corredor, Prateleiras e etc. O Endereço é a identificação destas subdivisões (localizações) do armazém.

**1.** A utilização das funcionalidades do controle de localização depende da ativação do parâmetro **MV\_LOCALIZ**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000344801)

**2.** Além disto, é necessário que. no Cadastro do Produto (MATA010), seja configurado com o campo **Contr. Ende**. (**B1\_LOCALIZ**) como “**Sim**”.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000345061)

**3.** Para criar o Endereço (localização), acesse ao caminho: **Atualizações -> Cadastros -> Endereços (ou simplesmente a rotina MATA015)**e clique em "Incluir"

Após acessar à rotina, basta selecionar o Armazém ao qual o local pertencerá, o Código do Endereço (pode ser caracteres e/ou numerais) e a Descrição do Endereço

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000345201)

Essas são as configurações básicas para um produto ser endereçado.

**OBSERVAÇÃO IMPORTANTE AO HABILITAR A CONFIGURAÇÃO DE ENDEREÇAMENTO**

Ao habilitar o controle de localização para um produto que **já possui saldo em estoque** é necessário realizar a distribuição deste saldo ao(s) endereço(s). Para isto deve-se utilizar o programa Criar Sld. no End. (**MATA805**) através do menu **Atualizações -> Movimentações -> Internas -> Endereçamento -> Criar Sld. no End.**

**ENDEREÇANDO PRODUTOS**

Após ativação do controle de localização para um produto, sempre que realizada a entrada em estoque deste produto, a quantidade de entrada deverá ser endereçada nos locais disponíveis cadastrados anteriormente (conforme tópico 3). Este endereçamento deverá ser realizado através da rotina de Endereçamento (**MATA265**), disponível no menu **Atualizações -> Movimentações -> Internas -> Endereçamento -> Endereçar.**

Ao acessar esta rotina serão exibidas as entradas realizadas para os produtos que possuem o controle de localização. Assim que localizar a entrada desejada do produto apto ao endereçamento (legenda verde), deve-se acionar a opção **Endereçar**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000334262)

No cabeçalho desta rotina são exibidas as informações referentes a entrada que originou o saldo a endereçar, apenas para visualização do usuário.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099211434)

Lembrando que é possível endereçar partes da quantidade em locais diferentes, desde que eles façam parte de um mesmo armazém (na configuração pela rotina MATA015 explicada no tópico 3)

Após selecionar abaixo o Endereço e Qtde a Distribuir, basta clicar em **"Salvar"**.

**PRINCIPAIS CAMPOS DO CABEÇALHO NA ROTINA DE ENDEREÇAMENTO**

**Produto (DA\_PRODUTO):** Código do produto a endereçar.

**Qtd Original (DA\_QTDORI)**: Quantidade movimentada pela entrada que originou o endereçamento.

**Saldo (DA\_SALDO):** Saldo disponível para o endereçamento.

**Data (DA\_DATA):** Data do movimento de entrada que originou o endereçamento.

**Lote (DA\_LOTECTL):** Número de lote da quantidade a endereçar (se houver controle de lote)

**Armazém (DA\_LOCAL):** Armazém onde se encontra o saldo a endereçar.

**Documento (DA\_DOC):** Número de documento que originou o endereçamento .

**Série (DA\_SERIE):** Série do documento de entrada que originou o endereçamento.

**PRINCIPAIS CAMPOS DA PARTE INFERIOR NA ROTINA DE ENDEREÇAMENTO**

**Estornado (DB\_ESTORNO):** Identifica se o endereçamento realizado neste endereço deve ser estornado (deve preenchê-lo somente quando desejar realizar o estorno de um endereçamento **já concluído**) Para estornar basta acessar à rotina MATA265 -> **Outras Ações-> Estornar.**

**Endereço (DB\_LOCALIZ)**: Código do endereço que será utilizado no armazenamento da quantidade a endereçar.

**Qtd. Distribu. (DB\_QUANT)**: Quantidade a endereçar no local (endereço) informado na coluna anterior.

**IMPORTANTE**: Quando o produto possui controle de localização, os saldos das entradas ficarão disponíveis no estoque para movimentação somente após a realização do endereçamento (MATA265)

**Pergunta:** Como posso fazer o estorno de endereçamento de forma automática para vários produtos de uma vez?

**Resposta:**  
Nesse caso, é possível utilizar o **ponto de entrada `TMATA265`**, que permite implementar uma **customização** para automatizar o processo de estorno de endereçamento em lote. Essa abordagem possibilita tratar diversos produtos de forma simultânea, conforme a lógica definida pela empresa.

Recomendamos que essa customização seja desenvolvida com o apoio da equipe de TI ou de um consultor técnico familiarizado com o ambiente Protheus.

[https://tdn.totvs.com/pages/releaseview.action?pageId=6087464](MATA265%20-%20Rotina%20Autom%C3%A1tica%20de%20Endere%C3%A7amento)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
