---
content_hash: f70efa733a7402b3c0ef360e99b62d7cb0936b57b5ad5acc21728a98d3d736ca
fetched_at: '2026-06-29T00:10:57.984379+00:00'
page_id: '601703025'
product: rm
source: tdn-rm
title: LGPD - Lei Geral de Proteção de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=601703025
version: 24
---

# 

#FFFFFF#004C99solidInformações Gerais sobre a LGPD

Saiba mais sobre os objetivos, princípios, direitos do titular e penalidades desta lei em: [Entregas Legais - Lei Geral de Proteção de Dados - LGPD](https://espacolegislacao.totvs.com/lgpd).

#FFFFFF#004C99Adequações para atender à LGPD

A TOTVS preparou algumas funções e orientações para ajudar os clientes a gerir a proteção de dados pessoais, considerando os principais requisitos previstos na lei:

Abaixo segue um breve resumo de cada requisito:

1BA1E2Configurador Campos Pessoais/Sensíveis - Art. 5º Inc. I, II e III

Consiste na configuração das tabelas e campos que contém dados pessoais/sensíveis ou que podem ser anonimizados.

A configuração de campos para LGPD pode ser acessada em **Serviços de Globais / Segurança / Proteção de Dados / Configurar Proteção de Dados.**Através desta função é possível visualizar o mapeamento dos campos pessoais e sensíveis existentes no produto RM e adequá-los de acordo com o entendimento da empresa.

Importante!

*A TOTVS liberou o mapeamento mínimo e sugestivo de campos pessoais, é de responsabilidade do cliente, como controlador, revisar a configuração, acrescentando ou alterando dados, inclusive as classificações que foram liberadas pela TOTVS, conforme seu entendimento e orientação de sua área jurídica.*

Saiba mais sobre esta função:

* [Gerenciamento dos campos pessoais e/ou sensíveis](https://tdn.totvs.com/pages/viewpage.action?pageId=527378009)
* [Configuração de Proteção de Dados](https://tdn.totvs.com/pages/viewpage.action?pageId=527375989)
1BA1E2Auditoria dos Dados - Art. 42 § 2º e Art. 49º

Consiste no monitoramento de ações (consulta, inclusão, alteração e exclusão) efetuadas com os campos pessoais e sensíveis mapeados.

No produto TOTVS - Linha RM, em atenção às responsabilidades atribuídas pela LGPD,  o Log de Auditoria já existente no produto passou por melhorias, facilitando a rastreabilidade de alterações referentes a campos pessoais e/ou sensíveis.

Veja como efetuar a configuração destas funções:

* [Log de Auditoria x LGPD](https://tdn.totvs.com/display/LRM/%5BLGPD%5D+-+Log+de+Auditoria+RM)
1BA1E2Segurança das Informações - Art. 6º Inc. VII

Consiste na configuração da segurança de acesso às informações pessoais e sensíveis.

É responsabilidade do cliente, como controlador, proteger a camada de banco e sua infraestrutura, de forma a atender aos requisitos de segurança, aos padrões de boas práticas e de governança e aos princípios gerais previstos nesta Lei e às demais normas regulamentares.

No produto TOTVS - Linha RM a segurança aos dados pessoais e sensíveis é tratada através do cadastro de **Perfil de Segurança** e **Usuários**, sendo necessário validar os perfis de usuários e as permissões existentes para acesso ao produto, restringindo o acesso à rotinas que apresentam dados pessoais e sensíveis, mantendo a segurança dos dados.

A segurança de dados sensíveis pode ser feita através da utilização de perfis de segurança e caberá ao “controlador” definir quais profissionais da empresa podem ter acesso a informação.

Saiba como configurar as permissões de acesso:

* [Manutenção de Perfis de Segurança](https://tdn.totvs.com/pages/viewpage.action?pageId=502453057)
* [Segurança de Dados - Especificações Técnicas Linha RM](https://tdn.totvs.com/pages/releaseview.action?pageId=501468493)
1BA1E2Consentimento - Art. 7º Inc. I

A lei estabelece que o consentimento é a manifestação livre, informada e inequívoca pela qual o titular concorda com o tratamento de seus dados pessoais para uma determinada finalidade.

Deve-se identificar a necessidade da solicitação do consentimento e elaborá-lo, através de documentação física, atentando para os princípios previstos na lei em relação ao tratamento dos dados pessoais. 

O cliente, como controlador, é responsável pela:

* **Elaboração:** criação do termo de consentimento, assegurando todos os princípios previstos na lei e necessidade de uso dos dados pessoais pela empresa.
* **Solicitação:**inserir a solicitação do consentimento ao titular nos processos da empresa, por exemplo, na contratação de funcionários e serviços.
* **Gestão:** controlar o consentimento dos titulares e a atualização do termo de consentimento em caso de atualizações ou mudanças na finalidade do tratamento dos dados pessoais, que neste caso deve ser solicitado novo consentimento ao titular, que possui o direito de revogá-lo.

É importante lembrar que o cliente, como controlador, deverá destacar no termo de consentimento quais produtos compartilha dados dentro e fora da organização.

*O TOTVS linha RM possui tratamento de consentimento somente para candidatos, para as demais personas da Empresa sugerimos avaliar as questões contratuais abordando o consentimento com a utilização de seus dados pessoais.*

Atenção!

**Dado pessoal de criança e adolescente**: O [Estatuto da Criança e do Adolescente (ECA)](http://www.planalto.gov.br/ccivil_03/leis/l8069.htm) considera criança a pessoa até 12 anos de idade incompletos e adolescente aquela entre 12 e 18 anos de idade. A   LGPD apresenta uma sessão específica sobre os dados de crianças e adolescentes, portanto, para titulares menores de idade deve existir um consentimento específico e claro dos pais ou responsável legal.

Saia como configurar o consentimento de candidatos para o RM:

* [Consentimento de Candidatos](https://tdn.totvs.com/display/public/LRM/Consentimento+-+RH+-+RM)
1BA1E2Protocolos - Art. 6º Inc. VII

Assegurar a proteção das informações nas integrações, de ponta a ponta, em relação aos protocolos utilizados pela empresa nas comunicações realizadas. O cliente, como controlador, é o responsável em assegurar esta proteção/segurança.

No sentido de orientar e auxiliar os clientes, a TOTVS sugere algumas validações:

* Verificar se a empresa faz uso de protocolos inseguros como: HTTP, ODBC, FTP, Telnet, etc.
* Avaliar a substituição destes por **protocolos SEGUROS**: HTTPS, FTPS, SSH, etc.
* Manter desativado por padrão os protocolos inseguros, caso não possua alternativa de substituição.
1BA1E2Integrações - Art. 6º Inc. VII

Garantir a segurança das informações nas comunicações, interna ou externa, por meio eletrônico ou físico.

É de responsabilidade do cliente garantir que a comunicação, entre os componentes de instalação, seja feita de maneira segura. Garantindo que as informações, trafegadas entre as pontas, não sejam interceptada ou sofra ataques.

A TOTVS apresenta algumas sugestões/orientações para segurança dos dados:

* mapear e avaliar as integrações de informações realizadas nos processos da empresa.
* evitar integrações a nível de banco de dados, quando não for possível, sugerimos o uso de criptografia em ambos os bancos.
* restringir acesso a diretórios e arquivos.
* para rotinas que geram arquivos em formatos txt, xml, html, csv e outros, sugerimos o descarte após o uso ou transferência para local seguro.
* inserir senhas em arquivos enviados por e-mail.
* utilizar integrações através de APIs contendo protocolos seguros.

1BA1E2Criptografia - Art. 6º Inc. VII

A criptografia garante a segurança da informação através de um conjunto de regras que visa codificar a informação de forma que só o emissor e o receptor consiga decifrá-la.

A TOTVS aconselha que seus clientes utilizem o recurso "**Criptografia de Dados Transparente (TDE)**"  do SGBD do produto.

Saiba mais: 

* [Criptografia de Dados - Linha RM](https://tdn.totvs.com/display/LRM/Criptografia+para+banco+de+dados+-+Linha+RM)
1BA1E2Anonimização - Art. 18 Inc. IV / VI

A anonimização consiste na utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo.

Já consta disponível o processo de anonimização do candidato junto ao produto de RH através da exclusão, as demais "personas" como: Funcionário, Dependente, Instrutor, entre outros existentes no produto, a TOTVS oferecerá um novo produto para estes fins, o TPD (Totvs Privacidade de Dados)  integrado com os ERPs.

1BA1E2Relatório Dados do Titular - Art. 9º / Art. 18 / Art. 19

Consiste na permissão de acesso facilitado e seguro sobre o tratamento do dado do titular e atendimento ao princípio do livre acesso.

O relatório ainda não possui definições nem modelo divulgado pela **ANPD** - Agência Nacional de Proteção de Dados, portanto, fica sob a responsabilidade do cliente elaborar seu relatório, de acordo com as necessidades e entendimento da empresa. Lembrando que no mesmo devem constar os dados pessoais/sensíveis e o motivo de uso dos mesmos.

1BA1E2Responsabilidades do Cliente

Em nosso "Espaço Legislação" possuímos muitas informações sobre a LGPD. Acesse o link <https://espacolegislacao.totvs.com/lgpd/> e localize o tópico **"Responsabilidades"** para obter maiores detalhes sobre as responsabilidades do cliente em torno da LGPD.

Importante!

* *O cliente deverá buscar, por sua conta, risco e ônus, orientação jurídica específica para garantir a observância da Legislação aplicável, sendo único e integralmente responsável por qualquer falha ou descumprimento da Legislação.*

* *Caberá exclusivamente ao cliente em adequar os processos internos e/ou externos dentro do que a LGPD exige, sendo pois, o responsável, como controlador, pelo tratamento de dados pessoais (ou sensíveis).*
