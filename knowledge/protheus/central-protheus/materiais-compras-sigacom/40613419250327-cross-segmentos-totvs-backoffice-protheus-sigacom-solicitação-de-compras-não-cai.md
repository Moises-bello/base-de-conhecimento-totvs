---
article_id: 40613419250327
category: Materiais - Compras (SIGACOM)
content_hash: 2e4af756c27805e60d86a074e36325373babf0114cdb42054a77049932e15bad
fetched_at: '2026-06-28T22:41:25.322891+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Solicitação de compras
  não caiu no Bloqueio de Alçada de Aprovação, o que fazer?
type: support-article
updated_at: '2026-05-20T16:46:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40613419250327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Solicita%C3%A7%C3%A3o-de-compras-n%C3%A3o-caiu-no-Bloqueio-de-Al%C3%A7ada-de-Aprova%C3%A7%C3%A3o-o-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40613419227543) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Mesmo após configurar a alçada de aprovação para a Solicitação de compras, ao incluir a solicitação de compras  cai liberada (legenda verde) sem cair para para aprovação da Alçada (legenda azul), o que é necessário verificar?  
  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**  
A solicitação pode cair liberada , devido alguma configuração faltantes ou incorretas.  
Peço por gentileza que revise a configuração na documentação abaixo correspondente ao processo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alçada de Solicitação de Compras por Entidade Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil)

Após revisar as configurações acima, realize o teste incluindo uma nova Solicitação de compras  para validar se a mesma será bloqueado na Alçada. Se não for, será necessário que realize as validações abaixo.

 **1º passo:** Verifique se os parâmetros estão preenchidos conforme abaixo

MV\_APRSCEC  = .T.

**2º passo:**Verifique se os cadastros abaixo foram realizados:

Cadastro de Aprovadores (MATA095) - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a utilidade do Cadastro de Aprovadores (MATA095)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025179531-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-utilidade-do-Cadastro-de-Aprovadores-MATA095)

Cadastro do Perfil de Aprovação (COMA210) - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Perfis de Aprovação (COMA210)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414660216343-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Perfis-de-Aprova%C3%A7%C3%A3o-COMA210)

Cadastro do Grupo de Aprovação (MATA114) - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Grupos de Aprovação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414195008279-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Grupos-de-Aprova%C3%A7%C3%A3o)

**3º passo:** Verifique se a aba Tipo de Documento do cadastro do Grupo de Aprovação está com a opção **Solicitação de compras** selecionada. Além disso, na Aba "Entidades Contábeis" deve preencher as entidades desejadas.

**Obs:**O preenchimento das entidades contábeis no mínimo Centro de custo é obrigatório para que ocorra o bloqueio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40613422964631)

**4º passo:** Verifique como está preenchido o campo **Valor mínimo do Perfil de aprovação**  vinculado ao aprovador no Grupo de aprovação.

Para que todas as solicitações de compras caiam bloqueadas, o valor Mínimo do Perfil de aprovação vinculado ao aprovador precisa estar com 0,00.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40613422965655)

Caso o **Valor  Mínimo do Perfil de aprovação** vinculado ao aprovador esterja configurado em seu ambiente **igual ou acima  0,01** o sistema verifica se possui valor nos campos valores nos campos abaixo considerando a seguinte ordem:

[PCOM09002 - Configuração para Controle de Alçadas por Entidade Contábil - Solicitação de Compras e Armazém](https://tdn.totvs.com/pages/viewpage.action?pageId=284348332)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40613422967319)

Para obter o valor total do item da solicitação é obedecida a seguinte regra na seguinte ordem (a que atender primeiro):

1. Preço Estimado da SA (CP\_VUNIT) ou Preço Estimado da SC (C1\_VUNIT) multiplicado pela Quantidade da SA (CP\_QUANT) ou da SC (C1\_QUANT);
2. Verificar o último preço de Compra (B1\_UPRC) e caso não estiver preenchido;
3. Verificar o Preço Standard (B1\_CUSTD) e caso não estiver preenchido;
4. Custo Médio do produto (B2\_CM1).

Se nenhum dos campos acima tiver valor preenchido na Solicitação de compras a mesma cairá liberada , caso queira que na aprovação da Solicitação o sistema também valide o valor, será necessário preencher o campo Preço Estimado da SC (C1\_VUNIT) ou um dos campos acima conforme sua necessidade.

**5º passo: Caso queirá considerar o valor no bloqueio da SC conforme passo 4º** Verifique se o valor da Solicitação de compras está dentro do range de valor mínimo e máximo que foram definidos no Perfil de Aprovação. Se no perfil de aprovação por exemplo o valor mínimo for 50 reais até 20000 reais e for incluído uma Solicitação de compras com valor de 2 reais, a solicitação em questão não cairá para aprovação.

**6º passo:**Verifique se os usuários Aprovadores, que estão dentro do Grupo de Aprovação, não estão com os cadastros bloqueados.

**7º passo:** Verifique se a Solicitação de compras foi incluída com as mesmas entidades informadas na aba Entidades Contábeis do Grupo de Aprovação.

***Saiba Mais :***

[Controle de Alçadas - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=270095502)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alçada de Solicitação de Compras por Entidade Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Controle de Alçadas no Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9058852149399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Trilha-de-Videos-Controle-de-Al%C3%A7adas-no-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
