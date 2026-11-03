---
content_hash: 73dbbbdc325588c1a4296cd0436d8cb0bebd0af7e9c22dfc183afbad24f5f70e
fetched_at: '2026-06-29T00:09:07.209148+00:00'
page_id: '384575719'
product: rm
source: tdn-rm
title: 3361339 FISCAL01-5808 DT - NF-e Exportação - Referência dos itens de exportação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384575719
version: 3
---

# NF-e Exportação - Referência dos itens de exportação

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio NF-e |
| **Situação/Requisito:** | Alterar o processo de emissão da NF-e para gerar as referências da exportação indireta somente considerando a nota de compra |
| **Solução/Implementação:** | Foi modificado o processo de emissão da NF-e de exportação indireta para selecionar as referência do item referência somente da nota de compra.  O filtro das referências para identificar qual é a nota de compra é realizado pelo tipo da natureza de operação do item (Entrada ou Saída). Serão selecionadas as referências dos itens que utilizaram natureza de entrada na nota referenciada.    Exemplo do Cadastro da Natureza   Rejeição Caso a quantidade total relacionada ao item da nota de exportação (é considerado somente o relacionamento com a nota da compra) não seja igual a quantidade do próprio item a SEFAZ irá rejeitar a nota com a seguinte mensagem:  NF-e foi rejeitada. Erro: Rejeicao: Somatorio das quantidades informadas na Exportacao Indireta nao corresponde a quantidade total do item  014 - NFe não autorizada - Corrija o problema e retransmita as notas fiscais eletrônicas. 346/Rejeicao: Somatorio das quantidades informadas na Exportacao Indireta nao corresponde a quantidade total do item |
