---
content_hash: 6a4b129b3b33035edbc4d501f7dcf898270fb465a52e70d5b9f7a36842d9e873
fetched_at: '2026-06-29T00:08:15.485152+00:00'
page_id: '244741664'
product: rm
source: tdn-rm
title: ER_FRW002-222_MELHORIAS_MASHUPS
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW002-222_MELHORIAS_MASHUPS
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Framework | **Módulo** | Globais |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_FRW\_FRW002 | **IRM1** | PCREQ-10030 |
| **Requisito1** | PCREQ-10086 | **Subtarefa1** | PDR\_FRW\_FRW002-223 |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

Adequar o sistema do TOTVS Mashups para permitir a consulta a sites baseados nas tecnologias AJAX.

A grande maioria dos sites estão sendo migrados para estas tecnologias, que atualmente não são compatíveis com a forma com que o Engine de Mashup faz para executar as consultas, impossibilitando a consulta a sites que utilizam estas tecnologias.

A proposta é utilizar um Engine baseado em um browser com capacidades de execução de scripts e renderização "fora da tela". Para isto foi escolhido a utilização da tecnologia do Chromium, browser baseado no Chrome que possui recursos de renderização que permitam extrair "pedaços" da tela do browser contendo as imagens de CAPTCHAS. Além de permitir a interação com o site para automatizar as ações necessárias para executar as consultas. 

### Definição da Regra de Negócio

### Serviços do Chromium

O Engine do Chromium deverá ser executado como um serviço no Servidor de Mashups ou integrado ao serviço de Proxy do Mashups. Devido a limitações na utilização da biblioteca do Chromium feita em C#, estes serviços somente funcionarão em arquiteturas 64 Bits, em sistemas operacionais superiores ao Windows 2008R2 (para servidores) ou Windows 7.

Será criado um novo aplicativo de serviço do Windows que será utilizado exclusivamente no servidor de Mashups, este serviço irá gerenciar as instâncias "vivas" do browser e será responsável por fazer a liberação dessas instâncias após um período pré-definido de Timeout. Este timeout será renovado a cada interação com a instância do browser. Cada sessão de execução do mashup poderá ter uma instância associada, e será controlado pelo ID de execução do Mashup, obtido na chamada GetService.

O serviço do Mashup irá comunicar com o serviço do Chromium utilizando comunicação via Named Pipes, através de um serviço WCF.

Este mesmo serviço será executado no Proxy do Mashup, portanto o código de manipulação do Chromium será compartilhado entre os dois serviços.

### Atividades do Workflow

Para manipulação do browser, serão criadas novas atividades de Workflow a seguir.

| Nome da Atividade | Funcionalidades |
| --- | --- |
| ChromiumRequestActivity | Esta atividade é responsável por fazer a navegação no Browser, ela tem como parâmetro a URL que o browser deverá navegar.  A sua execução também deverá extrair a versão atual do HTML da browser, para ser utilizado pela atividade de Parser padrão do Mashup, e portanto o parâmetro URL poderá ser deixado em branco com o objetivo de extrair o conteúdo do browser em outros estados do workflow. |
| ExecuteScriptActivity | Esta atividade é resposável por executar um javascript na instância do browser do Chromium. Este javascript poderá devolver valores para a execução do Mashup para serem utilizados posteriormente no fluxo de execução do mashup. |
| ExtractElementActivity | Esta atividade é semelhante a atividade ExecuteScriptActivity, porém permite executar uma lista de scripts de uma vez, permitindo a execução de vários comandos de forma sequencial ou a extração de várias informações ao mesmo tempo. |
| ExtractTableActivity | Esta atividade é semelhante a atividade ExtractElementActivity porém o seu resultado é uma tabela do Mashup, que poderá ser utilizada como parâmetro ou resultado da execução do mashup. |
| ScreenShotActivity | Esta atividade permite a "extração" de fotos do browser inteiro ou de um elemento específico. Ela é utilizada para extrair as imagens dos captchas para serem apresentadas na execução do Mashup.  Além de permitir a extração da imagem, ela deve possuir um recuro para "desenhar" os índices dos elementos da imagem, para permitir que sites que usam o engine do RECAPTCHA possam ser extraídos pelo Mashup.  Desta forma o usuário poderá informar quais são as imagens correspondentes de acordo com o seu número.  Ex: |
| SendClickActivity | Esta atividade permite que seja simulado um clique no Browser. Ela recebe como parâmetro a posição da tela que deverá ser clicada. |

### Opcional

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
