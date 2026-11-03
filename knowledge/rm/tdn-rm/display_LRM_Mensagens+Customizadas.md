---
content_hash: 7dc76bb854b52f1cc2dcce868dffb10d1924460e680dcb04e04e594ff9bf5d13
fetched_at: '2026-06-29T00:10:04.812444+00:00'
page_id: '452719257'
product: rm
source: tdn-rm
title: Mensagens Customizadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Mensagens+Customizadas
version: 32
---

A mensagem customizada é um recurso do módulo Gestão de Pessoas em que é possível montar uma mensagem customizada para ser enviada ao funcionário.

Esta opção está visível através do módulo Folha de Pagamento acessando 'Configurações >> Comunicação >> Mensagens Customizadas'.   As mensagens criadas serão vinculadas posteriormente, na etapa de 'Envio de E-mail' nos parâmetros do RM-Portal.   Acessar [Parâmetros do RM Portal](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719215)

Ao incluir uma nova mensagem é necessário preencher as seguintes informações:

* Aba de Identificação:  Inserir o código da mensagem e o assunto que será enviado no e-mail. As mesmas variáveis aceitas no corpo do e-mail podem ser utilizadas no assunto.
* Aba Corpo do E-mail:  Inserir o e-mail que será enviado ao funcionário.   O campo de texto é livre e permite a utilização de algumas variáveis para customizar o corpo da mensagem.

Segue as variáveis aceitas:

1. [NomeGestor]: Nome do Gestor do Funcionário;
2. [NomeFuncionario]: Nome do Funcionário;
3. [LinkAcesso]: Link para acesso à página de aprovação de férias (é necessário efetuar o login);
4. [DataInicioGozoFerias]: Data início do gozo de férias;
5. [DataFimGozoFerias]: Data fim do gozo de férias;
6. [TotalDiasFerias]: Número total de dias;
7. [DiasAbonoFerias]: Dias de abono pecuniário;
8. [AntecipacaoPrimeiraParc13]: Pode assumir os valore "Sim" ou "Não", informando se o funcionário solicitou ou não a antecipação da 1ª parcela do 13º salário.

Os e-mails serão formatados como Texto Rico e serão enviados com garantia de compatibilidade de formatação HTML. Os programas leitores/editores de e-mail dependerão de serem compatível com o formato HTML para que as formatações dos textos sejam mantidas. Imagens poderão ser adicionadas ao corpo do texto. Para o envio das imagens, será gerado o link da imagem a partir do ambiente do RM Portal. Para a leitura e abertura da imagem pelo programa leitor de e-mails (Outlook e outros) no corpo da mensagem, dependerá do local da imagem estar público, seguindo permissões do ambiente em que o Portal estiver publicado (em Intranet ou Internet).

Exemplo de mensagem Solicitação de Férias

Assunto: Sugestão de Férias

Corpo do e-mail:

"[NomeGestor], O empregado [NomeFuncionario] acabou de inserir uma sugestão de férias. Para aprová-la ou sugerir um período de férias diferente, acesse o Portal no link abaixo:

[LinkAcesso]

De [DataIncioGozoFerias] a [DataFimGozoFerias], totalizando [TotalDiasFerias] dias.

Abono de [DiasAbonoFerias] dias.

Solicitou antecipação do 13º? [AntecipacaoPrimeiraParc13]"

*O e-mail seria enviado para o gestor com o seguinte conteúdo:*

CLAUDIO LEOPOLDO PRAXEDES,

O empregado RAMON JOSE CAMPOS acabou de inserir uma sugestão de férias. Para aprová-la ou sugerir um período de férias diferente, acesse o Portal no link abaixo:

[https://Corpore.Net/AprovacaoFerias](https://Corpore.Net/AprovacaoFerias.html+_)

De 02/02/2015 a 21/02/2015, totalizando 20 dias.

Abono de 10 dias.

Solicitou antecipação do 13? Sim

**Ações que disparam envio de e-mail**

Atualmente, o envio de e-mails pode ser disparado quando ocorrem as seguintes ações:

1. **Funcionário cadastra sugestão de férias no RM Portal:** quando o funcionário incluir nova sugestão de férias, será disparado o envio de e-mail confirmando a inclusão da sugestão para o funcionário e um e-mail solicitação aprovação para o gestor, caso as mensagens a serem enviadas estejam informadas no [parametrizado do RM Portal](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719215).
2. **Gestor aprova no RM Portal sugestão de férias cadastrada pelo funcionário:** quando o gestor aprovar a sugestão de férias do funcionário no RM Portal, será enviado e-mail informando o fato ao funcionário, caso a mensagem a ser enviada esteja informada no [parametrizado do RM Portal](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719215). Para essa mensagem, são permitidas as variáveis [NomeFuncionario], [DataInicioGozoFerias], [DataFimGozoFerias], [TotalDiasFerias], [DiasAbonoFerias] e [AntecipacaoPrimeiraParc13].
3. **Departamento Pessoal aprova sugestão de férias através do processo "Aprovação de Alt. Cadastrais":** quando o departamento pessoal aprovar a sugestão de férias, será enviado e-mail ao funcionário informando do fato, caso a mensagem a ser enviada esteja informada no [parametrizado do RM Portal](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719215). Para essa mensagem são permitidas as variáveis [NomeFuncionario], [DataInicioGozoFerias], [DataFimGozoFerias], [TotalDiasFerias], [DiasAbonoFerias] e [AntecipacaoPrimeiraParc13].
4. **Gestor/Departamento Pessoal reprova a sugestão de férias do funcionário:** quando o gestor reprovar a sugestão do funcionário através do RM Portal ou o Departamento Pessoal reprovar através do processo de "Aprovação de Alt. Cadastrais", será enviado e-mail para o funcionário informando do ocorrido, caso a mensagem a ser enviada esteja informada no [parametrizado do RM Portal](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719215). Para esta mensagem não é permitido a variável [NomeGestor], pois a mesma mensagem é utilizada para o envio de reprovação do Gestor ou do Departamento Pessoal. Também não é permitido o envio da variável [LinkAcesso], uma vez que a sugestão de férias reprovada será excluída e não estará disponível no Portal para Consulta.
