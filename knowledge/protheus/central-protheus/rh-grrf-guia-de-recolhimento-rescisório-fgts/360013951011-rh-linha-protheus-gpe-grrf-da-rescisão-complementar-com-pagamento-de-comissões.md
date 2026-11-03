---
article_id: 360013951011
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: b04c9a5e86dd0d56110d7dfc18b8959d5ad05eb46b024802c904a2a88c441b49
fetched_at: '2026-06-28T22:43:32.374815+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - GRRF da rescisão complementar com pagamento de
  comissões
type: support-article
updated_at: '2025-10-20T12:25:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013951011-RH-Linha-Protheus-GPE-GRRF-da-rescis%C3%A3o-complementar-com-pagamento-de-comiss%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069822658071) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar a GRRF corretamente da rescisão complementar com pagamento de comissões?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**De acordo com a Circular Nº 450/2008 da Caixa Econômica Federal, o pagamento de **comissões** para **funcionários demitidos**, deve ter o FGTS recolhido através do Sistema Empresa de Recolhimento do FGTS – SEFIP – com código de Movimentação V3. O recolhimento da multa rescisória correspondente, deve ser efetuado por meio da Guia de Recolhimento Rescisório do FGTS – GRRF.

Para que o sistema faça os recolhimentos devidos, é necessário seguir os seguintes procedimentos descritos abaixo:  
  
**Cálculo da Rescisão Complementar**O valor da comissão a ser paga na rescisão complementar deve, obrigatoriamente, ser lançado em uma verba que possua o identificador apropriado de acordo com a necessidade:  
  
**Identificador        Descrição**

0121                      Comissões rescisão

0122                      D.S.R sobre comissões rescisão

**Geração do arquivo GRRF.RE**

Para que o sistema gere o arquivo seguindo esta instrução, é necessário informar nos parâmetros da rotina GPEM680 (GRRF Eletrônica) a pergunta "Tipo de Rescisão" como Complementar e a pergunta "Homologação Dissídio" com a data de pagamento da comissão. Com isso, o sistema irá gerar no arquivo GRRF.RE  o valor da **multa rescisória**, e a data de pagamento que constará no validador da GRRF como dissídio.  
  
Procedimentos para Utilização

1. Acesse o módulo Gestão de Pessoal e selecione a opção "Miscelânea/ Calculo/ Rescisão" (GPEM040);

2. O sistema pergunta se o cálculo refere-se à rescisão complementar, se já houver rescisão calculada, e também exibe uma caixa de checagem para marcar se a rescisão é por dissídio. Neste caso deve ser deixado desmarcado;

3. Lançar o valor da comissão em uma verba que possua o identificador 0121 (Comissão Rescisão) ou 0122 (D.S.R. Sobre Comissão Rescisão). Os dois lançamentos podem ser registrados caso seja pertinente;

4. Confirme o cálculo;

5. Selecione a opção "Miscelânea/ F.G.T.S./ GRRF Eletrônica" (GPEM680);

6. Nos parâmetros da rotina, a pergunta "**Tipo de Rescisão**" deve selecionado Complementar e a pergunta "**Homologação Dissídio**" deve ser preenchida com a data de pagamento da comissão;

7. Confirme a geração da GRRF e verifique o arquivo de LOG gerado;

8. Confira os dados e confirme.  
  
**Saiba Mais**  
[GPE010IMP\_GRRF\_complementar\_comissões](http://tdn.totvs.com/pages/viewpage.action?pageId=224112385)

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
