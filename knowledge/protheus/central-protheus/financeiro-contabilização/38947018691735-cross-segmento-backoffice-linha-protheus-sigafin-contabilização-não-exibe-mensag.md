---
article_id: 38947018691735
category: Financeiro - Contabilização
content_hash: 49ac0e8232f1466a4b602b7d2b50cd97836a25257bc41cbf6bc59cc97d922a75
fetched_at: '2026-06-28T22:38:05.254412+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Contabilização não exibe
  mensagem de erro e campos obrigatórios
type: support-article
updated_at: '2026-03-19T11:35:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38947018691735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Contabiliza%C3%A7%C3%A3o-n%C3%A3o-exibe-mensagem-de-erro-e-campos-obrigat%C3%B3rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38947018680087) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Por que o sistema não apresenta mensagens de aviso ou erro (Help) ao tentar salvar um lote ou realizar a contabilização (online/offline), impedindo o avanço do processo sem exibir a causa?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução:**  
No Protheus, o controle dessa funcionalidade é realizado por meio do parâmetro **MV\_CT105MS**. Quando esse parâmetro está configurado com o valor **"N"**, o sistema deixa de apresentar mensagens de aviso ou erro durante o processo de contabilização (online ou offline) ou ao salvar um lote. Nessa condição, caso exista alguma inconsistência que impeça a continuidade do processo, o fluxo pode parecer interrompido ou sem resposta, justamente porque a mensagem que explicaria o motivo não é exibida ao usuário.

Para ajustar esse comportamento, orientamos verificar a configuração do parâmetro no Configurador:

1. Acesse o módulo **Configurador (SIGACFG)**.
2. Vá em **Ambiente > Cadastros > Parâmetros**.
3. Localize o parâmetro **MV\_CT105MS**.
4. Clique em **Editar**.
5. Altere o conteúdo para **S (Sim)**, habilitando a exibição das mensagens.
6. Confirme a alteração e salve.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38947057636119)

Após a atualização do parâmetro, recomendamos reiniciar a rotina financeira onde o comportamento foi identificado e realizar um novo teste. Com essa configuração habilitada, o sistema voltará a apresentar as mensagens de Help sempre que houver alguma validação que impeça o avanço do processo, facilitando a identificação da causa, mas é importante reforçar que ajustes só serão permitidos quando o parâmetro **MV\_ALTLCTO** estiver com o contéudo = "S" permitindo os ajustes em tela.

**Saiba Mais:**

[**Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA105 - Contabilização Off-Line não valida a linha do lançamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento)
