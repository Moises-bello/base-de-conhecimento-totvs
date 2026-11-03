---
article_id: 11248979872279
category: Materiais - Compras (SIGACOM)
content_hash: c9d38c4e217b471b4fea5aa30f8c15ba53d06fd2f11e205286068961d28889df
fetched_at: '2026-06-28T22:41:24.326726+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual o uso e comportamento
  dos campos _MSBLQL e _MSBLQD
type: support-article
updated_at: '2022-12-27T16:58:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11248979872279-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-o-uso-e-comportamento-dos-campos-MSBLQL-e-MSBLQD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00**:10:00 min****Dúvida** Qual o uso e comportamento dos campos \_MSBLQL e \_MSBLQD?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**

* O campo **\_MSBLQD** não será tratado nos módulos **SIGACOM, SIGAGCT e SIGAGCP**.
* Somente serão tratadas tabelas de cadastro e que sejam tabelas **pai**. Exemplo: Tabela **SAL** pode ser validada mas não a tabela **DBL** que é sua filha.
* Tabelas de movimento não serão tratadas.
* A validação será realizada somente em tela, através da validação de campo (X3\_VALID) com a função ExistCPO().
* Rotinas de processamento que utilizarem tabelas de cadastro não realizarão a validação do bloqueio do registro.
* Rotinas que executarem internamento rotinas automáticas, vão executar as validações de bloqueio a depender da rotina chamada.
* Telas que não estiverem executando a validação de bloqueio do registro, serão tratadas como melhoria no produto.

As tabelas que possuem os campos **\_MSBLQD**(Bloqueio Automático por Data) ou **\_MSBLQL**(Bloqueio Automático), exibirão em seus cadastros o conteúdo destes campos somente para os usuários administradores.

Estes podem preencher uma data a partir da qual o registro será bloqueado para uso (no caso do campo **\_MSBLQD**), ou apenas definir se o registro será bloqueado, ou não, independente da data (**\_MSBLQL**).

Se o campo**\_MSBLQD**estiver preenchido e a data do sistema for superior à data cadastrada, ou se o campo **\_MSBLQL**estiver definido como **Sim**, o registro se encontrará bloqueado e será exibido no browser com uma cor diferente.

O ponto de entrada **MBLKCOLOR**, permite definir as cores de fundo e letra para os registros bloqueados. Este ponto de entrada retornará um array com o código numérico das cores da fonte e fundo.

Para validar se o campo está ou não bloqueado por padrão deve-se utilizar a função **RegistroOk.**A função retorna se o campo está ou não bloqueado.

**Saiba mais :**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
