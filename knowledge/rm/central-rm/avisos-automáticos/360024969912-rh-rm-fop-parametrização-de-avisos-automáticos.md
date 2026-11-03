---
article_id: 360024969912
category: Avisos Automáticos
content_hash: 97ad8ddfb05df70576ea75e429c7b34be5c37eab8a1f64d749165236ad6a5512
fetched_at: '2026-06-28T22:46:40.535287+00:00'
product: rm
section_id: 31224122282519
source: central-rm
title: RH - RM - FOP - Parametrização de Avisos Automáticos
type: support-article
updated_at: '2025-04-07T13:57:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024969912-RH-RM-FOP-Parametriza%C3%A7%C3%A3o-de-Avisos-Autom%C3%A1ticos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29613667854615) Tempo aproximado para leitura: **00:08:30 min  
  
Dúvida**Como parametrizar Avisos Automáticos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a parametrização de avisos automáticos no TOTVS Folha de Pagamento, siga os passos descritos abaixo:  
  
1. No cadastro dos usuários do aplicativo, meu **Serviços Globais | Segurança | Usuários | aba Identificação**, no campo **E-Mail** deve ser informado o endereço eletrônico do destinatário que receberá a mensagem:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023724071)  
  
2. Parametrização do servidor de e-mails pelo menu **Ambiente| Parâmetros | Globais | aba Envio de E-mails.** Os dados da imagem são fictícios:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023687212)  
  
**Parâmetros da Coligada Atual:**Informe os dados para os parâmetros que serão utilizados na coligada em uso.   
  
**Servidor SMTP (para envio de e-mails):**Informe o nome do servidor SMTP, isto é, o servidor de correios eletrônicos a ser utilizado.  
  
**Testar parâmetros para envio de e-mails:**A função deste botão é verificar se as configurações feitas para envio de e-mail estão funcionando corretamente.  
 **Parâmetros Globais:**Informe os dados para os parâmetros que serão utilizados por todas as coligadas quando estes não forem informados nos Parâmetros da Coligada Atual.  
  
Para maiores dúvidas sobre esta parametrização, acesse: [RH - RM - FOP - Configuração de envio de e-mail para funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413010063767-RH-RM-FOP-Configura%C3%A7%C3%A3o-de-envio-de-e-mail-para-funcion%C3%A1rios)  
3. Incluir os avisos automáticos pelo menu **Configurações | Avisos Automáticos**. Abaixo constam as definições das opções e dos campos desta tela:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023724091)  
  
Aba**Parâmetros da Programação:****Aviso****Descrição**Informe a descrição do Aviso automático.  
  
**Tipo**Serão definidos os tipos de avisos conforme constados no campo \*.   
  
**Tipos de Aviso:****Escala de férias**  
Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais Funcionários estiverem para tirar férias, **início de gozo próximo**. Este aviso tem como finalidade notificar os chefes da devida falta que aquele funcionário possa fazer e possivelmente, providenciar mudanças estruturais para minimizar o impacto, caso necessário. O número de dias de antecedência que será enviado o aviso é controlado pelo campo **Nro. Dias Ref**;  
  
**Término de Contrato de trabalho**Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários estiverem com contratos a vencer, **data de término de contrato próxima**. Este aviso tem como finalidade notificar os chefes com antecedência de modo que estes possam se preparar para a contratação ou demissão do(s) funcionário(s) em questão. O número de dias de antecedência que será enviado o aviso é controlado pelo campo Nro. Dias Ref.

**Férias em dobro**Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários estiverem para vencer férias em dobro, **data de vencimento de férias anterior a um ano da data atual**. Este aviso tem como finalidade notificar os chefes de que eles terão de pagar as férias dobradas ao funcionário caso este não tire férias imediatamente.  
  
**Alteração de Salário**Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários tiverem o salário alterado. Este aviso tem como finalidade notificar os chefes das alterações de salário e avisar aos funcionários o novo salário.  
  
**Alteração de Função**Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários sofrerem alteração na função. Este aviso tem como finalidade notificar os chefes qualquer alteração da função do funcionário alocado na empresa.  
  
**Demissão**Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários forem demitidos.  
  
**Solicitação alteração dados bancários**Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que um ou mais funcionários solicitarem a alteração de dados bancários via QUIOSQUE ou RM Labore.net.  
 **Confirmação alteração dados bancários**Será enviado um aviso automático pelo TOTVS Folha de Pagamento toda vez que o usuário realizar a aprovação dos dados em: **Administração de Pessoal | Aprovações de Alterações Cadastrais** ou realizar a liberação de competência.  
  
**Outros**O tipo de mensagens **Outros** foi criado para permitir que os clientes peçam customizações do comportamento do envio de mensagens, permitindo à equipe de desenvolvimento uma flexibilidade maior para a implementação destes códigos.  
  
**Nº dias Referência**Este parâmetro serve para determinar o intervalo de tempo em dias que uma programação irá gerar uma  
mensagem para determinado destinatário tendo como referência à data de ocorrência do evento menos o número de dias de referência.

**Exemplo:**Um funcionário vai tirar férias no dia 01/06/2020, se colocarmos o valor **30** no campo dias de referência, será gerada uma mensagem para o grupo selecionado quando fizer 30 ou menos dias do dia que ele tirará férias, ou seja, 01/05/2020.  
  
**Importante**  
O sistema só verifica esta data para os Avisos **Escala de Férias** e **Término de contrato**.  
  
**Frequência de execução  
  
Periodicidade**  
Marque qual será a periodicidade dos envios dos avisos.  
  
**Opções de envio****Formas de envio:  
  
E-mail**Marcando esta opção, informe um ou mais endereços eletrônicos para os quais serão enviadas as mensagens, além dos destinatários do agrupamento.  
  
**Mensagem na Tela**Se marcada esta opção, o campo acima mudará o nome para Usuário(s) de terceiro(s), que devem ser separados por ponto e vírgula. Informe um ou mais usuários para os quais serão enviadas as mensagens além dos usuários do agrupamento.  
  
**Forma de montagem**Esta opção irá montar a mensagem a ser enviada para o grupo de destinatários.   
  
**Padrão - agrupamento por funcionário**O sistema enviará a mensagem padrão, cadastrada internamente no aplicativo.   
  
**Fórmula**Os avisos automáticos serão montados de acordo com o conteúdo das fórmulas informadas nos campos, Código da fórmula para o cabeçalho, Código da fórmula para o detalhe e Código da fórmula para o rodapé.   
  
**Gerador de Relatórios**Os avisos automáticos serão montados de acordo com o relatório previamente criado no RM Reports, sendo que o relatório deverá ter campo Tipo do Relatório = Aviso Automático e o Tipo de Saída = Texto. Atente-se a, ao usar esta opção, marcar o flag **RM Reports**, uma vez que os relatórios em visão Delphi estão descontinuados:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413844581271)  
  
4. **Envio do Aviso**Após parametrizado o envio do aviso conforme o passo acima, o mesmo será enviado automaticamente ao processar o tipo de aviso desejado, como demissão, alteração salarial, alteração de função, etc, ou poderá ser enviado acessando o cadastro do Aviso, menu**Configurações| Avisos Automáticos | Processos | Job que processa todos os avisos automáticos**.  
  
**Saiba mais**  
[AVISOS AUTOMÁTICOS](https://tdn.totvs.com/pages/viewpage.action?pageId=126190652)
