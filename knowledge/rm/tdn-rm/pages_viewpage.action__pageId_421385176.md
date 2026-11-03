---
content_hash: 03004ae247af5283ea348b8eccec7efb1849c1ae452f20983de3288e2f1fe614
fetched_at: '2026-06-29T00:09:14.269314+00:00'
page_id: '421385176'
product: rm
source: tdn-rm
title: Períodos do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385176
version: 29
---

No anexo, "Períodos do Contrato" temos a possibilidade de visualizar os períodos cadastrados para o contrato em questão e seus respectivos processos.

Caso não exista períodos cadastrados para o contrato, podemos gerar os períodos para medição através do processo de disponível na tela de Contrato ou clicando em incluir:

**Incluir:** Permite a criação do período um a um, de acordo com a data do contato.

**Alterar:** A tela de edição do período, permite alterar informações dos períodos criados para o contrato, assim como incluir ou excluir um período complementar ou de estorno do respectivo período. É também nesta tela que o usuário poderá informar o valor previsto de medição para o período.

**Excluir:** Permite excluir período.

Período de Estorno

**Estorno de Período Liberado**  
  
Quando o período está liberado e existe a necessidade de cancelar sua liberação é preciso fazer um estorno.  
  
**Existem 3 formas de realizar a geração do período de estorno:**  
1) Ao executar o processo de Cancelamento de Liberação de um período de um contrato que possua períodos **posteriores** já liberados, será gerado um período de estorno medido e liberado de forma AUTOMÁTICA com o mesmo valor do período, **desde que o status do seu movimento seja PENDENTE.**

2) Quando o status do movimento gerado é **diferente de PENDENTE**, o usuário deve criar um período de estorno **manualmente** e realizar a medição para estorno das tarefas.  
- Para incluir um período de estorno, basta dar duplo clique no período já liberado na tela de edição do mesmo e, será exibido do lado direito os campos de criação dos períodos de estorno.  
- A inserção e exclusão segue o mesmo padrão dos períodos complementares.  
- Clica-se no botão "Incluir" para inserir um período de estorno e para excluir, selecione o período de estorno na lista e clica-se no botão "Excluir".  
- O período de estorno é referente a apenas um período e seus complementares do contrato, sendo sua validação feita nos itens medidos e liberados do período.  
- Os períodos gerados, são visualizados suas informações no anexo de Períodos do Contrato.

3) Tendo um período liberado e o movimento gerado está PENDENTE no BackOffice, o cancelamento pode ser feito através do próprio "cancelar movimento" diretamente no BackOffice. Isso, gera automaticamente um período de estorno no Contrato.

**Obs.:** O cancelamento do movimento diretamente pelo BackOffice gerando período de estorno no Contrato só é permitida desde que as quantidades dos itens do movimento estejam iguais as originais enviadas pelo Contrato.

**Importante:** O período de estorno tanto gerado automaticamente quanto criado manualmente, não considera itens que tenham sido medidos em quantidade/valor negativos no período principal. Ou seja, se no período 001 o **item A** estiver medido no valor ***R$ -100,00*** e o item B ***R$ 300,00***, ao criar o estorno para esse período, o **item A** não será levado para a medição, sendo criado o estorno somente com **item B**.   
**O período de estorno somente considera itens medidos positivamente.**

Caso necessite estornar um item que foi medido negativo, deve-se medir o item novamente em um período complementar.

Importante

Existe uma coluna, chamada "Valor. Medido - Previsto" do anexo "Períodos do Contrato" que tem seu calculo da seguinte forma: Valor Medido - Valor Previsto - Valor Retido.  
O valor medido é caracterizado pelo gasto naquele período. O valor previsto é, como seu próprio nome diz, a previsão em seu planejamento.

 Há também os períodos de Reajuste, que são gerados após aplicar um reajuste por item em um período já liberado. Esse período é gerado com código 0001R001. Saiba mais de reajuste por item do contrato:  

## Processos

## Integrações

TOTVS Assinatura Eletrônica

Caso o projeto esteja habilitado para utilizar o  na medição do contato, poderá acompanhar o processo de assinatura através do respectivo botão:

Será exibida a aba de Integração com o TOTVS Assinatura Eletrônica, conforme imagem abaixo, mostrada como anexo do período do contrato em questão. Nela será possível saber qual o status da assinatura do documento, seja boletim de medição (relatório definido nos parâmetros do projeto) ou PDF anexado à mediação do contrato:

Ao editar, na aba Identificação, é possível ter uma visão detalhada de alguns parâmetros gerais definidos  no projeto para o Assinatura Eletrônica:

Na aba Documentos, são exibidos, os documentos anexados ao período:

E na aba Destinatários, as ações e os responsáveis:

Para saber mais sobre a integração com o TOTVS Assinatura Eletrônica .
