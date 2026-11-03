---
content_hash: e5f22892e6a4c6d96d3be053deb0e8cd4e14999f1aabe7bf7de7d447767be00d
fetched_at: '2026-06-29T00:08:14.220377+00:00'
page_id: '244443288'
product: rm
source: tdn-rm
title: RPT00015.1.1 - Adicionando uma Imagem (Passo a Passo)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244443288
version: 21
---

# Índice:

---

.\*ndice:

# Introdução:

---

       Com o advento da migração do **TOTVS Reports** da **versão 11.8x** para as versões **superiores a versão 12.1.4**, muitas alterações foram feitas principalmente **na geração sobre demanda dos dados** vinculados a cada componente presente no relatório.

Em relatórios da versão **11.8x**, por exemplo, **a geração sobre demanda dos dados** era realizada no momento da impressão de cada componente, ao contrário dos das versões mais atuais **(12.1.5 ou superiores)**, onde a geração dos dados é feita através de apenas uma consulta SQL **(Fase de Preparação)**, que é gerada a partir das tabelas e consultas SQL vinculadas ao relatório.

# Adicionando uma Imagem

---

   Utilizaremos o exemplo abaixo para explanarmos o assunto **"Adicionando uma Imagem".**

**Imagem 1 -** Relatório exemplo.

# Propriedades Importantes de um Componente Imagem

---

Ao adicionar uma imagem em um relatório, devemos nos atentar para algumas propriedades:

**Ligação de Dados**: Define a ligação de dados **(campos de uma Tabela ou Consulta SQL)** para cada uma das opções de preenchimento dos dados da imagem.

**Caminho:**Ao se definir a ligação de dados para uma das opções disponíveis de preenchimento dos dados da imagem, essa propriedade conterá o caminho da ligação escolhida. Caso a propriedade Ligação de Dados não esteja preenchida ela também permite que seja escolhido um caminho de relacionamento de dados.

**Caminho da Imagem:** Permite escolher o caminho local da imagem.

**Imagem:**Mostra o nome da imagem escolhida através da propriedade **Caminho da Imagem**. Caso a Propriedade **Caminho da Imagem** não seja preenchida, ela permite que se escolha uma imagem através dela própria.

**Tabela:**Ao se definir a ligação de dados para uma das opções disponíveis de preenchimento dos dados da imagem, essa propriedade conterá a tabela ou consulta SQL da ligação escolhida

**Propriedades que Definem a Apresentação de uma Imagem:**

falseILigação de dados

Através da Propriedade **(Ligação de Dados)** o usuário poderá escolher uma imagem proveniente de um campo de uma **Tabela** ou de um campo de uma **Consulta SQL**.

O usuário poderá escolher entre três formas de se ligar os dados ao componente Imagem:

**Caminho da Imagem:** **Parâmetros**, campo de **Tabela** ou **Consulta SQL** que contenha um **caminho físico na máquina**. Permite também escolher um arquivo de imagem diretamente na máquina.

**Imagem:** **Parâmetros**, campo de **Tabela** ou **Consulta SQL** que contenha uma**Imagem (em bytes)**. Caso o arquivo seja escolhido diretamente na máquina essa propriedade será preenchida automaticamente com a imagem escolhida.

**URL de Navegação:** **Parâmetros**, campo de **Tabela** ou**Consulta SQL**.

Caminho da imagem

Através da propriedade **Caminho da Imagem**o usuário poderá escolher uma imagem proveniente de um caminho local na máquina.

Caminho

Através dessa propriedade um relacionamento de dados entre a tabela master do detalhe e a tabela do campo a ser vinculado a imagem é estabelecido fazendo com que a imagem seja devidamente apresentada.

# **Cuidados ao Preencher as Propriedades de um Componente Imagem:**

falseI1º Cuidado

Ao se preencher a Propriedade **(Ligação de Dados)**deve se atentar a:

**Imagem 4 -** Vinculo errôneo da Propriedade **Caminho da Imagem**.

* **Não se deve vincular** uma imagem**(campos do Tipo BLOB, IMAGE, e outros)** proveniente de uma **Tabela** ou **Consulta SQL** nas Propriedades **Caminho da Imagem** e **URL de Navegação,**pois, a exceção abaixo será apresentada:
2º cuidado

No momento da geração existe a possibilidade de desmarcar a opção de **Parar a Execução do Relatório em Caso de Erros,**nesse caso a imagem não será gerada, porém as demais informações do relatório serão apresentados corretamente.

**Imagem 5 -** Exceção levantada devido a **vinculação errônea** das propriedades **Caminho da Imagem** ou **URL de Navegação**.

3º cuidado

Ao vincular uma Imagem **(campos do Tipo BLOB, IMAGE, e outros),** proveniente de uma **Tabela** ou **Consulta SQL,** à propriedade **Imagem**, o relatório será gerado com as imagens devidamente preenchidas.

Relatório com Imagem

**Imagem 8 -** Relatório gerado com a imagem.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Adicionando uma Imagem

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
