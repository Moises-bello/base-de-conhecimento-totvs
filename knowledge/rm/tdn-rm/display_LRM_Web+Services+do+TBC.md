---
content_hash: 0aa3964d692c60e65945f7e348f42cea377ca16cb05a619e1f77f981bf5c0b69
fetched_at: '2026-06-29T00:09:37.232317+00:00'
page_id: '425459578'
product: rm
source: tdn-rm
title: Web Services do TBC
type: documentation
url: https://tdn.totvs.com/display/LRM/Web+Services+do+TBC
version: 22
---

**Web Services do TOTVS Business Conector**

---

O TOTVS Business Conector possui os seguintes Web Services:

* Data Server – wsDataServer
* TOTVS Gestão de Relacionamento com o Cliente – wsCRMAtendimento
* Conceitos do TOTVS Business Connect – wsConConceito
* TOTVS Message (ByYouESB) – wsTOTVSMessage
* TOTVS Educacional – wsEdu
* TOTVS Obras e Projetos - wsPrj
* Lançamento Financeiro - wsFin

Todos os WebMethods  que fazem parte dos Web Services utilizam autenticação SOAP.  
Abaixo seguem detalhes de cada um dos web services.

### **1. Data Server (wsDataServer)**

Este serviço disponibiliza acesso direto aos objetos de negócio RM (DataServer).  
***Nota:*** *Os WebMethods que possuem no final do nome a expressão "Auth", não utilizam Token e podem ser consumidos através do Browser.*  
   
**WebMethods:**

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP, criando um Token para isto. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=82477609#ComoexporosWebServicesdoRMatrav%C3%A9sdoIIS-3.Autentica%C3%A7%C3%A3o).
* AutenticaAcessoAuth: Autentica o usuário no ambiente RM.
* GestSchema ou GestSchemaAuth: Faz a leitura do DataServer (regra de negócio RM) informado.
* ReadRecord ou ReadRecordAuth: Faz a leitura do DataServer (regra de negócio RM) e retorna o registro específico (XML), conforme chave primária.
* ReadView ou ReadViewAuth: Faz a leitura do DataServer (regra de negócio RM) e retorna conjunto de registros (XML), conforme definido no filtro.
* SaveRecord ou SaveRecordAuth: Insere um registro no DataServer (regra de negócio RM). Este método somente irá incluir o registro se este for válido de acordo com as regras de negócio definidas pelo DataServer.

