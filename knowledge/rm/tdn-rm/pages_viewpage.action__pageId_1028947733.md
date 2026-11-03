---
content_hash: 2d8b031832ad687df6452653e1dc05c7fb6daa5385ea05113a498198e938b4ac
fetched_at: '2026-06-29T00:05:48.795420+00:00'
page_id: '1028947733'
product: rm
source: tdn-rm
title: Integração TOTVS Folha de Pagamento (RM) e TOTVS Atração de Talentos (ATS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1028947733
version: 49
---

false

**A partir das Versões:**

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

A integração entre o sistema TOTVS Folha de Pagamento (RM) e TOTVS Atração de Talentos (ATS) representa um avanço significativo na digitalização do RH, eliminando processos manuais e a redigitação de informações. Utilizando a tecnologia SmartLink, a comunicação entre as plataformas ocorre de forma automatizada e segura: assim que a contratação de um candidato é aprovada no ATS, seus dados são enviados para uma fila de integração. No RM, um consumer (serviço de consumo) monitora essa fila, processa as informações e as armazena em uma tabela de transição.

O grande diferencial operacional desta melhoria está na etapa final da admissão. No módulo de Folha de Pagamento, ao cadastrar um novo funcionário, o usuário conta com a funcionalidade "Localizar Pessoa", que agora está vinculada diretamente à tabela alimentada pelo ATS. Isso permite que os dados do candidato sejam importados instantaneamente, garantindo agilidade no onboarding, redução de erros de digitação e total conformidade com os dados validados durante o processo seletivo.

## **02. EXEMPLO DE UTILIZAÇÃO**

1true1ParametrizaçãoParametrização

### 1 - Configurações para recepção

O License Server deve estar configurado para apontar para o ambiente correspondente, a fim de garantir a comunicação adequada com o Smart Link e a correta recepção das informações.

### 2 - Criar a instalação localmente no ERP

Essa etapa é necessária para criar a fila que será utilizada pelo ATS para o envio dos dados.

Para mais informações, consulte a documentação detalhada: .

Informe o seu **tenantId** (código gerado durante a ativação do Smart Link) ao responsável pelo ATS. Com base nesse ID, será configurado o ambiente correspondente e enviados os eventos que deverão ser consumidos pelo ERP.  
  
Exemplo:

### 3 - Parametrização da integração com o ATS

Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | 06.02 – Integrações | 06.02.12 – ATS e realize a parametrização da integração conforme a necessidade do ambiente.

ATENÇÃO:

* É necessária a execução do sistema **RM.Atualizador.exe** para a criação da nova tabela utilizada no processo.
* Após a ativação da integração, o sistema passa a localizar o candidato na tabela **PATSCANDIDATO**.
* As mensagens recebidas do **ATS** também são armazenadas na tabela **PATSCANDIDATO**.
2AdmissãoAdmissão

### Abaixo a demonstração da utilização da integração:

**1 –** Acesse o menu Administração de Pessoal | Funcionários | Incluir.

**2 –** Na aba **Identificação**, clique em **Localizar Pessoa / Registro Preliminar**.

**3 –** Será exibida uma nova tela com o pré-cadastro proveniente doATS. Informe o nome, e-mail ou CPF e clique em **Localizar**. Em seguida, selecione o candidato que será admitido e clique em **OK**.

**4 –** Para filtrar exclusivamente colaboradores do **Registro Preliminar**, acesse a tela **Pré-cadastro** e habilite a opção **'Exibir somente pessoas com registro preliminar'**. Após a ativação do filtro, execute a consulta via ícone de pesquisa, selecione o registro pertinente para a admissão e confirme a operação clicando em 'OK'."

ATENÇÃO:

* A integração trará automaticamente aos dados do cadastro do candidato conforme o cadastro do candidato no ATS.
* Para a conclusão da admissão, será necessário o preenchimento dos demais campos obrigatórios no cadastro do funcionário.
* No momento, a integração ainda **não realiza a conclusão das requisições de admissão criadas a partir do TOTVS Gestão de Pessoas**. Assim que essa funcionalidade estiver disponível, comunicaremos por meio das nossas novidades.
4DE | PARADE | PARA

O sistema irá preencher automaticamente os dados no ERP, desde que tenham sido enviados pela integração, conforme o **De/Para** apresentado abaixo.

| Item | CAMPOS | CAMPOS DA TABELA RM | CAMPOS DA TABELA PATSCANDIDATO | CAMPOS JSON ATS |
| --- | --- | --- | --- | --- |
| 1 | Data de admissão | PFUNC.DATAADMISSAO | DATAADMISSAO | ``` hiringDate ``` |
| 2 | Nome do candidato | PFUNC.NOME | NOME | fullName |
| 3 | Nome Social | PPESSOA.NOMESOCIAL | NOMESOCIAL | socialName |
| 4 | CPF do candidato | PPESSOA.CPF | CPF | cpf |
| 5 | E-mail do candidato | PPESSOA.EMAIL | EMAIL | email |
| 6 | Data de nascimento | PPESSOA.DTNASCIMENTO | DTNASCIMENTO | birthday |
| 7 | Telefone | PPESSOA.TELEFONE1 | TELEFONE | telephoneNumber |
| 8 | CEP | PPESSOA.CEP | CEP | address.zipCode |
| 9 | Cidade | PPESSOA.CIDADE | CIDADE | address.cityName |
| 10 | Estado | PPESSOA.ESTADO | ESTADO | address.stateSmallName |
| 11 | Rua | PPESSOA.RUA | RUA | address.street |
| 12 | Complemento | PPESSOA.COMPLEMENTO | COMPLEMENTO | address.complement |
| 13 | Bairro | PPESSOA.BAIRRO | BAIRRO | address.neighborhoodName |
| 14 | Sexo | PPESSOA.SEXO | SEXO | gender |
| 15 | Deficiência Física | PPESSOA.DEFICIENTEFISICO | DEFICIENTEFISICO | diversity.physical |
| 16 | Deficiência visual | PPESSOA.DEFICIENTEVISUAL | DEFICIENTEVISUAL | diversity.visual |
| 17 | Deficiência auditiva | PPESSOA.DEFICIENTEAUDITIVO | DEFICIENTEAUDITIVO | diversity.auditory |
| 18 | Deficiência intelectual | PPESSOA.DEFICIENTEMENTAL | PPESSOA.DEFICIENTEINTELECTUAL | DEFICIENTEINTELECTUAL | diversity.intellectual |
| 19 | CNPJ unidade | GFILIAL.CGC | CNPJUNIDADE | facility.cnpj |
| 20 | Código da área/departamento | PFUNC.CODSECAO | PSECAO.CODIGO | CODSECAO | department.integrationId |
| 21 | Código do cargo | PFUNC.CODFUNCAO | PFUNCAO.CODIGO | CODFUNCAO | position.integrationId |
| 21 | Regime de contratação CLT | PFUNC.CODTIPO | REGIMECONTRATACAOCLT | isCLT |
| 23 | Regime de contratação Pessoa jurídica | PFUNC.CODTIPO | REGIMECONTRATACAOPJ | isPJ |
| 24 | Regime de contratação Estágio | PFUNC.CODTIPO | REGIMECONTRATACAOESTAGIO | IsInternship |

false⚠️ OBSERVAÇÃO:

É uma premissa da integração que o campo **CNPJ** esteja devidamente preenchido no cadastro da empresa no **ATS**, pois a **Folha de Pagamento** identifica a coligada/empresa por meio dessa informação. Caso o CNPJ não esteja informado, o candidato **não será integrado**. Para mais detalhes sobre como preencher o CNPJ no ATS, acesse o link

## **03. TABELAS UTILIZADAS**

* PATSCANDIDATO

## **04. DOCUMENTAÇÃO**
