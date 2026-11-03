---
article_id: 360019896112
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 43f4ab67651c6cb6dfa78921392bf4978d94e7983ff03c20425015d09a26098c
fetched_at: '2026-06-28T22:39:07.971099+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: ' Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como preencher automaticamente
  o campo B5_CEME com a descrição informada no campo B1_DESC?'
type: support-article
updated_at: '2021-12-09T16:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019896112--Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-preencher-automaticamente-o-campo-B5-CEME-com-a-descri%C3%A7%C3%A3o-informada-no-campo-B1-DESC
---

**Dúvida**Como preencher automaticamente o campo B5\_CEME com a descrição informada no campo B1\_DESC

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  Estoque/Custos - Todas as versões.

**Solução**

Para solucionar essa dúvida será necessário criar um novo gatilho para o campo "Descrição" (B1\_DESC).  
  
Realize os seguintes passos para criação do gatilho:  
  
1. Acesse o módulo configurador;  
2. Acesse o caminho: Base de Dados - Dicionário - Gatilhos;  
3. Inclua um novo gatilho para o campo **B1\_DESC**;  
4. No campo Cnt. Domínio informe **B1\_DESC**;  
5. No campo Tipo informe **Primário**;  
6. No campo Regra informe **Mta010Ceme()**;  
7. No campo Posiciona selecione a opção **2 - Não.  
  
![Gatilho_b1_Desc.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360015829272/Gatilho_b1_Desc.PNG)**

**Observação:**

O gatilho irá funcionar com o parâmetro **MV\_CADPROD** dessa forma configurado **"|SBZ|SB5|SGI|"**.

É necessário apertar o botão TAB do teclado para que seja atualizada a informação do campo B5\_CEME, conforme imagem abaixo:

![20211209_134212.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4415448987159/20211209_134212.gif)

**Saiba Mais:**

*[MV\_CADPROD - Parâmetro para informar quais cadastros complementares devem ser apresentados no cadastro de produto](https://tdn.totvs.com/pages/releaseview.action?pageId=317003310)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
