---
article_id: 27441261453719
category: RH - Ambiente
content_hash: 0aedf26af311343d5fe2c911b7ff305063cab4a7b05ff77f6867de335a4cf811
fetched_at: '2026-06-28T22:44:55.991349+00:00'
product: protheus
section_id: 32302375681815
source: central-protheus
title: RH - Linha Protheus - PON - Lentidão no módulo de Ponto Eletrônico
type: support-article
updated_at: '2025-06-04T20:03:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27441261453719-RH-Linha-Protheus-PON-Lentid%C3%A3o-no-m%C3%B3dulo-de-Ponto-Eletr%C3%B4nico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27441294257175) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O que avaliar em casos de **lentidão** no módulo de Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Nos casos de **baixa *performance*** do módulo de Ponto Eletrônico, devem ser avaliados os tópicos abaixo de acordo com a rotina que está sendo impactada:  
  
**> Leitura/Apontamento**  
**-** avaliar o uso de ***multi threads*** através do parâmetro [MV\_PONMULT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050594293-RH-Linha-Protheus-PON-Uso-de-Multithreads-na-Leitura-Apontamento-das-marca%C3%A7%C3%B5es)  
**-** verificar se os **períodos anteriores** ao que está sendo lido já **foram fechados**, pois quanto maior o volume de dados nas tabelas de períodos em aberto (SP8, SPC, RFE e etc), menor a performance da rotina  
  
**> Fechamento Mensal**  
**-** avaliar se na rotina de **[Período de Apontamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290?source=search)** existem registros com bolinha de cor verde. Em caso positivo, significa que são linhas que o usuário criou manualmente, portanto, não se tratam de períodos efetivamente fechados, e podem impactar no processo de fechamento. Neste caso, é necessário avaliar os registros e excluí-los  
**-** verificar se os **períodos anteriores** ao que está sendo fechado já **foram finalizados**, pois quanto maior o volume de dados nas tabelas de períodos em aberto (SP8, SPC, RFE e etc), menor a performance da rotina  
  
Além das rotinas citadas, existem **integrações** com o módulo de Ponto Eletrônico que podem ter altas movimentações de dados, que são:  
**- Integração com [Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779731236119-RH-Linha-Protheus-PON-x-Suricato-Integra%C3%A7%C3%A3o-Protheus-x-Suricato)**  
**- Integração com [Carol Clock In](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083914-RH-Linha-Protheus-PON-Par%C3%A2metros-que-envolvem-a-integra%C3%A7%C3%A3o-entre-Carol-x-Ponto-Eletr%C3%B4nico)**  
**- Integração com [Gestão de Serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047548914-MP-TEC-MV-TECXRH)**  
  
Caso utilize alguma dessas integrações e note qualquer queda de *performance* em outras rotinas que **não** as citadas anteriormente, orientamos que entre em contato com o time de Suporte tendo em mãos **arquivos** para **análise de lentidão**, como **[Log Profile e DBTrace](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028124111-RH-Linha-Protheus-GPE-Como-gerar-arquivos-para-an%C3%A1lise-de-lentid%C3%A3o-performance).**  
  
**Importante:** caso utilize **Pontos de Entrada**, é indispensável a realização de testes desabilitando as customizações com a chave **[IXBLOG=NORUN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003365722-RH-Linha-Protheus-GPE-Habilitar-a-chave-IXBLOG).**Cabe ressaltar que para análise de *performance*, é levado em consideração tambem a **volumetria de dados da empresa**, ou seja: quantidade de funcionários X quantidade de marcações no período X quantidade de apontamentos no período X quantidade de trocas de turno, e etc.  
  
**Saiba Mais:**  
[RH - Linha Protheus - PON - Uso de Multithreads na Leitura/Apontamento das marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050594293-RH-Linha-Protheus-PON-Uso-de-Multithreads-na-Leitura-Apontamento-das-marca%C3%A7%C3%B5es)  
[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290?source=search)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
