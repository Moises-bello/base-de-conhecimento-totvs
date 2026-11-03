---
article_id: 360020914632
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 901000cf175b333bfcdfce19f9e207432384e37ff753ed12deb90e4a927dc3c2
fetched_at: '2026-06-28T22:38:43.998206+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Atualização de Estoque tardia
  na geração da NF de Saída MV_NFS_JOB
type: support-article
updated_at: '2025-10-31T20:32:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020914632-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Atualiza%C3%A7%C3%A3o-de-Estoque-tardia-na-gera%C3%A7%C3%A3o-da-NF-de-Sa%C3%ADda-MV-NFS-JOB
---

**Dúvida**Help **A520NEST** para exclusão de nota fiscal no sistema.  
Qual a finalidade do parâmetro **MV\_NFS\_JOB**?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Solução**Se o parâmetro **MV\_NFS\_JOB** estiver **habilitado,** um **JOB** é executado para a atualização do estoque após a geração da nota fiscal. Nestes casos, o documento de saída é gerado sem atualização de estoque e os campos **C9\_BLEST** e **C9\_BLCRED** são gravados com conteúdo **ZZ.** Por este motivo não é permitida a exclusão da nota.

O Job **FATXJOB** tem a função de **regravar** os campos **C9\_BLEST** e **C9\_BLCRED** com conteúdo **10** e chamar a função de atualização de estoque.

Sendo assim, se o parâmetro **MV\_NFS\_JOB estiver habilitado**, **o JOB FATXJOB** **também deve estar**. Caso contrário, se não houver Job configurado, o parâmetro MV\_NFS\_JOB deve ser alterado para **.F.**

Há duas maneiras de executar a atualização de estoque, sendo que uma não depende da outra, estou deixando a documentação para auxiliar.

**Saiba Mais:**  
**[Atualização de Estoque tardia na geração da NF de Saída ( MV\_NFS\_JOB )](https://tdn.totvs.com/pages/releaseview.action?pageId=58098378)**

Veja nosso Webinar: **[Análise e Bloqueio de Estoque no Faturamento (SIGAFAT)](https://youtu.be/6XfctVxULuY)**
