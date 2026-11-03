---
content_hash: 441885cd96957c54ccfafab5008da693aa481c812f041dbdb7c235626a598a08
fetched_at: '2026-06-29T00:09:36.030056+00:00'
page_id: '425459460'
product: rm
source: tdn-rm
title: Parâmetros do Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459460
version: 6
---

Esta guia compreende todos os parâmetros referentes ao Portal do Processo Seletivo:

**Guia "Área pública"**

Nome do portal de inscrições: determina qual nome será dado ao Portal de inscrições do Processo Seletivo. O nome dado ao Portal será visualizado na página de login do sistema, também conhecida como área pública do Portal.  
Texto da área pública: é possível configurar um texto para ser visualizado na área pública do Portal. Através deste parâmetro será possível realizar tal configuração.  
Utilizar senha no portal: determina se o campo senha será utilizado no Portal. A configuração deste parâmetro impacta no funcionamento de diversos serviços:  
**a)** Cadastro de candidato: se o parâmetro "senha" estiver habilitado, então o sistema exigirá o preenchimento do campo senha e confirmação de senha. No e-mail de confirmação de cadastro será enviada a senha informada pelo candidato. Se o parâmetro estiver desabilitado, então os campos de senha não aparecerão no formulário de cadastro e o e-mail de confirmação irá com uma senha aleatória gerada pelo sistema.  
**b)** Login do sistema: se o parâmetro "senha" estiver habilitado, então as credenciais exigidas serão "CPF" ou "RG" e "Senha". Se o parâmetro estiver desabilitado, então as credenciais exigidas serão "CPF" ou "RG" e "Data de Nascimento".  
**c)** Esqueci a senha: se o parâmetro "senha" estiver habilitado, então este serviço estará disponível, caso contrário não será disponibilizado no Portal.  
**d)** Dados pessoais: se o parâmetro "senha" estiver habilitado, então este serviço estará disponível, caso contrário não será disponibilizado no Portal.  
**e)** Alterar senha: se o parâmetro "senha" estiver habilitado, então este serviço estará disponível, caso contrário não será disponibilizado no Portal.  
Formas de identificação: determina quais dados serão disponibilizados para a identificação do candidato no momento de efetuar login no Portal de Inscrições. Os dados que poderão ser disponibilizados são: CPF, Carteira de identidade, Código de usuário e E-mail. Pelo menos uma forma de identificação deverá ser selecionada.

* **Importante:** Para que os dados CPF, Carteira de identidade e E-mail sejam utilizados no login, é necessários que estes campos estejam habilitados na configuração de "Campos de candidato". Uma vez que estes campos não foram habilitados no cadastro de candidato não tem como exigir que o candidato os informe no login, por isso, no momento de salvar os parâmetros esta consistência será validada e mensagens de alerta serão exibidas quando necessário.

**Guia "E-mails"**

* **Enviar e-mail de confirmação de cadastro de candidato:** determina se após a realização do cadastro de um candidato, o sistema irá enviar um e-mail com a confirmação de cadastro. É possível enviar e-mails personalizados de confirmação de cadastro. Por padrão, as instituições poderão continuar usando os modelos de e-mails fixos internos do sistema. Porém, as que desejarem poderão criar um modelo de e-mail próprio usando as tags disponíveis para este serviço.
* **E-mail de remetente do processo seletivo:** determina o e-mail que irá como remetente em todos os e-mails que o sistema enviar para os candidatos e também para e-mails de alertas quando não for possível alocar candidato automaticamente, quando utilizando a opção de "Utiliza alocação automática". Quando alguns dos serviços que utilizam e-mail forem selecionados o sistema irá obrigar o preenchimento deste campo

Tipo de e-mail: determina a forma como os e-mails do Portal serão enviados para os candidatos. Poderão ser enviados no formato "HTML" ou "TXT".

