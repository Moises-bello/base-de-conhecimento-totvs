---
article_id: 40110088788887
category: GPE - eSocial - Periódicos
content_hash: 35468b257c3e83db6545625d478539bd3e3299816323098134721fd044d9dc5e
fetched_at: '2026-06-28T22:45:07.447387+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5002 - Conferência dos valores de IRRF
  (Ano-Calendário 2025) para DIRF
type: support-article
updated_at: '2026-06-24T14:50:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40110088788887-RH-Linha-Protheus-GPE-eSocial-S-5002-Confer%C3%AAncia-dos-valores-de-IRRF-Ano-Calend%C3%A1rio-2025-para-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40110088774295) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
Como conferir os valores de IRRF através das incidências esocial para DIRF ?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**

**1º Passo: Identificar quais são os funcionários com valores divergentes.**

Antes de tudo, não tente analisar considerando o valor total. Isso dificulta muito encontrar o problema, o ideal é:

* Identificar **um funcionário com divergência**
* Usar ele como base para análise

O relatório do TAF pode auxiliar nessa busca:  
**TAF**: [**Relatório de IR - DIRF**](https://tdn.totvs.com/pages/viewpage.action?pageId=1025242921)   
**Middleware**:[**Relatório de conferência IRRF**](https://tdn.totvs.com/pages/releaseview.action?pageId=1032142738)   
  
**2º Passo: Gerar o relatório S-1200/S-2299 de um funcionário de exemplo:**  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE?source=search)  
[RH - Linha Protheus - GPE - eSocial - S-2299 - Como gerar o relatório de conferencia do evento S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299?source=search)

**⚠️** **Atenção importante:**  
**O S-1200/S-2299 deve sempre considerar a** **folha que originou o pagamento (S-1210)**

**Regime Caixa (exemplo)**

* Pagamento: 02/2026
* Folha: 01/2026 → esse é o período que deve ser gerado o relatório.

**Regime Competência (exemplo)**

* Pagamento: 01/2026
* Folha: 01/2026 → esse é o período que deve ser gerado o relatório.

**3º Passo : Analise as incidências de IRRF**  
Após gerar o relatório,  é importante conferir quais incidências estão compondo o cálculo do IRRF.

As principais são:

* **Rendimentos tributáveis:** 11 e 13
* **Retenção de IRRF:** 31 e 33
* **Previdência oficial:** 41 e 43
* **Abono pecuniário:** 75
* **Valor isento e não tributavel**: 79 (entre outras)

Você pode consultar todas as incidências aceitas pelo esocial para IRRF através do link: [Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-02-2024-rev-29-10-2024/tabelas.html#21)  
  
**Como validar ?**  
Acesse a **aba 8** do relatório e aplique os **filtros** por identificador, data de pagamento e pela incidência relacionada ao valor que está divergente no totalizador.   
Por exemplo, se a divergência estiver nos **rendimentos tributávei**s, **filtre as incidências 11 e 13 na coluna IRRF eSocial.**

**Em seguida, realize a conferência dos valores, somando os proventos e subtraindo os descontos conforme o tipo de cada verba, e compare o resultado com o valor apresentado no eSocial.**

**Se os valores coincidirem, o próximo passo é validar se:**

* Todas as verbas estão com a **incidência correta;**
* Essas verbas **deveriam compor a base de cálculo;**
* Os **valores informados nas verbas** estão corretos.

*Exemplo de validação abaixo:*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40110088774935)

**4º Passo: Atenção especial para férias**  
As verbas de férias podem gerar **duplicidade no eSocial** se não forem tratadas corretamente.Isso acontece porque as verbas de férias transitam pela folha de pagamento.

👉 Para evitar isso, verifique se existem as **verbas de contrapartida na folha:**

* ID 1562 – Contrapartida dos rendimentos tributáveis
* ID 1722 – Contrapartida do abono pecuniário
* ID 1723 – Contrapartida da previdência
* ID 1893 – Contrapartida da retenção de IRRF
* ID 1986 – Diferença de férias (retorno de férias partidas)

Caso na folha não tenha sido gerado algum desses identificadores , é necessário rodar o RDMAKE para serem incluídas ou ajustar os valores.

* Para os id's 1562, 1722, 1723 : RDMAKE UPDBIRFER  
  [Boletim técnico: DT Criação Ids 1562, 1722 e 1723](http://tdn.totvs.com/pages/viewpage.action?pageId=394210801)

Para a utilização , é necessário compilar o fonte UPDBIRFER que fica dentro da pasta RDMAKE de qualquer expedição contínua e incluir no menu.

* Para os id's 1893 e 1986 : Rotina GPEM026I  
  [RH - Linha Protheus - GPE - Rotina GPEM026I (Antigo Rdmake UPDBINFER)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER?utm_term=&utm_campaign=TOTVS_CONV_AON_MEIO_NATIVA_ASSINATURA-ELETRONICA-PLANOS-DE-VENDAS&utm_source=adwords&utm_medium=ppc&hsa_acc=5745705588&hsa_cam=23507107132&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23507109535&gbraid=0AAAAADrTa5xZfI_VjLtd7BciZvyJDhIbD&gclid=CjwKCAjwnZfPBhAGEiwAzg-VzBE9j1oA0deE_u-75l_wWYLkIPCs5RteKHa8XbVuvvXXJE06n0ikABoCE7wQAvD_BwE)

Para a utilização , é necessário incluir a rotina no menu.

Incluímos no link abaixo dois vídeos de como realizar a conferência nos casos de **férias e mensal na prática.** Caso hajanecessidade: Copie o link e cole em seu navegador para baixar os dois videos:  
<http://suporte.totvs.com/customer-portal-wdgt-fileupload/api/rest/uploadFile/downloadAttach?file=20260312/195791-fluig-elastic-N-FL-P-C99TTV-1-b7384LIN-SP06-1773335750497-183356.zip>   
  
Quando as Férias transitam pela Folha de Pagamento essa verba pode sofrer alterações, devido ao cálculo de INSS, que está atralado ao parâmetro **MV\_DINSSFM = N**. Veja a sugestão de parametrização:  
[Desconto da Previdência Oficial X eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=1060208641)

**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[RH - Linha Protheus - GPE - eSocial - Como adequar o Protheus para substituição da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30740106501527-RH-Linha-Protheus-GPE-eSocial-Como-adequar-o-Protheus-para-substitui%C3%A7%C3%A3o-da-DIRF)  
[RH - Linha Protheus - GPE - Divergência declaração Pré-Preenchida x eSocial x Folha Protheus RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/39342793656983-RH-Linha-Protheus-GPE-Diverg%C3%AAncia-declara%C3%A7%C3%A3o-Pr%C3%A9-Preenchida-x-eSocial-x-Folha-Protheus-RH)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)
