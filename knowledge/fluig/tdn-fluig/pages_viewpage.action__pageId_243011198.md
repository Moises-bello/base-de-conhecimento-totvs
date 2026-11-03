---
content_hash: 8c873a3f468a28ad211b7f2dc89e9dfcef76e04341bc828a2b7e074ed11ee5b9
fetched_at: '2026-06-28T21:35:22.966655+00:00'
page_id: '243011198'
product: fluig
source: tdn-fluig
title: BPM 047 - Como o evento validateForm o evento displayFields se comportam em
  movimentação em bloco?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243011198
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** Todas as versões

# Ocorrência

Ao realizar uma movimentação em bloco o evento validateForm é executado, porém o evento displayFields não. Esse é o comportamento padrão do produto?

# Solução

O **validateForm** é executado durante a movimentação em bloco para salvar ou gerar uma nova versão do formulário, já que é possível que outro evento seja executado antes da movimentação alterando o valor de um campo.   
  
O **displayFields** não é executado na movimentação em bloco porque ele só é executado quando o formulário é visualizado.

# Observações

Para saber mais acesse a documentação sobre [Desenvolvimento sobre a plataforma](http://tdn.totvs.com/display/fluig/Desenvolvimento+sobre+a+plataforma) e [Desenvolvimento de Formulários](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483).
