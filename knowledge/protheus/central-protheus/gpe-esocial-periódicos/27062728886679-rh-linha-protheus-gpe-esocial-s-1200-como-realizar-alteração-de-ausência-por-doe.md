---
article_id: 27062728886679
category: GPE - eSocial - Periódicos
content_hash: 33991b9cff6ec11b534d421441ecf35e06f6135bdb558ed355875704dd6e273d
fetched_at: '2026-06-28T22:45:07.745784+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como realizar alteração de ausência
  por doença para ausência por acidente do trabalho
type: support-article
updated_at: '2025-09-02T19:00:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27062728886679-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-realizar-altera%C3%A7%C3%A3o-de-aus%C3%AAncia-por-doen%C3%A7a-para-aus%C3%AAncia-por-acidente-do-trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27062728854935) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar alteração de afastamento por auxilio doença para afastamento por acidente do trabalho?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para alterar o afastamento, acesse **GPE - Atualizações - Lançamentos - Ausência**.  
Selecione o **funcionário** e clique em **Manutenção**.   
Altere a **coluna Cod. Ausência** de Afastamento temporário por doença, para Afastamento Temporário por Acidente do Trabalho:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27062728858263)  
Após alteração do tipo de ausência, **preencha** o campo **Data Efeito Retroativo** (R8\_DTER).   
O campo (R8\_DTER) na tabela Controle de Ausências (SR8), o qual será usado para gerar os valores retroativos do FGTS no envio do evento S-1200.

Este campo só é habilitado para preenchimento e se torna obrigatório quando se trata de uma alteração do afastamento de motivo 03 (Acidente/Doença não relacionada ao trabalho) para 01 (Acidente/Doença do trabalho).  
  
O campo **Data Alteração Motivo** (R8\_DATALT), será preenchida de acordo com a **data base** do sistema e confirme a alteração realizada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27062759411479)  
  
[Boletim técnico DRHESOCP-8601 - Criação do campo R8\_DTER (Data de efeito retroativo) na tabela SR8](https://tdn.totvs.com/pages/releaseview.action?pageId=421371836)  
[Consultoria eSocial - Base de FGTS - Conversão de licença saúde em acidente de trabalho](https://tdn.totvs.com.br/pages/releaseview.action?pageId=861547446)  
  
O **evento S-1200** levará os valores referentes a competências anteriores ao período de apuração que devem ser informados em rubricas próprias no grupo [**infoPerAnt**], e o **período a que se referem** deve ser informado no campo {**perRef**}.   
Na tag {**tpAcConv**} será informado qual foi o fato gerador da remuneração retroativa a competências anteriores, indicando um dos tipos constantes na tabela adiante, no cenário em questão vamos usar o tipo **E - Conversão de Licença Saúde em Acidente de Trabalho.**Será necessário cadastrar uma verba com o **identificador de cálculo 1966** para que no cálculo da folha de pagamento seja **gerado o valor de FGTS** e posteriormente enviado no evento de pagamento, como competências anteriores: **[FGTS de competências anteriores](https://tdn.totvs.com/pages/releaseview.action?pageId=880081335)**Ao efetuar o cálculo da folha, se for encontrado afastamento cujo **campo R8\_DATALT coincida com o período de cálculo** e que tenha **iniciado em período anterior**, o sistema pegará todos os dias de afastamento referentes aos períodos anteriores e irá gerar a **base de FGTS sobre acidente de trabalho de períodos anteriores na verba com identificador de cálculo 1966.**[RH - Linha Protheus - GPE - Como calcular FGTS retroativo quando há alteração do Motivo do afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29708825434775-RH-Linha-Protheus-GPE-Como-calcular-FGTS-retroativo-quando-h%C3%A1-altera%C3%A7%C3%A3o-do-Motivo-do-afastamento)  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
