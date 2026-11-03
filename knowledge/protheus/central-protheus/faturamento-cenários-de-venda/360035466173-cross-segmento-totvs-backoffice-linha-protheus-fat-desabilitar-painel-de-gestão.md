---
article_id: 360035466173
category: Faturamento - Cenários de Venda
content_hash: c28a37c95bc176eba3284df73737485892e8d12c8ed0051fe870e8e6092581a7
fetched_at: '2026-06-28T22:38:33.902091+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - Desabilitar Painel
  de Gestão
type: support-article
updated_at: '2023-01-30T21:15:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035466173-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FAT-Desabilitar-Painel-de-Gest%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao tentar alterar uma tabela de preços o sistema apresenta mensagem:  
“*Painel de Gestão Habilitado, para alterações de preços ou novos produtos, utilizar a Publicação de Preços.*”  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Faturamento – A partir da versão 11.80  
  
**Solução**O Painel de Gestão é uma funcionalidade do módulo SIGALOJA, para maiores detalhes das funcionalidades acessar disponível abaixo ou entrar em contato com a equipe de suporte do módulo SIGALOJA.

Caso não utilize esta funcionalidade (ou não utilize o módulo SIGALOJA), desabilite o Painel de Gestão, possibilitando a inserção e/ou alteração das tabelas de preços pela rotina **OMSA010**, informando o parâmetro **MV\_LJGEPRE** com .F. ele ira desabilitar.

![image2016-10-17 14:49:23.png](https://tdn.totvs.com/download/attachments/267795887/image2016-10-17%2014%3A49%3A23.png?version=1&modificationDate=1476723114000&api=v2)

**Saiba Mais**  
[Funcionalidades do Painel de Gestão - SIGALOJA](http://tdn.totvs.com/pages/viewpage.action?pageId=47908963)
