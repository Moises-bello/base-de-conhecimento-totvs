---
article_id: 4412849694743
category: Meu RH - Férias
content_hash: 15b7ba766d7e6464f8e1b75d21b2f500332d99c8a39f38f9b69cca4d532f3d53
fetched_at: '2026-06-28T22:47:31.686955+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Como customizar a Mensagem para envio de e-mail na solicitação
  de Férias
type: support-article
updated_at: '2026-01-09T18:41:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412849694743-RH-RM-Meu-RH-Como-customizar-a-Mensagem-para-envio-de-e-mail-na-solicita%C3%A7%C3%A3o-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37567098409751) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como customizar a mensagem para o envio de e-mail na solicitação de férias nos Portais?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
A customização da Mensagem deve deve ser realizado em: **Folha de Pagamento | Configurações | Mensagens Customizadas**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412898748055)  
  
Ao clicar em incluir ou editar, no cadastro da mensagem será apresentada a **Aba de Identificação** e **Aba Corpo do E-mail.**

Na **Aba de Identificação**, é possível inserir o código da mensagem e o assunto que será enviado no e-mail. As mesmas variáveis aceitas no corpo do e-mail podem ser utilizadas no assunto.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412851240471)  
  
Na **Aba Corpo de E-mail** deve-se inserir o texto que será enviado ao funcionário. O campo de texto é livre e permite a utilização de algumas variáveis para customizar o corpo da mensagem:  
  
**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412850289047)**  
  
**Segue as variáveis aceitas:**

1. [NomeGestor]: Nome do Gestor do Funcionário;
2. [NomeFuncionario]: Nome do Funcionário;
3. [LinkAcesso]: Link para acesso à página de aprovação de férias (é necessário efetuar o login);
4. [DataInicioGozoFerias]: Data início do gozo de férias;
5. [DataFimGozoFerias]: Data fim do gozo de férias;
6. [TotalDiasFerias]: Número total de dias;
7. [DiasAbonoFerias]: Dias de abono pecuniário;
8. [AntecipacaoPrimeiraParc13]: Pode assumir os valore "Sim" ou "Não", informando se o funcionário solicitou ou não a antecipação da 1ª parcela do 13º salário.

Atentar-se à flag **Envia email na sugestão e aprovação de férias** que se encontra em **Configurações | Parametrizador | RM Portal | E-mail de Férias.** Os campos abaixo é que devem ter vinculados os cadastros de Mensagens Customizadas descritos acima. Caso a flag esteja marcada e nenhum campo for preenchido, será enviado uma mensagem padrão para o funcionário.  
  
**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412832716951)**  
  
Atualmente, o envio de e-mails pode ser disparado quando ocorrem as seguintes ações:

1. **Funcionário cadastra sugestão de férias no RM Portal:** quando o funcionário incluir nova sugestão de férias, será disparado o envio de e-mail confirmando a inclusão da sugestão para o funcionário e um e-mail solicitação aprovação para o gestor.
2. **Gestor aprova no RM Portal sugestão de férias cadastrada pelo funcionário:** quando o gestor aprovar a sugestão de férias do funcionário, será enviado e-mail informando o fato ao funcionário.
3. **Departamento Pessoal aprova sugestão de férias através do processo "Aprovação de Alt. Cadastrais":** quando o departamento pessoal aprovar a sugestão de férias, será enviado e-mail ao funcionário informando do fato.
4. **Gestor/Departamento Pessoal reprova a sugestão de férias do funcionário:** quando o gestor reprovar a sugestão do funcionário ou o Departamento Pessoal reprovar através do processo de "Aprovação de Alt. Cadastrais", será enviado e-mail para o funcionário informando do ocorrido.

**Saiba mais**  
[Mensagem Customizado nas Solicitações de Férias](https://tdn.totvs.com/pages/releaseview.action?pageId=384573071)  
[RH - RM - FOP - Parametrização de Avisos Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024969912-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-de-Avisos-Autom%C3%A1ticos?source=search)
