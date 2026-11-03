---
article_id: 40717152820503
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9e52869f62fbf7c11bdc518f997bb2dd7a8feaa5702766efc928deb1399f3c22
fetched_at: '2026-06-28T22:39:11.256532+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV060 Ao ler o lote
  sempre volta para o campo de produto em branco
type: support-article
updated_at: '2026-05-25T12:57:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40717152820503-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV060-Ao-ler-o-lote-sempre-volta-para-o-campo-de-produto-em-branco
---

O problema ocorre porque o sistema, projetado para coletores de dados com telas pequenas, retorna o cursor ao campo "Produto" apagando seu conteúdo ao invés de avançar para armazém e endereço. O ponto de entrada V160FArm mantém o foco no campo de armazém, preservando o valor do produto, e o parâmetro MV\_CBFCQTD direciona o foco para a quantidade.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40717176359063) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O usuário preenche a nota, seleciona o produto e informa o lote na tela "Produto com rastro", o sistema não avança para as opções de armazém e endereço de destino. Em vez disso, ele retorna o cursor para o campo "Produto", apagando a informação digitada anteriormente e deixando o campo em branco. Como corrigir essa questão?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
A interface pouco amigável ocorre porque as aplicações são feitas para coletores de dados com telas pequenas, geralmente 2 linhas por 40 colunas, o que difere do uso em simuladores como vtdebug e tera term, usados apenas para testes.

O ponto de entrada [V160FArm](https://tdn.totvs.com/pages/releaseview.action?pageId=6091010) mantém o foco no campo de armazém, preservando o valor do campo produto, que é limpo ao receber foco novamente.

Temos também o parâmetro [MV\_CBFCQTD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)que realiza o foco na quantidade.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
