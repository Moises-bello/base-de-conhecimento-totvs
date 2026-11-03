---
article_id: 360016815811
category: RH - Leitura e Apontamento
content_hash: 902c9f2922e582e5eb285d6c8593794e548d97c8e3d03f661a17c740d2d64a1c
fetched_at: '2026-06-28T22:44:45.936090+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: RH - Linha Protheus - PON - Descrição e funcionalidade dos principais campos
  da tabela SP8
type: support-article
updated_at: '2025-10-03T18:37:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016815811-RH-Linha-Protheus-PON-Descri%C3%A7%C3%A3o-e-funcionalidade-dos-principais-campos-da-tabela-SP8
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32616449141911) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Quais são as descrição e funcionalidade dos principais campos da tabela SP8?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Segue abaixo um detalhamento sobre os principais campos da tabela SP8:  
**- P8\_FILIAL:** indica a Filial do funcionário;  
- **P8\_MAT:** indica a matrícula do funcionário;  
**- P8\_DATA:** indica a data em que a marcação foi realizada;  
**- P8\_HORA:** indica o horário em que a marcação foi realizada;  
**- P8\_CC:** indica o Centro de Custo do funcionário;  
**- P8\_ORDEM:** indica a ordem da marcação. Cada dia do período possui uma ordem, por exemplo:  Período de 01 à 31.10.2023. Todas as marcações efetuadas no dia 01, são de ordem 01. As marcações efetuadas no dia 02, são de ordem 02 e assim sucessivamente. Já, as marcações de turnos noturnos, onde o funcionário inicia sua jornada de trabalho em um dia e finaliza no outro, deverão estar com a ordem de acordo com a data de entrada, por exemplo: entrada no dia 01 e saída no dia 02.10. Todas as marcações desta jornada terão ordem 01;  
**- P8\_FLAG:** indica qual a origem da marcação de Ponto, podendo ser: **E** - eletrônica/original, **A** - automática que foi gerada através da rotina de Leitura/Apontamento, **I** - incluída manualmente, **G** - gerada pela rotina Geração Marcações ou **P** - vinda do App MEU RH;  
**- P8\_APONTA:** indica se a marcação foi ou não apontada. **N** significa que não foi apontada e **S** significa que foi apontada;  
**- P8\_TURNO:** indica o Turno de Trabalho vinculado ao funcionário no dia em que a marcação foi efetuada;  
**- P8\_RELOGIO:** indica de qual REP cadastrado no Protheus a batida veio;  
**- P8\_TPMARCA:** indica a classificação da marcação, ou seja, se ela é uma 1E (1ª entrada), 1S (1ª saída) e assim sucessivamente;  
**- P8\_PAPONTA:** indica qual período de apontamento a marcação pertence;  
**- P8\_DATAAPO:** indica qual a data utilizada para o apontamento da marcação, que pode ser a data de entrada ou de saída nos casos onde o Turno é noturno. Para mais detalhes [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406011766423-RH-Linha-Protheus-PON-Qual-a-funcionalidade-do-campo-Considera-Marca%C3%A7%C3%A3o-da-Regra-de-Apontamento)  
- **P8\_SEMANA**: corresponde a Sequência do Turno de Trabalho. Por exemplo: um Turno pode possuir 7 Sequências;  
(semanas) para atender uma escala de trabalho, onde a cada semana a folga ocorre em um dia diferente. Nesse caso, a primeira semana poderia ter o Domingo como o dia de folga, a segunda semana poderia ter a Segunda-Feira como o dia de folga e etc;  
- **P8\_NUMREP**: indica o número informado no campo REP do cadastro do Relógio no Protheus;  
- **P8\_TPMCREP**: apresenta a situação da marcação, onde: em branco significa que a marcação está ativa/apontada, **D** significa que a marcação foi desconsiderada e **E** significa que a marcação foi excluída manualmente pelo usuário;  
- **P8\_TIPOREG**: indica o tipo de registro, onde: **O** para registro eletrônico ORIGINAL, **I** para registro INCLUÍDO manualmente e **P** para intervalo PRÉ-ASSINALADO;  
- **P8\_MOTIVRG**: indica o motivo da inclusão, exclusão, desconsideração ou manutenção da marcação;  
- **P8\_EMPORG**: corresponde ao código da Empresa onde a marcação foi registrada;  
- **P8\_FILORG**: corresponde ao código da Filial onde a marcação foi registrada;  
- **P8\_MATORG**: corresponde ao código da matrícula do funcionário;  
- **P8\_DHORG**: corresponde a combinação do ano, mês, dia, minuto e hora da marcação;  
- **P8\_IDORG**: corresponde ao NSR da marcação eletrônica/original;  
- **P8\_DATAALT**: indica a data em que foi feita a leitura ou manutenção da marcação;  
- **P8\_HORAALT**: indica o horário em que foi feita a leitura ou manutenção da marcação;  
- **P8\_USUARIO**: indica o usuário autor da leitura, inclusão ou alteração do registro.  
  
**Importante**: Cabe ressaltar que todos os campos citados são de uso também da tabela **SPG** - Acumulado de Marcações.  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
