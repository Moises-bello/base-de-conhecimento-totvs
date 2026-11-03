---
article_id: 360006744012
category: GPE - eSocial - Saneamento de Base
content_hash: 22514b4e5db161836473c4d012a17ce7e15677c75efe3a33d34665214bbfaeb7
fetched_at: '2026-06-28T22:45:01.618670+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como gerar o XML de eventos eSocial integrados
  do SIGAGPE com o SIGATAF para analise do suporte técnico
type: support-article
updated_at: '2026-05-15T10:55:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006744012-RH-Linha-Protheus-GPE-eSocial-Como-gerar-o-XML-de-eventos-eSocial-integrados-do-SIGAGPE-com-o-SIGATAF-para-analise-do-suporte-t%C3%A9cnico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28157497026967) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como gerar (exportar) o XML de eventos eSocial integrados do **SIGAGPE** (Gestão de Pessoal) com o **SIGATAF** (Totvs Automação Fiscal) para analise do suporte técnico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
 **Solução**No sistema existe 2 tipos de **XML** que pode ser utilizado para analise de erros gerados na integração do **SIGAGPE**  com o **SIGATAF** ou do **SIGATAF** com o **RET** (governo). Com esses arquivos **XML** é possível identificar diversos erros.  
  
**Para gerar o XML do SIGAGPE execute os passos abaixo:**

**1ª Opção:** Quando o evento com erro foi gerado e está no TAF.

* Execute o passo a passo disponível no artigo: **[Como gerar ou comparar os arquivos XML do SIGAGPE e SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026656853).**

**2ª Opção:** Quando o suporte precisa especificamente do **XML** gerado pelo modulo **SIGAGPE** e não é possível gerar com as orientações da **opção 1**. Realize o procedimento abaixo e gere novamente o processo de integração para gerar para os casos em que o parâmetro estava desabilitado no momento da integração

* Acesse o modulo configurador (SIGACFG) e altere o parâmetro **MV\_XMLGPE** para **.T.** conforme detalhado no artigo: **[Como definir o local onde é gerado os arquivos XML's de eventos eSocial quando utilizado o parâmetro MV\_XMLGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035286913)**.

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
