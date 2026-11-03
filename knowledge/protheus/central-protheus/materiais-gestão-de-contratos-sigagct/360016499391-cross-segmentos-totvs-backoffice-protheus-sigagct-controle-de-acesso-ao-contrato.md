---
article_id: 360016499391
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 6b6bdb216788e0340a47d8655345cffd75c63261aa9b9fc3e5f7440023359619
fetched_at: '2026-06-28T22:37:21.726435+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Controle de Acesso
  ao contrato no Gestão de Contratos e Medição em outras Filiais
type: support-article
updated_at: '2026-06-18T13:51:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos-e-Medi%C3%A7%C3%A3o-em-outras-Filiais
---

**Dúvida**  
Controle de Acesso ao Contrato no Gestão de Contratos e Medição de Contratos em Filiais diferentes do cadastro do contrato

**Ambiente**

Cross Segmentos - Totvs Backoffice Protheus - Gestão de Contratos - A partir da versão 12.1.17

**Solução**

Na inclusão do contrato, as permissões de **Controle Total** são gravadas para o usuário responsável pela inclusão do contrato, onde para inclusão de outros usuários com permissão, deverá ter acesso pelo botão **Acessos** com login do responsável pela inclusão, sendo definido novo usuário com acesso. Segue abaixo Como conceder/retirar permissão de acesso a um contrato.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101493514)

Ao incluir determinado contrato, o usuário responsável pela inclusão torna-se proprietário do contrato, onde para que outros usuários tenham permissão para realizar alguma operação no contrato, o usuário proprietário deverá na rotina **Contratos** no botão **Acessos** incluir novo usuário e definir os níveis de acesso para este novo usuário.

O conceito presente na rotina visa validar que as informações dos contratos estejam disponíveis para qualquer usuário, realizando esse processo visando criar um nível de segurança no processo, onde as tabelas onde são armazenadas as configurações de acesso trata-se das tabelas: **CNN** e **CNO**.

A rotina disponibiliza campo para que seja definido se o conceito acima será utilizado, para que o usuário controle o acesso aos contratos e modifique-os:

Campo: CN9\_VLDCTR  
Tipo: Caracter  
Tamanho: 1  
Decimal  
Formato: @!  
Título Vl.Cont: S/N  
Descrição: Validação de Contrato  
Nível: 1  
Usado: Sim  
Obrigatório: Não  
Browse: Sim

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404263875863)

Para o controle dos acessos dos usuários aos contratos, as rotinas utilizam a tabela CNN.  
  
Na tabela Amarração Usuário X Contrato\Campos (CNN) existe o campo Transação (CNN\_TRACOD), este campo armazena um código que tem origem na tabela Transações X CNO.  
  
Este código representa qual ação(ões) o usuário poderá realizar para o contrato.  
  
Exemplo: Transação (CNN\_TRACOD) = 001 - Controle Total

Segue abaixo as opções disponíveis para configurar os acessos de usuários em "Outras Ações > Acesso", dentro da visualização do contrato na rotina de Manutenção (CNTA300):

**1- Incluir usuário**

Para incluir um usuário, deve posicionar o cursor no item correspondente ao usuário e pressionar o botão direito do mouse, após isso a opção de incluir usuário será habilitada:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404261044119)

**2- Editar ou excluir usuário:**

Para editar/excluir um usuário de um determinado usuário, deve-se posicionar em cima do usuário desejado, ativar o menu através do botão direito do mouse, apos isso as opções de editar/excluir serão habilitadas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5400412273559)

**3- Incluir grupo:**

Para incluir um novo grupo de usuários(Grupo de acesso atrelado ao usuário no configurador do sistema), o processo é igual ao do usuário, deve-se posicionar em cima do item referente a grupos e pressionar o botão direito do mouse.

