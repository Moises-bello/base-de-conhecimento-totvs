---
article_id: 38215137538327
category: Financeiro - Cadastros
content_hash: e4d627f6d7e3a96b5a4b2c1f6e8c852e1fbcb21f3b64c6df49fd9ff6c5384264
fetched_at: '2026-06-28T22:37:53.169557+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como desabilitar pop-up
  de cadastros e conversão de moedas.
type: support-article
updated_at: '2026-02-06T16:59:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38215137538327-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-desabilitar-pop-up-de-cadastros-e-convers%C3%A3o-de-moedas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38215137523351) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como desabilitar a exibição do pop-up de cadastros e conversão de moedas da rotina MATA090?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38220100921367)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução:**

Por padrão, existe a possibilidade de impedir que esta janela seja exibida para determinados usuários. O bloqueio da exibição desta janela é realizado individualmente por perfil de usuário restringindo o acesso ao processo correspondente no módulo Configurador.

##### **Passo a Passo:**

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Usuário -> Senhas -> Usuários**;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38215137524119)
3. Selecione o usuário desejado e clique em **Alterar**;
4. Acesse a aba **Restrições de Acesso**;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38215137527319)
5. Na guia **Acessos**, localize o **Processo 49** (referente ao pop-up de conversão de moedas);
6. Desmarque a opção para desativar o acesso;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38215137527703)
7. Clique em **Confirmar** para salvar as alterações.

Desta forma, o pop-up deixará de ser exibido exclusivamente para o usuário configurado.
