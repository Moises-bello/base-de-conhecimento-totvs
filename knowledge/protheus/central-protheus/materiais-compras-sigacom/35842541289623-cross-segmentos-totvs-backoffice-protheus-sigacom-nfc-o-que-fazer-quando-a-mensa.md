---
article_id: 35842541289623
category: Materiais - Compras (SIGACOM)
content_hash: 869d3bfb1e1c405a9e10699cb59d15c72a460a0588f8718a3b0c43fdfea582c0
fetched_at: '2026-06-28T22:41:21.860384+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - O que fazer quando
  a mensagem "A proposta do fornecedor não foi localizada na base de dados" ocorrer?
type: support-article
updated_at: '2025-10-23T20:35:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35842541289623-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-O-que-fazer-quando-a-mensagem-A-proposta-do-fornecedor-n%C3%A3o-foi-localizada-na-base-de-dados-ocorrer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35842541274263) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Ao enviar o formulário da Cotação via Workflow para o fornecedor no Novo Fluxo de Compras, é gerada a mensagem "A proposta do fornecedor não foi localizada na base de dados". O que fazer para solucionar a mensagem de erro?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35842594042263)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310  
  
**Causa**

Esse erro é causado pela **presença de caracteres especiais**, como **&**, **ç**, **º**, **ª**, entre outros, nos campos de Razão Social ou Nome Fantasia do cadastro do fornecedor.

**Solução**  
Para solucionar esta ocorrência, **Acesse o cadastro do fornecedor** e verifique se há caracteres especiais na Razão Social ou Nome Fantasia. Se houver, **r****emova o caractere especial** identificado (por exemplo, o símbolo **&**), **s****alve as alterações** e **realize um novo teste** no processo de cotação. **Valide** se o problema foi solucionado.

Se, após o ajuste, o problema persistir, verifique o **modo de compartilhamento** das tabelas **SC1** **SC8** **DHU** **DHV** em seu ambiente.

**Atenção:** O modo de compartilhamento dessas tabelas deve ser **idêntico** para o correto funcionamento do processo. Para maiores informações consulte o Guia do NFC abaixo.

[Novo Fluxo de Compras: Guia de Referência - Gestão de Compras - P12](https://tdn.totvs.com.br/pages/viewpage.action?pageId=680260500)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35842541275799)

Conforme demonstra na documentação: [Cadastro de fornecedor - Retirada de caracteres especiais](https://tdn.totvs.com/display/public/PROT/DT+Cadastro+de+fornecedor+-+Retirada+de+caracteres+especiais), o time de produto realizou um tratamento para que caracteres especiais sejam removidos da rotina de cadastro de fornecedores. Portanto se trata de um novo comportamento do sistema. As rotinas do NFC não permitirão caracteres especiais.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[Cadastro de fornecedor - Retirada de caracteres especiais](https://tdn.totvs.com/display/public/PROT/DT+Cadastro+de+fornecedor+-+Retirada+de+caracteres+especiais)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
