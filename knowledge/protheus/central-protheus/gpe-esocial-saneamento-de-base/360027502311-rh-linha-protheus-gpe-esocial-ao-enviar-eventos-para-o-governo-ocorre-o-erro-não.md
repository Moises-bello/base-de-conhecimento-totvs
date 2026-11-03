---
article_id: 360027502311
category: GPE - eSocial - Saneamento de Base
content_hash: df6163085321184c6c371fa298cca3977806e483f1c4e1e487c04e140ba6f360
fetched_at: '2026-06-28T22:45:01.564214+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - Ao enviar eventos para o governo ocorre
  o erro: Não foi possível obter a mensagem de inconsistência'
type: support-article
updated_at: '2023-09-27T16:57:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027502311-RH-Linha-Protheus-GPE-eSocial-Ao-enviar-eventos-para-o-governo-ocorre-o-erro-N%C3%A3o-foi-poss%C3%ADvel-obter-a-mensagem-de-inconsist%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17848174253975) Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao enviar eventos para o governo e retornar alguma inconsistência, ocorre o erro: Não foi possível obter a mensagem de inconsistência.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17847913700375)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**O erro ocorre por conta do Leiaute do **GPE** ou **TAF** estarem divergentes ou estar configurado com Leiaute **S-1.1** no **GPE** ou **TAF**, a convivência entre as versões **S-1.0** e **S-1.1** no ambiente de produção teve o prazo de **16/01/2023 a 19/03/2023**, a partir dessa data é obrigatório o envio dos evento a partir do Leiaute **S-1.1**Também pode ocorrer caso esteja utilizando a nova versão simplificada **S-1.1,** nesse caso o **TAF** e **GPE** também precisam estar na mesma versão.  
 **Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Verificar o leiaute do **GPE** e **TAF** em > Miscelânea > eSocial > Carga Inicial;   
![K0HhlhmqOF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099956474)  
  
**1.1** Clicar em visualizar versão dos eventos, exemplo utilizando a versão S-1.0: **![zp43zWGbM8.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412249186199)**  
 **1.2** Exemplo utilizando a versão S-1.1:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17847361278359)  
  
**2.** Caso a versão do **GPE** esteja com **S\_01\_00\_00** será necessário aplicar os últimos pacotes e dicionário do site [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais) e atualizar o parâmetro **MV\_VLESOC** para **S\_01\_01\_00**  
  
**3.** Caso a versão do **TAF** esteja com **S\_01\_00\_00** será necessário aplicar os últimos pacotes mencionado no item 2 e atualizar o parâmetro **MV\_TAFVLES** para **S\_01\_01\_00**  
  
**4.** Caso já esteja utilizando a nova versão do eSocial **S-1.1**, os parâmetros **MV\_VLESOC** e **MV\_TAFVLES** deve estar com o mesmo conteúdo **S\_01\_01\_00  
  
Obs.:** Para alteração dos parâmetros, utilize o caminho: *SIGACFG > Configurador > Ambiente > Cadastros > Parâmetros:***![](https://centraldeatendimento.totvs.com/hc/article_attachments/17848115504279)**[TAF- Atualização - Como atualizar a versão do layout para o e-Social Simplificado S 1.1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022224812-TAF-Atualiza%C3%A7%C3%A3o-Como-atualizar-a-vers%C3%A3o-do-layout-para-o-e-Social-Simplificado-S-1-0?source=search)  
  
**5.** Verifique sua pasta Schemas do TSS se esta atualizada, link com procedimentos: **[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)**  
**Saiba Mais**Para saber mais consulte os links abaixo:  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
