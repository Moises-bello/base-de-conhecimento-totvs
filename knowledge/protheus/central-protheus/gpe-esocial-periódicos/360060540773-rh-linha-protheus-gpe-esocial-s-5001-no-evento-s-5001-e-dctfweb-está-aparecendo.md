---
article_id: 360060540773
category: GPE - eSocial - Periódicos
content_hash: 8ebda6cb19aaf7527da78d6bf80dd853472cd85155d2793a216ce8e94dff845c
fetched_at: '2026-06-28T22:45:09.891902+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-5001 - No evento S-5001 e DCTFWEB está
  aparecendo o código 19 para funcionários que recebem salário maternidade
type: support-article
updated_at: '2025-07-25T15:17:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060540773-RH-Linha-Protheus-GPE-eSocial-S-5001-No-evento-S-5001-e-DCTFWEB-est%C3%A1-aparecendo-o-c%C3%B3digo-19-para-funcion%C3%A1rios-que-recebem-sal%C3%A1rio-maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33715510275095) Tempo aproximado para leitura: 00:02:00 min****Ocorrência**  
No evento S-5001 e DCTFWEB está aparecendo o código 19 (Base de cálculo da contribuição previdenciária exclusiva do empregado) para funcionários que recebem salário maternidade  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**   
Essa alteração ocorre devido a nova nota técnica nº 20/2020 referente a contribuição previdenciária patronal sobre o salário-maternidade.  
  
**Solução**  
Publicado em **01/12/20** a **Nota Técnica nº 20/2020** que tem como objetivo disponibilizar ajustes no layout do eSocial em vigência, para contemplar a decisão do Supremo Tribunal Federal (STF) quanto ao **salário-maternidade**.  
Tal decisão apresentou como inconstitucional a **incidência de contribuição previdenciária patronal sobre o salário-maternidade**, como benefício previdenciário, a verba não está sujeita à contribuição previdenciária patronal que incide sobre a remuneração devida pela empresa aos trabalhadores, que atualmente é de **20% sobre a folha de salários**. Os ajustes desta NT 20/2020 foram implantados no dia**01/12/2020** nos ambientes do **eSocial (governo)** de produção restrita e produção, como o cálculo é aplicado diretamente no ambiente do governo, tal adequação se restringe ao evento S-5001 Informações das Contribuições Sociais por Trabalhador.  
A decisão abrange todas as contribuições patronais (**previdência, RAT e "terceiros"**).   
  
Para efetuar o *download* da nota técnica acesse: [01/12/2020 - Implantação da NT nº 20/2020](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-20-2020.pdf)  
  
O governo irá verificar as verbas com a natureza 4050 (salário maternidade) e 4051 (salário maternidade 13º) e incidências previdenciárias 21 (salário maternidade mensal) e 22 (salário maternidade 13º). E faz o calculo automático do valor patronal sobre o Salario Maternidade. Com a NT 20/2020 o governo não vai mais calcular a **contribuição previdenciária patronal** sobre o **salário-maternidade.**  
  
Conforme *layout* vigente (a partir da nota técnica 20/2020), não será mais retornado no S-5001 o código 11 (Base de cálculo da Contribuição Previdenciária normal) quando o trabalhador possuir incidência para salário maternidade, será retornado no código 19 (Base de cálculo da contribuição previdenciária exclusiva do empregado), isso ocorre devido a mudança da nota técnica 20/2020, ou seja, no GPE (Gestão de Pessoal) não será efetuado nenhum ajuste pois o que foi alterado é somente o retorno no S-5001.  
  
**Novo leiaute S-5001:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33715491904151)  
  
**Antigo Leiaute S-5001:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101345333)  
  
**Exemplo de como será apresentado no eSocial:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000234022)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[DCTFWEB - Orientações NT 20/2020 contribuição previdenciária patronal sobre o salário-maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000054801-RH-Linha-Protheus-GPE-eSocial-DCTFWEB-Orienta%C3%A7%C3%B5es-NT-20-2020-contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-patronal-sobre-o-sal%C3%A1rio-maternidade?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
