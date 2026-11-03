---
article_id: 360036292274
category: RH - Contrato Intermitente
content_hash: 67ceebf828f14ea6c96a0433cde6b51ffe75e528f8911f533408f33cb433a833
fetched_at: '2026-06-28T22:43:40.124811+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Pagamento do funcionário com contrato intermitente
  por convocação
type: support-article
updated_at: '2025-04-15T17:27:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036292274-RH-Linha-Protheus-GPE-Pagamento-do-funcion%C3%A1rio-com-contrato-intermitente-por-convoca%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25966041266839)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar o pagamento de funcionário em contrato intermitente por convocação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que seja realizado o pagamento do contrato intermitente por convocação, realize a configuração conforme exemplo abaixo:  
  
1. Cadastre períodos para os processos de acordo com a convocação com números de pagamento diferentes. Para cada convocação, deverá ser cadastrado um período com os roteiros FOL e FER:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097372013)  
  
2. Cadastre o funcionário com contrato **intermitente**, Tipo de pagamento **semanal** e categoria **horista:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047433274)  
  
3. Execute o lançamento das convocações:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047435574)  
  
4. Execute a integração dos roteiros, caso exista roteiros que devem ser integrados e realize o cálculo da folha para o número de pagamento 01 (referente à primeira convocação do período):  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048322913)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047436354)  
  
5. Será necessário realizar o fechamento do período para que seja calculado o pagamento 02. Caso não seja executado o fechamento, o sistema não considerará o IR das semanas anteriores quando as convocações ocorrerem em uma mesma competência  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048323413)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047436694)  
  
6. Integre os roteiros abertos, caso existam e calcule a folha do pagamento do número de pagamento 02. O mesmo processo deve ser realizado caso exista outras convocações  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047437074)

**OBS.:** Os impostos serão apurados a cada convocação, considerando sempre os valores das semanas interiores para a correta apuração (INSS, IRRF, FGTS).  
  
**Saiba Mais**  
[Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)
