---
article_id: 360019903692
category: Configurador
content_hash: a8a58623a21dda5fd79743310c6a78d0d8fde276b6d768a13e4a02a7f6e3944e
fetched_at: '2026-06-28T22:42:18.877802+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Como criar índices no Protheus
type: support-article
updated_at: '2024-05-08T11:30:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019903692-Framework-Linha-Protheus-Como-criar-%C3%ADndices-no-Protheus
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23336863930263)*** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**  
Como criar índices no **Protheus**?  
  
**Ambiente**Framework - Framework (Linha Protheus) - Configurador - A partir da versão 11.80.   
  
**Solução**1. Entre no Módulo **Configurador**, esta opção é exclusiva para administradores do Sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893491)

2. Entre em **Base de Dados** > **Dicionário** > **Base de Dados** > clique no lado esquerdo do menu **Dicionário de Dados.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845212)

3. Pesquise pela tabela onde quer adicionar a pesquisa, clique sobre ela e clique em **Editar.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893551)

4. Clique em **Índices** no menu, e clique em **Incluir** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845532)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893571)

5. Clique no campo **Chave**, clique em **Ações Relacionadas** e clique em **Campos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893771)

6. Geralmente as pesquisas iniciam pela **Filial**, então selecione o campo **Filial**, depois selecione o(s) próximo(s) campo(s) que quer adicionar, clicando novamente em **Ações Relacionadas** > **Campos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015845612)

7. Após selecionar os campos, marque a caixinha **Mostra Pesq**;  
8. Selecione um apelido, **Nickname** para a pesquisa;  
9. Clique em **Confirmar**, depois em **Confirmar** novamente;  
10. Clique em **Atualizar** **Base de Dados**;  
11. Vá avançando até **Finalizar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015893911)

**Importante**O índice apenas irá constar efetivamente na estrutura da tabela no banco de dados, após a chamada da tabela por algum processo/rotina.
