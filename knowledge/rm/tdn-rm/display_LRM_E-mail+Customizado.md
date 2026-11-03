---
content_hash: 4342dc4a96d7de27921309852e411c3555f7e04a6cb2504d5053a9dc5a3ac1cc
fetched_at: '2026-06-29T00:10:06.987263+00:00'
page_id: '452719355'
product: rm
source: tdn-rm
title: E-mail Customizado
type: documentation
url: https://tdn.totvs.com/display/LRM/E-mail+Customizado
version: 80
---

**E-mail Customizado** 
O cadastro de E-mail Customizado tem como finalidade personalizar os e-mails de "Boas Vindas" e "Lembrete de Senha" enviados pelo Banco de Talentos e permite a criação de e-mails específicos para as etapas em cada tipo de requisição.
 
Assunto: assunto do e-mail que será enviado no Banco de Talentos.
 
Cód. Relatório: possibilidade de selecionar um relatório para ser gerado juntamente com a mensagem do E-mail Customizado.
 
Gerar em HTML: possibilidade de gerar o relatório selecionado no formato HTML.
 
Corpo do E-mail: possibilidade de inserir imagens e personalizar o e-mail de acordo com a necessidade da empresa. Em alguns e-mails é necessário definir parâmetros que substituirão informações relevantes. O parâmetro precisa seguir a seguinte regra: Iniciará com um "\[", seguido por um "NOME" e finalizado por outro "\]".
 
                E-mail Customizado - Boas Vindas
                Necessidade de 3 parâmetros: Código do usuário \[USUARIO\], CPF \[CPF\] e Senha \[SENHA\].
                                                                                     
                E-mail Customizado - Lembrete de Senha
                Necessidade de 2 parâmetros: Código do usuário \[USUARIO\] e Senha \[SENHA\].
 
 
\*Parametrização:\*
 
\*1) Sem utilização de relatórios\*
 ]]>

* Criar o e-mail customizado de boas vindas e lembrete de senha inserindo o Corpo do E-mail.
* Acessar Configurações| Parametrizador| RM Portal| Mensagens Automáticas e informar o E-mail Customizado nos campos "Boas Vindas" e "Lembrete de Senha".
* Ao realizar o cadastro do currículo ou relembrar a senha, o candidato receberá o e-mail com as informações contidas no E-mail Customizado.  
      
  **2) Com utilização de relatórios**
* Criar o e-mail customizado de boas vindas e lembrete de senha inserindo o Corpo do E-mail e o Cód.Relatório criado para este fim.
* Acessar Configurações| Parametrizador| RM Portal| Mensagens Automáticas e informar o E-mail Customizado nos campos "Boas Vindas" e "Lembrete de Senha".
* Ao realizar o cadastro do currículo ou relembrar a senha, o candidato receberá o e-mail com as informações contidas no E-mail Customizado (corpo do e-mail) e o relatório em formato PDF anexado a mensagem.  
     
  **3) Com utilização de relatórios no formato HTML**
