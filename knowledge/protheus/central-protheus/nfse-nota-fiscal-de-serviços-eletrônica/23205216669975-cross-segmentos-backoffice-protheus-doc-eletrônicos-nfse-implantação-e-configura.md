---
article_id: 23205216669975
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f01d6f935ccf9a0bf6878abd7886b05bdf2aed47f26b2c8c6341e8e02440bdef
fetched_at: '2026-06-28T22:39:57.494738+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Implantação
  e Configuração de Envio do DANFSE e/ou XML por e-mail
type: support-article
updated_at: '2024-06-06T19:12:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23205216669975-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Implanta%C3%A7%C3%A3o-e-Configura%C3%A7%C3%A3o-de-Envio-do-DANFSE-e-ou-XML-por-e-mail
---

**Dúvida**Como realizar a configuração para o envio do DANFSE e/ou XML por e-mail?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões  
  
**Solução**Seguem abaixo os detalhes para realização da configuração do envio do DANFSE e/ou XML no Protheus:  
  
**1.** Primeiramente é necessário que seja incluso o arquivo **printer.exe** dentro das pastas Appserver e SmartClient do Protheus e também do TSS.  
  
Windows: [64](https://suporte.totvs.com/portal/p/10098/download#detail/693168) | [32](https://suporte.totvs.com/portal/p/10098/download#detail/693163)  
Linux: [Printer 64](https://suporte.totvs.com/portal/p/10098/download#detail/711950) - [PDF Printer 64](https://suporte.totvs.com/portal/p/10098/download#detail/693160) | [Printer 32](https://suporte.totvs.com/portal/p/10098/download#detail/711949) - [PDF Printer 32](https://suporte.totvs.com/portal/p/10098/download#detail/693159)  
MAC: [Printer](https://suporte.totvs.com/portal/p/10098/download#detail/693162)  
  
**2.** Fazer um backup do RPO e aplicar o último **Pacote Acumulado do Protheus** (Expedição Contínua) conforme release:  
- [12.1.33](https://suporte.totvs.com/portal/p/10098/download#detail/1040489) | [12.1.2210](https://suporte.totvs.com/portal/p/10098/download#detail/1081419) | [12.1.2310](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)  
  
**3.** Fazer um backup e atualizar o RPO conforme documentação abaixo:  
- [MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)  
  
**4.** Após isso, deverá acessar o Wizard.cfg através da rotina FISA022, preencher todos os campos por completo e na última tela, se atentar com os dados da conta de e-mail e marcar o último campo conforme necessidade:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23347639914903)  
  
Lembrando que as opções acima, seguem o padrão abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23205346150807)  
  
**EXEMPLOS DE UTILIZAÇÃO**  
  
- Se configurada a opção 0, nem o XML e nem o DANFSE serão enviados por e-mail;  
- Se configuradas as opções 3 ou 5 (DANFSE Customizado), o schedule consultará no TSS os documentos autorizados (NFS-e) e após este processo, é disparado pelo TSS o DANFSE por e-mail;  
- Se configuradas as opções 1, 2 ou 4 (XML e/ou DANFSE Padrão), o DANFSE e XML serão gerados pelo TSS, e após a autorização do documento, será iniciado o processo do envio do e-mail.  
  
**IMPORTANTE!**Para as **opções padrões** (1, 2 ou 4), **não requer schedule** configurada no ERP.   
Já para as opções 3 ou 5 **(DANFSE Customizado) requer o schedule** configurado, portanto, favor se atentar ao item 4 do passo à passo mais abaixo.

**5.** Uma vez preenchidos, com modelo 2 por exemplo (Enviar XML + DANFSE do TSS), será apresentada a mensagem abaixo caso os dados estejam todos corretos:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23205832755223)  
  
**6.** O DANFSE poderá ser tanto no padrão, quanto customizado. E caso opte pelo **DANFSE Customizado**, é necessário uma configuração adicional:  
O primeiro passo seria a criação de uma pergunta dentro do Grupo de Perguntas via Configurador (SIGACFG):  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23206388498071)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23206344785687)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23206490916247)  
  
**Grupo**: AUTDSTMAIL   
**Pergunta**: Qual modelo do Documento ?   
**Tamanho**: 9   
**Tipo**: Caracter   
**Help**: Qual modelo do Documento deseja utilizar para realizar o envio de e-mail do DANFE/DANFSE gerado no ERP?   
Exemplo:   
55; (Para Considerar somente NF-e)   
55;56; (Para considerar NF-e e NFS-e)   
56; (Para Considerar somente NFS-e)  
  
Uma vez configurado a pergunta na Base de Dados, a rotina AUTDSTMAIL deverá ser cadastrada via Schedules, no menu 'Agendamentos', onde as principais informações são os campos:  
  
**Rotina:** Informando AUTDSTMAIL e configurar o modelo do documento a ser distribuído. **Empresa/Filial:** Empresas/filiais que irão realizar o processo de envio dos DANFSE customizados.  
[Schedule - Como agendar a execução de rotinas?](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23206543373079)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23347639930391)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23347639939735)  
 **7.** Após essas configurações, o ambiente estará preparado e pronto para o envio dos DANFSE e/ou XML via e-mail.  
  
Documentação completa: [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=839968168)  
  
**Obs.:** Importante ressaltar que essa configuração é gerada pelo Protheus/TSS **com base nos dados do RPS (Recibo Provisório de Serviços)**, porém o envio do XML/PDF original **da NFSE** **gerada pela prefeitura**, ainda continuará sendo uma outra opção e enviada exclusivamente pela própria pela prefeitura.
