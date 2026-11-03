---
article_id: 360017527952
category: Materiais - Compras (SIGACOM)
content_hash: ffeb6c159952f6008cb11a366df2f340d29f1992e127122013887e3af77b5667
fetched_at: '2026-06-28T22:41:07.406898+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alçada de Solicitação
  de Compras por Entidade Contábil
type: support-article
updated_at: '2026-05-18T15:30:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil
---

**Dúvida**  
Alçada de Solicitação de Compras por Entidade Contábil

**Ambiente**  
Protheus – Compras – A partir da versão P12.1.17   
  
**Solução**

Para que haja o Bloqueio para Aprovação de Alçadas de Solicitações de Compras, deve-se realizar os seguintes passos:

1. Preencha o preço Prc Estimado da SC **(C1\_VUNIT)** ou no cadastro do produto colocar informações no campo (**B1\_UPRC**) informando o último preço de compra;  
2. Configurar os parâmetros (**MV\_APRSCEC = T**) para habilitar a alçada por entidade contábil e o (**MV\_ALTPDOC = T)** para habilitar a aba "Tipo Documentos" na rotina de Grupo de Aprovação;  
3. No cadastro de grupo de aprovação configurar o **perfil de aprovação** e as demais informações do Aprovador informado;  
4. Continuando, no cadastro do grupo de aprovação, na aba "**Tipo de Documentos**" possuir "flegado" a opção "Sol Compras", e na aba "**Entidades Contábeis"** informar o *centro de custo* desejado para esta alçada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18889071086999)

5. Incluir a solicitação de compras (**MATA110**) , informar o *centro de custo* que foi infomrado no Grupo de Aprovação e salvar a solicitação de compras, onde ao confirmar, ela muda a **legenda** para "*cinza"* de bloqueado, conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34342581241367)

Após incluida a SC que entrou no processo de alçada, pode-se verificar a alçada de liberação da SC com os "aprovadores" envolvidos e a "situação atual" de cada aprovador, na visualização da SC, através da opção "Outras Ações - Log Aprov":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34342596131991)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34342596133655)

Assistam nosso vídeo com a configuração.

How To| MP-SIGACOM Alçada Por EC Para SC Na Prática #TOTVS Backoffice (linha Protheus) <https://www.youtube.com/watch?v=t83xSE2c98Q>

**Obs1:**

Caso o valor do Perfil de aprovação estiver configurado com Valor Mínimo 0,00 não será necessário informar valores nos campos **C1\_VUNIT e B1\_UPRC** informados no Passo 1 acima, visto que o Perfil com este valor mínimo 0,00, abrangerá o valor 0,00 dos campos **C1\_VUNIT e B1\_UPRC** que não sejam informados.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414484367895)

A consideração de valores referente a alçada da Soclicitação de Compras tem seu funcionamento conforme reporta o artigo abaixo:

[PCOM09002 - Configuração para Controle de Alçadas por Entidade Contábil - Solicitação de Compras e Armazém](https://tdn.totvs.com/pages/viewpage.action?pageId=284348332)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31870444731159)

Para obter o valor total do item da solicitação é obedecida a seguinte regra na seguinte ordem (a que atender primeiro):

1. Preço Estimado da SA (CP\_VUNIT) ou Preço Estimado da SC (C1\_VUNIT) multiplicado pela Quantidade da SA (CP\_QUANT) ou da SC (C1\_QUANT);
2. Verificar o último preço de Compra (B1\_UPRC) e caso não estiver preenchido;
3. Verificar o Preço Standard (B1\_CUSTD) e caso não estiver preenchido;
4. Custo Médio do produto (B2\_CM1).

**Obs2**:

Para que a Solicitação de Compras seja apresentada na rotina de Liberação de Documentos **(MATA094)** é necessário que o parâmetro **MV\_APRSCEC** esteja habilitado como .T., ou seja, não é possível a utilização da Alçada na Solicitação de Compras que não seja "Por Entidades Contabeis".

***Obs3:***

Para que a SC entre na alçada, além de todas as demais configurações, ao incluir a SC, a combinação das Entidades Contabeis (C.Custo+Cta.Contabil+Classe Valor+Item Contabil) existentes na SC deve ser igual à combinação das Entidades Contabeis contidas no Grupo de Aprovação cadastrado.

***Obs4:***

Para que a aprovação de solicitação de compra pelo grupo de aprovação seja feita pela rotina Liberação de Documentos (MATA094), é obrigatório utilizar a configuração de Alçada de Bloqueio Por Entidade Contábil para a Solicitação de Compra. Seguindo o procedimento desta documentação. Se utilizar o Bloqueio de Alçada Simples na Solicitação de Compras, ela deverá ser aprovada na própria rotina de Solicitação de Compras.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Controle de Alçadas no Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9058852149399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Trilha-de-Videos-Controle-de-Al%C3%A7adas-no-Compras?source=search)

[PCOM09012 - Configuração alçada versão 12.1.14, 12.1.16 e 12.1.17](http://tdn.totvs.com/pages/viewpage.action?pageId=286209197)

[PCOM09002 - Configuração para Controle de Alçadas por Entidade Contábil - Solicitação de Compras e Armazém](https://tdn.totvs.com/pages/viewpage.action?pageId=284348332)

[Controle de Alçadas - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=270095502)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
