---
content_hash: 0bb88087a36664357cfea53f7216cd646055792ef9eb7e1b0d4787c4649b1a62
fetched_at: '2026-06-29T00:10:52.262749+00:00'
page_id: '571523071'
product: rm
source: tdn-rm
title: Gestão do TCC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571523071
version: 45
---

A funcionalidade gestão de TCC (Trabalho de conclusão de curso) é um recurso que pode ajudar bastante aos usuários do sistema, tanto na agilidade do aluno cadastrar seu tema de TCC, solicitar orientações (para um professor), realizar acompanhamento de trabalho, envio de arquivos e marcação de reuniões por seu orientador. Pois os alunos e professores vão poder realizar todas essas atividades utilizando o Portal Educacional de qualquer lugar, bastando ter apenas um computador com acesso à internet.

De forma prática, o usuário da secretaria irá criar/configurar toda estrutura do TCC (Linha de pesquisa, Situação do TCC, Tipos de TCC, etc.) para que o aluno possa entrar no Portal Educacional, cadastrar seu tema do TCC e convidar o professor para ser seu orientador.

10.2Parametrização Geralfade

Para habilitar a funcionalidade, o usuário deverá conceder algumas permissões para que o operador do sistema, possa realizar a gestão do TCC no RM.exe e o Professor / Aluno possa acompanhar a gestão do TCC nos portais.

### **01.****PERMISSÃO DE SEGURANÇA POR PERFIL DE USUÁRIO - Operador do Sistema no RM.exe**

Essa permissão irá habilitar a funcionalidade no Trabalho de Conclusão de Curso no RM.exe.

**Serviços Globais | Segurança | Perfis | Educacional | Atividades Acadêmicas | Acadêmico | Trabalho de Conclusão de curso**

### **02. PERMISSÃO DE SEGURANÇA POR PERFIL DE USUÁRIO - 'Portal' para o Professor**

Essa permissão irá habilitar o menu: TCC no Portal Corpore.Net para o Perfil do Professor.

**Serviços Globais | Segurança | Perfis | Educacional | Educacional (Portal) | Professor | Trabalho de Conclusão de curso (TCC)**

### **03. PERMISSÃO DE SEGURANÇA POR PERFIL DE USUÁRIO - 'Portal' para o Aluno**

Essa permissão irá habilitar o menu: TCC no Portal Corpore.Net e novo portal do Aluno para o Perfil do Aluno.

**Serviços Globais | Segurança | Perfis | Educacional | Educacional (Portal) | Acadêmico| Trabalho de Conclusão de curso (TCC)**

###### Portal Corpore.Net                                                                                                                                         novo Portal do Aluno

### **04. PARAMETRIZAÇÃO CADASTRO DA COLIGADA**

**4.1**-  **Cadastro e-mail da Coligada**

No cadastro de coligadas, informar o campo “E-mail”, pois o sistema irá utilizar essa conta para enviar e-mail referente a assuntos do TCC.

**Serviços Globais | Administração | Cadastros | Coligada**

**4.2**-  **Configuração dos dados para envio de e-mail**

Depois de cadastrar o e-mail da coligada, devemos cadastrar os dados para envio de e-mail.

**Serviços Globais | Ambiente | Configuração | Parâmetros | Globais | Envio de e-mails**

Ao abrir o cadastro de parâmetros, na aba “Envio de E-Mails”, na opção “Considerar como remetente padrão de envio de e-mails”, devemos selecionar a opção “E-mail da coligada atual”.

### **05. PARAMETRIZAÇÃO DO TCC - PARÂMETROS DO SISTEMA**

Para finalizar as configurações, devemos acessar os parâmetros do sistema e realizar algumas configurações:

**Módulo Educacional | Configurações | Parâmetros | 15.07 - TCC**

Ao abrir o parametrizador, selecionar a opção “15.07 – TCC” e informar os parâmetros para utilização do TCC de acordo com as necessidades da instituição.

