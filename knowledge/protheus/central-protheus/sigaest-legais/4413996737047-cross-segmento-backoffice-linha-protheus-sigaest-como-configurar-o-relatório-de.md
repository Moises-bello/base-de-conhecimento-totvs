---
article_id: 4413996737047
category: SIGAEST - LEGAIS
content_hash: f5b92deed792c9e944521cf7e39c1403bc30f95cea6c353589e8ee10557cc76e
fetched_at: '2026-06-28T22:38:51.623677+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como configurar o
  relatório de registro de medicamentos MATR924 ?
type: support-article
updated_at: '2021-11-24T14:43:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413996737047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-configurar-o-relat%C3%B3rio-de-registro-de-medicamentos-MATR924
---

**Dúvida**Como configurar o relatório de registro de medicamentos (MATR924)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para Configuração do relatório deve seguir os passos abaixo:

1. É necessário ajustar alguns parâmetros via Configurador > Ambiente > Cadastro > Parâmetros:

- MV\_IMPPERI = .T.  Esse parâmetro define se o relatório deve ser impresso por período;

- MV\_RMEDAB = RMEDAB.TRM Esse parâmetro contém o nome do arquivo, que contém o termo de abertura do relatório;

- MV\_RMEDEN = RMEDEN.TRM Esse parâmetro contém o nome do arquivo, que contém o termo de encerramento do relatório;

**Importante:** Os arquivos estão disponíveis ao final desse documento. Esses arquivos devem ficar na pasta system do Protheus.

2. Após isso é necessário que os produtos pertinentes ao relatórios estejam cadastrados com seus devidos grupos preenchidos B1\_GRUPO;

3. Depois de validar os pontos acima, basta extrair o MATR924 conforme o Produto, Grupo e Período. Segue abaixo um exemplo do relatório:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413973726231/mceclip0.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
