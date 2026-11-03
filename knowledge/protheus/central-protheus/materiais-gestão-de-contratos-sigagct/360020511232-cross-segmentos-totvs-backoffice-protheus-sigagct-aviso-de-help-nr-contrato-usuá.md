---
article_id: 360020511232
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: de8fe4e5e8ab5e168d570e8f7d31475515910898784fefff11c19761568e1d0e
fetched_at: '2026-06-28T22:37:19.765830+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Aviso de Help Nr. Contrato
  Usuário sem direitos sobre a transação selecionada na alteração, visualização e
  exclusão da medição do contrato
type: support-article
updated_at: '2024-02-06T14:38:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020511232-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Aviso-de-Help-Nr-Contrato-Usu%C3%A1rio-sem-direitos-sobre-a-transa%C3%A7%C3%A3o-selecionada-na-altera%C3%A7%C3%A3o-visualiza%C3%A7%C3%A3o-e-exclus%C3%A3o-da-medi%C3%A7%C3%A3o-do-contrato
---

**Ocorrência**  
Após migração ou com contratos já migrados, ao visualizar, alterar ou tentar excluir a medição , apresenta o help Usuário sem direitos sobre a transação selecionada.  
Entre em contato com o gestor do contrato

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/13516577069335)**  
**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Causa**   
1 - Uma das possibilidades da mensagem exibida trata-se de contratos que foram migrados e vieram sem o **preenchimento do campo CND\_FILCTR** .

2 -  Pode ocorrer também devido ao **compartilhamento das tabelas do Gestão de Contrato que devem seguir o mesmo padrão.**

3  - Outra Possibilidade a Tabela CPD para o contrato correspondente estar deletada.

4 - Uma analise que pode ser realizada no ambiente, se o contrato foi cadastrado com controle de acesso ativado (CN9\_VLDCTR = Sim), é se as tabelas CNN e CNO estão preenchidas corretamente com as informações do contrato e no que tange a acessos dos usuários.

**Solução**  
Para solucionar essa ocorrência, realize o seguinte passo:  
1. Verifique o conteúdo do campo CND\_FILCTR, se o mesmo estiver em branco é necessário efetuar o preenchimento do campo, cuja alteração deve ser efetuada com analista que tenha conhecimentos em Manipulação de Base;

2. Verifique o compartilhamento das tabelas, conforme tdn abaixo:

**[Compartilhamento de Tabelas - GCT](https://tdn.totvs.com/x/FTMjJw)**

3. Recuperar o Registro deletado da tabela CPD correspondente ao contrato.

4. Se o contrato foi cadastrado com controle de acesso ativado (CN9\_VLDCTR = Sim), o mesmo deve possui registro principalmente na tabela CNN com os vínculos com o usuário e o código de transação contido na tabela CNO, e também os registro da tabela CNO, conforme informações do artigo: [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos?source=search). Caso necessário deve-se realizar a manutenção na base de dados.

***Saiba Mais:***

[GCT0134 - Aviso de Help Usuário sem direitos sobre a transação selecionada na alteração, visualização e exclusão da medição do contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=442044142)

[MP - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-MP-GCT-Qual-tabela-as-rotinas-utilizam-para-realizar-controle-de-acesso-dos-usu%C3%A1rios-ao-contrato-)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
