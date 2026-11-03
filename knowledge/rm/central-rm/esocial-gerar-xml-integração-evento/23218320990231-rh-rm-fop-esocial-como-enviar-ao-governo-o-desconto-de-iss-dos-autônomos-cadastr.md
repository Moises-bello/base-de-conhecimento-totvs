---
article_id: 23218320990231
category: eSocial - Gerar XML/ Integração Evento
content_hash: 7732cb182430e60434a3aa3a6ec88c2ad8eb6a78f95b93e362b02d6cfdef399c
fetched_at: '2026-06-28T22:47:12.024142+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como enviar ao governo o desconto de ISS dos autônomos
  cadastrados no módulo Gestão Financeira
type: support-article
updated_at: '2024-05-02T20:20:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23218320990231-RH-RM-FOP-eSocial-Como-enviar-ao-governo-o-desconto-de-ISS-dos-aut%C3%B4nomos-cadastrados-no-m%C3%B3dulo-Gest%C3%A3o-Financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23218320922647) Tempo aproximado para leitura: **00:02:40 min****Dúvida**Como enviar ao governo o desconto de ISS dos autônomos cadastrados no módulo de Gestão Financeira?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Para realizar a geração dos eventos S-1200 e S-1210 para autônomos do Gestão Financeira discriminando o valor de ISS, o usuário deve realizar as seguintes parametrizações:   
1.Acesse **RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Autônomos e Externos 1/2** e informe o evento previamente cadastrado com **Código de Cálculo [389 - ISS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718701)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218335238423)

2. Acesse o cadastro de **Cliente/Fornecedor** **em Tributos e em Anexos - eSocial** e informe os dados obrigatórios do autônomo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218335246231)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218320941335)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218320943255)

3. No módulo **Backoffice | Gestão Financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira | 02.01.01 - Manutenção de Lançamentos | Integração Labore** informe qual valor opcional representa o desconto de ISS;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218335258647)

4. Antes de realizar a geração dos eventos S-1200 e S-1210, verifique se os lançamentos estão baixados com os valores que serão informados nos respectivos eventos;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218320948503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218320954391)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218320956695)

XML S-1200 será gerado com a informação do ISS.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23218320961687)

**Saiba mais**Para mais informações acesse:  
- [Evento S-1200 para autônomos cuja categoria não demandam o envio do evento S-2300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015427792-RH-RM-FOP-eSocial-Evento-S-1200-para-aut%C3%B4nomos-cuja-categoria-n%C3%A3o-demandam-o-envio-do-evento-S-2300);  
- [Geração do S-1200 e S-1210 para autônomos do Gestão Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015349532-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-S-1200-e-S-1210-para-aut%C3%B4nomos-do-Gest%C3%A3o-Financeira);  
- [Como gerar os eventos S-1200 e S-1210 para autônomos cadastrado no módulo de Gestão Financeira que tem desconto ISS?](https://tdn.totvs.com/pages/releaseview.action?pageId=442045440)
