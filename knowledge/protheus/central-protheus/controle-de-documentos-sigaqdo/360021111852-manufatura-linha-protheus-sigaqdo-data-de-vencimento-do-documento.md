---
article_id: 360021111852
category: Controle de Documentos (SIGAQDO)
content_hash: 93e389bd4e8812b75e9fe96d63c6904edcf07798943090e03db43754dab5e81d
fetched_at: '2026-06-28T22:42:28.985797+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Data de vencimento do documento
type: support-article
updated_at: '2025-03-06T12:06:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021111852-Manufatura-Linha-Protheus-SIGAQDO-Data-de-vencimento-do-documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30445867251351)**Tempo aproximado para leitura: **00:02:15 min** **Dúvida**O que ocorre quando um documento atinge a **data de vencimento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Quando um documento atinge a **data de vencimento**, o mesmo fica bloqueado até que o responsável revise o documento ou faça o cancelamento do mesmo.  
  
Os avisos de documentos vencidos/a vencer são gerados com base no parâmetro **MV\_QDIALIM - Define a quantidade de dias limite para avisar que a validade do documento está terminando** que indica a quantidade de dias necessária para aviso do prazo limite de vencimento de um determinado documento.  
  
A partir da configuração do parâmetro **MV\_QDREVAL - Define se a rotina de revalidação é utilizada** é definido se será habilitado o processo de revalidação para documentos vencidos.   
  
**Exemplo**Quando um documento atinge a data de vencimento, o responsável pela pendência faz uma avaliação e decide por sua revalidação ou geração de uma nova revisão. Na tela de manutenção de documentos, é apresentado o aviso de documento vencido/a vencer. Deve dar um duplo clique sobre o item para responder sobre a revalidação do documento vencido/a vencer.  
  
Caso não queira revalidar o documento, deve clicar no botão **Cancelar**. O Sistema pergunta sobre a geração da revisão do documento, que pode ser confirmada ou cancelada.  
Caso queira revalidar o documento, deve clicar no botão **OK**. O Sistema apresenta a janela para a informação dos dados da revalidação. O processo de revalidação também pode ser executado na rotina de **Cadastro de Documentos**, por meio da opção **Gerar Revisão**.  
  
Caso o responsável pela pendência esteja ausente temporariamente, o Sistema transfere o aviso de documento vencido/a vencer para o responsável substituto. O Sistema verifica se o responsável substituto possui permissão para gerar revisões. Caso não possua, somente é possível efetuar a revalidação do documento.  
  
Seguem os parâmetros disponíveis para este processo:

|  |  |
| --- | --- |
| **MV\_QDIALIM** | **Define a quantidade de dias limite para avisar que a validade do documento está terminando.** |
| **MV\_QDIATR** | **Define a quantidade de dias que uma revisão obsoleta permanece ativa em conjunto com a revisão atual.** |
| **MV\_QDREVAL** | **Define se a rotina de revalidação é utilizada.** |
| **MV\_QDXAVLI** | **Define se haverá a verificação por data no envio de e-mail do Aviso de Vencimento, sendo: 1-Sim e 2-Não.** |

**Observação**  
No artigo a seguir encontra-se demais informações sobre a Revalidação de Documentos [Manufatura - Linha Protheus - SIGAQDO - Revalidação de Documentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9560690789527-Manufatura-Linha-Protheus-SIGAQDO-Revalida%C3%A7%C3%A3o-de-Documentos)
