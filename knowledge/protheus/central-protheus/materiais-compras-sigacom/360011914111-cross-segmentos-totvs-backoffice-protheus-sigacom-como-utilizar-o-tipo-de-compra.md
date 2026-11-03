---
article_id: 360011914111
category: Materiais - Compras (SIGACOM)
content_hash: ce2a8afd3d192a16fe38101b90ae06cc3b31e032d687d882a76e54a103a29b12
fetched_at: '2026-06-28T22:41:07.379502+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Como utilizar o Tipo
  de Compra para alçada ?
type: support-article
updated_at: '2025-01-22T11:48:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011914111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-o-Tipo-de-Compra-para-al%C3%A7ada
---

**Dúvida**MP - SIGACOM - Como utilizar o Tipo de Compra para alçada ?  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

A rotina Tipos de Compra (COMA200) compras tem como objetivo atender as necessidades de classificação dos documentos de alçadas de solicitação de compras e pedidos de compras, assim pode-se definir quais as diretrizes que serão aplicadas, sendo possível realizar o envio de e-mail, alterar ou adicionar um grupo de aprovação ou realizar uma aprovação automática de um pedido de acordo com um percentual de aprovação baseado no documento de alçada vale lembrar que seu uso é opcional. Abaixo alguns exemplos do seu uso.

Exemplo:

Código: 001 Descrição: Grupo de aprovação 001.

![tipo_de_compra.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008585991)

Neste exemplo possui um grupo de aprovação com 3 aprovadores, porém para algumas compras não se quer que seja enviada aprovação para o aprovador 03, para isso foi criado o tipo de compras para determinar que apenas certas compras sejam aprovadas por uma diretoria por exemplo. Caso não seja associada nenhum tipo de compra, o sistema considera que o usuário terá direto de aprovar todos os tipos de compras, caso contrario é necessário apontar quais os tipos de compras são permitidas a aprovação.

## Procedimento para Utilização

       1.           Acesse Atualizações / Administração de Compra / Tipo de Compra (COMA200).

       2.           Acesse a rotina de Tipos de Compra, preencha os seguintes campos:

1. * **Código:**Código do tipo de compras.
   * **Descrição:** Descrição do tipo de compra.
   * **Ordem:** Ordem que será executada a condição do tipo de compra.
   * **Legenda:**Cor da legenda que será exibida no item do documento que foi bloqueado por esse tipo de compra. Será possível visualizar a cor da legenda na visualização do grid do documento que foi bloqueado.
   * **Ativo:** Determina se o cadastro está valido para consulta.
   * **Condições para aplicação**: Fórmula para ser avaliada na utilização do tipo de compra para que no momento da inclusão de uma Solicitação ou Pedido, possa ser avaliada a condição para a classificação do item.  
     Ex. (C1\_QUANT > 12 )
   * **Aprv Especial:**Quando marcado serão considerados os aprovadores que tiverem tipos de compras associados para gerar a aprovação.
   * **Aprov Padrão:** Será efetuada a alçada padrão do sistema considerando apenas os aprovadores que não possuem tipos de compras atrelados. Caso selecione, é marcada automaticamente a aprovação especial, pois é obrigatório o uso em conjunto.
   * **Prazo:** Determina o prazo de vencimento que o aprovador tem para realizar a aprovação do item gerado. O campo prazo é definido em dias.
   * **Aviso:** Determina quantos dias começará a avisar o aprovador de suas pendências. Para a sua utilização, é necessário cadastrar o JOB **SCHEDCOMALC** no ambiente **SIGACFG.**
   * **Escalonar:** Determina se realiza envio de e-mail para o superior imediato, informado no cadastro de aprovador. Para a sua utilização, é necessário cadastrar o JOB **SCHEDCOMALC** no ambiente **SIGACFG.**
   * **Escalona Sup:** Determina se realiza a transferência da pendência para o superior imediato. Para a sua utilização, é necessário cadastrar o JOB **SCHEDCOMALC** no ambiente **SIGACFG.**
   * **Tolerância:**Determina se o tipo de compra utilizará o conceito de tolerância, em relação à solicitação de compra.
   * **%Tole. Dif.:**Determina qual o percentual de tolerância permitida em relação à quantidade da solicitação de compras cadastrada.
   * **Lib Pc c/ Sc:**Opção utilizada para aprovar direto pedidos de compras que tenham solicitação de compras associadas que já passaram por aprovações sem que a quantidade fosse alterada.

Exemplo:

Abaixo é apresentado a configuração do tipo de compras - rotina COMA200 (Tela 1).

![tipo_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008586791)

Tela 1

O exemplo configurado é para quando um pedido de compras for incluso no armazém 02, então este pedido ficará bloqueado e liberado apenas pelo o grupo de aprovação 000006 (Tela 2).

![tipo_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008586811)

 Tela 2

 No cadastro do grupo de aprovação deverá informar o tipo de compra na parte inferior da rotina MATA114 para que o sistema considere o tipo de compra cadastrado.

A mesma configuração vale para a solicitação de compras no controle de alçada onde é informado a fórmula (conforme regra de negócio da empresa) no cadastro de Tipo de Compra - COMA200.

***Obs1:***

A funcionalidade Tipo de Compras funcionará corretamente por itens individualmente, quando o Controle de Alçadas por Entidade Contábil está ativo, ou seja, parâmetro MV\_APRSCEC = T e/ou MV\_APRPCEC = T, bem como Entidade Contábil preenchida no Grupo de Aprovação e Solicitação de Compras e/ou Pedido de Compras com Entidade Contábil preenchida (No mínimo Centro de Custo).  
Caso utilize com a alçada tipo **"PC"**, a regra do tipo de compras deverá ser feita com base nos dados de cabeçalho, pois é gerado 1 regra para todo o pedido de compras (ex. comprador, fornecedor, etc.)

***Obs2:***

Quando incluir um novo Pedido e Solicitação que não apresenta nenhuma regra de Tipo de Compras na linha, a alçada será gerada normalmente para o grupo de aprovação que está utilizando.

**INFORMAÇÕES COMPLEMENTARES:**

* [8 - Tipo de Compra](https://tdn.totvs.com/display/public/PROT/8+-+Tipo+de+Compra)

***Saiba Mais :***

[PCOM09006 - Tipos de Compra (COMA200)](https://tdn.totvs.com/pages/releaseview.action?pageId=267795014)

[Utilização de arquivos para envio de e-mail HTML - Aprovação Documentos](https://tdn.totvs.com/x/UO3hK)

[MP - SIGACOM - Como configurar Controle de Alçadas utilizando Tipo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020735492)

[How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Padrão](https://www.youtube.com/watch?v=WiTxsyeqUKE)

[How To | SIGACOM  -  Tipo de Compras (COMA200): Aprovador Especial](https://www.youtube.com/watch?v=imQf541k9X8)

[PCOM09017 - Tipo de Compras - Campos que podem ser utilizados nas regras](https://tdn.totvs.com/x/hqnKMQ)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Uso de Filtro pela opção "Função" na rotina de Tipo de Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25245405872407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Uso-de-Filtro-pela-op%C3%A7%C3%A3o-Fun%C3%A7%C3%A3o-na-rotina-de-Tipo-de-Compras)

[8 - Tipo de Compra](https://tdn.totvs.com/x/2bptHg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
