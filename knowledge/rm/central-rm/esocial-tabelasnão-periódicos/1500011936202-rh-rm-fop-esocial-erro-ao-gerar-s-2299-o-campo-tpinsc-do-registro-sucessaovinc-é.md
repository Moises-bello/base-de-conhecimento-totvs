---
article_id: 1500011936202
category: eSocial - Tabelas/Não Periódicos
content_hash: c761440a9d802a901469b1662d0ad460fc37afae9ea1f83ef10f9d04b179975a
fetched_at: '2026-06-28T22:47:10.372685+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-2299: O campo ''tpInsc'' do registro
  ''sucessaoVinc'' é obrigatório e não está preenchido e O campo ''cnpjSucessora''
  do registro ''sucessaoVinc'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2025-08-19T19:08:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011936202-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2299-O-campo-tpInsc-do-registro-sucessaoVinc-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido-e-O-campo-cnpjSucessora-do-registro-sucessaoVinc-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19541476515351)**Tempo aproximado para leitura:**00:04:00 min**

**Ocorrência**Ao gerar o XML do evento S-2299 são retornados os erros: **O campo 'tpInsc' do registro 'sucessaoVinc' é obrigatório e não está preenchido** e **O campo 'cnpjSucessora' do registro 'sucessaoVinc' é obrigatório e não está preenchido**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14562743636375)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este problema acontece quando realizamos a transferência de um funcionário entre coligadas e o campo **CNPJ Empresa Sucessora** contido no cadastro de funcionários está em branco.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o cadastro do funcionário demitido em **Situação;**2. Preencha o campo **CNPJ Empresa Sucessora** com a devida informação e salve o cadastro;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17085662050327)

3. Gere novamente o XML do evento **S-2299**.  
  
**Saiba mais**  
Para mais informações acesse:  
- [Mapeamento evento S-2299;](http://tdn.totvs.com/display/LRM/Evento+S-2299)  
- [Rescisão: Transferência para outra base de dados;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017469652-RH-RM-FOP-Rescis%C3%A3o-Transfer%C3%AAncia-para-outra-base-de-dados)  
- [Transferência entre filiais ou coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020186252-RH-RM-FOP-Transfer%C3%AAncia-entre-filiais-ou-coligadas)
