---
article_id: 17178615741335
category: SIGAEST - SALDOS
content_hash: 6a1528e47914c16da7e6689d3f077456d7366539112c8710364f578080684048
fetched_at: '2026-06-28T22:39:14.852481+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Endereços sem saldo
  no Protheus, como consultar?
type: support-article
updated_at: '2025-07-29T17:39:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17178615741335-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Endere%C3%A7os-sem-saldo-no-Protheus-como-consultar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17178599237655) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como é possível consultar se temos **Endereços Desocupados e/ou Vazios** no Protheus? Existe um relatório que apresenta essa informação?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**  
Para consultar os Endereços que estão desocupados, é possível diretamente pela rotina **CADASTRO DE ENDEREÇO (MATA015)** verificando o campo **STATUS (BE\_STATUS)** na aba WMS quando a informação **Desocupado**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17179379335959)

***Dica:*** Para facilitar a consulta aos Endereços Desocupados, incluir a coluna Status no Browser da rotina MATA015. em seguida criar um filtro para exibição apenas dos Endereços Desocupados. Veja um passo a passo abaixo:

### ***1 -*** **Ajustar o Browser para exibir a coluna Status, em seguida clique em Filtrar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17179583787927)

### 

### ***2 -*** **Criar o filtro como no exemplo abaixo e Salvar:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17179775907479)

### 

### ***3 -*** **Pronto ao aplicar o Filtro criado são exibidos apenas os Endereços Desocupados.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17179920055959)

### 

### ***4 -*** **Também é possível a impressão do Browse. Veja um passo a passo a seguir. Clique em Outras Ações, Imprimir Browse**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17180031685655)

### 

### ***5 -*** **Na impressão da Listagem do Browse. Clique em Outras Ações, Personalizar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17180069898775)

### 

### ***6 -*** **Crie um Layout como desejado, mantendo o original ou mesmo retirnado colunas, No exemplo abaixo, mantemos apenas** ***Filial, Armazém, Endereço Descrição e Status*****, veja o resultado;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17180226859415)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17180291069335)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17180318591895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17180377111191)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre SALDOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
