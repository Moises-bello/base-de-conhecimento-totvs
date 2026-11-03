---
article_id: 16675236812183
category: GPE - eSocial - Periódicos
content_hash: bb8867a0667a0287f0224e75fa14488c7fb3ef9487095a104de15e411d930de0
fetched_at: '2026-06-28T22:45:09.968810+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - S-5002 - Como é definido o código de receita na
  DCTFWeb
type: support-article
updated_at: '2025-07-17T14:36:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16675236812183-RH-Linha-Protheus-GPE-S-5002-Como-%C3%A9-definido-o-c%C3%B3digo-de-receita-na-DCTFWeb
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16675194929431) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como é definido o código de receita na DCTFWeb?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O código de Receita é definido com base na **Categoria do eSocial** e informações relativas a residentes no exterior, esse código de receita não é enviado em nenhum evento do eSocial, ele é apresentado apenas no retorno do governo no evento S-5002 - Imposto de Renda Retido na Fonte por Trabalhador.

A regra dos CRs (código de receitas) de IRRF (Imposto de Renda Retido na Fonte) das diferentes categorias de trabalhadores, obedece o exemplo:

CRMen = **[056107]**: se codCateg = [101, 102, 103, 105, 106, 107, 108, 111, 201, 202, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 401, 410, 501, 721, 722, 723, 901, 902, 903, 904, 906], {indApurIR} = [0], os campos {indRRA} e paisResidExt não forem informados e classTrib em S-1000 for diferente de [22], efetuar o somatório de valor cujo tpInfoIR = [31, 32];

CRMen = **[058806]**: se codCateg = [701, 711, 712, 731, 734, 738, 741, 751, 761, 771, 781], {indApurIR} = [0] e os campos {indRRA} e paisResidExt não forem informados, efetuar o somatório de valor cujo tpInfoIR = [31, 32, 34];  
  
Veja mais exemplos, no leiaute do evento [S-5002 - Imposto de Renda Retido na Fonte por Trabalhador](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-03-2025/index.html#5002_ideTrabalhador_dmDev_totApurMen)  
  
A divisão acima é baseada na atual legislação vigente artigo 36 do Regulamento do Imposto de Renda (Decreto Nº 9.580/2018). Além disso, o contribuinte pode consultar o MAFON – Manual do Imposto sobre a Renda Retido na Fonte para dirimir eventuais dúvidas.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - S-1200 - Como conferir os valores e incidências de IR enviadas ao esocial no evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14973614458263)  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Diferença entre Rendimento não tributável (7950) e verba transitada pela folha de pagamento (7900)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14230504342935)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
