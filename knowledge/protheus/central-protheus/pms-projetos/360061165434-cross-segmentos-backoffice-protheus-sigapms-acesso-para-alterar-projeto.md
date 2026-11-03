---
article_id: 360061165434
category: PMS - Projetos
content_hash: 5ad4a41a13c236874eb97691df17ede0b4093a1eeb84256f586e1a55551442b0
fetched_at: '2026-06-28T22:37:14.854859+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Acesso para Alterar projeto
type: support-article
updated_at: '2024-02-23T11:48:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061165434-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Acesso-para-Alterar-projeto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21563088237591) Tempo aproximado para leitura: 00:03:00 min****Dúvida**Como configurar acesso de usuários no projeto?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.

**Solução**É possível controlar as alterações e manipulações dos projetos, atribuindo direitos de acesso para cada usuário.  
  
Desta forma, podemos definir por exemplo que determinado usuário tenha direitos totais sobre "Solicitações de Compras", porém para documentos do projeto, seu acesso seja somente para visualização.

**OBS**: o usuário que cria o projeto possui automaticamente direito de acesso total a todas as operações desse projeto.

Na rotina de **Gerenciamento Projetos**, é possível atribuir direitos de acesso temporário para cada usuário em determinado projeto.  
  
Existem dois tipos de informações que podem ser visualizadas a partir da referência do projeto:

* **Legenda**: Indica o que significa cada ícone na visualização da estrutura.
* **Fase**: Indica todas as operações e configurações (permitidas ou não) para a fase do projeto.

Para permissão acesse em *Gerenciamento de Projetos* > *Outras Ações* > *Incluir usuário* > *Cód. Usuário* > *Configure*, os direitos dos campos no qual o usuário terá acesso.

Na tela de exemplo a seguir podem-se observar os acessos passíveis de configuração:

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101348814)

Quando os usuários são configurados para alguma tarefa ou EDT, estes ficam na árvore abaixo da EDT/Tarefa a que foram atribuídos.

**Importante:**O campo de acesso ao projeto não é controlado por um parâmetro e vem habilitado como 1.  
Caso queira pode mudar para trazer como desabilitado, alterando o inicializado padrão no campo **AF8\_CTRUSR**.

![af8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406512365079)  
O campo de controle de usuário sempre existiu, e pode ser alterado na inclusão do projeto.

**Saiba Mais**  
Caso gere o Help **PMSUSRNFE** realize o procedimento da documentação: **[Cross Segmentos-TOTVS Backoffice (Linha Protheus) - Gestão de Projetos (SIGAPMS) - Help PMSUSRNFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053795633-MP-PMS-Help-PMSUSRNFE-)**
