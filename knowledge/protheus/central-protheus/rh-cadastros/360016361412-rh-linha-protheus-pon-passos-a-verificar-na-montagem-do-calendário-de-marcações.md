---
article_id: 360016361412
category: RH - Cadastros
content_hash: 49f32c54e85b62621180e9ff8a59fbdf1e3ccb2b6828aa00132cde6a7d960ad6
fetched_at: '2026-06-28T22:44:53.063012+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Passos a verificar na montagem do calendário de
  marcações
type: support-article
updated_at: '2026-04-23T16:35:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361412-RH-Linha-Protheus-PON-Passos-a-verificar-na-montagem-do-calend%C3%A1rio-de-marca%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35295789398551) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Quais são os passos a serem verificados na montagem do calendário de marcações?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para que as marcações sejam alocadas com os posicionamentos e dias corretos e que seus apontamentos sejam calculados corretamente, se tem por necessário as seguintes validações:  
  
**1.** Na [Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o), todos os campos devem estar preenchidos, mesmo quando o dia não é trabalhado. Isso auxiliará o sistema na montagem do calendário e dos apontamentos na semana.  
Cuidado no preenchimento do **Limite Inferior e Superior**. [Existem regras específicas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002754861-RH-Linha-Protheus-PON-Funcionalidades-dos-campos-de-Limite-inferior-e-Limite-superior-na-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o), e o preenchimento do campo afeta a alocação das batidas.  
![86.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519191)  
  
**2.** A [Troca de Turno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015528671-RH-Linha-Protheus-PON-Como-funciona-a-Troca-de-Turno-dos-funcion%C3%A1rios) do funcionário é importante para a [montagem do calendário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016361412-RH-Linha-Protheus-PON-Passos-a-verificar-quanto-a-montagem-do-calend%C3%A1rio-de-marca%C3%A7%C3%B5es). No momento do **fechamento mensal**, sempre é gravado uma troca de turno aos funcionários, este procedimento realiza a montagem do calendário do período de apontamento.   
Funcionários admitidos terá que lançar a troca de turno da data de admissão, para as próximas trocas ao realizar o fechamento mensal, o sistema criará a troca de turno do primeiro dia subsequente ao aberto.   
  
**Importante**: na troca de turno, verifique o cadastro **De - Para**, tanto do turno quanto da regra. O **Turno De**, em uma linha, deve ser igual ao **Turno Para** da linha anterior. Isso se aplica na **regra** também:  
![87.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519971)  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[Portaria 1510/2009](https://www.trt2.jus.br/geral/tribunal2/ORGAOS/MTE/Portaria/anexo_Portaria_1510_MTE.pdf)
