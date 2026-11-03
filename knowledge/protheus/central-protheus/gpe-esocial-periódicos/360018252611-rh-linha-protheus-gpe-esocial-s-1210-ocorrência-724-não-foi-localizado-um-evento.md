---
article_id: 360018252611
category: GPE - eSocial - Periódicos
content_hash: 075af4606a273f5e9092831cded0577d4fdf849f8cb7ab0b926051b738f6dba6
fetched_at: '2026-06-28T22:45:07.404799+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - Ocorrência 724: Não foi localizado
  um evento de remuneração do trabalhador para o período e com mesmo demonstrativo
  de pagamento.'
type: support-article
updated_at: '2026-06-24T15:28:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018252611-RH-Linha-Protheus-GPE-eSocial-S-1210-Ocorr%C3%AAncia-724-N%C3%A3o-foi-localizado-um-evento-de-remunera%C3%A7%C3%A3o-do-trabalhador-para-o-per%C3%ADodo-e-com-mesmo-demonstrativo-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27501206833303)Tempo aproximado para leitura: **00:01:00min  
  
Ocorrência**Inconsistências - Ocorrência 724: Não foi localizado um evento de remuneração do trabalhador para o período e com mesmo demonstrativo de pagamento. Ação Sugerida: Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202 ou S-1206 no campo Identificador de Recibo de Pagamento, obedecendo a relação: Se Tipo de Pagamento = [1], em S-1200;.Se Tipo de Pagamento = [5], em S-1202

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27501152220055)

**Causa**Esse retorno ocorre porque não consta o evento remuneratório **(S-1200 ou S-2299**) na base de dados do governo ou o mesmo encontra-se com o tipo de pagamento diferente. Também pode ocorrer quando o campo “**idem Dem Pgt**” não está com o código **idêntico** entre o evento remuneratório **(S-1200 ou S-2299)** e o de pagamento **(S-1210)****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Verifique se o e evento S-1200 ou S-2299 deste trabalhador foi enviado e protocolado pelo RET.  Caso não exista o protocolo deverá ser transmitido ao eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27501206840983)

2. Verifique no evento **S-1200 ou S-2299** se o campo **“idem Dem Pgt**” está com o código **idêntico** ao evento **S-1210**. Importante ressaltar que o evento S-1210 é gerado considerando o fator gerador **data de pagamento**, ou seja tudo que foi pago dentro do período que está sendo gerado será transmitido ao eSocial, podendo em casos de regime de pagamento caixa a informação do evento remuneratório estar no período anterior.   
**Exemplo**: Rejeição ocorre no evento **S-1210** de **09/2024**. Na visualização desse evento consta o recibo da folha de **08/2024** pois foi pago em **05/09/2024**. O campo “idem Dem Pgt” a ser comparado para conferência no evento remuneratório deverá ser do evento **S-1200** do período **08/2024** porque é o da competência que se refere  
  
S-1200

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27501152225047)

S-1210  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27501152226455)

**Saiba Mais**Para saber mais consulte os links abaixo:   
[RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência do RET - 723, 724, 726 no retorno do evento transmitido ao governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024125112-RH-Linha-Protheus-GPE-eSocial-S-1210-Inconsist%C3%AAncia-do-RET-723-724-726-no-retorno-do-evento-transmitido-ao-governo)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
