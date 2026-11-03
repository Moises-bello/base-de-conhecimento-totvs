---
article_id: 360034675574
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 8119608385ce7340f0af776f761748eaab407fe6d098e26f15fd1627fb607d7a
fetched_at: '2026-06-28T22:42:07.791644+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-SP - 1º
  Passo - Atualização do Ambiente
type: support-article
updated_at: '2025-07-14T11:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034675574-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-SP-1%C2%BA-Passo-Atualiza%C3%A7%C3%A3o-do-Ambiente
---

**Ocorrência**

Necessário atualizar o ambiente TAF para utilização da GIA-SP.  
  
**Ambiente**Protheus - Livros Fiscais – A partir da versão 12.1.17.  
 **Causa**Necessidade das configurações para a geração do arquivo da **Nova GIA**através do **TAF**.  
 **Solução**

**1. Atualização Completa TAF  - Expedição Contínua**

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1126399>

12.1.2410: <https://tdn.totvs.com/pages/releaseview.action?pageId=634272553>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045038734)

**2. Atualização de Dicionário de dados - UPDDISTR:**

    É necessário substituir os pacotes de acordo com a atualização mais recente.  
  
    Será necessário executar o **UPDDISTR** para que sejam criados os campos necessários para correto funcionamento da GIA.   
  
    No pacote de atualizações periódicas, contém o dicionário de dados diferencial, que será responsável por criar os campos **C20\_UF, C20\_DUF** (Campo Virtual), **C1H\_CONTRI e C30\_CODIPA**.   
  
**C20\_DUF** (Campo Virtual) = Este campo não será criado no banco de dados, será criado somente no dicionário de dados.   
  
**OBS**.: Antes da Execução do UPDDISTR deve-se realizar o procedimento indicado abaixo:  
  
    Inserir o arquivo sdfbra.txt na pasta SystemLoad.  
  
    Dentro da pasta system, deve-se excluir os arquivos:  
  
    mpupdlog.log  
    mpupdlog.fpt  
    mpwizard.hlp  
    mpwizardhlp.lck  
  
    Dentro da pasta Appserver, deve-se excluir os arquivos:  
    mpupddistri.tsk  
    mppatch.exe

**3. Implementação Relatório Nova Gia - TAF:** 

[MP - FIS - NOVA GIA SP - Implementação do Relatório da Nova GIA SP, Rotina TAFRGSP.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038990574-MP-FIS-NOVA-GIA-SP-Implementa%C3%A7%C3%A3o-do-Relat%C3%B3rio-da-Nova-GIA-SP-Rotina-TAFRGSP-?source=search)
