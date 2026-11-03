---
article_id: 360000240188
category: Relatórios
content_hash: 2bb30e4c2ec42bf41973bb9a14224a0c0139ddfc3e1ddf1d4cbbc70d58e9ad2c
fetched_at: '2026-06-28T22:47:43.496252+00:00'
product: rm
section_id: 1500000861522
source: central-rm
title: RH - RM - SMT - Como gerar o Relatório PPP
type: support-article
updated_at: '2025-05-07T16:39:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000240188-RH-RM-SMT-Como-gerar-o-Relat%C3%B3rio-PPP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036358388375) Tempo aproximado para leitura: 00:00:45 min****Dúvida**Como gerar o relatório do PPP (Perfil Profissiográfico Previdenciário)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - Todas as versões  
  
**Solução**Para geração do relatório **PPP** (Perfil Profissiográfico Previdenciário), siga as orientações abaixo:

1 - Acesse o Módulo RH | Segurança e Saúde Ocupacional

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639752687895)

2 - Guia Relatórios | PPP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639770863511)

3 - Para gerar o PPP dos funcionários que já estão com a situação D - Demitidos, deve marcar o parâmetro **'Exibir demitidos'** antes de selecionar o funcionário desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639770865815)

4 - Selecione o Funcionário e o Representante Legal da Empresa, e avance.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639752705175)

5 - Deve selecionar a opção de Profissiografia que deve ser gerada no relatório, avançar e executar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639770885271)

Obs: Ao clicar para incluir o funcionário e no momento que ir em Executar o relatório, as seguintes mensagens de alerta são exibidas na visão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639770888855)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639752714391)

Isso ocorre devido a entrada do PPP Eletrônico que se deu em 01/01/2023. A partir desta data, o PPP gerado no RM não gerará mais informações relacionadas ao funcionário que sejam iguais ou posteriores a esta data. Dessa forma, o PPP gerará informações referentes ao período do funcionário na empresa até 31/12/2022.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639770894615)

É recomendado que sempre utilizem as estruturas mais recentes para geração correta do PPP. Dessa maneira, siga as orientações a seguir para realizar essa importação.

A estrutura do relatório estará disponível no book de relatórios. Acesse o RM | Guia Gestão | TOTVS Compartilhamento e procure pela estrutura **RHUREL0004 - PPP**. Baixe a estrutura e salve no disco para importá-la em seguida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639770897431)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639770899863)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639752732951)

Antes da importação, é necessário que seja feita a exclusão do relatório disponível na base de dados através do Gestão | RM Reports.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26639752736279)

Segue orientações sobre a importação através da documentação abaixo:

[RH - RM - SMT - Importação de relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409650455703)

**Saiba mais**Para maiores informações sobre o relatório e validação dos campos, acesse:

- [PPP – Perfil Profissiográfico Previdenciário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719230)

- [PPP - Conferência de Dados Impressos](http://tdn.totvs.com/pages/releaseview.action?pageId=4812932)

Para informações sobre legislação do PPP, acesse o link:

- [INSS - Formulários](https://www.gov.br/inss/pt-br/centrais-de-conteudo/formularios)
