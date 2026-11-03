---
article_id: 360049722534
category: Financeiro - Contas a Receber
content_hash: 876b790e9ae5ef2c97b9d7f3b435b944fb6a32d1269ee04c9192b6433573bfd9
fetched_at: '2026-06-28T22:38:13.908571+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  Erros na função DETPROVA
  ou TRANSLCTA no Lançamento Padrão
type: support-article
updated_at: '2026-04-17T19:32:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049722534-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Erros-na-fun%C3%A7%C3%A3o-DETPROVA-ou-TRANSLCTA-no-Lan%C3%A7amento-Padr%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24651771611543)**Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Em módulos do ERP Protheus ao tentar realizar o processo de contabilização, é apresentada a ocorrência na função DETPROVA ou TRANSLCTA, gerando error.log  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Erros na função DETPROVA ou TRANSLCTA normalmente são erros de configuração do Lançamento Padrão do cliente. Este é causado devido às informações errôneas ou customizações.  
  
**Solução**  
Para realizar o processo a seguir, é necessário que seja realizado por um analista especialista com conhecimento para ajuste de lançamentos padrão e filtragem dentro do error.log.

1. Localize em seu system (PROTHEUS) o arquivo ERROR.LOG

2. Acesse com um editor de texto e localize pela palavra **CPADRAO.**

**OBS.: CPADRAO**é o código de lançamento padrão que está com problema.

3. Após localizar, abrir o ERP e localizar no menu do sistema a rotina de **Lançamento Padronizado** (**CTBA080**).

4. Efetuar a busca do lançamento padrão correspondente ao **CPADRAO** informado no error.log

5. Valide todos os campos de fórmula do cadastro de lançamento padrão, seguindo a seguinte sequência:

a. Verifique se as expressões utilizadas estão corretas.

b. Caso esteja utilizando customizações nestes campos, verifique se estão compiladas dentro do seu RPO e/ou se estão habilitadas dentro do cadastro de personalizações (dentro do menu cadastro no configurador (**SIGACFG**)

c. Caso esteja referenciando um campo do sistema, verifique se o mesmo está como usado e/ou disponível para utilização.

Exemplo de cenário em contabilização de uma baixa de titulo a pagar utilizando o lançamento padrão 530.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071395103639)

Seguindo o passo a passo desta documentação, ao filtrar a palavra **CPADRAO**dentro deste error.log, consigo saber qual o lançamento padrão que preciso corrigir.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071395107735)

Ao acessar o cadastro via rotina **CTBA080**, localizo o lançamento padrão e ajusto o conteúdo que está incorreto.

Antes do ajuste:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071409387415)

Depois do ajuste:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33071395113239)

Neste exemplo, o nome do campo da tabela SE5 estava incorreto, no que deveria ser **E5\_VALOR** estava **E5\_VALO**

Após este ajuste, o processo poderá seguir sem que seja apresentado o error.log.
