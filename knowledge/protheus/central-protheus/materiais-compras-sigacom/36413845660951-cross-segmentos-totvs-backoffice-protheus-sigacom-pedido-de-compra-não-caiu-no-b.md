---
article_id: 36413845660951
category: Materiais - Compras (SIGACOM)
content_hash: ee6b6952c97b8554f9d58cfd9404089c1f4d55508b0956176c29fa9967b7b972
fetched_at: '2026-06-28T22:41:22.076431+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pedido de Compra não
  caiu no Bloqueio de Alçada de Aprovação, o que fazer?
type: support-article
updated_at: '2026-05-18T13:45:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36413845660951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pedido-de-Compra-n%C3%A3o-caiu-no-Bloqueio-de-Al%C3%A7ada-de-Aprova%C3%A7%C3%A3o-o-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36413845643543) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Mesmo após configurar a alçada de aprovação para o Pedido de Compra, ao incluir o Pedido ele cai liberado (legenda verde) sem cair para para aprovação da Alçada (legenda azul), o que é necessário verificar?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 12.

**Solução**  
Na maioria das vezes, o Pedido de Compra não cai para aprovação pois há alguma configuração incorreta ou incompleta. Mediante isso, por gentileza, revise a configuração na documentação abaixo correspondente ao processo que utilizará.

Caso for utilizar a Alçada Padrão:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o Controle de Alçadas Padrão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006822671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-Controle-de-Al%C3%A7adas-Padr%C3%A3o)

Caso for utilizar a Alçada por Entidades Contábeis:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar a Alçada por item de pedido e entidade contábil ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823411-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-a-Al%C3%A7ada-por-item-de-pedido-e-entidade-cont%C3%A1bil)

Após revisar essas configurações, realize o teste incluindo um novo Pedido de Compra para validar se ele será bloqueado na Alçada. Se não for, será necessário que realize as validações abaixo.

**1º passo:** Verifique se os parâmetros estão preenchidos conforme abaixo

MV\_ALTPDOC  = .T.

**Alçada padrão:**

MV\_PCAPROV = código do cadastro do grupo de aprovação *(exemplo 000001)*

**Alçada por Entidade contábil:**

Se for Alçada por entidade contábil, verifique se o parâmetro **MV\_APRPCEC** está habilitado.

**2º passo:** Verifique se os cadastros abaixo foram realizados:

Cadastro de Aprovadores (MATA095) - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a utilidade do Cadastro de Aprovadores (MATA095)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025179531-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-utilidade-do-Cadastro-de-Aprovadores-MATA095)

Cadastro do Perfil de Aprovação (COMA210) - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Perfis de Aprovação (COMA210)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414660216343-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Perfis-de-Aprova%C3%A7%C3%A3o-COMA210)

Cadastro do Grupo de Aprovação (MATA114) - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Grupos de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414195008279-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Grupos-de-Aprova%C3%A7%C3%A3o)

**Se for alçada padrão pelo total do pedido, verifique por gentileza se possui grupo de aprovação atrelado no cadastro do comprador.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40552536615191)

Cadastro dos Compradores (COMA087) - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que é o Cadastro de Compradores MATA087 / COMA087 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024650292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-%C3%A9-o-Cadastro-de-Compradores-MATA087-COMA087)

**3º passo:** Verifique se a aba Tipo de Documento do cadastro do Grupo de Aprovação está com uma opção selecionada.

Se for utilizar **alçada padrão**, deve flegar a opção Pedido de Compra.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40552526499991)

Se for utilizar **alçada por entidade contábi**l, deve flegar a opção Item Pedido. Além disso, na Aba "Entidades Contábeis" deve preencher as entidades desejadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40552526501399)

**4º passo:** Verifique se o valor do Pedido de Compras está dentro do range de valor mínimo e máximo que foram definidos no Perfil de Aprovação. Se no perfil de aprovação do valor mínimo for 50 reais até 20000 reais e for incluído um Pedido de Compra com valor de 2 reais, o pedido em questão não cairá para aprovação.

**5º passo:** Verifique qual é a origem do Pedido de Compras, ou seja, através de qual rotina ele foi incluído. Por exemplo, através da análise da Cotação do Novo Fluxo de Compras. Mapeie se o pedido é incluído liberado apenas no NFC ou se ele também nasce liberado quando é incluído manualmente na rotina Pedido de Compras.

Para maiores informações sobre a Alçada de Aprovação quando o pedido é gerado através do Novo Fluxo de Compras, verifique a documentação abaixo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Alçada para Pedido de Compras gerado via Cotação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35931525407383-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Al%C3%A7ada-para-Pedido-de-Compras-gerado-via-Cota%C3%A7%C3%A3o)

**6º passo:** Verifique se os usuários Aprovadores, que estão dentro do Grupo de Aprovação, não estão com os cadastros bloqueados.

**7º passo:** No caso da alçada por Entidade Contábil, verifique se o Pedido de Compra foi incluído com as mesmas entidades informadas na aba Entidades Contábeis do Grupo de Aprovação.

***Saiba Mais :***

[Controle de Alçadas - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=270095502)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar o Controle de Alçadas Padrão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006822671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-o-Controle-de-Al%C3%A7adas-Padr%C3%A3o)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como configurar a Alçada por item de pedido e entidade contábil ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823411-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-configurar-a-Al%C3%A7ada-por-item-de-pedido-e-entidade-cont%C3%A1bil)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Controle de Alçadas no Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9058852149399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Trilha-de-Videos-Controle-de-Al%C3%A7adas-no-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
