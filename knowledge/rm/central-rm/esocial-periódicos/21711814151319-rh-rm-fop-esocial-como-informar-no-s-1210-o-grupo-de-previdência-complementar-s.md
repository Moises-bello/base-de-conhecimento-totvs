---
article_id: 21711814151319
category: esocial - Periódicos
content_hash: 39fdbffac0bcf3db65320d399ab0e027f1b212fff665640857a386640f285af8
fetched_at: '2026-06-28T22:47:09.210630+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Como informar no S-1210 o grupo de Previdência Complementar
  (S-1.2)
type: support-article
updated_at: '2025-12-29T14:47:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21711814151319-RH-RM-FOP-eSocial-Como-informar-no-S-1210-o-grupo-de-Previd%C3%AAncia-Complementar-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21711830889111) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como informar no S-1210 o grupo de Previdência Complementar?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir das versões 12.1.2302.235, 12.1.2306.182, 12.1.2310.116 e Superiores.  
  
**Solução**  
Para atender as alterações realizadas no leiaute S-1.2, para os funcionários que possuem **Previdência Complementar** foram criados novos campos no produto.  
O grupo será impresso sempre que houver lançamentos de eventos com os tipos **codIncIRRF (46, 47, 48, 61, 62, 63, 64, 65, 66) no envelope de pagamento do funcionário**.

Para correta geração, realize os seguintes passos:

1. Acesse **Administração de Pessoal | Eventos | Eventos**, para os eventos de Desconto ou Provento, nas abas Inc. Descontos e Inc. Proventos, foi incluído o campo **Tipo de Previdência Complementar**, neste passo é possível vincular o Tipo de Previdência Complementar, caso o evento não utilize nenhum código de cálculo. Caso utilize o código de cálculo referente à previdência complementar, a tag codIncIRRF será gerada automaticamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21712031773079)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21712031790487)

2. Há duas maneiras de informar os eventos da Previdência Complementar;

2.1 Acesse **eSocial | Previdência Complementar | Cadastro Previdência Complementar** e crie conforme tipo de previdência desejado e, após salvar a identificação, acesse a **aba Eventos da previdência complementar e associe os eventos** que foram configurados de acordo com o item 1;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21712086373271)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21712086378647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21712064352919)

2.2. Acesse o menu **eSocial | Previdência Complementar | Conversor Perfil DIRF x Previdência Complementar**, para que seja apresentada a tela de geração do processo e selecione a Coligada desejada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21712031799575)

![](https://tdn.totvs.com/download/attachments/791847949/image2023-10-17_20-3-27.png?version=1&modificationDate=1697583807230&api=v2)

![](https://tdn.totvs.com/download/attachments/791847949/image2023-10-17_20-3-59.png?version=1&modificationDate=1697583840180&api=v2)

**Observações:**

* É imprescindível salvar um perfil no processo DIRF/Informe de Rendimentos com os dados da Previdência complementar; caso contrário, o processo não copiará os dados;
* A criação dos cadastros ocorrerá somente para aqueles que possuírem eventos vinculados na DIRF, seja Privada, Fundo de Aposentadoria Programa Individual (FAPI) ou Fundação de Previdência Complementar do Servidor Público (Funpresp).
* Se um registro do cadastro de "Previdência Complementar" for excluído e a origem for do conversor, ele será reinseridos quando o processo for executado novamente, com o mesmo código de eventos.
* Ao cadastrar uma Previdência Complementar pelo Parametrizador da DIRF, a partir da versão desse documento, ela será automaticamente incluída no cadastro de "Previdência Complementar" do eSocial.

3. **XML S-1210**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21711814130583)

**Importante**  
Para os eventos que já constavam criados no produto e, que não possuem códigos de cálculos específicos de previdência privada e nem a informação preenchida no campo Tipo de Previdência Complementar, é necessário enviar ao governo a alteração do S-1010 com a informação da nova incidência codIncIRRF, antes do S-1210 e com competência igual ou anterior ao período desejado.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21733292140951)**

**Saiba mais**  
Para mais informações acesse:  
- [Previdência Complementar](https://tdn.totvs.com/pages/releaseview.action?pageId=791847949#1-3)  
- [Alterações - S-1210 - S-1.2](https://tdn.totvs.com/pages/releaseview.action?pageId=776113025)   
- [Códigos de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279)   
- [O campo 'cnpjEntidPC' do registro 'previdCompl' é obrigatório e não está preenchido (S.1.2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21734511893271-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-1210-ocorre-o-erro-S-1210-O-campo-cnpjEntidPC-do-registro-previdCompl-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido-S-1-2)
