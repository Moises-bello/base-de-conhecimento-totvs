---
article_id: 360018061492
category: Materiais - Compras (SIGACOM)
content_hash: e7d3c77a202068a9731b1304d448a397f80cebb7492afee1ddd408a8f82199cf
fetched_at: '2026-06-28T22:41:16.103501+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como validar se a chave
  informada no campo Chave NFe ( F1_CHVNFE ) confere com a nota que está sendo digitada
  ?
type: support-article
updated_at: '2025-06-18T16:46:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018061492-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-validar-se-a-chave-informada-no-campo-Chave-NFe-F1-CHVNFE-confere-com-a-nota-que-est%C3%A1-sendo-digitada
---

**Dúvida**Como validar se a chave informada no campo Chave NFe ( F1\_CHVNFE ) confere com a nota que está sendo digitada ?  
  
**Ambiente**Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Solução**Para atender esta necessidade, realize os seguintes passos:  
  
1. Acesse o módulo configurador(SIGACFG);  
2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;  
3. Selecione a opção Parâmetros;  
4. Localize o parâmetro MV\_VCHVNFE e configure o mesmo como .T.

***Obs1:***

Para validar se a chave confere com a nota que esta sendo digitada a rotina utiliza a seguinte composição: CNPJ do fornecedor + Número da Nota + Série.

***Obs2:***

Para verificar se o **CNPJ do fornecedor** está informado na chave da nota, consulte o CNPJ pelo código vinculado à lupa na Rotina de Documento de Entrada (conforme indicado no print abaixo) ou acesse a Rotina de Cadastros de Fornecedores (MATA020), pesquisando pelo código do fornecedor + loja.

Para confirmar se o **Número e a Série da nota** estão informados na chave, consulte o número e a série no cabeçalho do Documento de Entrada (conforme indicado no print abaixo):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32900461524119)

Para verificar como é a estrutura da chave da Nota consulte o artigo:[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é a estrutura da Chave NFE para verificação do parâmetro MV\_VCHVNFE ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011727892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-a-estrutura-da-Chave-NFE-para-verifica%C3%A7%C3%A3o-do-par%C3%A2metro-MV-VCHVNFE)

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é a estrutura da Chave NFE para verificação do parâmetro MV\_VCHVNFE ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011727892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-a-estrutura-da-Chave-NFE-para-verifica%C3%A7%C3%A3o-do-par%C3%A2metro-MV-VCHVNFE)

[Como é formada a Chave de Acesso de uma NF-e, NFC-e, de um CT-e ou MDF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018340871)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
