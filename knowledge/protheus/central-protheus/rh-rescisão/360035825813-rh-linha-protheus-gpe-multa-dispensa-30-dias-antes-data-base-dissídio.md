---
article_id: 360035825813
category: RH - Rescisão
content_hash: bed14062373c1d69a7c3667ad5b358b976502ee7850fc6bd150471a1c39daa24
fetched_at: '2026-06-28T22:43:51.002930+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus -  GPE - Multa dispensa 30 dias antes data base dissídio '
type: support-article
updated_at: '2025-05-20T19:22:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035825813-RH-Linha-Protheus-GPE-Multa-dispensa-30-dias-antes-data-base-diss%C3%ADdio
---

**Dúvida**Como gerar a multa por dispensa 30 dias antes da data base do dissídio?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O empregado dispensado, sem justa causa, no período de 30 (trinta) dias que antecede a data de sua correção salarial, terá direito à indenização adicional equivalente a um salário mensal.  
Desse modo, caso a rescisão do empregado se enquadre na hipótese acima, caberá ao empregador pagar esta indenização adicional, além de todas as verbas rescisórias anteriormente descritas.  
Para isso é necessário realizar as seguintes configurações:

1. Possuir a verba com identificador de cálculo 178 cadastrada em seu cadastro de verbas (GPEA040):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046863913)

2. Informar o mês de dissídio no cadastro de sindicato:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046003914)

**Obs: O campo Mes Dissidio não pode ficar em branco, o mesmo deve ser preenchido.**

3. Na tabela Tipo de rescisão, você deve selecionar o tipo de rescisão utilizado e deixar o conteúdo do campo "Inden. Dissídio" igual a S:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046003934)

Observação: Essa configuração na versão 11 é realizada através da rotina: Definições de calculo/ parâmetro/ 32-Tipos de Rescisão

 O sistema irá considerar sempre a S043 - Tipos de Rescisão quando o Aviso for Indenizado "I", para somar 30 dias à Data de Demissão e quando resultado final desta soma cair exatamente dentro do mês de dissídio definido no sindicato NÃO será pago a multa.

**Exemplo: Mês de Dissídio no Sindicato definido como: 05**Tipo de Rescisão com Aviso Indenizado/ Data de Demissão em 31/03 (31/03 + 30 dias = 30/04) = Neste caso será pago a multa Data de Demissão

Tipo de Rescisão com Aviso Indenizado/ Data de Demissão em 01/04 (01/04 + 30 dias = 01/05) = Neste caso NÃO será pago a multa

**Saiba mais**Para adquirir maior conhecimento acesse os *links* abaixo:

[RH - Linha Protheus - GPE - Como não efetuar pagamento de multa de dissídio em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051963093-RH-Linha-Protheus-GPE-Como-n%C3%A3o-efetuar-pagamento-de-multa-de-diss%C3%ADdio-em-rescis%C3%A3o?source=search)
