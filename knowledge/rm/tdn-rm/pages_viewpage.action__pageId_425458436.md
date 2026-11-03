---
content_hash: eb973880d163c528302bbe5bf2b9da5935da139979dccb557506a32b534efbb2
fetched_at: '2026-06-29T00:09:30.348915+00:00'
page_id: '425458436'
product: rm
source: tdn-rm
title: Arquivos Anexos ao Atendimento (Parâmetros)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458436
version: 22
---

Em um atendimento, que representa um chamado de problema, dúvida, solicitação e etc, algumas informações expostas de maneira apenas texto podem ser de difícil entendimento, e pensando nisto o sistema disponibiliza a possibilidade de se anexar arquivos ao atendimento (semelhante a arquivos anexos a um e-mail). Tais arquivos podem ser gráficos, imagens, planilhas ou qualquer item que julgado como necessário para auxiliar um entendimento e/ou solução rápida de tais solicitações.

## Armazenamento dos Arquivos anexos

A partir da versão 12.1.2410, o TOTVS Aprovações e Atendimento oferece mais flexibilidade no armazenamento de arquivos anexos. É possível manter a configuração atual, armazenando os arquivos diretamente na base de dados, ou optar pelo Repositório de Arquivos (FileRepo) para os novos arquivos.

**Observação:** Para que o Repositório de Arquivos (FileRepo) esteja disponível para armazenamento dos anexos, é necessário realizar previamente a configuração desse Repositório. Para saber mais sobre o Repositório de Arquivos (FileRepo) e como configurá-lo, [clique aqui](https://tdn.totvs.com.br/pages/releaseview.action?pageId=787855155)

Ao optar pelo Repositório de Arquivos (FileRepo), será necessário configurar o conector padrão, que indicará o local onde os arquivos serão armazenados.

O armazenamento dos arquivos anexados aos atendimentos será definida pela configuração do parâmetro selecionado.

É possível escolher entre:

* **Base de Dados:** Os arquivos são armazenados diretamente no banco de dados.
* **Repositório de Arquivos (FileRepo):** Os arquivos são armazenados no Google drive.

## Arquivos anexados na Base

Se optar por armazenar os anexos na base de dados, é possível realizar o controle de tamanho dos arquivos a serem anexados ao atendimento. Tal controle é realizado através da limitação de tamanho e de como o tamanho limite é calculado. As informações para efetuar tais verificações são feitas com base no conjunto de parâmetros a seguir:

* **Tamanho máximo por atendimento em MB**

Tamanho máximo que a soma do tamanho dos arquivos anexos ao atendimento podem ter (valor default 10 MB) .

* **Tamanho máximo por atendente em MB**

Tamanho máximo que a soma de arquivos que um atendente pode anexar a um determinado atendimento (valor default 2 MB).

* **Tipo de validação do tamanho dos arquivos anexos**

* Limitar arquivos por atendimento;
* Limitar arquivos por atendente;
* Limitar arquivos por atendimento e atendente.

**Observação:** Esses parâmetros ficam habilitados apenas se o usuário optar por utilizar arquivos anexos na base, ou seja, eles desabilitam caso o cliente altere para File Repo.
