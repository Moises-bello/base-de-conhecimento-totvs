---
article_id: 33881661439895
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 9c93582b50dc309e9e63002ef86c2a542493a7649a9383365e56fa8525564397
fetched_at: '2026-06-28T22:37:22.864153+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help A120LINOK ao encerrar
  Medição no Gestão de Contratos
type: support-article
updated_at: '2026-02-06T18:03:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33881661439895-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-A120LINOK-ao-encerrar-Medi%C3%A7%C3%A3o-no-Gest%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33881661431703) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como tratar a ocorrência do Help A120LINOK ao Encerrar uma Medição no Gestão de Contratos ?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**  
Para a tratativa do help de validação do help A120LINOK abaixo que pode também ser gerado/gravado em um txt conforme exemplo abaixo:

------------------------------------help---------------------------------------  
help:A120LINOK  
Solicitacao de Compra ja atendida.Item: 0001  
  
Tabela SC7 05/01/2026 09:44:38  
DT Emissao - C7\_EMISSAO := 05/01/2026  
Fornecedor - C7\_FORNECE := 002135  
Loja - C7\_LOJA := 01  
Cond. Pagto - C7\_COND := 030  
- ALCADA := S  
- MED\_GCT := GCT  
Moeda - C7\_MOEDA := 1  
Contato - C7\_CONTATO :=  
Filial Entr. - C7\_FILENT :=  
Vlr.Frete - C7\_FRETE := 0  
Vlr.Despesas - C7\_DESPESA := 0  
Vlr.Seguro - C7\_SEGURO := 0  
Mensagem - C7\_MSG :=  
Reajuste - C7\_REAJUST :=  
Cod. Usuario - C7\_USER := 000021  
--------------------------------------------------------------------------------  
Tabela SC7 05/01/2026 09:44:38  
Erro no Item 1  
--------------------------------------------------------------------------------  
Item - C7\_ITEM := 0001  
Produto - C7\_PRODUTO := 000033  
Descricao - C7\_DESCRI := SUPORTE INFORMATICA  
Quantidade - C7\_QUANT := 1  
Qtde da SC - C7\_QTDSOL := 1  
Unidade - C7\_UM := UN  
Qtd. 2a UM - C7\_QTSEGUM := 0  
Prc Unitario - C7\_PRECO := 40519.13  
Aliq. IPI - C7\_IPI := 0  
Dt. Entrega - C7\_DATPRF := 05/01/2026  
Armazem - C7\_LOCAL := 01  
Tipo Entrada - C7\_TES :=  
Observacoes - C7\_OBSM :=  
Item Medicao - C7\_ITEMED := 004  
Centro Custo - C7\_CC := 6204011  
Cta Contabil - C7\_CONTA := 4150100010  
Item Conta - C7\_ITEMCTA :=  
Cod Cl Val - C7\_CLVL :=  
Num.Contrato - C7\_CONTRA := 000000000000076  
Rev.Contrato - C7\_CONTREV := 003  
Num.Planilha - C7\_PLANILH := 000001  
Num.Medicao - C7\_MEDICAO := 001047  
Cod Nota Emp - C7\_CODNE :=  
Item Nt Emp - C7\_ITEMNE :=  
Fil. Origem - C7\_FISCORI := 010101  
Numero da SC - C7\_NUMSC := 000505  
Item da SC - C7\_ITEMSC := 0001  
Projeto Cred - C7\_EC05CR :=  
Projeto Deb - C7\_EC05DB :=  
Rateio - C7\_RATEIO := 2  
Erro --> Inconsistencia na Linha de Itens  
----------------------------------------------------------

Que ocorre ao encerrar uma Medição através do Gestão de Contratos, o help possui sua ocorrencia devido a uma validação que é padrão do sistema.

Caso se tenha esta ocorrência no ambiente abaixo artigo que reporta sobre ele e a possibilidade existente de tratativa para que ele não ocorra:

[GCT0164\_Encerrar medição de Solicitação de compra já atendida](https://tdn.totvs.com/pages/releaseview.action?pageId=948638443)

***Saiba Mais:***

[GCT0164\_Encerrar medição de Solicitação de compra já atendida](https://tdn.totvs.com/pages/releaseview.action?pageId=948638443)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
