---
content_hash: 79ef72bb8477d12cc0feb8fac0da5f27f1fdacd6377b066b97aa8ddeccb29981
fetched_at: '2026-06-29T00:11:49.390022+00:00'
page_id: '832637977'
product: rm
source: tdn-rm
title: Análise Proativa de Banco de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=832637977
version: 27
---

Este documento objetiva orientar os procedimentos para o compartilhamento do Schema de banco de dados através do RM Atualizador.

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Banco de Dados |
| **Versão RM** | : | A partir da Versão 12.1.2310 |
| **Banco de Dados** | : | SQL Server e Oracle |
| **Processo** | : | Atualizador RM |
| **Sub Processo** | : | Compartilhamento do Schema ( Estrutura de Banco de Dados) |

**Objetivo:**

Visando identificar melhorias, otimizar a experiência e antecipar possíveis falhas durante a conversão/atualização de base de dados RM, disponibilizamos uma nova funcionalidade na ferramenta **RM.Atualizador**, onde poderá compartilhar sua estrutura do banco de dados com a TOTVS para análise proativa e automatizada da mesma.

Atenção!

Ressaltamos que o compartilhamento é apenas do Schema do Banco de dados, não sendo enviado à TOTVS dados pessoais, sensíveis ou relativos ao negócio do cliente.

**Processo:**

 No processo de atualização da base de dados, o cliente informará se deseja compartilhar os dados, observando os seguintes critérios:

* Somente é realizada análise da base de Produção.
* Os dados somente são enviados com o consentimento do usuário.

**Dados gerados:**

Após a execução do RM Atualizador, caso o usuário opte por compartilhar as informações, será armazenado em seu ambiente o mesmo arquivo enviado à TOTVS.

O arquivo gerado pode ser encontrado no diretório de instalação do TOTVS RM, na pasta **Arquivos\Atualizador\Diagnostico.** Caso utilize a tag "FileserverPath" no arquivo de configuração do host, o arquivo será gravado conforme caminho indicado neste parâmetro.

O conteúdo do arquivo será composto por uma estrutura similar a esta:

text
