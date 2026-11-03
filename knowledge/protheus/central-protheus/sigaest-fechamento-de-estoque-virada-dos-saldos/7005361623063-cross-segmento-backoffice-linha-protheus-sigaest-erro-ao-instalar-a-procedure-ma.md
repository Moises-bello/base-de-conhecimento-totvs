---
article_id: 7005361623063
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 5a16429d701e1b3dcea0a30f9b11f0e5c968162cbbb7b418d7398b47a531faf9
fetched_at: '2026-06-28T22:38:52.713178+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro ao instalar a
  procedure [MAT036_17_01] - Invalid column name 'BJ_FILIAL'
type: support-article
updated_at: '2024-12-16T18:23:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7005361623063-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Erro-ao-instalar-a-procedure-MAT036-17-01-Invalid-column-name-BJ-FILIAL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28568249714839) Tempo aproximado para leitura: **00:01:15 min****Ocorrência**Erro ao instalar a procedure [MAT036\_17\_01] - Error : 207 (S0022) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Invalid column name 'BJ\_FILIAL'

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - A partir da release 12.1.27

**Causa**Foi corrigida a instrução interna T-SQL em um pacote de atualizações.

**Solução**Para resolver este problema, siga os passos abaixo:

**1. Atualização da Expedição Contínua do Estoque (para carga dos novos arquivos .ZPS dos Procedures):**

**[Clique aqui para baixar a Expedição Contínua do Estoque conforme a sua release](https://tdn.totvs.com/x/2hgdHw)**

**2. Atualização da versão do Gestor de Procedures, para sua última versão.**

**[Clique aqui para baixar a ultima versão do Gestor de Procedures](https://suporte.totvs.com/portal/p/10098/download?e=946864)**

**3. Reinstalar o Procedure 17**

**Observação**: sempre atualizar o ambiente primeiramente em base de homologação com backup prévio do RPO. Com isso, o esperado é de que problema não seja mais reproduzido.

**Atualizei com os pacotes acima e o meu problema persiste. O que fazer?**

Foram mapeados casos em que mesmo atualizando a Expedição Contínua do Estoque e Gestor de Procedures o problema persistia. Isso se dava por conta do LIB desatualizado. Com isso, basta manter o LIB atualizado **antes de aplicar novamente a atualização do Gestor de Procedures e reinstalação dos mesmos via Configurador.**

* Para atualizar o LIB, [clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/LIB_LABEL)
* Para conhecer o procedimento de atualização de LIB, [clique aqui](https://tdn.totvs.com/display/public/PROT/MP-+BD0054+-+Procedimento+para+atualizar+Lib+no+Protheus).

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro ao Instalar Procedure 18 - Must declare the scalar variable "@cEstFIS".](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6948454645271)*

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
