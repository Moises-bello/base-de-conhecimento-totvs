---
article_id: 360036061274
category: GPE - eSocial - Periódicos
content_hash: 8b5e3e58eb49883af4b20b198d7a46cec621b791a68ba9df9b26e0a1bfa47718
fetched_at: '2026-06-28T22:45:08.715313+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Para cenários de geração do
  evento que não existe calculo de dissidio o sistema demonstra o log com o aviso
  Não há dissídio calculado no período, confira a configuração das verbas
type: support-article
updated_at: '2025-07-22T12:20:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036061274-RH-Linha-Protheus-GPE-eSocial-S-1200-Para-cen%C3%A1rios-de-gera%C3%A7%C3%A3o-do-evento-que-n%C3%A3o-existe-calculo-de-dissidio-o-sistema-demonstra-o-log-com-o-aviso-N%C3%A3o-h%C3%A1-diss%C3%ADdio-calculado-no-per%C3%ADodo-confira-a-configura%C3%A7%C3%A3o-das-verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17010710864663)** Tempo aproximado para leitura: **00:03:00min  
  
Ocorrência**Para cenários de geração do evento que não existe calculo de dissidio o sistema demonstra o log com o aviso "**Não há dissídio calculado no período, confira a configuração das verbas**".   
Para mais informações, consulte a documentação disponível em: <http://tdn.totvs.com/pages/viewpage.action?pageId=392501017>   
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
 **Causa**Existem verbas de folha que estão configuradas indevidamente para dissidio. Verbas utilizadas no calculo da folha não podem estar preenchidas no campo **verbas para dissidi**" dentro do cadastro de verbas.  
  
Exemplo de caso: Se o código da verba **112 - Salario** estiver preenchido no campo Verba. P. Diss (**RV\_CODCOM**) dentro das configurações da verba **001 - Tarefa Padrão**, o sistema apresentaria erro.  
  
**Solução**  
Para ajuste verifique as verbas calculadas na folha do trabalhador conforme exemplo abaixo.

* Gerar o [Relatório do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-GPE-) , na aba **6-Inconsistências** serão apresentadas as verbas cuja amarração para Dissidio está incorreta;
* Acessar o cadastro de verbas no caminho: Atualizações > Definições de Calculo > Verbas (GPEA040) e realizar o ajuste na aba Dissidio Retroativo;

**Exemplo de caso:  
1.** Relatório de conferência do evento S-1200

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17010527361303)  
  
**2.** Note que na aba Inconsistência demonstrou que na verba **001 - Tarefa Padrão** eu tenho o código **112 - Salario** vinculado para ser pago como diferença de dissidio retroativo.   
De acordo com o [Manual do Dissidio Retroativo](https://tdn.totvs.com/pages/releaseview.action?pageId=220889925), esse procedimento está incorreto, pois com base na verba que está na aba de dissidio será gerado as diferenças, e não pode ser utilizada a mesma verba que já é utilizada no calculo da folha mensal. Ou seja, o campo verbas p/ dissidio (**RV\_CODCOM**) só pode conter códigos de verbas onde será pago a diferença de dissidio, e não verbas que já são utilizadas nos cálculos mensais.  
![2021-04-06_15-18-23.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008271641)  
  
**3.** Para corrigir o erro do cenário de exemplo acima você pode deixar vazio o campo Verba p/ Dissidio **(RV\_CODCOM)** da verba **001 - Tarefa Padrão**, ou preencher o campo com uma verba própria para pagamento de diferença de dissidio.    
  
**Observação:**  
É importante observar que no campo **Verba de Dissidio (RV\_CODCOM) só podem ser informadas verbas específicas para pagamento de diferença de dissidio**. Para mais informação relacionadas a configuração do Reajuste Retroativo/Dissídio no módulo **GPE**acesse a página do **[MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/releaseview.action?pageId=220889925)**.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
