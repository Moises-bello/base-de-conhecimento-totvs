---
article_id: 360020760691
category: GPE - eSocial - Periódicos
content_hash: d48b348074484e6d819b52114830d346a10fecb10206ddb268c7d986a1c58f31
fetched_at: '2026-06-28T22:45:07.362946+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Preenchimento incorreto
  das tabelas S050/S126. As informações de dissídio não foram geradas
type: support-article
updated_at: '2025-07-22T12:12:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020760691-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Preenchimento-incorreto-das-tabelas-S050-S126-As-informa%C3%A7%C3%B5es-de-diss%C3%ADdio-n%C3%A3o-foram-geradas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26904327609239) Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Preenchimento incorreto das tabelas S050/S126. As informações de dissídio não foram geradasIntegração **S-1200** ou **S-2299** quando existe calculo de **rescisão com dissídio** ou **complementar por dissidio** o sistema apresenta no log a mensagem "Preenchimento incorreto das tabelas **S050/S126**. As informações de dissídio não foram geradas" na integração do evento  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causas:**

* As informações cadastras nas tabelas **S050** e **S126** não estão de acordo com o que foi definido no calculo do dissidio retroativo;
* Existe calculo de dissidio retroativo, mas não existe cadastro das tabelas **S050** e **S126**.
* Existe verba configurada como verba de diferença de dissídio e o calculo do dissidio retroativo não foi executado;

**Solução**Para que essa mensagem não ocorra é necessário que as informações estejam devidamente preenchidas nas tabelas **S050** e **S126** de acordo com as informações definidas no **calculo do dissidio retroativo**, verifique abaixo os exemplos:Acesse: Atualizações - Definições de Cálculos - Manutenção de tabelas - S050 e verifique se o tipo de aumento que será utilizado está cadastrado **![](https://centraldeatendimento.totvs.com/hc/article_attachments/26904327615127)**

Na tabela **S050**, é efetuado relacionamento entre o tipo de aumento com o tipo de acordo do eSocial.  
**Exemplo:** Para um dissídio com tipo de aumento 003 (campo **RHH\_TIPOAUM**), é necessário possuir um registro com o campo "Tipo Aumento Tab. 41" preenchido com 003 e o campo "Tipo de Acordo eSocial" preenchido com o código do tipo de acordo.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26904343158295)**

No mesmo caminho selecione a tabela **S126**, a data acordo deverá ser informada nessa tabela, pois é efetuado **relacionamento** entre o **sindicato** e **data do acordo** com a descrição do acordo.  
**Exemplo:** Para um dissídio do sindicato 07 (campo **RHH\_SINDIC**) e data de acordo 01/01/2024 (campo **RHH\_DTACOR**) é necessário possuir um registro com o campo **"Sindicato"** preenchido com 07, o campo **"Data do Acordo"** preenchido com 01/01/2024 e efetuar a preenchimento da descrição do acordo coletivo no campo **"Descrição do Acordo"** e a data de efeito do acordo coletivo no campo **"Data Efeito Acordo"**. Para mais informações sobre o campo "Data Efeito Acordo", consulte a documentação a seguir: <http://tdn.totvs.com/pages/viewpage.action?pageId=403050807>.  
Observe na imagem abaixo a manutenção do cálculo do dissídio a data que consta no cabeçalho dessa rotina e o tipo de aumento informado deverão estar de acordo com as tabelas verificadas para que a integração ocorra de acordo. Ressaltamos que os campos do cabeçalho da rotina de dissídio retroativo não são editáveis e caso esteja incorreto deverá ser realizado um novo cálculo. Apenas os campos na manutenção de tabelas poderão ser alterados.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26904327618839)**

Deve existir o calculo de dissidio retroativo através da rotina GPEM690 mesmo que a diferença retroativa seja somente sobre o mês da **Rescisão**, esse calculo fará com que o sistema crie na tabela **RHH** as informações necessárias para gerar as TAGs de pagamentos de competências anteriores no **S-1200**. 1. O parâmetro **MV\_ESOCDIS** deve estar com .T. caso não exista o parâmetro na base consulte a documentação completa e veja como criar o parâmetro, link: [Documentação - S-1200 Geração Dissidio](http://tdn.totvs.com/x/laWbFg)  
  
Também deve ser verificado o campo Filial nas tabelas **S050** e **S126**, se o campo estiver preenchido a validação vai ocorrer somente para os trabalhadores da filial selecionada, apresentando erro caso exista outras Filiais com calculo de dissidio. Se o campo Filial estiver em branco a validação vai ocorrer para todas as filiais que tem o calculo do dissidio.  
  
Para acessar a documentação completa sobre o Dissidio no evento S-1200 clique no link: [Documentação - S-1200 Geração Dissidio](http://tdn.totvs.com/x/laWbFg)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes) 

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