Importante: Para utilizar envio de e-mail para confirmação de cadastro e inscrição do candidato, o campo E-mail deve estar habilitado na configuração de "Campos de candidato". Se o campo E-mail não for habilitado, não terá como o sistema enviar e-mails para os candidatos.

**Guia "Inscrições"**  
Utilizar responsável por candidato na inscrição? Este serviço possibilita a inscrição de candidatos por responsável. Esta opção será bem utilizada em Instituições que trabalham com processos seletivos que envolvem menores de 18 anos e precisam de um responsável para responder por eles. Consequentemente será necessário disponibilizar em campos do candidato o responsável financeiro, Dados do Pai e Dados da Mãe.  
Texto do campo Treineiro: determina o texto do campo Treineiro. Este campo fica visível na tela de inscrições do Portal. Se este parâmetro estiver vazio, o texto padrão será: "Após a divulgação dos resultados você NÃO estará com o 2º grau concluído? Ou seja, você é Treineiro?".

**Guia "Relatórios"**  
Tipo de boleto/comprovante: determina a plataforma em que os relatórios serão visualizados pelo candidato. Poderão ser exibidos na plataforma "PDF" ou "HTML". Os serviços do Portal que exibem estes relatórios são "2ª via de Comprovante de Inscrição" e "2ª via de Boleto".   
Relatório de boleto e comprovante integrado: determina se os relatórios de "comprovante de inscrição" e "boleto bancário" serão exibidos integrados em um único relatório ou de forma separada.   
Texto do comprovante de inscrição: é possível configurar um texto personalizado que irá compor o comprovante de inscrição do candidato. Através deste parâmetro será possível realizar tal configuração.   
**Apresentar boleto de cobrança registrada ainda não registrado no Portal:** Permite que os boletos originados de cobrança registrada que ainda não estiverem registrados nos bancos possam ser impressos no Portal do aluno.  
  
**Guia "Resultados"**  
Mostrar classificação geral: determina se o serviço de "classificação geral" estará disponível para consulta no Portal. Este serviço exibe a listagem de classificação por processo seletivo. Mostrar classificação por área: determina se o serviço de "classificação por área" estará disponível para consulta no Portal. Este serviço exibe a listagem de classificação por área ofertada. Mostrar lista de chamada: determina se o serviço de "lista de chamada" estará disponível para consulta no Portal. Este serviço exibe a listagem dos candidatos chamados em uma área ofertada. Mostrar candidatos desclassificados: determina se candidatos desclassificados serão incluídos na listagem de resultados gerais. É importante ressaltar que este parâmetro terá efeito no Portal somente se os parâmetros "Mostrar classificação geral" e/ou "Mostrar classificação por área" estiverem habilitados. Mostrar campo Classificação: determina se a informação que contém a classificação do candidato será exibida nos serviços do Portal "Divulgação de resultados" e "Inscrições/Resultados". O Serviço "Divulgação de resultados" fica na área pública do Portal e o "Inscrições/Resultados" fica na área privada. Mostrar campo Pontuação: determina se a informação que contém a pontuação do candidato será exibida nos serviços do Portal "Divulgação de resultados" e "Inscrições/Resultados". Mostrar campo Nº de inscrição: determina se a informação que contém o número de inscrição do candidato será exibida nos serviços do Portal "Divulgação de resultados" e "Inscrições/Resultados". Mostrar campo Nº de vagas: determina se a informação que contém o número de vagas da área ofertada será exibida no serviço do Portal "Inscrições/Resultados". Mostrar campo Situação atual: determina se a informação que contém a situação atual do candidato será exibida nos serviços do Portal "Divulgação de resultados" e "Inscrições/Resultados".

**Guia "Pessoa"**  
Nesta guia é possível configurar os campos de pessoa nos serviços de candidato. Através destes parâmetros será possível determinar se um campo será visível e/ou obrigatório.

