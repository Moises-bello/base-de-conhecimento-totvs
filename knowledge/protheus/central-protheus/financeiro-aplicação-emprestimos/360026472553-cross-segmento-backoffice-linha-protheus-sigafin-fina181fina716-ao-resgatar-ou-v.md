---
article_id: 360026472553
category: Financeiro - Aplicação / Emprestimos
content_hash: 8f102be12328c10823277f19a6b72373291ecfaa99066d169415396e8046bc4e
fetched_at: '2026-06-28T22:37:59.420836+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA181/FINA716 - Ao
  resgatar ou visualizar as parcelas apresentando Não foram encontradas parcelas para
  este contrato
type: support-article
updated_at: '2025-11-28T10:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026472553-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA181-FINA716-Ao-resgatar-ou-visualizar-as-parcelas-apresentando-N%C3%A3o-foram-encontradas-parcelas-para-este-contrato
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36636599885975)***Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**  
Nas rotinas **FINA171** / **FINA181** / **FINA716** ao resgatar ou visualizar as parcelas apresentando “Não foram encontradas parcelas para este contrato !”  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Caso seja alterado através de uma **sintaxe**/**função**/**customização** a filial, **prefixo**, **número do título** e **tipo** referente aos títulos gerados de um empréstimo na **tabela SE2**, irá apresentar o erro ao visualizar ou resgatar as parcelas.

Exemplo: Ao efetuar um contrato pela rotina **FINA171 Inclusão de Empréstimo** com um contrato de número 123456 em 10 vezes.

![01_inclusao.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360041805773)

Automaticamente o sistema terá que gerar o mesmo conteúdo no campo **E2\_NUM** contendo o mesmo tamanho e número do contrato gerado pela rotina **FINA171 – Inclusão de Empréstimo**. A geração dos títulos na rotina **FINA050 – Contas a Pagar** deverão ser na mesma filial do contrato, possuir o **prefixo EMP**, o **tipo: PR** eao contrário disso ter problema ao visualizar as parcelas ou no momento do resgate.

Segue na imagem abaixo as parcelas geradas corretamente na rotina **FINA050 – Contas a Pagar**

![02_parcelas_corretas.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360040977914)

Caso esteja utilizando qualquer tipo de **sintaxe**/**função**/**customização** para alterar o conteúdo dos títulos na tabela **SE2,** seja alteração na filial ou no **prefixo** ou no **número do título** ou no **tipo** irá gerar a inconsistência abaixo:

**Exemplo:**   
Veja que na tela abaixo foi utilizado algum tipo de função (na tabela **SX3** no campo **E2\_NUM**, **gatilho**, **user function**,**fonte customizado** para inserir zeros a esquerda do campo **número** **do título**, fazendo com que o número gerado na tabela **SE2** fique diferente da tabela **SEH contrato**.

![03_parcelas_com_zeros_no_numero.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360041805953)

Com isso ao tentar visualizar as parcelas ou tentar resgatar, irá apresenta a mensagem “Não foram encontradas parcelas para este contrato!”

![04_erro_ao_resgatar.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360040978114)

A mesma mensagem “Não foram encontradas parcelas para este contrato!” irá ocorrer caso tiver algum tipo de **sintaxe**/**função**/**customização** que faça com que o sistema altere o campo prefixo fazendo com que fique diferente do prefixo **EMP** conforme o exemplo abaixo:

![05_erro_no_prefixo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360040978274)

Essa alteração terá o mesmo impacto na rotina **FINA716**, onde não aparece a opção de visualizar as parcelas conforme o erro abaixo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36636599886359)  
  
Exemplo de um print com a opção das parcelas sendo demonstrada correta  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36636584113175)  
  
  
**Solução:**  
Será necessário retirar a **sintaxe**/**função**/**customização** feita através de algum gatilho ou campo da **tabela SX3** ou etc... e deixar conforme o padrão do sistema.
