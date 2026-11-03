---
article_id: 4407150451991
category: 'Aplicativo MNTNG '
content_hash: 14585673c538aee664cb303bffc84e783053ce0e8627b5d20ef71f246e691817
fetched_at: '2026-06-28T22:42:37.629843+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Configuração Ambiente de Homologação
type: support-article
updated_at: '2025-06-24T14:57:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407150451991-Manufatura-Linha-Protheus-APP-MNT-Configura%C3%A7%C3%A3o-Ambiente-de-Homologa%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33017916191255)*** Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como configurar o ambiente de homologação do aplicativo **MNT NG**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Versão 12  
  
**Solução**Para a configuração de um ambiente de homologação para o **MNT NG** é necessário que o mesmo seja uma réplica do ambiente de produção, porém com o **IP/porta** do serviço Rest do ambiente de homologação deve ser distinto da Produção, visto que será necessário possuir um **Alias Mingle** direcionado ao ambiente de homologação. Para isso, considere os itens listados abaixo:

* Criar uma réplica ao ambiente **Protheus** utilizado em produção, para isso deve ser realizado uma cópia do **binário**, **banco de dados**, **RPO - Recruitment Process Outsourcing** e **dicionário de dados**;
* Ajustar o arquivo de configuração **appserver.ini** de acordo com o ambiente de homologação, ou seja, alterar nomenclatura do banco, caminho do **RPO**, dicionário de dados. Nas seções de configuração do **WS REST** é necessário alterar na seção **HTTPREST** o **IP/porta (chave Port)** para os dados correspondentes ao novo ambiente de homologação;
* Solicite um novo **Alias mingle** para o aplicativo **MNT NG** direcionado ao ambiente de homologação. A solicitação do **Alias mingle**deve ser gerada a partir do <https://mingle.totvs.com.br/landpage/>
