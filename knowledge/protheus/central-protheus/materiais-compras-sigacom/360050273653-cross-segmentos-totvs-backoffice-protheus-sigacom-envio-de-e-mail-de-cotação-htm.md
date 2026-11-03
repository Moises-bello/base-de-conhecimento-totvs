---
article_id: 360050273653
category: Materiais - Compras (SIGACOM)
content_hash: 2bc2c571dbff683671094878fc52f2be4971a48af7e1e4f5dba530ee8be99860
fetched_at: '2026-06-28T22:41:17.601680+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Envio de e-mail de
  cotação html parâmetro MV_ENVCOT.
type: support-article
updated_at: '2025-02-18T20:18:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050273653-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Envio-de-e-mail-de-cota%C3%A7%C3%A3o-html-par%C3%A2metro-MV-ENVCOT
---

**Dúvida**

Envio de e-mail de cotação html parâmetro MV\_ENVCOT.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**

Para envio de e-mail de forma padrão. Realizar as configurações abaixo;

1. Atualizações> Cadastros>Produto x Fornecedor **(MATA061);**

**![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11705386277271)**

**1.2**- Atualizações >Cadastros > Fornecedores;

        Informar o e-mail, conforme o imagem a seguir:

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11705482201367)

3. Parâmetros;

### Exemplo de configuração dos Parâmetros:

* MV\_ENVCOT // .T.
* MV\_RELSERV //smtp.gmail.com:587
* MV\_RELACNT // [teste@gmail.com](mailto:teste@gmail.com)
* MV\_RELPSW //  (não copie a  senha, digite ela)
* MV\_RELAUTH // .T.
* MV\_RELAPSW // ( Senha do email precisa estar preenchida) Senha exemplo= [1234@5](mailto:1234@5)
* MV\_RELSSL // .F.
* MV\_RELTLS // .T.
* MV\_RELAUSR  // [teste@gmail.com](mailto:teste@gmail.com)
* MV\_RELFROM // [teste@gmail.com](mailto:teste@gmail.com)

OBS : Verifique se houve a alteração conforme o vídeo **: [Alteração na Configuração Gmail](https://www.youtube.com/watch?v=wGikJth4dN0&t=1s)**

4. Template ;

Para usar um template no envio de e-mail, é necessário criar o caminho na pasta Protheus\_Data:

* **samples/wf**

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11705601917335)

Com isso, o Protheus substituirá o layout do envio de e-mail padrão, pelo layout do template.

***\* É necessário criar a pasta samples e wf conforme exemplo acima dentro da Protheus\_Data e colocar o arquivo abaixo:***

* [MATA131\_Mail001.zip](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/360074288034/MATA131_Mail001.zip) (886 bytes)

Obs: Esse arquivo pode ter seu layout alterado para melhor atender ao cliente.

Caso deseje que seja levado novos campos criados no MATA131 para o layout pode ser utilizado do Ponto de Entrada [MT131AI - Adiciona campos no envio de email após gerar a cotação](https://tdn.totvs.com/pages/releaseview.action?pageId=511549002)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423034575895/mceclip1.png)

Exemplos:

* Envio de e-mail padrão da cotação:

![](https://tdn.totvs.com/download/attachments/512435120/image2019-8-28_10-25-6.png?version=1&modificationDate=1567000340693&api=v2)

* Envio do e-mail utilizando o template:

![](https://tdn.totvs.com/download/attachments/512435120/image2019-8-28_10-48-25.png?version=1&modificationDate=1567000319737&api=v2)

### **Observação:**

O campo Entrega que consta no e-mail da geração da cotação é consulto a partir da configuração Atualizações> Cadastros> Produto campo **ENTREGA**  ( B1\_PE ).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078371834/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079535653/mceclip2.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