#### **5.1- TCC 1/2**

**=> Parâmetros Gerais**

* **Permitir aceite do aluno para conclusão de reuniões de acompanhamento**

Marcando este parâmetro, o professor irá conseguir finalizar uma reunião de acompanhamento somente depois do aceite do

* **Exibir os participantes da banca para o aluno no portal**

Marcando este parâmetro, o aluno poderá visualizar os participantes de sua banca examinadora, ao expandir (+) os detalhes de seu

* **Enviar versão final dos trabalhos para os participantes da banca**

Marcando este parâmetro, quando o aluno postar a versão final do seu TCC, todos os participantes cadastrados em sua banca examinadora (que possuem e-mail cadastrado) irão receber a versão final do TCC por e-mail.

* **Permitir orientações acima do máximo cadastrado para o professor**

Marcando este parâmetro, mesmo que no cadastro “Professores/Orientadores por período letivo” esteja definido um número máximo de orientações, o professor poderá ultrapassar esse limite

**Relatório do aceite da publicação do trabalho final**

Informando o relatório de aceite de publicação (que deve ser o relatório “EDUREL0071 - Autorização para publicação do TCC” disponibilizado no book de relatórios do TOTVS Educacional), o aluno poderá imprimir essa autorização, depois de cadastrar o seu TCC no

**Situação do TCC (Padrão)**

A situação do TCC deve ser informada, pois quando o aluno cadastrar o seu TCC pelo portal, o sistema irá assumir essa situação padrão. Ou seja, quando um aluno cadastrar o seu TCC pelo portal o sistema irá buscar essa situação e cadastrar em seu

**Situação de matrícula em disciplina**

Essa situação de disciplina deve ser informada, pois quando a situação do TCC for alterada para uma que indique desistência, o sistema irá alterar a situação de matrícula da disciplina (matrícula em disciplina vinculada ao TCC) para essa

**Motivo de alteração da situação de matrícula em disciplina**

Esse motivo de alteração deve ser informado, pois quando a situação do TCC for alterada para uma que indique desistência, o sistema irá usar esse motivo quando alterar a situação de matrícula da

#### **5.2- TCC 2/2**

Upload de arquivos grandes

Caso a instituição permita uploads no portal com tamanho superior ao tamanho padrão **30mb** do **IIS(Internet Information Services)**será necessário realizar algumas configurações adicionais. Saiba mais em

**=> Parâmetros Gerais**

**Tipo de armazenamento**

Nesse parâmetro deve-se configurar o tipo de armazenamento que a Instituição de Ensino irá usar, podendo ser: Arquivo da base de dados, Arquivo de algum diretório ou Arquivo no

**Diretório de armazenamento**

Nesse parâmetro deve-se informar o diretório que os arquivos serão armazenados, quando o tipo de armazenamento for de Arquivo de algum diretório.

**Tamanho máximo de armazenamento**

Nesse parâmetro podemos informar o tamanho máximo dos arquivos que irão ser postados, pois é de extrema importância limitar os arquivos para economizar espaço, seja em disco ou no banco de

**Extensões de arquivos permitidas (Exemplo: “pdf, ppt”)**

Neste parâmetro podemos informar as extensões permitidas para postar arquivos referentes ao

### **06. PARAMETRIZAÇÃO DA DISCIPLINA**

Depois de realizar as configurações, precisamos cadastrar as “Disciplinas de TCC”, na grade do curso

**Módulo Educacional | Currículo e Oferta| Estrutura Curricular | Matrizes Curriculares | "Anexo" Período | "Anexo" Disciplinas da Matriz Curricular**

Neste cadastro, devemos informar qual a disciplina que será de TCC.

**Parâmetro: “Indica se a disciplina é de TCC”.**

Assim, quando o aluno realizar o cadastro de seu TCC no portal educacional, deverá selecionar uma matrícula em disciplina que seja de TCC para realizar o vínculo com o TCC.

