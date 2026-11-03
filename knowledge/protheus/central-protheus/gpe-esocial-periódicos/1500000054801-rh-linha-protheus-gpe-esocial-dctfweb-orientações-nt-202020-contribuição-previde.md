---
article_id: 1500000054801
category: GPE - eSocial - Periódicos
content_hash: de6d7a913837782d63baacfa3fcc170948cf4ee13327d0de2602ca2487c0bcc6
fetched_at: '2026-06-28T22:45:07.552344+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - DCTFWEB - Orientações NT 20/2020 contribuição
  previdenciária patronal sobre o salário-maternidade
type: support-article
updated_at: '2025-07-25T15:03:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000054801-RH-Linha-Protheus-GPE-eSocial-DCTFWEB-Orienta%C3%A7%C3%B5es-NT-20-2020-contribui%C3%A7%C3%A3o-previdenci%C3%A1ria-patronal-sobre-o-sal%C3%A1rio-maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33714912524311) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Orientações **Nota Técnica 20/2020** contribuição previdenciária patronal sobre o salário-maternidade.  
A pesquisa pode ser efetuada com os seguintes termos:  
Orientações sobre alteração / mudança no INSS Patronal licença maternidade.  
Houve mudança no INSS patronal de licença maternidade?   
INSS Patronal Salário Maternidade.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Solução**Publicado em **01/12/20** a **Nota Técnica nº 20/2020** que tem como objetivo disponibilizar ajustes no leiaute do eSocial em vigência, para contemplar a decisão do Supremo Tribunal Federal (STF) quanto ao **salário-maternidade**.  
  
Tal decisão apresentou como inconstitucional a **incidência de contribuição previdenciária patronal sobre o salário-maternidade**, como benefício previdenciário, a verba não está sujeita à contribuição previdenciária patronal que incide sobre a remuneração devida pela empresa aos trabalhadores, que atualmente é de **20% sobre a folha de salários**. Os ajustes desta NT 20/2020 foram implantados no dia **01/12/2020** nos ambientes do **eSocial (governo)** de produção restrita e produção, como o cálculo é aplicado diretamente no ambiente do governo, tal adequação se restringe ao evento S-5001 Informações das Contribuições Sociais por Trabalhador.  
  
A decisão abrange todas as contribuições patronais (**previdência, RAT e "terceiros"**).   
  
Fontes:

* [Parecer Consultoria de Segmentos Totvs](https://tdn.totvs.com/pages/releaseview.action?pageId=559286212)
* [Decisão do STF altera forma de cálculo das contribuições previdenciárias sobre Salário Maternidade](https://www.gov.br/esocial/pt-br/noticias/decisao-do-stf-altera-forma-de-calculo-das-contribuicoes-previdenciarias-sobre-salario-maternidade)
* [Implantação da NT nº 20/2020](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-20-2020.pdf)

**1.** O que muda no Protheus? **eSocial:**  
O governo verifica verbas com a **natureza 4050 (salário maternidade) e 4051 (salário maternidade 13º)** e **incidências previdenciárias 21** (salário maternidade mensal) e **22** (salário maternidade 13º). E faz o calculo automático do valor patronal sobre o Salário Maternidade. Com a NT 20/2020 o governo não vai mais calcular a **contribuição previdenciária patronal** sobre o **salário-maternidade.**Foi publicada no eSocial a **[FAQ 3.30](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#4-119--03-12-2020----com-a-recente-decis-o-do-stf--que-declarou-inconstitucional-a-incid-ncia-de-contribui--es-patronais--previd-ncia--rat-e--terceiros---sobre-o-sal-rio-maternidade----necess-rio-fazer-algum-ajuste-na-incid-ncia-da-rubrica-de-sal-rio-maternidade-)** **abaixo** sobre o tema:

**3.30 (26/10/2023)** - Com a recente decisão do STF, que declarou inconstitucional a incidência de contribuições patronais **(Previdência, RAT e “Terceiros”)** sobre o salário-maternidade, é necessário fazer algum ajuste na incidência da rubrica de salário-maternidade?  
  
**Não é necessário alterar a incidência da rubrica referente ao salário-maternidade.**Deve-se continuar utilizando a incidência de contribuição previdência igual a 21 (Salário-maternidade mensal pago pelo Empregador), 22 (Salário-maternidade - 13o Salário, pago pelo Empregador), 25 (Salário maternidade mensal pago pelo INSS) e 26 (Salário maternidade - 13° salário, pago pelo INSS), para que o sistema calcule a contribuição do segurado.  
Foi feita uma alteração no cálculo do eSocial para que as rubricas com **{codIncCP}=[21,22,25,26]** não componham a base de cálculo das contribuições patronais.

A Lei **nº 15.156/2025**, **sancionada em 1º de julho de 2025**, trouxe mudanças importantes na legislação trabalhista e previdenciária, **especialmente para famílias de crianças com deficiência permanente decorrente de síndrome congênita associada à infecção pelo vírus Zika.**Leia mais sobre o tema: [Licença-maternidade e paternidade ampliadas pela Lei nº 15.156/2025: entenda o que muda](https://www.totvs.com/blog/uncategorized/licenca-maternidade-e-paternidade-ampliadas-pela-lei-no-15-156-2025-entenda-o-que-muda/)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
