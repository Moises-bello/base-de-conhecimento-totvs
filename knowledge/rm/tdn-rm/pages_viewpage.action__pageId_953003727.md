---
content_hash: 7ed52ba5352d6a65a1c8c2ea6ac7037ecd843c61322bcd822d6d40661f0b1f6b
fetched_at: '2026-06-29T00:12:10.812387+00:00'
page_id: '953003727'
product: rm
source: tdn-rm
title: Grupo Z - Informações Adicionais da NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003727
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo Z - Informações Adicionais da NF-e** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 399 | Z01 | infAdic | Grupo de Informações Adicionais | G | A01 |  | 0-1 |  |  |  |  |  |
| 400 | Z02 | infAdFisco | Informações Adicionais de Interesse do Fisco | E | Z01 | C | 0-1 | 1-2000 | 0(v2.0) | TMOVFISCAL.INFADICIONAISFISCO | Informações Adicionais ao Fisco | Aba Integrações do movimento, na pasta NF-e Estadual. |
| 401 | Z03 | infCpl | Informações Complementares de interesse do Contribuinte | E | Z01 | C | 0-1 | 1-5000 |  | TMOVFISCAL.INFCOMPLCONTRIBUINTE | Informações Complementares do Contribuinte | Aba Integrações do movimento, na pasta NF-e Estadual.  ***Observação***: A tag será montada concatenando as seguintes informações: - Se algum produto tiver CST 60 de ICMS será colocada a informação de CST 60; - Informações da saída ST 60 (Produto - Base ICMS ST - Valor ICMS ST) : CÓDIGO DO PRODUTO - BASE ST RETIDO = VALOR ST RETIDO; - Informações Complementares do Contribuinte (INFCOMPLCONTRIBUINTE); - Histórico do Movimento; - Dispositivo Legal da Natureza (Se o parâmetro "inicializa observação" estiver marcado). Se o ultrapassar o limite de 5000 Caracteres o campo será truncado. |
| 401a | Z04 | obsCont | Grupo Campo de uso livre do contribuinte | G | Z01 |  | 0-10 |  | Campo de uso livre do contribuinte, Informar o nome do campo no atributo xCampo e o conteúdo do campo no xTexto |  | Criação de campos complementares. | Mais informações em:  [Geração dos Campos Livres NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=422545956) |
| 401b | Z05 | xCampo | Identificação do campo | A | Z04 | C | 1-1 | 1-20 | Identificação do campo |  |  | Mais informações em:  [Geração dos Campos Livres NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=422545956) |
| 401c | Z06 | xTexto | Conteúdo do campo | E | Z04 | C | 1-1 | 1-60 | Conteúdo do campo |  |  | Mais informações em:  [Geração dos Campos Livres NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=422545956) |
| 401d | Z07 | obsFisco | Grupo Campo de uso livre do Fisco | G | Z01 |  | 0-10 |  | Campo de uso livre do Fisco. Informar o nome do campo no atributo xCampo e o conteúdo do campo no xTexto |  |  | Mais informações em:  [Geração dos Campos Livres NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=422545956) |
| 401e | Z08 | xCampo | Identificação do campo | A | Z07 | C | 1-1 | 1-20 | Identificação do campo |  |  | Mais informações em:  [Geração dos Campos Livres NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=422545956) |
| 401f | Z09 | xTexto | Conteúdo do campo | E | Z07 | C | 1-1 | 1-60 | Conteúdo do campo |  |  | Mais informações em:  [Geração dos Campos Livres NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=422545956) |
| 401g | Z10 | procRef | Grupo Processo referenciado | G | Z01 |  | 0-100 |  | (NT 2012/003) |  |  | Estas tag's serão preenchidas conforme os processos judiciais informados no Movimento e/ou Item. |
| 401h | Z11 | nProc | Identificador do processo ou ato concessório | E | Z10 | C | 1-1 | 1-60 | Identificador do processo ou ato concessório | DPROCESSOJUDICIAL.NUMERO |  |  |
| 401i | Z12 | indProc | Indicador da origem do processo | E | Z10 | N | 1-1 | 1 | 0=SEFAZ; 1=Justiça Federal; 2=Justiça Estadual;  3=Secex/RFB;  4= CONFAZ; 9=Outros | DPROCESSOJUDICIAL.TIPO | Será gerado com base do valor literal informado no campo Origem do Processo. |  |
| 401j | Z13 | tpAto | Tipo do ato concessório | E | Z10 | N | 0-1 | 2 | Tipo de ato concessório: (NT 2021.004) 08=Termo de Acordo; 10=Regime Especial; 12=Autorização específica; 14=Ajuste SINIEF 15=Convênio ICMS | DPROCESSOJUDICIAL.TIPOATOCONCESSORIO | Será gerado com base na informação do campo Tipo do Ato Concessório, localizado no Cadastro do Processo. |  |
