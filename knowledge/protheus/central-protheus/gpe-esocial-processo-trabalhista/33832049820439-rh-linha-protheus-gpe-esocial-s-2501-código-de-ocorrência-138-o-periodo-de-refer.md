---
article_id: 33832049820439
category: GPE - eSocial - Processo Trabalhista
content_hash: 4d24df4154304fcc84f57e0905c226d5f97cff6f5ff536a45e635dae953fb4c6
fetched_at: '2026-06-28T22:45:00.456462+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2501 - Código de ocorrência 138 - O
  periodo de referencia AAAA-MM informado devera existir no campo homonimo do evento
  de Processo Trabalhista S-2500
type: support-article
updated_at: '2025-07-31T21:09:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33832049820439-RH-Linha-Protheus-GPE-eSocial-S-2501-C%C3%B3digo-de-ocorr%C3%AAncia-138-O-periodo-de-referencia-AAAA-MM-informado-devera-existir-no-campo-homonimo-do-evento-de-Processo-Trabalhista-S-2500
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33832025043991) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Erro - Codigo da ocorrência: 138 Localização: /eSocial/evtContProc/ideTrab/calcTrib/@perRef Descrição: O periodo de referencia AAAA-MM informado devera existir no campo homonimo do evento de Processo Trabalhista S-2500 (observado o campo de Numero sequencial atribuido pela empresa do evento correspondente, se existente) e ser igual ou posterior a [2008-12].  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
O erro ocorre quando o evento S-2500 não contém o período de referencia informado no S-2500 nas *tags* de competência inicial e competência final, ou casos de múltiplos processos com mesmo número de processo e não contém a *tag* de sequencia informada no S-2500.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Verifique no evento S-2500 se as datas informadas nos campos competência inicial e competência final, contemplam o período de referencia informado no S-2501.  
No Protheus podemos acessar a rotina Dados do eSocial (TAFA552D), clicar em alterar o contrato de trabalho. Abaixo mostramos um exemplo com dados fictícios:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859649364887)  
  
As informações devem contemplar o periodo de referencia informado no lançamento do S-2501 - Tributos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859672394775)  
  
**2.** O erro também ocorre em casos de processos com mesmo número e período de apuração. Nesse caso o é obrigatório o número de sequencia informado em cada S-2500.  
**Número sequencial** atribuído pela empresa a cada conjunto de dados de tributos decorrentes de processo trabalhista, quando for necessário enviar o mesmo processo em múltiplos S-2501, para o mesmo [perApurPgto](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-04-2025/index.html#2501_ideProc_perApurPgto).  
  
No sistema teremos a informação de sequencia no campo da rotina Processos (APTA100) que após preenchido, será levado a rotina Dados do eSocial e posteriormente no xml do S-2501.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859649369367)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859649374359)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
