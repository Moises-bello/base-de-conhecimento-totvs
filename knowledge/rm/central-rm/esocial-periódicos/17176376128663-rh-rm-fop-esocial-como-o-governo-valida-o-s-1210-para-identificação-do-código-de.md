---
article_id: 17176376128663
category: esocial - Periódicos
content_hash: 9e994dcee6b9c6e4599bbc18c82eeeaedca9e161138dd06947f5ff60ea4c9a2c
fetched_at: '2026-06-28T22:47:09.221530+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Como o governo valida o S-1210 para identificação
  do Código de Receita relativo ao IRRF de Autônomos Residentes no Exterior - 047301
type: support-article
updated_at: '2026-03-12T00:08:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17176376128663-RH-RM-FOP-eSocial-Como-o-governo-valida-o-S-1210-para-identifica%C3%A7%C3%A3o-do-C%C3%B3digo-de-Receita-relativo-ao-IRRF-de-Aut%C3%B4nomos-Residentes-no-Exterior-047301
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17176319954455) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como o governo valida o S-1210 para identificação do Código de Receita relativo ao IRRF de Autônomos Residentes no Exterior - 047301?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - À partir das versões 12.1.2310.229, 12.1.2402.174, 12.1.2406.105 e Superiores.  
  
**Solução**  
O código de receita **047301 - IRRF - Residentes no exterior, para fins fiscais**é  identificado pelo o governo no evento de retorno S-5002.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17210778934935)**

Para que o governo identifique que o funcionário reside no exterior, é necessário que seja enviado para o eSocial o evento S-1210 com tag **paisResidExt** preenchida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17174037506071)

Para que a tag em questão seja gerada no XML do evento S-1210 é necessário realizar os seguintes passos:

**- Autônomo da Folha de Pagamento**  
1. Identifique o cadastro do funcionário desejado e acesse **Anexos | Folha de pagamento | Dados do Residente ou Domiciliado no Exterior** :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17174314247063)

2. Realize o preenchimento dos campos conforme o cenário do funcionário;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26079751121303)

3. Ao gerar o XML S-1210 a tag **paisResidExt** será gerada no XML com o código do país e o Código da Receita no eSocial ficará **047301 - IRRF - Residentes no exterior, para fins fiscais** após o evento ser aceito pelo RET**.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26079751122839)

**- Autônomo da Gestão Financeira**

1. Acesse o menu Administração de Pessoal | Cliente e Fornecedor | Aba Identificação e preencha as informações do endereço na aba Principal, conforme demonstrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26079751124119)

2. Acesse o menu **Administração de Pessoal | Cliente e Fornecedor | Aba Tributos** e preencha os campos: **Situação do NIF** e **Forma de Tributação**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26079765382039)

3. Ao gerar o XML S-1210 a tag **paisResidExt** será gerada no XML com o código do país e o Código da Receita no eSocial ficará **047301 - IRRF - Residentes no exterior, para fins fiscais** após o evento ser aceito pelo RET**.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26079751131159)

**Importante**  
Necessário conferir se a codificação do País consta conforme [**Tabela 06 - Países do Leiaute do eSocial**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-03-2025/tabelas.html#06)e se foi realizado a configuração de endereço. Para mais informações [**Clique aqui.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007501531-RH-RM-FOP-eSocial-Classifica%C3%A7%C3%A3o-de-pa%C3%ADses-conforme-layout-do-eSocial)

**Saiba mais**  
Para mais informações acesse:   
- [Evento S-1210](https://tdn.totvs.com/display/public/LRM/Evento+S-1210)  
- [Pagamentos a Residentes ou Domiciliados no Exterior](https://tdn.totvs.com/display/public/LRM/FOP_0005_Pagamentos+a+Residentes+ou+Domiciliados+no+Exterior)
