---
article_id: 360004196091
category: RH - Ponto Eletrônico
content_hash: a5db36592feb6cb423570c8d9c0aa1a674efd354716073a8a264249958e613a4
fetched_at: '2026-06-28T22:44:58.293444+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar um abono de horas no ponto
type: support-article
updated_at: '2025-02-18T14:42:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004196091-RH-Linha-Protheus-PON-Como-efetuar-um-abono-de-horas-no-ponto
---

**Dúvida**Como efetuar um abono de horas no ponto?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**A princípio, qualquer evento apontado poderá ser abonado, inclusive horas extras, para isso, é necessário que exista cadastro de Motivos de Abono.  
  
O sistema permite que as horas dos eventos sejam ou não abonadas e se as horas serão consideradas no cálculo do desconto de DSR - Descanso Semanal Remunerado.  
  
O **abono** pode ser **lançado** através de duas **rotinas**:  
  
**1 -** Integrados  
**2 -** Apontamentos  
  
Os parâmetros MV\_ABOSEVE e MV\_SUBABAP devem estar com conteúdo S.  
  
**MV\_ABOSEVE:** Deduz Horas Abonadas das Horas Apontadas sem a necessidade de associar um motivo a um evento. Onde **S** - Deduz e **N** - Não Deduz (Valor Padrão)   
**MV\_SUBABAP**: Gerar Hrs de Abono no Evento Relacionado subtraindo-as das Horas Calculadas quando Motivo Nao Abona Horas e possui Evento. **S=Sim** ; **N=Nao**  
  
Alguns **exemplos** de como o sistema pode trabalhar com a utilização dos Motivos de Abono:  
  
**1.** Para abonar a falta e não ocorrer desconto em folha ou banco de horas, siga os passos abaixo:  
- o campo Abona Horas e Abona DSR como SIM e o Cod. Evento em branco  
  
**2.** Para abonar uma falta e trocar o evento para que ocorra desconto em Folha (exemplo: foi gerado o evento 009 que levará a falta para BH, porém, é necessário que em determinado dia a falta seja descontada em Folha, neste caso, existe a necessidade de que ocorra uma troca de eventos), siga os passos abaixo:  
- o campo Abona Horas como NÃO e no Cod. Evento informar um código de evento diferente do que já foi gerado no apontamento. Neste evento, deve existir uma verba de folha atrelada para que ocorra o desconto em Folha  
- se não quiser que ocorra o desconto de DSR, o campo Abona DSR deverá estar como SIM, caso contrário deixe como NÃO  
  
**Saiba Mais**  
Manual do ponto eletrônico: <https://tdn.totvs.com/pages/releaseview.action?pageId=630823373>
