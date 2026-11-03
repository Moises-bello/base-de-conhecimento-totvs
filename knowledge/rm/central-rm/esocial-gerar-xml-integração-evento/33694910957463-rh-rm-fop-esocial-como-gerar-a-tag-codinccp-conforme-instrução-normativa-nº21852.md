---
article_id: 33694910957463
category: eSocial - Gerar XML/ Integração Evento
content_hash: 6424100230fe7e65131e992b176d46303782b18e9ea2faac315235dccad5a592
fetched_at: '2026-06-28T22:47:12.031329+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como gerar a tag <codIncCP> conforme Instrução Normativa
  nº2185/2024 S-1010
type: support-article
updated_at: '2026-01-26T15:55:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33694910957463-RH-RM-FOP-eSocial-Como-gerar-a-tag-codIncCP-conforme-Instru%C3%A7%C3%A3o-Normativa-n%C2%BA2185-2024-S-1010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33694881927063) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como gerar o XML S-1010 garantindo que a tag <codIncCP> seja gerada conforme a Instrução Normativa n° 2185/2024?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir dos patches: 12.1.2402.245, 12.1.2406.185, 12.1.2410.120 e superiores  
  
**Solução**  
Houve uma implementação no produto para garantir que a tag <codIncCP> seja gerada em conformidade com a [Instrução Normativa nº 2185/2024](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2024/abril/publicada-instrucao-normativa-que-atualiza-as-normas-gerais-de-tributacao-previdenciaria).

O sistema foi ajustado para que, na geração do XML S-1010 do evento **com código de cálculo 352**, referente ao **Salário Maternidade Complementar**, a **tag** <codIncCP>seja preenchida conforme a regra abaixo:

* **Valor 15**: Quando houver **incidência de INSS exclusiva do segurado** (ou seja, sem contribuição patronal);
* **Valor 21**: Quando o evento possuir **apenas incidência de INSS** (tanto parte segurado quanto parte patronal).

**Exemplo:**

Cadastro do Evento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33696207603351)

Geração do XML S-1010:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33696207604247)

Comparativo de Incidências de Rubricas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33696211714711)

Saiba mais:

[Código de Cálculo 352 - Salário Maternidade Complementar](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719063)

[Licença Maternidade - Empresa Cidadã - Prorrogação ou Redução](https://tdn.totvs.com/pages/releaseview.action?pageId=769165458)
