---
article_id: 360042578454
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 5aef3d13b59e431ee4974a39d866d4f6b0e69c08e535ef48ce7760b697ebd515
fetched_at: '2026-06-28T22:39:31.153500+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Valor do imposto não
  é deduzido na aba duplicatas antes de salvar a nota fiscal
type: support-article
updated_at: '2021-07-29T14:16:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042578454-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valor-do-imposto-n%C3%A3o-%C3%A9-deduzido-na-aba-duplicatas-antes-de-salvar-a-nota-fiscal
---

**Dúvida**Ao lançar uma nota via documento de entrada (MATA103) a aba duplicatas não faz o desconto do imposto, sendo necessário confirmar o valor líquido após o salvamento da nota fiscal. O sistema tem tratativas para isso?

**Ambiente**Protheus – Compras – A partir da versão 12.1.17.  
  
**Solução**

O Protheus não tem tratativas para destacar o valor líquido antes de salvar a nota na aba duplicatas, pois esse é um conceito padrão do sistema. Após salvar a nota o sistema faz validações com outros fontes analisando regras como:

- Quem é o responsável pelo recolhimento;

- Devo integrar na rotina do financeiro no meu contas à pagar ou a receber;

- Fator da cumulatividade (ele pode somar outra nota abaixo de dez e atribuir no valor da duplicatas da nota atual, assim que a nota é salva);

- Se o valor do imposto tem dispensa de retenção;

- O tratamento é pela emissão ou na baixa (caso seja na baixa, os títulos dos impostos só serão gerados no financeiro após a baixa do título principal);

Entre outras validações pertinentes aos impostos envolvidos na escrituração da nota.

O sistema no momento da escrituração só está fazendo a inclusão dos dados, assim que a nota é salva o sistema faz a validação com fontes complementares e confirma como a nota deve ser destacada no financeiro.
