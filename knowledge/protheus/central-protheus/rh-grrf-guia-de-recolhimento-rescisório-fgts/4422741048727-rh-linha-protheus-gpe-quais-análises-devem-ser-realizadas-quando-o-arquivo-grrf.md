---
article_id: 4422741048727
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: 9d784cdb9c4545cb08f2c44975217b02f02e440eaf63a667f55c4812c3bcaac8
fetched_at: '2026-06-28T22:43:32.381964+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Quais análises devem ser realizadas quando o arquivo
  GRRF não é gerado?
type: support-article
updated_at: '2025-06-26T13:32:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422741048727-RH-Linha-Protheus-GPE-Quais-an%C3%A1lises-devem-ser-realizadas-quando-o-arquivo-GRRF-n%C3%A3o-%C3%A9-gerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069325029015) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Quais análises devem ser realizadas quando o arquivo GRRF não é gerado ou é gerado sem as informações do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**

Verifique os itens abaixo:

- No cálculo da rescisão o campo "Resc. Efetiv" deverá estar com "SIM"

- Verifique se as datas de demissão/ homologação/ geração no calculo da rescisão, estão divergentes do que foi informado nos parâmetros para a geração da GRRF

- Verifique se no parâmetro para a geração da GRRF, na pergunta, "Tipo de Rescisão" está conforme a rescisão calculada.

- Verifique se as tabelas S037 e S038 estão preenchidas corretamente.

- Verifique na tabela S043, se no Tipo de Rescisão, o campo FGTS Mês está = "S"

- Verifique na tabela S043, se no Tipo de Rescisão, o campo Cod.Afast.FGTS está preenchido com o código correto para recolhimento através da GRRF.

- Verifique no cadastro do funcionário, aba funcionais, se o campo Categ.SEFIP está preenchido corretamente com um código Sefip válido, exemplo "01-Empregado".

**Saiba mais:**

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
