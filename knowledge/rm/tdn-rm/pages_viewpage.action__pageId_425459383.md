---
content_hash: 30fb8700c90b2877ff1da49973ef232aa00326171d20b42dc2a57ecbfd081b26
fetched_at: '2026-06-29T00:09:35.532000+00:00'
page_id: '425459383'
product: rm
source: tdn-rm
title: Integração TOTVS Gestão de Pessoas x TOTVS e-Learning Management SUITE (LMS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459383
version: 12
---

**TOTVS Gestão de Pessoas x Fluig LMS - Elearning**

---

**TOTVS Gestão de Pessoas**

      O TOTVS Gestão de Pessoas é um dos sistemas de gestão integrada empresarial da linha RM que promove a eficiência nos processos de contratação, controle, desenvolvimento e acompanhamento da administração de Recursos Humanos, garantindo uma gestão segura.

**Fluig Learning Management Suite – Fluig LMS**

      É uma ferramenta e-Learning que une o mundo corporativo e acadêmico em um único Sistema. O Fluig LMS  provê de maneira ágil a disponibilização de cursos e treinamentos à distância.

**A Integração**

           Com o uso do EAI da TOTVS, é feita a integração entre as informações comuns do TOTVS Gestão de Pessoas e Fluig LMS, possibilitando que as instituições de ensino superior que utilizam o TOTVS Gestão de Pessoas forneçam aos seus Usuários a possibilidade de cursarem disciplinas à distância através do Fluig LMS. O Fluig LMS envia ao TOTVS Gestão de Pessoas dados referentes às notas obtidas pelos Usuários nas Turmas da modalidade à distância.

**Arquitetura**

      O adapter do Fluig LMS está preparado para receber as mensagens síncronas e assíncronas transmitidas pelo sistema TOTVS Gestão de Pessoas, porém o Fluig LMS não faz a exibição de todos os campos na tela do respectivo cadastro ou transação, mostrando somente os mais importantes e gravando os que tenham correspondência em seu banco de dados.

       TOTVS Gestão de Pessoas x Fluig LMS - Elearning: Os dados serão trafegados pelo fluxo normal até a Fila de Integração TBC, onde o mesmo irá consumir o WebService do EAI do Fluig LMS para envio da(s) mensagem(s). Após a resposta do Fluig LMS o TOTVS Gestão de Pessoas atualizará o registro, com o status de processamento e demais dados, no Monitor da Fila de Mensagem Única.  
    
 **Clique nos links abaixo para mais informações desta integração.**  
    
 [Configurações e Parâmetros TOTVS Gestão de Pessoas](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425459431)   
 [Configurações e Parâmetros Fluig LMS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=435104110)
