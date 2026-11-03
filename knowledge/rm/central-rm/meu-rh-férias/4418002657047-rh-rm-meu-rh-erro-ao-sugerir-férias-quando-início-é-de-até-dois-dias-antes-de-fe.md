---
article_id: 4418002657047
category: Meu RH - Férias
content_hash: 9b9016be2b4d5e0c3f92a2090654e2c21257bcdcd0fa2b1235cd44df1bbd4ef6
fetched_at: '2026-06-28T22:47:31.680755+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Erro ao sugerir Férias quando início é de até dois dias
  antes de feriado, descanso ou dia compensado
type: support-article
updated_at: '2025-09-11T18:16:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418002657047-RH-RM-Meu-RH-Erro-ao-sugerir-F%C3%A9rias-quando-in%C3%ADcio-%C3%A9-de-at%C3%A9-dois-dias-antes-de-feriado-descanso-ou-dia-compensado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22160859712279) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao realizar uma Sugestão de Férias via Meu RH, é retornado o erro: **Início de Férias não pode ser programado para até dois dias antes de feriado, descanso ou dia compensado**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.29  
  
**Causa**Esse incidente ocorre, pois conforme legislação, as férias dos funcionários não podem iniciar em até 2 dias que antecedem um feriado, descanso ou dia compensado.  
  
**Solução  
Cenário de exemplo**, o dia de descanso do funcionário João é Domingo e o dia Compensado é Sábado.  
  
Se sugerir férias, iniciando na Sexta-Feira, realmente vai ser apresentado a mensagem de erro, pois antecede de 2 dias do Domingo **(Descanso)**.  
  
Se sugerir férias, iniciando na Quinta-Feira, também vai apresentar a mensagem pois antecede de 2 dias do Sábado **(Compensado)**, porém pela ambiguidade de entendimento na legislação, é possível **retirar dessa regra o dia Compensado** conforme parâmetro abaixo:  
  
Acessar o RM / Folha de Pagamento / Configurações / Parametrizador / RM Portal /  Edite o quiosque vinculado ao funcionário / Férias e marque o parâmetro **Desconsiderar dia Compensado** e avança até salvar, conforme print:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418016579223)  
  
**Importante**-A **principal causa** de erros registrados no Suporte está relacionada à configuração da **Jornada e dos Índices** do funcionário, o que faz com que os dias de descanso ou compensados **caiam em dias da semana inadequados**, resultando no erro em questão. Para verificar se essa é a causa, elaboramos uma **documentação** para que o RH possa realizar a **conferência da Jornada** do funcionário. Pedimos que, por favor, valide essa documentação.  
[Conferir a Jornada do funcionário para solicitação de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7491846215447-RH-RM-Meu-RH-Como-visualizar-o-hor%C3%A1rio-para-solicita%C3%A7%C3%A3o-f%C3%A9rias-ocorrer-corretamente)  
  
-Os Feriados serão avaliados através dos calendários vinculados nas seções dos funcionários.  
-Caso queira que o Meu RH não apresente a mensagem de erro em questão, basta desmarcar o parâmetro **"Impedir início de férias em feriados, dias de descanso ou até 2 dias antes destes"  
  
Saiba mais**[Desconsiderar dia compensado](https://tdn.totvs.com/pages/releaseview.action?pageId=638719251)
