---
article_id: 6330508276759
category: Funcionários
content_hash: e650efe864398851405b14fa080b980102558ceef80d38203838770748dc1f4c
fetched_at: '2026-06-28T22:47:03.307931+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: 'RH - RM - FOP - Erro ao abrir cadastro de funcionários ORA-01013: o usuário
  solicitou o cancelamento da operação atual '
type: support-article
updated_at: '2025-03-12T10:51:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6330508276759-RH-RM-FOP-Erro-ao-abrir-cadastro-de-funcion%C3%A1rios-ORA-01013-o-usu%C3%A1rio-solicitou-o-cancelamento-da-opera%C3%A7%C3%A3o-atual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:40 min****Dúvida**Como realizar a correção do erro ORA-01013: o usuário solicitou o cancelamento da operação atual, ao realizar a abertura da tela do cadastro do funcionário?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6330141576343/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a correção do erro apresentado é necessário abrir o cadastro da pessoa vinculado ao funcionário,  remover a foto IDIMAGEM, e depois importar a foto novamente.  
Pode ser que o erro aconteça a um funcionário específico somente, ou em todos.  
O erro retorna pois a Foto pode ter corrompido quando feito o upload, ou sido corrompida em alguma transação do banco.  
Você pode verificar realizando alterações via banco de dados, Update no campo IDIMAGEM da tabela PPESSOA, para que  o acesso ao cadastro do funcionário seja restabelecido ou removendo e importando a foto novamente como citado anteriormente, mas é de suma importância que antes do processo seja  identificada a chapa problemática.  
  
**Saiba mais**Para auxílio na importação da foto do colaborador, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011041251)
