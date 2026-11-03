---
content_hash: d2492b9d1bb8d2e0acb09ed86f5d6d8a9abfed4ab2eef82845886cd2843b136e
fetched_at: '2026-06-29T00:10:07.953829+00:00'
page_id: '452719482'
product: rm
source: tdn-rm
title: Fontes Geradoras
type: documentation
url: https://tdn.totvs.com/display/LRM/Fontes+Geradoras
version: 2
---

**Fontes Geradoras**

---

Este cadastro tem como objetivo definir as possíveis fontes geradoras associadas aos riscos ambientais ou o agente diretamente relacionado a CAT ou relacionados a situações específicas.

O Código e-Social terá uma relação de códigos para seleção e o mesmo será informado no cadastro de Ocorrências do Acidente de Trabalho para o arquivo XML a ser gerado para o e-Social no módulo Folha de Pagamento.

O tipo da fonte geradora, se 'Agente Causador Acidente Trabalho', 'Situação Geradora Acidente Trabalho' ou 'Agente Causador Doença Profissional' será utilizado para separar onde será listado o item no cadastro de Ocorrências do Acidente de Trabalho.  
   
**Exemplo:**  
Fonte Geradora – 200012200 – marcado como *Tipo de*Agente 'Situação Geradora Acidente Trabalho'.  
Fonte Geradora – 302010300 – marcado como *Tipo de*Agente 'Agente Causador Acidente Trabalho'.  
Fonte Geradora – 200004600X – marcado como *Tipo de*Agente 'Agente Causador Doença Profissional'.  
   
Em *CAT | Ocorrências Acidente Trabalho*:

No campo *Código da situação geradora* será listado apenas o código 200012200.

No campo *Cód. Agente(s) Causador(es)* será listado os códigos 302010300 e 200004600X.

O parâmetro *Ativo* será possível controlar quais as Situações Geradoras ou Agentes Causadores serão listados no cadastro de Ocorrências do Acidente de Trabalho.

Os registros de '*Situação Geradora Acidente Trabalho*' ficam na tabela VFONTEGERADORA  
(Registros respeitando a tabela 16, leiaute v2.2 do e-Social)  
   
Os registros de '*Agente Causador Acidente Trabalho'* ficam na tabela VAGENTECAUSADOR  
(Registros respeitando a tabela 14, leiaute v2.2 do e-Social)  
   
Os registros de '*Situação Geradora Doença Profissional*' ficam na tabela VFONTEGERDOENCA  
(Registros respeitando a tabela 15, leiaute v2.2 do e-Social)  
   
**Observação**

Deverá ser definido o status da fonte geradora conforme o módulo no qual a fonte geradora será utilizada. O registro em questão poderá ser associado ao cadastro de Riscos ou ao cadastro de uma CAT.

**Atenção**

Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão em Cadastros | Segurança | Perfis | pasta Acesso a Menus.
