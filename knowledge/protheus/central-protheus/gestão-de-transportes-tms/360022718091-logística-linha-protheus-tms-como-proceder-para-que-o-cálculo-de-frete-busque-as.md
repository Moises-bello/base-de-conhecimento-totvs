---
article_id: 360022718091
category: Gestão de Transportes (TMS)
content_hash: ad5c43e7e6d89b923b832d5ab830fc056e3ab3935a4391cb8972dc15a701cac5
fetched_at: '2026-06-28T22:45:27.485732+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como proceder para que o cálculo de frete
  busque as informações da Tabela de Frete por Destinatário?
type: support-article
updated_at: '2022-07-19T13:00:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022718091-Log%C3%ADstica-Linha-Protheus-TMS-Como-proceder-para-que-o-c%C3%A1lculo-de-frete-busque-as-informa%C3%A7%C3%B5es-da-Tabela-de-Frete-por-Destinat%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**Como proceder para que o cálculo de frete busque as informações da **Tabela de Frete por Destinatário**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A configuração da **tabela de frete por destinatário** deve ser utilizada quando a transportadora deseja definir um valor fixo de frete por destinatário.   
  
Para que o cálculo do frete utilize a tabela de frete em questão, é necessário efetuar os procedimentos descritos abaixo:

* Acessar o **Configurador do Protheus - Base de Dados/Dicionário/Base de Dados/Parâmetros** e configurar o parâmetro **MV\_COMPDES - Quando for .T., indica que o cálculo do componente de frete será baseado em função do cliente destinatário**, deixando o mesmo com o conteúdo igual a **.T.**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019871911/mceclip0.png)

* Ainda no **Configurador - Base de Dados/Dicionário/Base de Dados/Dicionário de Dados**, localizar a tabela **DYE**. Nesta tabela, selecionar o campo **DYE\_DOCCOB**. Este campo deve ser alterado a sua propriedade para **Alterar**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020009372/mceclip6.png)

* Após, efetuar as configurações dentro do módulo **Protheus** **TMS**. A primeira configuração dentro do Sistema é a criação de um novo componente de frete na rotina **Componentes Frete - Atualizações/Comercial**, onde o mesmo precisa ter o seu **cálculo** e a **faixa** sobre o **cliente destinatário**, conforme demonstra imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019873791/mceclip3.png)

* Feito isso, acessar a rotina **Componente Frete Destinatário - Atualizações/Comercial**e criar um novo componente de frete de destinatário, associando o componente criado anteriormente, com um ou mais clientes destinatários. Informar o campo **Doc.Cobrança** igual a **2** quando o tipo do documento for **CTRC**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020009272/mceclip4.png)

* Acessar a rotina **Configuração Tabela de Frete - Atualizações/Comercial**e incluir ou alterar uma tabela de frete adicionando o componente em questão. É necessário que tenha pelo menos um componente onde o **Calc. Sobre** seja diferente de **15 - Cliente Destinatário**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019876771/mceclip7.png)

* Na rotina **Tabela de Frete - Atualizações/Comercial**, o componente de cliente destinatário não será apresentado, ou seja, ao abrir a mesma, irá apresentar somente os demais componentes relacionados a tabela. Desta forma, caso não tenha nenhuma tabela criada para a configuração de tabela de frete em questão, será necessário criar a mesma fazendo as configurações dos demais componentes da mesma. Será este código de tabela de frete que será informado no **Contrato do Cliente**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019877791/mceclip9.png)

* Após, na rotina **Tabela de Frete por Destinatário - Atualizações/Comercial**incluir uma tabela de frete por destinatário e vincular a tabela de frete configurada anteriormente, informando um ou mais destinatários e os valores definidos para cada um:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020011352/mceclip8.png)

* Na rotina **Contratos de Clientes - Atualizações/Comercial**, incluir ou alterar um contrato para um determinado devedor de frete e informar a tabela de frete configurada, que neste caso será a tabela de frete padrão, citada no item 6.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020012252/mceclip10.png)

Após efetuar as configurações citadas acima, ao fazer o cálculo do frete o mesmo terá como base o componente de cliente destinatário e os demais componentes configurados, caso os mesmos sejam preenchidos no momento da Entrada do Documento do Cliente. Segue abaixo imagem demonstrando como será apresentado o cálculo do frete na rotina Entrada Documento Cliente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019878331/mceclip11.png)
