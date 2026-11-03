---
article_id: 40299118109335
category: TAF - eSocial - Relatório
content_hash: 3a3593315973db9321e59114cd7c03d900e80e9ff9ca42c8b387605fc308097e
fetched_at: '2026-06-28T22:45:19.866274+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF - Relatório DIRF - Como validar a divergência
  do valor de IRRF Retido – Mensal / Férias
type: support-article
updated_at: '2026-05-07T16:48:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40299118109335-RH-Linha-Protheus-eSocial-TAF-Relat%C3%B3rio-DIRF-Como-validar-a-diverg%C3%AAncia-do-valor-de-IRRF-Retido-Mensal-F%C3%A9rias
---

**Dúvida**  
Como validar a divergência da coluna IR retido?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório DIRF - Todas as versões  
  
  
**Solução**  
  
1. Gerar o relatório somente como divergente.

Como gerar o Relatório DIRF Como somente divergente?

[RH (Linha Protheus) - eSocial - TAF - Relatório - Como gerar o Relatório DIRF como somente divergente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38893239676311-RH-Linha-Protheus-eSocial-TAF-Relat%C3%B3rio-Como-gerar-o-Relat%C3%B3rio-DIRF-como-somente-divergente)

2. Localize um registro com divergência, clique em detalhes.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40299132922135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40299132921623)

3. Valor divergente TAF, valide as incidências de rubrica (S-1010) informadas para esse registros.

**Conforme print abaixo, para o valor de IR Retido mensal / férias as incidências são:**

31- Remuneração mensal

32- 13º salário

33- Férias

34- PLR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40299928942487)

Saiba mais :<https://tdn.totvs.com/display/public/TAF/Painel+do+evento+S-5002+Imposto+de+Renda+Retido+na+Fonte+por+Trabalhador>

4. Para cliente Protheus é possível verificar as incidências gerando o relatório S-1200/S-2299 no GPE:

[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE)

[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299?source=search)

* Valide as informações da incidência 31, 32, 33 e 34.
* Valide o Tipo da verba esteja igual a [2,4] subtrair os valores ou [1,3] Somam os valores

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40299607675287)

5. Caso entenda que as verbas estão corretas no relatório do GPE e mesmo assim os valores não batem no relatório DIRF do TAF, valide o histórico de rubricas no TAF para identificar se o S-1200 pegou alguma alteração anterior da rubrica atual:  
[RH - Linha Protheus - TAF - eSocial - Eventos de tabelas - Como validar o cadastro de um evento de rubrica no TAF (S-1010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25509916713495-RH-Linha-Protheus-TAF-eSocial-Eventos-de-tabelas-Como-validar-o-cadastro-de-um-evento-de-rubrica-no-TAF-S-1010)

**SAIBA MAIS:**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:

[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
