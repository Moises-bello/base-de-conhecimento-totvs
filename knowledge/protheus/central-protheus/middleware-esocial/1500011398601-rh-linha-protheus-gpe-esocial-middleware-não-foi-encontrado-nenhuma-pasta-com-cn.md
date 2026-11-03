---
article_id: 1500011398601
category: MIDDLEWARE eSocial
content_hash: d31d0dcd111f9fc039d32ffd9a07a96f81c46b2a2dddd49bc9c4d4a14accc631
fetched_at: '2026-06-28T22:43:05.014651+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Middleware - Não foi encontrado nenhuma
  pasta com CNPJ's informados no diretório
type: support-article
updated_at: '2025-07-25T14:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011398601-RH-Linha-Protheus-GPE-eSocial-Middleware-N%C3%A3o-foi-encontrado-nenhuma-pasta-com-CNPJ-s-informados-no-diret%C3%B3rio
---

**Ocorrência**Ao realizar realizar a importação de XMLs de terceiros através da rotina de importação (GPEM017D) é apresentada a mensagem: "Não foi encontrado nenhuma pasta com CNPJs informados no diretório."  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018251282)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal -  Todas as versões  
  
**Causa**A mensagem é apresentada, devido **um erro no diretório que está sendo escolhido** no momento da importação.  
  
**Solução**Ao importar os XML's de terceiros, deverá ser escolhido ou criado uma pasta a critério do cliente e obrigatoriamente dentro da mesma, deverá ser criado uma nova pasta apenas com o CNPJ da empresa que está cadastrado no protheus. O usuário deve ter acesso as pastas.  
  
Segue **exemplo**:   
1- Foi criado uma pasta **Migrador-Mid** dentro da **protheus\_data**:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018252582)  
  
2- Dentro da mesma foi criado uma nova pasta apenas com o CNPJ da empresa onde foram armazenados os XML's de terceiros.    
  
3- Ao utilizar a rotina de importação o diretório deverá ser escolhido até a primeira pasta onde serão informados todos os CNPJ's:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018536381)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[RH - eSocial - Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005445753-RH-ESOCIAL-MIDDLEWARE)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
