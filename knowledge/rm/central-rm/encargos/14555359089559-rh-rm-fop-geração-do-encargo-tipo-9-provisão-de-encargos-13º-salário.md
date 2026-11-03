---
article_id: 14555359089559
category: Encargos
content_hash: 9214487c75cce01cd0e7a9ba0ea924cd4332f72b1b20656ca4381468ef4906df
fetched_at: '2026-06-28T22:46:52.315867+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do encargo  TIPO 9 -  Provisão de encargos 13º salário
type: support-article
updated_at: '2024-10-09T20:11:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14555359089559-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-9-Provis%C3%A3o-de-encargos-13%C2%BA-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:12 min****Dúvida**No módulo folha de pagamento, como gerar o encargo TIPO 9 - Provisão de encargos 13o. salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**Para geração do encargo TIPO 9 - Provisão de encargos 13º salário é necessário anteriormente gerar o histórico de provisão, Para geração do histórico de provisões, siga a orientação da documentação abaixo.

[RH - RM - FOP - Parâmetros da geração do Histórico de provisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413936936215-RH-RM-FOP-Par%C3%A2metros-da-gera%C3%A7%C3%A3o-do-Hist%C3%B3rico-de-provis%C3%A3o)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14554717234711)

Será necessário cadastrar o encargo: Acesse: **Encargo | Cadastros | Encargos** e crie conforme a necessidade da organização informando valor no campo porcentagem, pois para a geração do encargo a fórmula interna do sistema irá considerar (Provisão \* % encargo / 100) + (Provisão \* % Seção / 100) :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14554745965591)

A alíquota de SAT **agora denominada RAT** para funcionários com aposentadoria especial **15, 20, 25 anos** será tratada durante a contabilização para os encargos 6 e 9 porque somente estes encargos são de responsabilidade da empresa.  
Os encargos 2, 3, H e M são Bases de incidências e os encargos 4, 5, 7, 8 são relativos a valores a provisionar de férias e 13º salário e se este tratamento for aplicado a estes encargos o usuário que necessitar contabilizar apenas as bases de incidências ou provisões não conseguirá.

Cadastro do funcionário aba **FGTS/SEFIP:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14554916152087)

No momento da geração do encargo Acesse: **Encargos | Geração de encargos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14554919970967)

**Importante:** Verificar o código ativo associado ao cadastro do encargo, pois no momento da geração do encargo será necessário selecionar o mesmo código ativo. Caso precise de apoio para criar o código ativo para vincular no encargo, utilize a documentação abaixo.

[RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)

Log da geração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14554942811799)  
O percentual da seção da fórmula busca do campo da aposentadoria especial do cadastro da seção

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14554947041815)

Caso, no cadastro do colaborador na aba **FGTS/SEFIP** não for exposto a agente nocivo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14555002946199)

O comportamento do sistema no calculo da geração do encargo.![](https://centraldeatendimento.totvs.com/hc/article_attachments/14555040359959)  
  
Utilização da flag **Aplicar percentual FAP por filial** do cadastro do encargo com a mesma marcada, no momento do calculo o sistema irá considerar (Provisão \* % encargo / 100) + (Provisão \* % Seção / 100) + (Provisão \* % (FAP \* SAT) / 100):![](https://centraldeatendimento.totvs.com/hc/article_attachments/14555122446359)

**Importante:** o **FAP** e o **SAT** são informados na seção centralizadora do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14555243127319)

**FAP** por estabelecimento empresarial está em anexos da seção.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14555246221207)

**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
