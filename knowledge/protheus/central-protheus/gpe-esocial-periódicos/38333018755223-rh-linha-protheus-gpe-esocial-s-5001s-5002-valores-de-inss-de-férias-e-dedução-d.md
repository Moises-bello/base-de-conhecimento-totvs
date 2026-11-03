---
article_id: 38333018755223
category: GPE - eSocial - Periódicos
content_hash: 355f9ccae90f9504c9711b277d05408a8bd54abca18f5038e4a14207b60017cc
fetched_at: '2026-06-28T22:45:09.903219+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5001/S-5002 - Valores de INSS de férias
  e Dedução de INSS na base de IRRF férias duplicados após criação de verbas de substituição
type: support-article
updated_at: '2026-06-19T16:43:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38333018755223-RH-Linha-Protheus-GPE-eSocial-S-5001-S-5002-Valores-de-INSS-de-f%C3%A9rias-e-Dedu%C3%A7%C3%A3o-de-INSS-na-base-de-IRRF-f%C3%A9rias-duplicados-ap%C3%B3s-cria%C3%A7%C3%A3o-de-verbas-de-substitui%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38333018739479) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
O valor do INSS de férias e da dedução do INSS na base de IRRF ferias está duplicando no totalizador do eSocial, após gerar as verbas de substituição, como corrigir?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:   
  
**1**. Cria as verbas de substituição férias pagas no mês e férias pagas mês anterior e associe na verba de ID 0065. Veja o video Configuração verba 0065 que auxiliará na criação das verbas  
Atenção, para o **MV\_DINSSFM = N** veja o tdn disponibilizado: <https://tdn.totvs.com/pages/releaseview.action?pageId=1070852375>   
  
**2**. Cria as verbas de substituição férias pagas no mês e férias pagas mês anterior e associe na verba de ID 0168. Veja o video Configuração verba 0168 que auxiliará na criação das verbas  
  
**Se utilizar o id 0065, então as verbas de substituição do id 0168 ficarão com 9 para IRRF.**  
**Caso utilize o id 0168, então as verbas de substituição do id 0065 ficarão com 9**  
  
**3**. Será necessário recalcular as férias, ou utilizar o Rdmake [**UPDFERSUB**](https://tdn.totvs.com/pages/releaseview.action?pageId=1014630057#body-body2)que fará a inclusão das verbas de substituição no cálculo das ferias, sem precisar recalcular.   
Necessário compilar o Rdmake dos links abaixo:  
12.1.2310:<https://r.totvs.io/p/1238079> ;   
12.1.2410:<https://r.totvs.io/p/1238077> ;   
12.1.2510:<https://r.totvs.io/p/1238078> ;  
  
**4**. Para criação manual do menu do rdmake, verifique a imagem em anexo.  
  
**5**. Após os passos realizados, gere novamente o evento S-1200.  
  
Assista a playlist sobre as verbas de substituição e como conferir:

**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[RH - Linha Protheus - GPE - eSocial - Como se adequar e atualizar o ambiente para Nota Técnica 04/2025 leiaute S-1.3 referente a Natureza de Rubrica 1015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37108578059927-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-e-atualizar-o-ambiente-para-Nota-T%C3%A9cnica-04-2025-leiaute-S-1-3-referente-a-Natureza-de-Rubrica-1015)  
[RH - Linha Protheus - GPE - eSocial - Como retificar ou reprocessar os Totalizadores (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254-RH-Linha-Protheus-GPE-eSocial-Como-retificar-ou-reprocessar-os-Totalizadores-DCTFWEB-no-eSocial?source=search)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
