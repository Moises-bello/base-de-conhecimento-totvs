---
content_hash: 07512c9a5a126afeb2d842f724092b3683066cbf1547c7244cf942adff7d57c2
fetched_at: '2026-06-29T00:09:34.122924+00:00'
page_id: '425459147'
product: rm
source: tdn-rm
title: Empresa
type: documentation
url: https://tdn.totvs.com/display/LRM/Empresa
version: 13
---

---

São empresas conveniadas a instituição para a disponibilização das oportunidades de estágio e emprego.

*obs: Os campos campos com a escrito em negrito são obrigatórios.*

* **Funcionários da empresa**

Na inclusão de funcionários, o supervisor será a pessoa responsável pela supervisão do estagiário na empresa. O sistema permite que seja parametrizável quantos alunos cada supervisor poderá supervisionar. O funcionário do tipo contato é o ponto de contato Instituição – Empresa.   
No cadastro de funcionário foi criado um look up para realizar a inclusão de usuário, Com esse usuário o funcionário poderá acessar o portal educacional para realizar o cadastro das vagas e aprovações em relação ao estágio dos alunos.  
 Para realizar o cadastro de usuário para todos os funcionários daquela empresa, basta acessar o processo geração de usuários (funcionários) do registro da visão selecionada.   
Ao acessar o portal o funcionário deverá alterar no assistente de configuração o contexto global. Em entrar como, informar empresa. Além dos campos básicos é possível informar a categoria da empresa a ser cadastrada, que pode ser do tipo: Universidade; Instituto; Agência de fomento; Empresa; Profissional Liberal; Produtor Rural.  
**Observação:** caso o parâmetro **Obrigar o preenchimento dos campos CPF, RG e endereço para funcionário "Responsável Legal"** estiver marcado nas Configurações | Parâmetros | Estágio | Etapa 1, o sistema irá obrigar o preenchimento dos campos mencionados para os funcionários do tipo Responsável legal e Responsável legal/Supervisor.

A Partir do Patch: 12.1.2209.277

O Sistema permite cadastrar mais de um **Responsável legal** e/ou **Responsável legal/Supervisor** da Empresa de acordo com a legislação: [http://portal.mec.gov.br/diplomadigital/arquivos/in-05-versao-completa-anexos-i-ii-e-iii-v1.05.pdf](http://portal.mec.gov.br/diplomadigital/arquivos/in-05-versao-completa-anexos-i-ii-e-iii-v1.05.pdf "Follow link")

Para atender às alterações no processo do [Enade](https://tdn.totvs.com/display/LRM/ENADE), referentes à Avaliação Prática, conforme estabelecido pela Portaria nº 610, de 27 de junho de 2024, e pelo Edital nº 124, de 20 de julho de 2024, a Instituição passa a ser obrigada a realizar essa Avaliação Prática, que requer o cadastro contínuo dos alunos, professores orientadores e professores supervisores de estágio. Assim a Empresa do termo de compromisso, deve ser uma escola. Então foi incluído no campo categoria, a opção Escola, com a obrigatoriedade de informar a [Instituição de Ensino](https://tdn.totvs.com/pages/viewpage.action?pageId=425458695). Disponível a partir das versões: 12.1.2310.255,12.1.2402.224,12.1.2406.151.

* **Parametrização de vagas**

A parametrização de vaga define, a data de inicio e fim da vigência desta parametrização, a quantidade máxima de vagas disponíveis, além da possibilidade de enviar o currículo diretamente a empresa.   
Na aba convênio informamos o número do convenio e sua descrição.  
Alerta: É possível criar o alerta que será enviado via e-mail informando que as vagas do convênio ainda não foram preenchidas e estão próximas de ultrapassar a data limite de divulgação.  
No anexo publico alvo, associa à parametrização das vagas do público alvo estabelecido pela instituição de ensino e a empresa para disponibilização de vagas de estágio.  
No anexo documentos, informa quais os documentos necessários para os casos em que um aluno for selecionado a vaga de estágio. Estes documentos devem ser entregues no momento da definição do termo de compromisso do estágio

Para enviar o currículo diretamente a empresa, é necessário que conste o e-mail no cadastro da empresa ou na parametrização da vaga.

* **Vagas**

No cadastro de vagas preenchemos as informações pertinentes a vaga, os requisitos, cargo, departamento, local de trabalho, a carga horária semanal, hora inicial e final do expediente, horário de intervalo, a quantidade de vagas, vagas para deficientes, valor da bolsa, data limite para divulgação, se a vaga é de estágio ou emprego e o status atual: Pendente de aprovação, em aberto ou preenchida.

Veja Também

---
