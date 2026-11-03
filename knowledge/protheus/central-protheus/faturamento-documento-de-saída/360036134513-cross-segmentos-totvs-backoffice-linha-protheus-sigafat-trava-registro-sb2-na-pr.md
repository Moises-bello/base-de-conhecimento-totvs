---
article_id: 360036134513
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 213273d9c1b6e5125f89550fa20516c011760955961c8a9936638bd26b6971bb
fetched_at: '2026-06-28T22:38:45.095828+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Trava registro
  SB2 na preparação do Documento de Saída
type: support-article
updated_at: '2021-07-29T16:38:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036134513-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Trava-registro-SB2-na-prepara%C3%A7%C3%A3o-do-Documento-de-Sa%C3%ADda
---

**Ocorrência**Trava registro SB2 na preparação do Documento de Saída (**MV\_FATTRAV**).   
  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus) –  A partir da versão 12.  
  
**Causa**

Na **preparação do documento** de saída por mais de um usuário **simultaneamente**, ocorre **trava** do registro da tabela **SB2**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047304813/mceclip0.png)

Isso ocorre quando mais de um usuário prepara documentos de saída simultaneamente, dessa forma,  ocorre trava do registro da tabela SB2 (Saldo Físico) do produto.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se possui em seu ambiente a configuração do parâmetro **MV\_FATTRAV**;  
2. Configura o parâmetro com o conteúdo **3** ou **4**.

**Obs:  a partir do appserver versão 13.9.1.4, liberado em 14.12.2020 houve uma melhoria no contador de locks para não impedir a execução das rotinas caso a conexão esteja transacionada, melhorando o travamento de registros, desta forma, além de configurar o parâmetro é interessante avaliar a atualização do binário.**

**Saiba mais**:[**https://tdn.totvs.com/x/Y8zuDQ**](https://tdn.totvs.com/x/Y8zuDQ)

**Obs**: Dentro do processo de Faturamento, uma forma para trabalhar o uso da tabela SB2 e evitar seu travamento é efetuar a atualização do estoque posterior a geração da nota com a opção de atualização de estoque tardia através de JOB, maiores informações, acesse: **[MP - FAT - Atualização de Estoque tardia na geração da NF de Saída MV\_NFS\_JOB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020914632-MP-FAT-Atualiza%C3%A7%C3%A3o-de-Estoque-tardia-na-gera%C3%A7%C3%A3o-da-NF-de-Sa%C3%ADda-MV-NFS-JOB)**

**Saiba Mais: [FAT0241 O registro encontra-se Bloqueado por outro usuário](http://tdn.totvs.com/pages/releaseview.action?pageId=329024248)**
