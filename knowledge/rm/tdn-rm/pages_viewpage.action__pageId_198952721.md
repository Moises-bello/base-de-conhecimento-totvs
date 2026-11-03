---
content_hash: 48e4f0725526a75583a968a434d39af6176252e9c96e5900968c58c9e145ae44
fetched_at: '2026-06-29T00:06:03.285391+00:00'
page_id: '198952721'
product: rm
source: tdn-rm
title: Conversão de planilha Excel para planilha RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198952721
version: 11
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Fornecer ao usuário uma ferramenta prática para conversão de Planilhas .Net para Planilhas RM.

# Introdução

---

      Caso o usuário opte por parar de utilizar o Excel no seu ambiente, poderá converter planilhas eletrônicas, criadas através do Microsoft Excel, para o formato das Planilhas RM. Esta ferramenta é unidirecional, ou seja, não possibilita que uma Planilha RM seja convertida para uma Planilha .Net.

# Utilização

---

      Para habilitar a ferramenta de conversão, deve-se desabilitar o uso do Microsoft Excel, conforme descrito .

      Como o processo de conversão é **irreversível**, é de suma importância que seja feito um backup das planilhas que serão convertidas.

      Na visão das planilhas, selecione uma ou mais Planilhas. Net e acesse o menu Processos e opção "Converter planilha Excel para planilha RM". Será exibida uma mensagem solicitando a confirmação ao usuário.

      Caso aconteça algum erro, as informações sobre ele poderão ser recuperadas na aba "Progresso da execução do(s) processo(s)".

* Acesso ao processo de Conversão de Planilha;

* Conclusão da conversão;

# Detalhes Técnicos

---

      O processo de conversão insere automaticamente um registro na tabela GPLAN contendo as informações da planilha original. Estes registros diferem do registro original somente por conter, na coluna CODAPLIC, o caractere "\*", antes do código do sistema. Estes registros não serão listados na visão da Planilha Net e podem ser removidos da tabela sem nenhum prejuízo ao funcionamento do sistema.

Observação

*A partir da versão **12.1.23 não será mais possível o uso da Planilha.Net como RMPart nos Cenários**. Permanecendo a inclusão de [Planilhas RM](http://tdn.totvs.com/x/MceFDg) somente.*

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.5 ou Superiores

false

**Processo:** Conversão de Planilha .Net para Planilha RM

falsefalse

**Status:** Finalizado

false

**Data:** 19/07/2016

false

**Autores:**
