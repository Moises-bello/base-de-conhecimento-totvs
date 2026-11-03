---
article_id: 360043003714
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 97e780f219de583a6dfbfc99b85028014468be48170c2d3c0814f0bb9141e397
fetched_at: '2026-06-28T22:40:32.343131+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA105 - Alimentar
  campos adicionais na tabela CT2 através das Integrações Contábeis
type: support-article
updated_at: '2025-04-30T14:46:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043003714-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Alimentar-campos-adicionais-na-tabela-CT2-atrav%C3%A9s-das-Integra%C3%A7%C3%B5es-Cont%C3%A1beis
---

**Dúvida**Como faço para alimentar campos adicionais criados na CT2 através das Integrações de Lançamentos Contábeis no Protheus?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
  
**Solução**Para conseguir alimentar os campos adicionais na tabela **CT2** através de integração, basta seguir os passos abaixo:

1- Crie os campos adicionais nas tabelas **CT5, CTK e CT2**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058010734)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058893773)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058011034)

Após a criação dos campos, ainda no configurador, salve as alterações através do disquete:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058894333)

O campo da **CT5**, deve ser do tipo **Caracter**, pois é visto como uma formula no momento da integração, mesmo que o campo da CT2 seja de outro tipo, no exemplo em questão o dado final será numérico.

2- Após isso, alimente o campo adicional do Lançamento Padrão desejado através da rotina **CTBA080**, Exemplo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058011574)

Lembrando que passei os números diretos, pois os meus campos da CTK e CT2 são numéricos, em caso de retorno caractere esse deverá estar entre aspas.

3- Realize a integração do Lançamento Padrão configurado normalmente e veja que o campo será alimentado:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058011754)

**OBS:** Por padrão a alimentação dos campos de forma automática funcionará apenas em lançamentos sem aglutinação, em caso contabilização aglutinada, campos adicionais não serão gravados.

Porém temos o Ponto de Entrada CT105QRY, no qual é possível customizar a regra de aglutinação adicionando os novos campos.  
  
Documentação sobre o ponto de entrada:  
<https://tdn.totvs.com/display/public/PROT/PE+CT105QRY>

**Saiba mais:**<https://tdn.totvs.com/pages/releaseview.action?pageId=342313939#>
