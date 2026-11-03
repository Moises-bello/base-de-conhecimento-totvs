---
article_id: 8372551530775
category: MDT - Atendimento Médico
content_hash: 4ae1d0375cffb62863881b1cca21e331af1d55a67d3dcbbc428591da6c26eec5
fetched_at: '2026-06-28T22:44:21.529836+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Quais parâmetros podem ser consultados na utilização
  da rotina Ficha Médica Modelo 2 ou Prontuário Médico rotina MDTA410
type: support-article
updated_at: '2025-07-25T20:00:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8372551530775-RH-Linha-Protheus-MDT-Quais-par%C3%A2metros-podem-ser-consultados-na-utiliza%C3%A7%C3%A3o-da-rotina-Ficha-M%C3%A9dica-Modelo-2-ou-Prontu%C3%A1rio-M%C3%A9dico-rotina-MDTA410
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25286829400343)**Tempo aproximado para leitura: **00:02:00** min **Dúvida**Quais parâmetros podem ser consultados na utilização da rotina Ficha Médica Modelo 2 ou Prontuário Médico rotina MDTA410?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Cada empresa pode ter um cenário específico, portanto é importante avaliar os parâmetros abaixo:  
**MV\_ESTNEG** - Identifica se o sistema permitira que os saldos em estoque dos produtos fique negativo através de movimentação. conteúdo deve ser **(S) Sim ou (N) Não**.   
**MV\_LOCALIZ** - Indica se produtos poderão usar controle de localização física ou não. **(S) Sim ou (N) Não**.   
**MV\_MDTEPID** - Indica se solicita confirmação de exclusão de Epi entregue ao funcionário. **(S) Sim ou (N) Não.**  
**MV\_MDTPEPI** - Tipo que define se um produto de EPI. Esse tipo deve estar definido na tabela genérica 02.   
**MV\_MDTPS** - Indica se o cliente e um prestador de serviço de medicina. **(S) Sim ou (N) Não**  
**MV\_NG2ATM0** - Confirmação de alteração da Ficha Médica. 1 = Bloqueia, 2 = Questiona e 3 = Permite   
**MV\_NG2BIOM** - Indica se utiliza Biometria na Entrega de EPI. 1=Sim ou 2=Não.   
**MV\_NG2D685** - Indica a quantidade mínima de dias de afastamento suficiente para gerar automaticamente um exame(NR7)de retorno do trabalho.   
**MV\_NG2EPDU** - Indica se emite alerta de Epi vencido no cadastro funcionário x Epi (MDTA695). 0=Não, 1=Somente Epi c/ devolução, 2=Somente Epi s/ devolução, 3=Todos.  
**MV\_NG2ESTN** - Indica se o sistema ira trabalhar com estoque de medicamentos negativo. **(S) Sim ou (N) Não**  
**MV\_NG2SA** - Indica se gera solicitação ao armazém ao invés de baixar do estoque. **(S) Sim ou (N) Não**  
**MV\_NGEXREL** - Indica quais exames devem estar habilitados na inclusão de Atestado(ASO). 1=Apenas exames já realizados, 2=Todos os exames previstos.   
**MV\_NGFORPD** - Define o código do fornecedor padrão para ser utilizado na entrega de Epis da rotina de Funcionário x Epi. Informar codigo+loja.Ex:0000010   
**MV\_NGMDTAF** - Indica se o funcionário devera ser afastado do trabalho após o Atestado Medico **(S) Sim ou (N) Não**  
**MV\_NGMDTES** - integração do SIGAMDT com o Estoque Informar **(S) Sim ou (N) Não**  
**MV\_RASTRO** - Determina a utilização ou não da Rastreabilidade dos Lotes de produção (Informar **(S) Sim ou (N) Não**).

**Saiba Mais**  
[Artigos MDT eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
