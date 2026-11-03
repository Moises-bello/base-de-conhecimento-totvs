---
article_id: 360026949131
category: Gestão de Transportes (TMS)
content_hash: 2281e7d75600dccbd88e3837399c3092bc6ad7fb59ad4b9abe020dab50ed4276
fetched_at: '2026-06-28T22:45:33.430334+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - TMSAE80 Importação de Notas Fiscais - XML
type: support-article
updated_at: '2025-07-03T14:23:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026949131-Log%C3%ADstica-Linha-Protheus-TMS-TMSAE80-Importa%C3%A7%C3%A3o-de-Notas-Fiscais-XML
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30727945030807)***Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como importar notas fiscais dos clientes - **XML**para inclusão automática no **SIGATMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Para facilitar e agilizar a inclusão das notas fiscais dos clientes no módulo **SIGATMS**, o **Protheus TMS** oferece a funcionalidade **Importação de Documento do Cliente - TMSAE80.**Com essa funcionalidade, a transportadora recebe os arquivos **XML** das notas fiscais de seus clientes e ao processá-los, o Sistema inclui automaticamente as notas fiscais no Sistema com base nas informações dos arquivos **XMLs**, com isso, eliminando a necessidade de digitação manual e consequentemente, reduzindo o tempo de trabalho.  
Este processo é totalmente automatizado e funciona por meio da configuração do **Schedule** do fonte **TMSAE80**. Por esse motivo, o **TMSAE80** está ausente no menu do módulo **SIGATMS** e opera em segundo plano, garantindo mais eficiência no processo.  
  
**Processo para utilização:**

* **Cadastrar Schedule: SIGACFG** / **Ambiente** / **Schedule** / **Schedule**
* **Agent** / **Cadastro** / **Adicionar Agente**

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038965074)

* **Preencher o Agendamento / Cadastro**Nesse momento cadastrar a rotina **Importação de Documento do Cliente - TMSAE80**, deve ser cadastrada no agendamento para que o **JOB** responsável pela integração possa realizar a importação dos arquivos para o **Protheus**, em seguida clicar em **Recorrência.**

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039817453)

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038965134)

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039817513)

* Retornar em **Schedule** e iniciar os serviços.

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038965174)

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038965194)

* Após o serviço iniciado, observar no seu **appserver.ini**, se foram criadas automaticamente as configurações:

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039817573)

* Na pasta de instalação do **Protheus**, dentro do diretório **Protheus\_data** será criada a pasta **XMLNFE.**

![8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039817593)

* Contendo as pastas:**ERR, NEW, OLD**

![9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038965234)

* Caso as pastas não sejam criadas automaticamente, elas poderão ser criadas manualmente. Para isso, é necessário possuir permissão para incluir pastas no servidor do **Protheus**.
* As **Notas Fiscais** importadas com sucesso, são gravadas na rotina **NF - Nota Fiscal -  Atualizações/Movimentos/EDI/Nota Fiscal - TMSAE55,** tabela **DE5.**
* As **Notas Fiscais** não importadas estão disponíveis na rotina **NF. Não Importad.** - **Atualizações/Movimentos /EDI/NFes não Importad. - TMSAE85,** tabela **DEV**. Nesta rotina, na opção **Reprocessar**, é possível realizar o reprocessamento do arquivo para realizar novamente a importação. Esta opção deve ser utilizada após o ajuste da inconsistência ocorrida na importação.   
    
  **Saiba mais**Para mais informações sobre os cadastros necessários para a execução da rotina **TMSAE80,** acesse o *link*: **[Logística - Linha Protheus - TMS - Cadastros para importação de XML via Importação de Notas Fiscais - TMSAE80](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000288362-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-para-importa%C3%A7%C3%A3o-de-XML-via-Importa%C3%A7%C3%A3o-de-Notas-Fiscais-TMSAE80?source=search)  
    
  Glossário**  
  **CNPJ** - Cadastro Nacional da Pessoa Jurídica;  
  **CT-e** - Conhecimento de Transporte Eletrônico;  
  **EDI** - *Electronic Data Interchange;*  
  **NF** - Nota Fiscal;  
  **SIGACFG** - Configurador;  
  **SIGATMS** - Gestão de Transportes;  
  **XML** - *Extensible Markup* *Language.*
