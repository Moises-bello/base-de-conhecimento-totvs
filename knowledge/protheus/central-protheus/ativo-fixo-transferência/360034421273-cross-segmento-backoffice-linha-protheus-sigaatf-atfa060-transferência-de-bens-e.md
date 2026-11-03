---
article_id: 360034421273
category: Ativo Fixo - Transferência
content_hash: 9114709ca4d478c7f6c501fd7c9ecba3ec8fb8b0b62772f52c0d9dc3c8006fa9
fetched_at: '2026-06-28T22:41:52.147797+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 Transferência
  de bens entre filiais com geração de NF apresenta  HELP: AFA060NFE'
type: support-article
updated_at: '2022-05-09T13:44:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034421273-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-Transfer%C3%AAncia-de-bens-entre-filiais-com-gera%C3%A7%C3%A3o-de-NF-apresenta-HELP-AFA060NFE
---

**Ocorrência**Ao efetuar transferência  de bens entre filiais com geração de NF apresenta HELP:AFA060NFE

**Ambiente**Microsiga Protheus – Ativo Fixo – A partir da versão 11.80]  
  
**Causa**Esse incidente ocorre, pois os cadastros usados para TES e Produto não existe na filial destino.  
  
**Solução**Avalie  os seguintes passos:

1. Para transferência do bem com emissão de nota fiscal é necessário, além do preenchimento padrão, preencher as seguintes informações:

* Fornecedor;
* Número da Nota Fiscal;
* Série;
* Produto vinculado.

2.  No TES de Entrada/Saída (**Cadastro de TES (MATA080)**  utilizado para transferência, além dos campos padrões, também é necessário preencher os campos abaixo:

* + Gera Dupl. (**F4\_DUPLIC**) = NÃO
  + Atual.Ativo (**F4\_ATUATF**) = NÃO
  + Atu.Estoque (**F4\_ESTOQUE**) = NÃO

**Importante:** Se a tabela**Tipos de Entrada e Saída (SF4)** estiver exclusiva, deve-se cadastrar os dados em ambas as filiais.

3.Os campos informados abaixo devem estar, obrigatoriamente, preenchidos no bem que será transferido.

* A inclusão do Bem pode ser realizada a partir da rotina de**Documentos de Entrada (MATA103)** ou por inclusão manual via rotina de **Ativos (ATFA012).**  
    
  Na aba **Dados do Bem** , preencher os campos:
  + Nota Fiscal (**N1\_NFISCAL**);
  + Serie N.F. (**N1\_SERIE**);
  + Cod. Fornec. (**N1\_FORNEC**);
  + Loja (**N1\_LOJA**).  
  Na aba **Dados Complementares**, preencher o campo:   
  + Cód Produto (**N1\_PRODUTO**)

mais detalhes leia : [ATFA060 → Processo para gerar nota fiscal a partir da transferência do bem.](http://tdn.totvs.com/pages/releaseview.action?pageId=416848333)