![](https://tdn.totvs.com/download/attachments/344477072/image2018-3-14_14-57-3.png?version=1&modificationDate=1521050222000&api=v2)

**4- Editar ou excluir grupo:**

Para editar/excluir um grupo o processo é o mesmo, posicionar em cima do grupo desejado e acionar as opões através do botão direito do mouse.

![](https://tdn.totvs.com/download/attachments/344477072/image2018-3-14_14-59-22.png?version=1&modificationDate=1521050360000&api=v2)

**5- Opção para Autorizar Medição em Outras Filiais:**

Neste opção é possível permitir que um contrato cadastrado em determinado Filial, posso ser medido, ou ser incluída uma medição para este contrato, em um Filial diferente da que ele foi cadastrado, por exemplo, para um contrato que foi cadastrado para a Matriz, podem ser realizadas medições nas Filiais da empresa diferentes da que ele foi cadastrado.

Dessa forma, verifique que na parte inferior da tela na opção de "Acessos" que é possível também autorizar a realização de Medição em outras Filiais diferentes da Filial que o Contrato é cadastrado.

Quando é dado acesso a medição em uma outra Filial, é criado registro para o contrato para esta Filial na tabela CPD (Amarração Filial x Contrato) e caso seja retirado o acesso é deletado o registro nesta tabela.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9648991481367)

Posicione o cursor na planilha e pressione o botão direito do mouse

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416745800855)

Será disponibilizado a opção de Incluir Filial

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416753992087)

Será apresentada a tela abaixo, para incluir a filial desejada

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416753999511)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416754005015)

Selecione e clique em Salvar

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416738311447)

***Obs1:***

Quando um contrato é cadastrado com a funcionalidade de Controle de Acesso desabilitada (CN9\_VLDCTR = 2-Não), não se consegue para este contrato realizar medições em outras Filiais do sistema diferentes da que ele foi incluído originalmente.

***Obs2:***

O controle de acesso ocorre somente por **contrato selecionado,** ou seja , não é possível selecionar vários contratos para aplicar o controle de acesso.

***Obs3:***

O campo CN9\_VLDCTR só pode ser alterado quando Quando o contrato estiver sendo incluído ou a situação do contrato ainda estiver em Elaboração. Via revisões não é permitido alterar o campo.

***Obs4:***

Somente os contratos que possuem o Controle de acesso ativo (CN9\_VLDCTR = 1) terão registros incluídos na tabela CNN.

***Obs5:***

Para situações desejadas em que o usuário que elabora o contrato, não será o mesmo que realiza a medição segue abaixo:

O usuário que incluiu o contrato, possui acesso total no contrato e em todas as movimentações realizadas no contrato. Pelo menos um usuário precisar ter acesso a todas as movimentações do contrato.  
   
Uma possibilidade é configurar todos os acessos para o usuário que incluiu o contrato, exceto medições por exemplo e incluir um segundo usuário na seção de controle de acessos ao contrato para que possa ter acesso as medições.

***Obs6:***

Como possar dar acesso em lote de vários contratos para um usuário?

**R:** Atualmente não é possível realizar configuração ou ajuste de controle de acessos de contratos em lote ou em massa, mas somente para um único contrato por vez.

***Obs7:***

Somente quem criou o contrato pode dar o acesso ao mesmo? O usuário Admin não consegue?

**R:** Caso o campo CN9\_VLCTR esteja igual a "Sim", é criado um registro na tabela CNN apenas para o usuário que incluiu o contrato. Dessa forma o usuário "Admin" não terá acesso ao contrato, e somente o usuário que incluiu o contrato poderá conceder acesso aos demais usuários do sistema.

***Saiba Mais:***  
[GCT0102 - Aviso de Help CNNOTRANS ao realizar a Medição](http://tdn.totvs.com/pages/releaseview.action?pageId=318606402)

[GCT0037\_Medição\_de\_Contrato\_Por\_Filiais\_Distintas\_versão\_P12\_(SIGAGCT)](https://tdn.totvs.com/pages/releaseview.action?pageId=244424228)

[Exemplos da habilitação conforme posicionamento dentro da rotina de controle de acessos da Manutenção de Contratos](https://tdn.totvs.com/pages/releaseview.action?pageId=344477072)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
