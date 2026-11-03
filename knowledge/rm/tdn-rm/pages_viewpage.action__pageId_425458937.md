---
content_hash: 258f70ed292630500c8ff5bc611d7ebfd274f8a5d86d5e4a26bb4f6cea79ed1f
fetched_at: '2026-06-29T00:09:33.205605+00:00'
page_id: '425458937'
product: rm
source: tdn-rm
title: Inscrição do candidato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458937
version: 32
---

Esse cadastro é também um anexo do cadastro de "Processo Seletivo". Quando for acessado dentro do contexto de um processo seletivo específico, serão mostrados somente os candidatos dele. Por meio desse cadastro será possível criar uma inscrição e acompanhá-la durante o processo seletivo.

A configuração da inscrição será feita através das 7 guias que o cadastro possui,   para informações referentes ao preenchimento dos dados do candidato.

**Portal - Quero me inscrever**:

Alterada a regra dos serviços "Quero me inscrever" e "Dados pessoais". Toda pessoa que possuir algum papel no Corpore  (Professor, Funcionário, Aluno) não poderá ter seus dados alterados. O único dado que poderá ser editado é a Senha. Ou seja, quando o candidato logar no Portal de Inscrições e acessar o serviço Dados Pessoais, o sistema verificará se o mesmo é:

* Aluno em algum dos Classis.
* Professor em algum dos Classis com chapa cadastrada não demitido.
* Funcionário do Folha (Labore) que não demitido.

Se o usuário tiver algum destes papeis, o sistema bloqueará o acesso aos Dados Pessoais e informará a causa. Esta informação pode ser customizada nos parâmetros do sistema: Portal | Pessoa, na caixa "Restrição de acesso aos dados pessoais".

**Inscrição de candidatos estrangeiros**

Foram criadas funcionalidades para que seja possível ao Portal receber inscrições de candidatos e responsáveis estrangeiros, essa configuração está localizada no cadastro do Processo Seletivo na aba Parâmetros, Geral 3/3 :

* Nacionalidade do sistema: deverá será informado o país de nacionalidade do sistema.
* Obrigar preenchimento de um dos campos (CPF, Passaporte ou Registro Geral) caso estejam visíveis: se essa opção estiver marcada e os campos "CPF", "Passaporte" ou "Registro geral" também estiverem marcados como visíveis na aba "Visibilidade/Obrigatoriedade de campos", quando o candidato escolher um país diferente do informado na nacionalidade do Processo Seletivo, esses três campos ficarão obrigatórios, mas a partir do momento em que o mesmo preencher um desses campos, os demais ficarão opcionais.
* Utilizar parametrização dos campos de documentos sem exigir obrigatoriedade: nesta opção será definido se o sistema irá exibir os campos de documentos que foram definidos para serem visualizados nos cadastros de responsáveis e candidatos, porém, se algum destes campos forem obrigatórios, **exclusivamente para estrangeiros não serão obrigatórios**. Se estiver desabilitado, nenhum dos campos de documentos serão visualizados.

Exemplo: Se o sistema estiver parametrizado com nacionalidade do sistema: Brasil e ao informar no Portal que o campo "País natal" do candidato é Nova Zelândia, então o sistema irá entender que este candidato é estrangeiro e consultará a parametrização definida nos campos citados acima.

Observação: Para que verifique apenas o passaporte de candidatos estrangeiros, deve ser utilizado o campo designado como "Estado natal". Nenhum outro campo, como nacionalidade ou quaisquer outros irão funcionar. 

**Inscrição de candidatos em** **de acordo com a lei federal nº 12.711/2012**

**Para escolher as áreas de interesse**: Primeiramente deverá ser escolhida a 1ª opção do candidato, ou seja, aquela área que é o seu objeto de interesse prioritário no processo seletivo. Esta opção está na guia **Áreas de Interesse.** Nessa guia serão inseridas ou editadas as opções dos candidatos para uma ou mais áreas de interesse disponíveis no processo seletivo. De acordo com as configurações de "Área de Interesse Ofertada"  (a 1º opção) será permitido que o candidato informe áreas de interesse secundárias.

**Opções de Idiomas**

Se a área de interesse que o candidato escolheu como 1ª opção demandar a execução de provas de língua estrangeira, será necessário que ele escolha o(s) idioma(s) para realizar a prova. A composição da lista de idiomas escolhidos será feita por meio dessa guia.

**Agendamento**

A guia Agendamentos será exibida apenas para inscrições feitas em processos seletivos com atividades agendadas. Nesse caso, é necessário que o candidato escolha uma data e um horário, para comparecer ao local designado e realizar as provas. Sempre que necessário essa guia poderá ser utilizada para alterar as opções de agendamento que tenham sido feitas anteriormente.  
Sobre os campos:

