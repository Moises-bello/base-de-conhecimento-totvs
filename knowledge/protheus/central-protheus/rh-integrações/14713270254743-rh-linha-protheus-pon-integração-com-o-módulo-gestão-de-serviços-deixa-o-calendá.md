---
article_id: 14713270254743
category: RH - Integrações
content_hash: 2b35b1b77ecb06186a78dd142c5f98a6cfcb871d35473a31579a44efbbd5f88e
fetched_at: '2026-06-28T22:44:47.567688+00:00'
product: protheus
section_id: 32419269542935
source: central-protheus
title: RH - Linha Protheus - PON - Integração com o módulo Gestão de Serviços deixa
  o calendário no Ponto Eletrônico como Não Trabalhado
type: support-article
updated_at: '2026-02-11T19:53:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14713270254743-RH-Linha-Protheus-PON-Integra%C3%A7%C3%A3o-com-o-m%C3%B3dulo-Gest%C3%A3o-de-Servi%C3%A7os-deixa-o-calend%C3%A1rio-no-Ponto-Eletr%C3%B4nico-como-N%C3%A3o-Trabalhado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38336005832983) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Quando existe **integração** entre os módulos **Gestão de Serviços x Ponto Eletrônico**, ao acessar as rotinas de **manutenção** do **SIGAPON** o **calendário** exibe **todos os dias como Não Trabalhado**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14712757391639)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - A partir do release 12.1.23  
  
**Causa**  
O cenário **ocorre quando**:  
- O parâmetro **MV\_GSPNMTA** está com **conteúdo .T.**  
- Existe **cadastro de Atendente**, mas **não existe alocação do atendente na Mesa Operacional**, ambos cadastros existentes no módulo de **Gestão de Serviços**.  
  
**Solução**  
Para que o **calendário** do módulo de **Ponto Eletrônico** seja **montado corretamente**, será necessário que:  
- O parâmetro **MV\_GSPNMTA** seja definido com conteúdo **.F.**  
**OU**  
- Seja feita **alocação** do **Atendente** na rotina de **Mesa Operacional** dentro do módulo de **Gestão de Serviços.**  
  
O parâmetro **MV\_TECXRH**, também do módulo de **Gestão de Serviços**, serve para **definir** se a **integração** entre os módulos de **Ponto Eletrônico** e **Gestão de Serviços** está **ativa ou não**, além de **enviar** os **dados** de **Cargo**, **Turno e Sequência do Turno** vinculados ao **Cadastro do Funcionário (SRA)**, para o cadastro do **Atendente (AA1),** porém, **uma vez que o MV\_GSPNMTA está ativo**, se **não existir** **alocação** para o **Atendente** na **Mesa Operacional**, será entendido que **não há jornada prevista** no período, portanto, o **calendário** do **Ponto Eletrônico** será **montado** com **todos os dias** do período como **Não Trabalhados.**  
**Importante ressaltar que isso ocorre mesmo se o MV\_TECXRH estiver com conteúdo .F.**  
  
**Saiba Mais:**  
[Parâmetro MV\_GSPNMTA](https://tdn.totvs.com/pages/releaseview.action?pageId=538487778)  
[Parâmetro MV\_TECXRH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047548914-MP-TEC-MV-TECXRH)  
[Módulo Gestão de Serviços - SIGATEC](https://tdn.totvs.com/pages/releaseview.action?pageId=236601804#Terceiriza%C3%A7%C3%A3o(SIGATEC)Protheus12-Par%C3%A2metros/Configura%C3%A7%C3%B5es)