**Parâmetro: “Indica se o TCC pode ser em grupo**

Ao marcar esse parâmetro, a disciplina parametrizada para o TCC, poderá ser realizada em Grupo, isso é, o TCC poderá ser realizado por mais de um aluno.

0.2Parametrização do Processo TCCfade

Depois de realizar as parametrizações do sistema, precisamos cadastrar os **“Professores/Orientadores por período letivo**”.

 **Módulo Educacional | Atividades Acadêmicas | Acadêmico | Trabalho de conclusão de curso (TCC) | Professores/Orientadores por Período Letivo**

Neste cadastro, devemos informar todos os professores que podem ser orientadores em um determinado período letivo com o número máximo de orientações.

Depois de cadastrar os professores/orientadores por período letivo, precisamos **cadastrar as “Linhas de Pesquisas”**:

**Módulo Educacional | Atividades Acadêmicas | Acadêmico | Trabalho de conclusão de curso (TCC) | Linha de Pesquisa**

Neste cadastro, devemos informar todas as linhas de pesquisas da instituição. Lembrando que para cada linha de pesquisa informada, devemos informar os professores e as matrizes aplicadas que forem associadas à linha de pesquisa (Anexo do cadastro de linha de pesquisa).

Depois de cadastrar as linhas de pesquisas, precisamos cadastrar os **“Status do TCC”**:

 **Módulo Educacional | Atividades Acadêmicas | Acadêmico | Trabalho de conclusão de curso (TCC) | Status do TCC**

Neste cadastro, devemos informar todas as situações que o TCC poderá assumir. Ou seja, um status de TCC pode ser “Em aberto”, “Aprovado (parâmetro ‘Indica status final do TCC’ marcado)” ou “Desistência (parâmetro ‘Indica desistência’ marcado)”.

Depois de cadastrar os status de TCC, precisamos cadastrar os **“Tipos de participantes da banca”**:

 **Módulo Educacional | Atividades Acadêmicas | Acadêmico | Trabalho de conclusão de curso (TCC) | Tipos de Participantes da banca**

Neste cadastro, devemos informar todos os tipos de participantes da banca. Por exemplo: “Convidado”, “Avaliador”, etc.

Depois de cadastrar os tipos de participantes da banca, precisamos cadastrar os **“Tipos de TCC”:**

 **Módulo Educacional | Atividades Acadêmicas | Acadêmico | Trabalho de conclusão de curso (TCC) | Tipos de TCC**

Neste cadastro, devemos informar todos os tipos de TCC da instituição. Por exemplo: “Monografia”, “Tese”,

Depois de cadastrar os tipos de TCC, precisamos cadastrar o e-mail na matriz aplicada que irá receber os dados de novos participantes de banca, quando o professor realizar o cadastro pelo portal

**Módulo Educacional | Currículo e Oferta | Estrutura Curricular | Matrizes curriculares | 'Anexo' Matriz Aplicada | 'Aba' TCC**

Neste cadastro, devemos informar o e-mail (geralmente o e-mail da coordenação) que irá receber os dados de participantes da banca (pessoas externas) para serem cadastrados no sistema e associados a banca. Lembrando que este e-mail deve ser de um usuário no sistema (RM.exe) que tenha acesso para realizar o cadastro de participantes da banca.

Depois de cadastrar o e-mail na matriz aplicada, podemos cadastrar o TCC, vincular os orientadores, as bancas e a matrícula vinculada ao TCC.

0.2Gestão TCC - Alunofade

### **01. CADASTRO TCC**

**Novo portal do Aluno | Grade Curricular | (Disciplina configurada como TCC)**

Neste cadastro, o aluno deve informar o tema do TCC, a linha de pesquisa, tipo do TCC e a matrícula vinculada ao TCC. Ou seja, todo TCC deve estar relacionado com uma matrícula em uma disciplina de TCC. Lembrando que este cadastro também pode ser realizado pelo sistema (usuário da secretária).

