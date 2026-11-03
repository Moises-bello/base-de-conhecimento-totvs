---
article_id: 360021798751
category: Integrações Outros BackOffice
content_hash: b17cc42e172312083ab239d79dbded064b52a83a5c0de2ef0b9a467fa2743c1d
fetched_at: '2026-06-28T22:46:42.211106+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RH - RM - FOP - Criação da Integração TOTVS Folha de Pagamento (Linha RM) x
  BackOffice Protheus
type: support-article
updated_at: '2026-04-16T11:33:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021798751-RH-RM-FOP-Cria%C3%A7%C3%A3o-da-Integra%C3%A7%C3%A3o-TOTVS-Folha-de-Pagamento-Linha-RM-x-BackOffice-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:15 min  
  
Dúvida**Como realizar a integração TOTVS Folha de Pagamento (Linha RM) x BackOffice Protheus?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento  
  
**Solução**Para realizar a configuração da integração, realize os passos abaixo:  
  
1. Acesse o menu **Configurações | Parametrizador | Integrações | Outros Backoffice** e marque o parâmetro **Usa integração outros BackOffices**. No campo **Qtde partidas contábeis enviadas por pacote contábil**, a sugestão é a utilização de **20**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018514691/mceclip0.png)  
  
2. Acessar o menu **Integrações | Ferramentas | Configurar** e entrar com o usuário e senha do banco de dados. Na próxima tela, marque a integração **TOTVS Folha de Pagamento RM x Backoffice Protheus** e execute e faça validação se os logs e todos os scripts foram executados com sucesso:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018515151/mceclip1.png)  
  
3. Acessar o menu **INTEGRAÇÃO | MENSAGEM ÚNICA | INTEGRAÇÃO** e informar o Webservice do Protheus, o usuário e senha devem ser o de autenticação do Protheus:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018515831/mceclip2.png)  
  
4. Assim será criado o **Mapeamento de Entidades** no menu **Anexos**. As versões a serem utilizadas estão disponíveis no [manual da integração](http://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018515871/mceclip3.png)  
  
![integra__o_4_-_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360018571832/integra__o_4_-_2.jpg)  
  
5. XSLT é o padrão definido no qual as mensagens devem ser trocadas entre o RM X BackOffice Protheus. SourceCode é a codificação responsável por trazer as informações necessárias respeitando o perfil determinado pelo XLST.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018641872/mceclip4.png)  
  
6. Configuração da integração Protheus. Acesse o modulo de configuração **SIGACFG | Cadastros | Parâmetros**:  
  
![integra__o_6.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360018571852/integra__o_6.jpg)  
  
![integra__o_7.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360018571892/integra__o_7.jpg)  
  
![integra__o_8.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360018571872/integra__o_8.jpg)  
  
![integra__o_9.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360018571912/integra__o_9.jpg)  
  
7. Acesse **SCHEDULE | ADAPTER EAI** e crie os adapters da integração. Eles estão disponíveis no manual, conforme abaixo: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018642592/mceclip5.png)  
  
Saiba mais**Caso tenha interesse em conhecer ainda mais sobre a integração, [clique aqui](http://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus).
