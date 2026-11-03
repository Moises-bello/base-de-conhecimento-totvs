---
content_hash: ec5a2497998addcadc60635ef4a76f9b993a61f6d22561cd7b251992220fe18f
fetched_at: '2026-06-29T00:08:21.550487+00:00'
page_id: '269059271'
product: rm
source: tdn-rm
title: DT_Integreção_Saida_Inteligente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269059271
version: 18
---

# Integração TOTVS Educacional X Saída Inteligente

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Educacional | | |
| **Módulo:** | ***TOTVS Educacional*** | | |
| **Rotina:** | | **Rotina** | **Nome Técnico** | | --- | --- | | Cadastro Unidade de Ponto | Cadastro Unidade de Ponto | | Exportar dados aluno para a aplicação Saída Inteligente | Exportar dados aluno para a aplicação Saída Inteligente | | Sincronizar dados aluno para a aplicação Saída Inteligente | Sincronizar dados aluno para a aplicação Saída Inteligente | | Matricula no período letivo (exclusão de registro) | Mensagem de exclusão para a aplicação Saída Inteligente | | Parâmetros do Educacional | Parâmetros do Educacional | | | |
| **Requisito (ISSUE):** | [EDUEDU001-890](http://jiraproducao.totvs.com.br/browse/EDUEDU001-890) | | |
| **País:** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | **Disponível para todos os clientes a partir dos patchs: 12.1.31.242 | 12.1.32.177  | 12.1.33.107** | | |

### Objetivo

A integração do TOTVS Educacional com o Saída Inteligente foi criada para permitir que os responsáveis do aluno possam ter informações a respeito da saída dos alunos. 

 Esta integração é dividida em dois processos principais:

* Exportação de dados do TOTVS Educacional para o Saída Inteligente
* Sincronização de dados do TOTVS Educacional para a aplicação Saída Inteligente

O processo de exportação de dados para o Saída Inteligente permite que o usuário selecione os alunos/responsáveis que devem ser enviados possibilitando a definição do responsável principal do aluno. O processo possibilita o envio de fotos dos alunos/responsáveis para o FTP da aplicação de Saída Inteligente.

O processo de sincronização de dados para o Saída Inteligente é um processo que mapeia as alterações de situação de matrícula, alteração de unidade de ponto, ou alteração de dados do aluno e reenvia os dados alterados desde a última sincronização realizada com sucesso. O processo possibilita o envio de fotos dos alunos/responsáveis para o FTP da aplicação de Saída Inteligente.

 

### Definição da Regra de Negócio

# Parametrização de integração com a Saída Inteligente

Acessar**: Módulo Educacional | Parâmetros| Integração | Saída Inteligente**

* Selecione “Utiliza integração com a Saída Inteligente”.
* Usuário/Projeto.
* Senha.
* WebService de manutenção dos dados de aluno e responsáveis
* Endereço FTP para envio das fotos dos alunos.
* Enviar apenas alunos e responsáveis com código de usuário gerado.
* Data de última sincronização com sucesso.

**É necessário parametrizar todos campos para que seja possível exportar com sucesso, pois existem informações que são validadas no TOTVS Educacional durante o processo.** 

# Cadastro Unidade de Ponto

 Acessar**: **Módulo Educacional | Integrações | Saída Inteligente| Cadastro Unidade de Ponto**** 

* Este cadastro possibilita ao usuário cadastrar as unidades de ponto da instituição de ensino.

* Para que o aluno possa ser enviado para o Saída Inteligente a sua turma deverá possuir a definição da unidade de ponto, para tanto basta acessar o cadastro da Turma (**Currículo e Oferta | Turmas**) e informar a Unidade de Ponto:

* No processo de cadastro rápido de turmas e turmas/disciplinas (**Atividades Acadêmicas | Assistentes | Cadastro rápido de Turmas|Turmas/Disciplinas**) o usuário já poderá definir a unidade de ponto.

                                                                                                         

* O processo para copiar turmas entre períodos letivos também leva em conta o novo campo, desta forma a turma criada terá a mesma informação de unidade de ponto da turma original. (**Currículo e Oferta | Turmas | Copiar turmas entre período letivo**)

# Exportação de Dados para a Saída Inteligente

Acessar:**Módulo Educacional | Integrações | Saída Inteligente | Exportar dados aluno para a aplicação Saída Inteligente**

* + O usuário poderá realizar um filtro para seleção dos alunos matriculados no período letivo, lembrando que apenas alunos cujas turmas tenham unidade de ponto definida serão listados.
    - Como padrão o responsável principal do aluno será o "Responsável Acadêmico", no entanto, o usuário poderá no processo definir que o responsável principal é uma pessoa com outro papel (Papéis disponíveis: Pai, Mãe, Responsável Acadêmico e Responsável Financeiro). Para aplicar um novo papel para o responsável basta selecionar o pepel desejado e "Aplicar para todos". O botão "Remover" possibilita a exclusão de alunos da lista que será enviada para o Saída Inteligente.
  + O usuário poderá optar por também enviar as fotos dos alunos e responsáveis marcando a opção  "Enviar fotos dos alunos e responsáveis".

* + Execute o processo, ao final, os dados já estarão disponíveis na aplicação de Saída Inteligente

# Sincronização de Dados para a Saída Inteligente

Acessar:**Módulo Educacional | Integrações | Saída Inteligente | Sincronizar dados aluno para a aplicação Saída Inteligente**

* + O processo permite a definição de uma hierarquia para busca do responsável principal, desta forma o sistema sempre tentará encontrar um responsável que exerça o primeiro papel definido na lista e caso não seja encontrado é verificado o próximo. Também é possível parametrizar o envio da fotos dos alunos e responsáveis marcando a opção "Enviar fotos dos alunos  e responsáveis"
  + O processo poderá ser agendada.

* + Execute o processo, ao final, os dados já estarão disponíveis na aplicação de Saída Inteligente.

# Mensagem de exclusão para a aplicação Saída Inteligente

Acessar:**Módulo Educacional | Matrícula e Avaliação | Matrículas**

O sistema deve enviar uma mensagem de exclusão do aluno para o aplicativo de Saída Inteligente quando:

* Houver uma exclusão da matricula do aluno no período letivo
* O sistema estiver parametrizado para integrar com a Saída Inteligente
* O aluno não possuir nenhuma matricula ativa neste período letivo

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro Unidade de Ponto | Criação | Integrações -> Saída Inteligente -> Cadastro Unidade de Ponto | - |
| Exporta aluno/responsável para a aplicação Saída Inteligente | Criação | Integrações -> Saída Inteligente -> Exporta aluno/responsável para a aplicação Saída Inteligente | - |
| Sincronizar aluno/responsável para a aplicação Saída Inteligente | Criação | Integrações -> Saída Inteligente -> Sincronizar aluno/responsável para a aplicação Saída Inteligente | - |
| Exclusão de Matricula | Alteração | Envio de Mensagem de Exclusão para a aplicação Saída Inteligente |  |
| Parâmetros do TOTVS Educacional | Alteração | Configurações -> Parâmetros |  |
