---
article_id: 360025436711
category: ADVPL - Ponto de Entrada
content_hash: 8444ebe82481c9ac62f4a180722a0567bcf83b55c997042170d7298763ef1e1a
fetched_at: '2026-06-28T22:40:11.499745+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Como informar o campo
  COD_PART no ponto de entrada SPDFISBLCK
type: support-article
updated_at: '2021-12-21T21:05:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025436711-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Como-informar-o-campo-COD-PART-no-ponto-de-entrada-SPDFISBLCK
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como informar o campo COD\_PART no ponto de entrada **SPDFISBLCK**?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Ao utilizar o ponto de entrada [SPDFISBLCK](http://tdn.totvs.com/pages/releaseview.action?pageId=203761344) é necessário observar que toda a confecção do bloco K é desconsiderada no padrão e substituída pela que foi definida no PE, de forma totalmente manual, desde a criação das tabelas temporárias até a quantidade e informações de cada campo e registro do bloco em questão. As tabelas temporárias necessária são criadas neste PE, então primeiramente observe o tamanho do campo em questão, linha:

```
AADD(aCampos,{"COD_PART" ,"C",11,0}) //Campo 06 do registro K200
```

Neste caso defini com 11, a composição seria 'SA1' + Código(neste ambiente é padrão tamanho 6) + Loja do cliente.  
Ao adicionar a informação no campo, ficaria:

```
(cAliasK200)->COD_PART := 'SA100000101'
```

**O campo 6 COD\_PART somente será emitido com o valor de um cliente devidamente cadastrado no Protheus.**O exemplo documentado deve ser utilizado somente como referência, pois foi confeccionado com base na estrutura do ambiente do responsável pela documentação.

O tamanho do campo COD\_PART na tabela temporária deve ser criado com base no tamanho da sua tabela SA1/SA2.

O seek que a rotina padrão realiza é:

```
SA1->(MsSeek (xFilial ("SA1")+Substr((aAlias[K200])->COD_PART,4,Len((aAlias[K200])->COD_PART))))
```

A ordem de pesquisa do índice neste momento é a 1, Filial+Código+Loja, portanto caso o campo esteja saindo em branco, esteja emitindo um cliente ou fornecedor diferente do que foi informado no ponto de entrada, ou gerando o erro '**array out of bounds ( 1 of 0 ) on BLOCOK(SPEDXFUN.PRW)**', valide o seek acima no ponto de entrada, com o COD\_PART informado, para ter certeza de que a composição é a correta para esta busca.  
  
**Saiba mais**  
[SPDFISBLCK Geração do bloco K no SPED Fiscal - ALIAS no Banco de Dados](https://tdn.totvs.com/pages/releaseview.action?pageId=611789188)
