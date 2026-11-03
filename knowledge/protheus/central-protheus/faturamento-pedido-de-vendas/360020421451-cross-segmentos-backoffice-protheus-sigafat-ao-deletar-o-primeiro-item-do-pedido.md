---
article_id: 360020421451
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1f842eeb9f6c95b6481f9d564ffcc6606dd88832fd6e984fdcd961b45f50c40e
fetched_at: '2026-06-28T22:38:39.639024+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - Ao deletar o primeiro item
  do Pedido de Vendas o sistema retorna o alerta: Help A410FAT'
type: support-article
updated_at: '2025-12-29T20:20:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020421451-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ao-deletar-o-primeiro-item-do-Pedido-de-Vendas-o-sistema-retorna-o-alerta-Help-A410FAT
---

**Ocorrência**  
Ao deletar o primeiro item do Pedido de Vendas o sistema retorna o alerta: Help **A410FAT.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Causa**  
A validação do help A410FAT ocorre, normalmente, quando os campos C6\_QTDENT e C6\_NOTA estão preenchidos.

Essa validação está definida no fonte MATV410A e é acionada nas seguintes situações:

* Quando um item possuir quantidade entregue não deve ser permitida a exclusão neste item. O sistema olhará para os campos **C6\_QTDENT** que não pode ser diferente de zero e para o campo **C6\_NOTA** que não pode estar preenchido. Sendo o campo diferente de zero e/ou **C6\_NOTA** estando preenchido, a mensagem será apresentada.
* A outra validação se utilizar grade de produtos verifica a grade referente ao produto selecionado. Caso exista quantidade entregue para algum item da grade não permite a exclusão. Sistema olhará para o campo **C6\_GRADE** que se for igual a **S** não pode ter o campo **C6\_QTDENT** diferente de zero. Se estiver diferente, a mensagem é apresentada.

**Solução**  
Para corrigir o problema, siga uma das alternativas abaixo:

1. Se o pedido for de **Devolução de Compras**, verifique se a **Numeração do Pedido** que esta incluindo **já existe na SC5**, ou seja, se já existe outro pedido com o mesmo número. Caso exista, corrija a numeração.

2. Se pedido for de **Devolução de Poder de Terceiros**, uma possível solução é efetuar o retorno manualmente no pedido de venda conforme instruções abaixo:

     1. A saída deve ser efetuada pelo Pedido de Venda **MATA410**;   
     2. O Tipo do Pedido deve ser **N - Normal**, pois é obrigatório a informação do Cliente;    
     3. A Pergunta **Poder Terc.** (**F4\_PODER3**) deve estar preenchida como **D - Devolução**;  
     4. Pressionar **F4** na quantidade para selecionar a nota original.

3. Se o pedido for  **Normal**, verifique se a numeração trazida para esse novo pedido já existe no registro da tabela SC5. Em alguns casos em que a sequência de numeração de perde é repetida com algum registro que já possui **C6\_QTDENT** e **C6\_NOTA** já preenchidos.

Para ajuste da sequencia de numeração utilize a documentação :  
[FAT0046 Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=235570751%20)
