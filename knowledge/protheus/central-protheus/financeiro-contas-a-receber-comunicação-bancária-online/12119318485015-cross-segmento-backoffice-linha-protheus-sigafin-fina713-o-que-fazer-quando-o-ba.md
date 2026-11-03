---
article_id: 12119318485015
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: be5c2969467b5119919814a6180aaa2ac60382396f3bbb6b4fb5a1222add9762
fetched_at: '2026-06-28T22:37:49.164722+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - O que fazer
  quando o Banco faz o envio dos arquivos CRT e o KEY do Certificado Digital
type: support-article
updated_at: '2026-01-07T19:08:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12119318485015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA713-O-que-fazer-quando-o-Banco-faz-o-envio-dos-arquivos-CRT-e-o-KEY-do-Certificado-Digital
---

**Dúvida**  
O que fazer quando o Banco executa o envio dos arquivos CRT e o KEY do Certificado Digital?

**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA713 - Todas as versões

**Solução**

Nos casos em que o banco fornece os arquivos CRT e KEY, não é necessário realizar o procedimento por meio do Wizard de Conversão de Certificado (SIGACFG).

Basta adicionar os arquivos na pasta `\cert\ngf`, localizada dentro do diretório de dados do Protheus.

É fundamental que os nomes dos arquivos CRT e KEY correspondam exatamente ao nome informado na tela de configuração do Novo Gestor, na opção "Configuração de Novo Layout de Boleto".

![xxx.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/12119276014103)

**Saiba mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Não foi possível gerar os arquivos corretamente Erro ao extrair o Certificado de Autorização no CFGX060 Wizard de Conversão de Certificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10621741400087)
