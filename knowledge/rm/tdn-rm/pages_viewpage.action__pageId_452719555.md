---
content_hash: 5931d091ae703874d871337c5879556be305ebe114210387f4dcb4daa994fa2f
fetched_at: '2026-06-29T00:10:08.669037+00:00'
page_id: '452719555'
product: rm
source: tdn-rm
title: Novidades da Versão - SMT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719555
version: 1
---

**Novidades da Versão**   
**Novidades Releases:**  
   
**12.1.12 – Pessoas** - O anexo "Consultas Realizadas" passou a se chamar "Consultas Médicas". - No anexo "Consultas Médicas" é possível visualizar as consultas médicas e atendimentos ambulatoriais realizados pelas pessoas. E todo o controle de inclusão de consultas/exames é realizado agora no Prontuário Médico. - Incluído o anexo "Medicamentos Retirados" onde é possível registrar os medicamentos que foram fornecidos pela empresa ao colaborador.  
   
**12.1.12 – Candidatos** - O anexo "Consultas Realizadas" passou a se chamar "Consultas Médicas". - No anexo "Consultas Médicas" é possível visualizar as consultas médicas e atendimentos ambulatoriais realizados pelos candidatos. E todo o controle de inclusão de consultas/exames é realizado agora no Prontuário Médico.  
   
**12.1.12 – Funcionários** - O anexo "Consultas Realizadas" passou a se chamar "Consultas Médicas". - No anexo "Consultas Médicas" é possível visualizar as consultas médicas e atendimentos ambulatoriais realizados pelos funcionários. E todo o controle de inclusão de consultas/exames é realizado agora no Prontuário Médico. - Incluído o anexo "Medicamentos Retirados" onde é possível registrar os medicamentos que foram fornecidos pela empresa ao colaborador.  
   
**12.1.12 – Profissional de Saúde** - Implementado o anexo "Disponibilidade do Profissional de Saúde" que tem como objetivo registrar os períodos em que o Profissional de Saúde estará disponível para atendimentos para a empresa.  
   
**12.1.12 – Vacinas** - Implementado o anexo "Lotes de Vacina" que tem como objetivo registrar os lotes relacionados às Vacinas. - Implementado o Assistente de Lançamento de Vacinas que permite que seja lançado registros de Vacina para vários funcionários ao mesmo tempo.  
   
**12.1.12 – Tipo de Atendimento** - Implementado o "Tipo de Atendimento" que tem como objetivo armazenar os Tipos de Consulta, definindo em cada uma qual o tipo de procedimento: Consulta Médica Ocupacional, Atendimento Ambulatorial ou Ambos.  
   
**12.1.12 – Medicamentos** - Implementado o cadastro de Medicamentos que tem como objetivo registrar os medicamentos que serão fornecidos a pessoa/funcionário na empresa. - Implementado o processo de Retirada de Medicamentos que permite lançar vários medicamentos para a pessoa.  
   
**12.1.12 – Convênios** - O campo "Quantidade de dias para entrega do exame" foi acrescentado no cadastro de Convênio.  
   
**12.1.12 – Itens de Informação Clínica** - Implementado o anexo "Opções de Item de Informação Clínica" onde é possível definir opções de preenchimento dos itens de informação clínica dos exames, com possibilidade de definição de cores para tais legendas. - Implementado o anexo "Faixas de Item de Informação Clínica" onde é possível definir faixas de valores para preenchimento dos itens de informação clínica dos exames, com possibilidade de definição de cores para tais legendas. - Implementado o processo "Cópia de faixas entre itens de informação clínica" que realiza a cópia das faixas cadastradas para outro item de informação clínica. - Otimizado o processo de Cópia entre Coligadas no cadastro de Itens de Informação Clínica.  
   
**12.1.12 – Agenda de Exames** - Os campos "Consulta" e "Médico" foram acrescentados ao cadastro de Agenda de Exames.  
   
**12.1.12 – Assistente de Importação de Resultado de Exames** - Acrescentado na estrutura do arquivo XML a tag <IDCONSULTA> que é o identificador da consulta. Se este campo estiver em branco, uma consulta é criada para cada exame informado. Entretanto, se este campo estiver preenchido, o processo de importação de exames não criará uma consulta, mas apenas irá adicionar os exames à consulta cujo o "idConsulta" seja correspondente ao informado no XML.  
   
**12.1.12 – Prontuário Médico** - Implementado o cadastro de Prontuário Médico, onde é possível ter um acompanhamento da saúde do paciente através de uma única tela, abrangendo Consultas Médicas, Atendimentos Ambulatoriais, Atestados, CAT´s, Exames Pendentes, Medicamentos Retirados e Vacinas. - Possibilidade de realizar a pesquisa por Tipo de Paciente (Pessoa/Funcionário). - Criado o status da consulta "agendado". - Criado o tipo de atendimento da consulta, que pode ser Consulta Médica Ocupacional ou Atendimento Ambulatorial. - Possibilidade de registrar os medicamentos retirados durante a consulta. - Possibilidade de gerar o relatório ASO (Atestado de Saúde Ocupacional) através da edição da consulta, com status diferente de "Pendente" e "Agendado".  
   
**12.1.9 - Assistente de Importação de Resultado de Exames**

* Foi implementado melhorias na importação de Resultados de Exames.
* Alterado o processo para importar três novos campos: Tipo da Consulta, Tipo da Consulta E-Social, Código do Médico
* Alterado para importar os campos de consulta separadamente dos campos de exame.  
     
  **12.1.7 - Comissão da CIPA**
* Implementado a possibilidade de vincular várias seções na Comissão da CIPA.
* Implementado a possibilidade de definir quais os tipos de funcionários que poderão participar da Comissão da CIPA.
* Implementado a possibilidade de refazer a candidatura da CIPA através do Totvs Portal.  
     
  **12.1.6 – Filtro por Perfil**
* Implementado o processo de Filtro por Perfil para Unidade Protetora.
* Implementado o processo de Filtro por Perfil para EPC.
* Implementado o processo de Filtro por Perfil para Distribuição de EPC.
* Implementado o processo de Filtro por Perfil para Brigada.
* Implementado o processo de Filtro por Perfil para Comissão da CIPA.  
     
  **12.1.6 – Brigadista**
* Otimizado o cadastro de brigadista permitido a busca por PESSOAS ou apenas por FUNCIONARIOS através de um novo parâmetro.
    
  **12.1.6 – Comissão da CIPA**
* Otimizado o cadastro de candidatos a eleições da CIPA e participantes de reuniões da CIPA. Foi criado um parâmetro que determina a busca por PESSOAS ou apenas por FUNCIONARIOS.
    
  **12.1.4 – EPI**
* Otimizado módulo de EPI, implementado processo de Acerto de Local de Estoque. - Otimizado módulo de EPI, implementado processo de Transferir EPI.  
     
  **12.1.4 – Relátorio LTCAT**
* Implementado o processo para geração do Relátorio LTCAT.
