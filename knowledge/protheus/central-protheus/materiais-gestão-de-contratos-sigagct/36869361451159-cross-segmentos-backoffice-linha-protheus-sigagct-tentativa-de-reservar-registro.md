---
article_id: 36869361451159
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: fcb718730f6d5ffd0c69c7284ef006c8df8e7c738caf8deae20fc18ebd4eaae4
fetched_at: '2026-06-28T22:37:20.215140+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAGCT - Tentativa de reservar
  registro no Alias em EOF Stack de chamadas em MSRLOCK.eof
type: support-article
updated_at: '2025-12-08T20:41:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36869361451159-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAGCT-Tentativa-de-reservar-registro-no-Alias-em-EOF-Stack-de-chamadas-em-MSRLOCK-eof
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36869361435287) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**

Ao realizar um processo no Gestão de Contratos ocorre a mensagem:

"Tentativa de reservar registro no Alias "XXX" em EOF Stack de chamadas em MSROCK.eof .Tenta novamente? Essa mensagem será fechada em 5 segundos"

**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Gestão de Contratos – A partir da versão 12

**Causa**

A mensagem referente a EOF Stack em MSRLOCK indica que o registro em questão está reservado por outro processo.

Esta mensagem pode acontecer em duas situações:

1 -  o uso do registro por outro usuário;

2 - uma customização que iniciou o tratamento que provocou "unlock" travamento do registro.

**Solução:**

Nestes casos pode-se realizar os seguintes procedimentos:

**1º** - Reiniciar o servidor (parando os serviços do DBAccess, Banco de dados e demais serviços do Protheus) e realizar novos testes.

O reinício dos serviço também do Banco de Dados, é devido, pois já foram verificadas situações de registros presos somente na camada do Banco de Dados, e assim reiniciando este serviço do BD neste caso a questão pode ser solucionada.

Se erro persistir, seguir o segundo procedimento:

**2º** - Verificar se o arquivo **MSRLOCK.EOF** gravado na pasta **system, se** existe alguma customização no sistema que envolva o ALIAS da tabela apresentado na mensagem, caso exista, efetue um teste com a customização desativada, você pode identificar se tem uma customização no processamento, se existir uma linha iniciando com **U\_** na instrução do arquivo, então refazer o teste novamente de processamento ([Como desativar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus)).

***Saiba Mais:***

[FAT0240 EOF Stack de chamadas em MSRLOCK.eof Controle de transaçoes Habilitado](http://tdn.totvs.com/pages/releaseview.action?pageId=235575485)

[Controle de Transação - MV\_TTS](http://tdn.totvs.com/pages/releaseview.action?pageId=6814812)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