Depois de cadastrar o TCC, o aluno poderá convidar o professor para ser seu orientador no TCC, visualizar a banca cadastrada e seus participantes (dependendo de parametrização), cadastrar outros alunos para o grupo de TCC, caso o TCC possa ser feito em grupo. E por fim, se todas as reuniões de acompanhamento estiverem finalizadas, ele poderá enviar a versão final do arquivo de TCC.

|  |  |  |
| --- | --- | --- |
| Fluxo de cadastro de TCC | | |

### **02. Edição de TCC**

**Novo portal do Aluno | Grade Curricular | TCC - Trabalho de Conclusão de Curso**

A linha de pesquisa pode ser editada, desde que **não tenha** nenhum orientador convidado com **convite aceito**;

|  |  |  |
| --- | --- | --- |
| **Fluxo de edição de TCC** | | |

A partir da versão 12.1.2406 - Edição de linha de pesquisa no TCC

Se o houver orientadores convidados, o sistema irá avaliar se os mesmos estão associados a nova linha pesquisa escolhida, e caso encontre algum orientador não associado, o sistema irá notificar o usuário, conforme a imagem abaixo:

### **03. ACOMPANHAMENTO TCC**

****Novo portal do Aluno | Grade Curricular | TCC |** **Acompanhamento****

Neste cadastro, o aluno poderá visualizar as reuniões marcadas pelo seu orientador. Podendo interagir e enviar o(s) arquivo(s) para que o professor possa corrigir e/ou dar sugestões.

* Permite visualizar as reuniões de acompanhamento, contendo o histórico dos arquivos postados e os comentários separados por dia;
* Postar arquivo com comentário para o professor;
* Visualizar datas previstas dos acompanhamentos e data limite de entrega do arquivo para esses acompanhamentos;
* Visualizar orientações do professor e arquivo que possa ter sido incluído;
* Dar aceite para finalizar a(s) reunião(ões) de acompanhamento.

Para maior controle do acompanhamento do TCC, o mesmo contará com histórico de acordo com as seguintes legendas:

* **Em aberto**: Se a “Data Prevista” não estiver vazia, se a “Data Prevista” ainda não ter chegado (for maior do que HOJE) e o não tiver ACEITE do aluno.
* **Aceite Pendente**: Se a “Data Efetiva” não estiver vazia, se tiver orientação do professor, se NÃO tiver aceite do aluno e a “Data Prevista” já passou.
* **Encerramento Pendente**: Mesmas condições do "Aceite pendente", sem estar encerrado e o aluno já ter realizado o Aceite.
* **Encerrado**: Quando o Professor encerrou o Acompanhamento.

|  |  |  |
| --- | --- | --- |
| **Fluxo de edição de acompanhamento de TCC** | | |

false

**Arquivo Final**

Permite enviar o arquivo final contendo o TCC finalizado.

**Observação**: Para que consiga incluir o arquivo final, é necessário que todos os acompanhamentos/reuniões devem estar encerrados, com aceite do aluno.

**Banca**

Permite ao Aluno visualizar o horário, data e local da banca e os participantes da Banca.

0.2Gestão TCC - Professorfade

Depois que o TCC é cadastrado no sistema, o professor poderá cadastrar a banca do TCC, as linhas de pesquisa que ele irá trabalhar por período letivo, aceitar ou negar o(s) convite(s) para orientação do(s) aluno(s), marcar reuniões de acompanhamento e realizar o encerramento do TCC, além disso o professor poderá cadastrar/alterar/excluir as reuniões de acompanhamento do TCC. Nela o professor define as datas e orientações ao(s) aluno(s) do TCC que está orientando. Podendo também receber/enviar arquivos com correções do(s) aluno(s).

**Portal Educacional | TCC |****Ac****ompanhamento**

O cadastro da Banca e realizado pelo professor através do menu:

