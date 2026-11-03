---
article_id: 39308259933079
category: TAF - eSocial - Relatório
content_hash: 09c59a680026179a11dc148966bc01d32dace9e09a4ad1b96d186f2f5e2bc571
fetched_at: '2026-06-28T22:45:19.881375+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF - Relatório DIRF - Como validar a divergência
  do valor de Rendimento tributável
type: support-article
updated_at: '2026-03-26T19:44:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39308259933079-RH-Linha-Protheus-eSocial-TAF-Relat%C3%B3rio-DIRF-Como-validar-a-diverg%C3%AAncia-do-valor-de-Rendimento-tribut%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39308250052759) Tempo aproximado para leitura: **01:30:00 min**  
  
**Dúvida**  
Como validar a divergência da coluna rendimento tributável do relatório DIRF  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório DIRF - Todas as versões  
  
**Solução**  
  
  
1. Como gerar o Relatório DIRF 'como somente divergente'?

[RH (Linha Protheus) - eSocial - TAF - Relatório - Como gerar o Relatório DIRF como somente divergente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38893239676311-RH-Linha-Protheus-eSocial-TAF-Relat%C3%B3rio-Como-gerar-o-Relat%C3%B3rio-DIRF-como-somente-divergente)

Validação quando o valor do TAF estiver menor ou maior com relação ao valor do Governo.

![NOVO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39315740161431)

2.  Verificando a Incidência da rubrica:

Anote o CPF e o Período do colaborador

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39315736326039)

3.  Acesse o cadastro de folha de pagamento no TAF

Rotina no menu do TAF (Atualizações > Eventos Esocial > Periódicos > Folha de Pagamento)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39308417560599)

4. Utilize o filtro para localizar o funcionário através do CPF e Período:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39315740170647)

**Clique em Alterar** (atenção: não salve o cadastro após a análise).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39315736329879)

5.  Localize a **RUBRICA**

* Localize na Aba **Demonstrativos de Valores** o grupo **Informações da Remuneração do Trabalhador no Período de Apuração**
* **Instruções de Validação:**
  + **Identificação:** Procure a rubrica relativa ao campo avaliado (ex: Rendimento Tributável/Salário).
  + **Verificação:****Identifique possíveis rubricas adicionais.**
  + **Conformidade:** Se houver outros itens, valide se o tipo de incidência corresponde ao grupo selecionado.

![1200.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39311740037015)

6. Selecione a rubrica referente ao valor de Rendimento Tributável e depois clique na lupa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39308259901591)

Clique em Visualizar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39308250058007)

7. Valide se a rubrica corresponde ao item avaliado, Anote o seu valor e o tipo da rubrica, Certifique-se de que a Incidência de IRRF esteja definida como 11, 13, 14

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39308259909015)

Valide se o cadastro da rubrica está de acordo com a documentação, exemplo do print acima

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39308259909655)

Link: <https://tdn.totvs.com/display/TAF/Painel+do+evento+S-5002+Imposto+de+Renda+Retido+na+Fonte+por+Trabalhador>

|  |
| --- |
| **Divergências**  Eventuais erros no valor da incidência ou no tipo de **rubrica** são as causas prováveis de divergências no relatório. Por esse motivo, é indispensável realizar uma **análise** da folha em confronto com a documentação do campo no layout do eSocial, conforme orientado anteriormente.  **Fonte:** [Layout e-Social versão S-1.3 - Regras de composição evento S-5002](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-nt-06-2026/index.html#5002_ideTrabalhador_dmDev_infoIR) |

**SAIBA MAIS:**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina:

[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
