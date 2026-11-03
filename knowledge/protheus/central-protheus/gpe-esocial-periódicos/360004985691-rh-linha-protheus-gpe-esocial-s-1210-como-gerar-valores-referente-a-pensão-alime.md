---
article_id: 360004985691
category: GPE - eSocial - Periódicos
content_hash: f60033aa5c4444f6edb8accf4a72012358b92c6dd922b0cb8c6e423cf4a834dd
fetched_at: '2026-06-28T22:45:08.931305+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1210 - Como gerar valores referente
  a pensão alimentícia no evento S-1210
type: support-article
updated_at: '2025-07-29T13:51:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004985691-RH-Linha-Protheus-GPE-eSocial-S-1210-Como-gerar-valores-referente-a-pens%C3%A3o-aliment%C3%ADcia-no-evento-S-1210
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33791166833431) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como gerar valores referente a pensão alimentícia no evento S-1210 a partir do leaiute S-1.2?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para gerar o valor da **pensão** no evento **S-1210** é necessário que a verba esteja com as informações abaixo no cadastro de verbas do SIGAGPE.   
Caminho: atualizações > definições de calculo > **verbas > aba esocial.**

Campo Natureza deve ser igual a **9213.**Campo Cd. Inc. IRRF deve ser igual a **51, 52, 53, 54, 55.**As informações do Beneficiário da Pensão Alimentícia são preenchidas de acordo com as informações do cadastro de **Beneficiário e Dependentes** no GPE, onde também é parametrizado as regras do cálculo do valor da Pensão Alimentícia, nesse cadastro deve ser informado a verba para pagamento de acordo com cada coluna no cadastro.  
  
**Segue abaixo o Print do cadastro do beneficiário:**Caminho: Atualizações > Funcionários > Beneficiários  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25965864447511)  
O campo **CPF no cadastro do dependente** é obrigatório.  
  
Se for informado manualmente a Pensão Alimentícia no cálculo do GPE o S-1210 não será gerado com a tag onde contém valores de pensão, por isso se faz necessário a utilização do cadastro de beneficiário.  
  
No leiaute do S-1210 para a versão S-1.2 serão levadas as *tags,* conforme *print* abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25965864453911)  
 **Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Boletim técnico Leiaute S-1.2 Dependentes, Pensão Alimentícia e Previdência Complementar](https://tdn.totvs.com/pages/releaseview.action?pageId=789982783)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes) 

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
