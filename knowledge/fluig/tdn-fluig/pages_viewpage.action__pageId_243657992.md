---
content_hash: 60acff58861d029d038f151eafa5ff9e22f88d539095cb767b63c4cf0828a42a
fetched_at: '2026-06-28T21:35:23.084581+00:00'
page_id: '243657992'
product: fluig
source: tdn-fluig
title: BPM 054 - Como solucionar a lentidão em processos mobile?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243657992
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Nosso fluig interno apresenta muita lentidão ao realizar tarefas pelo Mobile, independente da conexão que esteja ou do aparelho. Existe alguma coisa a fazer para melhorar o desempenho ?

# Causa

Lentidão na movimentação de processo através do mobile normalmente envolve duas situações:

* A primeira seria a qualidade de conexão do dispositivo, se o mesmo está conectado em uma rede com *proxy* ou *firewall*, ou algo que possa causar essa lentidão.
* Já a segunda se refere ao desenvolvimento do formulário, onde o mesmo utiliza vários datasets.

# Solução

Caso o processo utilize vários datasets, avalie a documentação de  . Nesta documentação é explicado como implementar datasets sincronizados, que aumentam consideravelmente o desempenho do fluig.
