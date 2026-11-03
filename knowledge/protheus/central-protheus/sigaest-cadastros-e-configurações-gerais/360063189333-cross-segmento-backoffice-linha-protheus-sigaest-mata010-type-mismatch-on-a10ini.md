---
article_id: 360063189333
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 2208c84ea793cde70e76e69a0192286f16f588ea496e1be713f664a44911ed68
fetched_at: '2026-06-28T22:39:08.299408+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 -  type mismatch
  on A10INITCOD(MATA010.PRX)
type: support-article
updated_at: '2025-03-12T12:22:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063189333-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-type-mismatch-on-A10INITCOD-MATA010-PRX
---

**Dúvida**Ao incluir um novo produto na rotina MATA010 - Cadastro de Produtos é gerado o error.log: "*THREAD ERROR - type mismatch on + on A10INITCOD(MATA010.PRX)*". O que fazer para resolver este problema?

**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17

**Solução**Este erro normalmente é causado por validação de usuário. Normalmente ocorre no campo B1\_COD. Veja um exemplo abaixo de uma validação de usuário em campos:

*X3\_CAMPO(C) :B1\_COD*  
*Field 16: X3\_RELACAO(C) :EXECBLOCK("FTESTFNP",.F.,.F.)*    
  
![image.png](https://atendimento.totvs.com/attachments/token/4rJenBdhFXfIvxrXDRU3EPJGD/?name=image.png)

Avalie no log se o erro é apontado em alguma validação de usuário como o exemplo acima. Então basta acessar via Configurador a tabela e o campo correspondente para remoção.

**Observação**: É recomendável validar a existência de validações nas abas "Opções" -> Inic. Padrão ou na aba "Validações". Havendo, remova a validação, salve para conseguir incluir um produto normalmente.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