* Criar o e-mail customizado de boas vindas e lembrete de senha inserindo o Corpo do E-mail, o Cód.Relatório e marcando a opção "Gerar em HTML".
* Acessar Configurações| Parametrizador| RM Portal| Mensagens Automáticas e informar o E-mail Customizado nos campos "Boas Vindas" e "Lembrete de Senha".
* Ao realizar o cadastro do currículo ou relembrar a senha, o candidato receberá o e-mail apenas com o relatório em formato HTML, independente de haver ou não texto no corpo do E-Mail Customizado.  
     
  **Dicas na criação de Relatórios**:  
     
  Boas Vindas: Não é passado nenhum parâmetro, apenas um filtro contendo o Código da Pessoa.  
     
  Lembrete de Senha: É passado um parâmetro, senha do usuário, pois esta é criptografada no banco. E também um filtro contendo o Código da Pessoa.  
     
  Observação: Dúvidas na criação de relatório no RM Reports devem ser sanadas com a equipe responsável.  
     
   **Tipos de Requisição:**  
     
  Os usuários do Vitae poderão customizar os e-mails enviados pelas requisições nas seguintes situações:  
     
  **- Criação**
  + Aprovação\*
  + Reprovação\*
  + Cancelamento\*
  + Conclusão\*  
       
    Será necessário criar um e-mail customizado para cada situação em cada tipo de requisição, para exibir algumas informações necessárias no e-mail, iremos utilizar do recurso de parâmetros:

    - Código da Requisição;
      §  \[TIPOREQUISICAO\] > Parâmetro para exibir o Tipo da Requisição;
      §  \[LINKPARECERGLOBAL\] > Exibe link para acesso à tela de aprovação Global
      §  \[LINKPARECERINDIVIDUAL\] > Exibe link para acesso à tela de aprovação Global
      §  \[TEXTOPARECERESEMITIDOS\] > Exibe texto com os pareceres emitidos
      o    \*Ao cancelar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário que cancelou;
      §  \[DATAACAO\] > Data do cancelamento;
      §  \[HORAACAO\] > Hora do cancelamento;
      §  \[JUSTIFICATIVA\] > Justificativa do cancelamento;
       
       
      Foram criados parâmetros específicos para alguns tipos de etapa e requisição;
       ]]>
    - Mensagem automática, caso utilize o Quadro de Lotação;
       
      \* {\*}-          \*Desligamento\*
      o    \*Ao aprovar\*
      §  \[IDREQSUBSTITUICAO\] > ID da Requisição de Substituição, caso exista, e N/A, caso contrário;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao reprovar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao concluir\*
      §  \[IDREQSUBSTITUICAO\] > ID da Requisição de Substituição, caso exista, e N/A, caso contrário;
      §  \[STATUSREQSUBSTITUICAO\] > Status da Requisição de Substituição, caso exista, e N/A, caso contrário;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      §  \[DATAABERTURA\] > Data da abertura da requisição;
      §  \[DATACONCLUSAO\] > Data de conclusão da requisição;
      §  \[SECAO\] > Seção da requisição;
      \* \*
      \* {\*}-          \*Alteração de Dados Funcionais\*
      o    \*Ao aprovar\*
      §  \[IDREQSUBSTITUICAO\] > ID da Requisição de Substituição, caso exista, e N/A, caso contrário;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      o    \*Ao reprovar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao concluir\*
      §  \[IDREQFILHA\] > ID da requisição filha, caso exista com status aprovada ou concluída, e N/A, caso contrário;
      §  \[STATUSREQFILHA\] > Status da Requisição de Substituição, caso exista, e N/A, caso contrário;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      §  \[DATACONCLUSAO\] > Data de conclusão da requisição;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
      \* \*
      \* {\*}-          \*Substituição\*
      o    \*Ao aprovar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao reprovar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao concluir\*
      §  \[IDREQPAI\] > ID da requisição pai;
      §  \[TIPOREQPAI\] > Tipo da requisição pai;
      §  \[ALTREALIZADAREQPAI\] > Identifica a alteração realizada pela requisição pai;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
       
       -          \*Transferência\*
      o    \*Ao aprovar\*
      §  \[IDREQSUBSTITUICAO\] > ID da Requisição de Substituição, caso exista, e N/A, caso contrário;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      o    \*Ao reprovar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao concluir\*
      §  \[IDREQFILHA\] > ID da requisição filha, caso exista, com status aprovada ou concluída, e N/A, caso contrário;
      §  \[STATUSREQFILHA\] > Status da requisição filha, caso exista, e N/A, caso contrário;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      §  \[DATACONCLUSAO\] > Data de conclusão da requisição;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
       
       -          \*Transferência com Alteração de Dados Funcionais\*
      o    \*Ao aprovar\*
      §  \[IDREQSUBSTITUICAO\] > ID da Requisição de Substituição, caso exista, e N/A, caso contrário;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      §  \[FUNCAOORIGEM\] > Função de origem do funcionário;
      §  \[FUNCAODESTINO\] > Função de destino do funcionário;
      §  \[SECAOORIGEM\] > Seção de origem do funcionário;
      §  \[SECAODESTINO\] > Seção de destino do funcionário;
      §  \[FILIALORIGEM\] > Filial de origem do funcionário;
      §  \[FILIALDESTINO\] > Filial de destino do funcionário;
      o    \*Ao reprovar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao concluir\*
      §  \[IDREQFILHA\] > ID da requisição filha, caso exista, com status aprovada ou concluída, e N/A, caso contrário;
      §  \[STATUSREQFILHA\] > Status da requisição filha, caso exista, e N/A, caso contrário;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      §  \[DATACONCLUSAO\] > Data de conclusão da requisição;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
       
      \* {\*}-          \*Transferência em Lote\*
      o    \*Ao aprovar\*
      §  \[IDREQSUBSTITUICAO\] > IDs da Requisições de Substituição, caso existam, e N/A, caso contrário;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
      §  \[FUNCIONARIOCHAVE\] > Nome dos funcionários da requisição;
      §  \[DATAPREVISTA\] > Data prevista para conclusão;
      o    \*Ao reprovar\*
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      o    \*Ao concluir\*
      §  \[IDREQFILHA\] > ID da requisição filha, caso exista com status aprovada ou concluída, e N/A, caso contrário;
      §  \[STATUSREQFILHA\] > Status da requisição filha, caso exista, e N/A, caso contrário;
      §  \[FUNCIONARIOCHAVE\] > Nome do funcionário da requisição;
      §  \[DATACONCLUSAO\] > Data de conclusão da requisição;
      §  \[MSGLOTACAO\] > Mensagem automática, caso utilize o Quadro de Lotação;
      §  \[QTDPENDENTES\] > Transferências pendentes;
      \* \*
      Obs.: Caso algum parâmetro não seja encontrado, não será exibido a informação referente.
       
       
      Importante:
      Nos parâmetros globais do sistema, pasta gerais, campo "URL de acesso ao Portal RM" deve ser informado o endereço do Portal RM, exemplo: [{+}<http://engrm-site1200/corpore.net+>|http://engrm-site1200/corpore.net].]]>
