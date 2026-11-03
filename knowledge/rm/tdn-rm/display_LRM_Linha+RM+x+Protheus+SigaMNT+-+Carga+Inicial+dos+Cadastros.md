---
content_hash: a2e34dd42867cb69d00433b53320657c4b6363ef38bce5d57b3c11cb04413bd3
fetched_at: '2026-06-29T00:09:35.375391+00:00'
page_id: '425459332'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Carga Inicial dos Cadastros
type: documentation
url: https://tdn.totvs.com/display/LRM/Linha+RM+x+Protheus+SigaMNT+-+Carga+Inicial+dos+Cadastros
version: 2
---

**Linha RM x Protheus SigaMNT - Carga Inicial dos Cadastros**

---

Para que a carga inicial de dados existentes em bases de dados seja executada, é necessário que alguns pré-requisitos sejam obedecidos para sucesso do processo.

1. **Cadastrar Atividade responsável por controlar a Carga Inicial de dados da integração Linha RM x Protheus SigaMNT.**

**Passo 1:** Acesse: RM / Integração

**Passo 2:** Acesse: Gestão / Fórmula Visual / Atividades

**Passo 3:** Incluir um novo registro preenchendo os campos com os dados a seguir e salvar :

* Descrição : Sincronizar via Mensagem Única TOTVS
* Nome da Classe : RM.Mov.FormulaVisual.Activities.MovCargaInicialTotvsMessageActivity
* Nome do Assembly: RM.Mov.formulaVisual.Activities
* Ativo? : Selecionado

2. **Os cadastros devem ser sincronizados na ordem abaixo, pois são pré-requisitos uns dos outros.**

* Coligada e Filial
* Moedas
* Unidades de Medida
* Centros de Custo
* Condição de Pagamento
* Local de Estoque
* Cliente e Fornecedor
* Produto e Serviço
* Funcionário
* Patrimônio(Ativos)
* Projeto
* Obra, Etapa e tarefa

**Executar a Carga Inicial**

**Passo 1:** Acesse : Gestão / Fórmula Visual /Fórmula visual.

**Passo 2:** Acesse : Processos / Importar Fórmulas Visuais

**Passo3:** Clique em Adicionar Objetos

**Passo 4:** Selecione a Fórmula Visual de Sincronia dos cadastros e clique em abrir :

**Passo 5:** Para cada um dos Itens importados , selecionar a aba Parâmetros , preencher os campos e Executar:

* Categoria : 3 – Cadastros
* WorkFlow Pai : vazio
* Importar Gatilhos : Marcado

**Passo 6:** Clique em Fechar

**Passo 7:** Para visualizar a fórmula Visual clicar duas vezes sobre ela

**Passo 8:** Clicar sobre Salvar e Executar para sincronizar os registros.

Para mais detalhes sobre como importar as fórmulas visuais de Carga de Dados Inicial , acesse o boletim técnico.

---

**Recursos Adicionais**

Boletim Técnico TDN - [Criar Atividade  e Executar Fórmulas Visuais de  Carga Inicial de Dados](http://tdn.totvs.com/download/attachments/76251244/BT+-+Carga+INICIAL+NGI.pdf?version=1&modificationDate=1381327330449)
