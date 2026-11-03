---
article_id: 6811943186583
category: eSocial - Tabelas/Não Periódicos
content_hash: ffd656018d02156b9f6bf2c141768d971e67f5a92696d060d25f27c1c3fe4e2f
fetched_at: '2026-06-28T22:47:10.368242+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar S-2200: O campo ''paisNascto'' do
  registro ''nascimento'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2026-04-17T19:33:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6811943186583-RH-RM-FOP-eSocial-Erro-ao-gerar-S-2200-O-campo-paisNascto-do-registro-nascimento-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22719328718231)** Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao gerar o XML do evento S-2200 é apresentado o erro **O campo 'paisNascto' do registro 'nascimento' é obrigatório e não está preenchido**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH -  (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
O erro é apresentado quando o sistema não está com as informações de Países configurados.  
  
**Solução**  
Para realizar a configuração de países, siga os passos abaixo:

1. Acesse **eSocial | Endereços | Classificação de Países**  inclua um novo registro que será identificada para o eSocial;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788320121111)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788320123671)

2. Acesse **Configurações | Parametrizador | eSocial | De/Para de Endereço** e informe o item criado no passo 1 no campo **Conceito de Classificação para Códigos de Países;**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788296406551)**

3. Após, em **eSocial | Endereços | Países.** Edite o país desejado e em **Anexos | Codificação de País** associe a **Classificação criada no passo 1** e, no campo **Código País** informe o código presente na coluna [**Código do País** da **Tabela 06 - Países**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/tabelas.html#06) do leiaute do eSocial;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788420104471)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788296410007)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788296412311)

4. Identifique no **cadastro do funcionário a Nação** que consta informada;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788320133655)

4.1. Após, acesse **eSocial | Endereços | Classificação de Nações** e para o registro de nação desejada informe o nome do país correspondente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28788420110103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30620910089367)

5. Regere o XML.

**Saiba mais**  
Para mais detalhes, acesse:  
     - [Como realizar a associação da Tabela de Países do layout do eSocial no cadastro do sistema?](https://tdn.totvs.com/pages/releaseview.action?pageId=334334090)  
     - [Como realizar a liberação de acesso aos cadastros de endereço na aba eSocial?](http://tdn.totvs.com/pages/viewpage.action?pageId=361449123)  
     - [O campo 'paisNac' do registro 'nascimento' é obrigatório e não está preenchido](https://tdn.totvs.com/pages/releaseview.action?pageId=364920728#ErroseA%C3%A7%C3%B5es-2165554)
