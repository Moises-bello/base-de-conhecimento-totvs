---
article_id: 360033260494
category: MDFe - Manifesto de Carga
content_hash: 890684e720a44997d02701eb2c09d554f315755d04e3d9e634a15d9cb6320da3
fetched_at: '2026-06-28T22:40:08.093680+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos  - Rejeição 612
  - Código de Município diverge da UF de descarregamento do MDF-e'
type: support-article
updated_at: '2021-10-21T14:44:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033260494--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-612-C%C3%B3digo-de-Munic%C3%ADpio-diverge-da-UF-de-descarregamento-do-MDF-e
---

**Dúvida**Rejeição 612 - Código de Município diverge da UF de descarregamento do MDF-e  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

"Minha UF de carregamento é MG e UF de descarregamento RJ mas eu tenho notas fiscais que serão entregues em cidades de MG e o sistema não permite que eu escolha cidade de MG quando o descarregamento é RJ, como proceder?"

No sistema devemos informar a UFIni - Sigla da UF de Carregamento e UFFim - Sigla da UF de Descarregamento.  
  
Da mesma forma também temos o grupo <infMunDescarga> onde devemos informar o código e o nome dos municípios de descarregamento, esses municípios tem que pertencer a UFFim.

Se informar um município de descarregamento que não pertence a UF de descarregamento ocorre a rejeição 612: Código de Município diverge da UF de descarregamento do MDF-e  
  
Note que a rejeição diz: **Código de Município diverge da UF de descarregamento do MDF-e**

Ou seja, os dois primeiros dígitos do código informado em cMunDescarga que se refere a UF não condiz com a sigla informada em UFFim.  
  
Exemplo:  
Em UFFim você informa RJ, isso significa que a carga vai ser descarregada no estado Rio de Janeiro, mas informa como cidade de descarregamento: Belo Horizonte que fica no estado de Minas Gerais.

Se o caminhão vai fazer entrega em cidades de MG e de RJ, devemos emitir 2 MDF-e.  
  
No primeiro relacionando somente a carga que vai ser descarregada em MG e o segundo relacionando somente a carga que vai ser descarregada em RJ.  
  
Conforme legislação AJUSTE SINIEF 21, DE 10 DE DEZEMBRO DE 2010  
  
§ 2º Deverão ser emitidos tantos MDF-e distintos quantas forem as unidades federadas de descarregamento, agregando, por MDF-e, os documentos referentes às cargas a serem descarregadas em cada uma delas.
