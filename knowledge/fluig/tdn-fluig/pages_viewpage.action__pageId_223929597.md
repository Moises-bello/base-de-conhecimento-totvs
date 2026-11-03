---
content_hash: 6caa668fa5d5eca04171548ef72e5cd77c5271b71cbd1211fe3adea45ea58fff
fetched_at: '2026-06-28T21:35:19.842181+00:00'
page_id: '223929597'
product: fluig
source: tdn-fluig
title: BPM 019 - É possível que um processo criado via TDS seja exibido pelo código
  e não pela descrição?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223929597
version: 12
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Tenho um processo criado pelo TDS ou Eclipse. Contudo ao efetuar a exportação para o servidor fluig, o processo é exibido pelo seu código e não pela sua descrição.

# Causa

Este comportamento ocorre devido ao uso de literais pelo processo desenvolvido no TDS.

Quando a Descrição, Categoria e Instruções do processo são alterados no fluig pela web, a alteração não é realizada de forma automática nos arquivos literais. Por isso as alterações não são aplicadas.

# Solução

A modificação da descrição, categoria e instruções de um processo que contém literais deverá ser realizada de forma manual, através dos arquivos de literais armazenados na pasta "*literals*" do projeto no TDS.

Para realizar este procedimento, faça conforme descrito abaixo:

0.5falsesamplesfadetrue1Passo 1

* Importar o processo do servidor do fluig para o TDS.

**Figura 1 - Iniciar 'Importar Processo' do fluig**

**Figura 2 - Escolher servidor**

**Figura 3 - Selecionar o processo**

2Passo 2

* Alterar o código do arquivo pt\_BR (caso utilizar nas três línguas, alterar nos três arquivos) e Salvar. Poderão ser alteradas as três informações dependendo da necessidade. Lembrando que após a criação das literais, a edição destes três campos deverão ser alterados diretamente nos arquivos de literias conforme descrito na documentação [Tradução de Processos](http://tdn.totvs.com/x/iQOLCQ).

**Figura 4 - Abrir e alterar as informações do arquivo na língua pt\_BR**

3Passo 3

* Exportar o processo e os arquivos literais novamente para o fluig

**Figura 5 - Selecionar e exportar para o fluig**

**Figura 6 - Selecionar o servidor e Liberar Versão**