Data: nesse campo deverá ser selecionada a data que o candidato escolheu para fazer a prova. As datas que estarão disponíveis serão aquelas que foram disponibilizadas por meio do processo "Alocar recursos e horários para atividade". Não serão exibidas datas para os horários que tenham sido já agendados por candidatos.

Horário: permite que, dentro do dia que foi selecionado no campo Data, seja escolhido um dos horários ainda livres para execução de provas.

Nome do bem: Será visualizado somente após salvar a inscrição. O bem será determinado pela data e horário que foram definidas nos campos Data e Horário. Se existir mais de um bem disponível para execução de prova no horário selecionado, será reservado aleatoriamente pelo sistema qual bem será disponibilizado para o candidato.

**Situações possíveis**: Uma área ofertada que permita a 2ª opção e a 1ª opção não chegue a atingir um número de interesse suficiente, a instituição poderá utilizar alternativa. Neste caso, a área poderá ser cancelada pelo processo de cancelar área ofertada e o candidato passará a ter como 1ª opção o que antes era a sua 2ª opção.  Em outros casos, o próprio candidato pode não atingir pontuação suficiente para ser classificado para a vaga da sua 1ª opção e a instituição oferecer vaga da 2ª opção (se houver) para o candidato.  
   
Opcionalmente, o usuário poderá criar campos complementares para compor o cadastro. Nesse caso, além das guias citadas anteriormente, estará presente também a guia "Campos complementares", ela será disponibilizada no sistema pelo Menu Cadastro| Campos complementares| Inscrição do candidato.

Até a versão 11.00 os botões "2ª via de comprovante" e "Enviar login usuário", existentes na tela de inscrição WinForms, só ficavam habilitados durante o período de inscrição do processo seletivo. Alteramos esta regra e agora estes botões ficarão habilitados para sempre, ou seja, não haverá mais restrição.

**Itinerário informativo:**

Os itinerários formativos são o conjunto de disciplinas, projetos, oficinas, núcleos de estudo, entre outras situações de trabalho, que os estudantes poderão escolher no ensino médio.

O candidato visualiza quais itinerários estão disponíveis para se inscrever de acordo com a parametrização informada na área de interesse ofertada. 

Para que a aba fique visível é necessário que a área de interesse tenha itinerário informativo cadastro. Para parametrizar um itinerário informativo acesse:  . 

Ao selecionar uma área de interesse na primeira opção que estiver ofertando **dois** itinerários e a quantidade **mínima** e **máxima** for **dois**, de forma automática os dois itinerários formativos já serão inseridos na aba de itinerários. O mesmo vale se a quantidade **mínima** e **máxima** for **três** e a área de interesse estiver ofertando **três** itinerários, também será inserido os **três** itinerários e assim por diante.

**Observação:** Esta funcionalidade está disponível somente para o novo portal de inscrição. 

**Inscrição via portal**

A partir das versões 12.1.29, 12.1.31 e 12.1.32, quando uma inscrição for feita pelo portal o sistema passará a gravar no campo "Data de aceite da inscrição" a data e hora completa da inscrição, contendo também os milissegundos, porém esta implementação não está disponível para base de dados Oracle, somente bases SQL Server.

**Inscrição via portal e RM.exe**

A partir da versão 12.1.2310  
Foi disponibilizado dentro do Processo Seletivo na tela **Parâmetros** > **Informações 1/2** o parâmetro **"Utiliza a escolha obrigatória do Campus/Polo, da matrícula, no formulário de Inscrição"**. Para mais informações [Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=777934145).

**Questionário:**

Caso o processo seletivo possua um questionário definido, este poderá ser executado uma única vez, após a conclusão não será possível reabrir e caso o processo seletivo esteja fora do período de inscrição o questionário também não poderá ser executado. 

**Taxa de inscrição:**

Importante

A partir da versão 12.1.34 (prevista para fevereiro de 2022), ao criar uma inscrição em um processo seletivo que possua taxa de inscrição e o responsável pelo lançamento que será gerado, seja o próprio candidato ou o responsável financeiro, existam como "fornecedor" no cadastro de cliente/fornecedor do TOTVS Gestão Financeira, serão alterados para "Ambos", pois o sistema não permite geração de lançamentos para o tipo "Fornecedor".

 Informações Complementares

---

 

 

 

 

 Como Fazer

---

 

 

 

 

[Geração de Movimento para Inscrições](http://tdn.totvs.com/x/sf1bGQ)

 Veja Também

---

[Documento Técnico - Inscrição de Candidatos através de WebService](http://tdn.totvs.com/pages/viewpage.action?pageId=235333311)
