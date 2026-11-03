---
article_id: 34426052379671
category: GPE - eSocial - Periódicos
content_hash: cec8c163b38f20655e237ac1d2f0de7dce72e7d421da29fafbdb5a41d484175b
fetched_at: '2026-06-28T22:45:08.786062+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-1210 - Como gerar os eventos
  periódicos após calculo do roteiro RTF
type: support-article
updated_at: '2025-08-25T18:22:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34426052379671-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-gerar-os-eventos-peri%C3%B3dicos-ap%C3%B3s-calculo-do-roteiro-RTF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34426052360599) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar os eventos periódicos (S-1200/S-1210) após calculo do roteiro RTF?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
A inclusão do roteiro RTF é necessária quando não ocorre o pagamento de verbas na época correta.

A execução do roteiro prevê o cálculo de verbas vinculadas a ID´s específicos e diferença de INSS, mediante o lançamento da diferença por parte do usuário.  
Para isso verifique com atenção o [**Manual do Roteiro RTF.**](https://tdn.totvs.com/pages/releaseview.action?pageId=829317568)  
  
O valor a receber pelo funcionário deverá transitar pela folha em aberto, para que a retenção de IRRF seja feita corretamente no mês que será paga a diferença, pois para fins de Imposto de Renda sempre devemos considerar a data do fato gerador.  
  
Já os valores de INSS, serão gerados na Folha da época, que após ser enviada novamente ao RET (evento S-1200 - Retificador), fará com que o DCTFWeb gere um novo DARF com a diferença de INSS corrigida com Juros e Multas.

1. Reabrir o período que será retificado através da utilização do evento **S-1298 - Reabertura de Folha.**  
   **Através do Caminho: Módulo SIGATAF\Atualizações\eSocial\Periódicos\Reabertura de Folha**
2. **Excluir o evento S-1210 - Pagamentos Diversos**, do período que será retificado, referente aos funcionários  que terão a folha de pagamento retificada.   
   **Obs.**: esse processo é necessário devido ao conceito de ordem cronológica.
3. Gerar o evento **S-1200 do período que será retificado marcando a opção de Retificação.**  
   **Através do caminho: Módulo SIGAGPE\Miscelânea\eSocial\Periódicos**

Verifique no link a seguir o **passo a passo** para realizar a reabertura e retificação: [**RH - Linha Protheus - GPE - eSocial - Como retificar ou reprocessar os Totalizadores (DCTFWEB) no eSocial**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254-RH-Linha-Protheus-GPE-eSocial-Como-retificar-ou-reprocessar-os-Totalizadores-DCTFWEB-no-eSocial?source=search)  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
