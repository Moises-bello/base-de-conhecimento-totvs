---
article_id: 37679092379415
category: Financeiro
content_hash: 1f7fb032f23a8daf104cc9bcd88f6160e4010c29bfd7f7da5609b3ab35dc9fda
fetched_at: '2026-06-28T22:38:00.784616+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Como desativar as customizações
  pelo catálogo de personalizações
type: support-article
updated_at: '2026-01-14T21:02:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37679092379415-Cross-Segmento-Backoffice-Linha-Protheus-Como-desativar-as-customiza%C3%A7%C3%B5es-pelo-cat%C3%A1logo-de-personaliza%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37679092355991) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como desativar as customizações pelo catálogo de personalizações?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões.  
  
**Solução**  
A rotina **Catálogo de Personalização** permite desabilitar, por meio do **Configurador**, customizações e pontos de entrada que estejam compilados no **RPO**, sem a necessidade de recompilação ou remoção do código.

A seguir, descreve-se o procedimento para desativação de uma customização:

1. Acesse o menu:  
   **Configurador → Ambiente → Cadastros → Catálogo de Personalização**.
2. Localize a função de usuário desejada. No exemplo apresentado, a função **MSE2530** encontra-se compilada no **RPO**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37679092358167)
3. Selecione a função e clique na opção **Alterar**.
4. Na tela de edição, no campo **Situação**, selecione a opção **2 – Desabilitado**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37679092358807)
5. Clique em **Confirmar** para salvar a alteração. A partir desse momento, a customização estará **desativada no ambiente**.
6. Ao tentar executar a customização desabilitada, o sistema exibirá a mensagem informando que a **“Função de usuário não está compilada no repositório”**, indicando que a execução foi bloqueada com sucesso.

**Saiba mais**

Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como testar sem customizações do RpoCustom
