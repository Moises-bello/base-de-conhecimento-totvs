---
content_hash: ee673c5b69a9691714e02feb4e22466c0246f2426186b993245ce206ada10c32
fetched_at: '2026-06-29T00:08:33.064160+00:00'
page_id: '274300931'
product: rm
source: tdn-rm
title: RMEDU00005_Solicitações - Portal do Aluno - TOTVS Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274300931
version: 14
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | 12.1.34 e Superiores |
| **Processo:** | Integração TOTVS Educacional x CRM |

**TOTVS Educacional X CRM**

Possibilita a inclusão de Solicitações para Alunos no TOTVS Educacional ou Portal Acadêmico, criando um atendimento no TOTVS Gestão de Relacionamento com Clientes.

**Requisitos:**

****TOTVS Educacional****

Alunos com Matricula no Período Letivo e contrato Ativo

Ao gerar o usuário de acesso ao portal é **indispensável** informar um perfil de acesso ao CRM

****TOTVS Gestão de Relacionamento com o Cliente****

Atendente, Grupos de Atendimento, tipos de Atendimento

***TOTVS Gestão de Relacionamento com o Cliente***

***WorkFlow |******Tipos***

O tipo de atendimento deve ser associado ao serviço (Serviços Educacionais (RM Classis Net)) no serviço do tipo de atendimento.

Caso este serviço não apareça para vinculação, deve-se rodar um script na base de dados para criação.

 

INSERT INTO HSERVICODOTIPOATENDIMENTO (IDDLL, NOME, APLICATIVO, NOMEDLL, RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY, RECMODIFIEDON)  
VALUES (10 ,'Serviços Educacionais (RM Classis Net)', 'AG', 'RM.Edu.ServicosCRMEB', NULL, NULL, NULL, NULL)

O tipo de atendimento deve ter um prazo inicial e final, a mesma define o período que o atendimento poderá ser utilizado

É necessário para cada tipo de atendimento definir um local de entrega

Código da filial, Localidade e Descrição do local

No local de entrega Podemos definir um valor para cobrança em Anexos -> Preços

Cadastrar cada etapa do atendimento, e para cada etapa, podem-se definir as ações do atendimento, campos obrigatórios, etc.

Os parâmetros;

Ativar Tarefa, Etapa Padrão e Primeira etapa de um possível Fluxo são obrigatórios para a primeira etapa.

Definir o Fluxo de etapas, para as etapas criadas anteriormente é necessário ser definido um fluxo para o andamento da solicitação criada. 

Nas imagem abaixo detalhamos o cadastro do fluxo de etapas do atendimento.

Definir a etapa inicial do Fluxo

Definir o Motivo para a passagem para a próxima etapa

Definir a próxima etapa do atendimento

Definir o motivo do repasse

O motivo do repasse pode ser cadastrado conforme a necessidade da instituição

As instruções demonstradas abaixo não são de utilização obrigatória, porem algumas instituições utilizam para a solicitação de 2ª Chamada

Cadastrar o parâmetro do tipo de atendimento

O parâmetro exigido quando marcado informa que para dar sequencia no atendimento é necessário informar o valor desejado

Neste caso utilizaremos uma consulta SQL para buscar as disciplinas em que o aluno esteja com uma determinada situação de matricula no Período Letivo atual

SQL - Modelo

SELECT DISTINCT SDISCIPLINA.NOME, SDISCIPLINA.CODDISC  
FROM SMATRICULA (NOLOCK)   
INNER JOIN STURMADISC (NOLOCK)   
ON   
SMATRICULA.CODCOLIGADA = STURMADISC.CODCOLIGADA   
AND   
SMATRICULA.IDPERLET = STURMADISC.IDPERLET   
AND   
SMATRICULA.IDTURMADISC = STURMADISC.IDTURMADISC   
INNER JOIN SDISCIPLINA (NOLOCK)   
ON   
STURMADISC.CODCOLIGADA = SDISCIPLINA.CODCOLIGADA   
AND   
STURMADISC.CODDISC = SDISCIPLINA.CODDISC   
INNER JOIN SPARAM (NOLOCK)   
ON   
SMATRICULA.CODCOLIGADA = SPARAM.CODCOLIGADA   
AND   
STURMADISC.CODTIPOCURSO = SPARAM.CODTIPOCURSO   
AND   
SMATRICULA.IDPERLET = CAST(SPARAM.TEXTO AS INT)   
WHERE SPARAM.ID = 'IDPERLET'   
AND   
SMATRICULA.CODCOLIGADA = :CODCOLIGADA   
AND   
SMATRICULA.RA = :RA   
AND   
SMATRICULA.IDPERLET = :IDPERLET

*WorkFlow*|***Grupos***

Cadastrar o Grupo de atendimento

Anexos -> Tipos de Atendimento

***TOTVS Educacional***

Acessar o TOTVS Educacional

***Atividades Academicas | CRM | Configurações***

Configurar o tipo de atendimento vinculando-o a um serviço cadastrado no TOTVS Educacional.

Detalhamento da configuração do Tipo de Atendimento

No parâmetro abaixo deve ser informado o Tipo de Atendimento criado no CRM

O atendimento pode gerar cobrança financeira, para tal é necessário inserir um serviço, tendo valor informado.

Para que seja inserido um serviço extra no contrato do aluno é necessário que o parâmetro abaixo seja habilitado

O financeiro pode ser gerado através do valor informado no Serviço ou no Preço definido no local de entrega, para tal é necessário que o parâmetro seja habilitado.

Para validar débitos do aluno antes do atendimento ser inserido é necessário que o parâmetro abaixo seja habilitado

***Configurações*|*Parâmetros*|*Integração*| *Atendimento***

 Configurar a integração 

 Opções para a parametrização

* Utilizar a data de vencimento dos contratos com dia Fixo, respeita o dia fixo definido no contrato para inserir o vencimento da parcela quando a solicitação gera lançamento financeiro.

* Enviar e-mail ao solicitante na abertura do atendimento, Permite parametrizar o sistema para enviar e-mail ao confirmar a solicitação.

* Calcular automaticamente a data de vencimento da parcela, ao selecionar o parâmetro é necessário definir o número de dias após a data da solicitação para o vencimento da parcela.

* Definir parâmetros para inclusão do atendimento no TOTVS Gestão de Relacionamento com o Cliente

* É necessário inserir o Período Letivo, Data da solicitação deve ser informado uma data ATÉ (Exemplo solicitações inseridas até aquela data vencem na parcela informada), data de vencimento não é obrigatório pois o vencimento pode respeitar os parâmetros anteriores.

***Atividades Acadêmicas |******CRM | Solicitações***

Inclusão de Solicitações pelo EXE.

Parcela e lançamento financeiro criado através da solicitação inserida no Contrato do Aluno.

*Inclusão de Solicitação através do Portal do Aluno*

Acesso ao Portal
