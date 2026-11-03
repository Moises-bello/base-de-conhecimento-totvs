---
article_id: 360052347934
category: Chão de Fábrica (SIGASFC)
content_hash: 8d88315bc8ed233fff2a1ad7f2d7692f9ffcb249de0d01aaea0301ffa6051753
fetched_at: '2026-06-28T22:42:49.859237+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Horas no apontamento do Chão de Fábrica
type: support-article
updated_at: '2022-04-01T13:11:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052347934-Manufatura-Linha-Protheus-SIGASFC-Horas-no-apontamento-do-Ch%C3%A3o-de-F%C3%A1brica
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:43 min**  
**Dúvida**Por que quando é efetuado o apontamento no módulo de **Chão de Fábrica** e incluído mais de um operador ele não está multiplicando a quantidade de horas consumidas nesse apontamento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12   
  
**Solução**O tempo de operador é correspondente ao tempo de operação da máquina, ou seja, a máquina só ficou ocupada por um período, mesmo que sejam alocados dois operadores.  
O custo que é encaminhado para o **SIGAPCP - Planejamento e Controle da Produção** é o **GGF -****Gastos Gerais de Fabricação**. Quando o **GGF** é padrão, não é possível alterá-lo e vai exatamente o tempo de operação, caso o **GGF** seja real é possível alterar o **GGF**, e é isso que gera o movimento do **MOD -****Mão de obra** no **SIGAPCP** .  
Para que seja possível apontar esse **GGF**pelo real antes de criar a ordem, é necessário verificar o campo **Transf.MOD - F5\_TRANMOD** no tipo de movimento configurado no parâmetro **MV\_TMPAD - Tipo de movimentação padrão para produção PCP**. Quando o parâmetro estiver como **S** **- Sim** o **GGF** é padrão, quando **N** **- Não** o **GGF** é real.  
  
**Importante**  
Lembrando que a alteração do campo **Transf.MOD** não vale para ordens já criadas, pois essa informação somente é atualizada na criação da ordem de produção.
