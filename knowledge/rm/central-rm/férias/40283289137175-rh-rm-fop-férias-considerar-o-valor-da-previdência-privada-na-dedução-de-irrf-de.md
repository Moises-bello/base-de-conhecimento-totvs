---
article_id: 40283289137175
category: Férias
content_hash: bf7e798d3857256eb837bd4ff51dce30c223cdac80cb860c74b5c06eac7cbed9
fetched_at: '2026-06-28T22:46:56.114449+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Considerar o valor da Previdência Privada na Dedução
  de IRRF de Férias'
type: support-article
updated_at: '2026-05-07T14:38:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40283289137175-RH-RM-FOP-F%C3%A9rias-Considerar-o-valor-da-Previd%C3%AAncia-Privada-na-Dedu%C3%A7%C3%A3o-de-IRRF-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40283305492247) Tempo aproximado para leitura: **00:02:10 min**  
  
**Dúvida**  
Como considerar o valor da Previdência Privada na Dedução de IRRF Férias?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para que o valor da previdência privada seja considerado na dedução de IRRF de férias, é  preciso configurar o evento de Previdência Privada. O evento deve ser cadastrado em **Administração de Pessoal | Evento**s, e na configuração da verba informe o Código de Cálculo 420 no campo **Código de Cálculo**,e o tipo do evento Desconto/Valor.

Em caso de dúvidas no cadastro de eventos, verifique a documentação: [RH - RM - FOP - Cadastro de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815-RH-RM-FOP-Cadastro-de-Eventos)

**Atenção:**

* O valor a ser deduzido é limitado a 12% da base de IRRF. Caso o valor do evento com código de cálculo 420 seja menor que 12% da base de IRRF  Férias, será deduzido o valor total do evento, caso contrário , será deduzido 12% do valor da base de IRRF Férias;
* O parâmetro "Dedutível de IRRF" não deve estar marcado, pois o próprio Código de Cálculo já trata a dedução.

**Exemplos do cálculo:**

**Evento CC420 com valor inferior a 12% da base de IRRF.**

**Base de IRRF:**

Proventos = 7.273,75

Descontos = 0,00

Valor Dedutível = 0,00

Previdência Privada Total = 750,00

12% da Base Líquida de IRRF: 7.273,75 \* 12% = 872,85

Previdência Privada a Deduzir = 750,00

Base Líquida = 6.523,75

**Evento CC420 com valor superior a 12% da base de IRRF.**

**Base de IRRF:**

Proventos = 7.273,75

Descontos = 0,00

Valor Dedutível = 0,00

Previdência Privada Total = 950,00

12% da Base Líquida de IRRF: 7.273,75 \* 12% = 872,85

Previdência Privada a Deduzir = 872,85

Base Líquida = 6.400,90

**SAIBA MAIS:**

[Código de cálculo 420 - Previdência Privada Dedutível de IRRF Férias](https://tdn.totvs.com.br/pages/releaseview.action?pageId=518477913)

[RH - RM - FOP - Novo Cálculo IRRF - LEI 15.270](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37093881771159-RH-RM-FOP-Novo-C%C3%A1lculo-IRRF-LEI-15-270)
