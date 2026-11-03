---
article_id: 36392336831639
category: SIGAEST - CUSTOS
content_hash: 04bbaff959ee0b4f9ee06d4bbc6bde99d2e851b6d91ca2069ffe9c228a56d334
fetched_at: '2026-06-28T22:39:00.427251+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Parameters must be
  of number or date type on MVULMES(SIGACUS.PRW)
type: support-article
updated_at: '2025-11-26T13:28:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36392336831639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Parameters-must-be-of-number-or-date-type-on-MVULMES-SIGACUS-PRW
---

O erro HELP MV\_ULMES ocorre ao tentar excluir movimentos no módulo de Estoque quando o parâmetro MV\_ULMES não está configurado exclusivamente para cada filial ou não existe de forma padrão. Também deve-se verificar as restrições de acesso 114 e 115 e a configuração do parâmetro MV\_DBLQMOV. A solução é garantir parâmetros MV\_ULMES exclusivos por filial e que MV\_DBLQMOV tenha data superior ao MV\_ULMES.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36392371749783) Tempo aproximado para leitura: **00:01:15 min**  
  
**Ocorrência**

Ao tentar excluir algum movimento no módulo de Estoque apresenta o HELP MV\_ULMES e em seguida o errorlog abaixo, como sanar esse incidente?

**THREAD ERROR ([FFF], XXXXXXX, XXXXXX)   14/11/2025 10:55:08**  
**Parameters must be of number or date type on MVULMES(SIGACUS.PRW) 07/08/2025 10:27:46 line : 3372**

**[TOTVS build: 7.00.240223P-20250326]**  
**Called from MATA460A(MATA461.PRX) 22/09/2025 14:57:57 line : 308**  
**Called from \_\_EXECUTE(APLIB090.PRW) 27/06/2025 17:07:18 line : 733**  
**Called from MDIEXECUTE(APLIB260.PRW) 27/06/2025 17:07:18 line : 923**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

Esse error.log é apresentado quando ocorre alguma das siturações abaixo:

**1-** O ambiente tem mais de uma Filial e uma das Filiais não tem o parâmetro **MV\_ULMES**de **forma exclusiva**;

**2-** Também caso não existir o parâmetro de forma Default, ou seja, sem atribuição de filial ao mesmo, o tornando comum para todas as filiais.

**3-** Verificar também no módulo Configurador no Cadastro de Usuário em "Restrições de Acesso" >> "Acessos", e preencher as opções 114 e 115 que também o help do MV\_ULMES não é apresentado.  
   
      **114 - MBrowse** - Visualiza outras filiais  
      **115 - MBrowse** - Edita registro de outras filiais

**4-** Valide a configuração e data do parametro **MV\_DBLQMOV**.

**Solução**

Para solucionar essa ocorrência, é necessário que cada filial possua um parâmetro **MV\_ULMES** de forma Exclusiva para cada uma das Filiais, certifique tambem se o parametro MV\_DBLQMOV esta com data superior ao parametro MV\_ULMES caso esteja tentando emitir algum documento.

***Saiba Mais:***

[SIGAEST - Funcionalidade do parâmetro MV\_ULMES](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009616322-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-par%C3%A2metro-MV-ULMES)

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
