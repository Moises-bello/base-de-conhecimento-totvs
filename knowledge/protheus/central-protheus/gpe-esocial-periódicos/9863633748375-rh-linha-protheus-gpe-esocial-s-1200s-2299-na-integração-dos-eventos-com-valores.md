---
article_id: 9863633748375
category: GPE - eSocial - Periódicos
content_hash: 568dc6f2fee90f096b60efb3256c4c85e2d1e631cbf5b15e1858397f0d118ef5
fetched_at: '2026-06-28T22:45:08.843099+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Na integração dos eventos
  com valores de dissidio, o sistema apresenta a mensagem "Preenchimento incorreto
  das tabelas S050/S126. As informações de dissídio não foram geradas"
type: support-article
updated_at: '2025-07-22T13:01:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9863633748375-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Na-integra%C3%A7%C3%A3o-dos-eventos-com-valores-de-dissidio-o-sistema-apresenta-a-mensagem-Preenchimento-incorreto-das-tabelas-S050-S126-As-informa%C3%A7%C3%B5es-de-diss%C3%ADdio-n%C3%A3o-foram-geradas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25161566486039) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Na integração dos **eventos com valores de dissidio**, o sistema apresenta a mensagem [**FALHA**] **Preenchimento incorreto das tabelas S050/S126**. As informações de dissídio não foram geradas Data de Acordo DD/MM/AAAA, para o sindicato XX, não tem descrição do acordo preenchida na tabela S126."  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causas**

* As informações cadastrais nas tabelas **S050** e **S126** não estão de acordo com o que foi definido no **cabeçalho do calculo do dissidio** retroativo;
* Existe calculo de dissidio retroativo, mas não existe cadastro das tabelas **S050** e **S126**.

**Solução**Para que essa mensagem não ocorra é necessário que as informações estejam devidamente preenchidas nas tabelas **S050** e **S126** de acordo com as informações definidas no calculo do dissidio retroativo, verifique abaixo os exemplos:  
Acesse: Atualizações - Definições de Cálculos - Manutenção de tabelas - S050 e verifique se o tipo de aumento que será utilizado está cadastrado  
  
**Tabela S050 -**  Essa tabela é responsável pelo relacionamento entre o tipo de aumento com o tipo de acordo do eSocial.  
  
**Exemplo:** Para um dissídio com tipo de aumento 003 (campo **RHH\_TIPOAUM**), é necessário possuir um registro com o campo **Tipo Aumento Tab. 41** preenchido com 003 e o campo **Tipo de Acordo eSocial** preenchido com o código do tipo de acordo.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074736691735)  
  
No [leiaute esocial vigente](https://www.gov.br/esocial/pt-br/documentacao-tecnica) é possível encontrar os valores válidos para os tipos de acordo, cabe a empresa a opção de qual código irá utilizar  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229674591511)  
  
No mesmo caminho selecione a tabela **S126**, a data acordo deverá ser informada nessa tabela, pois é efetuado **relacionamento** entre o **sindicato** e **data do acordo** com a descrição do acordo.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12075485922839)

**Exemplo**: Para um dissídio do sindicato 01 (campo **RHH\_SINDIC**) e data de acordo 09/06/2022 (campo **RHH\_DTACOR**) é necessário possuir um registro com o campo **Sindicato** preenchido com 01, o campo **Data do Acordo** preenchido com 09/06/2022 e efetuar a preenchimento da descrição do acordo coletivo no campo **Descrição do Acordo.**   
A data efeito do acordo coletivo no campo **Data Efeito Acordo**. Para mais informações sobre o campo **Data Efeito Acordo**, consulte a documentação a seguir: <http://tdn.totvs.com/pages/viewpage.action?pageId=403050807>.  
  
Observe na imagem abaixo a manutenção do **cálculo do dissídio** a **data acordo** que consta no cabeçalho dessa rotina e o **tipo de aumento** informado deverão estar de acordo com as tabelas verificadas para que a integração ocorra de acordo. Ressaltamos que os campos do **cabeçalho da rotina de dissídio retroativo não são editáveis** e caso esteja incorreto deverá ser realizado um novo cálculo. Apenas os campos na manutenção de tabelas poderão ser alterados.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12075346626455)  
  
**Importante**: O parâmetro **MV\_ESOCDIS** deve estar com .T. para que as informações sejam integradas nas *tags* referente a periodos anteriores **infoPerAnt**do leiaute esocial vigente.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12073947981847)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Documentação - S-1200 Geração Dissidio](http://tdn.totvs.com/x/laWbFg)  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar informações de dissidio e rescisão complementar por dissidio no esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-informa%C3%A7%C3%B5es-de-dissidio-e-rescis%C3%A3o-complementar-por-dissidio-no-esocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
