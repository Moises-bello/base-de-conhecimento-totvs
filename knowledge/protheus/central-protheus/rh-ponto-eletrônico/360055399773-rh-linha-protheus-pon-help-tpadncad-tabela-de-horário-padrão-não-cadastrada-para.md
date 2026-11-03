---
article_id: 360055399773
category: RH - Ponto Eletrônico
content_hash: e3b78b8e05122c9edab4f5c495ce1ebe68ad73c1a906e6f84feeb8394f1ac93e
fetched_at: '2026-06-28T22:44:58.322666+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: 'RH - Linha Protheus - PON - Help: TPADNCAD - Tabela de Horário Padrão não
  cadastrada para o turno corrente'
type: support-article
updated_at: '2025-03-21T19:33:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055399773-RH-Linha-Protheus-PON-Help-TPADNCAD-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-n%C3%A3o-cadastrada-para-o-turno-corrente
---

**Ocorrência**No módulo Ponto Eletrônico, ao acessar as rotinas de Marcações ou Integrados, é exibida a mensagem: Help: TPADNCAD - Tabela de Horário Padrão não cadastrada para o turno corrente.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091751773)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões.  
  
**Causa**O motivo da mensagem ocorre pelos **motivos listados abaixo**:

1. Um novo Turno foi cadastrado, mas não foi adicionada uma Sequência na Tabela de Horário Padrão.
2. Existe uma divergência no compartilhamento entre as tabelas SR6 (Turnos de Trabalho) e SPJ (Tabela de Horário Padrão).
3. Na rotina de Troca de Turno, o funcionário já esteve vinculado ao Turno "X", mas foi removido do sistema, ou houve a exclusão de alguma Sequência de um Turno.
4. Na rotina de Troca de Turno, o funcionário está vinculado a um Turno que utiliza Turno Opcional.
5. Na rotina de Troca de Turno, o último registro apresenta os campos "Turno Para", "Sequência Para" e "Regra Para" em branco.

**Solução**Para **solucionar** essa ocorrência, **valide os passos abaixo**:

1. Acesse a rotina de Tabela de Horário Padrão e verifique se pelo menos uma Sequência está cadastrada para o Turno criado.
2. O compartilhamento entre as tabelas SR6 e SPJ deve ser idêntico, ou seja: CCC, EEE, CEE.
3. Verifique todo o histórico de Troca de Turno do Funcionário e confirme se todos os Turnos/Sequências aos quais ele foi vinculado em algum momento ainda estão cadastrados no sistema.
4. Se o campo "Turno Opcional" estiver sendo utilizado no cadastro de Turnos, valide o seguinte:
   * O parâmetro MV\_TNOOPC deve estar configurado como "S".
   * Caso o Turno Opcional seja diferente do principal, verifique se ele realmente existe no ambiente.
   * Se o Turno Opcional for igual ao principal, deve haver, no mínimo, duas Sequências cadastradas na Tabela de Horário Padrão.
5. Na rotina de Troca de Turno, todos os campos "De/Para" devem estar preenchidos para garantir que os dados sejam corretamente registrados no Cadastro do Funcionário (tabela SRA).

**Saiba Mais:**  
[RH - Linha Protheus - PON - Como cadastrar um Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho?source=search)  
[RH - Linha Protheus - PON - Para que serve o campo de Turno Opcional no cadastro do Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052521873-RH-Linha-Protheus-PON-Para-que-serve-o-campo-de-Turno-Opcional-no-cadastro-do-Turno-de-Trabalho?source=search)
