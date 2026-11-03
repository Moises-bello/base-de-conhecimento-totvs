---
article_id: 360018569132
category: RH - Rescisão
content_hash: 7ecc77d13056f75be390211f5252cef5dabe649614bed6e3289d1016acb8712d
fetched_at: '2026-06-28T22:43:50.988575+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: MP - GPE - Integrando roteiro de férias pelo cálculo de rescisão, gera incorretamente
  férias indenizadas do período já pago
type: support-article
updated_at: '2024-09-17T14:09:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018569132-MP-GPE-Integrando-roteiro-de-f%C3%A9rias-pelo-c%C3%A1lculo-de-rescis%C3%A3o-gera-incorretamente-f%C3%A9rias-indenizadas-do-per%C3%ADodo-j%C3%A1-pago
---

**Ocorrência**No módulo Gestão de Pessoal, quando integrado roteiro de férias pelo cálculo de rescisão, gera incorretamente férias indenizadas do período já pago.  
   
 **Ambiente**Microsiga Protheus - Gestão de Pessoal - A partir da versão 12  
   
 **Causa**Após integrar as férias através da rotina de rescisão, o cálculo está desprezando os dias pagos e calculando tudo como férias indenizadas.  
  
 **Solução**Efetuado ajuste para que o cálculo subtraia os dias de férias pagos no período, calculando apenas o excedente, quando houver.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize o *backup* prévio;  
2. Aplique o pacote de atualização;  
3. Refaça o teste.  
  
**Saiba Mais**Acesse o *link* a seguir para o pacote de atualização:  **12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=718172>**
