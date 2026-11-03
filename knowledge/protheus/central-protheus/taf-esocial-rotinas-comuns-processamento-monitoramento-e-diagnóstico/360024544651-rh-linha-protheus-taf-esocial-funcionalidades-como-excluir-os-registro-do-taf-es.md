---
article_id: 360024544651
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 7a0136be8d9fdf6715c61c8e4ef5dc626a2fec743d82a29f167469a02de43bae
fetched_at: '2026-06-28T22:45:20.976171+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Funcionalidades - Como excluir os registro
  do TAF eSocial
type: support-article
updated_at: '2024-08-02T17:18:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024544651-RH-Linha-Protheus-TAF-eSocial-Funcionalidades-Como-excluir-os-registro-do-TAF-eSocial
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25348283497879)* Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como excluir os registro do eSocial  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões  
  
**Solução**1 - Se o registro que deseja excluir não estiver no eSocial e no monitoramento do TAF estiver com o status "inconsistente", o TAF não vai gerar o evento S-3000; Ele apenas vai excluir o registro do sistema.  
  
2 - Se precisa gerar o evento S-3000, verifique se o seu ERP possui alguma funcionalidade que integra e gera automaticamente a exclusão dos eventos no TAF;  
  
3 - Na impossibilidade de integrar as exclusões do sistema de origem ou o evento estiver inconsistente, a exclusão pode ser feita manualmente no TAF;  
  
4 - Para realizar a exclusão, acesse a rotina do evento e filtre pelo registro que deseja apagar do sistema;  
  
5 - No bloco "Outras Ações" clique em Excluir Registro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25368816766231)  
  
6 - Para eventos de tabela e Cadastros do Trabalhador (S-2200/S-2205/S-2206/S-2190/S-2399) acesse:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360022726151)

7. Pelo monitor Painel eSocial, também é possível excluir o registro;

Selecione o ícone "..." (três pontinhos) localizado na linha do registro que deseja excluir.

Em seguida, selecione a opção "Excluir Registro" > o registro será aberto > confirme a exclusão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25369142512663)  
  
8 - Se o evento possuir número de recibo, será gerado um evento S-3000, se o registro não possuir número de recibo, o registro será excluído do sistema, e se existir um registro anterior, com número de recibo, o mesmo será reativado

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049242733)  
  
9 - Clique em **Confirmar**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25348283504791)  
  
10 - Será exibido a tela de que o registro foi excluído com sucesso:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049242793)

* **Caso a exclusão seja um evento de tabela:**
  + Se estiver transmitido, será gerado um evento de exclusão com o nome do próprio evento a ser excluído, que deverá ser transmitido ao Governo;
  + Se não estiver transmitido, o evento será excluído logicamente da aplicação, fisicamente ele permanece na base de dados, mas fica como deletado;
* **Caso a exclusão seja um evento periódico ou não periódico:**
* + - Se estiver transmitido, será gerado um evento S-3000 que deverá ser transmitido ao Governo( [Exclusão de Eventos - TAFA269 - TAF - P12](http://tdn.totvs.com/pages/viewpage.action?pageId=240290610) );
    - Se não estiver transmitido, o evento será excluído logicamente da aplicação, fisicamente ele permanece na base de dados, mas fica como deletado.



**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
