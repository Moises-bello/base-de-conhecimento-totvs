---
article_id: 360035983693
category: GPE - eSocial - Periódicos
content_hash: 9c0f21dad36dfb012dab53d9aaa6e5662e40215ededb1aa28b31d69c71577c0d
fetched_at: '2026-06-28T22:45:07.501825+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial  - No momento de integração de um evento
  do GPE ao TAF é apresentado a mensagem: "Não foi Possível criar o arquivo: GPE_XML_Dagnostico_XXX..."'
type: support-article
updated_at: '2025-07-25T14:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035983693-RH-Linha-Protheus-GPE-eSocial-No-momento-de-integra%C3%A7%C3%A3o-de-um-evento-do-GPE-ao-TAF-%C3%A9-apresentado-a-mensagem-N%C3%A3o-foi-Poss%C3%ADvel-criar-o-arquivo-GPE-XML-Dagnostico-XXX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28160884358295) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No momento de integração de um evento do GPE ao TAF é apresentado a mensagem: "Não foi Possível criar o arquivo: GPE\_XML\_Diagnostico\_XXX..."  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160838296983)  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Essa mensagem é apresentada sempre quando é gravado alguma informação no GPE e o Sistema vai enviá-la ao TAF.  
  
Isso ocorre porque o parâmetro **MV\_XMLGPE está com conteúdo igual a '.T.'** e o **usuário do Sistema não tem acesso a pasta selecionada** como destino de gravação do arquivo XML do GPE.  
  
**Solução**  
Para solucionar essa ocorrência pode ser executado um dos dois procedimentos abaixo:

1. Pode ser Alterado o conteúdo do parâmetro MV\_XMLGPE para '.F.', para mais informações sobre o parâmetro **[clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=320380007)**;
2. Pode ser alterada/ajustada a pasta selecionada como destino de gravação do arquivo XML do GPE. Para isso acesse a rotina de **Carga Inicial do GPE (GPEM023)**, depois **Outras Ações** e clique sobre **Parâmetros Grav. XML**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33713845747479)  
     
   Será aberto a tela abaixo onde poderá editar ou escolher o caminho para gravação dos próximos arquivos, é i**mportante que tenha acesso a pasta selecionada** e depois é só clicar em OK e fechar a rotina de carga inicial.  
     
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047097393)

**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
