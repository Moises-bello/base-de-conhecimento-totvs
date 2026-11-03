---
article_id: 6427101620631
category: SIGAEST - PROCESSAMENTOS
content_hash: 73209825e7c1cf74f06a6c87cda08a8abdd0c008fc197ee7fd2325a3bb558c5e
fetched_at: '2026-06-28T22:39:04.875384+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Transaction count
  after EXECUTE indicates a mismatching number of BEGIN and COMMIT statements. Previous
  count = 0
type: support-article
updated_at: '2022-06-24T14:25:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6427101620631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Transaction-count-after-EXECUTE-indicates-a-mismatching-number-of-BEGIN-and-COMMIT-statements-Previous-count-0
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:12 min****Ocorrência**Ao executar rotinas de Processamento no Estoque ocorre o erro: *Transaction count after EXECUTE indicates a mismatching number of BEGIN and COMMIT statements. Previous count = 0*

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da release 12.1.27

**Causa**Foi corrigida a instrução interna T-SQL em um pacote de atualizações.

**Solução**Para resolver este problema, siga os passos abaixo:

**1. Atualização da Expedição Contínua do Estoque (para carga dos novos arquivos .ZPS dos Procedures):**

**[Clique aqui para baixar a Expedição Contínua do Estoque conforme a sua release](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/EST_expedicao_continua)**

**2. Atualização da versão do Gestor de Procedures, para sua última versão.**

**[Clique aqui para baixar a ultima versão do Gestor de Procedures](https://suporte.totvs.com/portal/p/10098/download?e=946864)**

**3. Reinstalar o Procedure causador do erro (em caso de dúvidas, reinstalar todos os Procedures do Estoque - do 14 ao 22)**

**Observação**: sempre atualizar o ambiente primeiramente em base de homologação com backup prévio do RPO.

Com isso, o esperado é de que problema não seja mais reproduzido.

**Atualizei com os pacotes acima e o meu problema persiste. O que fazer?**

Foram mapeados casos em que mesmo atualizando a Expedição Contínua do Estoque e Gestor de Procedures o problema persistia. Isso se dava por conta do LIB desatualizado. Com isso, basta manter o LIB atualizado **antes de aplicar novamente a atualização do Gestor de Procedures e reinstalação dos mesmos via Configurador.**

* Para atualizar o LIB, [clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/LIB_LABEL)
* Para conhecer o procedimento de atualização de LIB, [clique aqui](https://tdn.totvs.com/display/public/PROT/MP-+BD0054+-+Procedimento+para+atualizar+Lib+no+Protheus).

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro ao Instalar Procedure 18 - Must declare the scalar variable "@cEstFIS".](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6948454645271)*

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
