---
article_id: 360015349532
category: esocial - Periódicos
content_hash: 43bcadf4a14bf7e00d4b2c2f1fb809b75ddd0843a585788cf138941ffdf6abee
fetched_at: '2026-06-28T22:47:09.400038+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Geração do S-1200 e S-1210 para autônomos do Gestão
  Financeira
type: support-article
updated_at: '2024-12-26T15:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015349532-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-S-1200-e-S-1210-para-aut%C3%B4nomos-do-Gest%C3%A3o-Financeira
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20940660687127)** Tempo aproximado para leitura: **00:03:15 min****Dúvida**Como gerar os eventos S-1200 e S-1210 para autônomos do TOTVS Gestão Financeira?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Quando o autônomo está cadastrado no TOTVS Gestão Financeira, deve-se primeiramente observar os seguintes pontos para a correta geração dos eventos **S-1200** e **S-1210**:

• Acesse **Configurações | Parametrizador | Integrações | Gestão Financeira** e verifique se o parâmetro **Considerar data de emissão em vez de data de vencimento** está marcado ou desmarcado. Ele influencia diretamente na geração do S-1200;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043253793)

• Em **Administração de Pessoal | Cliente e Fornecedor | Anexos | Lançamento**, no caso do S-1200 a **Data de Vencimento** ou **Data de Emissão** (de acordo com o parâmetro supracitado) deve estar compreendida no período de apuração a ser gerado. Já para a geração do S-1210, o sistema irá considerar se o lançamento foi baixado e se possui o cadastro **Anexos | Baixas do Lançamento** Preenchido;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20940749084055)

Tendo em vista os itens acima, para a geração dos eventos no RM siga os seguinte passos:

1. No TOTVS Folha de Pagamento, acesse **eSocial  | Gerar XML** (Eventos Periódicos);  
2. Selecione os eventos **S-1200** e **S-1210,**informe o período de apuração desejado e execute o processo marcando também o parâmetro **Gerar Autônomos Gestão Financeira/Externos**;

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20940644156183)

3. Quando o **Middleware** está ativado na coligada, o parâmetro acima não será exibido. O sistema irá gerar os autônomos do Gestão Financeira e autônomos externos automaticamente quando selecionado os eventos S-1200 e S-1210;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406595723031)

4. Após execução, acesse **eSocial | Eventos Periódicos** e, selecionando o período de apuração em questão, os eventos **S-1200** e **S-1210** estarão apresentados com a coluna **Cliente/Fornecedor** preenchida.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043254633)

**Importante**  
Para o correto lançamento das verbas no XML, os campos presentes em **Configurações | Parametrizador | eSocial | Autônomos e Externos 1/2** e **Autônomos e Externos 2/2** devem estar preenchidos.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20940660715927)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20940644181143)

Caso o usuário não utilize a integração com o TOTVS Gestão Financeira, é possível utilizar a integração com sistemas de terceiros alimentando as informações referentes as retenções dos autônomos no cadastro de **Autônomos Externos**.  
  
**Saiba mais**  
Para verificar mais informações sobre geração de eventos para autônomos, acesse:  
[- RM - eSocial - Geração de S-1200 e S-1210 para pagamento parcelado de autônomo do Fluxus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029350553)  
[- RM - eSocial - Geração do S-1200 para autônomos cuja categoria não demandam o envio do evento S-2300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015427792)  
- [Quais autônomos do TOTVS Gestão Financeira são considerados na geração do S-1200 e S-1210?](https://tdn.totvs.com/pages/releaseview.action?pageId=782315485)   
- [Como gerar S-1200 para Autônomos do Fluxus todas as categorias?](https://tdn.totvs.com/pages/releaseview.action?pageId=440855187)   
- [Autônomos e Externos 1/2](https://tdn.totvs.com/pages/releaseview.action?pageId=452719944)   
- [Autônomos e Externos 2/2](https://tdn.totvs.com/pages/releaseview.action?pageId=463823367)