**Portal Educacional | TCC | Banca**

Neste cadastro, o professor poderá cadastrar/alterar a banca do TCC informando tema, data e local da banca. Podendo também cadastrar os participantes da banca, sendo professor ou uma pessoa externa. Nessa última, os dados serão enviados por e-mail (de acordo com o e-mail informado no item 13 acima), para que o usuário responsável realize o cadastro e a associação da pessoa na banca.

Ainda no portal o professor poderá incluir ou excluir a linha de pesquisa que deseja acompanhar no período letivo, no qual deseja atuar, através do menu abaixo:

**Portal Educacional | TCC | Linhas de pesquisa**

**=> Convite para orientação do TCC.**

Neste cadastro, o professor poderá aceitar/recusar o convite de orientação. Mas em caso de recusa, ele deverá preencher uma justificativa.

**Portal Educacional | TCC | Convite para Orientador**

**=> Encerramento do TCC**

**Portal Educacional | TCC | Encerramento**

Ao final do período letivo, o professor poderá alterar a situação do TCC neste cadastro, caso as reuniões de acompanhamento estejam encerradas e o arquivo final postado pelo aluno.

0.1Processos TCC - RM.exefade

 Na funcionalidade gestão de TCC existem processos que permitem a cópia de informações entre períodos letivos. Estes processos tem o objetivo de facilitar a atualização das configurações do TCC em outros períodos letivos.

**Módulo Educacional** **| Atividades Acadêmicas | Acadêmico | Trabalho de Conclusão de Curso (TCC)  | Professores/orientadores por período letivo | Processos | Processo de cópia das configurações dos professores entre períodos letivos**

Este processo tem por finalidade copiar as configurações dos professores entre dois períodos letivos, podendo também realizar a cópia das linhas de pesquisa relacionadas. Parâmetros do processo:

* Período letivo origem;
* Período letivo destino;
* Copiar as linhas de pesquisa marcando a opção **“Copiar dados contidos no cadastro de professores orientadores da linha de pesquisa”**. Quando esta opção estiver marcada o usuário ainda poderá restringir a cópia marcando a opção **“Ignorar as linhas de pesquisa que não estejam ativa”**.
* Ignorar as configurações de professores demitidos marcando a opção **“Ignorar os professores demitidos”**.
* Em alguns momentos o período letivo destino já poderá conter alguns registros cadastrados, neste cenário o usuário deverá definir a opção **“Havendo conflitos no destino”** que estabelecerá uma ação a ser executada:
  + **Ignorar** – Não processa registros que já existem no destino;
  + **Atualizar** – Atualiza os registros no destino;
  + **Excluir** – Exclui os registros no destino substituindo-os pelos da origem
  + Para aumentar a flexibilidade do processo ainda é permitido ao usuário filtrar os registros da origem para realizar a cópia apenas de parte deles. Quando nenhum filtro é realizado todos os registros da   
    origem são copiados.

**Módulo Educacional** **| Atividades Acadêmicas | Acadêmico | Trabalho de Conclusão de Curso (TCC)  | Processo de cópia das linhas de pesquisa dos professores entre períodos letivos**

Este processo tem por finalidade copiar as linhas de pesquisa dos professores entre dois períodos letivos.

Parâmetros do processo:

* Período letivo origem;
* Período letivo destino;
* Ignorar a cópia das linhas de pesquisa inativas marcando a opção **“Ignorar as linhas de pesquisa que não estejam ativa”**;
* Ignorar as linhas de pesquisa de professores demitidos marcando a opção **“Ignorar os professores demitidos”**.
* Em alguns momentos o período letivo destino já poderá conter alguns registros cadastrados, neste cenário o usuário deverá definir a opção **“Havendo conflitos no destino”** que estabelecerá uma ação a ser executada:  
  + **Ignorar** – Não processa registros que já existem no destino;
  + **Atualizar** – Atualiza os registros no destino;
  + **Excluir** – Exclui os registros no destino substituindo-os pelos da origem;

