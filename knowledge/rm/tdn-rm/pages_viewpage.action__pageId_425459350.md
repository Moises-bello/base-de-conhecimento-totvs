---
content_hash: ed6a83d6fd491f02c2ee61ca4fefa3a36cdccce420b2a8b9076cbaebf70bacf3
fetched_at: '2026-06-29T00:09:35.425241+00:00'
page_id: '425459350'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x Fluig LMS - Elearning
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459350
version: 12
---

**TOTVS Gestão de Pessoas x Fluig LMS - Elearning**

---

**TOTVS Gestão de Pessoas**

      O TOTVS Gestão de Pessoas é um dos sistemas de gestão integrada empresarial da linha RM que promove a eficiência nos processos de contratação, controle, desenvolvimento e acompanhamento da administração de Recursos Humanos, garantindo uma gestão segura.

**TOTVS e-Learning Management Suite - LMS**

      É uma ferramenta e-Learning que une o mundo corporativo e acadêmico em um único Sistema. O TOTVS LMS provê de maneira ágil a disponibilização de cursos e treinamentos à distância.

**A Integração**

           Com o uso do EAI da TOTVS, faremos a integração entre as informações comuns do TOTVS Gestão de Pessoas e TOTVS LMS, possibilitando que as instituições de ensino superior que utilizam o TOTVS Educacional forneçam aos seus alunos a possibilidade de cursarem disciplinas à distância através do TOTVS LMS. É replicada qualquer ação (incluir, alterar e excluir) no TOTVS Educacional dos módulos integrados para o TOTVS LMS. O LMS envia ao TOTVS Gestão de Pessoas dados referentes às notas obtidas pelos alunos nas Turmas da modalidade à distância.

**Arquitetura**

      O adapter do sistema TOTVS LMS está preparado para receber as mensagens síncronas e assíncronas transmitidas pelo sistema TOTVS RM, porém o sistema TOTVS LMS não faz a exibição de todos os campos na tela do respectivo cadastro ou transação, mostrando somente os mais importantes e gravando os que tenham correspondência em seu banco de dados.

       A referência entre sistemas é feita por uma funcionalidade chamada De-Para, que cria chaves de acordo com os dados enviados para referenciar os cadastros e processos que venham a ser gerados. O De-Para também é enviado na mensagem única.

      TOTVS Gestão de Pessoas à TOTVS LMS: Os dados serão trafegados pelo fluxo normal até a Fila de Integração TBC, onde o mesmo irá consumir o WebService do EAI do TOTVS LMS para envio da(s) mensagem(s). Após a resposta do TOTVS LMS o TOTVS Gestão de Pessoas atualizará o registro, com o status de processamento e demais dados, no Monitor da Fila de Mensagem Única.

---

**Clique nos links abaixo para mais informações desta integração.**

[Configurações e Parâmetros TOTVS LMS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458985)

[Configurações e Parâmentros TOTVS Gestão de Pessoas](http://tdn.totvs.com/pages/viewpage.action?pageId=438297168)

Cadastros
