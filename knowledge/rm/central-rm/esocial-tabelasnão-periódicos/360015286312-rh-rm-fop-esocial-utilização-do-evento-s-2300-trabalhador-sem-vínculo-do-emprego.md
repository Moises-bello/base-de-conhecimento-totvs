---
article_id: 360015286312
category: eSocial - Tabelas/Não Periódicos
content_hash: 43f41c8fad98088ce4112ac3af2f8f3abb7ed027cf9d781215041f2d2caf092b
fetched_at: '2026-06-28T22:47:10.522261+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Utilização do evento S-2300 - Trabalhador Sem Vínculo
  do Emprego / Estatutário - Início
type: support-article
updated_at: '2024-12-30T15:05:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015286312-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-evento-S-2300-Trabalhador-Sem-V%C3%ADnculo-do-Emprego-Estatut%C3%A1rio-In%C3%ADcio
---

**Dúvida**Quando deve ser utilizado o evento S-2300 - Trabalhador Sem Vínculo do Emprego / Estatutário - Início?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**De acordo com o  Manual de Orientação do eSocial, o evento S-2300 deve ser utilizado para prestar informações cadastrais relativas a trabalhadores que não possuem vínculo de Emprego/Estatutário com a Empresa/Órgão público.

Quem **está** **obrigado** a realizar o **envio do evento**:  
1. O empregador/órgão público, órgão gestor de mão de obra, o sindicato de trabalhadores avulsos não portuários e a cooperativa, quando utilizarem mão de obra dos seguintes trabalhadores, sem vínculo de emprego ou estatutário e o concedente de estágio que se enquadrem nas categorias abaixo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13112493751063)

2. Além dos trabalhadores relacionados acima, o declarante pode cadastrar, opcionalmente, outros contribuintes individuais, que achar necessário, para facilitar seu controle interno, bem como outros trabalhadores (em sentido amplo), como os das categorias 307 (militar efetivo), 903 (bolsista) e 904 (participante de curso de formação, como etapa de concurso público, sem vínculo de emprego/estatutário).  
3. A parte concedente de estágio é obrigada a enviar os dados dos estagiários, independentemente da sua relação civil com o agente de integração e de eles receberem bolsa. Da mesma forma, deve informar os eventos S-1200 e S-1210. Por conseguinte, o agente de integração fica desobrigado de enviar os dados dos estagiários de seus clientes.  
4. Os trabalhadores da categoria 305, 401, 723 e 761 só precisam ser informados se receberem remuneração decorrente de trabalho ou da representação.  
  
**Importante**O eSocial permite que sejam enviados eventos não periódicos para determinadas categorias de funcionários que não são obrigatórias. Estes eventos podem ser enviados caso o empregador deseje ter algum tipo de controle sobre esses cadastros. Acessando o menu **Configurações | Parametrizador | eSocial | Configurações Gerais 4/7** e marcando o parâmetro **Gerar gatilho para trabalhador sem vínculo com categorias opcionais**, serão gerados gatilhos a cada situação que dispare a necessidade de envio de um evento não periódico para os funcionários de categoria 701, 711, 712, 741 e 903.

É importante lembrar que, os eventos periódicos continuarão sendo gerados normalmente, porém caso possua o evento S-2300 para esses funcionários na fila de eventos, o agrupamento de informações complementares no XML dos eventos periódicos, não será gerado. Caso não tenha enviado o S-2300 para as categorias opcionais, será incluso um grupo de informações complementares no XML dos eventos periódicos.  
  
**Saiba mais**  
Para maiores informações sobre, acesse:

* [Geração do S-1200 para autônomos cuja categoria não demandam o envio do evento S-2300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015427792)
* [RM - eSocial - Geração do S-1200 e S-1210 para autônomos do Fluxus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015349532)
* [Configurações Gerais 4/7](https://tdn.totvs.com/pages/releaseview.action?pageId=452719221)
