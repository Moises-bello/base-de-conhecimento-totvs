---
content_hash: a3b3372b9c69ffea0316a68b12e8e553f1bc938c699bae1d21a7b33f0221ef38
fetched_at: '2026-06-29T00:10:02.515128+00:00'
page_id: '452718937'
product: rm
source: tdn-rm
title: Tipos de Agentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Agentes
version: 5
---

**Tipos de Agentes**

O cadastro de Tipo de Agentes tem como objetivo, definir os tipos dos agentes que causam exposição dos colaboradores a riscos ambientais.  
  
Ao marcar a flag **'Desconsiderar para eSocial**' , o risco associado a este tipo de agente não será levado no evento S-2240 - Condições Ambientais do Trabalho - Fatores de Risco, ao ter um mapeamento de risco criado em Reconhecimento/Avaliação de Risco.

Exemplo:  Para o tipo de agente AG1 – Ruído marquei a flag ‘Desconsiderar para eSocial’ , e para o tipo de agente AG7 – Frio a flag está desmarcada. Foram criadas avaliações para riscos 00001 – Ruído e 00010 – Frio, e ao gerar o XML do evento S-2240, somente o tipo de agente do risco  00010 – Frio, foi exibido.

**Atenção**

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | pasta Acesso a Menus.
