---
article_id: 4410967360535
category: TAF - REINF
content_hash: 5ff20be2ab72cf6b48b29c91f3739fc8451bd1c892f7e9ccda3f0207141a276e
fetched_at: '2026-06-28T22:41:33.557785+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF -  Erro HTTP Painel Reinf:
  Não é possível acessar este site ou Conexão Recusada'
type: support-article
updated_at: '2023-03-31T16:34:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410967360535-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-HTTP-Painel-Reinf-N%C3%A3o-%C3%A9-poss%C3%ADvel-acessar-este-site-ou-Conex%C3%A3o-Recusada
---

**Dúvida**

Erro ao acessar o painel REINF "Não é possível acessar este site"

**Ambiente**

TAF - A partir de 12.1.25

**Solução**

  O erro pode ocorrer por alguns motivo.

1° Caminho da PATCH errado no Appserver.ini.

EX: O caminho deve seguir a estrutura conforme documentação:

[TAF – REINF - Configuração Painel Reinf - Appserver](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409133202199-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf-Appserver?source=search)

Importante: No seu ambiente contém a pasta protheus\_data aonde deve ser criada a pasta http-root.

O caminho do htttp-root deve ser o mesmo caminho da protheus\_data do environment do ambiente.

[HTTP]  
Enable=1  
Port=8081  
Path=c:\users\totvs\protheus\_data\http-root

2° A Porta inserida no Appserver.ini diferente da porta configurada no parâmetro MV\_GCTPURL.

3° A Porta inserida deve ser exclusiva, caso haja outro serviços com a mesma porta ocorre este erro.

Teste validação do HTTP:

**1 - Validar se o servidor HTTP está no ar:**

Na pasta http-root que fica dentro do RootPath, criar um arquivo chamado teste.csv.

Na URL do servidor digitar: [http://SeuIP:PortaHTTP/teste.csv](http://seuipportahttp/).

Se o servidor HTTP estiver configurado corretamente, será realizado o download do arquivo teste.csv.

**2 - Validar se o parâmetro MV\_GCTPURL está preenchido de acordo com as configurações do arquivo appserver.ini:**

Exemplo: [http://IP:PortaHTTP](http://ipportahttp/).

**3 - Validar se está sendo utilizado mais de um serviço na mesma porta:**

Exemplo: Servidor HTTP na porta 78 e Help do Protheus na porta 78.  
Neste caso é necessário utilizar portas diferentes para os serviços.
