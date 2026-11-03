---
article_id: 360043294453
category: GPE - eSocial - Periódicos
content_hash: 2f172782fa3c6e3ad58ef92bf71027589c639970fbdffa229cac72b1cbb29595
fetched_at: '2026-06-28T22:45:07.693636+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como é gerado e demonstrado
  o dissidio retroativo pago em parcelas no eSocial
type: support-article
updated_at: '2025-05-07T10:49:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043294453-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-%C3%A9-gerado-e-demonstrado-o-dissidio-retroativo-pago-em-parcelas-no-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27049495234839) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como é gerado e demonstrado o dissidio retroativo pago em parcelas no eSocial? **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – Todas as versões  
  
**Solução**Ao calcular o dissidio retroativo no SIGAGPE a geração para folha deve ter o seu lançamento para valores futuros e depois deve ser executados os processos de calculo da folha normalmente. Com isso o **S-1200** de cada mês será gerado considerando os valores parcelados do dissidio na aba "**informações relativas a remuneração do trabalhador em períodos anteriores**".

Segue abaixo um exemplo com *prints* de como as informações são demonstradas na folha e S-1200.

**1. Rotina Dissidio Retroativo:**  
Caminho: *Miscelânea > Reajuste > Dissidio Retroativo*

Print tela de manutenção após o calculo  
*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058418733)*

*Print* tela de geração do dissidio em parcelas:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058418873)

**2. Rotina valores Futuros:**  
Caminho: *Atualizações > Lançamentos> Valores Futuros*

*Print* tela valores futuros demonstrando o total e o valor de cada parcela:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057567054)

**3. Calculo da Folha:**  
Caminho para folha em aberto: *Consultas > Cálculos > Por F**uncionário* Caminho para folha em fechada: **Consultas > Cadastro > Acumulado**

*Print* cálculo da folha com o valor da parcela do dissidio:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058419193)

**S-1200 no módulo SIGATAF:**  
Caminho: *Atualizações > Eventos eSocial > Periódicos > Folha de Pagamento*

*Print* do evento S-1200 01/2020:  
Na aba "**Informações relativas a remuneração do trabalhador em períodos anteriores**" consta no quadro de "**períodos**" todos os meses que ocorreu a diferença de dissidio e mais abaixo em "**itens da remuneração do trabalhador**" consta os valores.

Nessa parte os valores estão parcelados de acordo com cada mês do dissidio.  
  
**Exemplo:**   
No mês **05/2019** o valor do dissidio foi R$ 1.462,50 na verba 112 de salário (vide cálculo dissidio), então o valor da parcela na verba será **R$ 162,50** (R$ 1462,50 / 9 parcelas). Já no mês **10/2019** o valor foi R$ 487,50 então o valor da parcela na verba será **R$ 54,16** (R$ 487,50 / 9 parcelas). A soma do valor de todos os meses que consta no quadro "**períodos**" vai ser igual a parcela da folha de pagamento **01/2019.**Esse processo vai acontecer no S-1200 dos meses seguintes até que seja descontado as 9 parcelas do exemplo utilizado aqui.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058419533)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058419673)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058419753)

**Exemplo Folha 02/2020** veja nos print abaixo que o mesmo conceito para desconto de parcelas no S-1200 vai se repetir.

**1. Rotina valores Futuros:**  
Caminho: *Atualizações > Lançamentos> Valores Futuros*

*Print* tela valores futuros demonstrando o total e o valor de cada parcela:![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057569214)

**2. Cálculo da Folha:**  
Caminho para folha em aberto: *Consultas > Cálculos > Por F**uncionário* Caminho para folha em fechada: *Consultas > Cadastro > Acumulado*

*Print* do cálculo da folha com o valor da segunda parcela do dissidio:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058421913)

**3. S-1200 no módulo SIGATAF:**  
Caminho: *Atualizações > Eventos eSocial > Periódicos > Folha de pagamento*

*Print* do evento S-1200 02/2020:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057569794)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058422573)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058422633)

**Atenção:**Esse documento **não** tem como objetivo de demonstrar como é feita a configuração e cálculo para o dissidio retroativo, caso exista duvidas nesses processos verifique os artigos abaixo:

* [RH - Linha Protheus - GPE - Como parametrizar e calcular o dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-MP-GPE-Manual-do-diss%C3%ADdio-retroativo-?source=search)
* [RH - Linha Protheus - GPE - Como fazer dissidio parcelado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028453332-MP-GPE-Como-fazer-dissidio-parcelado?source=search)
* [RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar informações de dissidio e rescisão complementar por dissidio no esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271-MP-GPE-eSocial-S-1200-Como-gerar-informa%C3%A7%C3%B5es-de-dissidio-e-rescis%C3%A3o-complementar-por-dissidio-no-esocial?source=search)
* [RH - Linha Protheus - GPE - eSocial - S-1200 - Quais verbas serão enviadas para o eSocial nos casos de Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852-MP-GPE-eSocial-S-1200-Quais-verbas-ser%C3%A3o-enviadas-para-o-eSocial-nos-casos-de-Dissidio-Retroativo-?source=search)
* [RH - Linha Protheus - GPE - eSocial - Como o eSocial vai apurar os encargos nos casos de Reajuste/Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342453-MP-GPE-eSocial-Como-o-eSocial-vai-apurar-os-encargos-nos-casos-de-Reajuste-Dissidio-Retroativo?source=search)

**Saiba Mais**Para adquirir mais conhecimento acesse os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página ***[TOTVS Informa](https://informa.totvs.com/)*** selecione em categorias a área e pesquise por "**Eventos**".
