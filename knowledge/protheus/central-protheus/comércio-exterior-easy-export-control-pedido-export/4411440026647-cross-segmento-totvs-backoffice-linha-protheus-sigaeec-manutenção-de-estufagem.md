---
article_id: 4411440026647
category: Comércio Exterior - Easy Export Control - Pedido - Export
content_hash: 8e2c7db14d83a39bc5bd31d7ac706cf37599be01103e431955f8289a7f2b46a5
fetched_at: '2026-06-28T22:36:59.035931+00:00'
product: protheus
section_id: 1500001538181
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Manutenção de
  estufagem
type: support-article
updated_at: '2022-12-27T14:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411440026647-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Manuten%C3%A7%C3%A3o-de-estufagem
---

**Dúvida**Como realizar a manutenção de estufagem?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.   
  
**Solução**Pré-Requisito  
Para executar a nova rotina de Estufagem é imprescindível a configuração dos parâmetros abaixo:

* **MV\_AVG0005** - Desativar botão volume e gravação embalagens do Processo e

Embarque (este parâmetro deve ser marcado como Falso - .F.);

* **MV\_AVG0146** - Habilita a nova rotina de estufagem no SIGAEEC(este parâmetro deve ser marcado com Verdadeiro - .T.).

**Como será utilizado a embalagem no processo:**

* No Pedido de Exportação (EECAP100) , preencha os dados da capa do processo e clique em Outras ações→ Incluir para inclusão de um item para o pedido.
* Preencha os dados dos itens informando a quantidade, informe uma embalagem e no campo "Qt. de Embal.(EE8\_QTDEM1)" informe um campo que não seja múltiplo pela quantidade na embalagem que o sistema irá validar a informação.

![](https://tdn.totvs.com/download/attachments/235310803/image2019-2-1_12-5-26.png?version=1&modificationDate=1549033527050&api=v2)

Obs: o mesmo procedimento ocorre para a fase de embarque apenas com a mudança para o campo "Qt. de Embal(EE9\_QTEEM1).  
  
**Estufagem**  
Para realizar a estufagem é necessário que tenha efetuado o cadastro da embalagem junto com as devidas amarrações entre as embalagens e também o embarque.

Veja um exemplo, baseando-se que no item do embarque foram colocadas as seguintes informações:

|  |  |  |  |
| --- | --- | --- | --- |
| **Embalagem Final na capa do processo** | --------- | **Embalagem Final na capa do processo** | --------- |
| Item | 01 | Item | 02 |
| Quantidade | 4000 | Quantidade | 500 |
| Embalagem | Caixa de papelão | Embalagem | Caixa de Madeira (Com peso zero) |
| Quantidade na Embalagem | 200 | Quantidade na Embalagem | 10 |
| Quantidade de Embalagem | 20 | Quantidade de Embalagem | 50 |

**Exemplo – Manutenção da Estufagem:**

1. Selecione o menu “Atualizações\ Embarque\ Manutenção”.
2. Selecione o processo desejado, clique no botão “Ações Relacionadas” e clique na opção “Estufagem”.
3. De acordo com o exemplo citado acima, abaixo a estrutura da estufagem.
4. Clique em “Confirmar”.

A estufagem de mercadorias é dividida por: “Mercadorias não estufadas” e “Mercadorias estufadas”, onde:

- “Mercadorias não estufadas” à São as mercadorias que ainda não foram estufadas no *container*, nesta parte o sistema separa as embalagens de acordo com o item do processo, a embalagem utilizada com suas respectivas quantidades. Isso de acordo com a amarração efetuada no cadastro de embalagens.

- “Mercadorias Estufadas” à São as mercadorias que já foram estufadas no *container,*após a notificação do agente embarcador de quantos *containers* serão utilizados, o sistema separa corretamente quantas embalagens vão dentro de cada *container*mencionado.

No botão “Ações Relacionadas” temos as seguintes opções*:*

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411444825367/mceclip0.png)*

