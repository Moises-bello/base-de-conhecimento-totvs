---
article_id: 36977499360535
category: esocial - Periódicos
content_hash: c0ae4e7889575746333836e7394936c2f51a1c86b6acffc4b6a659ff5efe67a0
fetched_at: '2026-06-28T22:47:09.493422+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - S-1200/S-2299 Código do erro: 198 Descrição: O trabalhador
  XXX, matrícula XXX, possui parcela(s) de empréstimo consignado do Programa Crédito
  do Trabalhador prevista para desconto na competência de apuração XX/XXXX.'
type: support-article
updated_at: '2026-03-17T22:06:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36977499360535-RH-RM-FOP-eSocial-S-1200-S-2299-C%C3%B3digo-do-erro-198-Descri%C3%A7%C3%A3o-O-trabalhador-XXX-matr%C3%ADcula-XXX-possui-parcela-s-de-empr%C3%A9stimo-consignado-do-Programa-Cr%C3%A9dito-do-Trabalhador-prevista-para-desconto-na-compet%C3%AAncia-de-apura%C3%A7%C3%A3o-XX-XXXX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36977546404375)  Tempo aproximado para leitura: **00:02:00 min**  
  
  
**Ocorrência**  
Ao enviar o evento S1200/S-2299 para o Governo, ocorre o erro: **Código do erro 198:** **O trabalhador** **XXXXXXXXX****, matrícula** **XXXXXXXXX****, possui parcela(s) de empréstimo Crédito do Trabalhador do Programa Crédito do Trabalhador prevista para desconto na competência de apuração XX****/XXXX**. **No entanto, o empregador informou os dados incorretos ou não informou rubrica de desconto do empréstimo neste evento. Verifique a informação correta no arquivo disponibilizado no Portal Emprega Brasil e retifique este evento. Foram localizados os seguintes contratos de empréstimo consignado com previsão de pagamento de parcela nesta competência:** **Instituição Financeira: XXX, Contrato XXXXXXXXXX | Instituição Financeira: XXX, Contrato XXXXXXXXXX**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões - 12.1.2502.219, 12.1.2506.167, 12.1.2510.101 e superiores  
  
**Causa**  
Esse erro pode ser apresentado no envio dos eventos **S-1200** ou **S-2299** quando ocorre alguma das situações abaixo:

* **Desconto do empréstimo não lançado na folha** na competência em que o PCT possui parcela prevista;
* **Rubrica do empréstimo configurada incorretamente**, impedindo o envio correto ao eSocial;
* O **XML leva a verba de desconto**, porém **sem a TAG** `<descFolha>` **contendo os dados obrigatórios do contrato**, como número do contrato e instituição financeira.

**Solução**

Para solucionar o erro, siga os passos abaixo:

**1.** Validar se o desconto do empréstimo está corretamente lançado na folha:  
1.1. Acesse o módulo **Folha de Pagamento** no RM;  
1.2. Verifique se o evento de desconto do empréstimo consignado foi lançado corretamente na competência em questão;  
1.3. Caso não tenha sido lançado, inclua o evento de desconto no envelope de pagamento e gere novamente o evento **S-1200;**

**2.** Conferir a configuração da rubrica de empréstimo consignado:  
2.1. Acesse o módulo **Tabela de Rubricas** no RM;  
2.2. Verifique se a rubrica de empréstimo consignado está configurada corretamente;  
2.3. Se necessário, ajuste a rubrica envie o S1010 e gere novamente o evento **S-1200** para garantir que a rubrica correta seja enviada;

**3.** Verificar a TAG `<descFolha>` no XML:  
3.1. Gere o arquivo XML do evento **S-1200** ou **S-2299** no RM;  
3.2. Abra o XML e verifique se a TAG `<descFolha>` está presente e contém todos os dados obrigatórios, como o número do contrato e a instituição financeira;  
3.3. Se a TAG estiver ausente ou incompleta, verifique a configuração de consignado no cadastro do funcionário e reenvie o evento com a correção no XML.

**Saiba Mais**  
Para mais informações, acesse:

* [RH - RM - FOP - eSocial - S-1200/S-2299 Erro código 8: Grupo #39;Informacoes de desconto do emprestimo em folha#39; deve ser preenchido.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32133966658455-RH-RM-FOP-eSocial-S-1200-S-2299-Erro-c%C3%B3digo-8-Grupo-39-Informacoes-de-desconto-do-emprestimo-em-folha-39-deve-ser-preenchido)
* [RH - RM - FOP - eSocial - Erro na geração do S-1200 e S-2299: O valor do campo 'nrDoc' do registro 'descFolha' excedeu o tamanho do campo e foi truncado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32291024548375-RH-RM-FOP-eSocial-Erro-na-gera%C3%A7%C3%A3o-do-S-1200-e-S-2299-O-valor-do-campo-nrDoc-do-registro-descFolha-excedeu-o-tamanho-do-campo-e-foi-truncado)
* [RH - RM - FOP - eSocial - Erro de Schema nrDoc na transmissão dos eventos S-2299/S-1200 com o Governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31996414541975-RH-RM-FOP-eSocial-Erro-de-Schema-nrDoc-na-transmiss%C3%A3o-dos-eventos-S-2299-S-1200-com-o-Governo)
* [RH - RM - FOP - eSocial - Erro de Schema instFinanc na transmissão dos eventos S-2299/S-1200 com o Governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31988354717847-RH-RM-FOP-eSocial-Erro-de-Schema-instFinanc-na-transmiss%C3%A3o-dos-eventos-S-2299-S-1200-com-o-Governo)