Para aumentar a flexibilidade do processo ainda é permitido ao usuário filtrar os registros da origem para realizar a cópia apenas de parte deles. Quando nenhum filtro é realizado todos os registros da   
origem são copiados.

0.1Informações Adicionaisfade

Para facilitar a soma das notas fornecidas pelos participantes da banca, foi disponibilizado algumas funções de fórmulas para serem utilizadas na apuração de resultado, são elas:   
• **SomaNotaNumericaTCC:** Essa função irá somar e retornar as notas (numérica) concedidas pelos participantes da banca e retornar;

**• MediaNotaNumericaTCC:** Neste caso, a função irá somar e tirar a média das notas (numérica) concedidas pelos participantes da banca e retornar;

**• MaiorNotaConceitualTCC:** Neste caso, a função irá obter a maior nota (Conceitual) concedida pelos participantes da banca e retornar;

• **MaiorNotaConceitualTCC:** Neste caso, a função irá obter a maior nota (Conceitual) concedida pelos participantes da banca e retornar;

Assim o usuário poderá alterar sua fórmula de apuração de resultado, utilizando uma das fórmulas acima para recuperar a nota da banca e atualizar etapa final da disciplina de TCC.

Para facilitar ainda mais a gestão do TCC, a TOTVS disponibilizou alguns relatórios voltados para essa nova funcionalidade no book de relatórios, são eles:

• EDUREL0070 - Declaração de apresentação à banca examinadora (TCC);  
• EDUREL0071 - Autorização para publicação do TCC;  
• EDUREL0072 - Autorização de uso e divulgação de imagem fotográfica (TCC);  
• EDUREL0073 - Autorização para coleta e divulgação de informações (TCC);  
• EDUREL0074 - Acompanhamento do processo de TCC;  
• EDUREL0075 - Ata de defesa do TCC.

No quadro abaixo descrevemos as tabelas envolvidas na Gestão de TCC.

| Tabela | Descrição |
| --- | --- |
| STCC | Trabalho de conclusão de curso |
| STCCACOMPANHAMENTO | Acompanhamento do TCC |
| STCCBANCA | Banca do TCC |
| STCCLINHAPESQUISA | Linhas de pesquisas do TCC |
| STCCLINHAPESQUISAMATRIZAPLIC | Linhas de pesquisas da matriz aplicada |
| STCCLINHAPESQUISAPROFESSOR | Linhas de pesquisas do professor |
| STCCMATALUNO | Matrículas dos alunos vinculadas ao TCC |
| STCCORIENTADOR | Orientadores do TCC |
| STCCPARTICIPANTESBANCA | Participantes da banca do TCC |
| STCCPROFESSORPERLET | Configuração dos professores orientadores por período letivo |
| STCCSTATUS | Status do TCC |
| STCCTIPO | Tipos de TCC |
| STCCTIPOPARTICIPANTEBANCA | Tipos de participantes da banca |

false

* Os professores disponíveis são somente aqueles que estão cadastrados e aprovados para as linhas de pesquisa da matriz aplicada do aluno;
* O professor precisa ainda estar com o número de orientações dentro do máximo permitido, caso o parâmetro permitir ultrapassar o número máximo não estiver marcado.
* Permite incluir outro aluno para o TCC caso a disciplina permite que o TCC seja realizado em grupo.

**Observação:** O Botão imprimir só estará disponível se o relatório estiver parametrizado nas configurações do TCC em: **Módulo Educacional | Configurações | Parâmetros | TCC | Relatório de Aceite da Publicação do Trabalho Final**

Dica

Para saber mais sobre o processo de Gestão de TCC, acessar o documento: [Processo do TCC](http://tdn.totvs.com/download/attachments/149881049/EDU_BT_Gest%C3%A3o_TCC_1183_REQ000097.pdf?api=v2)
