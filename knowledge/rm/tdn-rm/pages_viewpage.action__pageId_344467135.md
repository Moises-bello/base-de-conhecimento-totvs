---
content_hash: 53dc2551bc54047bbce246c47adfe57717e74cec8ac995725e6255f7b949e88b
fetched_at: '2026-06-29T00:08:53.295724+00:00'
page_id: '344467135'
product: rm
source: tdn-rm
title: Quebra de Página x Ordenação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344467135
version: 1
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     O objetivo deste documento é apresentar  informações acerca da quebra de página x ordenação

# Informações:

O comportamento normal de uma ferramenta de relatórios é priorizar a quebra à ordenação. Vamos a um exemplo para melhor entendimento:

Temos um relatório que traz funcionários por seção. Aplicamos a ordenação pelo nome de cada funcionário. Sem a quebra o retorno seria:

Seção 0003 - Aline Almeida  
Seção 0002 - Carlos Machado  
Seção 0001 - Diego Souza   
Seção 0002 - Ester Silva  
Seção 0001 - Maria Pereira

Agora, vamos atrbuir a quebra pela seção, reparem que a quebra é prioridade em relação à ordenação, porém, dentro da quebra a ordenação permanece respeitada:

Seção 0001  
                  Diego Souza  
                  Maria Pereira  
Seção 0002  
                 Carlos Machado  
                  Ester Silva  
Seção 0003   
                 Aline Almeida

falsefalse

**Produto:** Framework

false

**Versão:** 12.1

false

**Processo:** Totvs Reports

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

**hilippe Fernandes Lima Gonçalves**
