---
article_id: 17440776514711
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 78b210ec6c0f2ef001002cd97791e79c187ec6f46833ebbda0cb1c121f926b22
fetched_at: '2026-06-28T22:38:55.677979+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Como configurar
  Controle de Alçada para Solicitação ao Armazém?
type: support-article
updated_at: '2026-03-18T11:58:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17440776514711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Como-configurar-Controle-de-Al%C3%A7ada-para-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

O artigo explica como configurar o Controle de Alçada para aprovação ou rejeição de Solicitações ao Armazém no Protheus, utilizando aprovação por Entidade Contábil. Para isso, deve-se habilitar os parâmetros MV\_ALTPDOC, MV\_APRSAEC e MV\_APROVSA como ".T.", criar grupos de aprovação e utilizar a rotina MATA094 para gerenciar aprovações. O sistema valida permissões e calcula valores dos itens conforme regras específicas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17440753188503) Tempo aproximado para leitura: **00:04:12 min**  
  
**Dúvida**

Como configurar Controle de Alçada para Solicitação ao Armazém para poder aprovar ou rejeitar a S.A?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**Veja nosso vídeo instrutivo sobre como Configurar a Controle de Alçada por Entidade Contábil na Solicitação ao Armazém no Protheus:**

Visando atender os usuários que necessitam aprovar os itens das solicitações ao armazém segregados por entidades contábeis, está disponível no módulo de Compras a aprovação dos itens aglutinados por Entidades Contábeis.

Nele, o usuário criar o modelo de aprovação aglutinado por entidades contábeis para a Solicitação ao Armazém. Esta melhoria permitirá uma melhor segurança na aprovação dos documentos e controle do custo por Entidade Contábil (Centro de Custo, Conta contábil, Item, Classe de Valor, etc.).

Para isso, o usuário deve habilitar a aprovação por entidades contábeis na Solicitação ao Armazém: parâmetros **MV\_ALTPDOC**,  **MV\_APRSAEC** e **MV\_APROVSA** devem estar igual a ".T.".

**Caso o parâmetro MV\_RESTSAC estiver ligado**, ao informar uma entidade contábil para um item da Solicitação ao Armazém (MATA105) o sistema deverá validar se o usuário possui permissão para informá-la, e caso não tenha permissão, o sistema deverá alertá-lo. Para disponibilização da validação será consultada o Cadastro de Solicitantes (MATA084) que deverá ser feita apenas quando habilitado o controle de aprovação das Entidades Contábeis, além disso, deverá ser permitida a inclusão de itens com as Entidades Contábeis em branco.

**Exemplificando em passos:**

***- 1 -*** Habilitar o controle de alçadas por entidade contábil - **Parâmetros MV\_ALTPDOC, MV\_APRSAEC = T e MV\_APROVSA = .T.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21375911567511)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17440662625815)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17440601432983)

***- 2 -*** Criar um Grupo de Aprovação - MATA114 (Exemplo abaixo):

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38389422364951)![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/38389422365847)

***- 3 -*** Com isso, as S.A's para esse Centro de Custos, por exemplo, entrarão sempre para aprovação:

![image 3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38389422367255)

***- 4 -*** Acesse à rotina MATA094 (Aprovação de Documentos). Lá, clique em "Outras Ações" para depois Aprovar ou Rejeitar:

![image 4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38389412936087)![image 4.1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38389422369175)

***- 5 -*** Com isso, a S.A fica rejeitada:

![image 5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38389412938263)

Ao confirmar a Solicitação ao Armazém (MATA105), é realizado o cálculo dos valores dos itens informados na Solicitação, realizando a aglutinação por Entidades Contábeis, considerando o campo de valor total e verificando o rateio por entidades contábeis. (Opção não integrada com o módulo PCO)

Para obter o valor total do item da solicitação é obedecida a seguinte regra na seguinte ordem (a que atender primeiro):

* Prc Estimado da SA (CP\_VUNIT) multiplicado pela Quantidade da SA (CP\_QUANT)
* Verificar o último preço de Compra (B1\_UPRC) e caso não estiver preenchido;
* Verificar o Preço Standard (B1\_CUSTD) e caso não estiver preenchido;
* Custo Médio (B2\_CM1).

**Saiba mais:**

[*Configuração para Controle de Alçadas por Entidade Contábil - Solicitação de Compras e Armazém*](https://tdn.totvs.com/pages/releaseview.action?pageId=284348332)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Solicitação ao Armazém não entra em aprovação por controle de alçada quando não há saldo em estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36093300285847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m-n%C3%A3o-entra-em-aprova%C3%A7%C3%A3o-por-controle-de-al%C3%A7ada-quando-n%C3%A3o-h%C3%A1-saldo-em-estoque)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
