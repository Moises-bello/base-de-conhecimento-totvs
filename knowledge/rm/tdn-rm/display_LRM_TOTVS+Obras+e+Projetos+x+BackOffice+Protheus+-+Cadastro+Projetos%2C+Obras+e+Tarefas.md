---
content_hash: 664f143b285b33579c2d895f143b61b75e5ea3f8559d757f7613277fe6673f26
fetched_at: '2026-06-29T00:09:38.011673+00:00'
page_id: '425459670'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Projetos, Obras e Tarefas
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Obras+e+Projetos+x+BackOffice+Protheus+-+Cadastro+Projetos%2C+Obras+e+Tarefas
version: 2
---

**TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Projetos, Obras e Tarefas**

---

Após os cadastros básicos serem integrados, é possível realizar a inclusão de um projeto, obras e tarefas no TOP. A inclusão, alteração e exclusão do cadastro são realizadas no TOP e podem ser visualizadas no Protheus somente para referência nos lançamento e títulos.   
    
 Para incluir, alterar ou excluir um projeto, acesse: RM | Projetos | Construção e Projetos | Selecionar Projeto  
 Para incluir, alterar ou excluir obras e tarefas, selecione o projeto e acesse: RM | Projetos | Construção e Projetos | Cadastros | Atividades  
 Para visualizar os projetos, obras e tarefas sincronizados para o Protheus, acesse: Protheus| SigaEst | Atualizações | Estoques | Solicitação de Armazém   
    
 Dentro da visão de cadastro da solicitação clique no botão "Projetos". Após, dê um duplo clique no campo "Projetos", e uma visão será aberta listando todos os projetos sincronizados do TOP. Abaixo do campo "Projetos", está disponível o campo "Tarefas". Dê um duplo clique no campo e será aberta uma visão listando todas as tarefas do projeto selecionado anteriormente.   
    
 Os parâmetros do projeto serão preenchidos automaticamente pela integração na criação de um novo projeto, não sendo possível alterá-los manualmente. Para visualizar estes parâmetros acesse: RM | Projetos | Construção e Projetos | Opções | Construção e Projetos | Projetos | Integração | Suprimentos e Faturas | Geral  
    
 Abaixo são listados os parâmetros e seus respectivos valores.

* INTEGRADONUCLEUS = 1
* TIPOMOVESTOQUE = 1.1.01
* NUCLEUSTIPOMOVHISTORICO = 1.1.02
* UTILIZARATEIOCC = 1
* TIPOMOVNUCLEUSCOTACAO = 1.1.01
* NUCLEUSTIPOMOVREQ = 1.1.01
* NUCLEUSTIPOMOVADIA = 1.2.02
* NOMENUCLEUSTIPOMOVREQ = Solicitacao de Armazem
* USATIPOMOVNUCLEUSCOTACAO = 1
* USANUCLEUSTIPOMOVHISTORICO = 1
* USANUCLEUSTIPOMOVCOMPRA2 = 1
* NOMENUCLEUSTIPOMOVCOMPRA2 = Solicitacao de Compra
* NUCLEUSTIPOMOVCOMPRA2 = 1.1.03

**Dados Sincronizados**  
    
 São sincronizadas para o Protheus apenas as informações mínimas dos projetos e tarefas cadastrados no TOP, para que seja possível a posterior vinculação às solicitações de compra e outras movimentações. São elas:

* Código
* Descrição
* Valor

**Pré-Requisitos**

* Ter realizado o sincronismo de Empresa / Filial

*Observações:*

* Esta integração é a única que ocorre de maneira assíncrona, sendo necessário executar um módulo qualquer para que o projeto seja visualizado no Protheus.

**Dica:** é possível criar um botão chamado "**Sincronismo de Projetos**" como alternativa do procedimento citado anteriormente. Para mais detalhes, **clique aqui**.

* Os projetos sincronizados serão aqueles cujo status estiver configurado nos parâmetros da integração. Por default, todos os status serão sincronizados. Caso um projeto passe para um status que não está definido como integrado, o mesmo será excluído do Protheus.
* A função de Projeto Global não poderá ser utilizada, e o código do projeto não poderá ser alterado.
* No processo de importação de produto para insumo, do TOP, as pastas "por classificação" e "por faixa de fornecedor" estarão desabilitadas.
* O campo "departamento" estará desabilitado no TOP, pois este conceito não existe no Protheus.
* O projeto só será sincronizado após o preenchimento da filial.
* O projeto será sincronizado no momento de login ou ao acessar algum modulo do Protheus, na mesma filial definida no projeto.