Os serviços existentes no Portal de Inscrições que irão utilizar esta configuração são: Quero me inscrever, Dados pessoais e E-mail de confirmação de cadastro. O formulário do cadastro de candidato (Quero me inscrever) no Portal será montado dinamicamente de acordo com configurações definidas aqui, ou seja, só serão exibidos no formulário os campos que forem configurados como "visível".  A configuração dos campos de candidato está dividida em 7 grupos de informação que são: Configurações Gerais 1 e 2, Dados básicos, Informações adicionais, Endereço, Documentos, Passaporte e Dados gerais de estrangeiro*s.*

Em configurações gerais 2 será possível determinar máscaras para os campos telefone e CEP. Caso estes campos estejam em branco nenhuma máscara será utilizada. Também foi disponibilizada a edição de uma mensagem para validação de Unicidade da pessoa por CPF se no módulo RH estiver com o parâmetro de unicidade por CPF selecionado.

Existem quatro informações do candidato que serão sempre visíveis e obrigatórias. O motivo é que estas informações validam a unicidade de pessoa, portanto, devem sempre ser utilizadas no cadastro do candidato. São elas: Nome,  Data de nascimento, Cidade natal e Estado natal.

O campo CPF também é utilizado na unicidade de pessoa. Isto irá depender da forma que será definido como visível e obrigatório o campo CPF na aba documentos.   
No caso do campo "Canhoto" estiver habilitado, esta informação será utilizada no processo "Alocar Candidatos em Locais de Prova". Caso contrário, ao alocar os candidatos, os canhotos serão alocados em lugares de destros.

**Aba Configurações Gerais da Pessoa**  
Nesta tela existe uma área de configuração exclusiva para os responsáveis. Será possível definir se serão utilizados na inscrição. Podem ser parametrizados por checkbox com a opção de "Exigir preenchimento". Se marcados ou Desmarcados, irão afetar os parâmetros de cada campo do responsável definidos em outra aba de parametrização de dados. O parâmetro "Exigir preenchimento do sobrenome" tem como objetivo não permitir um Nome sem sobrenome no momento de cadastrar uma pessoa. Se desmarcado poderá ter somente o nome no cadastro.  O parâmetro "Gravar dados em letras maiúsculas" tem como objetivo gravar os dados no banco tudo em letras maiúscula, mesmo sendo informados minúsculas no momento da inscrição.

O parâmetro "Utilizar campos complementares"  quando marcado irá exibir no Portal todos os campos complementares definidos para a tabela PPESSOA no momento de inclusão ou edição do cadastro da pessoa.   
Restrição de Acesso aos Dados Pessoais: Neste campo poderá ser configurado um texto para ser exibido no momento que uma pessoa com papel no corpore tentar acessar seus dados pessoais. O papel poderá ser de aluno, professor ou funcionário.

**Aba Passaporte**  
Foram criados funcionalidades nos parâmetros do sistema para que seja possível o portal receber cadastros de candidatos e responsáveis estrangeiros:

* Nacionalidade do sistema: localizado na aba Gerais - será informado o país de nacionalidade do sistema.
* Obrigar preenchimento de passaporte para estrangeiros: localizado na aba Portal | Pessoa - Passaporte - aqui irá definir se o preenchimento dos dados de passaporte de candidatos e de responsáveis serão obrigatórios quando estrangeiros.
* Utilizar parametrização dos campos de documentos sem exigir obrigatoriedade: localizado na aba Portal | Pessoa - Passaporte - neste campo será definido se o sistema irá exibir os campos de documentos que foram definidos para serem visualizados nos cadastros de responsáveis e de candidatos, porém, se algum destes campos forem obrigatórios, exclusivamente para estrangeiros não serão obrigatórios.  Se desabilitado, nenhum dos campos de documentos serão visualizados.  
  Exemplo: Se o sistema estiver parametrizado com nacionalidade do sistema: Brasil e ao informar no portal que a nacionalidade do candidato: Nova Zelândia, então o sistema irá entender que este candidato é estrangeiro e consultará a parametrização definida nos campos de passaporte para candidatos e responsáveis.
