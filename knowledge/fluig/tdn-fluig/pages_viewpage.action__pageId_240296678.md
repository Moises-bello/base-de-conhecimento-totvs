---
content_hash: 2550ea30b1f41d1321ddf78ada05fce1723e942f0508c2c3a08564e6cdba7337
fetched_at: '2026-06-28T21:35:22.794626+00:00'
page_id: '240296678'
product: fluig
source: tdn-fluig
title: BPM 043 - Como converter solicitações no fluig?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240296678
version: 16
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** todas

# Descrição

A finalidade da conversão de processos é converter processo com versões mais antigas para versões mais novas. Isso é feito mapeando as atividades do processo mais antigo para atividades da versão mais recente. Assim, o processo antigo passa a contar com as configurações e atividades da versão mais nova com uma simples conversão.

Observação 1

Caso a solicitação esteja em uma atividade que permite retorno, ela não poderá retornar à atividade anterior após o processo de conversão da solicitação. Isso ocorre porque a conversão representa uma nova movimentação para o processo e portanto perderá a capacidade de retornar a atividade anterior, que pertence à versão antiga.

Observação 2

Caso a atividade com a versão antiga esteja com consenso configurado, só será permitido converter para uma nova versão, quando possuir atividades destino que também estejam com consenso configurado.

# Procedimentos

help1Passo 1  

* Selecionar a funcionalidade **Converter Solicitações** no menu **Processos**.

2Passo 2  

* Selecione o processo e a versão que receberá a conversão, em seguida, clique em **Avançar**.

  false

  Só é possível converter versões que possuem solicitações abertas, como pode ser visto na coluna **Solicitações Abertas** na imagem abaixo.

3Passo 3  

* Selecione a **Versão Destino** para qual as solicitações de versão antiga serão convertidas, feito isso, será listado as atividades que poderão ser selecionadas como destino, faça o mapeamento e clique em **Avançar**.

  false

  O mapeamento é feito para relacionar as atividades que são iguais ou semelhantes entre as duas versões do processo.

4Passo 4  

* Neste momento, as solicitações abertas que podem ser convertidas serão listadas para a seleção, em seguida, clique em **Avançar**.

5Passo 5  

* A página seguinte servirá para confirmar o mapeamento feito e as solicitações selecionadas que serão convertidas. Os dados estando corretos, clique em **Converter**.

6Passo 6  

* As solicitações serão convertidas, trazendo em tela o log do processo de conversão.

  false

  O log exibirá:

  **INFO**: Informações com dados da solicitação.

  **WARN**: Mensagens de atenção que devem ser observados pelo usuário. Não impedem a conversão.

  **ERROR**: Retornará ao usuário, a mensagem do porque a solicitação não ter sido convertida.

# Observações

Consulte a documentação sobre [Conversão de Solicitações](http://tdn.totvs.com/pages/viewpage.action?pageId=233763179) no Help Online fluig.
