---
article_id: 360039956213
category: Call Center - Dúvidas Gerais
content_hash: c1ffc02b2eb025faec3088c22720451fe859a2870e8e090caabf91ba5ea93ef9
fetched_at: '2026-06-28T22:41:26.675097+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - HELP TK010VALOK
type: support-article
updated_at: '2025-10-14T11:30:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039956213-Cross-Segmentos-Backoffice-Protheus-SIGATMK-HELP-TK010VALOK
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35616006300439) Tempo aproximado para leitura: **00:02:00 min******

**Dúvida**

O que fazer quando é exibida a mensagem de help "**TK010VALOK**" ao salvar o **Atendimento**?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões

**Solução**

O help **TK010VALOK** é apresentado quando há **inconsistência entre o valor total do atendimento e o valor total das parcelas** geradas pela condição de pagamento.

Essa divergência pode ocorrer por diferentes motivos, tais como:

* **Diferença de arredondamento** entre o total do atendimento e o somatório das parcelas;
* **Soma dos valores totais e percentuais das parcelas inferior ou superior a 100%** na condição do tipo 9.  
  Nessa condição, o sistema permite que o usuário crie manualmente as parcelas, não aplicando nenhuma regra automática de rateio. Entretanto, exige que o somatório manual das parcelas feche exatamente no valor total do atendimento.  
  Se houver qualquer diferença, o help **TK010VALOK** será exibido;
* **Interferência de customizações**, como o ponto de entrada **TMKVPA**, que substitui a lógica padrão de geração de parcelas.

---

### Para solução, é orientado que:

1. **Verifique a condição de pagamento utilizada no atendimento.**  
   Se for do tipo 9, confirme se a soma das parcelas é igual ao valor total do atendimento, incluindo os decimais.
2. **Verifique se os seguintes parâmetros estão interferindo no valor total:**

   * **MV\_PVRECAL** – Indica se o recálculo da tabela de preço no pedido está desabilitado;
   * **MV\_ARREFAT** – Define se o sistema deve arredondar o valor total dos pedidos.
3. **Caso exista o uso de ponto de entrada (como o TMKVPA),** realize um teste em ambiente de homologação desativando-o, a fim de validar o comportamento padrão do sistema.

Saiba Mais:

* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Condição de Pagamento Tipo 9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016176512-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-9)
* [Ponto de Entrada TMKVPA](https://tdn.totvs.com/x/0JJn)
