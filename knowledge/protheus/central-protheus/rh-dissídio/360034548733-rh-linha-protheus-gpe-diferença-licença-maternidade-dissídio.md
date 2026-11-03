---
article_id: 360034548733
category: RH - Dissídio
content_hash: 7c39f6b4f3fbe265436462713ff20cc801a910567e3019a55f10752d303fdcdc
fetched_at: '2026-06-28T22:43:43.563689+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Diferença licença maternidade dissídio
type: support-article
updated_at: '2025-08-20T13:04:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034548733-RH-Linha-Protheus-GPE-Diferen%C3%A7a-licen%C3%A7a-maternidade-diss%C3%ADdio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314728886807) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como separar a diferença dos proventos e licença maternidade no cálculo do dissídio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Solução**Normalmente todos os proventos são vinculados através da aba dissídio ao identificador 0341, mas pela necessidade de deduzir o valor da diferença de licença maternidade da guia de INSS é necessário separar esses valores no cálculo do dissídio.  
Para separar é necessário criar uma nova verba para representar o valor de diferença da licença maternidade, a mesma deve ser configurada com o campo Ded. G. INSS (RV\_DEDINSS) igual a SIM. Após, a verba de licença maternidade - identificador 0040 deve ser vinculada a verba criada no passo anterior, através da aba dissídio que está localizada na configuração de verbas.  
  
1. Criando uma nova verba:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044761813)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044761833)  
\* As demais configurações dessa tela são ilustrativas, sendo de responsabilidade do departamento pessoal definir a incidência de cada verba.  
  
2. Vinculo das verbas:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044761853)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044761873)

**Saiba Mais:**  
[Página Centralizadora do Dissídio (GPEM690)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)  
Manual do dissídio: <http://tdn.totvs.com/pages/releaseview.action?pageId=220889925>
