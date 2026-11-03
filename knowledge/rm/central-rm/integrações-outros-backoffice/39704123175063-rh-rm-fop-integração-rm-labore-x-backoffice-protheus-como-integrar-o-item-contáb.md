---
article_id: 39704123175063
category: Integrações Outros BackOffice
content_hash: 5bf9501850c36fd64356b2704750cff645fa6723109e08b543ff67ee749babc7
fetched_at: '2026-06-28T22:46:42.074636+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RH - RM - FOP - Integração RM Labore x BackOffice Protheus - Como integrar
  o item contábil e classe de valor para os lançamentos?
type: support-article
updated_at: '2026-04-13T12:18:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39704123175063-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Como-integrar-o-item-cont%C3%A1bil-e-classe-de-valor-para-os-lan%C3%A7amentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39704154986007) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como integrar a classe de valor para utilizar nos lançamentos que serão integrados?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para disponibilizar a Classe de Valor do Protheus no RM, é necessário realizar a carga inicial do adapter correspondente e validar a integração.

1. Acesse o módulo configurador do Protheus (**SIGACFG**) e navegue até: **Ambiente > Schedule > Sinc. Carga Inicial EAI.**  
   **![](https://centraldeatendimento.totvs.com/hc/article_attachments/39704154986519)**
2. Selecione o adapter **CLASSVALUE** e inicie a sincronização, que será responsável por enviar todas as Classes de Valor do Protheus para o RM.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39704154986647)
3. Após a execução, valide se os registros foram integrados corretamente no RM por meio da consulta abaixo no banco de dados:

   ```
   SELECT * FROM SCLASSEVALORPROTHEUS
   ```

   Nesta tabela será possível verificar a coligada e as Classes de Valor integradas.
4. Com a carga realizada, acesse no RM o caminho:  
   **Folha de Pagamento > Encargos > Cadastros > Cadastros Contábeis > Agrupamento de Contas**.  
   Ao editar um agrupamento, o campo **Classe de Valor** estará disponível para seleção conforme as informações integradas.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39704154987031)
