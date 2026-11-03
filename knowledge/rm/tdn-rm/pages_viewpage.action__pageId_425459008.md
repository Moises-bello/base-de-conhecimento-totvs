---
content_hash: 6751591f157fdbfb967e9fd70a71c528dee7860e3a85b7ec5b03121e4c4fb280
fetched_at: '2026-06-29T00:09:33.387865+00:00'
page_id: '425459008'
product: rm
source: tdn-rm
title: Pesquisa de Satisfação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459008
version: 3
---

**Pesquisa de Satisfação**

A Pesquisa de satisfação é uma forma de o cliente avaliar como ele considerou o atendimento prestado pela empresa com relação a sua solicitação bem como permite que ele escreva, documente algum comentário sobre o caso.  
Esta avaliação e opinião são relatadas pelo cliente através de um formulário/página web (disponibilizada pela empresa que prestou solução à solicitação efetuada) e gravada na base de dados.  
Para responder esta pesquisa o contato por parte do cliente (ambos informados no atendimento) recebe um e-mail informando que o atendimento foi concluído. Neste e-mail consta, além de informações sobre o atendimento, um link (com código que Server para controle de segurança e identificador do atendimento) que ao ser clicado direciona a navegação à página de pesquisa de satisfação do atendimento para que possa ser respondida/preenchida.  
O processo normal de um atendimento até que ele gere a pesquisa de satisfação é:  
1.   O atendimento com a solicitação, cliente e contato do cliente é aberto;  
   
2.   A solicitação é analisada (submetida a processos internos), elaborada uma solução, gravada no atendimento e o mesmo é concluído a responder;  
   
3.   O responsável pelo contato com o cliente o informa sobre a solução e o atendimento é concluído respondido;  
   
4.   Processos internos geram um registro para a pesquisa de satisfação e enviam um e-mail (para o cliente) sobre a conclusão do atendimento e neste um link para responder a pesquisa de satisfação (detalhes no item Regras);  
   
5.   Cliente acessa o link, responde a pesquisa de satisfação e a grava;  
   
6.   Ao gravar, a pesquisa envia um e-mail ao atendente responsável pelo contato com o cliente informando que a pesquisa foi respondida;  
   
7.   Pesquisa de satisfação fica disponível para acesso.  
   
   
Vale ressaltar que a pesquisa de satisfação possui como requisito "alias de base de dados" que direciona a uma base de dados específica. O alias, que direcionará para qual base de dados a funcionalidade acessará, é o que está configurada no arquivo XML "\Corpore.NET\web.config" mais precisamente na chave "ServiceAlias". O resultado da Pesquisa de satisfação - preenchida pelo cliente - pode ser acessado por dentro do atendimento, através na visão e/ou edição do atendimento.   
Na janela de Identificação devem ser informados os seguintes dados:  
Parecer do Cliente: Satisfeito ou Insatisfeito.  
Motivo: Selecione o motivo que levou o cliente a dizer que ficou satisfeito ou insatisfeito.  
Data Alarme: Preenchido automaticamente pelo sistema.  
Comentário: Digite as inferências, opiniões, sugestões e reclamações do cliente ou quaisquer outras observações.  
**Pontos de atenção**  
   
 - Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | pasta Acesso a Menus.

 - O e-mail com o link da pesquisa de satisfação, pode ser um relatório personalizado, para isso, tal relatório deve possuir a tag [PESQUISASATISFACAO] no local desejado, ele também deve ser vinculado ao relatório de conclusão do atendimento, seja no tipo de atendimento ou nos parâmetros gerais do sistema. Outro ponto importante, é que o parâmetro geral: e-mail → Características do e-mail →  Enviar e-mail para o cliente na conclusão do atendimento esteja marcado, caso a conclusão for realizada via fórmula e não deseje que tal parâmetro esteja marcado, outra opção é usar a função CONCLUIDORESPONDIDOCOMEMAIL, nesse caso o e-mail de conclusão seria enviado independente do parâmetro. Vale reforçar que nenhum outra relatório além do de conclusão ira levar o link da pesquisa de satisfação, mesmo se ele possuir a tag adequada.  
**Observação**  
A pesquisa de satisfação pode ser personalizada ou não. Verificar configuração com o administrador.
