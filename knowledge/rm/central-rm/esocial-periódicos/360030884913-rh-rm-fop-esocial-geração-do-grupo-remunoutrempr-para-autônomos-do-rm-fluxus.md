---
article_id: 360030884913
category: esocial - Periódicos
content_hash: fadd4ea361f0f72b941d77001b0f07fad6f148fc67e71eaf59dc98ce674a65d4
fetched_at: '2026-06-28T22:47:09.393360+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Geração do grupo remunOutrEmpr para autônomos do
  RM Fluxus
type: support-article
updated_at: '2024-06-26T18:31:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030884913-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-grupo-remunOutrEmpr-para-aut%C3%B4nomos-do-RM-Fluxus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24398561283991) Tempo aproximado para leitura: 00:03:30 min  
  
Dúvida**Como gerar as tags de remuneração outro emprego **remunOutrEmpr** para autônomos do **TOTVS Gestão Financeira**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da versão 12.1.26  
  
**Solução**Para que o grupo **remunOutrEmpr** seja corretamente gerado para casos de autônomos cadastrados no TOTVS Gestão Financeira, realize os passos abaixo:  
1. Acesse **Folha de Pagamento |** **Administração de Pessoal | Cliente Fornecedor | Anexo | Múltiplos vínculos Autônomos** e inclua um registro. Será necessário o preenchimento dos campos **Tipo da Inscrição**, **Número da Inscrição**, **Código da Categoria**, **Competência Inicial**, **Salário contribuição INSS** e **Valor Desconto INSS**referentes ao vínculo empregatício externo à base RM;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059070653)

2. Acesse****Folha de Pagamento |** **Administração de Pessoal | Cliente Fornecedor | eSocial**** e preencha o campo****Indicador de Desconto da Contribuição Previdenciária do Declarante****;

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058158794)**

O campo **Indicador de Desconto da Contribuição Previdenciária do Declarante** deverá ser preenchido referente aos valores do autônomo na empresa onde o cadastro está sendo realizado;  
3. Após o cadastro das informações basta gerar o XML **S-1200** em **Folha de Pagamento | eSocial | Gerar XML.**Os grupos **infoMV** e **remunOutrEmpr** serão gerados considerando as informações cadastradas.

**Importante**Para versões anteriores à 12.1.26 a geração do grupo **remunOutrEmpr** deverá seguir o link abaixo:  
[Como gerar as tags de remuneração outro emprego para autônomos do Totvs Gestão Financeira?](https://tdn.totvs.com/pages/releaseview.action?pageId=421375083#1-1)  
No caso de mais de um lançamento financeiro para o autônomo com o campo complementar **INDMV** preenchido com valores diferentes, será considerado sempre o maior valor para a geração do XML  
  
**Saiba mais**Para mais informações sobre o processo, acesse:  
   • [Cálculo de INSS conforme o eSocial para múltiplos vínculos](http://tdn.totvs.com/pages/viewpage.action?pageId=440829559#C%C3%A1lculodeINSSconformeoeSocialparam%C3%BAltiplosv%C3%ADnculos.-7)
