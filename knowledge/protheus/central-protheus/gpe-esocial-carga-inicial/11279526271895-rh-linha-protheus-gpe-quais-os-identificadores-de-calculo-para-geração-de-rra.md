---
article_id: 11279526271895
category: GPE - eSocial - Carga Inicial
content_hash: aece6dc72aaadcbfdf79d79615002062dc7161438e3ae971eb5faf1d619389a3
fetched_at: '2026-06-28T22:45:03.356161+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os identificadores de calculo para geração
  de RRA
type: support-article
updated_at: '2024-06-26T14:42:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11279526271895-RH-Linha-Protheus-GPE-Quais-os-identificadores-de-calculo-para-gera%C3%A7%C3%A3o-de-RRA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446139585431) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais os identificadores de calculo para geração de RRA?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Cadastre as verbas para cada novo **identificador de RRA** conforme abaixo:

|  |  |  |
| --- | --- | --- |
| Identificador (RV\_CODFOL) | Descrição | Tipo (RV\_TIPOCOD) |
| 0974 | Base IR RRA | Base |
| 0975 | Contr. Previdenciária RRA | Desconto |
| 0976 | Pensão Aliment. RRA | Desconto |
| 0977 | Liquido RRA | Base |
| 0978 | IR RRA | Desconto |
| 0979 | Base IR 13º. RRA | Base |
| 0980 | Contr. Previdenciária 13º. RRA | Desconto |
| 0981 | Pensão Aliment. 13º. RRA | Desconto |
| 0982 | Liquido RRA 13º | Base |
| 0983 | IR RRA 13º | Desconto |
| 0986 | Dif. Dissídio RRA - Provento | Provento |
| 0987 | Dif. Dissídio RRA – Desconto | Desconto |

Configure o campo RRA (**RV\_RRA**) com a **opção Sim**, para todas as **verbas de Diferença de Dissídio** (Identificadores de cálculo: 0337, 0338, 0339, 0340, 0341, 0342, 0398, 0399, 0400, 0401, 0402, 0403).  
Verifique no Manual do Dissidio exemplo de configuração: **[MANUAL GPE - Dissídio Retroativo](https://tdn.totvs.com/pages/viewpage.action?pageId=220889925)**  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - Como cadastrar a tabela S034 de IR para RRA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10632803238679-RH-Linha-Protheus-GPE-Como-cadastrar-a-tabela-S034-de-IR-para-RRA-)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina:[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
