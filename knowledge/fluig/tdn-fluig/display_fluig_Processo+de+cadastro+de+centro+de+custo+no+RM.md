---
content_hash: 3edc5b4dfcc3b473b073cc811d507f2e5df41d5ab7f94c8711e5462bab3cfc6c
fetched_at: '2026-06-28T21:35:28.243751+00:00'
page_id: '624110229'
product: fluig
source: tdn-fluig
title: Processo de cadastro de centro de custo no RM
type: documentation
url: https://tdn.totvs.com/display/fluig/Processo+de+cadastro+de+centro+de+custo+no+RM
version: 10
---

# Índice

true.\*ndicenone

# Processo de cadastro de centro de custo no RM

---

Nesse exemplo, vamos utilizar um processo de cadastro de centro de custo no RM que possui um formulário e é composto pelas seguintes atividades: Início → Cadastrar Centro de Custo → Fim ou Cancelar.

Esse processo é iniciado para incluir um centro de custo na base de dados do RM. O formulário do processo tem 3 campos de texto: CODCOLIGADA, CODCCUSTO e NOME.

Para o processo foi criado um *script* de evento *Workflow* do tipo *beforeTaskSave* onde está a codificação para salvar o centro de custo.

## Componentes utilizados

---

Vamos exemplificar o uso dos seguintes componentes que são utilizados nesse processo:

* formulário que permite a inclusão de um centro de custo no RM.

## Diagrama

---

Esse é o diagrama do processo que estamos utilizando como exemplo:

## Desenvolvimento

---

Os desenvolvimentos que foram necessários para criar esse processo estão disponíveis para visualização e *download*. Desta forma, você pode baixá-los, ajustar ao seu negócio ou as suas necessidades e utilizá-los nos processos do seu dia a dia!

#f2f2f2#f2f2f2

**[Clique aqui](https://git.fluig.com/projects/SAMPLES/repos/exemplos-avancados-de-processos/browse/cadastro-centro-custos-rm)** para ver e baixar o código fonte dos desenvolvimentos desse processo.

Dica!

O arquivo **README.md** – existente no repositório – contém informações técnicas mais detalhadas. Ao longo dos próprios códigos fonte também existem várias explicações para auxiliar no entendimento e na utilização desse exemplo.
