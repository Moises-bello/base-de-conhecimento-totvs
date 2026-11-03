---
article_id: 360060020573
category: RH - Relatórios Folha
content_hash: 9b917813d047cd6297eea8ff7d5bc58cab5c294aa6a442d150c5d4e195506222
fetched_at: '2026-06-28T22:43:17.583405+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Cargos e Salários (GPER340) trazendo
  o salário igual para todos os Funcionários/Funções
type: support-article
updated_at: '2025-08-04T14:36:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060020573-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Cargos-e-Sal%C3%A1rios-GPER340-trazendo-o-sal%C3%A1rio-igual-para-todos-os-Funcion%C3%A1rios-Fun%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25908243131671) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Ao gerar relatório de Cargos e Salários (GPER340), o sistema está trazendo o salário igual para todos os Funcionários/Funções.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Verificado que o salario estava sendo impresso no final do processamento, trazendo assim os dados do salário do ultimo registro. Foi necessário ajustar a rotina para imprimir os dados de cada funcionário juntamente com as informações do salario.

Verificado também que a quebra/totalizador do relatório precisava de ajuste, pois para as ordenações abaixo, o sistema deve quebrar e totalizar por centro de custo.

* CUSTO + MATRICULA
* CUSTO + NOME
* CUSTO + FUNCAO

Aplique o pacote do RH Acumulado conforme *link* abaixo para o problema ser resolvido!

**P12.1.2410:**<https://suporte.totvs.com/portal/p/10098/download?e=1170810>  
**P12.1.2310:** <https://suporte.totvs.com/portal/p/10098/download?e=1123885>  
**P12.1.2210:** <https://suporte.totvs.com/portal/p/10098/download?e=1080347>

**Saiba Mais**:

[RH - Linha Protheus - GPE - Relatório de Cargos e Salários GPER340 em planilha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053099034-MP-GPE-Rela%C3%A7%C3%A3o-de-Cargos-e-Sal%C3%A1rios-GPER340-em-planilha-)

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
