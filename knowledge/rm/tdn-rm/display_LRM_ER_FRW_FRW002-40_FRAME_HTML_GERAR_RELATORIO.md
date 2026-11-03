---
content_hash: 7e95c3d62e65bf6075941230192e6a1c9385596cca4a909e661e0cae5a4d9897
fetched_at: '2026-06-29T00:08:15.502790+00:00'
page_id: '244742319'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-40_FRAME_HTML_GERAR_RELATORIO
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW_FRW002-40_FRAME_HTML_GERAR_RELATORIO
version: 110
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Framework | **Módulo** | TOTVS Reports |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

# Objetivo

Implementar as funções na Frame HTML necessárias para a geração de relatórios síncronos. Esta função é necessária para alguns processos do produto onde o usuário deverá aguardar a geração do relatório.

Atualmente só existe o recurso para geração dos relatórios de forma assíncrona, onde o usuário recebe uma notificação no fluig de que o relatório foi gerado.

### Definição da Regra de Negócio

Uma nova função no Controller de relatórios será disponibilizada para esta geração. Os dados do relatório gerado serão retornados pela função.

js1FrontEnd - Generate Reporttruetruejs1RptReportGenerateParametertruetrue

### Formatos Suportados

|  |  |
| --- | --- |
| CSV | Arquivo texto separado por vírgula |
| JPEG | Imagem no formato JPEG |
| HTML | Arquivo Hypertexo |
| XLSX | Planilha do Excel > 2012 |
| MHT | Arquivo de Ajuda em formato HTML |
| PDF | Arquivo PDF |
| RTF | Arquivo de Texto Rico |
| TXT | Arquivo de Texto |
| XLS | Planilha do Excel < 2012 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
