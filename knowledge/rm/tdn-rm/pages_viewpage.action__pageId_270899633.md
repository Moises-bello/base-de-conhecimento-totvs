---
content_hash: 22286ed8f13576fda9aa89dc67d42436d0033e80acdb98fdca6d8571ed5c3627
fetched_at: '2026-06-29T00:08:24.672668+00:00'
page_id: '270899633'
product: rm
source: tdn-rm
title: Portal do Aluno - Solicitações - Integração com o Gestão de Relacionamento
  com o Cliente(TAA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270899633
version: 14
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.2205 e superiores |
| **Processo:** | Inclusão de Solicitação para Aluno |

**TOTVS Educacional X Gestão de Relacionamento com Clientes**

Possibilita a inclusão de Solicitações para Alunos criando um atendimento no TOTVS Gestão de Relacionamento com Clientes.

**Requisito:**

Alunos com Matricula no Período Letivo e contrato Ativo

***TOTVS Gestão de Relacionamento com o Cliente***

***WorkFlow |*** ***Tipos***

Cadastrar o Tipos de Atendimentos que serão listados no portal para que o aluno selecione ao realizar uma solicitação.

 

O tipo de atendimento deve ser associado ao serviço (Serviços Educacionais (RM Classis Net)) no serviço do tipo de atendimento.

O tipo de atendimento deve ter um prazo inicial e final.

Caso este serviço não apareça para vinculação, deve-se rodar um script na base de dados para criação.

 

INSERT INTO HSERVICODOTIPOATENDIMENTO (IDDLL, NOME, APLICATIVO, NOMEDLL, RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY, RECMODIFIEDON)  
VALUES (10 ,'Serviços Educacionais (RM Classis Net)', 'AG', 'RM.Edu.ServicosCRMEB', NULL, NULL, NULL, NULL)

É necessário para cada tipo de atendimento definir um local de entrega

Código da filial, Localidade e Descrição do local

É necessário definir etapas para o atendimento, para a primeira etapa é obrigatório parametrizar que é a primeira etapa de um possível fluxo.

Cadastrar cada etapa do atendimento, e para cada etapa, podem-se definir as ações do atendimento, campos obrigatórios, etc.

Os parâmetros;

Ativar Tarefa, Etapa Padrão e Primeira etapa de um possível Fluxo são obrigatórios para a primeira etapa.

Definir o Fluxo de etapas, para as etapas criadas anteriormente é necessário ser definido um fluxo para o andamento da solicitação criada. 

 

Na imagem acima o fluxo do atendimento foi definido com a etapa inicial e a próxima etapa para o tratamento do atendimento.

**Duvidas sobre cadastros de etapas e Fluxos, gentileza entrar em contato com a equipe de Suporte do TOTVS Gestão de Relacionamento com o Cliente.**

*WorkFlow* |***Parâmetros***

Para disponibilizar um Tipo de Atendimento no Educacional e Portal Acadêmico é necessário que exista o vínculo do Tipo de Atendimento com o Grupo de Atendimento. O cadastro é feito em Cadastros / Atendimentos / Grupo de atendimento.

Podemos criar um novo Grupo ou utilizar um já existente

Acessando o Grupo - Anexos - Tipo de Atendimento do Grupo de atendimento neste caminho vinculamos o tipo de atendimento ao grupo a ser utilizado.

***TOTVS Educacional***

***Atividades Acadêmicas |******Configurações***

Configurar o tipo de atendimento vinculando-o a um serviço cadastrado no TOTVS Educacional.

A Solicitação pode ou não gerar cobrança financeira para o Responsável financeiro do aluno, para isso observar os detalhes abaixo

O serviço vinculado ao atediamento deve ter o campo valor preenchido

A Cobrança pode também buscar o valor do Local de entrega

Para validação de onde buscar e se será inserido o lançamento observar os parâmetros

O parâmetro "Verifica inadimplência" valida débitos financeiros para o aluno na instituição e havendo impossibilita que o aluno prossiga com requerimento.

*Configurações* | *Parâmetros* | *Integração* | ***Atendimento***

Configurar a integração 

Opções para a parametrização

* Utilizar a data de vencimento dos contratos com dia Fixo, respeita o dia fixo definido no contrato para inserir o vencimento da parcela quando a solicitação gera lançamento financeiro.

* Enviar e-mail ao solicitante na abertura do atendimento, Permite parametrizar o sistema para enviar e-mail ao confirmar a solicitação.

* Calcular automaticamente a data de vencimento da parcela, ao selecionar o parâmetro é necessário definir o número de dias após a data da solicitação para o vencimento da parcela.

* Definir parâmetros para inclusão do atendimento no TOTVS Gestão de Relacionamento com o Cliente

* É necessário inserir o Período Letivo, Data da solicitação deve ser informado uma data ATÉ (Exemplo solicitações inseridas até aquela data vencem na parcela informada), data de vencimento não é obrigatório pois o vencimento pode respeitar os parâmetros anteriores.

***Atividades Acadêmicas |*** ***Requerimentos***

* Avançar o processo

* Selecionar o Grupo, Tipo de Atendimento

* Informar Período Letivo, Aluno e Contrato

* Informar Local de Entrega e Justificativa

No exemplo acima o campo "Seleção de Disciplinas" é um parâmetro criado no Tipo de Atendimento.

* Informar Parcela, Cota a data de vencimento é calculada automaticamente conforme parametrização podendo ser alterada o valor é informado no serviço podendo ser alterado.

No formulário acima o campo "Data Vencimento" deve possuir um valor válido entre 01/01/1753 e 31/12/9999.

* Executar o Processo

Atendimento criado no CRM

Lançamento financeiro gerado no contrato do Aluno.
