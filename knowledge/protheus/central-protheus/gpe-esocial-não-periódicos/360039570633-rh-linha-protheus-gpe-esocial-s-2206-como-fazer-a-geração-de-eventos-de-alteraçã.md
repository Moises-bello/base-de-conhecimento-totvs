---
article_id: 360039570633
category: GPE - eSocial - Não Periódicos
content_hash: 674169198722921bdf489489789cb477b540cc3515bb7b227405d313a7c65751
fetched_at: '2026-06-28T22:45:04.687835+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Como fazer a geração de eventos
  de alteração contratual S-2206 / S-2306 em lote
type: support-article
updated_at: '2026-06-16T11:25:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039570633-RH-Linha-Protheus-GPE-eSocial-S-2206-Como-fazer-a-gera%C3%A7%C3%A3o-de-eventos-de-altera%C3%A7%C3%A3o-contratual-S-2206-S-2306-em-lote
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28057012028567)** Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como fazer a geração de eventos de alteração contratual **S-2206/S-2306** em lote?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Foi disponibilizado no sistema a rotina GPEM047 (Geração Eventos S-2206/S-2306 Em Lote) onde é possível gerar os eventos de alteração contratual em massa para o TAF.  
  
Adicionando no menu via Configurador a opção de **Geração S-2206/S-2306** em Cadastros\Menus, selecione o modulo Gestão de Pessoal. A opção pode ser inclusa em qualquer parte do menu, ficando a critério do cliente:  
  
![image2020-4-27_18-1-32.png](https://tdn.totvs.com/download/attachments/490975169/image2020-4-27_18-1-32.png?version=1&modificationDate=1588021292540&api=v2)  
  
Preenchimento dos campos:  
![image2020-4-27_18-2-24.png](https://tdn.totvs.com/download/attachments/490975169/image2020-4-27_18-2-24.png?version=1&modificationDate=1588021344827&api=v2)  
  
Após clicar em **OK**, clique no botão **Gerar** e digite **SIGAGPE**. Será apresentada mensagem:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9251861614999)  
  
Cliente em **SIM** para confirmar a geração do Menu e depois em **SIM** novamente para conformar a substituição.  
![](https://tdn.totvs.com/download/attachments/490975169/image2020-4-27_18-4-6.png?version=1&modificationDate=1588021446693&api=v2)  
  
2 - Entre novamente no Gestão de Pessoal e verifique a apresentação da nova opção no Menu:  
![](https://tdn.totvs.com/download/attachments/490975169/image2020-4-27_18-13-16.png?version=1&modificationDate=1588021996717&api=v2)  
  
3 - Criação da rotina GPEM047 para ser possível gerar o evento S-2206/S-2306 em lote, informando os parâmetros para a geração na tela abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9251940695959)  
![image2019-11-26_10-45-0.png](https://tdn.totvs.com/download/attachments/490975169/image2019-11-26_10-45-0.png?version=1&modificationDate=1574779500303&api=v2)  
  
Por padrão a rotina GPEM047 gera o evento S-2206 com a descrição **Alteração no contrato de trabalho**, porém, foi disponibilizado espaço para informar a descrição da alteração contratual, a ser gerada na tag **dscAlt** dos eventos S-2206 em lote.   
Segue **boletim técnico**: <https://tdn.totvs.com/pages/releaseview.action?pageId=845752877>  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28057017834775)

O preenchimento é opcional. Caso não informe nenhum dos campos, a geração dos eventos seguirá com a descrição padrão acima.

Ao **Confirmar**, serão gerados eventos S-2206/S-2306 dos trabalhadores escolhidos, considerando os dados mais atuais do Cadastro de Funcionários, Horários, Atualização Salarial, conforme layout do eSocial.  
Durante o processo será gerado um log de processamento, conforme demonstrado:  
![](https://tdn.totvs.com/download/attachments/490975169/image2019-11-26_10-41-19.png?version=1&modificationDate=1574779279517&api=v2)  
  
Para acessar o boletim técnico, clique no *link*: <https://tdn.totvs.com/pages/releaseview.action?pageId=490975169>   
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [*TOTVS Informa*](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".
