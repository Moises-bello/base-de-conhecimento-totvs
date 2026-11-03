---
article_id: 27883810936983
category: eSocial - Gerar XML/ Integração Evento
content_hash: 748e6f0ca92ecb58b9851eb8e55904a822095028e6e92027004aee37876840ad
fetched_at: '2026-06-28T22:47:12.237917+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O grupo descFolha é obrigatório
  devido o evento XXXX ter a natureza da rubrica 9253'
type: support-article
updated_at: '2026-06-05T17:14:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27883810936983-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-grupo-descFolha-%C3%A9-obrigat%C3%B3rio-devido-o-evento-XXXX-ter-a-natureza-da-rubrica-9253
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27883810885911)**Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao gerar evento S-1200, S-1202, S-1207, S-2299 ou S-2399, é apresentada mensagem: **O grupo descFolha é obrigatório devido o evento XXXX ter a natureza da rubrica 9253. Preencha as informações do empréstimo eConsignado disponível no anexo do funcionário**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27883783145751)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da versão 12.1.2402.245 e superiores  
  
**Causa**  
Esse erro geralmente ocorre quando foi informado no cadastro de empréstimos uma verba com natureza de rubrica **9253 - Empréstimos ECONSIGNADO - Desconto** mas o parâmetro **Funcionário firmou contrato de empréstimo consignado com garantia de FGTS** está desmarcado.  
  
**Solução**  
Para correção, siga os passos considerando as opções abaixo:

* **Empréstimo NÃO É eConsignado**

Acesse o menu **Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Empréstimos** e verifique a verba informada no campo **Evento para Desconto**.

Posteriormente, acesse o menu **Administração de Pessoal | Eventos**, faça a edição da verba informada no cadastro do empréstimo e altere a natureza de rubrica para uma **diferente de 9253**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27883810894615)

* **Empréstimo É eConsginado**

Acesse o menu **Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Empréstimos** e verifique a verba informada no campo **Evento para Desconto**. Ela deverá possuir a natureza de rubrica 9253.

Além disso, deve-se selecionar a modalidade do empréstimo e preencher os campos **Matrícula da instituição Consignatária** e **No. do contrato de empréstimo consignado CEF**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36786014144535)

Após informar os dados, o XML será corretamente gerado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27883810897687)

Ainda que o sistema já esteja preparado para configuração da rubrica **9253**- Empréstimos eConsignado - Desconto, o envio através do evento S-1010 está condicionada à tag *iniValid (deve ser **igual ou posterior ao mês de início do eConsignado**no eSocial)*. Portanto, mesmo que as informações do eConsignado estejam previstas na solução da NT 04/2024 e as parametrizações realizadas no sistema, elas **só serão enviadas após a oficialização da normatização supracitada.****Saiba mais**  
Para mais informações, acesse:  
     - [Nota Técnica V. S-1.2 03/2024 e 04/2024](https://tdn.totvs.com/pages/viewpage.action?pageId=853920910)  
     -  [Leiaute Versão S-1.3 e NT 01/2024](https://tdn.totvs.com/pages/releaseview.action?pageId=862114556)
