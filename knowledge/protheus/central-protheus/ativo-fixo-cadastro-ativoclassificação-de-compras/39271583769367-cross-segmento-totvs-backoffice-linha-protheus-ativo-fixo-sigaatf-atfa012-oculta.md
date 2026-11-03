---
article_id: 39271583769367
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: efb3506d51727017534f802cd4194e2abe5f3778c29574b14f239779a9d841e5
fetched_at: '2026-06-28T22:41:48.481577+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) -
  ATFA012 Ocultação da opção Salvar e Criar Novo no Cadastro de Ativos
type: support-article
updated_at: '2026-03-30T13:04:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39271583769367-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Ativo-Fixo-SIGAATF-ATFA012-Oculta%C3%A7%C3%A3o-da-op%C3%A7%C3%A3o-Salvar-e-Criar-Novo-no-Cadastro-de-Ativos
---

No cadastro de Ativo (ATFA012) do TOTVS Protheus, para habilitar o botão "Salvar e Criar Novo", é necessário ajustar o parâmetro "Exibe painel de detalhes (F12)" para "Não", pois quando ativado, essa opção é ocultada para manter a integridade e performance da interface. Após essa alteração, o botão para inclusão sequencial de ativos será exibido novamente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39271583761559) Tempo aproximado para leitura:00:10 min  
  
**Dúvida**  
No cadastro do Ativo (ATFA012), a opção de "Salvar e Criar Novo", não esta disponível, como habilitar.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Ativo Fixo (SIGATF) - A partir da release 12.1.2310

**Solução**  
Para exibição botão "Salvar e Criar Novo" é nescessario ajustar a pergunta "Exibe painel de detalhes (F12)" com não pois quando ela estiver com "Sim" habilitada, a ação "Salvar e Incluir Novo" é ocultada automaticamente. Essa medida foi adotada a fim de manter a integridade e a performance da interface.

Caso deseje utilizar a funcionalidade de incluir múltiplos ativos sequencialmente utilizando o botão "Salvar e Criar Novo", siga os passos abaixo para ajustar a parametrização:

1. Acesse a rotina de Cadastro de Ativos (ATFA012).
2. Antes de clicar em "Incluir", pressione a tecla **F12** para abrir os Parâmetros da rotina.
3. Localize o parâmetro **"Exibe painel de detalhes?"**.
4. Altere a configuração deste parâmetro para **"Não"**.
5. Confirme a parametrização e acesse a rotina de Inclusão novamente. O botão de inclusão sequencial voltará a ser exibido.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39271583762583)

**Saiba Mais**  
[Cadastro sequencial de ativos (ATFA012)](https://tdn.totvs.com/pages/viewpage.action?pageId=1010268140)  
[Ativo fixo (ATFA012 - SIGAATF)](https://tdn.totvs.com/pages/viewpage.action?pageId=306851592)
