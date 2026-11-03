---
article_id: 28794837623191
category: eSocial - Gerar XML/ Integração Evento
content_hash: a9801bed8cf657afed7ab5f1843c21777df32eaaa5a54b8d58d03ca8fc402c26
fetched_at: '2026-06-28T22:47:13.041257+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Gerar a incidência de INSS exclusivo do segurado
  = 15 no S-1010, conforme Instrução Normativa nº2185/2024 para licença maternidade
type: support-article
updated_at: '2026-05-27T21:16:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28794837623191-RH-RM-FOP-eSocial-Gerar-a-incid%C3%AAncia-de-INSS-exclusivo-do-segurado-15-no-S-1010-conforme-Instru%C3%A7%C3%A3o-Normativa-n%C2%BA2185-2024-para-licen%C3%A7a-maternidade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28794819567127) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como gerar a incidência de INSS exclusivo do segurado = 15 no S-1010, conforme Instrução Normativa nº2185/2024?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da release 12.1.24.  
  
**Solução**

O sistema foi ajustado para que, na geração do XML do evento com código de cálculo **352 - Salário Maternidade Complementar**, a tag <codIncCP> seja preenchida como **15**, quando a incidência de INSS for exclusiva do segurado;

Para isso acesse: **Módulo Folha de Pagamento**| **Administração de pessoal | Eventos** | Acesse o evento de código de cálculo 352 e marque a incidência conforme exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28794837589783)

Para gerar o xml acesse: Módulo Folha de Pagamento | eSocial | Fila de eventos | Gere o gatilho S-1010 do evento anterior e envie para o governo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28794819574039)

Retirando a informação de exclusiva do segurado, o evento é gerado com incidência 21.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28794837594263)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28794819578903)

**Saiba mais**  
Para mais informações acesse:

* [S-1010 - Gerar a tag <codIncCP> conforme Instrução Normativa nº2185/2024](https://tdn.totvs.com/pages/releaseview.action?pageId=887728147)
* [Alterações nas Contribuições Sociais Previdenciárias](https://www.totvs.com/blog/fiscal-clientes/alteracoes-nas-contribuicoes-sociais-previdenciarias/)
