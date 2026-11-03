---
article_id: 360028765733
category: GPE - eSocial - Periódicos
content_hash: 140119b50fa8a264f42a215a7aa0bb165646b2cc27fe8bcd87a1f2c964780557
fetched_at: '2026-06-28T22:45:09.873100+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5001 - Como é realizada a apuração
  do INSS de 13º Salário para Trabalhadores Intermitentes no eSocial
type: support-article
updated_at: '2025-07-21T14:45:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028765733-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-%C3%A9-realizada-a-apura%C3%A7%C3%A3o-do-INSS-de-13%C2%BA-Sal%C3%A1rio-para-Trabalhadores-Intermitentes-no-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26848502940951) Tempo aproximado para leitura: 01:00 min  
  
Dúvida**Como é realizada a apuração do INSS de 13º Salário para Trabalhadores Intermitentes no eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**De acordo com o [Manual de Orientações eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica) vigente, o valor devido de 13º salário a trabalhador intermitente e avulso deve ser informado em rubrica com o código de incidência 12 para os campos {codIncCP} e {codIncFGTS} e {codIncIRRF}.  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9905036095767)**Os valores apresentados no portal do eSocial são computados de acordo coma incidência das rubricas, mas o cálculo é realizado pelo próprio RET (Governo), ou seja, é uma ferramenta externa ao Protheus, o que podemos fazer é certificar que essas informações estão saindo do Protheus da forma esperada pelo leiaute do eSocial, ou seja códigos de rubricas e valores corretos.  
Em testes de integração de um Trabalhador com contrato Intermitente com o RET (Governo) em ambiente de pré-produção e o resultado apurado pelo RET (Governo) é o mesmo apresentado na Folha de Pagamento do GPE.  
  
Vale destacar que o 13º Salário Proporcional do Trabalhador Intermitente é remunerado/pago mensalmente com os demais valores que ele tem direito.  
  
Os valores apresentados no portal do eSocial são computados respeitando o teto da Contribuição Previdenciária e informações já enviadas em meses anteriores **com o mesmo código de incidências de Contribuição Previdenciária**.  
  
**Observação:**A**configuração das Verbas/Rubricas com relação a Natureza e as Incidências Tributárias é algo particular de cada Empresa** e que deve ser analisado em conjunto com o departamento Jurídico e Contábil.   
Segue abaixo o teste realizado  em ambiente de pré-produção do RET (Governo).  
  
Exemplo: No primeiro momento foi enviado o S-1200 de 11/2018 com uma base de cálculo de 13º Salário de R$ 1.088,89 e um INSS de 13º retido de R$ 87,11, ou seja, uma alíquota de 8%, segue abaixo os *prints* do S-5001 retornado pelo RET.  
 **![](https://totvssuporte.zendesk.com/attachments/token/qA6qqDskD4LyPDgt2SgEDBGlx/?name=inline348594015.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/hgqFcJC8qwYz3Vpyu9BUQ7fSI/?name=inline475066484.png)​**Exemplo: No segundo momento foi enviado o S-1200 de 12/2018 com uma base de cálculo de 13º Salário de R$ 13.890,67 e um INSS de 13º retido de R$ 533,92, ou seja, uma alíquota de 11%, porém respeitando o teto do INSS de 13º de R$ 621,03 devido parte da contribuição anual já ter sido retida em 11/2018, segue abaixo os *prints* do S-5001 retornado pelo RET. **![](https://totvssuporte.zendesk.com/attachments/token/xYRpaQ12z5z1MrPiqsd4Hmqv3/?name=inline2138732936.png)​  
  
![](https://totvssuporte.zendesk.com/attachments/token/yn9xA89SkSkaCNyMlkF3OtkvD/?name=inline1683010556.png)​**  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-5001 - Como conferir as divergências encontradas entre o INSS apurado pelo governo e o relatório do TAF (TAFR120)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024628231-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-conferir-as-diverg%C3%AAncias-encontradas-entre-o-INSS-apurado-pelo-governo-e-o-relat%C3%B3rio-do-TAF-TAFR120)  
[RH - Linha Protheus - GPE - eSocial - S-1010 - Como configurar a Natureza e Código de Incidência Tributária das Verbas/Rubricas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023121291-RH-Linha-Protheus-GPE-eSocial-S-1010-Como-configurar-a-Natureza-e-C%C3%B3digo-de-Incid%C3%AAncia-Tribut%C3%A1ria-das-Verbas-Rubricas)  
[RH - Linha Protheus - GPE - eSocial - S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512-RH-Linha-Protheus-GPE-eSocial-S-5001-Como-ajustar-incid%C3%AAncia-e-validade-de-rubricas-no-governo-TAF-e-GPE)  
  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes) 

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
