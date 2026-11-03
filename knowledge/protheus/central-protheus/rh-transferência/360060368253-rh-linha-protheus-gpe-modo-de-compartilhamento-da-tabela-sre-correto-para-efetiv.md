---
article_id: 360060368253
category: RH - Transferência
content_hash: 4c372c4a9c740a57d6464eb11bce981deb27f85607c55dc6a5f8d5d7107ffe57
fetched_at: '2026-06-28T22:43:23.358281+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Modo de compartilhamento da tabela SRE correto
  para efetivação de transferência de funcionários entre empresas
type: support-article
updated_at: '2025-08-13T16:58:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060368253-RH-Linha-Protheus-GPE-Modo-de-compartilhamento-da-tabela-SRE-correto-para-efetiva%C3%A7%C3%A3o-de-transfer%C3%AAncia-de-funcion%C3%A1rios-entre-empresas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24270262574359)** Tempo aproximado para leitura**: 00:03:00 min**

**Dúvida**Qual o modo de compartilhamento correto da tabela SRE para transferência de funcionários entre empresas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o Sistema efetive a transferência entre Empresas, a tabela **SRE** - **Histórico** **de Transferências** - deve ser totalmente **Compartilhada** tanto na **Empresa Origem** quanto na **Empresa Destino**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098944594)

Após compartilhar a tabela é necessário renomear a mesma, apontando apenas para uma SRE. Para tal, abra a tabela de **Transferências - SRE** via **Configurador > Base de Dados > Dicionário > Arquivos;**Supondo que a transferência seja da empresa 99 para 01. Para outras empresas o processo será o mesmo:  
  
**Empresa 99 - SRE990** - Deve deixar essa tabela **Compartilhada** como na imagem acima  
**Empresa 01 - SRE010** -  Deve deixar essa tabela **Compartilhada também** e além disso, alterar o nome, de **SRE010** para **SRE990**Além disso, o tamanho dos campos **RE\_FILIALD** - Filial de Origem e **RE\_FILIALP** - Filial de Destino,  devem ter **tamanho 12.**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101159993)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000069002)  
  
Após fazer estes processos, salve as alterações feitas no SIGACFG e **Atualize a Base de dados.****Importante**Caso tenha alguma dúvida nesse processo, sugerimos que entre em contato com o suporte de **Framework** para obter auxílio  
  
**Observação:**  
Sempre que há em um mesmo SIGAMAT (Arquivo de Empresas), grupo de empresas **diferentes**, neste exemplo acima temos o grupo 99 e 01, a orientação é que seja usado apenas um arquivo para o gerenciamento das transferências, que no caso é a tabela **SRE**, mesmo que inicialmente não sejam previstas transferências entre as empresas do grupo, ainda assim deve-se manter um único controle, ou seja, uma única SRE recebendo as transferências e todas as SX2 apontando para ela, neste exemplo acima, apontar tanto a Empresa 01 quanto 99, **ambas para a SRE990**  
  
Caso este processo não tenha sido definido desde o início, ou seja, se cada empresa tem a sua SRE com movimentações, e agora precisa fazer a transferência entre empresas, deve fazer o procedimento acima, compartilhando e apontando apenas para uma SRE, e posteriormente os dados terão que ser unificados, ou seja, depois de apontar todas as SX2 das empresas para a **SRE990**, deve posteriormente, appendar os dados das demais SRE's na **SRE990**.

**Para saber mais:**

**[RH - Transferência](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781974-RH-Transfer%C3%AAncia)**

[RH - Linha Protheus - GPE - Movimentação de Tabelas em Transferência entre Empresas/Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057237614-RH-Linha-Protheus-GPE-Movimenta%C3%A7%C3%A3o-de-Tabelas-em-Transfer%C3%AAncia-entre-Empresas-Filiais)

[RH - Linha Protheus - GPE - Como realizar a transferência entre empresas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409859163671-RH-Linha-Protheus-GPE-Como-realizar-a-transfer%C3%AAncia-entre-empresas)
