---
article_id: 360036060134
category: GPE - eSocial - Periódicos
content_hash: d65e79e4f31c827ff6dd4e49501c4e6051f4436b11c7ebc3c5d63abd035f46db
fetched_at: '2026-06-28T22:45:09.033841+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1299 - Ao tentar gerar o evento S-1299
  Fechamento eSocial, esta aparecendo apenas a opção de selecionar a filial Matriz
type: support-article
updated_at: '2025-07-24T21:52:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036060134-RH-Linha-Protheus-GPE-eSocial-S-1299-Ao-tentar-gerar-o-evento-S-1299-Fechamento-eSocial-esta-aparecendo-apenas-a-op%C3%A7%C3%A3o-de-selecionar-a-filial-Matriz
---

**Ocorrência**Ao tentar gerar o evento **S-1299** Fechamento **eSocial**, esta aparecendo apenas a opção de selecionar a filial Matriz.  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Conforme leiaute do **eSocial** o evento **S-1299** deve ser gerado por **Empregador** e não por filial. Para o **eSocial** o **Empregador** é toda a empresa e seus estabelecimentos que possui a raiz do CNPJ (8 primeiros dígitos) iguais.  
  
**Solução**Foi feito um ajuste no sistema para que apareça somente a filial matriz para geração do **S-1299**, pois o XML gera apenas informações do Empregador (Empresa Matriz), trazendo os 8 primeiros dígitos do CNPJ. E não existindo para o eSocial S-1299 por filial.  
  
**Perguntas e respostas governo**04.34 - (01/03/2018) Tenho uma empresa sem movimento, mas as filiais têm movimento. Neste caso, como faço a informação? Preciso ter certificado digital para enviar as empresas sem movimento? Ou posso enviar direto pelo site do eSocial?

Uma empresa será considerada "sem movimento", **apenas quando nenhum de seus estabelecimentos tiver informações a serem prestadas.**Não há eventos do eSocial por estabelecimento. As regras de envio do evento S-1299 "sem movimento" são as mesmas para empresas com movimento. Ou seja, deverá ser utilizado o certificado digital para o envio do S-1299 "sem movimento", se ele for exigido para a transmissão dos outros eventos.   
  
**Evento S-1299**  
![](https://totvssuporte.zendesk.com/attachments/token/tqRNhB08r1Mmum4SEuaolJInK/?name=inline425455851.png)​  
*Link*: <https://www.gov.br/esocial/pt-br/documentacao-tecnica> 

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais) [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
