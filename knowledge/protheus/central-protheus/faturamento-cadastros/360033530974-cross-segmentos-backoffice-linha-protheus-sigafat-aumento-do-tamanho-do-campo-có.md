---
article_id: 360033530974
category: Faturamento - Cadastros
content_hash: 06e956d872f3bfcd1ad743baf9713e163fd87678be5e3a480a31dfd55908164d
fetched_at: '2026-06-28T22:38:35.387620+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Aumento do Tamanho
  do campo "Código de Cliente" A1_COD
type: support-article
updated_at: '2023-01-17T12:00:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033530974-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Aumento-do-Tamanho-do-campo-C%C3%B3digo-de-Cliente-A1-COD
---

**Dúvida**Pode-se aumentar o tamanho do campo **A1\_COD**e não gerar inconsistência no sistema?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) -  a partir da versão 12.

**Solução**

Para aumentar o campo **A1\_COD**, precisará utilizar o **Grupo de Campos - Código Cliente/Fornecedor**.

O tamanho padrão do sistema é , porém o grupo de campo permite utilizar até 20 posições via alteração por grupo de campos.

Ao efetuar a alteração o tamanho  do campo código no Cliente (**MATA030**) , também será definido este tamanho para o código do Fornecedor (**MATA020**).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043939033/mceclip0.png)

Como a alteração é via grupo de campos, o sistema atualizará todas as tabelas que buscam o código do cliente/fornecedor,  deixando com tamanho escolhido, desta forma, não causando erros de um campo está com um tamanho e outro estar com tamanho padrão que é 6.

Com relação a relatórios, geralmente o sistema ajusta conforme a mudança na SX3, então não é para gerar nenhum problema quanto a posicionamento de campo e tamanho.

As alterações valerão para os novos registros do sistema, desta forma, se houver no sistema registros antigos com 6 posições, somente os registros antigos serão trazidos com 6 dígitos numa eventual consulta, já os novos obedecerão a nova configuração que for efetuada, senão o sistema poderá não encontrar o registro pesquisado.
