---
article_id: 360024729993
category: RH - Férias
content_hash: ba31b562b05f3ef89d72137d7f48e4ea20d81a888a70b95874013b25dd770333
fetched_at: '2026-06-28T22:43:58.000293+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Férias em Dobro para funcionária Afastada
  por Licença Maternidade no Período Concessivo
type: support-article
updated_at: '2026-02-03T20:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024729993-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-F%C3%A9rias-em-Dobro-para-funcion%C3%A1ria-Afastada-por-Licen%C3%A7a-Maternidade-no-Per%C3%ADodo-Concessivo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22737874924439) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Ao realizar o cálculo de férias para funcionária afastada por licença maternidade no período concessivo, é calculado férias em dobro.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Conforme orientação da consultoria de segmentos, a licença maternidade deve ser tratada da mesma forma que o afastamento por doença e acidente de trabalho, quando o afastamento ocorre dentro do período concessivo deve ser suspenso durante o afastamento, retomando sua contagem após o término da licença. Dessa forma, a empregada mantém o direito às férias sem que o empregador seja penalizado pela redução do prazo originalmente previsto.

Foi criado o mnemônico **P\_SUSPMAT** com conteúdo padrão .F., ao habilitar com conteúdo .T. caso a empregada tenha afastamento por licença maternidade durante o período concessivo, será suspenso e estendido por prazo idêntico ao do afastamento.

**OBS:** O uso do mnemônico P**\_SUSPMAT** deve ser em conjunto do parâmetro **MV\_SUSPCON**, ou seja, para suspender os dias da licença maternidade no período concessivo o **MV\_SUSPCON** também deverá estar ativo.

Para alterar o mnemônico **P\_SUSPMAT acesse o Módulo SIGAGPE / Atualizações / Definições de Cálculo / Mnemônicos**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/38141822138903)**

Para alterar o parâmetro **MV\_SUSPCON** acesse o **Módulo SIGACFG / Ambiente / Parâmetros**   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38141833322903)

**Saiba Mais**  
[Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=144412091)  
[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=1005887809)  
[RH - Linha Protheus - GPE - Como lançar ausência por Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053399713-RH-Linha-Protheus-GPE-Como-lan%C3%A7ar-aus%C3%AAncia-por-Licen%C3%A7a-Maternidade-?source=search)  
[RH - Linha Protheus - GPE - Ajuste no cadastro de ausências para funcionarias que estavam de férias e entraram de licença maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021113232-RH-Linha-Protheus-GPE-Ajuste-no-cadastro-de-aus%C3%AAncias-para-funcionarias-que-estavam-de-f%C3%A9rias-e-entraram-de-licen%C3%A7a-maternidade?source=search)  
[RH - Linha Protheus - GPE - Como não calcular férias em dobro quando o colaborador tem afastamento dentro do período concessivo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020113451-RH-Linha-Protheus-GPE-Como-n%C3%A3o-calcular-f%C3%A9rias-em-dobro-quando-o-colaborador-tem-afastamento-dentro-do-per%C3%ADodo-concessivo)
