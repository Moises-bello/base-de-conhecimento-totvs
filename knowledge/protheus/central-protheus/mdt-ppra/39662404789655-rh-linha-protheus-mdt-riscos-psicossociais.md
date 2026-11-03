---
article_id: 39662404789655
category: MDT - PPRA
content_hash: af14e18f377b65945da4e7d4a209c8de304de72d8cb86e66d391dcbe93d4b228
fetched_at: '2026-06-28T22:44:27.537413+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Riscos psicossociais
type: support-article
updated_at: '2026-05-06T12:07:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39662404789655-RH-Linha-Protheus-MDT-Riscos-psicossociais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39662371856151) Tempo aproximado para leitura: **02:30:00 min**  
  
**Dúvida**  
Como serão abordados os riscos psicossociais no módulo de Medicina e Segurança do Trabalho?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões

**Solução**  
As informações disponibilizadas na NR-1 sobre riscos psicossociais são básicas. Dessa forma, a equipe de produto realizou apenas o ajuste de incluir a opção de riscos psicossociais na rotina de agentes, no campo “Grupo”.  
   
Segue outras informações liberadas pela equipe de desenvolvimento:  
A atualização da NR-01 passou a exigir que os riscos psicossociais também sejam considerados no processo de Gerenciamento de Riscos Ocupacionais (GRO) e, consequentemente, no PGR. No entanto, a norma não criou novos controles específicos em sistemas nem exigências adicionais de funcionalidades.  
   
Controle de treinamentos  
A NR-01 não estabeleceu regras específicas para controle de treinamentos ou reciclagens relacionadas a riscos psicossociais. A norma apenas mantém a obrigação geral de capacitação dos trabalhadores sobre os riscos existentes em suas atividades. Caso o PGR identifique riscos psicossociais, a empresa pode definir medidas de controle, que podem incluir treinamentos, programas de prevenção ao assédio ou ações relacionadas à organização do trabalho. Essas medidas podem ser registradas no cadastro do risco e acompanhadas por meio de planos de ação.  
   
Gestão de riscos  
A norma não determina que a gestão de riscos seja obrigatoriamente estruturada por função. A empresa pode organizar a identificação e avaliação dos riscos conforme sua realidade operacional, podendo utilizar critérios como função, tarefa, setor ou ambiente de trabalho. No sistema, esses critérios podem ser utilizados no cadastro de riscos conforme a forma de avaliação adotada pela empresa. Caso um risco afetar todas as funções, por exemplo, o campo função deve ser preenchido com asterisco.  
   
Inventário de riscos  
O inventário de riscos é o registro onde são documentados os perigos identificados, os riscos ocupacionais, a avaliação realizada, os trabalhadores expostos e as medidas de prevenção existentes. No sistema, essas informações são registradas principalmente nas rotinas de agentes e riscos disponíveis no submenu PPRA.  
   
Plano de ação  
O plano de ação é utilizado para organizar e acompanhar a implementação das medidas de controle definidas no PGR, podendo incluir responsáveis, prazos e acompanhamento das ações. Caso riscos psicossociais sejam identificados, as medidas definidas para tratá-los podem ser acompanhadas por meio dessa mesma rotina.  
   
Controle de EPI  
A atualização da NR-01 não trouxe alterações no controle de EPI. Esse tema continua sendo tratado principalmente pela NR-06. No contexto do GRO, o EPI pode ser definido como medida de controle para determinados riscos, porém riscos psicossociais normalmente são tratados por medidas organizacionais ou administrativas, e não por EPI.  
   
Relatórios e auditorias  
A NR-01 não criou novos relatórios obrigatórios relacionados a riscos psicossociais. Em auditorias ou fiscalizações, a empresa deve apresentar os registros da gestão de riscos, como inventário de riscos, medidas de controle e acompanhamento das ações do PGR.  
   
Indicadores e alertas  
A norma não exige indicadores ou alertas automáticos em sistemas para acompanhamento de riscos psicossociais. Indicadores como absenteísmo, horas extras, afastamentos por saúde mental ou turnover podem ser utilizados pela empresa como ferramentas de gestão, mas não constituem exigência normativa.  
   
Relatórios gerenciais  
Relatórios gerenciais podem ser utilizados como apoio à análise das informações registradas no processo de gestão de riscos, porém a NR-01 não determina modelos ou relatórios específicos voltados exclusivamente para riscos psicossociais.  
   
Governança e confidencialidade de dados  
Questões relacionadas à proteção e confidencialidade de dados sensíveis estão associadas principalmente à Lei Geral de Proteção de Dados (LGPD). A NR-01 não estabelece requisitos específicos de governança de dados em sistemas.  
   
Mapeamento de riscos  
Atualmente, o módulo não possui um conjunto de rotinas específicas voltadas ao apoio direto no mapeamento de riscos por meio de indicadores gerenciais, como por exemplo o turnover citado. Esse tipo de indicador depende de informações do módulo SIGAGPE, não sendo nativamente tratado pelo SIGAMDT. A criação de funcionalidades para apoiar o mapeamento de riscos, de forma geral e não apenas para riscos psicossociais, está em discussão interna. Caso haja interesse, pode ser aberta uma solicitação de melhoria via Central Colaborativa, detalhando as necessidades para avaliação e possível engajamento de outros clientes.  
   
Auditorias  
A questão de auditoria não é específica de um módulo, sendo tratada por configurações gerais do Protheus. Para mais detalhes sobre esse tema, é necessário acionar o atendimento responsável.  
   
Mais informações sobre as rotinas de gestão de riscos podem ser consultadas nas documentações:  
<https://tdn.totvs.com/x/ogOIF> (Submenu PPRA)  
<https://tdn.totvs.com/x/IUi2Fg> (Riscos)  
<https://tdn.totvs.com/x/8IlEFQ> (EPI)  
<https://tdn.totvs.com/x/6NybFg> (Laudos)  
<https://tdn.totvs.com/x/__N5IQ> (Relatórios de atendimento médico)

Quanto ao evento S-2240, não houve, até o momento, alteração no layout do eSocial que contemple uma tag específica ou um agente exclusivo para riscos psicossociais. Dessa forma, entende-se que o processo de envio do evento permanece o mesmo já adotado atualmente.  
   
Assim, ao vincular o tipo psicossocial ao agente e, posteriormente, relacionar esse agente ao risco, o eSocial irá considerar o código do agente e as configurações associadas, como tipo de avaliação, intensidade e medidas de proteção. Isso ocorre porque não existem, no XML, tags específicas para tratar exclusivamente o tipo de risco psicossocial.  
   
Vale reforçar que as tags do XML são padronizadas e definidas pelo próprio eSocial, não sendo possível realizar parametrizações diferentes desse modelo.  
   
Dessa forma, neste momento, o tratamento dos riscos psicossociais está mais voltado ao controle e à gestão interna da empresa, inclusive para fins de auditoria. Para isso, podem ser utilizadas as rotinas já mencionadas na documentação encaminhada anteriormente.

Saiba mais  
[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
