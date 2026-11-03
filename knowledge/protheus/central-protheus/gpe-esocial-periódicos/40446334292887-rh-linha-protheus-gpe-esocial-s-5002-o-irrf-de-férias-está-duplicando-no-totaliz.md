---
article_id: 40446334292887
category: GPE - eSocial - Periódicos
content_hash: 92f74a353e0212a8d99ff2c286b8d6967fa709924bfcf464744a4a7e3b8570b6
fetched_at: '2026-06-28T22:45:07.452477+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5002 - O IRRF de férias está duplicando
  no totalizador, o que devo analisar
type: support-article
updated_at: '2026-06-24T16:08:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40446334292887-RH-Linha-Protheus-GPE-eSocial-S-5002-O-IRRF-de-f%C3%A9rias-est%C3%A1-duplicando-no-totalizador-o-que-devo-analisar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40446334274327) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
O IRRF de férias está duplicando no totalizador, o que devo analisar? Id 1893 não gera no S-1200.  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para férias a partir de 01/01/2026 devemos utilizar as verbas de substituição, para que o sistema envie no S-1200 de férias as verbas substitutas com incidencia de IRRF para eSocial, assim no S-1200 FOL serão levados codigo de verbas diferentes, deixando de duplicar o valor no eSocial.  
  
Sendo assim, devemos analisar se a verba de id 0067 possui no cadastro de verbas, aba eSocial, os campos Verba Substituta paga no mês e Verba Substituta paga mês anterior preenchidos.  
  
Acessar Atualizações - Definição Cálculos - Verbas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40446334275735)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40446334276887)  
  
A verba original que contém identificador de cálculo deve ficar com incidência 9 para IRRF pois essa verba será levada para folha de pagamento.  
  
As verbas de substituição terão as configurações conforme abaixo, exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40446334278679)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40446317276183)  
**Veja também o video mostrando essas parametrizações!**  
  
Após analise e criação, se necessário das verbas substitutas para o IRRF férias, analise se no cálculo das férias, na coluna Verb. Substituta foram levadas as verbas corretas. Segue video para auxiliar nessa conferencia: [How To | Conferência Incidências Verbas Substituição de Férias #TOTVS\_RH\_Linha\_Protheus](https://www.youtube.com/watch?v=Sg7RqCopp7s)  
  
O parametro **MV\_DTINFER** deve ter conteudo **20260101**  
  
Caso o**cálculo de ferias tenha sido realizado sem a criação das verbas de substituição**, realize o cadastro das verbas conforme passo a passo acima e **recalcule as ferias**.   
  
Para **férias que não podem ser recalculadas**, utilize o Rdmake [**UPDFERSUB**](https://tdn.totvs.com/pages/releaseview.action?pageId=1014630057#body-body2)que fará a inclusão das verbas de substituição no cálculo das ferias, sem precisar recalcular.   
Necessário compilar o Rdmake dos links abaixo:  
12.1.2310:<https://r.totvs.io/p/1238079> ;   
12.1.2410:<https://r.totvs.io/p/1238077> ;   
12.1.2510:<https://r.totvs.io/p/1238078> ;  
  
Por regra do esocial, para alteração de valores por conta de incidências ou naturezas de rubricas, é necessário enviar o S-1010 com competência igual ou anterior ao período que precisam ajustar e retificar os eventos periódicos conforme documento abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254-RH-Linha-Protheus-GPE-eSocial-Como-retificar-ou-reprocessar-os-Totalizadores-DCTFWEB-no-eSocial?source=search>  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:  
[RH - Linha Protheus - GPE - eSocial - S-5002 - Conferência dos valores de IRRF (Ano-Calendário 2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40110088788887-RH-Linha-Protheus-GPE-eSocial-S-5002-Confer%C3%AAncia-dos-valores-de-IRRF-Ano-Calend%C3%A1rio-2025)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
