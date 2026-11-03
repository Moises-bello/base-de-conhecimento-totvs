---
content_hash: e2ea521f147c18bd101afb810dbdc9b23d19fcc4496fb0110d904f5cdd7a46f4
fetched_at: '2026-06-28T21:35:25.282922+00:00'
page_id: '275151216'
product: fluig
source: tdn-fluig
title: BPM 093 - É possível ajustar o fuso horário do servidor para que não gere erro
  ao gravar  os horários de início e conclusão das solicitações?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=275151216
version: 3
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig  
**Versão**: 1.6.0

# Ocorrência

Identificamos que o fuso-horário configurado no servidor de aplicação do Fluig não era o horário de Brasilia e, desta forma, as atividades executadas no BPM estavam sendo gravadas com horários de início e conclusão incorretos.

# Causa

Já alteramos a configuração do servidor e o problema foi solucionado para os processos executados após a mudança, porem gostaríamos de saber se existe alguma forma de atualizar a base histórica que ficou gravada com os horários incorretos.

# Solução

O fluig não possui um recurso para atualização dos dados históricos, e não recomendamos alterações diretamente na base de dados, visto o grande impacto que tais alterações podem causa na plataforma como um todo.
