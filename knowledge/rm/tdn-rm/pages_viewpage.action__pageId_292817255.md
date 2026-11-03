---
content_hash: fa6cf39a31c5d25e3167f56323389ac549c4cf2657b5512e7ccf225d594490ef
fetched_at: '2026-06-29T00:08:42.840007+00:00'
page_id: '292817255'
product: rm
source: tdn-rm
title: Utilizando a atividade "Preparar Execução do Processo"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=292817255
version: 16
---

# Preparar Execução do Processo:

---

A atividade de **"Preparar Execução do Processo"** serve para antecipar a preparação da classe de Parâmetros relativa à action de Processos que será executada através da atividade de **"Executar Processo",** fazendo com que a execução do processo seja mais performática. Em adição à maior performance, existe também a possibilidade de enviar um XML com os parâmetros já preenchidos, podendo fixar os valores à serem submetidos à execução do processo.

Utilização em Conjunto

A Atividade **"Preparar Execução do Processo"**:

* Não deve ser utilizada isoladamente, ela deve ser utilizada em Conjunto com a atividade de:

* Pode ser utilizada em Conjunto com a atividade de:

A atividade de **"Preparar Execução do Processo"**possui duas propriedades específicas:

| Nº | Nome | Descrição | Obrigatoriedade |
| --- | --- | --- | --- |
| 1 | Nome do Processo | Deve-se escolher qual Action será utilizada na preparação da Execução do Processo. | GreenObrigatório |
| 2 | XML dos Parâmetros | Ao se preencher essa propriedade, é criado uma instância da classe de parâmetros do Processo com os valores passados através do XML. | YellowOPCIONAL |

Vamos configurar a atividade **"Preparar Execução do Processo"**.

**1)** Escolha uma **Action de Processo** através da propriedade **Nome do Processo**

**2) (Opcional)** Preencha o campo **XML dos Parâmetros** com um XML especifico contendo os parâmetros do Processo. (Pode-se utilizar a atividade de  juntamente com  para poder preencher a propriedade **XML dos Parâmetros**)

**3)** Vincular a atividade **"Preparar Execução do Processo"** à atividade  através da propriedade **"Atividade de Preparar Parâmetros"**

**4)** Preencher a Propriedade **Nome do Processo** da atividade

**Os próximos passos e exemplos estão no documento**

falsefalse

**Produto:** Framework

false

**Versão:** 12.1 e Superiores

false

**Processo:** Fórmula Visual - Utilizando a atividade "Preparar Execução do Processo"

falsefalse

**Status:** Finalizado

false

**Data:** 10/05/2016

false

**Autores:**
