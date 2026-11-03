---
article_id: 19222743777943
category: REQUISIÇÕES
content_hash: ad012bc19c6d06a5aff6615e1c3aba8c8119d44e963f07e3b729573bb3d114ef
fetched_at: '2026-06-28T22:44:37.594215+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como emitir um Relatório para acompanhamento
  das solicitações feitas no App Meu RH
type: support-article
updated_at: '2025-09-16T17:51:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19222743777943-RH-Linha-Protheus-Meu-RH-Como-emitir-um-Relat%C3%B3rio-para-acompanhamento-das-solicita%C3%A7%C3%B5es-feitas-no-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19222756789143) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como emitir um Relatório para acompanhamento das solicitações feitas no App Meu RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Não temos um relatório, que seja específico para acompanhamento ou listagem, das solicitações feitas pelo Portal GCH, junto com o *status* da requisição.  
  
No Protheus, há uma rotina em todos os módulos que é a **Consulta Genérica**, ou então a **Consulta Genérica Relacional**, que é possível realizar a extração de um relatório das tabelas envolvidas com este processo.  
  
No caso das solicitações realizadas pelo Meu RH, o Protheus possui **três tabelas principais**:  
- **RH3**: Solicitações ao RH, feitas pelo App Meu RH;  
- **RH4**: Tabela de alteração cadastral, mediante solicitações feitas;  
- **RGK**: Histórico de Movimentação dessas solicitações realizadas.  
  
Inicialmente, é necessário **acessar o SIGACFG - Configurador**, e na rotina **Ambiente > Cadastros > Menus**, inserir as tabelas relacionadas na rotina **Consulta Genérica, no menu do módulo 18 - SIGATCF**, conforme exemplo:  
  
1 - abrir o menu do SIGATCF e em Adicionar, levar o menu para o quadrante direito:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222727314967)  
  
2 - clicar na rotina Genéricos e em Detalhes:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222735265175)  
  
3 - selecionar as três tabelas citadas e salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222749393943)  
  
4 - salvar o menu com o nome SIGATCF e, reiniciar o Protheus.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222743680791)  
  
5 - Confirmar a geração do Menu  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222735273751)  
  
Assim, logar novamente no Protheus, acessar a **rotina de Consulta Genérica**, selecionando a tabela RH3:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222749400855)  
  
Por fim, basta selecionar a tabela correspondente e, gerar o relatório, conforme necessidade.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222727328535)  
  
Poderá então, ser gerado em planilha, com ou sem algum filtro.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222735283095)  
  
O mesmo procedimento, será para a rotina de **Consulta Genérica Relacional**, com a diferença que poderá utilizar uma relação de duas ou mais tabelas, na extração relatório.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222749422999)  
  
Selecionando a tabela principal:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222743692695)  
  
Incluindo relacionamento com outras tabelas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222720309015)  
  
**Exemplo com a RH4 e SRA:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222756815127)  
  
Selecionar os campos para a **extração do relatório:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222743698711)  
  
Selecionar os campos pertinentes, sendo possível **montar a ordenação**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222735298455)  
  
Resultado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19222749441815)  
  
**Artigos sobre:**  
**- Consulta Genérica, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052080693)**  
**- Consulta Genérica Relacional, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000070561)  
  
Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
