---
article_id: 360016327011
category: RH - Lançamentos
content_hash: e9bf32e1849b78fda08689bca9d65680ebe935023032c7120059abf3c0007665
fetched_at: '2026-06-28T22:44:46.910874+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Funcionalidade do parâmetro MV_APHEDTM para apontamento
  de Horas Extras
type: support-article
updated_at: '2025-06-05T11:22:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016327011-RH-Linha-Protheus-PON-Funcionalidade-do-par%C3%A2metro-MV-APHEDTM-para-apontamento-de-Horas-Extras
---

**Dúvida**  
Funcionalidade do parâmetro **MV\_APHEDTM** para apontamento de Horas Extras.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O parâmetro que pode ser encontrado em **Configurador(SIGACFG), acessando Ambiente - Cadastros - Parâmetros, filtre MV\_APHEDTM,** ele com conteúdo **S** tem a finalidade de **calcular as Horas Extras** de acordo com o **tipo do dia**, ou seja, ele terá funcionalidade em jornadas noturnas onde existem marcações iniciadas em um dia e finalizadas em outro.  
Para funcionar corretamente, o **cadastro** de **Tipos de Horas Extras** deve estar devidamente **criado** com cada um dos **tipos de Horas Extras e eventos diferentes para cada tipo**.  
  
  
**Configurações**:  
**MV\_APHEDTM = S**  
![](https://tdn.totvs.com/download/attachments/630574629/image2021-7-21_15-34-9.png?version=1&modificationDate=1626892449263&api=v2)  
  
  
**Tabela de Horário Padrão** para todos os dias: 15:00 - 19:00 - 20:00 - 23:00 (Sábado Compensado e o Domingo DSR):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986619374359)  
  
  
**1. Início e término da jornada em dias trabalhados:  
Acesse em Atualizações-Lançamentos-Integrados, filtre o funcionário e entre como alterar.**Como o tipo da hora extra não muda de um dia para o outro o sistema gera apenas um evento com o total das horas extras realizadas.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986619392535) **2. Início da jornada em dia trabalhado e término em dia não trabalhado**Neste caso, o funcionário começou a jornada em uma Sexta-feira, um dia trabalhado, mas terminou no Sábado, dia compensado segundo a tabela de horário  
Com isso o sistema gerou uma hora extra noturna na sexta (23:00 - 00:00) e duas horas extras compensada noturna no Sábado (00:00 - 02:00):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986619408023)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986645742359)  
  
  
**3. Início e término da jornada em dias não trabalhados**Neste cenário, o funcionário trabalhou em um sábado, dia compensado, e terminou a jornada em um domingo, DSR. Com isso, o sistema gerou duas horas extras compensadas noturna no Sábado (22:00 - 00:00) e três horas extras DSR noturna no Domingo (00:00 - 03:00)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986619439127)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986619456279)  
 **4 - Prorrogação do horário noturno**Quando o parâmetro **MV\_APHEDTM** estiver habilitado ( Conteúdo = S ), **o horário noturno será prorrogado de acordo com a definição na regra de apontamento.** Com isso o sistema gerou uma hora extra noturna na Sexta (23:00 - 00:00) e Seis horas extras compensada noturna no Sábado (00:00 - 05:00):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986619469335)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986619479831)  
  
  
**MV\_APHEDTM = N**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986645816343)  
  
  
As Horas Extras são geradas no dia Compensado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20986653059735)

**Saiba Mais:**[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=630574629)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
