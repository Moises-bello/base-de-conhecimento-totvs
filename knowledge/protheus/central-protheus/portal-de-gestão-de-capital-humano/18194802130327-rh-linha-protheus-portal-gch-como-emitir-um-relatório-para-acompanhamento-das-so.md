---
article_id: 18194802130327
category: Portal de Gestão de Capital Humano
content_hash: 66173afe95793db859a595211fd25b0e08a7cda588c7161941b571f17a930dd2
fetched_at: '2026-06-28T22:42:58.921622+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - Portal GCH - Como emitir um Relatório para acompanhamento
  das solicitações feitas no Portal GCH
type: support-article
updated_at: '2023-10-13T10:36:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18194802130327-RH-Linha-Protheus-Portal-GCH-Como-emitir-um-Relat%C3%B3rio-para-acompanhamento-das-solicita%C3%A7%C3%B5es-feitas-no-Portal-GCH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18194772638743) Tempo aproximado para leitura: **00:07:00 min** **Dúvida**Como emitir um Relatório para acompanhamento das solicitações feitas no Portal GCH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - PORTAL GCH – Todas as versões  
  
**Solução**Não temos um relatório, que seja específico para acompanhamento ou listagem, das solicitações feitas pelo Portal GCH, junto com o *status* da requisição.  
  
No Protheus, há uma rotina em todos os módulos que é a **Consulta Genérica**, ou então a **Consulta Genérica Relacional**, que é possível realizar a extração de um relatório das tabelas envolvidas com este processo.  
  
No caso das solicitações realizadas pelo **Portal GCH**, o Protheus possui **três tabelas principais**:  
- **RH3**: Solicitações ao RH, feitas pelo Portal GCH ou App Meu RH;  
- **RH4**: Tabela de alteração cadastral, mediante solicitações feitas;  
- **RGK**: Histórico de Movimentação dessas solicitações realizadas.  
  
Inicialmente, é necessário **acessar o SIGACFG - Configurador**, e na rotina **Ambiente > Cadastros > Menus**, inserir as tabelas relacionadas na rotina **Consulta Genérica, no menu do módulo 18 - SIGATCF**, conforme exemplo:  
  
1 - abrir o menu do SIGATCF e em Adicionar, levar o menu para o quadrante direito:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194041191447)  
  
2 - clicar na rotina Genéricos e em Detalhes:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194082075031)  
  
3 - selecionar as três tabelas citadas e salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194134023575)  
  
4 - salvar o menu com o nome SIGATCF e, reiniciar o Protheus.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194189597591)  
  
5 - Confirmar a geração do Menu  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194191177623)  
  
Assim, logar novamente no Protheus e, acessar a **rotina de Consulta Genérica**, selecionando a tabela RH3:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194224299671)  
  
Por fim, basta selecionar a tabela correspondente e, gerar o relatório, conforme necessidade.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194241553431)  
  
Poderá então, ser gerado em planilha, com ou sem algum filtro.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194331777431)  
  
O mesmo procedimento, será para a rotina de **Consulta Genérica Relacional**, com a diferença que poderá utilizar uma relação de duas ou mais tabelas, na extração relatório.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194388777239)  
  
Selecionando a tabela principal:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194409236887)  
  
Incluindo relacionamento com outras tabelas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194431525143)  
  
**Exemplo com a RH4 e SRA:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194451960087)  
  
Selecionar os campos para a **extração do relatório:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194508862871)  
  
Selecionar os campos pertinentes, sendo possível **montar a ordenação**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194534931351)  
  
Resultado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18194568592023)  
  
**Artigos sobre:**  
**- Consulta Genérica, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052080693)**  
**- Consulta Genérica Relacional, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000070561)  
  
Saiba Mais  
[Artigos Sobre Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)**
