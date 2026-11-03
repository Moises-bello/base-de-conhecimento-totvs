---
article_id: 31964289610775
category: SIGAACD - Automação e Coleta de Dados
content_hash: af495d715bd1aec462ef4a70db7146e82c4ad663c90384712b6b14814d8b5cc0
fetched_at: '2026-06-28T22:39:11.309042+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV150 - Quantidade
  excede o saldo disponível. Como corrigir?
type: support-article
updated_at: '2026-05-06T17:49:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31964289610775-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV150-Quantidade-excede-o-saldo-dispon%C3%ADvel-Como-corrigir
---

Ao realizar transferência de endereço com produto e aparecer "Quantidade excede o saldo disponível", verifique o campo Qtd.Embalag (B1\_QE), que multiplica a quantidade informada nas movimentações. O padrão é 0, desativando essa função. Se o produto tem controle de endereço e número de série, preencha o campo B5\_NSERIE na aba ACD do cadastro para evitar a mensagem, pois o sistema exige o número de série para concluir a transferência.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31964289597463) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Quando realizo uma transferência de endereço com um produto, ocorre a mensagem "Quantidade excede o saldo disponível". Como corrigir?   
![Exibindo image.png](https://chat.google.com/u/0/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEU%2B9%2Br9mleeF1HYr1mj8noBlbOJYtTHz%2F6bk9rHt2gpWyROF6PchLLefhnYKXfvuWegunMNKJI4x9oVHnAncPkKoQDxaeWXARCYQizKzdIl67tn4TfGKLKE3DRsnYxVDqJmTaZKeo3oAvSmkgyrIoUsFsaVCUKqiqTn%2Bq53QjDv4qSZ8u%2FJGY0Sl4izN%2Bb0skRiMbqpGCejw%2F1%2F6Ke6sWPdGYLrQnA8%2Bwndqngw0a5LPXEscrwHUQdFXWwADcKNJvCR2X%2FCTVcbUTNWAANNN78HXnZQE%2BBO97c4D%2FPWdAKEIwPXwquiGg9xH%2Bkxd06wc0O7AfPIvlRKptezHKp8IXwZndGMaKWEw4%2F4r41cu3W38aYq%2Bt20K4J1naCGa5QZ8uYLezAp6QkqNkm0R9p2jPcZeWJSxoEiEknjgCSBzk17PhgJLw8MjufaRqArTBOgnTBcTY6nj1PZuQu74tmhrzyM%2B3pbS4V7TGWPl0jpLB20pdVvKt0pu6wWNV2C1FbjqR%2FMF2QS4WE6EFSEFIMoo1panIBzLvkfZRq4bcQRbPCUl%2FWx6sL6ClcEnCsPMoI94g%3D%3D&allow_caching=true&sz=w1542-h930)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Verificar como consta o campo Qtd.Embalag(B1\_QE) para o produto em questão. Esse campo multiplica a quantidade informada em qualquer rotina de movimentação dentro do ACD(Transferência entre armazéns, inventário, movimentações múltiplas, etc). Ou seja, a quantidade informada em qualquer uma dessas rotinas de movimentações, será **multiplicada** pela quantidade informada nesse campo.

![B1_QE.webp](https://centraldeatendimento.totvs.com/hc/article_attachments/40276474025751)

**OBS:** O padrão desse campo é 0, e nessa condição ele não é ativado. Maiores detalhes sobre o campo [**B1\_QE**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037063574)

Outro cenário é quando é informado o controle de endereço no produto e o mesmo tem número de série, é necessário preencher o campo B5\_NSERIE na aba ACD, do cadastro do produto, conforme o Print.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31964304963991)

Realizando o preenchimento desse campo, ao fazer a transferência de endereço(ACDV150) não será apresentada mais a mensagem. Pois o emulador do SIGAACD foi entender que precisa ser passado o número de série para finalizar a transferência.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
