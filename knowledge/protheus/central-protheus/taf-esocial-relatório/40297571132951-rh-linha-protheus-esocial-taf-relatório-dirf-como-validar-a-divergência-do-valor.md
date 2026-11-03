---
article_id: 40297571132951
category: TAF - eSocial - Relatório
content_hash: 7024d5ad2f40d1a3efea05c60b2e99e8ea933cb07feafc3500fe49267f37c5d6
fetched_at: '2026-06-28T22:45:19.891758+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF - Relatório DIRF - Como validar a divergência
  do valor Previdência Oficial
type: support-article
updated_at: '2026-05-07T14:56:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40297571132951-RH-Linha-Protheus-eSocial-TAF-Relat%C3%B3rio-DIRF-Como-validar-a-diverg%C3%AAncia-do-valor-Previd%C3%AAncia-Oficial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40297571105431) Tempo aproximado para leitura: **01:30:00 min**  
  
**Dúvida**  
Como validar a divergência da coluna Previdência Oficial   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório DIRF - Todas as versões

**Solução**  
  
**1.** Como gerar o Relatório DIRF 'Como somente divergente'?

[RH (Linha Protheus) - eSocial - TAF - Relatório - Como gerar o Relatório DIRF como somente divergente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38893239676311-RH-Linha-Protheus-eSocial-TAF-Relat%C3%B3rio-Como-gerar-o-Relat%C3%B3rio-DIRF-como-somente-divergente)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40299266878871)

**2.** Validação Incidência de Rubrica S-1010

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40299266888087)

**Saiba mais:** <https://tdn.totvs.com/display/public/TAF/Painel+do+evento+S-5002+Imposto+de+Renda+Retido+na+Fonte+por+Trabalhador>

**3**. Gere o relatório do S-1200/S-2299 do GPE referente ao funcionário para saber: o porque o relatório está voltando valor a mais do que deveria ou a menos do que deveria ou valor negativo.

[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE?source=search)

[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299)

**Atenção:**

* Valide as informações da incidência de IRRF 41 e 43
* Valide o Tipo da verba esteja igual a [2,4] subtrair os valores ou [1,3] Somam os valores

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40299266889623)

**4.** Caso entenda que as verbas estão corretas no relatório do GPE e mesmo assim os valores não batem no relatório DIRF do TAF, valide o histórico de rubricas no TAF para identificar se o S-1200 pegou alguma alteração anterior da rubrica atual:

[RH - Linha Protheus - TAF - eSocial - Eventos de tabelas - Como validar o cadastro de um evento de rubrica no TAF (S-1010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25509916713495-RH-Linha-Protheus-TAF-eSocial-Eventos-de-tabelas-Como-validar-o-cadastro-de-um-evento-de-rubrica-no-TAF-S-1010)

**Obs:** Caso encontre a divergência, para ajustar, terá que alterar a rubrica e fazer uma nova integração do S-1200 e S-1210 do GPE para o TAF já com a rubrica ajustada. Assim o relatório irá acatar a mudança feita.

Para clientes que utilizam o TAF - SEGREGADO precisam identificar o valor do Previdência Oficial no XML do S-1200, identificar a rubrica que está levando esse valor e validar se condiz com as informações acima.

**SAIBA MAIS:**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:

[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
