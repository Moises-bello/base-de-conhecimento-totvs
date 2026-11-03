---
article_id: 360020688571
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ec8ee044caf34ca838f6fcc2c991b13e289483cedff4c2684357a1908b7d3c95
fetched_at: '2026-06-28T22:38:53.981213+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Conceito e usabilidade
  de Apropriação Indireta (MV_LOCPROC)
type: support-article
updated_at: '2026-02-20T17:04:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020688571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-usabilidade-de-Apropria%C3%A7%C3%A3o-Indireta-MV-LOCPROC
---

Produtos de Apropriação Indireta no Protheus são materiais de difícil controle no processo produtivo, como tintas usadas gradualmente. Para configurá-los, defina o armazém de processo (padrão 99), cadastre o produto com B1\_APROPRI=I e ajuste os tipos de movimentação e saldos conforme orientações do artigo, usando sempre o armazém padrão para requisições e devoluções.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38527849125015) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

O que são produtos de **"Apropriação Indireta"** **(B1\_APROPRI=I)** e como configurá-los no Protheus?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Neste artigo trataremos do armazém de processo para materiais de apropriação indireta, como cadastrar o produto e fazer a requisição e/ou devolução ao armazém de processo.

Materiais de apropriação indireta são materiais de difícil controle no processo de produção como por exemplo um barril de tintas, no qual os funcionários vão coletando os litros aos poucos.

**Veja também a FAQ abaixo com as instruções e conceitos:**

[***https://tdn.totvs.com/pages/viewpage.action?pageId=235592220***](https://tdn.totvs.com/pages/viewpage.action?pageId=235592220)

Para facilitar e fixar o entendimento, abaixo algumas demonstrações sobre produtos com **Apropriação Indireta** e **Armazém de Processo** neste artigo.

**1. Definindo o Armazém de Processo**

O primeiro a passo é definir o armazém de processo, por padrão o parâmetro **MV\_LOCPROC** vem preenchido com o armazém **99**.

**2. Cadastrando um produto que será de Apropriação Indireta**

Posteriormente, devemos cadastrar o produto e preencher o campo **B1\_APROPRI** com o conteúdo “**I-INDIRETO**” conforme imagem abaixo.

![SB1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016683171)

**3. Criação dos armazéns 99 (Armazém de Processo) e 01 (Armazém Padrão)**

Através da rotina **AGRA045**, devemos criar os armazéns 99 e 01, além de dar saldo inicial com quantidade 10 para o armazém 01 (não é permitido dar saldo inicial ao armazém 99 (MV\_LOCPROC)).

**4. Criando os Tipos de Movimentações (TM) para Remessa e Devolução**

Devemos cadastrar dois Tipos de Movimentação através da rotina **MATA230,** sendo um tipo de TM Remessa e outro Devolução. Em ambos, devemos preencher o campo F5\_APROPR =  “NÃO”, pois, conforme a imagem abaixo ilustra, quando preenchemos com o conteúdo “NÃO”, o sistema **ativa** a apropriação indireta, enquanto o conteúdo “SIM” **desativa** a apropriação indireta.

![TM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016626632)

**OBS:** No caso da apropriação indireta, devemos fazer as requisições e/ou devoluções apenas no armazém padrão do produto (não fazer no armazém 99 (MV\_LOCPROC)).

**5. Dando saldo inicial ao produto PI2;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003092421)**

**6. Transferindo 7 unidades do nosso produto ao Armazém de Processo**

Vamos fazer uma requisição de quantidade 7 ao armazém 01. Com isso, o sistema gerará automaticamente movimentos do tipo “RE3” no armazém 01 e “RE3\*”  no armazém 99. Assim, nosso armazém padrão (01) ficará com 3 unidades e o nosso armazém de processo (99) ficará com a quantidade 7 (conforme imagens abaixo mostrando a movimentação e os resultados impressos no relatório MATR900).

![MATA241.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016626672)

![MATR900.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016626712)

**7. Transferindo 2 unidades do nosso produto do Armazém de Processo (99) para o Armazém Padrão (01)**

Se quisermos transferir um saldo do armazém 99  para o armazém 01 devemos fazer uma devolução (utilizando o TM mencionado acima no artigo) **filtrando o armazém 01** **(nunca fazer movimento filtrando o armazém de processo)** e o sistema fará o inverso da operação anterior transferindo o saldo para o armazém padrão.

![MATA241_DEV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016626732)

![MATR900_DEV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360016683431)

Se em algum momento for preciso fazer ajustes no saldo do armazém 99 deve ser feita uma devolução ao armazém 01 usando a TM com F5\_APROPR = NAO. Depois que o saldo voltar ao armazém padrão, poderás fazer os ajustes necessários no saldo do produto (em caso de geração de Bloco K no SPED o recomendável é fazer ajustes de estoque através de inventário para correta apuração).

### **O Armazem de processo pode ter saldos movimentados negativo?**

Sim, caso voce use o parametro **MV\_INDNEG,** conforme boletim: [Manufatura - Linha Protheus - SIGAPCP - Estoque negativo no armazém de processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025351072-Manufatura-Linha-Protheus-SIGAPCP-Estoque-negativo-no-armaz%C3%A9m-de-processo)

Processo pararelo: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como corrigir o Help A240LOCPRC na rotina Solicitação ao Armazém?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34722314376343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-corrigir-o-Help-A240LOCPRC-na-rotina-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m)

***Observações:***

***-**Não é necessário ter um local de estoque cadastrado com o definido no parâmetro MV\_LOCPROC.*

***-**Caso seja cadastrado um local de estoque igual ao usado no parâmetro MV\_LOCPROC, as movimentações para este local serão iguais as movimentações de qualquer outro local cadastrado.*

***Saiba mais:***

[*Clique aqui e acesse mais artigos sobre Movimentação no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Como utilizar produto com apropriação indireta?](https://tdn.totvs.com/pages/viewpage.action?pageId=235592220)
