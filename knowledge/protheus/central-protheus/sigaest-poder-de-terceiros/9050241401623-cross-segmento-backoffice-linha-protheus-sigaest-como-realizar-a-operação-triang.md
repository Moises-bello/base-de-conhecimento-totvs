---
article_id: 9050241401623
category: SIGAEST - PODER DE TERCEIROS
content_hash: a633b455fe0b2785c469bbbad4f2668ac0ae3b8b4fd7d2ba1d67e95c91b1837e
fetched_at: '2026-06-28T22:39:03.179020+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar a Operação
  Triangular no papel de Industrializador ?
type: support-article
updated_at: '2023-12-22T18:02:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9050241401623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-a-Opera%C3%A7%C3%A3o-Triangular-no-papel-de-Industrializador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20062324965271) Tempo aproximado para leitura: **00:07:21 min****Dúvida**Como realizar a Operação Triangular no papel de Industrializador?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

A operação triangular consiste em um processo que envolve três sujeitos diferentes:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049378485143)

- O **Encomendante** (que é o adquirente original);  
- O **Industrializador**;  
- E o **Fornecedor** das matérias primas.  
Nesta operação, o **Encomendante** adquire as matérias-primas necessárias do **Fornecedor** e as encaminha ao **Industrializador** para serviços de beneficiamento.

A seguir vamos entender como realizar a Operação Triangular no Protheus:

- Para exemplificar este cenário realizamos a criação de Três Produtos, sendo duas matérias primas (MP1087 - CAIXA e MP1086 FIO) que serão compradas do **Fornecedor** pelo **Encomendante** e um Produto Acabado (PA1085 ALÇA) que será elaborado pelo **Industrializador**.

**1.**Realizamos o Cadastro dos Produtos:  
- PA1085 ALÇA:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049579394839)  
  
​  
- MP1086 FIO:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049631524887)  
​  
- MP1087 CAIXA:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049615739799)

**2.** Efetuamos o Cadastro da Estrutura:

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049576447639)**

**3.** Vamos precisar Cadastrar a primeira TES, para realizar a entrada da NF, no nosso exemplo Cadastramos a TES 220, que atualiza estoque (F4\_ESTOQUE = S), mas não controla poder de terceiros (F4\_PODER3 = N):

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049658819095)

**4.** Após a Criação da TES 220, realizamos a entrada da NF (MATA103), informando os dados do **Fornecedor**:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049679308567)

**5.**Após a  conclusão do Documento de Entrada, vamos efetuar uma extração do MATR460 para demonstrar como ficou o saldo do item:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049718098839)

**6.**Na rotina de Documento de Entrada (MATA103) devemos posicionar na Nota (realizada no passo 4) e, após isso, é necessário realizar a vinculação do documento, clicando em "Outras Ações" > “Doc.vinculado" > "Vincular" > "Alterar":

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049881957399)

**7.**Após isso será apresentada a tela de alteração, onde deve informar a operação que será feita, o **Encomendante** (cliente) e a quantidade:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9049918994967)

**Importante: Neste momento não foi alterada nenhuma quantidade em Estoque.**

**8.**Será necessário realizar a criação de uma TES para realizar o controle de Poder de Terceiros, neste exemplo utilizaremos a TES 260 (F4\_ESTOQUE = N e F4\_PODER3 = R):

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050140930583)

**9.** O **Encomendante** (seu cliente) irá enviar uma nota fiscal de Industrialização (Cobertura). Para fazer isso, vamos entrar na rotina Documento de Entrada (MATA103). Após isso, devemos posicionar na nota (realizada no passo 4) e clicar em Outras Ações >“Doc.vinculado" > "Cobertura" > "Documento de Entrada":

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050065032471)

**10.**Após o passo 9 será apresentada a tela com as informações preenchidas (Cliente, Produto, Quantidade e etc...) sendo necessário apenas informar a TES (neste caso, o TES 260):

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050182501783)

**Importante: Neste momento a nota entra com uma TES que Controla poder de terceiros = Remessa e Não atualiza estoque, para não duplicar o estoque que já recebeu anteriormente. Neste momento é alimentado a tabela SB6 (que controla poder de terceiro).**

**11.** Vamos verificar o relatório MATR460 para validarmos os saldos após a nota de cobertura:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050223188119)

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050240959767)

Veja que na seção "Em Estoque" ficou com 1.000 UN de cada produto por conta da primeira nota de entrada. E após a cobertura alimentou o estoque "DE Terceiro". 

**12.** Agora vamos realizar a Produção do Produto Acabado (Obs: No F12 da rotina Ordem de Produção MATA650 deixamos para não considerar o Poder de terceiro, haja vista que a entrada já alimentou o estoque):

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050335922327)

- Após esse ajuste no F12 da rotina, vamos fazer a Ordem de Produção informando que é uma OP de Terceiro:

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050838639511)

**13.** Realizamos o Apontamento da Produção (MATA250):

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050325418007)

**14.** Veja que após a Produção extraímos novamente o MATR460, e conseguimos visualizar que foi zerado o saldo da sessão "Em Estoque" pois foi consumido na OP, e ficou pendente apenas o retorno do Insumo (MP) para dar baixa na SB6:

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050380971159)

![gRjpAxf3JM8AR6h76QNQ7gyay (1082×650)](https://p23.zdusercontent.com/attachment/888110/gRjpAxf3JM8AR6h76QNQ7gyay?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..cEcijKnsvMqlGuG8R-0j0w.OX1a7tLASbH0DO2_ibz8roZPtcjc_KvBwkJc0zHKxPIO67N76lp3Gb7OMnq-VmGLyv7W9yTGSnVrR1dNzTJ7mRDTvc_W54Vcw5yIJ7qlzAHzhuhLxTiAXoAxd586dsQJnPBxX7g1vzpxeUi9zY9h-EkqtdLBUMFn8k46Obc5u4Zpn62LZ3agcOTHgK9Z174r0TXTT8rlT7Z07Hq2bPjLZl2E_0SHxq46CBcnzM_OKVMrLNchQy1E5_e8lJYgaj5Hu4VFFGrA1Pqxx4IBZ2_PbawNfhb9imTse2vjHvXAqU4.fTl0BJaQy5RkCqr2BhL4SQ)

**15.** Efetuamos o Cadastro de uma TES de Devolução (F4\_ESTOQUE = Não e F4\_PODER3 = D):

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050421910679)

**16.** Após a Produção, precisamos devolver as MP's ao **Encomendante** (Cliente) simbolicamente para dar baixa no Poder de Terceiros. Para isso, precisamos chamar a nota Origem (Cobertura) na Rotina de Pedido de Venda (MATA410) pelo botão "Retornar". Além disso encaminhamos o Produto Acabado com uma TES de saída que não controla Poder de Terceiro:

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050584163223)

**17.** Após o passo 16 foi concluído a baixa do Poder de terceiro e, como já mandamos o Produto Acabado deixando o estoque zerado, vejamos como ficou o MATR460:

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050680248087)

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050683223959)

- A partir desse momento não temos mais nenhuma pendência de saldos, pois o processo foi concluído.​​

**18.** Em relação ao SPED, é necessário realizar o apontamento de Produção de terceiro, na MATA037:

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9050844654359)

- Neste momento o SPED e toda questão de estoque ficou de maneira correta, desta maneira, realizando o processo padrão, com a Nota de Cobertura, não existe problema no controle de estoque e no bloco K.

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar a Operação Triangular no papel de Industrializador sem a nota de cobertura ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20061858184343)

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
