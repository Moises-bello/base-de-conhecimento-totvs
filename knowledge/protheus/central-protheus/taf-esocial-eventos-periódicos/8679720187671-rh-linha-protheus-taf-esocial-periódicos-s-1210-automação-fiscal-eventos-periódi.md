---
article_id: 8679720187671
category: TAF - eSocial - Eventos Periódicos
content_hash: 8ce18c33b4f44b87bbe1887f6ad37ebb45032e242d4b25fe8432e2e3340e9283
fetched_at: '2026-06-28T22:45:18.945493+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial  - Periódicos -  S-1210 - Automação Fiscal
  - Eventos Periódicos - Código do erro: 726 Descrição: Nao foi localizado um evento
  de rescisao contratual para o trabalhador com mesmo recibo de pagamento.'
type: support-article
updated_at: '2026-06-25T12:30:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8679720187671-RH-Linha-Protheus-TAF-eSocial-Peri%C3%B3dicos-S-1210-Automa%C3%A7%C3%A3o-Fiscal-Eventos-Peri%C3%B3dicos-C%C3%B3digo-do-erro-726-Descri%C3%A7%C3%A3o-Nao-foi-localizado-um-evento-de-rescisao-contratual-para-o-trabalhador-com-mesmo-recibo-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16335872693783) Tempo aproximado para leitura: **05:00:00 min** **Dúvida**

Ao transmitir para o eSocial o **evento S-1210** , o governo retorna a inconsistência abaixo, erro 726:

*"Código do erro: 726 Descrição: Não foi localizado um evento de rescisão contratual para o trabalhador com mesmo r**ecibo de pagamento**. Ação Sugerida: Deve ser um **identificador de recibo de pagamento atribuído** pela empresa em um dos eventos rescisórios (**S-2299 ou S-2399**), no campo "Identificador de recibo de pagamento". Se Tipo de Pagamento = [2] deve ser um valor atribuído pela empresa em S-2299; Se Tipo de Pagamento = [3], deve ser um valor atribuído pela empresa em S-2399."*

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial- Periódicos - S-1200 - Pagamento de Rendimento do Trabalho (TAFA250) - Todas as Versões

#### 

**Solução**Esta inconsistência ocorre quando o Governo (eSocial) **não encontra** o identificador de pagamento do **S-2299 ou S-2399**;

Observe se no **XML do S-1210** consta tipo de pagamento **2 ou 3**, tag ***<tpPgto>**,* correspondentes á *Pagamento de verbas rescisórias,* o número do identificador de pagamento na tag ***<ideDmDev>*** precisa ser igual ao identificador transmitido no evento S-299 e S-2399, que já se encontra no Portal do eSocial.

*Exemplo das tags no S-1210:*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8678849801751)

Consulte as documentações abaixo, para correção:

[RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência do RET - 723, 724, 726 no retorno do evento transmitido ao governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024125112)

[RH - Linha Protheus - GPE - eSocial - S-1210 - Erro 723 e 726 ao tentar transmitir o evento S-1210 para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420966802583)

[RH - Linha Datasul - eSocial - Erro 726 no envio do S-1210 ao Governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409133039511)

[RH - RM - FOP - eSocial - Validação dos erros 724 e/ou 726 no envio do evento S-1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025168831)
