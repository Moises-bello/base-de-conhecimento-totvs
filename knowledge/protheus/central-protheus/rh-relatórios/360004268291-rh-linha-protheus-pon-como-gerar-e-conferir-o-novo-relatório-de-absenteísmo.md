---
article_id: 360004268291
category: RH - Relatórios
content_hash: 42ead3d02e322a66b69e3c063a8b9320812634a17f0d07f8d4f1e783fbf04f51
fetched_at: '2026-06-28T22:44:43.471981+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar e conferir o novo Relatório de Absenteísmo
type: support-article
updated_at: '2025-12-04T17:07:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004268291-RH-Linha-Protheus-PON-Como-gerar-e-conferir-o-novo-Relat%C3%B3rio-de-Absente%C3%ADsmo
---

**Dúvida**Como gerar e conferir o novo Relatório de Absenteísmo - PONR210  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir do release 12.1.33  
  
**Solução**O **relatório de absenteísmo foi reescrito** utilizando a **classe tReport**, que possibilita a geração em planilha no formato tabela e oferece diversas opções de customização.  
Além da opção de gerar o relatório em planilha, foram implementadas outras melhorias:  
**1.**Informações detalhadas sobre os Afastamentos ocorridos no período;  
**2.** Opção de considerar ou não as Férias nos Afastamentos;  
**3.** Novo grupo de perguntas, com perguntas do tipo Range, oferecendo maior flexibilidade ao preencher os filtros para o relatório;  
**4.** Opção para gerar o relatório com horas em Sexagesimal ou Centesimal.  
**5.** A informação de **Horas Extras** **foi retirada** para que o relatório contemple somente os **eventos de desconto.**  
  
O relatório de **Absenteísmo** pode ser utilizado para conferência de **eventos de desconto, abonos e afastamentos**, através de percentuais. Este relatório também gera o comparativo das **horas previstas** para serem trabalhadas durante o intervalo de datas selecionadas e **quanto efetivamente foi feito**. A impressão pode ser feita de **qualquer período**, seja ele aberto ou fechado, além disso, não é necessário que o intervalo de datas seja exatamente igual ao dos períodos de apontamento utilizados, ele pode ser impresso para períodos de três meses, por exemplo.  
É importante apenas ressaltar que nos casos onde o período de apontamento ainda está aberto, recomendamos que a data base do sistema esteja no último dia do período.  
  
Os cadastros/rotinas utilizadas para a consolidação das informações deste relatório são:  
**1 -** Regra de Apontamento  
**2 -** Turno de Trabalho  
**3 -** Tabela de Horário Padrão  
**4** - Eventos  
**5 -** Motivos de Abono  
**6 -** Troca de Turno  
**7 -** Afastamentos  
  
É necessário que os eventos tenham sido apontados para o intervalo de datas a ser impresso do relatório.  
  
Para gerar o relatório, deve ser acessado o menu em **Relatórios -> Diversos -> Absenteísmo,** os parâmetros serão exibidos conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18949355904919)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18949355915031)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18949351286039)  
  
  
O relatório será impresso dessa forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18949355931927)  
  
  
Com esta nova versão do Relatório, é possível fazer a impressão em Excel:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19041332479895)  
  
 **Funcionamento do relatório:**- O sistema calcula as **Horas Previstas** para o funcionário com base no calendário do ponto gerado para o funcionário, já considerando trocas de turno ou exceções cadastradas. Para os dias em que o funcionário estiver afastado, o sistema seguirá a definição da pergunta **Afast. Como H. Prevista?, que** caso esteja com Sim, as horas de afastamento serão incluídas nas horas previstas, e o percentual de Horas de Afastamento só será calculado quando essa pergunta estiver com Sim;  
- Para as **Horas Não Trabalhadas** o sistema irá buscar os eventos de Desconto gerados nos apontamentos do funcionário, dentro das tabelas SPC e SPH;  
- As **Horas Realizadas** serão a diferença entre as Horas Previstas - Horas Não Trabalhadas.

**Observação:***Para que o relatório consiga calcular as **horas previstas** é necessário que o turno do funcionário possua horários cadastrados na tabela de horário padrão **(SPJ).** Sem o cadastro da tabela de horário padrão o relatorio não conseguirá definir dias e horários que o funcionário deveria trabalhar e consequentemente realizar o cálculo das horas previstas.*  
**Percentuais:**O relatório apresenta diversas colunas com o percentual correspondente do total das horas, por exemplo, o percentual de Horas Realizadas é calculado com base nas Horas Previstas, já o percentual de Horas Abonadas tem como base as Horas Não Realizadas.  
Obs.: Os percentuais sempre são calculados com as horas em Centesimal.

**% Horas Realizadas =**  Horas Realizadas / Horas Previstas  
**% Horas Não Trabalhadas =** Horas Não Trabalhadas / Horas Previstas  
**% Horas Abonadas =** Horas Abonadas / Horas Não Trabalhadas  
**% Horas de Afastamento =** Horas Afastamento / Horas Previstas (Quando pergunta Afast. Como H. Prevista? = Sim)

No detalhamento, onde são mostrados os eventos, abonos e afastamentos, temos:

**% Horas =** Horas / Horas Não Trabalhadas  
**% Hrs. Abonadas =** Hrs. Abonadas (Detalhamento) / Horas Abonadas (Período)  
**% Hrs. Afast. =** Hrs. Afast.  (Detalhamento) / Horas Afastamento (Período)

**Pergunta Férias como Afastamento?**A pergunta **Férias como Afast.?** define se o sistema irá considerar as Férias no relatório, demonstrando as horas de Férias nas Horas de Afastamento

**Exemplos:**Pergunta **Férias como Afast.? = Sim** e **Afast. Como H. Prevista? = Sim**

As horas de Férias são apresentadas no relatório como Afastamento e são incluídas no total de Horas Previstas:  
  
![Relatório de Absenteísmo considerando as férias do funcionário](https://tdn.totvs.com/download/attachments/781854828/image2023-8-28_10-23-55.png?version=1&modificationDate=1693229035330&api=v2&effects=drop-shadow)

Pergunta**Férias como Afast.? = Não** e **Afast. Como H. Prevista? = Sim**

As Férias não são demonstradas e não são incluídas nas Horas Previstas:

![Relatório de Absenteísmo sem as férias do funcionário](https://tdn.totvs.com/download/attachments/781854828/image2023-8-28_10-27-35.png?version=1&modificationDate=1693229255853&api=v2&effects=drop-shadow)  
  
  
**Importante:**Para utilizar o novo Relatório de Absenteísmo é necessário aplicar o pacote de atualização da Expedição Contínua do RH, com data 11/09/2023 ou superior, e executar o UPDDISTR com o arquivo diferencial.  
  
Após atualizar o sistema com o pacote de atualização e criar o novo grupo de perguntas executando o UPDDISTR, ao acessar o menu do relatório de Absenteísmo o sistema passará a abrir a nova rotina PONR210, não sendo necessário realizar alterações no Menu.  
Caso o **rdmake ABSENT** esteja compilado no ambiente, o sistema irá priorizar o RDMake, sendo necessário neste caso a inclusão da nova rotina no menu, ou a exclusão do RDMake do repositório do ambiente para utilização da rotina PONR210.  
  
O layout do rdmake ABSENT é bastante parecido com o novo relatório, porém, as informações de Afastamento não são exibidas e não é possível a impressão em outros formatos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19059813255191)  
  
**Saiba Mais:**[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=781854828)[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
