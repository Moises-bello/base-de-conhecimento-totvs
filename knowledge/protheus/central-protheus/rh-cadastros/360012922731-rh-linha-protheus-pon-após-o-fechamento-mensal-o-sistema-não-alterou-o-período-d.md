---
article_id: 360012922731
category: RH - Cadastros
content_hash: 2fcf16bfb7686303bf802b0b9de711ddc84fb8fdc1563f6f31e0d4da85a71c96
fetched_at: '2026-06-28T22:44:52.745888+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Após o fechamento mensal, o sistema não alterou
  o período de apontamento
type: support-article
updated_at: '2026-02-16T14:11:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012922731-RH-Linha-Protheus-PON-Ap%C3%B3s-o-fechamento-mensal-o-sistema-n%C3%A3o-alterou-o-per%C3%ADodo-de-apontamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31994311668759) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
No módulo Ponto Eletrônico, ao realizar o **Fechamento Mensa**l de um período, o sistema **não altera o parâmetro** **MV\_PONMES** automaticamente para o próximo período.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Esse incidente ocorre, pois o conteúdo dos parâmetros **MV\_PAPONTA** e **MV\_PONMES** estão iguais (preenchidos com data), isso acontece quando o usuário inclui o período de apontamento pela opção **Período** e não na opção **Dia Inicial/Final**.  
  
A opção de alteração por **período** é utilizada quando existe a necessidade da empresa possuir um [período maior ou menor que 30 dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011060231) , se configurado dessa forma a inclusão do período seguinte terá que ser manual.  
  
Para que o processo seja efetuado sem problemas e o período automaticamente seja incluído, é necessário que sua configuração esteja conforme abaixo:  
  
**1.** Acessar a rotina de Período de apontamento em **Atualizações > Cadastro do Ponto > Períodos de Apontamentos.** clique em **Modif. Per. Apont.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36159176114199)  
  
**2.** Selecionar **Dia Inicial/Final** e **Salvar:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36159161106583)  
  
**3.** Na opção **Dia Inicial/Final** cadastre o primeiro e o último dia do período de apontamento.   
Exemplo, informar 01/31 e clicar em **Salvar**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36159176122391)  
  
**4.** Na próxima tela, inserir o último dia do período em questão, exemplo 31/10/2025 e clicar em **OK**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36159176124823)

**5.** Será apresentado a mensagem de informativo abaixo, clicar em **Fechar**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36159161120151)  
  
**6.** Execute novamente a rotina de **Fechamento Mensal** e ao finalizar sem erros, esses parâmetros serão alterados com sucesso.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como efetuar o Fechamento Mensal do Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232-RH-Linha-Protheus-PON-Como-efetuar-o-Fechamento-Mensal-do-Ponto)  
[RH - Linha Protheus - PON - Migração de dados no Fechamento Mensal do Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013084192-RH-Linha-Protheus-PON-Migra%C3%A7%C3%A3o-de-dados-no-Fechamento-Mensal-do-Ponto)  
[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)
