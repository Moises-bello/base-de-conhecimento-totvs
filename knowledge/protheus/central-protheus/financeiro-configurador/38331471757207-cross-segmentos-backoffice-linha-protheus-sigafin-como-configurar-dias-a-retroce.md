---
article_id: 38331471757207
category: Financeiro - Configurador
content_hash: cca6b580c20648cdfca71e8f642e8aa53d97772387d7880f1f6f1d5c81bd278d
fetched_at: '2026-06-28T22:37:57.588724+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como configurar dias
  a retroceder no módulo financeiro?
type: support-article
updated_at: '2026-02-11T17:37:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38331471757207-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-configurar-dias-a-retroceder-no-m%C3%B3dulo-financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38331496951831) Tempo aproximado para leitura: **00:06 min**  
  
**Dúvida**  
Como permitir que o usuário consiga retroceder a data do sistema para consultas financeiras de períodos anteriores (exemplo: ano passado), superando o limite atual de XXX dias?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38331496952855)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.2210.  
  
**Solução**

O limite de dias para retrocesso de data nas rotinas do Protheus é controlado pelas configurações de privilégios do usuário ou do grupo de usuários no módulo Configurador (SIGACFG). Quando o campo de limite de retrocesso está configurado com um valor baixo (como 366 dias), o sistema impede a digitação ou seleção de datas anteriores a esse intervalo.

Para ajustar, siga os passos abaixo:

* Acesse o módulo **Configurador (SIGACFG)**;
* Vá em **Usuário / Senhas / Usuários**;
* Selecione o usuário desejado e clique em **Alterar**;
* Acesse a aba **Restrições de Acesso** e, em seguida, a sub-aba **Parametrizações.**
* Localize o campo **Dias p/ retroceder** e informe a quantidade necessária (ex.: 600 dias ou conforme a necessidade do cenário);  
  ![retroceder.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/38331496955927)
* Clique em **Confirmar** para salvar a alteração.

É importante considerar também que o usuário pode estar configurado para **herdar validações do grupo de usuários** ao qual pertence. Nesses casos, pode existir uma regra definida no grupo financeiro com valor diferente do configurado diretamente no usuário, prevalecendo sobre o ajuste individual.

Por isso, recomendamos verificar as configurações do grupo vinculado. Se houver restrição ativa, o ajuste pode ser realizado diretamente no grupo ou, se aplicável, pode-se optar por desconsiderar as regras herdadas para esse usuário específico, através do caminho:

* Vá em **Usuário > Senhas > Usuários > Alterar >** **Aba "Usuário"** > **Parâmetro:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38331471737495)

**Saiba Mais**

[TDN - Configurar dias de troca da Data Base do Sistema](https://tdn.totvs.com/display/public/framework/Configurar+dias+de+troca+da+Data+Base+do+Sistema)