[Lista de DataServers disponíveis para os métodos acima](http://tdn.totvs.com/download/attachments/143655277/DataServer+para+WebServices.rar?version=1&modificationDate=1398882522704).

### **2. TOTVS Message - ByYou ESB (wsTOTVSMessage)**

O serviço é utilizado para comunicação com o ByYou ESB.  
   
**WebMethods:**

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP criando um Token para isto. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=82477609#ComoexporosWebServicesdoRMatrav%C3%A9sdoIIS-3.Autentica%C3%A7%C3%A3o).
* ReceberArquivo: recebe uma mensagem XML do ESB e grava na fila do TOTVS Business Conector para posterior processamento. No header do XML estarão contidas informações que identificam a mensagem, inclusive qual o DataServer (regra de negócio RM) irá processar a inclusão no RM.

### **3. TOTVS Educacional (wsEdu)**

Este serviço disponibiliza métodos para integração com o TOTVS Educacional.   
   
**WebMethods:**

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP criando um Token para isto. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=82477609#ComoexporosWebServicesdoRMatrav%C3%A9sdoIIS-3.Autentica%C3%A7%C3%A3o).
* ImprimeBoleto: Retorna o Stream do boleto para impressão. É necessário informar os parâmetros:
* ListarBoletos: Lista boletos em aberto.
* SimularValoresContratoTurmaDisc: Simulação de parcelas de contratos utilizando uma lista de parcelas e turmas disciplinas (sem necessidade de se ter uma matrícula na turma disciplina). [Saiba mais](http://tdn.totvs.com/pages/viewpage.action?pageId=392496907)

### **4. TOTVS Obras e Projetos (wsPrj)**

Este serviço disponibiliza métodos para integração com o TOTVS Obras e Projetos.   
   
**WebMethods:**

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP criando um Token para isto. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=82477609#ComoexporosWebServicesdoRMatrav%C3%A9sdoIIS-3.Autentica%C3%A7%C3%A3o).
* ApropriarMovimentoTituloAPagar:  Apropriação de custos de um título a pagar.

### **5. TOTVS Gestão de Relacionamento com Cliente (wsCRMAtendimento)**

Este serviço disponibiliza métodos para integração com o TOTVS Gestão de Relacionamento com Cliente.  
   
**WebMethods:**

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP criando um Token para isto. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=82477609#ComoexporosWebServicesdoRMatrav%C3%A9sdoIIS-3.Autentica%C3%A7%C3%A3o).
* avancaEtapaAtendimento: Executa o processo de avançar etapa do atendimento com todos os seus procedimentos, regras e fórmulas, encaminhando o atendimento a princípio para a etapa informada (pode ser alterado por alguma fórmula).
* avancaEtapaAtendimentoSetResponsavel:  Executa o processo de avançar etapa do atendimento com todos os seus procedimentos, regras e fórmulas, encaminhando o atendimento a princípio para a etapa e atendente informados (pode ser alterado por alguma fórmula) .
* buscaAtendenteByUsuario:  Atendente que está associado ao usuário informado.
* buscaAtendenteContatoCliente: Atendente que é o responsável, neste atendimento, por manter contato com o cliente para trocar informações sobre a solicitação constante no atendimento.
* buscaAtendentesByRamal: Lista de atendentes que possuem, no cadastro de atendentes, o campo ramal informado.
* buscaAtendenteResponsavelPeloAtendimento: Atendente atual que se encontra com o atendimento.
* buscaRamalAtendente: Ramal do atendente
* buscaDadosClienteByCPFCNPJ: Lista de clientes e suas informações cujo CPF e/ou CNPJ combinem com o informado.
* buscaDadosClienteByTelefone: Lista de clientes e suas informações cujo telefone combina com o informado.
* buscaDadosContatoClienteByTelefone: Lista de contatos e suas informações (algumas informações do cliente do contato) cujo telefone combina com o informado.
* buscaEmailAtendente: e-mail do atendente.
* buscaRamalUsuario: Ramal do usuário (que deve estar associado a um atendente).
* criarAtendimento: Cria um novo atendimento no TOTVS Gestão do Relacionamento com o Cliente.
* criarAtendimentoCliente: Cria um novo atendimento no TOTVS Gestão do Relacionamento com o Cliente.
* criarAtendimentoSimples: Cria um novo atendimento no TOTVS Gestão do Relacionamento com o Cliente.
* criarAtendimentoWorkflow: Cria um novo atendimento no TOTVS Gestão do Relacionamento com o Cliente.
* encaminharAtendimentoParaAtendente: Repassa/Encaminha um determinado atendimento para um atendente ou grupo de atendente possibilitando prover algumas informações adicionais.
* encaminharAtendimentoParaUsuario: Repassa/Encaminha um determinado atendimento para um atendente ou grupo de atendente possibilitando prover algumas informações adicionais.
* sendMail: Envia e-mail.

### **6. Conceitos do TOTVS Business Connect (wsConConceito)**

Este serviço disponibiliza métodos para integração com o Conceito do TOTVS Business Conector.  
 A ferramenta Conceito e os Web Services (WS) do TBC são independentes, mas tanto pode usar um WS como destino de um Conceito, como pode usar o "wsConConceito" para executar um Conceito existente.   
   
**WebMethods:**

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP criando um Token para isto. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=82477609#ComoexporosWebServicesdoRMatrav%C3%A9sdoIIS-3.Autentica%C3%A7%C3%A3o).
* ExecutarConceito: Executa um conceito pré-cadastrado, conforme o identificador informado.

### **7. Lançamento Financeiro (wsFin)**

O WebService do TBC (Totvs Business Conector) irá proporcionar aos clientes o uso de um Web Method para realizar lançamentos financeiros. O Web Service não irá comunicar diretamente com o módulo financeiro, antes será preenchido um DataServer do TBC, onde os dados serão pré-validados e entregue ao financeiro no formato esperado. O módulo financeiro não sofrerá alteração para esta integração.  
Com o objetivo de padronizar a integrações com os produtos TOTVS, foi definida uma nova diretriz para os projetos de integração, a de que todos os produtos TOTVS devam trabalhar com uma mensagem XML única evitando, desta forma, o processo de transformação de mensagens.  
Neste contexto, qualquer produto TOTVS trabalhará com o mesmo XML para uma mesma entidade. Uma vez que os vários produtos TOTVS terão a plataforma de mensagem única, as integrações entre estes produtos não exigirão mais que as mensagens sejam transformadas de um formato para outro. Baseando nisto o Web Method de Lançamento Financeiro será consumido passando como parâmetro um Xml, este por sua vez, será validado, transformado e por fim enviado a Base de Dados da Linha RM.

Saiba mais sobre **Transformação**, **clicando aqui.**  
   
**Recursos:**

Os recursos do Web Method no TBC são:

* **Inclusão**
* **Baixa e Exclusão de Lançamentos Financeiros**

**Observação:**

A alteração de lançamentos não está contemplada. Em alternativa pode ser feita uma exclusão seguida de uma inclusão com os dados já alterados.  
   
**Pré-requisitos:**

Os pré-requisitos para uso adequado deste Web Method, são:

* Ter a Biblioteca RM na versão 11.50 ou superior.
* Ter o TOTVS Business Conector devidamente instalado/configurado.
* A base de dados deve obrigatoriamente possuir o Novo Modelo de Baixa (Para o cliente possuir este recurso o mesmo deve entrar em contato com o Suporte da Linha RM, produto Gestão Financeria), caso o cliente tente utilizar este Web Service no modelo antigo de baixa, o recurso **não irá funcionar.**

### **8 - Totvs Gestão Hospitalar (wsSau)**

Este serviço disponibiliza métodos para integração com o TOTVS Gestão Hospitalar.

Endereço WSDL:   <http://localhost:8051/wsSau/mex?wsdl>

Os webservices foram migrados do “TBC via IIS” para “TBC via Host”, disponibilizados em <http://localhost:8051/wsSau/mex?xsd=xsd0>, conforme comunicação citada em <https://centraldeatendimento.totvs.com/hc/pt-br/articles/9198729724439-Aviso-de-substitui%C3%A7%C3%A3o-Integra%C3%A7%C3%A3o-TBC-via-IIS-para-TBC-via-Host-Linha-RM>

   
**WebMethods:**

### **8.1 - Painel de Chamadas**

* AutenticaAcesso: Autentica o usuário no ambiente RM. O usuário e senha devem ser informados via SOAP criando um Token para isto. [Mais informações](https://tdn.totvs.com/pages/viewpage.action?pageId=82477609#ComoexporosWebServicesdoRMatrav%C3%A9sdoIIS-3.Autentica%C3%A7%C3%A3o).
* getUnidadesAtendimento: Busca unidades de atendimentos que realizam classificação de risco.
* getSenhaPainel:  Busca a próxima senha a ser chamada.
* getSenhaPainelString: Busca a próxima senha a ser chamada.
* getFilas: Busca as últimas senhas chamadas
* setSenhaChamada: Atualiza que a senha já foi chamada
* TempoEntreChamadas: Tempo em segundos entre uma chamada e outra
* getTotens: Busca Totens configurados
* ObterChaveGoogleApi: Obtém chave Google API
* getXmlUnidadesToten: Busca unidades do Toten selecionado

Documentação para instalação do Painel de Chamadas: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025267612-RM-SAU-Painel-de-chamadas>

### **8.2 – Resultado OnLine de Exames**

* AutenticaAcesso: Autentica o usuário

* GetListaExames: Método que lista os exames de um pedido.  Obrigatório estar marcado o Parâmetro Geral/Unidade de Diagnóstico II – Resultado de Exames Online:  “Disponibiliza resultados online?”

* GetResultadoExame:  Método que retorna o resultado do exame. Obrigatório estar marcado o Parâmetro Geral/Unidade de Diagnóstico II – Resultado de Exames Online:  “Disponibiliza resultados online?”

* getResultadoExame: Método que retorna o resultado do exame.

Conforme parametrização do sistema, este método poderá retornar:

Resultado de Exames da Integração: AgileWork, Matrix, Tuxxon.

Gerar Relatório de Evolução de Exames.

Gerar Arquivo de Resultado OnLine.

### **8.3 – Integração com BackOffice EMS Datasul**

* AutenticaAcesso: Autentica o usuário
* RetrieveMessage: Grava um arquivo XML na fila de Integração com EMS Datasul.

Transforma uma mensagem recebida no formato do EAI do Datasul em mensagem com o cabeçalho de mensageria Padrão Totvs. Desta forma o RM está pronto para receber mensagens no formato do EMS.

### **8.4 –**Integrações Diagnóstico por Imagem (RIS/PACS) - antigo wsIntegracaoRIS

* AutenticaAcesso: Autentica o usuário
* AtualizaStatusExame: Recebe e registra o recebimento do exame com Imagem e Laudos confeccionados.

Documentação para configuração: <https://tdn.totvs.com/x/olV0Ig>

### **8.5 –** Integração com LIS da SISLAB - antigo wsIntegracaoSILAB

* AutenticaAcesso: Autentica o usuário
* CriaAtendimentoSILAB: O método Cadastra Atendimento/Faturamento no Totvs Gestão Hospitalar através da Integração com sistema SILAB
* CancelaAtendimentoSILAB: O método Cadastra Atendimento/Faturamento no Totvs Gestão Hospitalar através da Integração com sistema SILAB.

### **8.6 –**Integração com SANE - antigo wsIntegracaoSANE

* AutenticaAcesso: Autentica o usuário
* RegistroAtendimentoTOTVS: O método realiza o Registro de Atendimento no TOTVS Gestão Hospitalar através da Integração com SANE