1. Clique no botão “Incluir”.
2. Selecione a opção *“Container”,* abrira uma nova tela para informar os dados do container.
3. Na manutenção, o campo “No. *Container*” a numeração aparece em sequência, podendo ser alterado quando necessário.
4. Em seguida, clique no botão “Confirmar”.
5. Ao confirmar o *container* cadastrado os dados aparecerão na parte “Mercadorias Estufadas”.
6. Para mover o produto “Parafuso” para dentro do *container*, clique na embalagem 01-pallet.
7. Em seguida, no botão “Ações Relacionadas”, pressione a opção “Mover De”.
8. Caso queria controlar o saldo preencha os valores desejados, após isso confirme. Caso contrário deixe em branco.
9. Depois selecione o *Container* desejado e pressione o botão “Ações Relacionadas”, em seguida em “Mover Para”.
10. Note que a embalagem movida aparecerá dentro do *container* na parte “mercadorias estufadas”.
11. Para remover a embalagem do *container*, efetue os mesmos passos anteriores.
12. Imaginando que foi removido a embalagem do *container*, ou que todas as embalagens estão na parte “Mercadorias não estufadas”.
13. Em “Ações Relacionadas”, clique no botão “Wizard”, para realizar os dados da estufagem automaticamente, aparecerá à seguinte tela:
14. Nesta tela, clique na opção avançar.
15. Nesta tela preencha o tipo do *container*desejado e clique na opção avançar.
16. Informe a quantidade de *container* que será necessário para a estufagem e clique na opção avançar.
17. Nesta tela informe quantas caixas de madeira e quantos pallets irão dentro de cada container. Em seguida clique na opção avançar.
18. Informe se será utilizada a rotina de controle de lotes, caso queira deixe a opção como “Sim”, caso contrário, deixe como “Não”. E em seguida clique na opção avançar. Neste exemplo deixe a opção como “Não”.
19. Em seguida clique na opção “Finalizar”.
20. Ao clicar em “Finalizar”, automaticamente os produtos respectivamente com suas embalagens são transferidos para “Mercadorias Estufadas”.
21. No botão “Ações Relacionadas” utilize as opções “Alterar” e “Excluir” para a manutenção dos *containers*.
22. Caso no processo não tenha a embalagem “Pallet” na parte de “Mercadorias Estufadas”, é possível fazer alteração selecionando a embalagem a qual precisa ser palletizada. Clique em “Ações Relacionadas” e utilize a opção “Alterar”.
23. Marque o tipo de Embalagem como “Pallet”. Em seguida a imagem da embalagem que era como “”, será substituída pela imagem “” pallet.
24. Selecione o container, clique no botão “Ações Relacionadas” e utilize o botão “Alterar”, para informar o número correto do container e também outras informações.
25. Caso tenha que alterar o(s) item(s) do processo, é necessário que não tenha preenchido o campo data do embarque e que não tenha nenhuma mercadoria estufada.
26. Para incluir uma embalagem manualmente em “Mercadorias Estufadas”, selecione um container ou uma embalagem e clique em “Ações Relacionadas”, depois no botão “Incluir”, onde aparecerá a seguinte tela:
27. Selecione a opção “Embalagem”, onde será exibida a tela se seleção de Embalagens.
28. Clique em “Confirmar” e a embalagem será incluída conforme a seguir.
29. Clique sobre o botão “Confirmar” para gravar a estufagem.
30. Ao preencher o campo “Data de Embarque” no processo, não é possível realizar nenhuma manutenção e/ou alteração na rotina estufagem. Para utilizar a rotina estufagem, retire a data do embarque.
31. Ao informar o(s) item(s) do pedido, os mesmos não poderão ser modificados.

**Saiba mais**   
[EEC0003\_Manutenção\_de\_Estufagem\_e\_Embalagem](https://tdn.totvs.com/pages/viewpage.action?pageId=235310803)

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Cadastro de embalagem (EECAT170)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411439477271)
