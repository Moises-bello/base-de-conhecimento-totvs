---
content_hash: a8c8afe9d934f26cc408dc96e934e143918155d956ae63c3b5b0162be5318d34
fetched_at: '2026-06-29T00:05:51.901688+00:00'
page_id: '1056143227'
product: rm
source: tdn-rm
title: XML NFS-e Modelo único para integração com o TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227
version: 13
---

### Voltar para

| Nome | Pai | Tipo | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **rps** | **raiz do xml** | **Grupo** | **1-1** | **Grupo raiz do xml da NFS-e** | **-** |  |
| id | rps | Atributo | 1-1 | Informe o atributo ID. (Ex.: rps id=”rps:1016”) | O Id é gerado com o número do Movimento no RM |  |
| tssversao | rps | Atributo | 1-1 | Versão (Ex: tssversao=”2.00”) | É gerado fixo com o valor 2.00 |  |
| assinatura | rps | Elemento | 1-1 | Código hash de validação do conteúdo. |  | É gerada com o resultado da expressão abaixo será encriptado como codigo hash. A assinatura deverá ser montada conforme regra abaixo InscricaoMunicipalPrestador + SerieRPS + NumeroRPS + DataEmissaoRPS + Tributacao + SituacaoRPS + TipoRecolhimento + strValorTotalServ + strValorTotalDeducoes + CodigoAtividade + CNPJTomador InscricaoMunicipalPrestador => Tamanho 11 utilizar zeros à esquerda para completar SerieRPS => Tamanho 5 Utilizar espaços à direita para completar NumeroRPS => Tamanho 12 utilizar zeros à esquerda para completar DataEmissaoRPS => Utilizar mascará yyyyMMdd Tributacao => Tamanho 2 Utilizar espaços à direita para completar SituacaoRPS => Tamanho 1 TipoRecolhimento => Tamanho 1 strValorTotalServ => Tamanho 15 utilizar zeros à esquerda para completar strValorTotalDeducoes => Tamanho 15 utilizar zeros à esquerda para completar CodigoAtividade => Tamanho 10 utilizar zeros à esquerda para completar CNPJTomador => Tamanho 14 utilizar zeros à esquerda para completar    Links Relacionados:  [CNPJ para assinatura de lotes de NFS-e](https://tdn.totvs.com/display/LRM/CNPJ+para+assinatura+de+lotes+de+NFS-e) |
| **identificacao** | **rps** | **Grupo** | **1-1** |  |  |  |
| **substituicao** | **rps** | **Grupo** | **0-1** |  |  |  |
| **cancelamento** | **rps** | **Grupo** | **0-1** |  |  |  |
| **atividade** | **rps** | **Grupo** | **0-1** |  |  |  |
| **prestador** | **rps** | **Grupo** | **1-1** |  |  |  |
| **prestacao** | **rps** | **Grupo** | **0-1** |  |  |  |
| **intermediario** | **rps** | **Grupo** | **0-1** |  |  |  |
| **tomador** | **rps** | **Grupo** | **1-1** |  |  |  |
| **servico** | **rps** | **Grupo** | **1-1** |  |  |  |
| **valores** | **rps** | **Grupo** | **1-1** |  |  |  |
| **fatura** | **rps** | **Grupo** | **0-1** |  |  |  |
| **pagamentos** | **rps** | **Grupo** | **0-1** |  |  |  |
| **deducoes** | **rps** | **Grupo** | **0-1** |  |  |  |
| **infcompl** | **rps** | **Grupo** | **0-1** |  |  |  |
| **construcao** | **rps** | **Grupo** | **0-1** |  |  |  |
| **impostois** | **rps** | **Grupo** | **0-1** |  |  |  |
| **impostoibscbs** | **rps** | **Grupo** | **0-1** |  |  |  |
| **ISTot** | **rps** | **Grupo** | **0-1** |  |  |  |
| **IBSCBSTot** | **rps** | **Grupo** | **0-1** |  |  |  |
| **totTrib** | **rps** | **Grupo** | **0-1** |  |  |  |

Dicas
