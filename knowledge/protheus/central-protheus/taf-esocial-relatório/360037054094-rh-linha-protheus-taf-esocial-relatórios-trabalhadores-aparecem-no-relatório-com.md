---
article_id: 360037054094
category: TAF - eSocial - Relatório
content_hash: 8d3c3a10b859b4392f4e27cbaf7d74a96c39bc33c0f38d18b5713dee039e0747
fetched_at: '2026-06-28T22:45:20.003228+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Relatórios - Trabalhadores aparecem no
  relatório como Não Transmitido
type: support-article
updated_at: '2026-06-26T11:59:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037054094-RH-Linha-Protheus-TAF-eSocial-Relat%C3%B3rios-Trabalhadores-aparecem-no-relat%C3%B3rio-como-N%C3%A3o-Transmitido
---

**Dúvida**

Trabalhadores são exibidos no relatório como Não Transmitido

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**O erro ocorre devido ao evento S-1200, S-2299 ou S-2399 do funcionário não ter sido transmitido ou não ter sido atualizado no TAF.

**Solução**

Neste artigo iremos auxiliar a verificar se os eventos **(S-1200 ou S-2299 ou S-2399)** foram transmitidos para o eSocial e se estão protocolados com o número de recibo no TAF:

**1.** Se for evento de **Folha de Pagamento (S-1200)**, acesse a rotina **Folha de Pagamento** no TAF. Para mais detalhes, verifique a documentação abaixo:  
[RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - Como acessar a rotina dos eventos de Folha de Pagamento (S-1200) no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037457113)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26583611297303)  
  
**2.** Se for evento de Desligamento do **Trabalhador com vínculo (S-2299)** ou **Sem Vínculo (S-2399)**, acesse a rotina **Desligamento** ou **Término Trab. Sem Vínculo**, respectivamente. Para mais detalhes, verifique a documentação abaixo:

[RH - Linha Protheus - TAF - eSocial - Não Periódicos- Como acessar a rotina de desligamento para funcionários com vínculo (S-2299) e/ou sem vínculo (S-2399)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036969174)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26583611302423)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26583636226455)  
  
**3.** Filtre pelo trabalhador na rotina desejada, e clique em **Visualizar** e depois vá a aba **Info. Controle eSocial** e busque pelo campo **Nº Recibo**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26583636229143)  
  
**4.** Se estiver sem recibo, provavelmente é essa a causa do erro no relatório;

**Consultando o histórico do evento:**

**5.** Verifique o histórico deste evento e analise se o evento já foi transmitido e está com o número do recibo ou se possui alguma outra ação;

**6.** Vamos nos atentar primeiro com as legendas no TAF. Na lista dos trabalhadores, existe uma bolinha que possui uma cor e cada cor representa algum tipo de histórico do registro **(Inclusão, Alteração, Exclusão ou Aguardando Retorno de Exclusão)**. Segue exemplo na imagem abaixo:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048571794)  
  
**7.** Dê um duplo clique em uma das bolinhas para abrir a legenda:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049466573)  
  
**8.** Se o registro que estiver no relatório como "Não Transmitido" e possuir a cor da legenda verde na rotina do evento, deve verificar se o mesmo consta no eSocial. Caso contrário, acesse a rotina do Painel eSocial e realize a transmissão;  
  
**Os passos 9 a 11 se referente ao registro que possuir a cor da legenda verde ![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048571954)****(Registro incluído) e também a cor da legenda amarela ![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049466813) e em ambos os status esteja "Aceito RET". Verifique a cor da legenda em sua rotina antes de prosseguir:**

**9.** Se o registro estiver com status **"Aceito RET"** e não possuir o número de protocolo no TAF, acesse o portal do do eSocial e localize-o, e procure pelo número do recibo:

**10.** Realize o **Ajuste de Recibo** conforme a documentação abaixo:

[RH - Linha Protheus - TAF - eSocial - Funcionalidades - Como realizar ajuste de recibo do eSocial no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672)

**11.** Após preencher o protocolo, gere o relatório novamente;

**Os passos 12 a 16 se referente ao registro que possuir a cor da legenda verde ![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048571954)****(Registro incluído) e também a cor da legenda amarela ![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049466813) e em ambos os status esteja "Inconsistente". Verifique a cor da legenda em sua rotina antes de prosseguir:**

**12.** Se o registro estiver com status **"Inconsistente",** e o mesmo estiver no portal do e-Social, deverá realizar o ajuste de recibo:

[RH - Linha Protheus - TAF - eSocial - Funcionalidades - Como realizar ajuste de recibo do eSocial no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672)

**13.** Mesmo realizando o ajuste de recibo o totalizador não será exibido no relatório;

**14.** Gere o evento S-3000 no ERP de origem para excluir o referido evento e o transmita ao eSocial. A exclusão é necessário, para o TAF receber as informações do Totalizador quando for retransmitir.

**15.** O governo aceitando o evento de exclusão, volte no ERP de origem e gere novamente o evento (**S-1200 ou S-2299 ou S-2399**) e retransmita para o eSocial;

**16.** Retornando com sucesso, gere o relatório e verifique se o relatório possui os valores em seu conteúdo;

**Os passos 17 a 21 se referente ao registro que possuir somente a****cor da legenda amarela ![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049466813) status esteja, "Não Processado", "Válido", "Inválido" ou "Inconsistente". Verifique a cor da legenda em sua rotina antes de prosseguir:**

**17.** Se o evento que está visualizando em sua rotina estiver com a legenda de alteração, mas essa alteração foi enviado de forma equivocada e ainda não transmitida ao eSocial, clique em **Exibir hist. Alt.** para consultar o histórico de alteração:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049448733)  
  
**18.** Clique em **Visualizar** e observe se este registro está com o mesmo número do recibo conforme o portal do eSocial;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048556034)  
  
**19.** Se possuir o mesmo número do recibo como no governo, clique em **Sair**:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049450493)

**20.** Filtre novamente o evento alterado e exclua a alteração do TAF, ficando somente o registro original no TAF;

**Obs.:** Devido o evento estiver com status diferente de "Aceito RET", não será gerado o evento S-3000.

**21.** Gere o relatório novamente e verifique se o os valores serão preenchidos no relatório.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
