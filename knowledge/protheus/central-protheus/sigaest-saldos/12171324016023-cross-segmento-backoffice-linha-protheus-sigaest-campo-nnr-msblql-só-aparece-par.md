---
article_id: 12171324016023
category: SIGAEST - SALDOS
content_hash: e017fdc046a81b79fd0826ac2b5f94006a36ff423f745a28eeea64c0a1d9b0f3
fetched_at: '2026-06-28T22:39:14.807885+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo NNR_MSBLQL só
  aparece para usuário adm?
type: support-article
updated_at: '2025-03-12T12:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12171324016023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-NNR-MSBLQL-s%C3%B3-aparece-para-usu%C3%A1rio-adm
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15770012924823) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**Qual o conceito de usabilidade do campo NNR\_MSBLQL no estoque, e como ele é exibido?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**O campo em questão, vai ser exibido somente para usuários administradores**, no estoque ele tem como funcionalidade, informar se o armazém será bloqueado ou não para movimentações, caso configurado como si será apresentado o HELP REGBLOQ

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - AGRA045 - Como bloquear armazém para movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022132132)

Mais sobre campo Reservado \_MSBLQD e \_MSBLQL

<https://tdn.totvs.com/display/public/framework/Campo+Reservado+_MSBLQD+e+_MSBLQL>  
  
**Funcionalidades dos campos reservados \_MSBLQD (Bloqueio Automático por Data) ou \_MSBLQL (Bloqueio Automático).**  
  
As tabelas que possuem os campos **\_MSBLQD**(Bloqueio Automático por Data) ou **\_MSBLQL**(Bloqueio Automático), exibirão em seus cadastros o conteúdo destes campos somente para os usuários administradores.

Estes podem preencher uma data a partir da qual o registro será bloqueado para uso (no caso do campo **\_MSBLQD**), ou apenas definir se o registro será bloqueado, ou não, independente da data (**\_MSBLQL**).

Se o campo**\_MSBLQD**estiver preenchido e a data do sistema for superior à data cadastrada, ou se o campo **\_MSBLQL**estiver definido como **Sim**, o registro se encontrará bloqueado e será exibido no browse com uma cor diferente.

O ponto de entrada **MBLKCOLOR**, permite definir as cores de fundo e letra para os registros bloqueados. Este ponto de entrada retornará um array com o código numérico das cores da fonte e fundo.

Para validar se o campo está ou não bloqueado por padrão deve-se utilizar a função **RegistroOk.**

A função retorna se o campo está ou não bloqueado.  
**Poderá ser utilizada a função padrão ou criar um tratamento especifico para o registro bloqueado.**  
  
Por exemplo: Na rotina de **Pedidos de Venda**, existe a verificação se o registro de cliente, produto etc, se encontra bloqueado para uso. Logo, ao selecionar um produto bloqueado, é exibida a mensagem de alerta que o registro se encontra bloqueado.   
**Somente os usuários administradores podem liberar o registro.**  
  
**Importante:** Cabe às rotinas do módulo avaliar como e se será possível tratar a funcionalidade destes campos no processo. no caso do Estoque/Custo a premissa é que o campo não seja apresentado para usuários não administradores.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - AGRA045 - Como bloquear armazém para movimentações?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022132132)
